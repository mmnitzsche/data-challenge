# 🚀 Data Challenge - Looqbox

Este repositório contém a minha solução para o desafio de dados proposto pela [Looqbox](https://github.com/looqbox/data-challenge). O desafio é dividido em três partes (cases), cada uma com um foco diferente de análise e manipulação de dados.

---

## 📁 Estrutura do Repositório

<span style="font-size: 30px;">🚨</span>
<span style="font-size: 16px; font-weight: bold;">Importante:</span>
<span style="font-size: 16px;">
Para conectar ao banco de dados de forma segura, é necessário configurar a variável de ambiente <code>DATABASE_URL</code>.
Em ambiente local, essa configuração deve ser feita em um arquivo <code>.env</code>.
Já em produção (Streamlit Cloud), a variável deve ser adicionada na seção <code>Settings > Secrets</code> do seu aplicativo.
</span>
---

`.env`
 ``` py
  DATABASE_URL=protocolo+driver://usuario:senha@endereco_do_host/nome_do_banco
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
├── .env
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

___
## 🧠 Resolução dos desafios  
Você vai ver apenas um resumo das soluções questões/desafios.
Caso queira ver os desafios mais mais detalhes acesse: [Looqbox](https://github.com/looqbox/data-challenge).


## 1️⃣ Case 1

### **Case 1.1** - **Questão**: What are the 10 most expensive products in the company?

```sql
SELECT
    product_cod,
    product_name,
    product_val
FROM `looqbox-challenge`.data_product
ORDER BY product_val DESC
LIMIT 10;
```

> 💡 **Descrição da Solução:** Foi apenas achar a tabela que era a responsável por conter o valor "cheio" dos produtos, ordenar a coluna `PRODUCT_VAL` que responsável pelo valor, ordernar por `DESC` e limitar o retorno em 10 linhas, como pedido na questão usando o `LIMIT 10`

| Código  | Produto                                                                 | Preço  |
|---------|-------------------------------------------------------------------------|------------|
| 320046  | Escova Dental Eletrica ORAL B D34 Professional Care 5000 110v           | 399.90     |
| 315481  | Cafeteira Expresso 3 CORACOES Tres Modo Vermelho                        | 499.00     |
| 311397  | Conjunto de Panelas Allegra em Inox TRAMONTINA 5 Pecas Gratis Utensilios 5 Pecas | 359.00     |
| 301409  | Whisky Escoces THE MACALLAN Ruby Garrafa 700ml com Caixa                | 741.99     |
| 190817  | Champagne Rose VEUVE CLICQUOT PONSARDIM Garrafa 750ml                   | 366.90     |
| 176185  | Whisky Escoces JOHNNIE WALKER Blue Label Garrafa 750ml                  | 735.90     |
| 154431  | Champagne Frances Brut Imperial MOET & CHANDON Garrafa 750ml            | 315.90     |
| 153795  | Champagne Frances Brut Imperial MOET Rose Garrafa 750ml                 | 359.90     |
| 147706  | Whisky Escoces CHIVAS REGAL 18 Anos Garrafa 750ml                       | 329.90     |
| 100280  | Vinho Portugues Tinto Vintage QUINTA DO CRASTO Garrafa 750ml            | 445.90     |



<br>

### **Case 1.2** - **Questão**: What sections do the ``BEBIDAS`` and ``PADARIA`` departments have?

```sql
SELECT DISTINCT
    SECTION_NAME
FROM `looqbox-challenge`.data_product
WHERE
    DEP_NAME IN ('BEBIDAS', 'PADARIA')
ORDER BY SECTION_NAME;
```

> 💡 **Descrição da Solução:** quando identifiquei que os valores estavam na tabela `.data_product` eu fiz um `WHERE` onde estava a coluna dos departamentos (`dep_name`) e ordenei pelo nome de seção (`section_name`)

| Departamento          |
|----------------------|
| BEBIDAS              |
| CERVEJAS             |
| DOCES-E-SOBREMESAS   |
| GESTANTE             |
| PADARIA              |
| QUEIJOS-E-FRIOS      |
| REFRESCOS            |
| VINHOS               |



## 2️⃣ Case 2

### **Case 1.1** - **Questão**: What are the 10 most expensive products in the company?

```sql
SELECT
    product_cod,
    product_name,
    product_val
FROM `looqbox-challenge`.data_product
ORDER BY product_val DESC
LIMIT 10;
```

> 💡 **Descrição da Solução:** Foi apenas achar a tabela que era a responsável por conter o valor "cheio" dos produtos, ordenar a coluna `PRODUCT_VAL` que responsável pelo valor, ordernar por `DESC` e limitar o retorno em 10 linhas, como pedido na questão usando o `LIMIT 10`


___
### Case 1.2

```bash
cd .\case2\      
python main.py
```

Ira renderizar Esse dataframe:
| Loja          | Categoria    | TM    |
|---------------|--------------|-------|
| Bahia         | Atacado      | 15.39 |
| Bangkok       | Posto        | 13.67 |
| Belem         | Proximidade  | 15.37 |
| Berlin        | Proximidade  | 15.39 |
| Buenos Aires  | Atacado      | 15.39 |
| Chicago       | Varejo       | 15.53 |
| Dubai         | Atacado      | 15.39 |
| Hong Kong     | Farma        | 26.33 |
| London        | Farma        | 28.96 |
| Madri         | Farma        | 29.00 |
| Miami         | Posto        | 13.67 |
| New York      | Proximidade  | 15.39 |
| Paris         | Proximidade  | 15.39 |
| Rio de Janeiro| Farma        | 29.56 |
| Roma          | Varejo       | 15.39 |
| Salvador      | Atacado      | 15.39 |
| Sao Paulo     | Varejo       | 15.39 |
| Sidney        | Posto        | 13.67 |
| Tokio         | Varejo       | 15.39 |
| Vancouver     | Posto        | 13.67 |


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