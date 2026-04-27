<h1 align="center">🕵️‍♂️ Projeto 10: Auditoria Contábil e Detecção de Fraudes</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/CyberSec-000000%3Fstyle%3Dfor-the-badge%26logo%3Dhackerone%26logoColor%3Dwhite" alt="Cyber Security Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 10!** Como achar 1 nota fiscal falsa em um banco com 10.000 notas? Com força bruta algorítmica e estatística. Vocês construirão um varredor forense que usa a Regra dos 3-Sigmas e a Lei de Benford.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Grandes escândalos financeiros usam adulteração de dados. Auditores utilizam duas malhas finas matemáticas:

1. **Regra dos 3-Sigmas:** Identifica gastos *absurdamente* fora do padrão (Outliers).  
2. **Lei de Benford:** Descobriu-se que, na natureza (e no dinheiro), o número 1 aparece como primeiro dígito em 30% das vezes; o 2 em 17% e assim por diante. Se um humano inventar valores aleatórios (ex: 45.00, 71.00), ele quebra essa lei natural, e o computador descobre a fraude.

## **🧮 2. Regras de Negócio (Estatística "Na Unha")**

Atenção: É **PROIBIDO** o uso de import statistics ou import math. Tudo deve ser feito com acumuladores e laços.

### **📉 2.1. Motor Clássico (Outliers)**

* **Média:** Soma total / Quantidade.  
* **Variância:** A soma do quadrado das diferenças (Valor - Media)**2 dividido pela Quantidade.  
* **Desvio Padrão (DP):** Variancia ** 0.5  
* **Alerta de Fraude:** Se o valor for maior que Média + (3 * DP).

### **🔍 2.2. A Lei de Benford**

* Lógica de Tipagem (Casting): Pegar o valor 450.00, transformar em string "450.00" e puxar a posição [0] (o caractere "4").  
* O sistema deve contar quantos 1, 2, 3 apareceram na primeira posição de todo o lote. Se a % real do 1 fugir violentamente dos ~30% esperados matematicamente, a base está fraudada.

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: O Lote Corrompido**

* **Valores:** 9 notas de 100 e 1 nota falsa de 2.000.  
* [100, 100, 100, 100, 100, 100, 100, 100, 100, 2000]

**Passo a passo da Validação (Outliers):**

* [x] **Média:** 2900 / 10 = **290.0**.  
* [x] **Variância:** A soma das diferenças ao quadrado dá 3.249.000. Dividido por 10 = **324.900**.  
* [x] **Desvio Padrão:** Raiz de 324.900 = **570.0**.  
* [x] **Limite Máximo:** 290 + (3 * 570) = **2.000**. (A nota falsa bateu no teto do desvio permitido!).

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: Coleta de Dados (main.py e entrada.py)**

* **Responsabilidade:** Interface e entrada do Livro Diário.  
* **Desafio:** Criar função que aceite colar uma string enorme 100, 200, 450... e converter numa lista de floats limpa, eliminando valores zeros ou negativos (não existem em Benford).

### **2️⃣ Aluno 2: Estatística Forense (motor_outliers.py)**

* **Responsabilidade:** Média, Variância e Desvio "na unha".  
* **Desafio:** A variância obriga que o laço for passe pela lista duas vezes: uma para descobrir a média e outra para subtraí-la de cada elemento.

### **3️⃣ Aluno 3: Engine Benford e POO (motor_benford.py)**

* **Responsabilidade (AV2):** A extração do 1º dígito e a classe Transacao.  
* **Desafio:** Usar Dicionários ({'1': 0, '2': 0}) para ir acumulando a contagem de cada dígito num laço gigantesco.

### **4️⃣ Aluno 4: Relatório de Compliance (auditoria_viz.py)**

* **Responsabilidade:** O veredito do sistema.  
* **Desafio:** Mostrar apenas os IDs das transações identificadas como fraude (Outliers). Mostrar tabela de Benford formatada lado a lado:  
  Dígito 1 | Esperado: 30.1% | Obtido: 10.0% | MANIPULAÇÃO!

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Estatística Bruta**

* **Foco:** Laços for, Acumuladores e Matemática.  
* **Entrega:** Uso de uma lista pré-chumbada no código. O sistema varre, calcula Variância/DP sem bibliotecas prontas, acha o 3-Sigma e imprime qual o valor estourou a métrica.

### **🚩 Milestone 2 (AV2 - Semana 13): O Scanner Corporativo**

* **Foco:** POO, Cast de Tipos e Dicionários.  
* **Entrega:** Lotes massivos geridos em Objetos. O Aluno 4 entrega a visualização ASCII e os painéis com vereditos automáticos (ex: Base Limpa ou Base Fraudadada).

💡 *Dica:* Lembrem-se que transformar um número em String para pegar o 1º dígito só funciona se o número não tiver casas decimais malucas ou zeros à esquerda. O Aluno 3 vai precisar "limpar" a string mentalmente antes de puxar o índice [0]!