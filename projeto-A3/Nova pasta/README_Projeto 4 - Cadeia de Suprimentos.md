<h1 align="center">📦 Projeto 4: Simulador de Cadeia de Suprimentos (MRP/PEPS)</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Log%C3%ADstica-FF4500%3Fstyle%3Dfor-the-badge%26logo%3Dtruck%26logoColor%3Dwhite" alt="Logistics Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 4!** Este é um dos desafios algorítmicos mais ricos do semestre. Vocês construirão o motor logístico de um armazém, garantindo que produtos não vençam nas prateleiras (PEPS) e classificando o valor do estoque (Curva ABC).

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Redes de supermercados perdem milhões porque lotes velhos ficam esquecidos no fundo da prateleira. Sistemas usam o algoritmo **PEPS (Primeiro que Entra, Primeiro que Sai)**.

Além disso, um armazém tem milhares de itens. Para saber o que é mais importante, usa-se a **Curva ABC**: separa-se os produtos que representam muito dinheiro (Classe A) dos baratos e menos vitais (Classe C).

## **🧮 2. Regras de Negócio e Cálculos**

### **🛒 2.1. Algoritmo PEPS (Baixa Fracionada)**

* O sistema deve **esvaziar os lotes antigos primeiro**.  
* *Exemplo:* Venda de 40 caixas. Lote Velho tem 30. Lote Novo tem 50. O código deve dar baixa de 30 no Velho (zerar) e tirar 10 do Novo.

### **🚨 2.2. Ponto de Pedido**

* Após cada venda: Se Estoque_Total < Estoque_Minimo, emitir alerta visual.

### **💰 2.3. Curva ABC (Regra Simplificada)**

* Valor_Estoque = Qtd_Total * Custo_Unitario.  
* O sistema ordena a lista do mais caro para o mais barato.  
* **Classe A:** Itens que somam os primeiros 70% do dinheiro investido.  
* **Classe B:** Próximos 20%. **Classe C:** Últimos 10%.

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário PEPS: Pedido de 65 unidades**

* **Lote 001:** 20 unidades (Mais antigo)  
* **Lote 002:** 50 unidades

**Como seu código (usando while) deve agir:**

* [x] **Iteração 1:** Pedido=65. Pega 20 do Lote 001. Faltam 45. (Zera Lote 001).  
* [x] **Iteração 2:** Pedido=45. Pega 45 do Lote 002. Faltam 0.  
* [x] **Resultado:** Lote 001 Excluído. Lote 002 fica com 5 unidades.

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: Front-end e Compras (main.py e entradas.py)**

* **Responsabilidade:** Loop de Menus e simulação de "Entrada de Nota Fiscal" (cadastrar produtos e novos lotes com data).  
* **Desafio:** Validação de entradas (evitar quantidades negativas).

### **2️⃣ Aluno 2: O Motor PEPS (motor_vendas.py)**

* **Responsabilidade:** A lógica algorítmica pesada das saídas.  
* **Desafio:** Uso de laço while quantidade_pedida > 0: para fazer a dedução fracionada saltando entre índices de lotes diferentes.

### **3️⃣ Aluno 3: Estruturas e ABC (classes_poo.py)**

* **Responsabilidade (AV2):** Criar class Produto com uma lista interna de Lotes.  
* **Desafio extra:** Algoritmo que varre os produtos, ordena pelo valor e atribui a string 'A', 'B' ou 'C'.

### **4️⃣ Aluno 4: Dashboards Textuais (relatorios.py)**

* **Responsabilidade:** Relatórios gerenciais.  
* **Desafios:** Tabela de "Ponto de Pedido" (itens que precisam de compra) e Inventário Geral impresso em colunas ASCII perfeitamente alinhadas.

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Lógica PEPS**

* **Foco:** Laços while aninhados e listas estáticas.  
* **Entrega:** Sistema inicia com 1 produto e 2 lotes fixos no código. O usuário faz uma venda, e o sistema mostra a subtração fracionada (peps) funcionando perfeitamente.

### **🚩 Milestone 2 (AV2 - Semana 13): O ERP Logístico**

* **Foco:** POO e Ordenação.  
* **Entrega:** Múltiplos produtos armazenados via Objetos. Os relatórios ABC e de Ponto de Pedido funcionam para todos os cadastros, navegáveis via menu.

💡 *Dica:* Para excluir um lote que zerou a quantidade, investiguem o uso dos métodos .pop() ou del em listas do Python!