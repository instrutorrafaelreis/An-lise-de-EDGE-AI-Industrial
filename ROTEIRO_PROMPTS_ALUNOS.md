# 🎓 Roteiro de Prompts Guiados para os Alunos Finalizarem o Projeto (Rumo à Feira — Dia 10)
**Professor Responsável:** Instrutor Rafael Reis  
**Projeto:** Edge AI Specialist — Inspeção Sanitária de Frigorífico (SIF/MAPA) em TV Box de R$ 100  
**Repositório Oficial do Projeto:** `https://github.com/instrutorrafaelreis/An-lise-de-EDGE-AI-Industrial`  
**Portal Online (GitHub Pages):** `https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/`  

---

## 📌 Como os Alunos Devem Usar Este Guia
A base matemática do projeto (otimização do modelo `nvidia/nemotron-ocr-v2` / `RegNetX-8GF` de **217 MB para 11,9 KB em INT8**), o portal web e o sistema de visão já estão no repositório.  
Para **terminar o projeto até o Dia 10**, a turma deve ser dividida em **5 Missões Práticas**. Em cada missão abaixo, o aluno encontra **o que precisa fazer fisicamente** e o **Prompt Exato (Copiar e Colar)** para usar na IA assistente (ChatGPT, Claude, Gemini ou Antigravity/Cursor) caso precise adaptar ou concluir aquela etapa!

---

## 🚀 MISSÃO 1: Baixar o Projeto e Rodar o Benchmark no Computador da Equipe
**Objetivo do Aluno:** Clonar o repositório oficial, instalar o PyTorch/OpenCV e comprovar que o modelo de `11,9 KB` roda na máquina da equipe.

### 📋 Prompt 1 (Para o aluno copiar e colar na IA se precisar de ajuda para rodar):
```text
Estou trabalhando no projeto escolar/industrial "Edge AI Specialist para Frigorífico (SIF/MAPA)" do repositório https://github.com/instrutorrafaelreis/An-lise-de-EDGE-AI-Industrial.
Nossa arquitetura otimiza o backbone RegNetX-8GF (do modelo nvidia/nemotron-ocr-v2) usando Poda Estrutural, Destilação de Conhecimento, Poda L1 de 30% e Quantização INT8 para rodar em uma TV Box ARM Cortex-A53 de R$ 100.

Me ajude passo a passo no terminal do Windows (PowerShell) a:
1. Clonar o repositório do GitHub e entrar na pasta do projeto.
2. Criar e ativar um ambiente virtual Python (venv) e instalar as dependências do arquivo requirements.txt (torch, torchvision, opencv-python, numpy).
3. Executar o script `python treinar_modelo_frigorifico.py` para gerar o modelo `modelos_poc/modelo_frigorifico_int8.pt` e verificar o arquivo `modelos_poc/benchmark_frigorifico.json`.
4. Executar o sistema visual `python bancada_feira_ao_vivo.py` e me explicar como testar as teclas [1], [2], [3], [T] e [M].
```

---

## 📸 MISSÃO 2: Substituir Imagens Sintéticas por Fotos Reais das 3 Bandejas (Pórtico de PVC)
**Objetivo do Aluno:** Assim que o grupo montar o arco de cano de PVC de 25mm com a Webcam USB e preparar as **3 bandejas de isopor** (*Bandeja 1: Corte Conforme SIF*, *Bandeja 2: Contaminação/Hematoma*, *Bandeja 3: Sem Rótulo SIF*), os alunos devem capturar **30 fotos reais de cada bandeja** usando a webcam e retreinar o modelo com fotos reais!

