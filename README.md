# 🚀 Data Challenge - Looqbox

Este repositório contém a minha solução para o desafio de dados proposto pela [Looqbox](https://github.com/looqbox/data-challenge). O desafio é dividido em três partes (cases) + um teste de SQL, cada uma com um foco diferente de análise e manipulação de dados.

---

## 📁 Estrutura do Repositório

<span style="font-size: 30px;">🚨</span>
<span style="font-size: 16px; font-weight: bold;">Importante:</span>
<span style="font-size: 16px;">
Para conectar ao banco de dados de forma segura, é necessário configurar a variável de ambiente <code>DATABASE_URL</code>.
Em ambiente local, essa configuração deve ser feita em um arquivo <code>.env</code>.<br>
<br>
Streamlit:  [Dashboard em publicado](https://imdb-dashboard.streamlit.app/)
<br>
Caso queira publicar essa solução no Stramlit (Streamlit Cloud), a variável da string de conexão deve ser adicionada na seção <code>Settings > Secrets</code> do seu aplicativo.
</span>
---

`.env`
 ``` py
  DATABASE_URL=protocolo+driver://usuario:senha@endereco_do_host/nome_do_banco
```

```
├── .devcontainer
│   └── devcontainer.json
├── case1
│   ├── case_1.py
│   ├── main.py
│   └── sql_queries.py
├── case2
│   ├── case_2.py
│   ├── main.py
│   └── sql_queries.py
├── case3
│   ├── app.py
│   ├── functions.py
│   └── sql_queries.py
├── media
│   ├── cards_title.png
│   ├── filters.gif
│   ├── hint_multbox.gif
│   ├── table_filter.gif
│   └── top_metrics.gif
├── sql_test
│   ├── case-1-1.sql
│   ├── case-1-2.sql
│   └── case-1-3.sql
├── venv
│   └── pyvenv.cfg
├── __pycache__
│   ├── connection.cpython-311.pyc
│   └── connection_string.cpython-311.pyc
├── .env
├── .gitignore
├── connection.py
├── connection_string.py
├── README.md
└── requirements.txt
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
Nesse documento vai conter apenas um resumo das questões do desafio Caso queira ver os as questões do desafios com mais detalhes acesse o repositório: [Looqbox](https://github.com/looqbox/data-challenge)


# 0️⃣ SQL TEST

### **SQL TEST.1** - **Questão**: What are the 10 most expensive products in the company?

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

### **SQL TEST.2** - **Questão**: What sections do the ``BEBIDAS`` and ``PADARIA`` departments have?

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


### **SQL TEST.3** - **Questão**:What was the total sale of products (in $) of each Business Area in the first quarter of 2019?

```sql
SELECT
    c.BUSINESS_NAME        AS business_area,
    SUM(s.SALES_VALUE)     AS total_sales_usd
FROM `looqbox-challenge`.data_store_sales AS s
JOIN `looqbox-challenge`.data_store_cad   AS c
      ON s.STORE_CODE = c.STORE_CODE
WHERE s.DATE >= '2019-01-01'
  AND s.DATE <  '2019-04-01'    
GROUP BY c.BUSINESS_NAME
ORDER BY total_sales_usd DESC;
```
> 💡 **Descrição da Solução:**  
> Para obter o total de vendas  (`SALES_VALUE`) por área de negócio (`BUSINESS_NAME`) durante o **primeiro trimestre de 2019** (de 1º de janeiro a 31 de março). Usei menor que  `< 2019-04-01`
> 
> Fiz um `JOIN` entre as tabelas `data_store_sales` e `data_store_cad` com base na coluna `STORE_CODE`, garantindo que os dados de venda sejam associados.
> 
> Em seguida, filtrei os dados de vendas para incluir apenas o período desejado.  
> 
> agrupei por área de negócio (`BUSINESS_NAME`) e a soma das vendas (`SALES_VALUE`) foi calculada para cada grupo.  
> 
> Por fim, os resultados são ordenados em ordem decrescente de vendas totais (`total_sales_usd`).

| Área de Negócio | Total de Vendas (US$) |
|------------------|------------------------|
| Farma            | 81.776.691,73          |
| Varejo           | 81.032.347,65          |
| Atacado          | 80.384.884,60          |
| Proximidade      | 80.171.122,80          |
| Posto            | 32.072.326,40          |

___

# 1️⃣ Case 1


### **Questão**:  The Dev Team was tired of developing the same old queries just varying the filters accordingly to their boss demands.
As a new member of the crew, your mission now is to create a dynamic function in Python, on the most flexible of ways, to produce queries and retrieve a dataframe based on three parameters:

- product_code: integer
- store_code: integer
- date: list of ISO-like strings
- Date e.g. ``['2019-01-01', '2019-01-31']``

```py
#%%
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection import read_database  

def retrieve_data(product_code: int, store_code: int, date: list) -> pd.DataFrame:
    try:
        start_date, end_date = date
        query = f"""
        SELECT *
        FROM data_product_sales
        WHERE PRODUCT_CODE = {product_code}
          AND STORE_CODE = {store_code}
          AND DATE BETWEEN '{start_date}' AND '{end_date}'
        """

        df = read_database(query)
        return df

    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")
        return pd.DataFrame()
```

> 💡 **Descrição da Solução:**  
> Para recuperar os dados criei a `retrieve_data`, que recebe como parâmetros o código do produto (`product_code`), o código da loja (`store_code`) e uma lista com duas datas (`date`) representando o início e o fim do período desejado.  
> A partir desses parâmetros, construo uma query SQL dinamicamente utilizando f-string (<em>usei ``'''`` para deixar mais legível</em>) para filtrar os dados da tabela `data_product_sales` com base nas colunas `PRODUCT_CODE`, `STORE_CODE` e `DATE`. Em seguida, utilizo a função `read_database` para executar essa query e carregar os dados em um DataFrame do Pandas.

<br>

## 🛠️ Como executar
```bash
cd .\case1\ 
python main.py
```
___
# 2️⃣ Case 2

### **Questão**: A brand new client sent you two ready-to-go queries. Those are listed below:

**Query 1:**
``` sql
SELECT
      STORE_CODE,
      STORE_NAME,
      START_DATE,
      END_DATE,
      BUSINESS_NAME,
      BUSINESS_CODE
FROM data_store_cad
```

**Query 2:**
``` sql
SELECT
        STORE_CODE,
        DATE,
        SALES_VALUE,
        SALES_QTY
FROM data_store_sales
WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31'
In addition, he gave you this set of instructions:
```
Use the queries as they are (do not modify them or create a new one);

Please filter the period between this given range: `['2019-10-01','2019-12-31']`

> 💡 **Descrição da Solução:**  
> Para calcular o **Ticket Médio (TM)** por loja e categoria, comecei importando os dados das tabelas `data_store_sales` e `data_store_cad` usando a função `read_database` com as queries pré estabelecidas (<em>das quais as queries já estão prontas no arquivo `case2/sql_queries.py`</em>).
> Em seguida, realizei um `merge` entre essas duas bases utilizando a coluna `STORE_CODE` como chave, garantindo que cada venda fosse associada à loja e à categoria correta.  
<br>
> Após isso, agrupei os dados por `STORE_NAME` e `BUSINESS_NAME`, somando os valores de `SALES_VALUE` (valor vendido) e `SALES_QTY` (quantidade vendida).  
> Com esses dados agregados, calculei o **Ticket Médio (TM)** dividindo o valor vendido pela quantidade de itens vendidos, e arredondei o resultado para duas casas decimais. Pra ficar igual ao dataframe sugerido.
```python
resumo["TM"] = (resumo["SALES_VALUE"] / resumo["SALES_QTY"]).round(2)
```
> Por fim, renomeei as colunas para `Loja`, `Categoria` e `TM`, retornando apenas essas três informações no dataframe final.
<br>

| Loja            | Categoria     | TM    |
|------------------|---------------|--------|
| Bahia           | Atacado       | 15.39 |
| Bangkok         | Posto         | 13.67 |
| Belem           | Proximidade   | 15.37 |
| Berlin          | Proximidade   | 15.39 |
| Buenos Aires    | Atacado       | 15.39 |
| Chicago         | Varejo        | 15.53 |
| Dubai           | Atacado       | 15.39 |
| Hong Kong       | Farma         | 26.33 |
| London          | Farma         | 28.96 |
| Madri           | Farma         | 29.00 |
| Miami           | Posto         | 13.67 |
| New York        | Proximidade   | 15.39 |
| Paris           | Proximidade   | 15.39 |
| Rio de Janeiro  | Farma         | 29.56 |
| Roma            | Varejo        | 15.39 |
| Salvador        | Atacado       | 15.39 |
| Sao Paulo       | Varejo        | 15.39 |
| Sidney          | Posto         | 13.67 |
| Tokio           | Varejo        | 15.39 |



## 🛠️ Como executar

```bash
cd .\case2\ 
python main.py
```
____
<br>

# 3️⃣ Case 3

### **Case 3** - **Questão**: Building your own visualization
Create at least one chart using the table IMDB_movies. The code must be in Python, and you are free to use any libraries, data in the table and graphic format. Explain why you chose the visualization (or visualizations) you are submitting.


### 🔹 `Visuais e Dashboard`
> 💡 **Descrição da Solução:**  
> Para construir um dashboard com os dados do IMDB, utilizei o **Streamlit** em conjunto com **Plotly** e **Pandas**. Separei o projeto em três arquivos principais:  
<br>
> `app.py`, responsável por toda a parte visual e lógica do dashboard; <br>
`functions.py`, onde concentro todas as funções auxiliares; <br>`sql_queries.py`, que guarda as queries SQL de forma organizada.  
>
> A conexão com o banco de dados foi feita usando uma função chamada `read_database`, e na versão de produção, estou utilizando as **credenciais via `secrets` do próprio Streamlit Cloud**.  
>> Toda essa estrutura foi pensada para ser **modular**, **escalável** e **fácil de manter**, separando responsabilidades em arquivos distintos e aproveitando os recursos do Streamlit.
>
> **Destaques da solução:**
> - Criei filtros dinâmicos de **atores**, **gêneros** e **ano** de lançamento, interdependentes: ao selecionar um ator, os gêneros se ajustam com base na nova filtragem (e vice-versa).
![alt text](media/filters.gif)
>
><br>
><br>

> - Exibi os principais indicadores em `metrics`/`cards` no topo do dashboard, como **total de filmes**, **rating médio** e **receita total**.
![alt text](media/cards_title.png)
>
><br>
><br>


> - Criei explicações personalizadas para as opções dos `selectbox`, para tornar a navegação mais intuitiva; o famoso 'hint'.
![alt text](media/hint_multbox.gif)
>
><br>
><br>

> - 🥇 Implementei uma visualização de **Top 10** com `Plotly Express`, baseada na métrica Y (ex: revenue, Rating) e agrupada pela métrica X (ex: Genre, Year). Você pode alterar a métrica de ambos os eixos se necessário, isso evita a criação de multiplos visuais e deixa a aplicação mais simples e performática.
![alt text](media/top_metrics.gif)
>
><br>
><br>

> - Por fim, exibo a tabela filtrada no final para permitir análise direta do dataset e filtro também aplicado.
![alt text](media/table_filter.gif)
>


<br>

### 🔹 `Códigos e funções:`
> 💡 **Leitura e Pré-processamento dos Dados:**  
> Os dados foram carregados diretamente do banco de dados com a função `read_database`, a partir de uma query definida no módulo `sql_queries.py`.  
> Em seguida, registros com valores ausentes em colunas críticas como `Rating`, `RevenueMillions`, `Actors`, `Genre` e `Year` foram descartados para garantir qualidade na análise.  
>  
> Após isso, foram aplicadas as funções `ensure_list_format` e `clean_list_items` para converter colunas de texto (`Actors` e `Genre`) em listas limpas, permitindo filtros múltiplos e buscas parciais.

> 💡 **Geração de Filtros Dinâmicos:**  
> Através de funções como `get_filtered_actors` e `get_filtered_genres`, foram criadas listas de opções que se atualizam de acordo com as seleções atuais do usuário.  
> Isso permite, por exemplo, que ao selecionar um gênero, apenas os atores que atuaram nesse gênero fiquem disponíveis no filtro de atores (e vice-versa).  
>  
> Para isso, os filtros aplicam a função `filter_df_by_list_contains`, que verifica se qualquer item da lista do usuário está contido nos itens da coluna (`Genre` ou `Actors`).

> 💡 **Aplicação dos Filtros no DataFrame:**  
> Após o ajuste dos filtros, o dataframe é filtrado por:
> - Intervalo de anos escolhido no slider
> - Atores e/ou gêneros selecionados  
> Isso resulta no dataframe `df_filtered`, base principal usada no restante do dashboard.

--

> 💡 **`ensure_list_format`:**  
> Converte valores que são `str` em listas (usando split por vírgula), ou retorna listas já existentes.  
> Garante consistência no formato dos dados para aplicar filtros de forma robusta.

> 💡 **`clean_list_items`:**  
> Percorre listas e aplica `.strip()` em cada item, removendo espaços em branco indesejados.

> 💡 **`filter_df_by_list_contains`:**  
> Recebe um dicionário de filtros (`{"Actors": [...], "Genre": [...]}`) e aplica uma filtragem em qualquer linha onde **pelo menos um dos termos** está presente (com `lower()` para garantir case-insensitive).  
> Essa função é o coração da lógica de filtragem múltipla.

> 💡  `get_filtered_actors` e `get_filtered_genres`:
> Responsáveis por retornar os valores disponíveis para os filtros dinâmicos da interface, com base nas seleções atuais.  
> Elas utilizam `filter_df_by_list_contains` para refinar as opções de filtro oferecidas ao usuário.
> 💡  `update_selected_genres` e `update_selected_actors`:
> Atualizam o estado de seleção (`st.session_state`) com base nas escolhas do usuário, permitindo reatividade e manutenção da seleção mesmo com re-renderização da interface.


Estrutura:
```
├── case3/
│   ├── app.py
│   ├── functions.py
│   └── sql_queries.py
```

## 🛠️ Como executar

```bash
cd .\case3\ 
streamlit run app.py
```

## 👨‍💻 Author

Developed by Mateus Nitzsche. 
[Blog](https://blog-mmnitzsches-projects.vercel.app/)
 | [Linkedin](https://www.linkedin.com/in/mateusnit/)
 | [Github](https://github.com/mmnitzsche/)
