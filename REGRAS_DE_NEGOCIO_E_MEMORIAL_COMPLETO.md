# 📘 Documento Oficial de Regras de Negócio, Engenharia de Otimização e Memorial Descritivo Completo
**Projeto:** Edge AI Specialist — Inspeção Industrial e Sanitária de Frigoríficos (SIF/MAPA) de Ultrabaixo Custo  
**Responsável:** Instrutor Rafael Reis & Equipe de Inovação  
**Repositório Oficial (GitHub):** https://github.com/instrutorrafaelreis/An-lise-de-EDGE-AI-Industrial  
**Portal Web Interativo (GitHub Pages):** https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/  

---

## 🎯 1. Visão Estratégica e Modelo de Negócio (Por que o Projeto Existe)

### 1.1. O Problema Real da Indústria Brasileira
Estudos globais e nacionais comprovam que a adoção de Inteligência Artificial na indústria enfrenta uma barreira estrutural severa:
* **Mais de 80% dos projetos de IA falham** antes de gerar retorno operacional, principalmente por superdimensionamento tecnológico (*RAND Corporation, 2024* `[1]`).
* **Entre 53% e 85% dos protótipos de IA travam na fase piloto** e jamais chegam à linha de produção devido ao custo proibitivo de servidores GPU e infraestrutura de rede (*Gartner Research, 2022–2024* `[2]`).
* **66% das indústrias brasileiras** apontam o alto custo financeiro de implantação (CAPEX) como o principal impeditivo para a digitalização (*Sondagem Especial Indústria 4.0 — CNI* `[3]`).
* **Apagão de conectividade no interior produtivo:** Frigoríficos, usinas sucroenergéticas e plantas agroindustriais sofrem com instabilidade crônica de internet 4G/5G (*ConectarAGRO / ESALQ-USP* `[4]`), tornando inviáveis soluções dependentes de processamento em Nuvem (*Cloud AI*).

### 1.2. A Tese de Engenharia e Negócio do *Edge AI Specialist*
O mercado tradicional tenta resolver problemas industriais simples usando **modelos generalistas gigantescos** (capazes de reconhecer 1.000 objetos genéricos como cães, carros e aviões), o que exige servidores com placas de vídeo dedicadas (**R$ 35.000 a R$ 60.000 por ponto de inspeção**).

**Nossa Regra Fundamental de Negócio:**
> *"Uma linha de produção industrial não precisa de um modelo generalista pesado de 1.000 classes; ela precisa de um **Especialista Ultraleve** focado exclusivamente nas classes reais do seu gargalo produtivo, rodando **100% offline** em processadores comuns de baixo custo (TV Box ARM de R$ 100 ou PCs legados já existentes na fábrica a custo R$ 0)."*

### 1.3. Viabilidade Financeira (CAPEX, OPEX e Payback)

| Indicador Financeiro | Solução Tradicional (Servidor GPU + Cloud) | Nossa Solução (*Edge AI Specialist*) | Impacto no Negócio |
| :--- | :--- | :--- | :--- |
| **CAPEX de Computação (Cérebro)** | R$ 25.000 a R$ 45.000 *(Servidor GPU NVIDIA)* | **R$ 100,00** *(TV Box ARM Cortex-A53)* ou **R$ 0,00** *(Notebook/PC Legado)* | **Redução de 99,7% no custo de hardware** |
| **CAPEX Óptico e Estrutural** | R$ 10.000 a R$ 15.000 *(Câmera proprietária)* | **R$ 55,00** *(Pórtico PVC 25mm R$ 25 + Webcam USB R$ 20 + LED R$ 10)* | **Manutenção simples com peças locais** |
| **Investimento Total por Linha** | **R$ 35.000 a R$ 60.000** | **R$ 55,00 a R$ 155,00** | **Viabiliza IA em pequenas e médias indústrias** |
| **OPEX Mensal (Nuvem / Energia)** | R$ 1.500+/mês *(Link dedicado + 350W GPU)* | **R$ 0,00 de Nuvem** *(Consumo de apenas 5W a 15W)* | **Custo recorrente praticamente nulo** |
| **Tempo de Retorno (Payback / ROI)** | 18 a 36 meses | **Imediato (menos de 30 dias)** | Evitar 1 único lote devolvido pelo SIF já paga 50 kits |

---

## 📜 2. Regras de Negócio Operacionais (`RN-01` a `RN-08` — Domínio Frigorífico SIF/MAPA)

O sistema foi modelado para o setor de **Desossa, Embalagem e Controle Sanitário de Frigoríficos**, seguindo rigorosamente as exigências do **Serviço de Inspeção Federal (SIF / MAPA)**, **NR-36** e normas internacionais de automação:

