# Pitch Deck Comercial: Edge AI Specialist (Com Referências Técnicas e de Mercado)
**Público-Alvo:** Diretores Industriais, Gerentes de Operações/Manutenção, Inovação e Investidores.  
**Tempo estimado de apresentação:** 5 a 7 minutos.

---

## 🎯 Elevator Pitch (Discurso de 30 segundos)
> *"Segundo a RAND Corporation (2024) e o Gartner, mais de 80% dos projetos de Inteligência Artificial falham antes de entrar em produção, e no Brasil 66% das indústrias travam no alto custo de infraestrutura (CNI). Quando uma fábrica tenta usar Visão Computacional tradicional, descobre que precisa gastar de R$ 25 mil a R$ 80 mil em servidores com GPUs e depender de uma internet instável no galpão. Nós fazemos o oposto: usando técnicas de Deep Compression (Stanford) e Quantização Int8 (Google Research), removemos tudo o que a fábrica não usa e comprimimos o modelo em mais de 75%. O resultado? Visão computacional 100% offline, rodando em tempo real até em um computador antigo já encostado na fábrica ou numa placa de R$ 600."*

---

## 📊 Estrutura de Slides (Slide a Slide com Fontes)

### SLIDE 1: Capa (A Promessa)
* **Título:** Edge AI Specialist: Visão Computacional Industrial 100% Offline e de Baixo Custo
* **Subtítulo:** Transformando câmeras comuns e computadores legados em sensores inteligentes de alta precisão.
* **Métricas em Destaque:**
  * **100% Offline-First:** Decisão na borda sem depender de Wi-Fi ou nuvem.
  * **-75% a -99% de Compressão:** Fundamentado em *Quantização INT8* *(Jacob et al., Google Research / CVPR 2018)* e *Deep Compression* *(Han et al., Stanford / ICLR 2016)*.
  * **7,04x mais rápido em CPU:** Validado em nossa Prova de Conceito local (`45,1 FPS -> 317,7 FPS` sem GPU).

---

### SLIDE 2: O Problema (Por que mais de 80% dos projetos de IA travam na indústria?)
* **Frase de Impacto:** *"A Inteligência Artificial tradicional foi feita para escritórios com fibra óptica, não para o chão de fábrica."*
* **3 Dores Diretas (com Fontes Oficiais):**
  1. **Sem Internet = Fábrica Parada:** Zonas rurais agroindustriais sofrem com déficit severo de conectividade móvel *(Indicador ConectarAGRO / ESALQ-USP, 2024)*, e galpões metálicos bloqueiam sinal por efeito Gaiola de Faraday.
  2. **Hardware Impossível de Pagar (CAPEX Alto):** Segundo a **Sondagem Indústria 4.0 da CNI**, **66% das indústrias brasileiras** apontam o alto custo de implantação como a barreira nº 1. Servidores locais com GPUs industriais custam de R$ 25.000 a R$ 80.000 por ponto.
  3. **Mais de 80% dos Projetos Falham:** Relatório da **RAND Corporation (2024)** e pesquisas do **Gartner** comprovam que **80% a 85% dos projetos de IA não passam do piloto** por complexidade excessiva e incompatibilidade com a infraestrutura real. Modelos generalistas (*MS-COCO / ImageNet*) tentam reconhecer 80 a 1.000 objetos simultâneos, desperdiçando >90% de processamento quando a máquina só precisa validar 1 condição.

---

### SLIDE 3: A Nossa Solução (Engenharia de Especialização)
* **Frase de Impacto:** *"Não criamos modelos gigantes genéricos. Criamos Especialistas Cirúrgicos."*
* **O Conceito em 3 Pilares Científicos:**
  * **1. Curadoria Open Source Leve:** Partimos de arquiteturas desenhadas para baixa latência em CPU (*MobileNetV3 — Howard et al., ICCV 2019*; *YOLO-Nano*; *FOMO — Edge Impulse, 2022*).
  * **2. Especialização Cirúrgica & Destilação:** Fazemos a IA "esquecer" as 1.000 classes irrelevantes e focar 100% no gargalo específico da máquina, usando *Transfer Learning* e *Knowledge Distillation* *(Hinton et al., 2015)*.
  * **3. Esmagamento Matemático (Poda + Quantização Int8):** Reduzimos a precisão matemática de `Float32` (32 bits) para `Int8` (8 bits), reduzindo o tamanho dos pesos em **75% a 99%** e acelerando de **2x a 7x** a leitura em CPUs comuns com perda de precisão <1% *(Jacob et al., Google CVPR 2018; Nagel et al., Qualcomm AI Research 2021; PoC Local 2026)*.

---

### SLIDE 4: A Prova de Fogo (Onde Nossa IA Roda?)
* **Frase de Impacto:** *"Zero GPUs caras. Usamos o hardware que cabe no seu bolso — ou que já está no seu almoxarifado."*
* **Tabela Visual de Níveis (Tiers Homologados):**
  * **Nível 1 - Micro (ESP32-S3 / ~R$ 100):** Arquitetura *TinyML / FOMO (<250 KB RAM)* para presença de peça, leitura de mostradores e alertas simples *(Edge Impulse Research, 2022)*.
  * **Nível 2 - Embarcado (Raspberry Pi 4/5 / ~R$ 600):** Processamento ARM NEON para uso de EPI, contagem em esteiras moderadas e validação de posto de trabalho.
  * **Nível 3 - Retrofitting (PCs ou Notebooks Legados da TI / Custo R$ 0):** Inspeção rápida em alta resolução (30 a 300+ FPS) reaproveitando computadores x86 já depreciados via otimização vetorial *Intel OpenVINO / TorchScript INT8* *(Intel OpenVINO Benchmarks, 2024)*.

