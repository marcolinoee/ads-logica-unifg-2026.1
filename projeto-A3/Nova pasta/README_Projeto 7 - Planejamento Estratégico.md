<h1 align="center">🎯 Projeto 7: Simulador de Planejamento Estratégico (SWOT & GUT)</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Estrat%C3%A9gia-FF8C00%3Fstyle%3Dfor-the-badge%26logo%3Dtarget%26logoColor%3Dwhite" alt="Strategy Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 7!** A Diretoria da empresa precisa de você. Em vez de tomar decisões baseadas em "achismos", vocês criarão um software gerencial que mapeia o cenário da empresa e cria um ranking matemático dos maiores problemas a serem resolvidos.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

A jornada padrão de consultoria empresarial funciona em passos:

1. **O Diagnóstico (Matriz SWOT):** Mapear Forças, Fraquezas, Oportunidades e Ameaças.  
2. **A Priorização (Matriz GUT):** A empresa não tem dinheiro para resolver tudo. A Matriz GUT classifica os problemas dando notas para **G**ravidade, **U**rgência e **T**endência, criando um ranking matemático do que deve ser apagado primeiro.

🎯 **A Missão:** Desenvolver um software de terminal que conduz o gestor por essa jornada, filtra os problemas, calcula os pesos e exibe o ranking final de prioridades ordenado.

## **🧮 2. Regras de Negócio e Cálculos**

### **🔍 2.1. O Diagnóstico SWOT**

O sistema cadastra fatores com:

* Nome (ex: "Concorrente novo").  
* Categoria (1. Força, 2. Fraqueza, 3. Oportunidade, 4. Ameaça).  
* Impacto (Nota de 1 a 5).

### **🚨 2.2. O Motor de Priorização (Matriz GUT)**

O sistema deve filtrar a lista geral e separar **apenas Fraquezas e Ameaças**. Para cada problema, pede-se notas de 1 a 5 para:

* **Gravidade (G):** Qual o impacto se nada for feito?  
* **Urgência (U):** Quanto tempo temos para agir?  
* **Tendência (T):** Se não fizermos nada, vai piorar rápido?

Score_GUT = Gravidade * Urgencia * Tendencia

### **📊 2.3. Algoritmo de Ordenação**

O motor lógico deve pegar a lista de scores calculados e **ordená-la de forma decrescente** (do maior para o menor).

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: Diagnóstico da Empresa**

* **Problema 1:** Software lento (G=4, U=5, T=4)  
* **Problema 2:** Falta de café (G=1, U=2, T=1)  
* **Problema 3:** Novo concorrente (G=5, U=3, T=5)

**Passo a passo da Validação:**

* [x] **Score P1:** 4 * 5 * 4 = **80 pontos**.  
* [x] **Score P2:** 1 * 2 * 1 = **2 pontos**.  
* [x] **Score P3:** 5 * 3 * 5 = **75 pontos**.  
* [x] **Ordenação do Algoritmo (Saída Esperada):**  
  1. Software lento (80 pts)  
  2. Novo concorrente (75 pts)  
  3. Falta de café (2 pts)

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: O Pesquisador (main.py e formularios.py)**

* **Responsabilidade:** Menus e captura de dados.  
* **Desafio:** Validação defensiva (while True com try/except). Se pede nota de 1 a 5 e o usuário digita "A", travar o erro e pedir novamente.

### **2️⃣ Aluno 2: Cientista de Dados (motor_priorizacao.py)**

* **Responsabilidade:** Matemática da GUT e filtros.  
* **Desafio:** Como pegar uma lista misturada e criar uma sublista só com os problemas? Depois, aplicar a ordenação (.sort(reverse=True)).

### **3️⃣ Aluno 3: Estruturas (entidades_poo.py)**

* **Responsabilidade (AV2):** Classes FatorEstrategico e ProblemaGUT.  
* **Desafio:** Trabalhar com heranção básica ou composição. Salvar instâncias numa lista da memória do sistema.

### **4️⃣ Aluno 4: Painel Executivo (painel_ascii.py)**

* **Responsabilidade:** Relatórios visuais no terminal.  
* **Desafio:** Desenhar a Matriz SWOT formatada em 4 quadrantes (requer domínio de fatiamento e alinhamento de strings como .ljust()). Sinalizar com tag [CRÍTICO] se o Score GUT > 80.

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): A Calculadora GUT**

* **Foco:** Laços for e lógica condicional.  
* **Entrega:** Script sem POO. Um laço roda N vezes perguntando o nome e as 3 notas. O sistema calcula e já exibe na hora a classificação (Crítico, Alto, Médio, Baixo).

### **🚩 Milestone 2 (AV2 - Semana 13): O Software Gerencial**

* **Foco:** POO e Algoritmos de Ordenação.  
* **Entrega:** Sistema completo. O usuário cadastra todo o ambiente. O Aluno 2 processa a ordenação dos objetos e o Aluno 4 desenha a matriz em cruzamento na tela do terminal.

💡 *Dica:* Na hora de desenhar a Matriz em 4 quadrantes, lembrem-se que o print() escreve linha por linha. Vocês terão que imprimir a Linha 1 das "Forças" acompanhada da Linha 1 das "Fraquezas" na mesma string!