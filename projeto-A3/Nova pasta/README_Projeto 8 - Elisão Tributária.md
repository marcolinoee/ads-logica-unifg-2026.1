<h1 align="center">⚖️ Projeto 8: Planejamento e Elisão Tributária</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Tribut%C3%A1rio-B22222%3Fstyle%3Dfor-the-badge%26logo%3Dscales%26logoColor%3Dwhite" alt="Tax Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 8!** A escolha do regime de impostos errado pode falir uma empresa. Vocês construirão um poderoso Motor de Cálculo Legal que resolve tudo através da força bruta algorítmica: testar todos os cenários e recomendar o mais barato.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

As empresas podem escolher entre 3 regimes: **Simples Nacional**, **Lucro Presumido** e **Lucro Real**. A prática de simular a lei para pagar menos imposto de forma lícita chama-se **Elisão Fiscal**.

🎯 **A Missão:** O sistema receberá os dados anuais da empresa. Em milissegundos, calculará o imposto nos 3 regimes simultaneamente e emitirá um laudo recomendando a opção mais barata, exibindo a economia gerada.

## **🧮 2. Regras de Negócio e Cálculos**

### **🏷️ 2.1. O Simples Nacional (Faixas Múltiplas)**

Calculado com base em faixas (If/Elif pesados).

* Imposto = (Faturamento * Alíquota) - Parcela_a_Deduzir  
* *Faixa 3:* (Ex: 360k a 720k) -> Alíquota: 9.5% | Parcela: R$ 13.860.  
* *Faixa 5:* (Ex: 1.8M a 3.6M) -> Alíquota: 14.3% | Parcela: R$ 87.300.

### **💼 2.2. Lucro Presumido**

Presume-se que o lucro foi de 8% do Faturamento.

* Base_Presumida = Faturamento * 0.08  
* IRPJ = Base * 0.15 | CSLL = Base * 0.09  
* PIS/COFINS = Faturamento * 0.0365

### **🏢 2.3. Lucro Real**

Imposto sobre o que realmente sobrou.

* Lucro_Real = Faturamento - Folha_Salarial - Despesas  
* **Condicional Especial:** Se Lucro_Real <= 0 (Prejuízo), o IRPJ e CSLL dão **ZERO**.  
* PIS/COFINS (Abatendo despesas): (Faturamento - Despesas) * 0.0925

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: Indústria ABC**

* **Faturamento:** R$ 2.000.000,00  
* **Folha Salarial:** R$ 300.000,00  
* **Despesas Dedutíveis:** R$ 1.500.000,00

**Passo a passo da Validação:**

* [x] **Simples Nacional (Faixa 5):** (2.000.000 * 0.143) - 87.300 = **R$ 198.700,00**  
* [x] **Lucro Presumido:** - Base = 160k. IRPJ+CSLL = 38.400. PIS/COFINS = 73.000.  
  * Total = **R$ 111.400,00**  
* [x] **Lucro Real:**  
  * Lucro de Fato = 200k. IRPJ+CSLL = 48.000. PIS/COFINS (sobre 500k) = 46.250.  
  * Total = **R$ 94.250,00**  
* [x] **Decisão:** Lucro Real (Economia de R$ 104.450,00 contra o pior cenário).

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: O Entrevistador (main.py e coleta.py)**

* **Responsabilidade:** Menu interativo de dados.  
* **Desafio:** Validação cruzada (ex: A Folha + Despesas não pode ser absurdamente maior que o faturamento se a empresa declarou não ter prejuízo). Arredondamentos adequados (round(valor, 2)).

### **2️⃣ Aluno 2: Contador Nível 1 (simples_presumido.py)**

* **Responsabilidade:** Engine do Simples e Presumido.  
* **Desafio:** O bloco colossal de if/elif do Simples Nacional. Atenção máxima aos limites exatos (ex: <= 360000).

### **3️⃣ Aluno 3: Contador Nível 2 e POO (lucro_real_poo.py)**

* **Responsabilidade:** Matemática do Lucro Real e a Classe Empresa.  
* **Desafio:** Proteger o código de "imposto negativo" caso o lucro real dê prejuízo.

### **4️⃣ Aluno 4: O Auditor Final (auditoria_tributaria.py)**

* **Responsabilidade:** Comparativo visual no terminal.  
* **Desafio:** Encontrar o menor valor da lista calculada e montar uma tabela lado a lado com a economia formatada.

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Cálculo Bruto**

* **Foco:** Condicionais aninhadas (If/Elif/Else) e Funções.  
* **Entrega:** Script puramente procedural. Digita-se 1 empresa, e o código "cospe" os 3 resultados na tela apontando o menor. O teste de mesa deve bater centavo por centavo.

### **🚩 Milestone 2 (AV2 - Semana 13): Auditoria em Lote**

* **Foco:** POO e Laços de Coleção.  
* **Entrega:** Cadastro de N empresas via objetos. O sistema gera uma "Auditoria em Lote", varrendo a lista e exibindo uma mega-tabela recomendando os regimes para a carteira inteira de clientes.

💡 *Dica:* Na engine do Simples Nacional, usem o formato de condicionais contínuas do Python (if 180000 < faturamento <= 360000:) para o código ficar mais elegante!