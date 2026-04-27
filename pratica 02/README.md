# [AULA] Lista de Exercícios 02: Estruturas Condicionais e Laços

Esta lista de exercícios foca no domínio de **estruturas de decisão** (`if`, `elif`, `else`) e **laços de repetição** (`while` e `for`) para consolidar a lógica de programação em Python.

---

### 📋 Instruções de Entrega

1. Siga o fluxo de repositório ensinado em sala: **Fork**, **Clone**, **Branch** e **Pasta Pessoal**.
2. Crie um arquivo `.py` individual para cada exercício (ex: `ex01.py`, `ex02.py`).
3. Realize o **commit** e envie o seu **Pull Request** com seu nome completo no título.

---

### 💻 Exercício 1: Classificação de Número (Decisão)

Crie um programa que leia um número inteiro e informe se ele é positivo, negativo ou zero.
* **Objetivo**: Praticar `if/elif/else` com faixas exclusivas.
* **Dica**: Teste com os valores 0, 5 e -3.

---

### 🎂 Exercício 2: Faixa Etária Essencial (Decisão)

Leia a idade de uma pessoa e informe sua classificação de acordo com as regras:
* **Menor de idade**: Menos de 18 anos.
* **Maior de idade**: Entre 18 e 59 anos.
* **Idoso**: 60 anos ou mais.

---

### ⚖️ Exercício 3: Par ou Ímpar (Laços e Decisão)

Utilizando a estrutura `for`, percorra os números de 1 a 20 e informe se cada um deles é par ou ímpar.
* **Regra**: Utilize o operador de módulo `numero % 2 == 0` para verificar a paridade.

---

### 🔐 Exercício 4: Senha até Liberar Acesso (Laços)

Desenvolva um sistema que utilize `while` para ler uma senha repetidamente até que o usuário digite a palavra **"acesso"**.
* **Atenção**: Lembre-se de ler a senha novamente dentro do laço para evitar um loop infinito.

---

### 📈 Exercício 5: Contar Positivos (Laços e Decisão)

Solicite 10 números ao usuário usando `for` e, ao final, informe quantos desses números são positivos.
* **Dica**: Inicialize um contador em zero (`contador_positivos = 0`) antes do laço.

---

### 📝 Exercício 6: Validação de Nota (Laços)

Peça uma nota entre 0 e 10. Se o usuário digitar um valor inválido, use `while` para repetir a pergunta até que uma nota válida seja inserida.
* **Critério**: O programa deve continuar enquanto `nota < 0` ou `nota > 10`.

---

### ➕ Exercício 7: Soma dos Pares (Acumuladores)

Leia 8 valores inteiros e calcule a soma apenas daqueles que forem números pares.
* **Objetivo**: Praticar o uso de acumuladores e filtros de paridade.

---

### 🔢 Exercício 8: Tabuada Dinâmica (Matemática e Laços)

Solicite um número ao usuário e exiba sua tabuada de 1 a 10 utilizando a estrutura `for`.
* **Saída esperada**: `7 x 3 = 21`.

---

### 💵 Exercício 9: Reajuste Salarial por Faixa (Decisão)

Aplique um percentual de reajuste ao salário informado seguindo a tabela:
* **Até R$ 1.500,00**: 15% de aumento.
* **De R$ 1.500,01 a R$ 3.000,00**: 10% de aumento.
* **Acima de R$ 3.000,00**: 5% de aumento.

---

### 🖱️ Exercício 10: Menu de Operações (Sentinela)

Crie um menu interativo com as opções: **1-Somar**, **2-Subtrair** e **0-Sair**.
* O programa deve repetir o menu até que o usuário digite a opção 0.

---

### 🎓 Exercício 11: Classificação de Turma (Contadores)

Leia a quantidade de alunos e, em seguida, suas médias. Informe ao final o total de:
* **Aprovados**: Média >= 7.
* **Recuperação**: Média entre 4 e 6.9.
* **Reprovados**: Média < 4.

---

### 🛒 Exercício 12: Registro de Compras (Interatividade)

Solicite o valor de várias compras. Após cada entrada, pergunte: "Deseja continuar? (S/N)". O programa encerra quando o usuário decidir parar.

---

### 🛠️ Exercício 13: Depuração de Código (Lógica)

Corrija o código abaixo para que ele realize uma contagem regressiva de 10 a 1 sem entrar em loop infinito:

```python
contador = 10
while contador >= 1:
    print(contador)
    # Adicione a linha que falta aqui
```

---

### 🔄 Exercício 14: Refatoração (While para For)

Escolha um exercício anterior que você resolveu com `while` e reescreva-o obrigatoriamente utilizando a estrutura `for`. Explique se a leitura do código ficou mais simples.

---

### 🏆 Exercício 15: Desafio - Maior Nota (Busca)

Leia 5 notas de alunos e, utilizando um laço `for`, informe qual foi a maior nota encontrada no grupo.
* **Dica**: Inicialize a variável `maior` com um valor bem baixo ou com a primeira nota lida.

---

### 💡 Dica do Professor: Atalho Mental de Escolha

Para não errar a estrutura, faça a pergunta correta ao problema:
* **"Até quando?"** (Depende de uma condição) -> Use **while**.
* **"Quantas vezes?"** (Quantidade fixa ou conhecida) -> Use **for**.
* **"Qual caminho?"** (Decisão entre faixas) -> Use **if/elif/else**.

---

### ⚠️ Checklist Anti-Erro

- [ ] Verificou se o `while` possui atualização da variável de controle?
- [ ] A ordem dos seus `if/elif` respeita as faixas de valores corretamente?
- [ ] Testou os "casos de borda" (ex: notas exatas 0, 7 e 10)?
- [ ] O código está identado corretamente dentro dos blocos de decisão e repetição?