### 🔹 `RN-01`: Classificação Tripla de Decisão Industrial na Esteira
Toda bandeja que passa sob o pórtico óptico deve ser classificada instantaneamente em uma de **3 categorias de negócio**, disparando ações distintas no CLP (Controlador Lógico Programável) para evitar tanto o risco sanitário quanto o desperdício de matéria-prima:

1. **Classe 0 — `0_CORTE_CONFORME_SIF` (Aprovado para Expedição):**
   * **Critério Visual:** Corte bovino com coloração vermelha característica, capa de gordura íntegra e **Etiqueta Oficial de Rastreabilidade do SIF (Azul/Branca)** devidamente afixada.
   * **Ação de Negócio / CLP:** Aciona sinal **VERDE (`LIBERAR_TUNEL_CONGELAMENTO`)**, emite bipe sonoro curto (`950 Hz`) e incrementa o lote aprovado no ERP.
2. **Classe 1 — `1_CONTAMINACAO_HEMATOMA` (Bloqueio Sanitário Crítico):**
   * **Critério Visual:** Presença de mancha esverdeada/amarelada (**contaminação biliar ou gastrointestinal**) ou coágulo escuro (**hematoma severo / abscesso**) na superfície do corte.
   * **Ação de Negócio / CLP:** Aciona imediatamente o pistão pneumático de **REJEITE SANITÁRIO (`ACIONAR_PISTAO_REJEITE_SANITARIO`)**, dispara **Sirene Industrial Vermelha (`310 Hz`)** e registra ocorrência crítica para inspeção veterinária do SIF.
3. **Classe 2 — `2_FALHA_ROTULO_EMBALAGEM` (Desvio para Reprocessamento — Economia de Matéria-Prima):**
   * **Critério Visual:** O corte de carne está saudável, porém a bandeja está **sem o selo obrigatório do SIF** ou apresenta rasgo/violação na borda do filme plástico.
   * **Ação de Negócio / CLP:** Aciona o desvio secundário de **RE-ROTULAGEM (`DESVIAR_PARA_REROTULAGEM_SIF`)** com alerta amarelo (`520 Hz`). **Regra de Ouro:** Não descarta a carne boa no lixo sanitário; apenas devolve a bandeja para a rotuladora, economizando milhares de reais por turno!

### 🔹 `RN-02`: SLA Determinístico de Tempo Real (`Latência < 15 ms`)
* **Regra:** Para que o atuador pneumático da esteira consiga desviar uma bandeja defeituosa em movimento sem parar a linha, o tempo total de resposta da IA deve ser **inferior a 15 milissegundos** (`> 66 FPS`).
* **Cumprimento Técnico:** Nosso modelo otimizado executa em **`2,55 ms` (`392 FPS`)** mesmo quando restrito a **1 único núcleo físico de CPU** (simulando a TV Box ARM), e em **`1,35 ms` (`740 FPS`)** em Notebook legado.

### 🔹 `RN-03`: Operação 100% Offline e Autônoma (*Zero-Cloud Dependency*)
* **Regra:** O sistema é proibido de depender de chamadas de API externas, servidores na internet ou conexão Wi-Fi para classificar produtos. Mesmo com o cabo de rede desconectado (Modo Avião), a inspeção na esteira opera com 100% de capacidade.

### 🔹 `RN-04`: Privacidade Industrial *By Design* e Cibersegurança OT/IT (`Norma IEC 62443`)
* **Regra:** Nenhuma imagem ou vídeo do interior da planta industrial pode ser transmitido pela rede corporativa ou salvo em nuvem de terceiros (proteção de segredo industrial e LGPD).
* **Cumprimento Técnico:** O frame capturado pela Webcam USB é lido diretamente em buffer volátil na memória RAM, processado pela rede neural em `< 3 ms` e **imediatamente sobrescrito/descartado**. Apenas metadados textuais leves (`JSON` de ~120 bytes) ou pulsos elétricos seguem para o CLP/ERP.

### 🔹 `RN-05`: Auditoria Automática de Lote e Rastreabilidade SIF (`CSV` / `JSON`)
* **Regra:** Toda mudança de estado ou peça inspecionada deve gerar registro auditável contendo `Timestamp`, `Modo de Hardware`, `Classe Detectada`, `Confiança (%)`, `Latência (ms)` e `Ação do CLP`.
* **Cumprimento Técnico:** Pressionando a tecla **`[R]`** na estação SCADA (`simular_ambiente_tvbox.py`), o sistema exporta instantaneamente a planilha oficial **`auditoria_lote_sif.csv`** pronta para fiscalização do MAPA/SIF.

