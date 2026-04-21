<h1 align="center">⚙️ Projeto 12: Parametrização de Máquinas Elétricas</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Eng_El%C3%A9trica-000080%3Fstyle%3Dfor-the-badge%26logo%3Dlightning%26logoColor%3Dwhite" alt="Electrical Engineering Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 12!** Este é um laboratório virtual. Vocês construirão um sistema capaz de simular o comportamento de um Motor de Indução Trifásico (MIT), plotando a curva de "Torque vs Velocidade" utilizando laços de repetição densos.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Motores elétricos não giram perfeitamente na velocidade teórica do campo magnético; eles sofrem um "escorregamento". Se você colocar peso demais (carga), o motor trava e queima. Para evitar desastres, engenheiros desenham a curva do motor e encontram seu limite máximo.

🎯 **A Missão:** Construir um simulador que recebe dados de placa do motor e, através de um laço for ou while, calcula a força (Torque) do motor em diversas faixas de rotação (RPM), exibindo um gráfico ASCII no terminal.

## **🧮 2. Regras de Negócio e Fórmulas Matemáticas**

### **🔄 2.1. Velocidade Síncrona (Ns)**

* **Regra:** O número de polos (P) **obrigatoriamente** tem que ser par e positivo (2, 4, 6...). Bloquear ímpares.  
* Ns = (120 * Frequencia) / P

### **📉 2.2. Escorregamento (s)**

A diferença entre a teórica (Ns) e a real (N).

* Escorregamento = (Ns - N) / Ns

### **💪 2.3. Torque (Fórmula de Kloss)**

A força do motor depende do escorregamento atual e do escorregamento máximo (s_max).

* Torque_Atual = (2 * Torque_Maximo) / ( (s / s_max) + (s_max / s) )  
* **Exceção Matemática:** Se N == Ns, o escorregamento é 0 e a divisão quebrará. Use um if para definir que neste caso o Torque_Atual = 0.

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: Motor Genérico**

* **Rede:** 60 Hz | **Polos:** 4  
* **Torque Máx:** 150 Nm | **s_max:** 0.20 (20%)

**Passo a passo da Validação:**

* [x] **Velocidade Síncrona:** (120 * 60) / 4 = **1800 RPM**.  
* [x] **Validação Rotação 1440 RPM:**  
  * s = (1800 - 1440) / 1800 = **0.20**.  
  * Torque = (2 * 150) / ((0.20/0.20) + (0.20/0.20)) = 300 / 2 = **150 Nm**. *(Faz sentido, pois bateu com o s_max).*  
* [x] **Validação Rotação 1710 RPM:**  
  * s = (1800 - 1710) / 1800 = **0.05**.  
  * Torque = (2 * 150) / (0.25 + 4.0) = 300 / 4.25 = **70.58 Nm**.

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: Técnico de Laboratório (main.py e inputs.py)**

* **Responsabilidade:** Menus e formulário da placa do motor.  
* **Desafio:** Loop defensivo while para garantir que os Polos do motor sejam números inteiros pares maiores que zero.

### **2️⃣ Aluno 2: Motor Matemático (fisica_maquinas.py)**

* **Responsabilidade:** Transformar as fórmulas de Ns, Escorregamento e Torque em funções puras.  
* **Desafio:** Prevenir a divisão por zero programaticamente dentro das funções da fórmula de Kloss.

### **3️⃣ Aluno 3: Arquivista POO (motores_poo.py)**

* **Responsabilidade (AV2):** A classe MotorInducao.  
* **Desafio:** O método __init__ já deve chamar automaticamente a função do Aluno 2 para calcular o Ns e guardar dentro do objeto no momento da criação. Manter banco de motores.

### **4️⃣ Aluno 4: Interface de Gráficos (plotagem_ascii.py)**

* **Responsabilidade:** Gerar a "Curva de Torque" em lote.  
* **Desafio:** Construir um loop (for N in range(...)) que varie de 0 até Ns, chame o Aluno 2 para calcular o Torque e desenhe uma barra proporcional (ex: RPM: 1440 | Torque: 150 Nm | ###############).

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Validação Numérica**

* **Foco:** Funções e Estruturas Condicionais Básicas.  
* **Entrega:** Script simples. Pede dados de um motor. Testa se polos são pares. Pede para o usuário digitar *uma* rotação qualquer e cospe o Torque e Escorregamento exatos do Teste de Mesa.

### **🚩 Milestone 2 (AV2 - Semana 13): O Plotter de Curvas**

* **Foco:** POO e Laços Massivos.  
* **Entrega:** Motores instanciados na memória. O usuário clica em "Gerar Curva" e o Aluno 4 usa o laço de repetição para calcular e desenhar instantaneamente as dezenas de pontos matemáticos formatados no console.