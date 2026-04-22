<h1 align="center">🧠 Projeto 9: Engine de BI e ETL (Data Science em Texto)</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Data_Science-4169E1%3Fstyle%3Dfor-the-badge%26logo%3Ddataiku%26logoColor%3Dwhite" alt="Data Science Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 9!** Os dados do mundo real são "sujos". Antes de gerar gráficos bonitos, a Engenharia de Dados precisa extrair, limpar e tipar essas informações (Processo ETL). Preparem-se para dominar a manipulação de strings!

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Ao ler um arquivo de vendas, aparecem absurdos: espaços extras (" Notebook "), centavos com vírgula ao invés de ponto (150,00) ou textos onde deveriam ter números ("tres"). Se o sistema tentar calcular isso diretamente, o servidor quebra.

🎯 **A Missão:** Construir um mini *Data Warehouse* no console. O sistema receberá blocos de texto sujos, aplicará tratamento de exceções rigoroso para salvar o que presta, e permitirá consultas de KPIs (Indicadores) com gráficos em ASCII.

## **🧮 2. O Pipeline de Dados (Regras)**

### **📥 2.1. Extract (Extração)**

Receber linhas simulando um arquivo CSV.

* Padrão: Data, Produto, Quantidade, Valor_Unitario, Estado

### **🧹 2.2. Transform (Transformação)**

* **Remover Espaços:** Aplicar .strip() nas bordas.  
* **Corrigir Números:** Onde tem ,00, trocar por .00 (.replace()).  
* **Tratar Exceções:** Ao fazer int() ou float(), o código deve estar blindado por um try/except ValueError. Linhas corrompidas devem ser ignoradas (e um [LOG] de aviso gerado).

### **📈 2.3. Load e Analytics**

* **Receita Bruta:** Somatório de (Qtd * Valor).  
* **Ticket Médio:** Receita / Qtd_Vendas.  
* **Filtro (Queries):** Receita apenas de um estado específico.

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: O Lote Sujo**

1. 10/01, Monitor 24p, 1, 800.50, RJ (Perfeito)  
2. 11/01, Teclado Mecanico , 2, 150,00, SP (Espaço sobrando e vírgula no preço)  
3. 12/01, Mouse, tres, 50.00, MG (Qtd escrita em texto - ERRO)

**Passo a passo da Validação:**

* [x] **Linha 1:** Processada normalmente.  
* [x] **Linha 2:** Espaço cortado, vírgula vira ponto. Convertida com sucesso.  
* [x] **Linha 3:** O try/except detecta erro ao converter "tres" para int. O código avisa: *Linha 3 ignorada*.  
* [x] **Receita Bruta Total:** (1 * 800.50) + (2 * 150.00) = **R$ 1.100,50**

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: Engenheiro de Ingestão (main.py e cli_ingestao.py)**

* **Responsabilidade:** Permitir ao usuário colar várias linhas de texto de uma vez no terminal até digitar "FIM". Enviar o "blocão" de texto para o Aluno 2.

### **2️⃣ Aluno 2: Arquiteto de Limpeza (etl_transformer.py)**

* **Responsabilidade:** A mágica de Strings.  
* **Desafio:** Quebrar o texto em linhas (.split('n')), depois em colunas (.split(',')). Aplicar o try/except linha por linha sem deixar a aplicação parar. Retornar uma matriz limpa.

### **3️⃣ Aluno 3: Modelador POO (data_warehouse.py)**

* **Responsabilidade (AV2):** Em vez de matrizes comuns, mapear para a classe RegistroVenda.  
* **Desafio:** A classe já deve ter um método get_valor_total(self) e os objetos devem residir em uma classe mestre BancoDeDados.

### **4️⃣ Aluno 4: Analista de BI (dashboard_viz.py)**

* **Responsabilidade:** Computar os KPIs através de laços for.  
* **Desafio:** Histograma lateral em ASCII.  
  Exemplo:  
  SP [R$ 300] : ### (1 hashtag = 100 reais)

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): O Filtro Lógico**

* **Foco:** Strings, Métodos nativos e Tratamento de Exceção.  
* **Entrega:** Digita-se 1 linha. O sistema limpa os espaços, converte os tipos e exibe mastigado. Se houver erro numérico, exibe a tratativa sem quebrar.

### **🚩 Milestone 2 (AV2 - Semana 13): O Data Warehouse**

* **Foco:** POO e DataViz ASCII.  
* **Entrega:** Ingestão de dezenas de vendas via objetos. O Aluno 4 assume a tela com o Menu de Consultas e gera os gráficos de barra baseados nos dados limpos.

💡 *Dica:* A função nativa .split(',') transforma uma string imediatamente em uma lista onde cada elemento é uma coluna. Essencial para o Aluno 2!