<h1 align="center">⚡ Projeto 14: Análise Numérica de Fluxo de Potência</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Sistemas_Pot%C3%AAncia-FFD700%3Fstyle%3Dfor-the-badge%26logo%3Delectron%26logoColor%3Dblack" alt="Power Systems Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 14!** Este desafio insere a equipe no coração da computação de alto desempenho. Sistemas complexos (como redes elétricas) não podem ser resolvidos com equações simples diretas. É preciso ensinar o computador a usar um "Método Iterativo", calculando milhares de vezes até chegar na resposta.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Em uma rede com 3 bairros e 1 usina, se o Bairro B ligar milhares de motores, a tensão (voltagem) nos fios vai cair. Mas cai quanto? Não dá para resolver de cabeça.

O computador usa o **Método de Gauss-Seidel**: ele "chuta" que todas as tensões estão perfeitas (100V). Ele joga na equação e a resposta dá 95V. Ele pega esse 95V e recalcula, dando 92V. Ele repete isso num laço infinito até que a resposta pare de mudar. É o ápice da Lógica de Repetição!

🎯 **A Missão:** Construir o simulador simplificado de fluxo DC. O usuário cadastra os bairros (barras) e fios. O Motor Iterativo descobre as tensões finais e o analista de perdas aponta fios em perigo.

## **🧮 2. Regras de Negócio e Método Numérico**

### **🏛️ 2.1. O que é a Rede?**

* **Barra Slack (Usina - Barra 1):** Tensão fixa de **100V** sempre.  
* **Barras de Carga (Bairros):** Possuem um consumo em Ampères (Negativo, ex: -10). O "Chute Inicial" delas é 100V.

### **🔄 2.2. A Equação Iterativa**

Para descobrir o V_novo de uma Barra, usamos a soma dos seus vizinhos:

V_novo = (Corrente_Carga + Soma(V_Vizinhos / R_linhas)) / Soma(1 / R_linhas)

### **🛑 2.3. O Critério de Parada**

O laço while True para quando a diferença entre o V_velho e o V_novo for minúscula (o erro).

* erro = abs(V_novo - V_velho). Se o erro máximo for < 0.001, use o break.

### **🔥 2.4. Cálculo de Perdas**

* Corrente_no_Fio = (V_barra_A - V_barra_B) / R_do_Fio  
* Perda_em_Watts = R_do_Fio * (Corrente_no_Fio ** 2)

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**A Rede Teste:**

* **Barra 1 (Usina):** 100V | **Barra 2:** Carga -10A | **Barra 3:** Carga -5A  
* **Fios:** Barra 1-2 (R=1). Barra 2-3 (R=1). Barra 1-3 (R=2).

**Validação (Primeira Iteração - Chute V=100 em tudo):**

* [x] **Novo V2:** Numerador: -10 + (100/1) + (100/1) = 190. Denominador: (1/1) + (1/1) = 2. Novo V2 = 190 / 2 = **95.0 V**.  
* [x] **Novo V3:** Num: -5 + (100/2) + (95/1) = 140. *(Veja que já usa o V2 atualizado)*. Denom: (1/2) + (1/1) = 1.5. Novo V3 = 140 / 1.5 = **93.33 V**.

**Convergência (Milésima Iteração):**

* [x] Ao parar, o código precisa cravar exatamente em: **V2 = 90.00 V** e **V3 = 90.00 V**.

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: Operador de Rede (main.py e construtor_rede.py)**

* **Responsabilidade:** Menus e montagem da topologia.  
* **Desafio:** Impedir que o usuário crie um fio interligando uma barra que não foi cadastrada.

### **2️⃣ Aluno 2: O Gênio Matemático (solver_iterativo.py)**

* **Responsabilidade:** O motor while do método Gauss-Seidel.  
* **Desafio:** Lógica densa de laços for vasculhando quem são os "vizinhos" de quem na lista, somando os numeradores e denominadores, e parando no critério de 0.001.

### **3️⃣ Aluno 3: Arquiteto de Grafos POO (entidades_poo.py)**

* **Responsabilidade (AV2):** Classes Barra e Linha.  
* **Desafio:** Instanciar tudo nas listas da memória (lista_barras = []), guardando status de tensão atual e corrente injetada.

### **4️⃣ Aluno 4: Analista de Perdas (relatorios.py)**

* **Responsabilidade:** Relatórios visuais.  
* **Desafio:** Rodar a fórmula das perdas, desenhar a tabela final e exibir alertas de [SUBTENSÃO] em vermelho (usando os códigos de cor do terminal, se possível) se a barra ficar abaixo de 93V.

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Prova Numérica**

* **Foco:** Laços while/for e Lógica Matemática Pura.  
* **Entrega:** Código "hardcoded" (lista fixa) resolvendo apenas a Rede do Teste de Mesa. O programa roda e imprime "Iteração 1.. 2..", até imprimir a tela final "Convergiu!". Se mostrar os 90.00 V, está aprovado.

### **🚩 Milestone 2 (AV2 - Semana 13): O Simulador Flexível**

* **Foco:** POO e Validação de Grafos.  
* **Entrega:** Sistema dinâmico construído via Menu. O usuário cria quantas barras quiser, puxa os fios entre elas e o algoritmo resolve no ato. Relatório visual exibe as perdas por fio.

💡 *Dica:* Usem a função abs() do Python (Valor Absoluto) na hora de testar a Condição de Parada do erro, senão a oscilação entre negativos e positivos travará o seu while num Loop Infinito!