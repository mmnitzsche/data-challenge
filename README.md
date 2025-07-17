# 🚀 Data Challenge - Looqbox

Este repositório contém a minha solução para o desafio de dados proposto pela [Looqbox](https://github.com/looqbox/data-challenge). O desafio é dividido em três partes (cases), cada uma com um foco diferente de análise e manipulação de dados.

---

## 📁 Estrutura do Repositório

<span style="font-size: 30px;">🚨</span> 
<span style="font-size: 16px; font-weight: bold;">Importante:</span> 
<span style="font-size: 16px;">
  O arquivo <code>connection_string.py</code> contém a string de conexão responsável por estabelecer a comunicação segura com o banco de dados. Por questões de segurança, ele foi omitido, mas você pode reproduzi-lo conforme necessário.
</span>


`connection_string.py`
 ``` py
  cs = "protocolo+driver://usuario:senha@endereco_do_host/nome_do_banco" 
```

```
├── case1/
│   ├── case-1-1.sql
│   ├── case-1-1.sql
│   └── case-1-1.sql
├── case2/
│   ├── main.py
│   ├── analysis.py
│   ├── sql_queries.py
│   └── loja_categoria_tm.csv
├── case3/
│   ├── app.py
│   ├── functions.py
│   └── sql_queries.py
├── connection.py
├── connection_string.py ❌
├── requirements.txt
└── README.md
```

---

## 📦 Requisitos

- Python 3.10+
- Bibliotecas listadas em `requirements.txt`

Para instalar os requisitos, utilize:

```bash
pip install -r requirements.txt
```

---

## 💼 Descrição dos Cases

### 📊 Case 1: SQL & Raciocínio Lógico

- Esse case é focado em resolução de perguntas de negócio utilizando SQL.
- As respostas e explicações podem estar em um arquivo `.sql`, `.py`, `.md` ou diretamente no corpo de um notebook ou script.
- Exige raciocínio lógico e clareza na explicação.

### 📈 Case 2: Análise e Criação de Métricas

- Análise de um dataset de vendas fictício (presente no arquivo `loja_categoria_tm.csv`).
- Criação de métricas relevantes por categoria, loja e produto.
- Organização do código modular em scripts:
  - `main.py`: ponto de entrada
  - `analysis.py`: funções principais de análise
  - `sql_queries.py`: contém as queries de apoio

### 📉 Case 3: Desenvolvimento de API Simples

- Simula a construção de uma pequena API para responder a perguntas baseadas em dados.
- Utiliza FastAPI (ou estrutura simples similar) para responder endpoints REST.
- Principais arquivos:
  - `app.py`: define os endpoints
  - `functions.py`: lógica de negócio
  - `sql_queries.py`: queries de apoio

---

## 🛠️ Como Executar

### Case 2

```bash
cd case2
python main.py
```

### Case 3

```bash
cd case3
uvicorn app:app --reload
```

Acesse [http://localhost:8000](http://localhost:8000) no navegador para testar os endpoints.

---

## 📌 Observações

- O arquivo `connection_string.py` está preparado para conter as credenciais de conexão com banco de dados PostgreSQL (mas não inclui senhas por segurança).
- O projeto foi modularizado para facilitar manutenção, leitura e reutilização de código.
- Algumas partes foram adaptadas para rodar localmente sem conexão real com banco, simulando resultados onde necessário.

---

## 🧠 Autor

Desenvolvido por **[Seu Nome Aqui]** como parte do processo seletivo da Looqbox.