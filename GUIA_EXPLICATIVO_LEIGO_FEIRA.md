# 📖 Guia Explicativo do Projeto (Linguagem Simples / Para Leigos e Visitantes da Feira)
**Projeto:** Edge AI Specialist — Inspeção Industrial e Sanitária (Frigorífico SIF/MAPA) de Ultrabaixo Custo  
**Portal Online (GitHub Pages):** https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/  
**Aplicativo da Bancada (TV Box 4K):** https://instrutorrafaelreis.github.io/An-lise-de-EDGE-AI-Industrial/app_tvbox_feira.html  

---

## 💡 1. Qual é o grande problema que resolvemos? (A Dor das Fábricas)

Hoje, quando uma fábrica ou um **frigorífico** quer usar Inteligência Artificial para vigiar a esteira de produção com câmeras (por exemplo, para verificar se um corte de carne está contaminado ou se a bandeja saiu sem o selo obrigatório do governo, o **SIF**), as empresas de tecnologia cobram uma fortuna.

* **Por que é tão caro hoje?** Porque as soluções tradicionais usam "cérebros de IA gigantescos e genéricos" que foram treinados para reconhecer mil coisas diferentes no mundo (cachorro, avião, carro, flor, semáforo...).
* Como esse cérebro é gigante e pesado, ele exige **computadores servidores caríssimos com placas de vídeo especiais (GPUs) que custam de R$ 35.000 a R$ 60.000 por ponto**, ou precisa enviar o vídeo o tempo todo para a **Internet (Nuvem)** — o que trava a produção inteira sempre que a internet oscila na fábrica.

### 🎯 A Nossa Grande Sacada:
> *"Uma esteira de frigorífico não precisa saber o que é um avião ou um cachorro! Ela só precisa olhar para a bandeja de carne e responder **3 coisas** em uma fração de segundo:*
> 1. ***Está boa e com o selo azul do SIF? (Aprovado)***
> 2. ***Está com mancha escura ou contaminação? (Rejeite Sanitário)***
> 3. ***Está sem o selo de rastreabilidade do SIF? (Desvio de Embalagem)"***

---

## 🧠 2. O que fizemos com a Inteligência Artificial? (A "Cirurgia de Emagrecimento")

Para provar que a nossa ideia funciona de verdade com tecnologia de ponta, nós fomos até o catálogo oficial da **NVIDIA** (`https://build.nvidia.com/models`) — a maior fabricante de placas e chips de IA do mundo — e baixamos a arquitetura de um modelo profissional deles chamado **`nvidia/nemotron-ocr-v2` (`RegNetX-8GF`)**.

Originalmente, esse modelo da NVIDIA é um "caminhão pesado" que exige placas de vídeo de servidor de mais de R$ 45.000. No nosso código (`treinar_modelo_frigorifico.py`), nós fizemos uma **"cirurgia de emagrecimento" em 3 etapas** nesse modelo:

1. **Especialização (O "Professor" e o "Aluno"):** Tiramos tudo o que era inútil para uma fábrica e deixamos no "cérebro" da IA apenas os neurônios necessários para enxergar as **3 situações da bandeja do frigorífico**. Usamos o modelo gigante da NVIDIA como um **"Professor"** ensinando um modelo **"Aluno"** super enxuto (*Destilação de Conhecimento*).
2. **Poda Neural (Corte de Gordura):** Cortamos **30% das conexões internas** que faziam pouco esforço, mantendo a inteligência intacta (*Pruning*).
3. **Arredondamento de Números (`INT8`):** Originalmente, a IA faz contas usando números enormes cheios de casas decimais (32 bits / `FP32`). Nós convertemos tudo para números inteiros simples de 8 bits (`INT8`). É como trocar `3,14159265` por `3`: o processador faz a conta quase 100 vezes mais rápido e gasta muito menos memória!

### 📊 O Resultado Real (Antes vs. Depois da Nossa Otimização)

| O que medimos | Antes: Modelo Original da NVIDIA (`nvidia/nemotron-ocr-v2`) | Depois: Nosso Modelo Otimizado (`RegNetX-Edge-SIF INT8`) | O que isso significa na prática? |
| :--- | :--- | :--- | :--- |
| **Tamanho do "Cérebro" (Arquivo)** | **217,12 Megabytes (MB)** *(Pesado como um vídeo longo)* | **11,9 Kilobytes (KB)** *(Menor que uma mensagem de WhatsApp!)* | Encolhemos o modelo em **99,995%**! |
| **Quantidade de Neurônios/Parâmetros** | **56.916.232** (~56,9 Milhões) | **9.731** parâmetros | Redução de **99,98%** da complexidade. |
| **Velocidade sem Placa de Vídeo (CPU)** | **8,6 fotos por segundo** (`116,77 ms` — lento, engasga na esteira) | **840,7 fotos por segundo** (`1,19 ms` — instantâneo!) | Ficou **98,2 vezes mais rápido** no mesmo computador! |
| **Taxa de Acerto nas Bandejas SIF** | Modelo genérico pesado | **100,0% de acerto** nas 3 classes do frigorífico | Mesma precisão industrial, sem custo de servidor. |