### 📋 Prompt 2 (Para o aluno criar o capturador de fotos reais da Webcam):
```text
No nosso projeto Edge AI de Frigorífico, o script `treinar_modelo_frigorifico.py` atualmente usa a função `gerar_dataset_frigorifico()` com imagens sintéticas para treinar as 3 classes:
- Classe 0: `0_CORTE_CONFORME_SIF` (Bandeja com corte vermelho padrão e etiqueta azul do SIF)
- Classe 1: `1_CONTAMINACAO_HEMATOMA` (Bandeja com mancha esverdeada/escura de contaminação biliar ou hematoma)
- Classe 2: `2_FALHA_ROTULO_EMBALAGEM` (Bandeja sem etiqueta do SIF ou com embalagem rasgada)

Crie para mim um script em Python chamado `capturar_fotos_reais_bancada.py` usando OpenCV (`cv2.VideoCapture(0)`) que:
1. Abra a imagem da nossa Webcam USB presa no pórtico de PVC e desenhe um quadrado guia central de 224x224 pixels.
2. Quando eu apertar a tecla [1], tire 30 fotos seguidas (com pequeno intervalo de 0.1s) da Bandeja 1 e salve na pasta `dataset_real/0_CORTE_CONFORME_SIF/`.
3. Quando eu apertar a tecla [2], tire 30 fotos seguidas da Bandeja 2 e salve na pasta `dataset_real/1_CONTAMINACAO_HEMATOMA/`.
4. Quando eu apertar a tecla [3], tire 30 fotos seguidas da Bandeja 3 e salve na pasta `dataset_real/2_FALHA_ROTULO_EMBALAGEM/`.
5. Depois, adapte o nosso `treinar_modelo_frigorifico.py` para carregar essas fotos reais da pasta `dataset_real/` (com Data Augmentation de brilho e rotação leve) e gerar o novo `modelo_frigorifico_int8.pt` de 11,9 KB!
```

---

## 🔌 MISSÃO 3: Adicionar Alerta Sonoro (Bipe Industrial) e Acionamento Físico (LED / Relé / Arduino)
**Objetivo do Aluno:** Na feira de inovação, barulho e luz chamam muita atenção! Quando o visitante colocar a **Bandeja 2 (Contaminação)** ou a **Bandeja 3 (Sem Selo SIF)** debaixo da câmera, o sistema deve emitir um **Bipe Sonoro de Alarme Industrial** na caixa de som da TV/Notebook (e, opcionalmente, acender um LED vermelho via porta USB/Arduino se a equipe quiser ganhar pontos extras de automação).

### 📋 Prompt 3 (Para o aluno colocar Sirene/Bipe Sonoro no App da TV Box e no Python):
```text
Queremos deixar a demonstração da nossa bancada na Feira de Inovação ainda mais impactante nos arquivos `app_tvbox_feira.html` e `bancada_feira_ao_vivo.py`:
1. No arquivo `app_tvbox_feira.html`, adicione um sintetizador de áudio nativo do navegador (`Web Audio API`, sem precisar de arquivos MP3 externos para funcionar 100% offline na TV Box) que:
   - Emita um bipe curto e agudo de confirmação ("BIP VERDE" em 880 Hz) quando uma bandeja `CORTE_CONFORME_SIF` passar pela câmera.
   - Emita um alarme sonoro industrial duplo ("SIRENE VERMELHA" em 220 Hz / 440 Hz) quando detectar `CONTAMINACAO_HEMATOMA` ou `FALHA_ROTULO_EMBALAGEM`.
   - Inclua um botão "🔊 Som: Ligado/Desligado" no topo da tela.
2. No arquivo Python `bancada_feira_ao_vivo.py`, adicione também o alerta sonoro usando a biblioteca nativa `winsound.Beep()` do Windows quando detectar defeito sanitário.
Me entregue o código pronto para atualizar os dois arquivos.
```

---

## 📺 MISSÃO 4: Preparar o "Kit Pendrive Offline" + QR Code para a TV Box Smart Pro 4K
**Objetivo do Aluno:** Garantir que no dia da feira (Dia 10) a equipe não dependa do Wi-Fi do evento. Tudo deve caber num Pendrive USB espetado na **TV Box Smart Pro Android 4K**, e a tela deve mostrar um **QR Code** para os visitantes escanearem com o celular e abrirem o GitHub Pages da turma.

