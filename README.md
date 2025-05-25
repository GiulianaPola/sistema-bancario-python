Claro! Vou deixar o README ainda mais profissional, organizado, atraente e com um tom mais envolvente para destacar seu trabalho. Vou adicionar badges, melhorar a formatação, e ajustar a linguagem para ser mais fluida e clara, sem perder o foco técnico e comportamental.

---

# Sistema Bancário em Python – Bootcamp DIO Suzano

![Python](https://img.shields.io/badge/python-3.x-blue?logo=python\&style=flat-square) ![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square) ![Status](https://img.shields.io/badge/status-completo-brightgreen?style=flat-square)

Projeto desenvolvido durante o Bootcamp Python Developer da DIO, que simula um sistema bancário simples, focado em operações essenciais como depósito, saque e consulta de extrato. O sistema reforça conceitos fundamentais de programação e boas práticas em Python, com foco na lógica de negócio e experiência do usuário.

---

## 📑 Sumário

* [Descrição](#descrição)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Funcionalidades](#funcionalidades)
* [Como Executar](#como-executar)
* [Exemplos de Uso](#exemplos-de-uso)
* [Contribuição](#contribuição)
* [Créditos](#créditos)
* [Licença](#licença)
* [Habilidades Técnicas e Soft Skills](#habilidades-técnicas-e-soft-skills)
* [Contato](#contato)

---

## 📋 Descrição

Este projeto consiste em um **sistema bancário básico** que permite realizar operações de depósito, saque e visualização do extrato. Desenvolvido em Python, o sistema atende regras reais de negócio, como:

* Limite máximo de saques por dia (3 vezes);
* Limite de valor por saque;
* Restrições de saldo disponível;
* Registro detalhado das operações realizadas para consulta.

O objetivo principal foi aplicar conhecimentos em lógica de programação, estruturas condicionais, loops, manipulação de strings e tratamento de erros, desenvolvendo um código limpo, eficiente e de fácil manutenção.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x** – Linguagem de programação principal
* **Git** – Controle de versão
* **VSCode / PyCharm / outro editor** – Ambiente de desenvolvimento

---

## 🚀 Funcionalidades

* **Depósito:** aceita somente valores inteiros e positivos, registra cada operação no extrato.
* **Saque:** permite até 3 saques diários, respeitando limite por operação e saldo disponível, registra cada saque no extrato.
* **Extrato:** exibe todas as operações detalhadas e o saldo atual, com valores formatados em reais (R\$).
* **Interface amigável:** menu interativo via terminal, com validações para entradas inválidas e mensagens de feedback claras.

---

## ⚙️ Como Executar

### Pré-requisitos

* [Python 3.x](https://www.python.org/downloads/) instalado no sistema.

### Passos

```bash
# Clone o repositório
git clone https://github.com/seuusuario/sistema-bancario-python.git

# Acesse a pasta do projeto
cd sistema-bancario-python

# Execute o script principal
python sistema_bancario.py
```

---

## 🎯 Exemplos de Uso

Menu interativo exibido ao iniciar o programa:

```
=== Banco DIO ===

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção desejada: d
Informe o valor do depósito: 1000

Depósito de R$ 1000.00 realizado com sucesso!

Digite a opção desejada: s
Informe o valor do saque: 500

Saque de R$ 500.00 realizado com sucesso!

Digite a opção desejada: e

=== EXTRATO ===
Depósito: R$ 1000.00
Saque: R$ 500.00
Saldo atual: R$ 500.00
================
```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork deste repositório.
2. Crie uma branch para sua modificação (`git checkout -b feature/nome-da-feature`).
3. Faça commit das suas alterações (`git commit -m "Descrição da feature"`).
4. Envie para o seu fork (`git push origin feature/nome-da-feature`).

---

## 🙌 Créditos

* Bootcamp Python Developer – [DIO](https://www.dio.me/bootcamp/suzano-python-developer)
* Mentores e equipe da DIO pela estrutura e desafios inspiradores.
* Documentação oficial do Python.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](./LICENSE).

---

## 💡 Habilidades Técnicas e Soft Skills

### Técnicas

* Proficiência em **Python 3**: manipulação de variáveis, condicionais, loops, funções e strings.
* Implementação de regras de negócio complexas com foco em integridade e segurança financeira.
* Desenvolvimento de interfaces interativas no terminal, com tratamento robusto de erros e validação de entrada.

### Comportamentais

> Demonstrei **organização** e **autonomia** para planejar e estruturar o código do projeto, garantindo clareza e reutilização.
>
> Exercitei **pensamento crítico** ao implementar validações e restrições do sistema bancário, antecipando possíveis erros e comportamentos indesejados.
>
> Valorizei a **comunicação clara** e documentação detalhada para facilitar entendimento por outros desenvolvedores e recrutadores, refletindo meu compromisso com boas práticas.

---

## 📬 Contato

* LinkedIn: [https://www.linkedin.com/in/giulianapola/](https://www.linkedin.com/in/giulianapola/)
* GitHub: [https://github.com/GiulianaPola](https://github.com/GiulianaPola)
* E-mail: [giulianapolasp@gmail.com](mailto:giulianapolasp@gmail.com)