### 🔹 `RN-06`: Explicabilidade Neural para Fiscalização (*Explainable AI / Grad-CAM*)
* **Regra:** A IA não pode ser uma "caixa-preta" inexplicável perante um auditor sanitário. O supervisor deve poder visualizar *por que* a rede aprovou ou condenou determinado corte.
* **Cumprimento Técnico:** Pressionando a tecla **`[G]`**, o sistema ativa o módulo **Grad-CAM (Mapa de Calor de Ativação Espacial)** em tempo real sobre o vídeo, destacando em vermelho/amarelo exatamente os pixels que ativaram os neurônios da decisão (a mancha biliar ou a etiqueta SIF).

### 🔹 `RN-07`: Calibração Instantânea de Turno (*On-Device Few-Shot Calibration*)
* **Regra:** Mudanças na iluminação do galpão ou troca do lote de bandejas devem poder ser calibradas pelo próprio operador de linha em menos de 10 segundos.
* **Cumprimento Técnico:** O operador posiciona as 3 bandejas padrão sob o pórtico de PVC e pressiona **`[1]`**, **`[2]`**, **`[3]`** e **`[T]`**, recalibrando os pesos do classificador final localmente na CPU em menos de 1 segundo.

### 🔹 `RN-08`: Padronização Óptica e Ambiental (`ABNT NBR IEC 60529 IP65/IP67` e `NR-36`)
* **Regra:** Câmeras no chão de fábrica não podem depender da iluminação variável do telhado da fábrica. O pórtico óptico deve possuir iluminação LED dedicada a 90° sobre a esteira e prever invólucro selado (`IP67`) para ambientes úmidos de frigorífico.

---

## 🛠️ 3. Memorial Descritivo Completo: Tudo o que Foi Feito no Projeto

Abaixo está o registro técnico completo de todas as entregas desenvolvidas neste repositório:

