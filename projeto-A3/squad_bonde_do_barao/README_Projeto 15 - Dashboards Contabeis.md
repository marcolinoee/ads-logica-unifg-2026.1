<h1 align="center">📊 Projeto 15: Motor Analítico de Demonstrações Contábeis</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/An%C3%A1lise_Financeira-85BB65%3Fstyle%3Dfor-the-badge%26logo%3Dcashapp%26logoColor%3Dwhite" alt="Finance Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 15!** Como os robôs de Wall Street decidem em quais empresas investir? Eles usam Árvores de Decisão baseadas em demonstrações contábeis. Neste projeto final, você construirá um conselheiro financeiro automatizado, dominando matrizes e milhares de regras condicionais.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Toda empresa publica anualmente sua saúde financeira. O **Balanço Patrimonial** mostra o que a empresa tem e o que deve. A **DRE** (Demonstração do Resultado) mostra se deu lucro.

Analisar isso tudo de forma manual é lento. Fundos de investimento usam algoritmos para fazer "Análise Fundamentalista" instantânea, cruzando contas para saber: a empresa vai falir mês que vem? A dívida dela estourou? A rentabilidade é boa?

🎯 **A Missão:** Construir um robô de terminal. Ele irá ingerir balanços contábeis, cruzar os dados usando fórmulas padrão de mercado, e acionar Árvores de Decisão (if/elif/else) para "escrever" relatórios automáticos sobre a saúde e evolução da empresa.

## **🧮 2. Regras de Negócio e Indicadores**

### **⚖️ 2.1. Validação de Ouro (Proteção)**

* A primeira regra contábil é intransigente. Se a matemática não fechar, recuse a entrada.  
* Ativo_Total == Passivo_Total + Patrimonio_Liquido

### **💧 2.2. Liquidez (Risco de Quebra)**

Capacidade de pagar contas imediatas.

* **Liq. Corrente:** Ativo_Circulante / Passivo_Circulante. *(Alerta Crítico se < 1.0)*.  
* **Liq. Seca:** (Ativo_Circulante - Estoques) / Passivo_Circulante.

### **💳 2.3. Endividamento**

* **Endiv. Geral:** (Passivo_Circulante + Pass_Nao_Circulante) / Ativo_Total. *(Risco extremo se > 0.8 / 80%)*.

### **💰 2.4. Rentabilidade**

* **Margem Líquida:** Lucro / Receita. *(Alerta de Prejuízo se < 0)*.  
* **ROE:** Lucro / Patrimonio_Liquido. *(Ótimo se > 0.20)*.

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: Indústria Pé Firme (Ano 2025)**

* **Ativos:** Circulante (150k), Estoque (50k), Não-Circ. (150k) = **Total 300k**.  
* **Passivos:** Curto (100k), Longo (50k) = **Total 150k**.  
* **Patr. Líquido:** 150k. | **Receita:** 500k. | **Lucro:** 50k.

**Passo a passo da Validação:**

* [x] **A = P + PL?** 300k == 150k + 150k (Aprovado).  
* [x] **Liq. Corrente:** 150k / 100k = **1.50** (Folga).  
* [x] **Liq. Seca:** 100k / 100k = **1.00**.  
* [x] **Endividamento:** 150k / 300k = **0.50 (50%)**.  
* [x] **Margem Líquida:** 50k / 500k = **0.10 (10%)**.  
* [x] **ROE:** 50k / 150k = **0.33 (33%)**.

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: O Auditor (main.py e ingresso_dados.py)**

* **Responsabilidade:** Formulários de input anual.  
* **Desafio:** Implementar o loop defensivo da Validação de Ouro. Se o balanço não bater, impedir o cadastro e forçar a redigitação com alerta vermelho.

### **2️⃣ Aluno 2: Analista Quantitativo (motor_indices.py)**

* **Responsabilidade:** As fórmulas matemáticas da Seção 2 e o Motor de Decisão.  
* **Desafio:** Proteger o código contra Divisão por Zero (ZeroDivisionError) e encadear os milhares de if/elif que retornam as mensagens em texto (os conselhos).

### **3️⃣ Aluno 3: Arquiteto Contábil POO (banco_poo.py)**

* **Responsabilidade (AV2):** Classe DemonstracaoAnual e Classe Empresa.  
* **Desafio:** A classe DemonstracaoAnual (que representa 1 ano) deve ser armazenada em uma lista temporal da empresa (self.historico = []).

### **4️⃣ Aluno 4: O Criador de Dashboards (painel_evolutivo.py)**

* **Responsabilidade:** A temida Análise Horizontal.  
* **Desafio:** Varrer a lista histórica, comparar o ano "N" com o "N-1". Calcular a variação percentual do Lucro e emitir uma mega tabela visual com as tags verdes de [CRESCIMENTO] ou vermelhas de [QUEDA].

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Calculadora Robusta**

* **Foco:** Try/Except, If/Elif em profusão, Aritmética.  
* **Entrega:** Sistema de via única sem POO. Pergunta 1 ano isolado, testa a Regra de Ouro, e imprime o laudo financeiro textual. Teste de mesa é a base de correção.

### **🚩 Milestone 2 (AV2 - Semana 13): O Conselheiro Temporal**

* **Foco:** POO e Manipulação Avançada de Vetores/Listas.  
* **Entrega:** Sistema ganha história. O usuário cadastra de 2023 a 2025 (guardados em objetos instanciados). O Aluno 4 aciona seu módulo e exibe o Raio-X evolutivo comparando a saúde da empresa ao longo do tempo.

💡 *Dica:* A variação percentual de dois anos na Análise Horizontal é calculada pela fórmula ((Ano_Novo / Ano_Velho) - 1) * 100. O Aluno 4 deve ter muito cuidado na varredura da lista usando len() para não cruzar o limite do índice.