---

## 📺 3. Onde essa IA vai rodar na Feira? (O Choque de Baixo Custo)

Como o nosso cérebro de IA ficou minúsculo (`11,9 KB`), nós provamos que **não precisamos mais de um servidor de R$ 45.000**.

Montamos uma bancada de inspeção industrial completa gastando apenas **R$ 155,00**:
1. **O Computador da Esteira (R$ 100,00):** Uma **TV Box Smart Pro Android 4K** comum (aquela caixinha de transformar TV antiga em Smart TV). Por dentro, ela tem um processador de celular (ARM Quad-Core de 64 bits com 4 entradas USB) que roda o nosso sistema perfeitamente.
2. **A Estrutura da Esteira (R$ 25,00):** Um arco feito com **tubos de PVC de 25mm** pintados ou encaixados sobre um tapete de EVA preto (simulando a esteira do frigorífico).
3. **Os Olhos do Sistema (R$ 30,00):** Uma **Webcam USB simples + uma fitinha de luz LED USB** presas no topo do cano de PVC apontando para baixo, garantindo que a iluminação nas bandejas seja sempre igual.

> **Resumo Financeiro para o Dono da Fábrica:** Troca-se um projeto de **R$ 45.000,00** (que demora 2 anos para se pagar) por um kit de **R$ 155,00** (que se paga no primeiro mês e funciona **100% sem internet / em Modo Avião**).

---

## 🖥️ 4. Tudo o que já deixamos pronto no projeto

| Parte do Projeto | Arquivo / Link | Para que serve em linguagem simples? |
| :--- | :--- | :--- |
| **1. Tela Ao Vivo da TV Box + Bandejas para Imprimir** | `app_tvbox_feira.html` | É o painel que fica ligado na tela da feira. Mostra a câmera ao vivo (ou esteira simulada), apita **Verde / Vermelho / Amarelo** para o CLP da fábrica e traz no rodapé os **3 desenhos de carne prontos para imprimir** e colar nas bandejas de isopor. |
| **2. Programa do Notebook com Câmera e Treino Ao Vivo** | `bancada_feira_ao_vivo.py` | Programa em Python que abre a câmera do computador e permite apertar a tecla `[T]` para treinar a IA ao vivo na frente do visitante em 2 segundos. |
| **3. Cirurgia de Otimização do Modelo da NVIDIA** | `treinar_modelo_frigorifico.py` | O programa que baixa o modelo gigante da NVIDIA (`217 MB`), faz a poda e o arredondamento `INT8`, e gera o nosso cérebro de `11,9 KB` (`modelos_poc/modelo_frigorifico_int8.pt`). |
| **4. Site Oficial com Slides + Planta da Mesa + Etiquetas** | `index.html` | O site publicado no GitHub Pages com **9 slides executivos**, **14 referências científicas** (Stanford, Google, NVIDIA, CNI, USP), o desenho de como arrumar a mesa e as **4 etiquetas de preço (`R$ 155 vs R$ 45.000`)** prontas para imprimir. |

---

## 🎤 5. Como explicar o projeto em 30 segundos na Feira (Roteiro Rápido)

Se um visitante parar na sua mesa e perguntar **"O que é isso aqui?"**, basta apontar para a mesa e dizer:

> *"Sabe por que 80% das fábricas desistem de colocar Inteligência Artificial na produção? Porque tentam empurrar servidores de R$ 45 mil com placas de vídeo caras para vigiar uma simples esteira.*
> *Nós fizemos o oposto: pegamos um modelo profissional pesado da NVIDIA de 217 Megabytes, fizemos uma 'cirurgia matemática' nele para focar só na inspeção sanitária de um frigorífico e reduzimos ele para **11 Kilobytes** — ficou **98 vezes mais rápido**.*
> *Resultado: em vez de gastar R$ 45 mil, nossa IA roda **100% sem internet** dentro dessa **TV Box de R$ 100** com um suporte de **cano de PVC de R$ 25**. Coloque uma dessas 3 bandejas de carne aqui embaixo da câmera para você ver ela aprovando ou bloqueando a esteira em 1 milissegundo!"*
