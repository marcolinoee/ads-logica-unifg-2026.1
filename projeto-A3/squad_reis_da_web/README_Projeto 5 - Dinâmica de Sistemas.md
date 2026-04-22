<h1 align="center">🏙️ Projeto 5: Simulador de Dinâmica de Sistemas (SimCity Texto)</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Simula%C3%A7%C3%A3o-2E8B57%3Fstyle%3Dfor-the-badge%26logo%3Dchart-line%26logoColor%3Dwhite" alt="Simulation Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 5!** Vocês irão construir a "Engine" de um jogo de simulação. Preparem-se para trabalhar com *Game Loops*, equações de diferença e gerenciamento de estado, onde cada decisão do usuário afeta o futuro da cidade.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Prefeitos e governadores usam a **Modelagem de Sistemas** para prever o futuro. Se a população cresce, o consumo de água sobe. Se construirmos usinas a carvão, a energia sobe, mas a poluição também, o que aumenta a mortalidade. É um ecossistema matemático interligado.

🎯 **A Missão:** Construir um simulador em modo texto. O jogador toma decisões de investimento e avança de ano em ano. Se a população zerar: *Game Over*. Se sobreviver 50 anos: *Vitória*.

## **🧮 2. A Física do Jogo (Equações Iterativas)**

### **👥 2.1. Demografia**

* **Natalidade:** 5% (0.05). **Mortalidade:** 2% (0.02).

Nova_Populacao = Pop_Atual + (Pop_Atual * 0.05) - (Pop_Atual * 0.02)  
# Obrigatório usar int() para habitantes.

### **💵 2.2. Economia**

* Cada cidadão paga R$ 10 de impostos/ano.  
* Caixa = Caixa + (Populacao * 10) - Manutencao_Obras

### **⚡ 2.3. Infraestrutura e Crise**

* **Consumo:** 2 kWh/hab e 3 L d'água/hab.  
* **Crise:** Se Demanda Água > Capacidade -> Dobra a Taxa de Mortalidade. Se faltar Energia -> Arrecadação cai pela metade.

### **🏭 2.4. Poluição**

* Cumulativa. Acima de 1.000 pontos, mata 10% da população. Construir "Hospitais" anula os efeitos mortais.

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário: Virada do Ano 1 para o Ano 2**

* **Estado Ano 1:** Pop: 1.000 | Caixa: R$ 50.000 | Obras: 1 Usina Carvão (5k kWh, +50 poluição), 1 Água (10k L).  
* **Ação:** Nenhuma construção. Avançar ano.

**Passos calculados pelo código:**

* [x] **Poluição:** +50 (Usina a carvão). Total = 50.  
* [x] **Arrecadação:** 1000 * 10 = R$ 10.000. Caixa = R$ 60.000.  
* [x] **Demandas OK:** 2000 kWh (Menor que 5000), 3000 L (Menor que 10000).  
* [x] **População Ano 2:** +50 - 20 = **1.030 habitantes**.

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: Game Loop (main.py e game_loop.py)**

* **Responsabilidade:** Loop infinito while ano_atual <= 50:. Menu de ações ("Construir Usina", "Avançar Ano").  
* **Desafio:** Lógica de bloqueio financeiro (if caixa >= custo_obra).

### **2️⃣ Aluno 2: Motor da Física (fisica_simulacao.py)**

* **Responsabilidade:** Função processar_ano().  
* **Desafio:** A cascata de condicionais (if crise hídrica, elif poluição). Todas as fórmulas da Seção 2.

### **3️⃣ Aluno 3: POO e Entidades (entidades_poo.py)**

* **Responsabilidade (AV2):** Classes Cidade, Usina, Hospital.  
* **Desafio:** A cidade terá listas (ex: self.usinas = []). Para calcular energia total, deve fazer um for somando a produção de cada objeto Usina.

### **4️⃣ Aluno 4: Gráficos ASCII (analytics_graficos.py)**

* **Responsabilidade:** Salvar histórico (arrays/listas) ano a ano.  
* **Desafio:** Plotar gráficos no terminal baseados no histórico:  
  Ano 1: [1000 hab] ##########

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Game Loop Matemático**

* **Foco:** While, Variáveis e Equações.  
* **Entrega:** O jogo roda iterativamente. Não salva histórico nem usa POO. Aplica a matemática hardcoded. Se os números do teste de mesa baterem, o laço temporal está aprovado.

### **🚩 Milestone 2 (AV2 - Semana 13): O Ecossistema**

* **Foco:** POO e Matrizes/Vetores.  
* **Entrega:** Cidade instanciada como Objeto. Histórico salvo. Aluno 4 apresenta painéis e gráficos ASCII mostrando a evolução (ou decadência) da cidade.

💡 *Dica:* Usem a instrução os.system('cls' if os.name == 'nt' else 'clear') (importando os) no início do Game Loop para limpar o console a cada ano e dar cara de Jogo!