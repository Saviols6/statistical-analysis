"""
Análise Estatística de Dados com NumPy para a Área de Marketing
Mini-Projeto 3 - Data Science Academy (Fundamentos de Linguagem Python)
Autor: Sávio Giovani

Gera uma massa fictícia de dados de comportamento de usuários de um
e-commerce (visitas, tempo no site, itens no carrinho, valor da compra),
calcula estatísticas descritivas, segmenta clientes e analisa correlações
entre as variáveis.

As perguntas de negócio respondidas por este script estão documentadas em
ANALISE.md, junto com os insights extraídos de cada etapa.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Semente fixa para reprodutibilidade dos resultados
np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Geração dos dados fictícios
# ---------------------------------------------------------------------------
# Conjunto de dados para 1200 usuários, com 4 métricas cada:
#   visitas            -> nº de visitas ao site no mês
#   tempo_no_site       -> tempo total (min) no site
#   itens_no_carrinho  -> nº de itens adicionados ao carrinho
#   valor_compra        -> valor total (R$) da compra no mês

num_usuarios = 1200

# 1. Número de visitas (entre 1 e 50)
visitas = np.random.randint(1, 51, size=num_usuarios)

# 2. Tempo no site (distribuição normal, correlacionado com as visitas)
# Média de 20 min, desvio padrão de 5, com um bônus por visita
tempo_no_site = np.random.normal(loc=20, scale=5, size=num_usuarios) + (visitas * 0.5)
tempo_no_site = np.round(tempo_no_site, 2)

# 3. Número de itens no carrinho (dependente das visitas e do tempo)
# Usuários que visitam mais e passam mais tempo tendem a adicionar mais itens
itens_no_carrinho = np.random.randint(0, 8, size=num_usuarios) + (visitas // 10)
# Garante que o tempo no site também influencie positivamente
itens_no_carrinho = itens_no_carrinho + (tempo_no_site // 15).astype(int)

# 4. Valor da compra (correlacionado com os itens no carrinho)
# Preço médio por item de R$ 50, com alguma variação aleatória
valor_compra = (itens_no_carrinho * 50) + np.random.normal(loc=0, scale=10, size=num_usuarios)

# Se não houver itens no carrinho, o valor da compra deve ser 0
valor_compra[itens_no_carrinho == 0] = 0
valor_compra[valor_compra < 0] = 0  # corrige eventuais valores negativos
valor_compra = np.round(valor_compra, 2)

# Une tudo em uma única matriz: cada linha = 1 usuário, cada coluna = 1 métrica
# Colunas: [Visitas, Tempo no Site (min), Itens no Carrinho, Valor da Compra (R$)]
dados_ecommerce = np.column_stack((visitas, tempo_no_site, itens_no_carrinho, valor_compra))

print("\nFormato da massa de dados:", dados_ecommerce.shape)
print("\nExemplo dos 5 primeiros usuários (linhas):")
print("\nColunas: [Visitas, Tempo no Site (min), Itens no carrinho, Valor da compra (R$)]\n")
print(dados_ecommerce[:5])


# ---------------------------------------------------------------------------
# 2. Análise Estatística Descritiva
# ---------------------------------------------------------------------------
# Pergunta 1: Qual é o perfil médio do nosso usuário em termos de visitas,
# tempo de navegação e valor de compra (ticket médio)?

visitas_col = dados_ecommerce[:, 0]
tempo_col = dados_ecommerce[:, 1]
itens_col = dados_ecommerce[:, 2]
valor_col = dados_ecommerce[:, 3]

print("--- ANÁLISE ESTATÍSTICA GERAL ---")

# Média
media_visitas = np.mean(visitas_col)
media_tempo = np.mean(tempo_col)
media_itens = np.mean(itens_col)
media_valor = np.mean(valor_col)

print(f"\nMédia de Visitas: {media_visitas:.2f}")
print(f"\nMédia de tempo no site: {media_tempo:.2f}")
print(f"\nMédia de itens no carrinho: {media_itens:.2f}")
print(f"\nTicket médio: R${media_valor:.2f}")

# Mediana (valor central, menos sensível a outliers)
mediana_valor = np.median(valor_col)
print(f"\nMediana do valor de compra: {mediana_valor:.2f}")

# Desvio padrão (mede a dispersão dos dados)
std_valor = np.std(valor_col)
print(f"\nDesvio padrão do valor de compra: {std_valor:.2f}")

# Valores máximos e mínimos
max_valor = np.max(valor_col)
min_valor = np.min(valor_col[valor_col > 0])
print(f"Maior valor de compra: R${max_valor:.2f}")
print(f"Menor valor de compra: R${min_valor:.2f}")

# Histograma da distribuição dos valores de compra, com média, mediana
# e faixa de +/- 1 desvio padrão destacados
plt.figure(figsize=(12, 5))
plt.hist(valor_col, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.axvline(media_valor, color='red', linestyle='--', linewidth=2,
            label=f'Média = R${media_valor:.2f}')
plt.axvline(mediana_valor, color='orange', linestyle='--', linewidth=2,
            label=f'Mediana = R${mediana_valor:.2f}')
plt.axvline(media_valor + std_valor, color='green', linestyle=':', linewidth=2,
            label=f'+1 DP = R${media_valor + std_valor:.2f}')
plt.axvline(media_valor - std_valor, color='green', linestyle=':', linewidth=2,
            label=f'-1 DP = R${media_valor - std_valor:.2f}')
plt.title('Distribuição dos valores de compra')
plt.xlabel('Valor da compra (R$)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('distribuicao_valores_compra.png', dpi=150, bbox_inches='tight')
plt.show()


# ---------------------------------------------------------------------------
# 3. Segmentação e Análise de Clientes
# ---------------------------------------------------------------------------

# Pergunta 2: Quais são as características e comportamentos distintos dos
# nossos clientes de "Alto Valor"? Eles visitam mais o site? Passam mais
# tempo navegando?
clientes_alto_valor = dados_ecommerce[dados_ecommerce[:, 3] > 250]

print("\n--- ANÁLISE: CLIENTES DE ALTO VALOR (COMPRAS > R$250) ---")
print(f"Número de clientes de alto valor: {clientes_alto_valor.shape[0]}")

media_visitas_alto_valor = np.mean(clientes_alto_valor[:, 0])
media_tempo_alto_valor = np.mean(clientes_alto_valor[:, 1])

print(f"Média de visitas: {media_visitas_alto_valor:.2f}")
print(f"Média de tempo: {media_tempo_alto_valor:.2f}")

# Pergunta 3: Qual é o comportamento dos usuários que visitam o site, mas
# não realizam nenhuma compra? Onde está a oportunidade de conversão com
# este grupo?
visitantes_sem_compra = dados_ecommerce[dados_ecommerce[:, 3] == 0]

print("\n--- ANÁLISE: VISITANTES QUE NÃO COMPRAM ---")
print(f"Número de visitantes: {visitantes_sem_compra.shape[0]}")

media_tempo_sem_compra = np.mean(visitantes_sem_compra[:, 1])
media_visitas_sem_compra = np.mean(visitantes_sem_compra[:, 0])

print(f"Média de visitas: {media_visitas_sem_compra:.2f}")
print(f"Apesar de não comprarem, eles passam em média {media_tempo_sem_compra:.2f} min na plataforma")


# ---------------------------------------------------------------------------
# 4. Análise de Correlação
# ---------------------------------------------------------------------------
# Pergunta 4: Existe uma correlação estatisticamente relevante entre o tempo
# gasto no site, o número de itens no carrinho e o valor final da compra?

# np.corrcoef calcula a matriz de correlação;
# rowvar=False indica que as colunas são as variáveis
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar=False)

print("\n--- MATRIZ DE CORRELAÇÃO ---")
print("[Visitas, Tempo, Itens, Valor]\n")
print(np.round(matriz_correlacao, 2))

# Versão gráfica da matriz de correlação (mapa de calor)
nomes_variaveis = ["Visitas", "Tempo no site", "Itens no carrinho", "Valor da compra"]
df_correlacao = pd.DataFrame(matriz_correlacao, index=nomes_variaveis, columns=nomes_variaveis)

plt.figure(figsize=(7, 5))
sns.heatmap(df_correlacao, annot=True, cmap="Blues", fmt=".2f")
plt.savefig('matriz_correlacao.png', dpi=150, bbox_inches='tight')
plt.show()
