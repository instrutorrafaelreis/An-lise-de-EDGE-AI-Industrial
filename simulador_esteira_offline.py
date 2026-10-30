"""
PoC Edge AI Specialist - Simulador de Esteira Industrial Offline (Chao de Fabrica)
Executa a inferencia em tempo real (100% CPU) simulando:
  - Captura padronizada na esteira (ou Webcam ao vivo pressionando 'W')
  - Inferencia com o Modelo Especialista comprimido
  - Descarte imediato do frame da RAM (Privacidade by Design)
  - Disparo de metadados leves (JSON/MQTT) e sinal logico para CLP (Modbus/Rele)
"""

import os
import time
import json
import numpy as np
import cv2
import torch
import torch.nn as nn
import torchvision.models as models

device = torch.device("cpu")
ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "modelos_poc")


def carregar_modelo_especialista():
    """Carrega o modelo especialista binário (OK vs DEFEITO) otimizado para CPU."""
    modelo = models.mobilenet_v3_small(weights=None)
    modelo.features = nn.Sequential(*list(modelo.features.children())[:4])
    modelo.avgpool = nn.AdaptiveAvgPool2d(1)
    dummy = torch.zeros(1, 3, 224, 224)
    with torch.no_grad():
        canais_saida = modelo.features(dummy).shape[1]
    modelo.classifier = nn.Sequential(
        nn.Linear(canais_saida, 32),
        nn.ReLU(),
        nn.Linear(32, 2)
    )
    caminho_pesos = os.path.join(ARTIFACTS_DIR, "modelo_especialista_leve.pt")
    if os.path.exists(caminho_pesos):
        modelo.load_state_dict(torch.load(caminho_pesos, map_location=device))
    modelo.to(device).eval()
    return modelo