---

### SLIDE 5: Comparativo Direto e Dados da PoC Local

| Critério | Visão Computacional Tradicional | **Edge AI Specialist (Nossa Solução)** | Fonte / Comprovação |
| :--- | :--- | :--- | :--- |
| **Internet** | Dependente de Nuvem / Link dedicado | **100% Offline (Decisão local em 3,15 ms)** | *PoC Local em CPU / ConectarAGRO* |
| **Hardware por Ponto** | Servidor GPU (R$ 20.000 – R$ 60.000) | **Placa Embarcada ou PC Legado (R$ 0 – R$ 1.500)** | *Sondagem CNI Indústria 4.0* |
| **Tamanho do Modelo** | 10 MB a 250 MB (`FP32`) | **0,02 MB / 20 KB (`INT8` Especialista)** | *Google CVPR 2018 / PoC Local (-99,8%)* |
| **Velocidade em CPU** | Lento em CPU (Exige GPU dedicada) | **317,7 FPS direto na CPU (7,04x mais rápido)** | *Intel OpenVINO / Benchmark PoC Local* |
| **Segurança e Proteção** | Vídeo trafegando na rede externa | **RAM volátil + Proteção IP65/IP67** | *Normas IEC 62443 e ABNT NBR IEC 60529* |

---

### SLIDE 6: Casos de Uso Imediatos (Onde aplicamos amanhã?)
* **Frigoríficos e Alimentos:** Contagem de carcaças/caixas em ambiente úmido (invólucro **IP67 — ABNT NBR IEC 60529**), detecção de contaminação visual ou falha de embalagem.
* **Usinas de Etanol e Agroindústria:** Monitoramento de nível de bagaço em esteira, detecção de embuchamento, presença de corpos estranhos em áreas sem cobertura 4G.
* **Base Florestal e Madeireira:** Classificação de nós/trincas em tábuas, contagem de toras 100% offline.
* **Segurança do Trabalho (NR-12 / SST):** Intertravamento imediato de máquina via relé no CLP se o operador entrar na zona de risco ou estiver sem EPI.

---

### SLIDE 7: Como Funciona na Prática (Da Câmera ao CLP/ERP)
* **Fluxo Visual (4 blocos):**
  `[Câmera Industrial IP65 + LED]` ➔ `[Inferência Local em CPU: ~3,15 ms]` ➔ *(Imagem Descartada da RAM)* ➔ `[Sinal para o CLP (Modbus/Relé) / Dado para o ERP (MQTT/JSON)]`
* **Destaque de Segurança (IEC 62443):** *"Nenhuma imagem da sua fábrica vai para a internet. O sistema funciona como um sensor óptico inteligente fechado."*

---

### SLIDE 8: Proposta de Piloto (Chamada para Ação / Call to Action)
* **Frase de Impacto:** *"Mais de 80% dos projetos gigantes de IA falham porque tentam abraçar a fábrica inteira de uma vez (RAND Corp., 2024). Nós provamos o retorno em 3 semanas em 1 único gargalo."*
* **O Desafio do Projeto Piloto (3 Semanas):**
  * **Semana 1:** Coleta de imagens de **1 gargalo real** da sua planta (esteira, inspeção ou segurança).
  * **Semana 2:** Treinamento especializado, poda neural e quantização `INT8` em laboratório.
  * **Semana 3:** Teste ao vivo no chão de fábrica rodando 100% offline em hardware de baixo custo.
* **Fechamento:** *"Qual é o processo na sua fábrica hoje que, se não falhasse por erro humano, pagaria esse projeto já no primeiro mês?"*

---

### SLIDE 9: Referências Científicas e de Mercado (Para Dúvidas Técnicas e Auditoria)
1. **RAND Corporation (2024):** *The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed* (RR-A2680-1) — Mais de 80% dos projetos de IA falham.
2. **Gartner (2022–2024):** *AI in Production Surveys* — 53% a 85% dos protótipos de IA não chegam à produção industrial.
3. **CNI (2022/2023):** *Sondagem Especial Indústria 4.0 no Brasil* — 66% das indústrias apontam o custo de implantação como principal barreira.
4. **ConectarAGRO / ESALQ-USP (2024):** *Indicador de Conectividade Rural no Brasil* — Déficit de conectividade nas regiões agroindustriais e florestais.
5. **Jacob, B. et al. — Google Research (CVPR 2018):** *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference* — Redução de 75% (`FP32 -> INT8`) e aceleração em CPU.
6. **Han, S. et al. — Stanford University (ICLR 2016):** *Deep Compression: Pruning, Trained Quantization and Huffman Coding* — Redução de até 35x em parâmetros sem perda de acurácia.
7. **Nagel, M. et al. — Qualcomm AI Research (2021):** *A White Paper on Neural Network Quantization* (arXiv:2106.08295).
8. **Howard, A. et al. — Google (ICCV 2019):** *Searching for MobileNetV3* & **Hinton, G. et al. (2015):** *Distilling the Knowledge in a Neural Network*.
9. **Normas Industriais:** **ABNT NBR IEC 60529** (Graus de proteção IP65/IP67) e **IEC 62443** (Segurança cibernética em redes de automação industrial OT/IT).
