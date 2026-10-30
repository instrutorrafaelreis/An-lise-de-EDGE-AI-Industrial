# Cronograma de Execução (Sprint de 11 Dias — Até o Dia 10)
**Objetivo:** Deixar o projeto **Edge AI Specialist** 100% pronto, testado e blindado para demonstração ao vivo em **Feira de Inovação**.

---

## 💡 O Segredo para Vencer na Feira de Inovação (O "Efeito Uau" no Estande)
Em uma feira de inovação, visitantes e avaliadores passam 30 segundos na frente de cada bancada. Slides sozinhos não prendem atenção; **interação física ao vivo** sim.

A estratégia do estande será o **"Desafio Modo Avião (Zero Internet + Zero GPU)"**:
1. **Notebook antigo / Mini-PC ou Raspberry Pi na bancada com o Wi-Fi visivelmente DESLIGADO (Modo Avião).**
2. **Uma Webcam USB comum (fixada em um suporte simples com LED) apontada para a bancada.**
3. **3 a 4 objetos físicos reais na mesa** para o próprio visitante colocar debaixo da câmera (ex.: 2 peças/embalagens perfeitas e 2 peças com trinca/defeito marcado, ou mini-EPI).
4. **Reação Instantânea na Tela (e opcionalmente num LED/Relé USB):** Em **3 milissegundos**, a tela fica VERDE (*Peça Aprovada*) ou VERMELHA (*Defeito Detectado — Acionando Relé CLP*), mostrando que o modelo tem apenas **20 KB** e roda a **300+ FPS na CPU**.

---

## 📅 Cronograma Dia a Dia (Dia 30 até Dia 10)

| Data / Dia | Fase | Entregas e Tarefas Práticas | Status Atual |
| :--- | :--- | :--- | :---: |
| **Dia 30 (Hoje)** | **Fase 1: Fundação & PoC Virtual** | • Documento Técnico e Referências Científicas (`PROPOSTA_EDGE_AI.md`)<br>• Roteiro de Pitch Comercial (`PITCH_COMERCIAL_EDGE_AI.md`)<br>• Slides Interativos Offline (`APRESENTACAO_EDGE_AI.html`)<br>• PoC de Compressão `INT8` (20 KB / 317 FPS) e Simulador de Esteira (`simulador_esteira_offline.py`) | ✅ **CONCLUÍDO** |
| **Dia 31** | **Fase 2: Escolha do Objeto Físico da Feira** | • Definir qual **objeto físico real** será levado para a bancada da feira (ex.: chapas metálicas, garrafas/embalagens, peças impressas em 3D ou EPIs).<br>• Posicionar a Webcam USB + luminária LED simples sobre a mesa. | ⏳ Pendente |
| **Dia 01** | **Fase 2: Coleta de Imagens Reais** | • Capturar **50 fotos da peça BOA** e **50 fotos da peça COM DEFEITO** usando a própria webcam que irá para a feira (leva ~30 minutos).<br>• Organizar nas pastas `dataset_feira/ok` e `dataset_feira/defeito`. | ⏳ Pendente |
| **Dia 02** | **Fase 3: Treinamento Real & Compressão INT8** | • Rodar o script `pipeline_especializacao_int8.py` com as fotos reais das peças da feira.<br>• Validar se a acurácia pós-poda e quantização `INT8` atingiu **>98%** nas peças físicas. | ⏳ Pendente |
| **Dia 03** | **Fase 3: Integração Webcam Ao Vivo** | • Testar o modo Webcam ao vivo no sistema de demonstração.<br>• Ajustar a caixa de inspeção (ROI) na tela para que, ao colocar a peça na marcação da mesa, o diagnóstico apareça instantaneamente. | ⏳ Pendente |
| **Dia 04** | **Fase 4: Hardware Físico / "Efeito Uau" (Opcional mas Recomendado)** | • Conectar um **ESP32 ou Arduino via USB** (custo ~R$ 40) com 1 LED Verde, 1 LED Vermelho e 1 Buzzer/Relé físico.<br>• Quando a IA detectar defeito na webcam, o relé dá o "clique" físico e acende a luz vermelha na bancada (simulando o CLP real da indústria). | ⏳ Pendente |
| **Dia 05** | **Fase 5: Identidade Visual e Material de Apoio** | • Gerar um **QR Code** (impresso em plaquinha de acrílico/papel couchê para a mesa) que leva para o PDF do Pitch / WhatsApp / LinkedIn.<br>• Imprimir 1 folha A4 plastificada com o **"Desafio Modo Avião: Teste você mesmo a IA de 20 KB"**. | ⏳ Pendente |
| **Dia 06** | **Fase 6: Teste de Estresse ("Prova de Fogo")** | • Deixar o sistema rodando por **2 horas seguidas** fora da internet na máquina que irá para a feira.<br>• Testar variações de luz (luz do salão ligada/desligada) usando a luminária LED dedicada sobre a peça. | ⏳ Pendente |
| **Dia 07** | **Fase 7: Ensaio do Pitch (Treino de 1 Minuto e 5 Minutos)** | • Treinar o **Pitch de Bancada (60 segundos)**: falar enquanto coloca a peça boa e a peça com defeito sob a câmera.<br>• Treinar as respostas para perguntas difíceis usando o **Slide 9 de Referências** (RAND Corp, Gartner, CNI, Google CVPR). | ⏳ Pendente |
| **Dia 08** | **Fase 8: Plano de Contingência (Plano B)** | • Gravarmos um vídeo de 45 segundos da demonstração funcionando perfeitamente (caso a webcam quebre no transporte).<br>• Deixar o **Modo Simulador Virtual (`simulador_esteira_offline.py`)** pronto num atalho da Área de Trabalho como backup imediato. | ⏳ Pendente |
| **Dia 09** | **Fase 9: Checklist de Maleta e Pré-Montagem** | • Separar na mochila/maleta: Notebook/PC + Fonte + Extensão elétrica/Filtro de linha + Webcam USB + Luminária LED + Peças de teste + Plaquinha QR Code.<br>• Verificar se os arquivos abrem sem internet (Modo Avião ligado). | ⏳ Pendente |
| **Dia 10** | **🚀 DIA DA FEIRA DE INOVAÇÃO** | • Montagem da bancada em 15 minutos.<br>• Abrir na tela dividida: **Simulador/Webcam ao vivo** + **Apresentação Executiva (`APRESENTACAO_EDGE_AI.html`)**.<br>• Executar a demonstração interativa com visitantes, avaliadores e potenciais clientes! | 🎯 **META FINAL** |