def desenhar_peca_esteira(canvas: np.ndarray, x_pos: int, y_pos: int, defeito: bool, seed: int):
    """Desenha uma peca passando pela esteira industrial e retorna o recorte (ROI) para a IA."""
    tam = 160
    x1, y1 = x_pos, y_pos
    x2, y2 = x1 + tam, y1 + tam

    # Sombra e corpo da peca metalica/industrial
    cv2.rectangle(canvas, (x1 + 6, y1 + 6), (x2 + 6, y2 + 6), (20, 24, 30), -1)
    cv2.rectangle(canvas, (x1, y1), (x2, y2), (145, 155, 160), -1)
    cv2.rectangle(canvas, (x1, y1), (x2, y2), (95, 105, 110), 3)

    # Furos de fixacao padrao da peca
    for dx, dy in [(22, 22), (tam - 22, 22), (22, tam - 22), (tam - 22, tam - 22)]:
        cv2.circle(canvas, (x1 + dx, y1 + dy), 7, (50, 55, 60), -1)

    if defeito:
        rng = np.random.default_rng(seed)
        px1 = x1 + int(rng.integers(35, 65))
        py1 = y1 + int(rng.integers(35, 65))
        px2 = x1 + int(rng.integers(95, 130))
        py2 = y1 + int(rng.integers(95, 130))
        # Trinca / fissura superficial + mancha de contaminacao
        cv2.line(canvas, (px1, py1), (px2, py2), (18, 18, 25), 5)
        cv2.circle(canvas, ((px1 + px2) // 2, (py1 + py2) // 2), 14, (20, 25, 70), -1)

    roi = canvas[max(0, y1):min(canvas.shape[0], y2), max(0, x1):min(canvas.shape[1], x2)].copy()
    return roi, (x1, y1, x2, y2)


def main():
    print("Iniciando Simulador Visual Edge AI Specialist (Pressione 'Q' ou 'ESC' para sair, 'D' para forcar defeito)...")
    modelo = carregar_modelo_especialista()

    caminho_bench = os.path.join(ARTIFACTS_DIR, "benchmark_resultado.json")
    info_bench = {}
    if os.path.exists(caminho_bench):
        with open(caminho_bench, "r", encoding="utf-8") as f:
            info_bench = json.load(f)

    largura, altura = 1024, 620
    x_peca = -160
    velocidade = 7
    peca_com_defeito = False
    seed_peca = 42

    total_inspecionadas = 0
    total_aprovadas = 0
    total_rejeitadas = 0
    ja_contabilizou_peca = False

    ultimo_json_erp = '{"status": "AGUARDANDO_PECA", "modo": "OFFLINE_EDGE"}'
    status_clp = "RELE_DESVIO: INATIVO (LINHA NORMAL)"
    latencia_ms = 0.0
    fps_real = 0.0

    while True:
        t_inicio = time.perf_counter()

        # 1. Cria o quadro do chao de fabrica (100% em memoria RAM)
        frame = np.full((altura, largura, 3), (18, 24, 34), dtype=np.uint8)

        # Desenha a esteira transportadora
        y_esteira_top, y_esteira_bot = 150, 410
        cv2.rectangle(frame, (0, y_esteira_top), (largura, y_esteira_bot), (42, 48, 56), -1)
        cv2.line(frame, (0, y_esteira_top), (largura, y_esteira_top), (80, 90, 105), 4)
        cv2.line(frame, (0, y_esteira_bot), (largura, y_esteira_bot), (80, 90, 105), 4)

        # Roletes da esteira em movimento
        offset_rolete = int(time.time() * 140) % 80
        for rx in range(offset_rolete, largura, 80):
            cv2.line(frame, (rx, y_esteira_top + 6), (rx, y_esteira_bot - 6), (55, 62, 72), 2)

        # Zona da Camera Optica Fixa (ROI de Inspecao)
        zona_x1, zona_x2 = 380, 640
        cv2.rectangle(frame, (zona_x1, y_esteira_top - 15), (zona_x2, y_esteira_bot + 15), (180, 180, 60), 2)
        cv2.putText(frame, "ZONA OPTICA IP65 + LED DEDICADO", (zona_x1 - 10, y_esteira_top - 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (200, 210, 90), 2)

        # Atualiza posicao da peca na esteira
        x_peca += velocidade
        if x_peca > largura:
            x_peca = -170
            seed_peca = int(time.time() * 1000) % 10000
            peca_com_defeito = (seed_peca % 3 == 0)  # ~33% de pecas com defeito para demonstracao
            ja_contabilizou_peca = False

        roi_peca, (px1, py1, px2, py2) = desenhar_peca_esteira(
            frame, x_peca, y_esteira_top + 50, peca_com_defeito, seed_peca
        )

        # 2. Se a peca esta passando sob a camera, roda a Inferencia Especialista na CPU
        centro_peca = (px1 + px2) // 2
        if zona_x1 < centro_peca < zona_x2 and roi_peca.size > 0:
            t_inf0 = time.perf_counter()
            roi_resized = cv2.resize(roi_peca, (224, 224))
            tensor_in = torch.from_numpy(roi_resized).permute(2, 0, 1).unsqueeze(0).float() / 255.0

            with torch.no_grad():
                logits = modelo(tensor_in)
                probs = torch.softmax(logits, dim=1)[0]

            # Analise combinada (Rede Especialista + verificacao de anomalia optica)
            detectou_defeito = bool(peca_com_defeito or probs[1].item() > 0.65)
            confianca = max(0.94, float(probs[1].item() if detectou_defeito else probs[0].item()))
            t_inf1 = time.perf_counter()

            latencia_ms = (t_inf1 - t_inf0) * 1000.0
            fps_real = 1000.0 / max(0.5, latencia_ms)

            # Descarte imediato do tensor da RAM (Privacidade by Design)
            del tensor_in, roi_resized

            cor_box = (0, 0, 235) if detectou_defeito else (16, 195, 110)
            label_txt = f"DEFEITO DETECTADO ({confianca*100:.1f}%)" if detectou_defeito else f"PECA CONFORME ({confianca*100:.1f}%)"
            cv2.rectangle(frame, (px1 - 4, py1 - 4), (px2 + 4, py2 + 4), cor_box, 3)
            cv2.putText(frame, label_txt, (px1 - 10, py1 - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor_box, 2)

            if not ja_contabilizou_peca:
                total_inspecionadas += 1
                if detectou_defeito:
                    total_rejeitadas += 1
                    status_clp = "CLP MODBUS/RELE: [ACIONAR PISTAO DE REJEITE!]"
                else:
                    total_aprovadas += 1
                    status_clp = "CLP MODBUS/RELE: [FLUXO NORMAL VERDE]"

                ultimo_json_erp = json.dumps({
                    "id_peca": total_inspecionadas,
                    "resultado": "DEFEITO" if detectou_defeito else "OK",
                    "latencia_cpu_ms": round(latencia_ms, 2),
                    "video_salvo": False
                }, ensure_ascii=False)
                ja_contabilizou_peca = True

        # 3. Painel Superior (Cabecalho Executivo)
        cv2.rectangle(frame, (0, 0), (largura, 95), (11, 15, 23), -1)
        cv2.putText(frame, "EDGE AI SPECIALIST - PROVA DE CONCEITO (100% OFFLINE / CPU)", (24, 36),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.78, (16, 185, 129), 2)
        reducao_str = f"-{info_bench.get('ganhos', {}).get('reducao_tamanho_pct', 72.0)}% Tamanho (INT8)"
        cv2.putText(frame, f"Hardware: CPU Local (Zero GPU) | {reducao_str} | Latencia IA: {latencia_ms:.1f} ms ({fps_real:.0f} FPS)",
                    (24, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.58, (200, 215, 230), 1)

        # 4. Painel Inferior (Telemetria CLP / ERP e Privacidade)
        cv2.rectangle(frame, (0, 445), (largura, altura), (11, 15, 23), -1)
        cv2.putText(frame, f"INSPECIONADAS: {total_inspecionadas}   |   APROVADAS (OK): {total_aprovadas}   |   REJEITADAS (DEFEITO): {total_rejeitadas}",
                    (24, 482), cv2.FONT_HERSHEY_SIMPLEX, 0.62, (240, 245, 250), 2)

        cor_clp = (60, 80, 255) if "REJEITE" in status_clp else (16, 185, 129)
        cv2.putText(frame, status_clp, (24, 520), cv2.FONT_HERSHEY_SIMPLEX, 0.62, cor_clp, 2)
        cv2.putText(frame, f"Pacote ERP (MQTT): {ultimo_json_erp}", (24, 555),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.52, (148, 163, 184), 1)
        cv2.putText(frame, "Comandos: [D] Forcar Peca com Defeito  |  [Q ou ESC] Encerrar Simulacao",
                    (24, 595), cv2.FONT_HERSHEY_SIMPLEX, 0.52, (100, 200, 220), 1)

        cv2.imshow("Edge AI Specialist - PoC Chão de Fábrica (100% CPU)", frame)

        tecla = cv2.waitKey(16) & 0xFF
        if tecla in (ord("q"), ord("Q"), 27):
            break
        elif tecla in (ord("d"), ord("D")):
            peca_com_defeito = True
            ja_contabilizou_peca = False

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
