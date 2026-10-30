# PoC (Prova de Conceito) — Edge AI Specialist

Esta Prova de Conceito valida na prática os **3 Pilares da Engenharia de Especialização** operando **100% em CPU local e Offline**, com respaldo em literatura científica revisada por pares `[5, 6, 7, 8, 9]`.

---

## 📊 Resultados Medidos na PoC Local (`benchmark_resultado.json`)

| Métrica | Modelo Generalista (`FP32` - 1.000 classes) | **Especialista Edge (`INT8` - 2 classes)** | Ganho Real / Referência |
| :--- | :--- | :--- | :--- |
| **Parâmetros da Rede** | 2.542.856 | **11.354** | **-99,6% parâmetros** *(Han et al., Stanford ICLR 2016)* `[6]` |
| **Tamanho do Arquivo** | 9,83 MB | **0,02 MB (~20 KB)** | **-99,8% menor** *(Jacob et al., Google CVPR 2018)* `[7]` |
| **Latência por Quadro (CPU)** | 22,16 ms | **3,15 ms** | **7,04x mais rápido na mesma CPU** |
| **Taxa de Quadros (FPS)** | 45,1 FPS | **317,7 FPS** | **Tempo Real Folgado sem GPU** |
| **Acurácia pós-compressão** | — | **100,0%** | **Zero perda no gargalo industrial** |

---

## 📂 Estrutura dos Arquivos da PoC

1. **[`pipeline_especializacao_int8.py`](file:///c:/Users/rafael.filipe/Documents/EDIGE_AI/pipeline_especializacao_int8.py)**
   * **Pilar 1 (Curadoria Open Source):** Carrega uma arquitetura `MobileNetV3` generalista (1.000 classes, `FP32`) `[5]`.
   * **Pilar 2 (Especialização Cirúrgica):** Remove blocos profundos desnecessários e substitui o classificador pesado de 1.000 classes por uma cabeça enxuta binária (`PECA_OK` vs `PECA_DEFEITO`), treinando no gargalo industrial `[8]`.
   * **Pilar 3 (Poda Estrutural + Quantização INT8):** Aplica *Neural Pruning* (30%) `[6]` + conversão matemática para `INT8` `[7, 9]` e otimização de grafo para CPU (`TorchScript Freeze`).
   * **Resultado:** Salva os artefatos na pasta `modelos_poc/` e gera o relatório [`benchmark_resultado.json`](file:///c:/Users/rafael.filipe/Documents/EDIGE_AI/modelos_poc/benchmark_resultado.json).

2. **[`simulador_esteira_offline.py`](file:///c:/Users/rafael.filipe/Documents/EDIGE_AI/simulador_esteira_offline.py)**
   * Simulador visual interativo de chão de fábrica em tempo real (OpenCV + PyTorch CPU).
   * Simula peças passando em uma esteira sob uma **Zona Óptica IP65 + LED Dedicado** (norma **ABNT NBR IEC 60529** `[12]`).
   * Executa a inferência em milissegundos na CPU, **descarta a imagem bruta da memória RAM imediatamente** (Privacidade Industrial — **IEC 62443**) e exibe o acionamento lógico do **CLP (Modbus/Relé)** e o pacote JSON enviado ao **ERP (MQTT)**.

---

## 🚀 Como Executar

### 1. Rodar a Esteira de Compressão e Benchmark na CPU
```powershell
python pipeline_especializacao_int8.py
```

### 2. Abrir o Simulador Visual de Esteira Industrial (Ao Vivo)
```powershell
python simulador_esteira_offline.py
```
* **Tecla `D`:** Força a próxima peça na esteira a vir com trinca/contaminação para demonstrar o disparo do relé do CLP ao vivo.
* **Tecla `Q` ou `ESC`:** Fecha o simulador.

---

## 📚 Referências Científicas e de Mercado

1. **RAND Corporation (2024).** Ryseff, J., De Bruhl, B., & Newberry, S. *The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed.* RAND Corporation Research Report RR-A2680-1. *(Mais de 80% dos projetos de IA falham).*
2. **Gartner (2022–2024).** *Gartner AI in Production Surveys.* *(Entre 53% e 85% dos protótipos de IA não avançam para a produção industrial).*
3. **CNI — Confederação Nacional da Indústria (2022/2023).** *Sondagem Especial: Indústria 4.0 no Brasil.* *(66% das indústrias brasileiras apontam o alto custo de implantação como principal barreira).*
4. **ConectarAGRO & ESALQ/USP (2023/2024).** *Indicador de Conectividade Rural no Brasil.* *(Déficit de conectividade móvel no interior agroindustrial e florestal).*
5. **Howard, A. et al. (2019).** *Searching for MobileNetV3.* IEEE/CVF International Conference on Computer Vision (ICCV), Google Research.
6. **Han, S., Mao, H., & Dally, W. J. (2016).** *Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding.* ICLR 2016 (Stanford University).
7. **Jacob, B. et al. (2018).** *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference.* IEEE/CVF CVPR 2018 (Google Research).
8. **Hinton, G., Vinyals, O., & Dean, J. (2015).** *Distilling the Knowledge in a Neural Network.* NIPS Deep Learning Workshop (arXiv:1503.02531).
9. **Nagel, M. et al. (2021).** *A White Paper on Neural Network Quantization.* Qualcomm AI Research (arXiv:2106.08295).
10. **Edge Impulse Research (2022).** *FOMO: Faster Objects, More Objects — Constrained Object Detection on Microcontrollers.*
11. **Intel Corporation (2024).** *Intel Distribution of OpenVINO Toolkit Benchmark Results.*
12. **ABNT NBR IEC 60529 & IEC 62443.** *Graus de proteção providos por invólucros (Códigos IP65/IP67)* e *Segurança cibernética em sistemas de automação e controle industrial (OT/IT)*.
