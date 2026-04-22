<h1 align="center">📈 Projeto 2: Plataforma de Gestão de Portfólio de Investimentos</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Finan%C3%A7as-008000%3Fstyle%3Dfor-the-badge%26logo%3Dgoogle-sheets%26logoColor%3Dwhite" alt="Finanças Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 2!** Neste desafio, você e sua equipe construirão o motor de decisão financeira de uma grande empresa. O sistema ajudará a Diretoria a escolher quais projetos aprovar baseado no valor do dinheiro no tempo (VPL) e no orçamento disponível.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Toda empresa possui um orçamento limitado e dezenas de ideias. A equipe de Engenharia quer comprar máquinas (400 mil); a TI quer criar um app (300 mil); o Marketing quer uma campanha (600 mil). Como decidir se o dinheiro não dá para todos?

As empresas usam **Engenharia Econômica**. O princípio básico é: R$ 1.000 hoje valem mais do que R$ 1.000 no futuro.

🎯 **A Missão:** Construir um Mini-ERP para o Diretor Financeiro (CFO). O sistema deve receber propostas, calcular se elas dão lucro real descontando a inflação/taxa de atratividade, e montar o melhor portfólio sem estourar o orçamento.

## **🧮 2. Regras de Negócio e Motor Matemático**

### **💡 2.1. O que é um Projeto?**

* **Investimento Inicial:** Gasto no Ano 0 (Negativo).  
* **Fluxos de Caixa Anuais:** Dinheiro líquido gerado nos Anos 1, 2, 3...  
* **TMA (Taxa Mínima de Atratividade):** Rendimento mínimo exigido pela empresa (ex: 10% ou 0.10).

### **📉 2.2. VPL (Valor Presente Líquido)**

Traz os lucros futuros para o valor de hoje, descontando a TMA.

# A lógica (fazer dentro de um laço FOR iterando pelos anos)  
VPL = -Investimento  
VPL += Fluxo_Ano_1 / (1 + TMA)**1  
VPL += Fluxo_Ano_2 / (1 + TMA)**2

* **Regra:** Se VPL > 0, o projeto é viável. Se < 0, rejeitado.

### **⏱️ 2.3. Payback Simples**

Em qual ano o projeto se paga? Some os fluxos de caixa até que o saldo negativo do investimento vire positivo.

### **🏆 2.4. Índice de Lucratividade (IL)**

Usado para desempate. Projetos com maior IL têm prioridade.

IL = (VPL + Investimento) / Investimento

## **🧪 3. Exemplo Prático (Teste de Mesa)**

Para validar o código, use este cenário:

**Cenário de Teste: Compra de Servidores**

* **Investimento:** R$ 100.000,00 | **TMA:** 10% (0.10)  
* **Fluxos (Ano 1 a 3):** R$ 40.000, R$ 50.000, R$ 60.000

**Passo a passo da Validação:**

* [x] **Desconto Ano 1:** 40000 / (1.10)**1 = **36.363,63**  
* [x] **Desconto Ano 2:** 50000 / (1.10)**2 = **41.322,31**  
* [x] **Desconto Ano 3:** 60000 / (1.10)**3 = **45.078,88**  
* [x] **Soma das Receitas no Presente:** **R$ 122.764,82**  
* [x] **VPL Final:** 122.764,82 - 100.000 = **R$ 22.764,82** *(Aprovado!)*  
* [x] **Payback:** Ano 3.  
* [x] **Índice de Lucratividade (IL):** 122.764,82 / 100.000 = **1,22**

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: A Interface (main.py e interface.py)**

* **Responsabilidade:** Loop principal while True e os menus.  
* **Desafio:** Tratamento de exceções try/except para não aceitar letras onde são esperados números flutuantes. Formatar valores como R$ 100.000,00.

### **2️⃣ Aluno 2: O Motor Financeiro (motor_financeiro.py)**

* **Responsabilidade:** Codificar as funções de VPL, Payback e IL.  
* **Desafio:** A função deve receber uma *lista* com os fluxos e lidar com precisão de casas decimais dinamicamente (1 a N anos).

### **3️⃣ Aluno 3: O Estado e POO (gestao_estado_poo.py)**

* **Responsabilidade (AV2):** Criar a class ProjetoInvestimento.  
* **Desafio:** Atributos (nome, investimento, fluxos, vpl, il). Manter um banco de projetos em uma lista global.

### **4️⃣ Aluno 4: Otimização e Relatórios (otimizacao.py)**

* **Responsabilidade:** O algoritmo de decisão da diretoria (Algoritmo Guloso).  
* **Desafio:** Filtrar projetos com VPL negativo. Ordenar os viáveis pelo maior IL. Subtrair do "Orçamento Global" até o dinheiro acabar e imprimir os aprovados.

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Calculadora Financeira**

* **Foco:** Laços for e funções com potenciação.  
* **Entrega:** Um script que pede o investimento, quantidade de anos e fluxos. Chama as funções do Aluno 2 e imprime o VPL e Payback na tela.

### **🚩 Milestone 2 (AV2 - Semana 13): O Gestor de Portfólio**

* **Foco:** POO e Ordenação de Listas.  
* **Entrega:** Sistema armazena N projetos via objetos. O Aluno 4 analisa a lista, cruza com o Orçamento da empresa e dita quais devem ser feitos.

💡 *Dica:* Na hora de ordenar os projetos pelo IL, pesquisem como usar o método .sort(key=...) em listas de objetos no Python!