<h1 align="center">🎓 Projeto 3: ERP Educacional - Gestão e Alocação</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Educa%C3%A7%C3%A3o-4B0082%3Fstyle%3Dfor-the-badge%26logo%3Dbook%26logoColor%3Dwhite" alt="Education Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 3!** Você e sua equipe construirão o sistema nervoso de uma instituição de ensino. O desafio une dois problemas complexos: a alocação de horários (impedindo choques) e o cálculo matricial do diário de classe.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Toda faculdade enfrenta um pesadelo logístico. O Professor João não pode dar aula para duas turmas diferentes na segunda-feira às 08h00. O sistema precisa ter "travas lógicas" para impedir coordenadores de quebrarem regras físicas.

Além disso, o "Diário de Classe" requer o armazenamento de notas de dezenas de alunos, calculando médias com pesos distintos e definindo matematicamente quem passa, quem reprova e quem vai para a Prova Final.

## **🧮 2. Regras de Negócio e Lógica Booleana**

### **📅 2.1. Regras do Validador de Horários**

* **Slots de Tempo:** A semana tem 5 dias e 2 blocos (Manhã/Noite), gerando 10 slots.  
* **Regra 1:** Um professor NÃO pode ter 2 turmas no mesmo Slot.  
* **Regra 2:** Uma turma NÃO pode ter 2 disciplinas no mesmo Slot.  
* **Regra 3:** Limite de carga horária máxima por professor.

### **📝 2.2. Sistema de Notas e Pesos**

* **Pesos:** AV1 (30%), AV2 (30%), AV3 (40%).

Media_Parcial = (AV1 * 0.3) + (AV2 * 0.3) + (AV3 * 0.4)

### **⚖️ 2.3. Regras de Aprovação**

* **Aprovado Direto:** MP >= 7.0  
* **Reprovado Direto:** MP < 4.0  
* **Prova Final:** Se 4.0 <= MP < 7.0.  
  * Cálculo da Final: Media_Final = (MP + PF) / 2. Se >= 5.0 (Aprovado na Final).

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: Diário de Classe**

* **Aluno:** Maria  
* **Notas:** AV1 = 5.0 | AV2 = 6.0 | AV3 = 4.0

**Passo a passo da Validação:**

* [x] **MP:** (5.0 * 0.3) + (6.0 * 0.3) + (4.0 * 0.4) = 1.5 + 1.8 + 1.6 = **4.9**  
* [x] **Status Parcial:** Vai para a **Prova Final**.  
* [x] **Prova Final:** Maria tira 6.5.  
* [x] **Media Final:** (4.9 + 6.5) / 2 = **5.7**  
* [x] **Status Final:** **Aprovada na Final.**

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: A Interface (main.py e menus_interface.py)**

* **Responsabilidade:** Interface de texto e navegação infinita em menu.  
* **Desafio:** Proteções com while e try/except. Se pede nota de 0 a 10 e o usuário digita "doze", avisar o erro sem travar.

### **2️⃣ Aluno 2: Motor de Alocação (motor_alocacao.py)**

* **Responsabilidade:** A lógica de validação de choques.  
* **Desafio:** Uso pesado de for e if/else. Varrer uma lista de aulas cadastradas e verificar o "Slot", "Turma" e "Professor" usando operadores lógicos (and, or).

### **3️⃣ Aluno 3: Matriz do Diário (matriz_diario.py)**

* **Responsabilidade:** Cálculo de Notas em uma Matriz Bidimensional (Lista de Listas).  
* **Desafio:** Laços for aninhados para percorrer a lista de alunos (ex: diario = [["Maria", 5.0, 6.0, 4.0]]), calcular a média de todos e atualizar o status de aprovação.

### **4️⃣ Aluno 4: Entidades POO (entidades_poo.py)**

* **Responsabilidade (AV2):** Transição de listas simples para Classes (Aluno, Professor, Disciplina).  
* **Desafio:** A classe Professor deve ter um método para bloquear a adição de aulas caso a sua carga horária máxima estoure.

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Calculadora e Regras**

* **Foco:** Laços, Condicionais e Precedência Matemática.  
* **Entrega:** Sistema pergunta notas, faz conta ponderada e diz o status. No caso de alocação, uma função estática detecta um choque em aulas pré-chumbadas no código para provar que o if funciona.

### **🚩 Milestone 2 (AV2 - Semana 13): O ERP Completo**

* **Foco:** Listas Bidimensionais e POO.  
* **Entrega:** Instancia alunos na memória. Permite lançar as notas em uma matriz e gera um relatório ASCII em formato de tabela com o status de toda a turma.

💡 *Dica:* Cuidado com a ordem dos operadores na Média Final. O uso correto de parênteses garantirá que o Python faça a soma antes da divisão por 2!