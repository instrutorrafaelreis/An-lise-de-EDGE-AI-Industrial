# Edge AI Specialist: Inspeção Industrial e Sanitária (Frigorífico SIF/MAPA) de Ultrabaixo Custo

Repositório oficial do projeto **Edge AI Specialist** — arquitetura de Visão Computacional Industrial **100% Offline** baseada em **Engenharia de Especialização, Destilação de Conhecimento, Fusão Algébrica de Operadores (`Conv2d + BatchNorm2d Folding`), Poda Neural L1 (*35% Sparsity*) e Quantização Consciente Por Canal (`Per-Channel QAT INT8`)** do modelo oficial **[nvidia/nemotron-ocr-v2](https://build.nvidia.com/nvidia/nemotron-ocr-v2)** (`RegNetX-8GF`) para execução em uma **TV Box Smart Pro Android 4K (ARM Cortex-A53 — R$ 100)** ou Notebooks/PCs legados (`R$ 0`), sem necessidade de GPU dedicada.

🌐 **Portal Oficial Interativo (GitHub Pages):**  
👉 **[https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/](https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/)**

📺 **Aplicativo Ao Vivo da TV Box (Controle Remoto + Webcam USB + Sirene Industrial):**  
👉 **[https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/PENDRIVE_TVBOX_PRONTO/ABRIR_NA_TVBOX.html](https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/PENDRIVE_TVBOX_PRONTO/ABRIR_NA_TVBOX.html)**

📦 **Pacote Pronto para Pendrive da TV Box (`.zip`):**  
👉 **[https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/PENDRIVE_TVBOX_PRONTO.zip](https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/PENDRIVE_TVBOX_PRONTO.zip)**

---

## 📊 Resultados Reais Auditados (`NVIDIA Build RegNetX-8GF -> Nosso Fused INT8`)

| Métrica Auditada | Modelo Base Original (`nvidia/nemotron-ocr-v2` — `RegNetX-8GF FP32`) | **Nosso Especialista (`RegNetX-Edge-SIF Fused INT8` — 3 Classes)** | Ganho Real / Referência |
| :--- | :--- | :--- | :--- |
| **Parâmetros da Rede** | `56.916.232` (~56,9 Milhões) | **`9.571` parâmetros** *(+ 5 BatchNorms fundidas)* | **`-99,983%` parâmetros** *(Han et al., Stanford ICLR 2016)* `[6]` |
| **Tamanho em Disco** | `217,12 MB` (`FP32`) | **`11,2 KB` (`0,011 MB` em `INT8`)** | **`-99,995%` menor** *(Jacob et al., Google CVPR 2018)* `[7]` |
| **Operações por Foto (`FLOPs`)** | `16,02 GFLOPs` (`16.024.936.832` contas) | **`89,11 MFLOPs` (`89.111.120` contas)** | **`-99,44%` menos cálculos matemáticos** |
| **Velocidade no Emulador TV Box (`1 Núcleo Core 0`)** | `228,72 ms/quadro` (`4,4 FPS` — trava a linha) | **`2,55 ms/quadro` (`392,0 FPS`)** | **`89,8x mais rápido` em 1 único núcleo físico** |
| **Velocidade no Notebook (`8 Núcleos CPU`)** | `154,03 ms/quadro` (`6,5 FPS`) | **`1,35 ms/quadro` (`740,7 FPS`)** | **`114,3x mais rápido` na mesma CPU (Zero GPU)** |
| **Acurácia / `F1-Score` Macro (3 Classes SIF)** | — | **`100,0%` (`F1 = 100,0%`)** | Matriz de Confusão 3x3: `[[46,0,0],[0,51,0],[0,0,38]]` |
| **Custo de Hardware / Linha** | R$ 35.000 a R$ 60.000 *(Servidor GPU H100/A100)* | **R$ 55 a R$ 155 Total** *(Notebook R$ 0 ou TV Box R$ 100 + PVC R$ 55)* | **Economia de até 99,8% em CAPEX** `[3, 13, 14]` |

---

## 📂 Documentação de Regras de Negócio, Manuais e Guias (`.md` e `.docx`)

| Documento (Markdown) | Download Direto Word (`.docx`) | Descrição |
| :--- | :--- | :--- |
| **[`REGRAS_DE_NEGOCIO_E_MEMORIAL_COMPLETO.md`](./REGRAS_DE_NEGOCIO_E_MEMORIAL_COMPLETO.md)** | **[📥 Baixar `.docx`](./REGRAS_DE_NEGOCIO_E_MEMORIAL_COMPLETO.docx)** | **Documento Mestre:** Regras de Negócio (`RN-01` a `RN-08` SIF/MAPA), Engenharia de Otimização em 5 Estágios e Memorial Completo de tudo o que foi feito. |
| **[`GUIA_EXPLICATIVO_LEIGO_FEIRA.md`](./GUIA_EXPLICATIVO_LEIGO_FEIRA.md)** | **[📥 Baixar `.docx`](./GUIA_EXPLICATIVO_LEIGO_FEIRA.docx)** | Explicação completa do projeto em linguagem simples para leigos, visitantes e roteiro de fala de 30 segundos na feira. |
| **[`MANUAL_INFRAESTRUTURA_E_MONTAGEM.md`](./MANUAL_INFRAESTRUTURA_E_MONTAGEM.md)** | **[📥 Baixar `.docx`](./MANUAL_INFRAESTRUTURA_E_MONTAGEM.docx)** | Lista de compras detalhada (cortes exatos do cano de PVC de 25mm, EVA, 3 bandejas de isopor, TV Box, Webcam/LED) e montagem em 20 min. |
| **[`ROTEIRO_PROMPTS_ALUNOS.md`](./ROTEIRO_PROMPTS_ALUNOS.md)** | **[📥 Baixar `.docx`](./ROTEIRO_PROMPTS_ALUNOS.docx)** | Guia de 5 Missões com **Prompts prontos (Copiar e Colar)** e divisão de equipes para os alunos. |
| **[`PROPOSTA_EDGE_AI.md`](./PROPOSTA_EDGE_AI.md)** | — | Proposta Técnica e Executiva com os 4 Pilares de Engenharia, Matriz de Hardware (Tiers) e Referências. |
| **[`PITCH_COMERCIAL_EDGE_AI.md`](./PITCH_COMERCIAL_EDGE_AI.md)** | — | Roteiro de Pitch Comercial de 9 slides e perguntas de fechamento. |

---

## 💻 Sistemas Executáveis, Emulador de Hardware TV Box e Modelos Treinados

| Arquivo | Descrição |
| :--- | :--- |
| **[`simular_ambiente_tvbox.py`](./simular_ambiente_tvbox.py)** | **Estação SCADA + Explainable AI (Grad-CAM) com Emulador de Hardware TV Box:** Trava o processo do Windows em **1 único núcleo físico (`Core 0` / Máscara `0x01`)**, monitora o teto de 2GB RAM da TV Box, projeta Mapa de Calor Neural (`[G]`), Osciloscópio de Latência e exporta Laudo CSV do SIF (`[R]`). |
| **[`RODAR_SIMULADOR_TVBOX_NO_NOTEBOOK.bat`](./RODAR_SIMULADOR_TVBOX_NO_NOTEBOOK.bat)** | Atalho de 1 clique no Windows para iniciar a Estação SCADA + Emulador de Hardware da TV Box no Notebook. |
| **[`treinar_modelo_frigorifico.py`](./treinar_modelo_frigorifico.py)** | Pipeline PyTorch de 5 estágios (Destilação + Fusão `Conv+BN` + Poda L1 35% + `QAT INT8` Por Canal + `torch.jit.freeze`). |
| **[`PENDRIVE_TVBOX_PRONTO/`](./PENDRIVE_TVBOX_PRONTO/)** | Pasta completa pronta para copiar para um Pendrive USB e espetar diretamente na **TV Box Smart Pro 4K** ou Notebook Antigo. |
| **[`modelos_poc/modelo_frigorifico_jit_otimizado.pt`](./modelos_poc/modelo_frigorifico_jit_otimizado.pt)** | Grafo TorchScript congelado com operadores `Conv2d + BatchNorm2d` fundidos e pesos quantizados. |
| **[`modelos_poc/modelo_frigorifico_int8.pt`](./modelos_poc/modelo_frigorifico_int8.pt)** | Pesos finais quantizados por canal em `INT8` (`11,2 KB`). |
| **[`modelos_poc/benchmark_frigorifico.json`](./modelos_poc/benchmark_frigorifico.json)** | Relatório JSON auditável completo (Parâmetros, MB/KB, FLOPs, Latência 1-Core vs Multi-Core, F1-Score e Matriz de Confusão 3x3). |

---

## 🚀 Como Executar no Computador (Simulando o Hardware da TV Box)

```powershell
# 1. Rodar a Estacao SCADA + Explainable AI (Grad-CAM) travada em 1 Nucleo Fisico (Simulador TV Box 4K)
python simular_ambiente_tvbox.py

# 2. (Opcional) Re-executar o pipeline de 5 estagios de otimizacao e auditoria matematica
python treinar_modelo_frigorifico.py
```

---

## 📚 Referências Científicas e Fontes de Mercado

1. **RAND Corporation (2024).** Ryseff, J., De Bruhl, B., & Newberry, S. *The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed.* RAND Corporation Research Report RR-A2680-1.
2. **Gartner (2022–2024).** *Gartner AI in Production Surveys.*
3. **CNI — Confederação Nacional da Indústria (2022/2023).** *Sondagem Especial: Indústria 4.0 no Brasil.*
4. **ConectarAGRO & ESALQ/USP (2023/2024).** *Indicador de Conectividade Rural no Brasil.*
5. **Howard, A. et al. (2019).** *Searching for MobileNetV3.* IEEE/CVF ICCV, Google Research.
6. **Han, S., Mao, H., & Dally, W. J. (2016).** *Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding.* ICLR 2016 (Stanford University).
7. **Jacob, B. et al. (2018).** *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference.* IEEE/CVF CVPR 2018 (Google Research).
8. **Hinton, G., Vinyals, O., & Dean, J. (2015).** *Distilling the Knowledge in a Neural Network.* NIPS Deep Learning Workshop (arXiv:1503.02531).
9. **Nagel, M. et al. (2021).** *A White Paper on Neural Network Quantization.* Qualcomm AI Research (arXiv:2106.08295).
10. **Edge Impulse Research (2022).** *FOMO: Faster Objects, More Objects — Constrained Object Detection on Microcontrollers.*
11. **Intel Corporation (2024).** *Intel Distribution of OpenVINO Toolkit Benchmark Results.*
12. **ABNT NBR IEC 60529 & IEC 62443.** *Graus de proteção providos por invólucros (Códigos IP65/IP67)* e *Segurança cibernética em sistemas de automação e controle industrial (OT/IT)*.
13. **Hardware Referência Tier 2 (TV Box Smart Pro Android 4K — ARM64).** SoC Quad-Core ARM Cortex-A53 64-bit, 2GB RAM DDR3, 16GB eMMC Flash, 4x USB 2.0 Host, HDMI ([Referência Mercado Livre](https://www.mercadolivre.com.br/tv-box-smart-pro-android-4k-wifi-transforme-sua-tv-em-smart/up/MLBU5230875966)).
14. **NVIDIA Build / NIM Model Catalog (2026).** Modelo Oficial **[nvidia/nemotron-ocr-v2](https://build.nvidia.com/nvidia/nemotron-ocr-v2)** (*Backbone Convolucional RegNetX-8GF*, Radosavovic et al., *Designing Network Design Spaces*, CVPR 2020).
