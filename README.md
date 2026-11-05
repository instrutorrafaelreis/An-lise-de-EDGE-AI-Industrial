# Edge AI Specialist: Inspeção Industrial e Sanitária (Frigorífico SIF/MAPA) de Ultrabaixo Custo

Repositório oficial do projeto **Edge AI Specialist** — arquitetura de Visão Computacional Industrial **100% Offline** baseada em **Engenharia de Especialização, Destilação de Conhecimento, Poda Neural (*Pruning*) e Quantização Matemática (`FP32 -> INT8`)** do modelo oficial **[nvidia/nemotron-ocr-v2](https://build.nvidia.com/nvidia/nemotron-ocr-v2)** (`RegNetX-8GF`) para execução em uma **TV Box Smart Pro Android 4K (ARM Cortex-A53 — R$ 100)** ou CPUs legadas, sem necessidade de GPU dedicada.

🌐 **Portal Oficial Interativo (GitHub Pages):**  
👉 **[https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/](https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/)**

📺 **Aplicativo Ao Vivo da Bancada (TV Box 4K + Webcam USB + Moldes Imprimíveis):**  
👉 **[https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/app_tvbox_feira.html](https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/app_tvbox_feira.html)**

---

## 📊 Resultados Reais da Otimização (`NVIDIA Build -> TV Box Edge AI`)

| Métrica | Modelo Base Original (`nvidia/nemotron-ocr-v2` — `RegNetX-8GF FP32`) | **Nosso Especialista (`RegNetX-Edge-SIF INT8` — 3 Classes)** | Ganho Real / Referência |
| :--- | :--- | :--- | :--- |
| **Parâmetros da Rede** | 56.916.232 (~56,9 Milhões) | **9.731 parâmetros** | **-99,983% parâmetros** *(Han et al., Stanford ICLR 2016)* `[6]` |
| **Tamanho em Disco** | 217,12 MB (`FP32`) | **11,9 KB (`0,0116 MB` em `INT8`)** | **-99,995% menor** *(Jacob et al., Google CVPR 2018)* `[7]` |
| **Latência por Quadro (CPU)** | 116,77 ms/quadro | **1,19 ms/quadro** | **98,2x mais rápido na mesma CPU (Zero GPU)** |
| **Taxa de Quadros (FPS)** | 8,6 FPS *(engasga sem GPU)* | **840,7 FPS** | **Tempo Real Folgado em CPU Modesta** |
| **Acurácia nas 3 Classes SIF** | Modelo generalista pesado | **100,0%** (`Conforme`, `Contaminação`, `Sem SIF`) | **Precisão total no gargalo industrial** |
| **Custo de Hardware / Linha** | R$ 35.000 a R$ 60.000 *(Servidor GPU H100/A100)* | **R$ 155,00 Total** *(TV Box R$ 100 + Pórtico PVC R$ 55)* | **Economia de 99,6% em CAPEX** `[3, 13, 14]` |

---

## 📂 Guias para a Feira, Manuais de Montagem e Roteiro de Alunos (`.md` e `.docx`)

| Documento (Markdown) | Download Direto Word (`.docx`) | Descrição |
| :--- | :--- | :--- |
| **[`GUIA_EXPLICATIVO_LEIGO_FEIRA.md`](./GUIA_EXPLICATIVO_LEIGO_FEIRA.md)** | **[📥 Baixar `.docx`](./GUIA_EXPLICATIVO_LEIGO_FEIRA.docx)** | Explicação completa do projeto em linguagem simples para leigos, visitantes e roteiro de fala de 30 segundos na feira. |
| **[`MANUAL_INFRAESTRUTURA_E_MONTAGEM.md`](./MANUAL_INFRAESTRUTURA_E_MONTAGEM.md)** | **[📥 Baixar `.docx`](./MANUAL_INFRAESTRUTURA_E_MONTAGEM.docx)** | Lista de compras detalhada (cortes exatos do cano de PVC de 25mm, EVA, 3 bandejas de isopor, TV Box, Webcam/LED) e montagem em 20 min. |
| **[`ROTEIRO_PROMPTS_ALUNOS.md`](./ROTEIRO_PROMPTS_ALUNOS.md)** | **[📥 Baixar `.docx`](./ROTEIRO_PROMPTS_ALUNOS.docx)** | Guia de 5 Missões com **Prompts prontos (Copiar e Colar)** e divisão de equipes para os alunos finalizarem o projeto até o Dia 10. |
| **[`CRONOGRAMA_FEIRA_DIA_10.md`](./CRONOGRAMA_FEIRA_DIA_10.md)** | — | Cronograma dia a dia (Dias 01 a 10) de preparação para a Feira de Inovação. |
| **[`PROPOSTA_EDGE_AI.md`](./PROPOSTA_EDGE_AI.md)** | — | Proposta Técnica e Executiva completa com os 4 Pilares de Engenharia, Matriz de Hardware (Tiers) e Referências. |
| **[`PITCH_COMERCIAL_EDGE_AI.md`](./PITCH_COMERCIAL_EDGE_AI.md)** | — | Roteiro de Pitch Comercial de 9 slides e perguntas de fechamento. |

---

## 💻 Códigos-Fonte, Aplicativos e Modelos Treinados

| Arquivo | Descrição |
| :--- | :--- |
| **[`index.html`](./index.html)** | Portal Unificado (Apresentação Executiva de 9 Slides + Cronograma Interativo + Planta Visual da Bancada + Etiquetas de Preço Imprimíveis). |
| **[`app_tvbox_feira.html`](./app_tvbox_feira.html)** | WebApp 100% Offline para rodar na **TV Box Smart Pro 4K** com Webcam USB ao vivo, Simulador de Esteira SIF e os **3 Moldes de Bandejas de Carne para Imprimir**. |
| **[`treinar_modelo_frigorifico.py`](./treinar_modelo_frigorifico.py)** | Pipeline PyTorch que baixa a arquitetura `RegNetX-8GF` (`nvidia/nemotron-ocr-v2`), aplica Destilação + Poda L1 (30%) + Quantização `INT8` e gera o modelo de `11,9 KB`. |
| **[`bancada_feira_ao_vivo.py`](./bancada_feira_ao_vivo.py)** | Central Desktop em Python + OpenCV + PyTorch para inspeção ao vivo na Webcam e recalibração instantânea na feira (teclas `[1]`, `[2]`, `[3]`, `[T]`). |
| **[`modelos_poc/modelo_frigorifico_int8.pt`](./modelos_poc/modelo_frigorifico_int8.pt)** | Pesos finais quantizados em `INT8` (`11,9 KB`) do especialista de Frigorífico SIF. |
| **[`modelos_poc/benchmark_frigorifico.json`](./modelos_poc/benchmark_frigorifico.json)** | Relatório JSON auditável do comparativo `nvidia/nemotron-ocr-v2` vs. `RegNetX-Edge-SIF INT8`. |

---

## 🚀 Como Executar Localmente no Computador

```powershell
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Executar o pipeline de otimizacao do modelo NVIDIA RegNetX-8GF -> INT8 (11,9 KB)
python treinar_modelo_frigorifico.py

# 3. Iniciar a central de inspecao ao vivo com Webcam para a Feira de Inovacao
python bancada_feira_ao_vivo.py
```

---

## 📚 Referências Científicas e Fontes de Mercado

1. **RAND Corporation (2024).** Ryseff, J., De Bruhl, B., & Newberry, S. *The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed.* RAND Corporation Research Report RR-A2680-1. *(Documenta que mais de 80% dos projetos de IA falham).*
2. **Gartner (2022–2024).** *Gartner AI in Production Surveys.* *(Entre 53% e 85% dos protótipos de IA não avançam para a produção industrial).*
3. **CNI — Confederação Nacional da Indústria (2022/2023).** *Sondagem Especial: Indústria 4.0 no Brasil.* *(66% das indústrias brasileiras apontam o alto custo de implantação como principal barreira).*
4. **ConectarAGRO & ESALQ/USP (2023/2024).** *Indicador de Conectividade Rural no Brasil.* *(Déficit de conectividade móvel no interior produtivo brasileiro).*
5. **Howard, A. et al. (2019).** *Searching for MobileNetV3.* IEEE/CVF International Conference on Computer Vision (ICCV), Google Research.
6. **Han, S., Mao, H., & Dally, W. J. (2016).** *Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding.* ICLR 2016 (Stanford University).
7. **Jacob, B. et al. (2018).** *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference.* IEEE/CVF CVPR 2018 (Google Research).
8. **Hinton, G., Vinyals, O., & Dean, J. (2015).** *Distilling the Knowledge in a Neural Network.* NIPS Deep Learning Workshop (arXiv:1503.02531).
9. **Nagel, M. et al. (2021).** *A White Paper on Neural Network Quantization.* Qualcomm AI Research (arXiv:2106.08295).
10. **Edge Impulse Research (2022).** *FOMO: Faster Objects, More Objects — Constrained Object Detection on Microcontrollers.*
11. **Intel Corporation (2024).** *Intel Distribution of OpenVINO Toolkit Benchmark Results.*
12. **ABNT NBR IEC 60529 & IEC 62443.** *Graus de proteção providos por invólucros (Códigos IP65/IP67)* e *Segurança cibernética em sistemas de automação e controle industrial (OT/IT)*.
13. **Hardware Referência Tier 2 (TV Box Smart Pro Android 4K — ARM64).** SoC Quad-Core ARM Cortex-A53 64-bit, 2GB RAM DDR3, 16GB eMMC Flash, 4x USB 2.0 Host, HDMI ([Referência de Mercado Livre Brasil](https://www.mercadolivre.com.br/tv-box-smart-pro-android-4k-wifi-transforme-sua-tv-em-smart/up/MLBU5230875966)).
14. **NVIDIA Build / NIM Model Catalog (2026).** Modelo Oficial **[nvidia/nemotron-ocr-v2](https://build.nvidia.com/nvidia/nemotron-ocr-v2)** (*Backbone Convolucional RegNetX-8GF*, Radosavovic et al., *Designing Network Design Spaces*, CVPR 2020).
