## [AULA] Lista de Exercícios 01: Fundamentos de Python

Esta lista de exercícios foca no domínio de **entrada/saída de dados**, **conversão de tipos (casting)**, **operadores matemáticos** e **lógica básica**.

---

### 📋 Instruções de Entrega
1. Siga o fluxo de repositório ensinado em sala: **Pull**, **Branch** e **Pasta Pessoal**.
2. Crie um arquivo `.py` individual para cada exercício (ex: `ex01.py`, `ex02.py`).
3. Realize o **commit** e envie o seu **Pull Request**.

---

### 💻 Exercício 1: O Registro do Sistema (I/O e Tipagem)
Crie um programa que simule o registro de um novo usuário, solicitando as seguintes informações:
* **Nome do usuário** (string).
* **Ano de nascimento** (inteiro).
* **Altura em metros** (float).

O programa deve calcular a idade atual e exibir a mensagem:
> "Olá, [Nome]! Você tem [Idade] anos e sua altura é de [Altura]m. Registro concluído."

**Fórmula:**
$$Idade = Ano_{Atual} - Ano_{Nascimento}$$

> **Dica:** Lembre-se de converter o ano de nascimento usando `int()` antes da subtração.

---

### 💰 Exercício 2: Calculadora de Freelancer (Matemática)
Desenvolva um script para calcular o valor de um projeto freelancer solicitando:
1. O valor cobrado por hora.
2. A estimativa de horas para conclusão.

Exiba o **valor bruto**, o **valor dos impostos (15%)** e o **valor líquido final**.

**Fórmulas:**
* $Valor_{Bruto} = Horas \times Valor_{Hora}$
* $Impostos = Valor_{Bruto} \times 0.15$
* $Valor_{Liquido} = Valor_{Bruto} - Impostos$

---

### 🍕 Exercício 3: Divisão Justa (Divisão Inteira e Módulo)
Crie um programa para dividir fatias de pizza entre uma equipe, perguntando:
* O número total de fatias.
* O número de programadores na equipe.

Calcule e imprima quantas fatias inteiras cada um comerá e o resto que sobrará na caixa.

**Fórmulas:**
* $Fatias_{PorPessoa} = Total_{Fatias} // Programadores$
* $Sobra = Total_{Fatias} \% Programadores$

---

### 🔐 Exercício 4: Verificador de Acesso (Lógica e Relacionais)
Desenvolva um sistema de verificação que solicite a **idade** e os **anos de experiência** do usuário.

**Regra Importante:** Não utilize `if/else`. O programa deve imprimir apenas `True` ou `False` para a condição de acesso.

**Regra Lógica:**
$$Acesso = (Idade \geq 18) \text{ AND } (Experiencia > 2)$$

**Saída esperada:** "Acesso Liberado: True".

---

### 🚀 Exercício 5: Desafio do Download (Mistura de Conceitos)
Calcule o tempo estimado de download solicitando:
1. O tamanho do arquivo em **Megabytes (MB)**.
2. A velocidade da internet em **Megabits por segundo (Mbps)**.

**Regra de Negócio:** Considere que 1 Byte = 8 bits. Converta o tempo total para minutos inteiros e segundos restantes.

**Fórmulas:**
* $Tempo_{Segundos} = \frac{Tamanho_{MB}}{(Velocidade_{Mbps} / 8)}$
* $Minutos_{Inteiros} = Tempo_{Segundos} // 60$
* $Segundos_{Restantes} = Tempo_{Segundos} \% 60$

**Saída:** "X minutos e Y segundos".

---

### 💡 Dica do Professor: F-Strings
Para facilitar a impressão de textos com variáveis, utilize as **f-strings**:
`print(f"O valor total do projeto é R$ {valor_liquido}")`
### 💡 Dica do Professor: F-Strings
[cite_start]Para facilitar a impressão de textos com variáveis, utilize as **f-strings**:
[cite_start]`print(f"O valor total do projeto é R$ {valor_liquido}")`