### 3.1. Seleção e Download do Modelo Oficial da NVIDIA (`build.nvidia.com/models`)
1. Acessamos e auditamos o catálogo empresarial de modelos da NVIDIA (**NVIDIA NIM / Build** em `https://build.nvidia.com/models`).
2. Selecionamos como arquitetura base ("Modelo Professor") o modelo oficial **[nvidia/nemotron-ocr-v2](https://build.nvidia.com/nvidia/nemotron-ocr-v2)**, cujo detector visual utiliza o backbone convolucional **`RegNetX-8GF`** (*Radosavovic et al., CVPR 2020*).
3. Baixamos os pesos oficiais pretreinados do `RegNetX-8GF` e instanciamos a arquitetura completa (`56.916.232` parâmetros, ocupando **`217,12 MB`** em precisão `FP32` de 32 bits e exigindo **`16,02 Bilhões de operações matemáticas (16,02 GFLOPs)`** por imagem).
4. Medimos o desempenho desse modelo original sem placa de vídeo: ele levou **`228,72 ms` por foto (`4,4 FPS`)** em 1 núcleo de CPU — comprovando que o modelo original da NVIDIA trava sem uma GPU cara de servidor.

### 3.2. Pipeline de Otimização Matemática em 5 Estágios (`treinar_modelo_frigorifico.py`)
Construímos o script automatizado `treinar_modelo_frigorifico.py` que aplica **5 técnicas científicas do estado da arte** para transformar o modelo pesado da NVIDIA no nosso especialista **`RegNetX-Edge-SIF Fused INT8`**:

1. **Estágio 1 — Poda Estrutural de Profundidade (*Early-Exit Stem + Block 1*) + Especialização de Domínio:**
   * Removemos os blocos convolucionais profundos voltados às 1.000 classes genéricas do ImageNet e conectamos um cabeçote classificador ultraleve focado exclusivamente nas **3 classes do Frigorífico SIF**.
2. **Estágio 2 — Destilação de Conhecimento (*Knowledge Distillation — Hinton et al., 2015* `[8]`):**
   * O modelo gigante `RegNetX-8GF` atua como *Professor*, transferindo sua distribuição de probabilidades suavizada por temperatura (`T = 2.0`, divergência de Kullback-Leibler) para guiar o treinamento do modelo *Aluno* em um dataset industrial de 540 imagens com ruído óptico e variação de brilho.
3. **Estágio 3 — Poda Neural Não-Estruturada L1 de 35% (*Deep Compression — Han et al., Stanford ICLR 2016* `[6]`):**
   * Eliminamos 35% das conexões sinápticas de menor magnitude absoluta nas camadas convolucionais e lineares.
4. **Estágio 4 — Fusão Algébrica de Operadores (`Conv2d + BatchNorm2d Folding`):**
   * Absorvemos matematicamente todas as **5 camadas `BatchNorm2d`** dentro dos pesos e bias das camadas `Conv2d` anteriores ($W_{\text{fused}} = W \cdot \frac{\gamma}{\sqrt{\sigma^2 + \epsilon}}$), reduzindo a **zero** o custo de normalização em lote durante a inferência.
5. **Estágio 5 — Quantização Simétrica Por Canal (`Per-Channel QAT INT8` `[-127, +127]`) + Congelamento JIT (`torch.jit.freeze`):**
   * Aplicamos ajuste fino consciente de quantização (*Google CVPR 2018* `[7]`), comprimimos os pesos para inteiros de 8 bits por canal (`modelo_frigorifico_int8.pt` de **`11,2 KB`**) e congelamos o grafo compilado para execução nativa em CPU (`modelo_frigorifico_jit_otimizado.pt`).

### 3.3. Resultados Auditados do Modelo (Salvos em `modelos_poc/benchmark_frigorifico.json`)

| Indicador Técnico Auditado | Antes: Modelo NVIDIA (`RegNetX-8GF FP32`) | Depois: Nosso Especialista (`RegNetX-Edge-SIF Fused INT8`) | Ganho Real Obtido |
| :--- | :--- | :--- | :--- |
| **Número de Parâmetros** | `56.916.232` | **`9.571`** *(+ 5 BatchNorms fundidas)* | **`-99,983%` parâmetros** |
| **Tamanho do Modelo em Disco** | `217,12 MB` (`FP32`) | **`11,2 KB` (`0,011 MB` em `INT8`)** | **`-99,995%` menor** |
| **Cálculos por Foto (`FLOPs`)** | `16,02 GFLOPs` (`16.024.936.832` contas) | **`89,11 MFLOPs` (`89.111.120` contas)** | **`-99,44%` menos cálculos** |
| **Latência no Emulador TV Box (`1 Núcleo Core 0`)** | `228,72 ms` (`4,4 FPS`) | **`2,55 ms` (`392,0 FPS`)** | **`89,8x MAIS RÁPIDO` em 1 núcleo!** |
| **Latência no Notebook (`8 Núcleos CPU`)** | `154,03 ms` (`6,5 FPS`) | **`1,35 ms` (`740,7 FPS`)** | **`114,3x MAIS RÁPIDO` no Notebook!** |
| **Acurácia / `F1-Score` Macro (Validação)** | — | **`100,0%` (`F1 = 100,0%`)** | Matriz de Confusão 3x3: `[[46,0,0],[0,51,0],[0,0,38]]` |

### 3.4. Simulador de Hardware da TV Box no Notebook (`simular_ambiente_tvbox.py`)
Para permitir testes rigorosos e demonstração ao vivo no próprio Notebook simulando exatamente as restrições físicas da **TV Box Smart Pro 4K (`ARM Cortex-A53 / 2GB DDR3 RAM`)**, desenvolvemos a estação SCADA + XAI (`simular_ambiente_tvbox.py` e `RODAR_SIMULADOR_TVBOX_NO_NOTEBOOK.bat`) que:
* Chama a API nativa do Kernel do Windows (`ctypes.windll.kernel32.SetProcessAffinityMask = 0x01`) para **travar o processo em 1 único núcleo físico da CPU (`Core 0`)** e reduzir a prioridade de clock (`BELOW_NORMAL_PRIORITY_CLASS`).
* Monitora em tempo real o consumo de memória RAM (`WorkingSetSize`) frente ao limite de **`2048 MB (2 GB)`** da TV Box (consumindo apenas `~118 MB`, ou seja, menos de 6% da memória da TV Box).
* Exibe **Mapa de Calor Neural Grad-CAM (`Tecla [G]`)**, **Osciloscópio de Latência em Tempo Real**, **Barras de Probabilidade Softmax das 3 Classes**, **Alarme Sonoro Industrial (`winsound.Beep`)** e **Exportador de Laudo CSV do SIF (`Tecla [R]`)**.

### 3.5. Pacote Chave-na-Mão para Pendrive da TV Box (`PENDRIVE_TVBOX_PRONTO/` e `.zip`)
Criamos a estrutura completa pronta para copiar para um Pendrive USB e espetar diretamente na TV Box ou em qualquer Notebook antigo:
* `ABRIR_NA_TVBOX.html`: WebApp 100% offline compatível com o **Controle Remoto da TV Box**, Mouse USB e Webcam USB, com sirene sonora via `Web Audio API` e seletor de modo de hardware.
* `MOLDES_E_ETIQUETAS_PARA_IMPRIMIR.html`: Folha única pronta para impressão contendo os **3 Moldes de Bandejas de Carne do SIF** (para colar nas bandejas de isopor) e as **4 Etiquetas de Preço (`R$ 155 vs R$ 45.000`)**.
* `APRESENTACAO_SLIDES_E_BANCADA.html` / `index.html`: Portal com 9 Slides Executivos, Cronograma de Execução, Planta Visual das 3 Zonas da Mesa e as **14 Referências Científicas e de Mercado**.
* Documentação completa em Word (`.docx`) e Markdown (`.md`) para leigos, montagem de infraestrutura física (cortes exatos do cano de PVC de 25mm) e roteiro de prompts para os alunos.
