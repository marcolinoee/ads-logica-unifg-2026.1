<h1 align="center">🏭 Projeto 13: Planejamento e Controle da Produção (Mini-MRP)</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Ind%C3%BAstria-8B4513%3Fstyle%3Dfor-the-badge%26logo%3Dcodeigniter%26logoColor%3Dwhite" alt="Industry Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 13!** Vocês construirão o "coração" de fábricas gigantes como a Apple ou a Tramontina. Como explodir um produto em milhares de peças, deduzir o estoque e criar um cronograma de compras sem falhar um parafuso? Este é o mundo do MRP.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Para montar 1.000 iPhones na sexta-feira, o sistema da fábrica não pode pedir baterias na própria sexta, senão a linha de montagem para. O **MRP (Material Requirements Planning)** sabe exatamente a "receita" do produto, subtrai o que já tem no estoque e emite a ordem de compra deslocada no tempo (Lead Time) de acordo com o prazo de entrega do fornecedor.

🎯 **A Missão:** Construir um mini-ERP fabril. Cadastrar a Bill of Materials (Receita), processar um pedido de venda grande, aplicar a lógica de Necessidade Líquida e desenhar a Matriz de Compras cronológica.

## **🧮 2. Regras de Negócio e Cálculos**

### **🧾 2.1. A Árvore (BOM) e Necessidade Bruta**

* A Receita é um Dicionário (Ex: {"Rodinha": 4, "Assento": 1}).  
* Necessidade_Bruta = Demanda_do_Cliente * Qtd_da_Receita.

### **📦 2.2. O Saldo (Necessidade Líquida)**

Não se compra o que já tem na prateleira.

* Necessidade_Liquida = Necessidade_Bruta - Estoque_Atual  
* **Condicional:** Se a Necessidade Líquida for ![][image1] (ou seja, tem estoque sobrando), o sistema precisa pedir 0. Não existem ordens de compra negativas.

### **⏳ 2.3. Lead Time (Deslocamento no Tempo)**

Tempo de espera até o fornecedor entregar.

* **Regra do Vetor:** Se a entrega para o cliente é na Semana 5, e a Peça tem um Lead Time de 2 semanas, o sistema deve registrar a Ordem de Compra na Semana 3.

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: Pedido de 100 Cadeiras para a SEMANA 5**

* **Receita:** 1 Assento, 1 Encosto, 1 Eixo, 5 Rodinhas.  
* **Estoque Atual:** Assento (20), Encosto (0), Eixo (10), Rodinhas (40).  
* **Lead Time:** Assento (1 Sem), Encosto (2 Sem), Eixo (1 Sem), Rodinhas (3 Sem).

**Passo a passo da Validação (O Motor do MRP):**

* [x] **Assentos:** Precisa 100. Estoque 20. Líquido = 80. Semana 5 - 1 = **Comprar 80 na Semana 4**.  
* [x] **Encostos:** Precisa 100. Estoque 0. Líquido = 100. Semana 5 - 2 = **Comprar 100 na Semana 3**.  
* [x] **Eixos:** Precisa 100. Estoque 10. Líquido = 90. Semana 5 - 1 = **Comprar 90 na Semana 4**.  
* [x] **Rodinhas:** Precisa 500 (100 * 5). Estoque 40. Líquido = 460. Semana 5 - 3 = **Comprar 460 na Semana 2**.

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: Diretor Comercial (main.py e plano_mestre.py)**

* **Responsabilidade:** Menu de interação e Pedidos (Qual produto, Qual quantidade, Para qual semana).  
* **Desafio:** Validações de limites de tempo. O projeto considera 8 semanas totais. Impedir que peçam demandas no passado.

### **2️⃣ Aluno 2: Engenheiro de Algoritmos (motor_mrp.py)**

* **Responsabilidade:** A mágica da explosão.  
* **Desafio:** Varrer o dicionário de componentes de um produto usando um laço for. Fazer o cálculo multiplicador, subtrair o estoque com o limite da barreira de zero e devolver os dados para o Aluno 4.

### **3️⃣ Aluno 3: Gerente de Almoxarifado POO (classes_poo.py)**

* **Responsabilidade (AV2):** A classe ProdutoAcabado (contendo o dict de receita) e a classe Componente (contendo estoque e lead_time).  
* **Desafio:** Conectar as instâncias. O Aluno 2 precisará acessar componente_atual.saldo_estoque dinamicamente durante o cálculo.

### **4️⃣ Aluno 4: Relatório de Compras (cronograma_viz.py)**

* **Responsabilidade:** Desenhar o calendário da fábrica.  
* **Desafio:** Montar uma Matriz Tabular (Peças nas Linhas x Semanas nas Colunas). Preencher as quantidades nas semanas corretas de forma alinhada no terminal (usando strings padronizadas).

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Motor de Explosão**

* **Foco:** Dicionários, Laços for e Aritmética.  
* **Entrega:** Script procedural contendo o Teste de Mesa "hardcoded" (em listas). Ele apenas varre a receita, calcula a Necessidade Líquida e imprime frases na tela (ex: "Necessário 460 Rodinhas").

### **🚩 Milestone 2 (AV2 - Semana 13): O ERP Completo**

* **Foco:** POO, Atualização de Objetos e Matrizes Visuais.  
* **Entrega:** Orientação a Objetos ativa. Usuário pede as produções livremente. O Aluno 4 exibe a belíssima matriz semanal em ASCII. Ao confirmar o pedido, o sistema deve abater os saldos de estoque dentro dos objetos Componente.

💡 *Dica:* Na hora de montar a tabela do Cronograma, utilizem uma "Lista de Zeros" (Ex: semanas = [0, 0, 0, 0, 0, 0, 0, 0]) e atualizem apenas o índice da semana correspondente ao Lead Time.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAXCAYAAAAcP/9qAAABVUlEQVR4Xu2UP0vDQBjGU6yCWHCQEEpCLgmImKGDGRwcBHFxbaFj6+bSycVdF8FvINJCv0YXR7+Di34Tn6fcCffSphcE0yEP/Mjl/Z/LJZ7XqNEflKZpQJIkucyy7FD6nRQEwYFSaoIid0T6pRA7AFMSRdGxXtM2kLGl+tfGYRgeIfBJ8wK6MkYKManmI47jjNDOK2wLwu2XeUzs4omeCdaPbE5k3Doh50bzxVpmWL3+JBjiehmMCU4IjG9gwm0lVkVHmVeBOt8rGtNG+svguhq3TTC2YMYB7FLVhBoPpKwx/VYSTt8+BriFc04wRA/mlsZJVZ74V7U1NiqKYpdgS4ZmCBQ79xwGUFVO9QbtECRcgSmSLogMMlJrvmPcn4J3svI73qCW64lHwxEHJfrP9Qr6RMa6qLbGlWT+emh25vt+x3Lmeb4Hx72GU5WCQzYmVpFG26wfKMiMBYWSp78AAAAASUVORK5CYII=>