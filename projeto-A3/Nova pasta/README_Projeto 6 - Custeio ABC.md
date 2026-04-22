<h1 align="center">🏭 Projeto 6: Sistema de Custeio Baseado em Atividades (ABC)</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Contabilidade-800000%3Fstyle%3Dfor-the-badge%26logo%3Dcalculator%26logoColor%3Dwhite" alt="Accounting Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 6!** Vocês construirão um poderoso simulador gerencial para as áreas de Engenharia de Produção e Contabilidade. O desafio é usar matrizes, repetições e acumuladores para distribuir centavos e reais de maneira perfeitamente proporcional.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Dividir custos como Aluguel e Energia igualmente por todos os produtos de uma fábrica é injusto (Rateio Simples). O método **ABC (Activity-Based Costing)** resolve isso distribuindo os custos baseado no que o produto *realmente* consumiu (ex: quantas Horas de Máquina ele precisou).

🎯 **A Missão:** Construir um motor matemático de ERP. O sistema cadastrará Produtos e Atividades. O algoritmo deve calcular as "Taxas de Custo" e ratear os valores indiretos produto a produto de forma dinâmica.

## **🧮 2. Regras de Negócio e Cálculos**

### **⚙️ Etapa 1: Custo Direto Unitário**

* Custo fácil de rastrear. Custo_Dir_Total / Quantidade_Produzida

### **📊 Etapa 2: A Taxa do Direcionador**

O custo da atividade dividido por quantas vezes ela foi executada no total.

* Total_Geral = Uso_ProdutoA + Uso_ProdutoB  
* Taxa_Atividade = Custo_da_Atividade / Total_Geral

### **💸 Etapa 3: O Rateio (Cobrando do Produto)**

* Custo_Indireto_do_Produto = Uso_Individual_do_Produto * Taxa_Atividade  
* Custo_Total = Custo_Direto_Total + Custos_Indiretos_Recebidos

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste:**

* **Camiseta:** 1.000 un. | Custo Direto: R$ 5.000 | Uso: 100h-Máquina, 10 Lotes.  
* **Calça:** 500 un. | Custo Direto: R$ 8.000 | Uso: 400h-Máquina, 40 Lotes.  
* **Ativ. 1 (Corte):** Custo R$ 2.000. **Ativ. 2 (Qualidade):** Custo R$ 3.000.

**Passo a passo da Validação:**

* [x] **Taxas:** Corte (500h total) = **R$ 4,00/h**. Qualidade (50 Lotes total) = **R$ 60,00/Lote**.  
* [x] **Rateio Camiseta:** (100h * 4) + (10Lotes * 60) = R$ 1.000 Indireto.  
* [x] **Unitário Camiseta:** (5000 + 1000) / 1000 = **R$ 6,00/un**.  
* [x] **Rateio Calça:** (400h * 4) + (40Lotes * 60) = R$ 4.000 Indireto.  
* [x] **Unitário Calça:** (8000 + 4000) / 500 = **R$ 24,00/un**.

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: Coletores e Interface (main.py e cadastros.py)**

* **Responsabilidade:** Menus e formulários.  
* **Desafio:** A rotina "Lançar Consumo" exige cruzar produtos e atividades já cadastradas, validando a digitação do usuário.

### **2️⃣ Aluno 2: A Máquina de Rateio (motor_rateio.py)**

* **Responsabilidade:** A mágica matemática das etapas 1, 2 e 3.  
* **Desafio:** Laços for aninhados! Um laço varre as atividades e, dentro dele, outro varre os produtos acumulando as somas e multiplicando taxas.

### **3️⃣ Aluno 3: Entidades Contábeis (entidades_poo.py)**

* **Responsabilidade (AV2):** Classes Produto e Atividade.  
* **Desafio:** A classe Produto deve ter um dicionário interno para guardar os usos de cada atividade (ex: self.consumo = {"Corte": 100}).

### **4️⃣ Aluno 4: Relatório DRE (relatorio_dre.py)**

* **Responsabilidade:** Dashboard contábil ASCII.  
* **Desafio:** Matriz de consumo (Produtos nas linhas, Atividades nas colunas) impressa perfeitamente. DRE cruzando preço de venda e custo para exibir Margem de Lucro com alerta [PREJUÍZO] se necessário.

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Motor Matemático**

* **Foco:** Acumuladores em laços e funções.  
* **Entrega:** Script procedural que resolve os números do Teste de Mesa e exibe os R$ 6 e R$ 24 finais. Validado na força bruta das equações.

### **🚩 Milestone 2 (AV2 - Semana 13): O ERP Contábil**

* **Foco:** POO, Dicionários e Tabelas Strings.  
* **Entrega:** Escala dinâmica! Sistema comporta N produtos e M atividades usando objetos. O Aluno 4 exibe a DRE tabulada e limpa.

💡 *Dica:* O uso de Dicionários no Python ({chave: valor}) é a arma secreta do Aluno 2 e 3 para mapear facilmente os nomes das atividades com os valores numéricos de consumo!