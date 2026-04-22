<h1 align="center">⚡ Projeto 1: Sistema Integral de Faturamento e Despacho de Energia</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Eng_El%C3%A9trica-FFD700%3Fstyle%3Dfor-the-badge%26logo%3Dlightning%26logoColor%3Dblack" alt="Eng Eletrica Badge"/>

<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub_Team-181717%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub Badge"/>

</p>

**Bem-vindo(a) ao Projeto 1!** Neste desafio, você e sua equipe assumirão o papel de Engenheiros de Software desenvolvendo o "Cérebro Digital" (backend) de uma concessionária de energia. Preparem-se para aplicar lógica, matemática e versionamento de código no mundo real.

**Público-alvo:** Equipe de 4 alunos (1º Período - Ciência da Computação / ADS)

**Disciplina:** Fundamentos da Programação

## **🌍 1. Contexto da Aplicação (O Problema do Mundo Real)**

No Brasil, a conta de luz que chega às nossas casas não é simplesmente *"Consumo x Preço"*. O setor elétrico possui regras rígidas estipuladas pela ANEEL. O valor final da fatura é composto por:

1. **Consumo de Energia (kWh):** O quanto os aparelhos gastaram no mês.  
2. **TE (Tarifa de Energia):** O custo da energia gerada pelas usinas.  
3. **TUSD (Tarifa de Uso do Sistema de Distribuição):** O custo para transportar a energia pelos fios até o cliente.  
4. **Bandeiras Tarifárias:** Multa/acréscimo aplicado quando os reservatórios estão baixos (termelétricas ligadas).  
5. **Impostos "Por Dentro":** ICMS (Estadual), PIS e COFINS (Federais).  
6. **CIP (Contribuição de Iluminação Pública):** Taxa municipal fixa.

🎯 **A Missão:** O sistema deve ler o consumo do cliente e "cuspir" a conta matemática perfeitamente calculada, além de guardar o histórico de vários clientes ao longo do ano para gerar estatísticas.

## **🧮 2. Regras de Negócio e Motor Matemático**

A equipe responsável pelo motor de cálculo deve programar as funções baseadas *estritamente* nas regras abaixo:

### **💡 2.1. Tabela de Tarifas Base**

A concessionária possui 3 perfis. Cada um paga valores distintos por 1 kWh:

* **Residencial (R):** TE = R$ 0,29 | TUSD = R$ 0,35  
* **Comercial (C):** TE = R$ 0,33 | TUSD = R$ 0,40  
* **Industrial (I):** TE = R$ 0,40 | TUSD = R$ 0,45

Custo_Base = Consumo_kWh * (TE + TUSD)

### **🚩 2.2. Bandeiras Tarifárias**

Cobrado a cada **100 kWh consumidos** (arredonde para baixo usando divisão inteira //).

* **Verde (V):** R$ 0,00 de acréscimo.  
* **Amarela (A):** R$ 1,88 a cada 100 kWh.  
* **Vermelha 1 (V1):** R$ 4,46 a cada 100 kWh.  
* **Vermelha 2 (V2):** R$ 7,87 a cada 100 kWh.

Acrescimo_Bandeira = (Consumo_kWh // 100) * Valor_Bandeira

### **📉 2.3. Cálculo de Impostos ("Por Dentro")**

* **Alíquotas:** ICMS = 18% | PIS = 1.65% | COFINS = 7.6% (Soma = 0.2725 ou 27.25%)  
* **Fórmula:**  
  1. Subtotal = Custo_Base + Acrescimo_Bandeira  
  2. Base_de_Calculo = Subtotal / (1 - 0.2725)  
  3. Total_Impostos = Base_de_Calculo - Subtotal

### **🏙️ 2.4. Iluminação Pública (CIP)**

* **Residencial:** R$ 15,00 | **Comercial:** R$ 40,00 | **Industrial:** R$ 120,00

### **💰 2.5. Total da Fatura**

Fatura_Final = Base_de_Calculo + CIP

## **🧪 3. Exemplo Prático (Teste de Mesa)**

Para validar se o código Python está correto, use este caso nos testes da sua equipe:

**Cenário de Teste:**

* **Perfil:** Residencial  
* **Consumo:** 250 kWh  
* **Bandeira:** Vermelha 1 (V1)

**Passo a passo da Validação:**

* [x] **Custo Base:** 250 * (0.29 + 0.35) = **R$ 160,00**  
* [x] **Bandeira:** (250 // 100) = 2. Logo, 2 * 4.46 = **R$ 8,92**  
* [x] **Subtotal:** 160.00 + 8.92 = **R$ 168,92**  
* [x] **Base de Cálculo (Com impostos):** 168.92 / 0.7275 = **R$ 232,19**  
* [x] **CIP:** **R$ 15,00**  
* [x] **TOTAL A PAGAR:** 232.19 + 15.00 = **R$ 247,19**

## **👨‍💻 4. Divisão de Trabalho no GitHub**

Para evitar conflitos de merge, a equipe de 4 pessoas deve se dividir nos seguintes módulos (arquivos .py separados):

### **1️⃣ Aluno 1: A Interface (main.py e interface.py)**

* **Responsabilidade:** Loop principal while True e os menus do sistema.  
* **Desafio:** Blindar o sistema. Se o sistema pede consumo e o usuário digita "batata", o programa não pode "crashar" (use try/except ValueError). Formatar saídas de texto de forma legível.

### **2️⃣ Aluno 2: O Motor (motor_calculo.py)**

* **Responsabilidade:** Criar funções lógicas/matemáticas (ex: calcular_fatura()). Sem inputs ou prints dentro destas funções (funções puras).  
* **Desafio:** Implementar condicionais if/elif/else alinhadas perfeitamente com a regra de negócio e tratar a matemática.

### **3️⃣ Aluno 3: O Estado (banco_dados_poo.py)**

* **Responsabilidade (AV2):** Criar a class UnidadeConsumidora: com __init__.  
* **Desafio:** Atributos devem ser id_cliente, nome, perfil e uma lista de 12 posições simulando os meses (historico). Gerenciar o cadastro salvando-os em uma lista global.

### **4️⃣ Aluno 4: Analytics (relatorios_analytics.py)**

* **Responsabilidade:** Funções que varrem a lista de clientes usando laços for.  
* **Desafios:** 1. Imprimir matriz de consumo (Cliente x Meses).  
  2. Encontrar a conta mais alta (auditoria).  
  3. Listar IDs com consumo acima da média (suspeita de fraude).

## **📅 5. Cronograma de Entregas (Milestones)**

### **🚩 Milestone 1 (AV1 - Semana 9): O Esqueleto Funcional**

* **Foco:** Lógica Sequencial, Laços (while/for) e Funções.  
* **Entrega:** O sistema não precisa de classes nem listas longas. Ele pergunta os dados (Consumo, Perfil, Bandeira), usa as funções do Aluno 2, imprime a conta cravada na tela e pergunta se deseja calcular outra. O teste de mesa deve funcionar perfeitamente.

### **🚩 Milestone 2 (AV2 - Semana 13): O Sistema Persistente**

* **Foco:** Coleções (Listas/Matrizes) e Programação Orientada a Objetos.  
* **Entrega:** O usuário cadastra N clientes instanciando objetos (Aluno 3). Lança consumos variados para eles em uma matriz mensal. Ao final, o sistema imprime os relatórios complexos gerados pelo Aluno 4 através do menu principal.

💡 *Dica:* Usem e abusem de commits descritivos e branches separadas (git checkout -b feature-calculo-impostos) para manter a sanidade do projeto!