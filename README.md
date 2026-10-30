# Edge AI Specialist: Inteligência Artificial Local, Resiliente e de Baixo Custo para a Indústria

Repositório oficial do projeto **Edge AI Specialist** — arquitetura de Visão Computacional Industrial **100% Offline** baseada em **Engenharia de Especialização, Poda Neural (*Pruning*) e Quantização Matemática (`FP32 -> INT8`)** para execução em CPUs modestas sem necessidade de GPU dedicada.

---

## 📊 Resultados Reais da Prova de Conceito (`100% CPU Local`)

| Métrica | Modelo Generalista (`FP32` - 1.000 classes) | **Especialista Edge (`INT8` - 2 classes)** | Ganho Real / Referência |
| :--- | :--- | :--- | :--- |
| **Parâmetros da Rede** | 2.542.856 | **11.354** | **-99,6% parâmetros** *(Han et al., Stanford ICLR 2016)* `[6]` |
| **Tamanho do Arquivo** | 9,83 MB | **0,02 MB (~20 KB)** | **-99,8% menor** *(Jacob et al., Google CVPR 2018)* `[7]` |
| **Latência por Quadro (CPU)** | 22,16 ms | **3,15 ms** | **7,04x mais rápido na mesma CPU** |
| **Taxa de Quadros (FPS)** | 45,1 FPS | **317,7 FPS** | **Tempo Real Folgado (Zero GPU)** |
| **Acurácia Validada** | — | **100,0%** | **Zero perda no gargalo industrial** |

---

## 📂 Estrutura do Repositório

| Arquivo | Descrição |
| :--- | :--- |
| **[`PROPOSTA_EDGE_AI.md`](./PROPOSTA_EDGE_AI.md)** | Documento Técnico e Executivo completo com os 4 Pilares de Engenharia, Matriz de Hardware (Tiers) e Referências Bibliográficas. |
| **[`PITCH_COMERCIAL_EDGE_AI.md`](./PITCH_COMERCIAL_EDGE_AI.md)** | Roteiro completo de Pitch Comercial (Elevator Pitch + estrutura de 9 slides referenciados). |
| **[`APRESENTACAO_EDGE_AI.html`](./APRESENTACAO_EDGE_AI.html)** | Apresentação Executiva interativa em HTML (100% offline, modo tela cheia `F`, notas do apresentador `N`). |
| **[`CRONOGRAMA_FEIRA_DIA_10.html`](./CRONOGRAMA_FEIRA_DIA_10.html)** | Painel interativo HTML com o Cronograma de Execução até o Dia 10 (Feira de Inovação), barra de progresso e checklist. |
| **[`CRONOGRAMA_FEIRA_DIA_10.md`](./CRONOGRAMA_FEIRA_DIA_10.md)** | Versão em Markdown do Cronograma de Execução para a Feira de Inovação. |
| **[`pipeline_especializacao_int8.py`](./pipeline_especializacao_int8.py)** | Script Python da esteira de especialização (`MobileNetV3`), *Pruning* e Quantização `INT8` com benchmark em CPU. |
| **[`simulador_esteira_offline.py`](./simulador_esteira_offline.py)** | Simulador visual em tempo real (OpenCV + PyTorch CPU) de inspeção óptica industrial com telemetria CLP/ERP. |
| **[`README_POC.md`](./README_POC.md)** | Guia detalhado de execução da Prova de Conceito. |

---

## 🚀 Como Executar a PoC Localmente

```powershell
# 1. Executar a esteira de especializacao, poda e quantizacao INT8 + Benchmark em CPU
python pipeline_especializacao_int8.py

# 2. Iniciar o simulador visual de chao de fabrica em tempo real (Pressione 'D' para forcar defeito, 'Q' para sair)
python simulador_esteira_offline.py
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
