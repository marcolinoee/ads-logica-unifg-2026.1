<h1 align="center">🚀 Guia de Entrega de Atividades - ADS 2026</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git Badge"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"/>
</p>

> **Bem-vindo(a) à nossa trilha de aprendizado!** Este repositório é o centro das nossas atividades práticas. Aqui, você não apenas aprenderá **Python**, mas também dominará o fluxo de trabalho real de um desenvolvedor profissional utilizando **Git** e **GitHub**.

---

## 📂 Estrutura de Pastas

Para manter o projeto organizado, utilizaremos uma estrutura de **Monorepo**. Cada aula terá sua própria pasta, e dentro dela, você criará a sua pasta individual para entrega:

```text
📦 Raiz do Repositório
├── 📁 Aula-01-Introducao
│   ├── 📄 README.md           <-- Instruções da Aula 01
│   ├── 📁 joao-silva          <-- Pasta do aluno (Exemplo)
│   │   └── 🐍 ex01.py
│   └── 📁 maria-souza         <-- Pasta da aluna (Exemplo)
│       └── 🐍 ex01.py
├── 📁 Aula-02-Condicionais
│   ├── 📄 README.md           <-- Instruções da Aula 02
│   └── 📁 [sua-pasta-aqui]
└── ⚙️ .gitignore              <-- Arquivo para ignorar lixo eletrônico
```

---

## 🛠️ Passo 1: Configuração Inicial

> **Nota:** Este passo precisa ser feito **apenas uma vez** antes da sua primeira entrega.

1. **Fork:** No topo desta página, clique no botão `Fork`. Isso criará uma cópia exata deste repositório na sua conta pessoal.
2. **Clone:** Abra o terminal no seu computador e baixe o seu fork (substitua pelo seu nome de usuário):
   ```bash
   git clone [https://github.com/SEU_USUARIO/ads-python-2026.git](https://github.com/SEU_USUARIO/ads-python-2026.git)
   ```
3. **Configurar o Upstream:** Para receber automaticamente as atualizações (novas aulas) que o professor postar, execute:
   ```bash
   git remote add upstream [https://github.com/anderson-oliveira/ads-python-2026.git](https://github.com/anderson-oliveira/ads-python-2026.git)
   ```

---

## 🔁 Passo 2: O Ritual de Entrega (Toda Semana)

Siga estes **5 passos** rigorosamente para garantir que sua atividade seja enviada e corrigida:

### 1️⃣ Sincronize seu código
Antes de começar, pegue as novidades que o professor postou:
```bash
git checkout main
git pull upstream main
git push origin main
```

### 2️⃣ Crie uma Branch para a Aula
**Nunca trabalhe na branch `main`.** Crie uma "linha do tempo" separada para cada aula:
```bash
git checkout -b entrega-aula-01
```

### 3️⃣ Crie sua pasta e codifique
1. Entre na pasta da aula vigente (ex: `cd Aula-01-Introducao`).
2. Crie sua pasta seguindo o padrão exigido: `mkdir seu-nome-sobrenome` (sem espaços ou acentos).
3. Salve seus arquivos `.py` dentro dela.

### 4️⃣ Envie as alterações
```bash
git add .
git commit -m "feat: entrega aula 01 - Seu Nome"
git push origin entrega-aula-01
```

### 5️⃣ Abra o Pull Request (PR)
1. Vá até o **seu repositório** no GitHub.
2. Clique no botão verde **Compare & pull request**.
3. No título, coloque exatamente: `[AULA 01] Nome Completo`.
4. Clique em **Create Pull Request**.

---

## ⚠️ Regras de Ouro (Checklist)

Para que sua atividade seja avaliada, certifique-se de cumprir todos os itens abaixo:

- [ ] **Nomenclatura:** Sua pasta pessoal deve seguir o padrão `nome-sobrenome` (tudo minúsculo e com hífen). Pastas com nomes como *projeto1* ou *exercicios* serão desconsideradas.
- [ ] **Não altere o alheio:** Você só tem permissão para criar e editar arquivos dentro da **sua** pasta pessoal.
- [ ] **Comentários no PR:** No Pull Request, sinta-se à vontade para escrever as dificuldades que teve ou o que aprendeu de novo na semana.
- [ ] **Clean Code:** Use nomes de variáveis descritivos e claros (ex: `soma_notas` em vez de `s`).