---

## 🛠️ Checklist Físico da Bancada (O que levar no Dia 10)

- [ ] **Computador de Demonstração** (quanto mais modesto/antigo, mais impressiona os engenheiros quando virem `300+ FPS` na CPU).
- [ ] **Webcam USB** + pequeno tripé ou suporte articulado apontado para baixo (visão superior da esteira/bancada).
- [ ] **Luminária LED USB simples** apontada para a área da peça (garante que a iluminação do pavilhão da feira não atrapalhe a câmera — prova o **Pilar 4** na prática).
- [ ] **Tapete escuro / EVA preto demarcado** na mesa indicando *"COLOQUE A PEÇA AQUI PARA INSPEÇÃO"*.
- [ ] **Kit de Peças de Teste:** 2 peças perfeitas (identificadas com adesivo verde na base) e 2 peças com defeito visível (trinca, risco forte ou mancha).
- [ ] **Extensão elétrica / Régua de tomadas** (essencial em feiras).

---

## 🎤 Roteiro de Abordagem de 45 Segundos no Estande (Como atrair o visitante)

1. **Gancho (10s):** *"Posso te mostrar como uma IA industrial de apenas 20 Kilobytes inspeciona peças em 3 milissegundos num computador sem internet e sem placa de vídeo?"*
2. **Ação Física (15s):** *(Entregue a peça com defeito na mão do visitante)* *"Coloque essa peça aqui debaixo da câmera. Repare que o computador está em Modo Avião."*
3. **Impacto (10s):** *(A tela acusa DEFEITO em vermelho e mostra o comando do CLP)* *"Em 3 milissegundos a CPU detectou a falha, acionou o relé do CLP para expulsar a peça da esteira e já descartou a imagem da memória RAM por segurança."*
4. **Fechamento de Negócio (10s):** *"Enquanto uma solução tradicional custa R$ 50 mil em servidores GPU, isso aqui roda até num PC antigo que a sua fábrica já tem parado no almoxarifado."*
