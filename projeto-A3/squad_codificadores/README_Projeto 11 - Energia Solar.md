<h1 align="center">☀️ Projeto 11: Simulador de Dimensionamento Fotovoltaico</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Eng_Solar-FFB600%3Fstyle%3Dfor-the-badge%26logo%3Dsun%26logoColor%3Dblack" alt="Solar Engineering Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 11!** Com o aumento do custo da eletricidade, a energia solar virou uma necessidade. Neste projeto, a sua equipe criará uma plataforma de orçamentação e engenharia que dimensiona sistemas solares (On-Grid e Off-Grid) baseado em variáveis de consumo e dados climáticos.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

Para saber quantas placas solares vão no telhado, o engenheiro não pode "chutar". Ele precisa do consumo do cliente, do índice climático de incidência solar (HSP - Horas de Sol Pleno) e da eficiência do sistema. Se o sistema for para uma fazenda (Off-Grid), ele precisará ainda calcular a capacidade do banco de baterias.

🎯 **A Missão:** Construir o algoritmo que recebe a conta de luz do cliente, calcula a Potência de Pico (kWp) necessária, descobre a quantidade de painéis arredondada para cima e emite uma proposta comercial indicando o retorno do investimento (Payback).

## **🧮 2. Regras de Negócio e Cálculos**

### **⚡ 2.1. Cálculo da Potência (kWp)**

* **Consumo Diário:** Consumo_Mensal_kWh / 30.  
* **Perdas:** O sistema tem uma eficiência global de 80% (0.80).  
* **Potência Pico:** Pot_Pico_kWp = Consumo_Diario / (HSP * 0.80)

### **🧮 2.2. Quantidade de Painéis**

* Converter painel para kW (ex: 550W = 0.55 kW).  
* Qtd_Paineis = Pot_Pico_kWp / Potencia_Painel_kW  
* **Arredondamento:** Não se vende meia placa. Se o cálculo der 6.2, arredonde para 7. *(Desafio: usar lógica com int() sem importar bibliotecas extras)*.

### **🔋 2.3. Banco de Baterias (Apenas Off-Grid)**

* Para o sistema isolado, com Autonomia (ex: 2 dias) e Baterias que não podem descarregar 100% (Profundidade de Descarga = 0.80).  
* Capacidade_Ah = (Consumo_Diario * 1000 * Autonomia) / (Tensao_Sistema_V * 0.80)

## **🧪 3. Exemplo Prático (Teste de Mesa)**

**Cenário de Teste: Casa na Cidade (On-Grid)**

* **Consumo:** 360 kWh/mês | **HSP Local:** 5.0 horas  
* **Placa Escolhida:** 500W (R$ 800 cada)  
* **Outros Custos:** Inversor (R$ 3.000) | Mão de Obra (R$ 2.000) | Tarifa da rua: R$ 1,00/kWh

**Passo a passo da Validação:**

* [x] **Consumo Diário:** 360 / 30 = **12 kWh/dia**.  
* [x] **Potência Pico:** 12 / (5.0 * 0.80) = 12 / 4 = **3.0 kWp**.  
* [x] **Quantidade de Placas:** 3.0 / 0.5 = **6 placas exatas**.  
* [x] **Custo Total:** (6 * 800) + 3000 + 2000 = **R$ 9.800,00**.  
* [x] **Economia Mensal:** 360 * 1.00 = **R$ 360,00**.  
* [x] **Payback:** 9800 / 360 = **27.2 meses** (~2 anos e 3 meses).

## **👨‍💻 4. Divisão de Trabalho no GitHub**

### **1️⃣ Aluno 1: O Vendedor / Coletor (main.py e crm.py)**

* **Responsabilidade:** Menus e formulários.  
* **Desafio:** Blindar o formulário. Não permitir inserir consumo negativo e calcular a média dos 12 meses usando um laço for.

### **2️⃣ Aluno 2: Engenheiro Calculista (motor_solar.py)**

* **Responsabilidade:** Transformar as equações da Seção 2 em funções.  
* **Desafio:** A lógica matemática de arredondamento para cima e prever a não-divisão por zero.

### **3️⃣ Aluno 3: Almoxarifado POO (catalogo_poo.py)**

* **Responsabilidade (AV2):** Classes PainelSolar, Inversor, Bateria.  
* **Desafio:** Montar um catálogo na memória (lista de objetos) para o usuário escolher o modelo dinamicamente e a função do Aluno 2 conseguir acessar o painel.potencia.

### **4️⃣ Aluno 4: Analista de Contratos (proposta.py)**

* **Responsabilidade:** Impressão do orçamento.  
* **Desafio:** Montar a Proposta Comercial em ASCII com formatação de strings e alinhamento de colunas (f"{texto:<20}"), parecendo um Ticket impresso.

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): Cálculo Bruto**

* **Foco:** Funções em cascata e conversões aritméticas.  
* **Entrega:** Sistema sem baterias (sem Off-Grid). Recebe valores brutos pelo terminal e "cospe" a quantidade de placas e o payback. O teste de mesa deve bater exatamente.

### **🚩 Milestone 2 (AV2 - Semana 13): Sistema Comercial Completo**

* **Foco:** POO e Condicionais If/Else (Rotas do programa).  
* **Entrega:** O sistema pergunta se é On-Grid ou Off-Grid. Se for Off, puxa a rotina extra de baterias. O catálogo funciona via Objetos e a Proposta Comercial sai visualmente formatada.

💡 *Dica:* A conversão de kW para W (e vice-versa) é onde 90% dos erros acontecem. Fiquem atentos às ordens de grandeza!