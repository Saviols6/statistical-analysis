# statistical-analysis

# 📊 Análise Estatística de Dados com NumPy para Marketing

Mini-Projeto desenvolvido no curso **Fundamentos de Linguagem Python — Do Básico a Aplicações de IA** (Data Science Academy).

Simulação e análise estatística de dados de comportamento de usuários em um e-commerce (visitas, tempo no site, itens no carrinho e valor de compra), usando **NumPy** como ferramenta central, com visualizações em Matplotlib/Seaborn.

## 🎯 Objetivo

Segmentar clientes e identificar quais indicadores de comportamento (visitas, tempo no site, itens no carrinho) mais se relacionam com o valor final de compra, gerando insights acionáveis para marketing e produto.

## ❓ Perguntas de negócio respondidas

1. Qual é o perfil médio do usuário (visitas, tempo de navegação, ticket médio)?
2. Quais características distinguem os clientes de "Alto Valor"?
3. Como se comportam os visitantes que não compram?
4. Existe correlação relevante entre tempo no site, itens no carrinho e valor da compra?

As respostas completas, com os insights e ressalvas metodológicas, estão em **[ANALISE.md](ANALISE.md)**.

## 🛠️ Tecnologias

- Python 3
- NumPy — geração dos dados, estatística descritiva, indexação booleana e correlação
- Pandas — apenas para rotular a matriz de correlação em um DataFrame
- Matplotlib / Seaborn — visualizações (histograma e heatmap)

## 📁 Estrutura do repositório

```
.
├── analise.py      # Código Python completo (geração dos dados + análises)
├── ANALISE.md       # Contexto de negócio, perguntas, respostas e insights
└── README.md         # Este arquivo
```

## ▶️ Como executar

```bash
pip install numpy pandas seaborn matplotlib
python analise.py
```

O script imprime as estatísticas no console e gera dois gráficos:
- `distribuicao_valores_compra.png` — histograma dos valores de compra
- `matriz_correlacao.png` — heatmap da matriz de correlação

## 📌 Observação sobre os dados

Os dados usados são **fictícios**, gerados com `numpy.random` (semente fixa `42` para reprodutibilidade) e com dependências propositalmente embutidas entre as variáveis (ex.: valor da compra calculado a partir do número de itens no carrinho). Isso é útil para praticar as técnicas do NumPy, mas significa que algumas correlações (como Itens ↔ Valor = 1,00) refletem a construção do dataset, não um padrão real de comportamento de compra — detalhe explicado em [ANALISE.md](ANALISE.md).

## ✍️ Autor

Sávio Giovani