### 📋 Prompt 4 (Para o aluno gerar o QR Code e o pacote de Pendrive da TV Box):
```text
Precisamos preparar o pacote final de implantação offline para espetar via Pendrive USB na nossa TV Box Smart Pro Android 4K (ARM Cortex-A53) no dia da Feira de Inovação.
Crie um script Python chamado `gerar_kit_pendrive.py` que:
1. Gere uma imagem de QR Code (ou um SVG offline embutido direto no HTML) apontando para o nosso site oficial da feira: `https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/`.
2. Insira esse QR Code no canto do arquivo `app_tvbox_feira.html` e também nas etiquetas imprimíveis do `index.html`, com a legenda: "📱 Escaneie para ver o Código, Benchmark NVIDIA e Artigos Científicos".
3. Crie uma pasta chamada `PENDRIVE_FEIRA_DIA_10/` contendo todos os arquivos necessários (`index.html`, `app_tvbox_feira.html`, `MODELO_VISUAL_BANCADA.html` e a pasta `modelos_poc/`) prontos para copiarmos para o Pendrive.
```

---

## 🎤 MISSÃO 5: Simulador de Banca Avaliadora (Treino de Pitch para os Alunos)
**Objetivo do Aluno:** Todos os integrantes do grupo precisam saber responder às perguntas dos juízes, professores e empresários na feira sem gaguejar.

### 📋 Prompt 5 (Para cada aluno colar na IA e treinar a apresentação individualmente):
```text
Atue como um Juiz Avaliador rigoroso de uma Feira de Inovação Industrial e Tecnológica.
Eu sou aluno expositor do projeto "Edge AI Specialist para Frigoríficos (Inspeção SIF/MAPA)".
Aqui estão os dados reais do nosso projeto:
- Problema: 80% dos projetos de IA falham (RAND Corp, 2024) e 66% das indústrias brasileiras travam no custo de hardware (CNI). Um servidor com placa de vídeo GPU custa R$ 45.000 por ponto de inspeção.
- Nossa Solução: Pegamos o modelo oficial `nvidia/nemotron-ocr-v2` (arquitetura RegNetX-8GF com 56,9 milhões de parâmetros e 217,12 MB em FP32) do catálogo `build.nvidia.com/models`.
- Nossa Otimização: Aplicamos Especialização para 3 classes do SIF (Corte Conforme, Contaminação Biliar/Hematoma e Falha de Rótulo SIF), Destilação de Conhecimento, Poda L1 de 30% e Quantização para inteiros de 8 bits (INT8).
- Nosso Resultado: O modelo caiu de 217,12 MB para apenas 11,9 KB (-99,995%), ficou 98,2 vezes mais rápido na CPU (1,19 ms por foto / 840 FPS) com 100% de acurácia nas 3 classes.
- Nosso Hardware na Bancada: Roda 100% offline dentro de uma TV Box Smart Pro Android 4K (ARM Cortex-A53 Quad-Core 64-bit) de R$ 100 + Pórtico de PVC de R$ 25 + Webcam/LED USB de R$ 30 (Total: R$ 155 vs R$ 45.000).

Me faça 1 pergunta difícil de cada vez (como se você fosse um jurado na frente da minha bancada), aguarde a minha resposta, dê uma nota de 0 a 10 para o que eu respondi e me mostre como melhorar minha argumentação!
```

---

## 📅 Divisão Sugerida de Tarefas para a Turma (Quem faz o quê até o Dia 10)

| Equipe / Dupla | Responsabilidade Principal | Entrega Obrigatória até o Dia 08 |
| :--- | :--- | :--- |
| **Equipe A (Infra & Maquete)** | Seguir o `MANUAL_INFRAESTRUTURA_E_MONTAGEM.docx` | Pórtico de PVC cortado e montado + Tapete EVA + 3 Bandejas de Isopor coladas + 4 Etiquetas de Preço impressas. |
| **Equipe B (IA & Visão Computacional)** | Executar os **Prompts 1 e 2** | Capturar as fotos reais das 3 bandejas sob o PVC e calibrar o modelo `RegNetX-Edge-SIF (11,9 KB)`. |
| **Equipe C (TV Box & Automação)** | Executar os **Prompts 3 e 4** | Configurar a TV Box Smart Pro 4K com Mouse + Webcam + Som de Alarme + Pendrive Offline + QR Code. |
| **Equipe D (Comercial & Pitch)** | Estudar o `GUIA_EXPLICATIVO_LEIGO_FEIRA.docx` e rodar o **Prompt 5** | Dominar a apresentação nos 9 slides do `index.html` e conduzir o desafio interativo das 3 bandejas com os visitantes. |
