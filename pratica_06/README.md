# Lista de Exercícios - POO em Python

# 📘 Lista de Exercícios Comentados – POO em Python

Esta lista foi desenvolvida para guiar o estudante de forma **progressiva e didática** no aprendizado da **Programação Orientada a Objetos (POO) em Python**.

Os exercícios seguem uma sequência que vai desde a **criação de classes básicas** até a **modelagem de sistemas com múltiplos objetos e coleções**.

---

## 🎯 Objetivos de Aprendizagem

Ao concluir esta lista, você deverá ser capaz de:

- Compreender os conceitos de **classe, objeto, atributo e método**
- Utilizar corretamente o método especial `__init__`
- Aplicar o uso de **self** em métodos
- Criar e manipular **coleções de objetos**
- Desenvolver pensamento de **modelagem orientada a objetos**

---

## 🧩 Exercícios

### 1️⃣ Criando uma Classe
**Descrição:**  
Crie uma classe chamada `Estudante` com atributos `nome` e `matricula`.

**Orientações:**
- Use a palavra-chave `class`
- Defina o método `__init__`
- Utilize `self` para armazenar os atributos

---

### 2️⃣ Adicionando Lista de Notas
**Descrição:**  
Adicione um atributo `notas` que seja uma lista vazia.

**Orientações:**
- Declare dentro do `__init__`
- Utilize: `self.notas = []`

---

### 3️⃣ Método adicionar_nota
**Descrição:**  
Implemente um método para adicionar notas ao estudante.

**Orientações:**
- Utilize `self.notas.append(nota)`
- Teste adicionando mais de uma nota

---

### 4️⃣ Método calcular_media
**Descrição:**  
Crie um método para calcular a média das notas.

**Orientações:**
- Use `sum()` e `len()`
- Trate lista vazia retornando `0`

---

### 5️⃣ Criando Objetos
**Descrição:**  
Crie diferentes objetos da classe `Estudante`.

**Orientações:**
- Instancie múltiplos estudantes
- Verifique que os dados são independentes

---

### 6️⃣ Método situacao
**Descrição:**  
Implemente um método que retorne a situação do estudante.

**Regra:**
- Média ≥ 7 → **Aprovado**
- Média < 7 → **Recuperação**

**Dica:**  
Não armazene a situação como atributo — calcule com base na média.

---

### 7️⃣ Validação de Notas
**Descrição:**  
Garanta que apenas notas entre 0 e 10 sejam aceitas.

**Orientações:**
- Use `if`
- Lance `ValueError` em caso inválido

---

### 8️⃣ Classe Produto
**Descrição:**  
Crie uma classe `Produto` com um atributo de classe.

**Orientações:**
- Exemplo: `imposto_padrao = 0.10`
- Entenda a diferença entre atributo de classe e de instância

---

### 9️⃣ Método preco_com_imposto
**Descrição:**  
Calcule o preço final com imposto.

**Orientações:**
- Use `self.preco`
- Use `Produto.imposto_padrao`

---

### 🔟 Classe Turma
**Descrição:**  
Crie uma classe `Turma` para armazenar estudantes.

**Orientações:**
- Crie uma lista: `self.estudantes = []`

---

### 1️⃣1️⃣ Método matricular
**Descrição:**  
Adicione estudantes à turma.

**Orientações:**
- O método deve receber um objeto `Estudante`

---

### 1️⃣2️⃣ Média Geral
**Descrição:**  
Calcule a média geral da turma.

**Orientações:**
- Percorra a lista de estudantes
- Use `calcular_media()` de cada objeto

---

### 1️⃣3️⃣ Relatório
**Descrição:**  
Exiba os dados dos estudantes.

**Orientações:**
- Imprima nome, média e situação
- Utilize um loop (`for`)

---

### 1️⃣4️⃣ Corrigir uso do self
**Descrição:**  
Corrija erros em códigos onde `self` não foi utilizado corretamente.

**Orientações:**
- Identifique variáveis locais
- Substitua por atributos (`self.atributo`)

---

### 1️⃣5️⃣ Reflexão Final
**Descrição:**  
Explique a diferença entre:

- Atributo de classe
- Atributo de instância

**Orientações:**
- Inclua exemplo em Python
- Demonstre comportamento diferente

---

## 💡 Dica do Professor

Antes de programar, sempre pergunte:

1. Qual é a **entidade** do problema?
2. Quais são seus **dados (atributos)**?
3. Quais são suas **ações (métodos)**?

👉 Esse raciocínio é o coração da **Programação Orientada a Objetos**.

---

## 📂 Sugestão de Estrutura do Repositório

```bash
pratica_06/
│
├── README.md
├── seu-nome/
    └── exercicio1.py

