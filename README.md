#  Dashboard de Gastos Pessoais

Este projeto é um dashboard interativo criado com **Streamlit** para visualizar e analisar seus **gastos mensais** de forma simples e intuitiva.

---

## Tecnologias utilizadas

- Python 🐍
- Pandas 📊
- Plotly 📈
- Streamlit 🌐

---

##  Estrutura do projeto

```
gastos_dashboard/
├── dashboard.py
├── requirements.txt
├── README.md
└── dados/
    └── gastos.csv
```

---

##  Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd gastos_dashboard
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o dashboard:

```bash
streamlit run dashboard.py
```

---

##  O que o dashboard exibe

- Total de gastos no período
- Evolução dos gastos por mês (linha)
- Distribuição por categoria (pizza)
- Tabela de despesas detalhadas
- Filtros por mês e categoria
- Suporte a upload de CSV

---

## Exemplo de CSV

```csv
data,descricao,categoria,valor
2025-01-10,Supermercado,Alimentação,250.00
2025-01-11,Uber,Transporte,45.00
...
```

---


## 📌 Licença

Este projeto está sob a licença MIT.
