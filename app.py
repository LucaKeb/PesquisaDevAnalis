import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar e preparar os dados
@st.cache_data
def load_data():
    df = pd.read_csv('Pesquisa Desenvolvedores - Respostas ao formulário 1.csv')
    df.columns = [
        'Timestamp', 'Faixa de Idade', 'Gênero', 'Escolaridade', 'Tempo de Carreira',
        'Ano Início TI', 'Qtd Empresas', 'Cargo Atual', 'Regime de Trabalho',
        'Modalidade de Trabalho', 'Faixa Salarial', 'Linguagem Principal',
        'Forma de Estudo', 'Cursos Contínuos', 'Importância Socializar',
        'Canais de Aprendizado', 'Projetos Open Source', 'Habilidade Social',
        'Maior Dificuldade', 'Região', 'Comentários'
    ]

    # Limpeza da coluna de Linguagem Principal
    def clean_language(lang):
        lang = str(lang).lower().strip()
        if '/' in lang:
            lang = lang.split('/')[0].strip()
        if 'jaca' in lang:
            return 'java'
        if 'typescript' in lang or 'ts' in lang:
            return 'typescript'
        return lang

    df['Linguagem Principal'] = df['Linguagem Principal'].apply(clean_language)
    return df

# Título do Dashboard
st.title('Dashboard da Pesquisa de Desenvolvedores')

# Carregar os dados
df = load_data()

# dados brutos
if st.checkbox('Mostrar dados brutos'):
    st.write(df)

# Insights
st.header('Principais Insights')
st.markdown("""
* **Perfil dos Respondentes:** A maioria dos desenvolvedores está na faixa etária de **18 a 24 anos** e **25 a 34 anos**.
* **Senioridade e Salário:** Há uma clara progressão salarial com a senioridade. Desenvolvedores **Sênior, Tech Leads e CTOs** concentram as maiores faixas salariais, acima de **R$ 8.000,00**.
* **Tecnologias Populares:** As linguagens mais citadas, após a limpeza dos dados, foram **Java, PHP e TypeScript**.
* **Modalidade de Trabalho:** A preferência por trabalho **remoto** e **presencial** está bem dividida, com o modelo **híbrido** aparecendo como uma terceira via.
* **Região:** A maioria dos respondentes reside na região **Sul**, seguida pela **Sudeste**.
""")

# Visualizações
st.header('Visualizações dos Dados')

# Gráfico de Faixa Salarial
st.subheader('Distribuição de Faixa Salarial')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.countplot(y=df['Faixa Salarial'], order = df['Faixa Salarial'].value_counts().index, ax=ax1)
ax1.set_title('Distribuição de Faixa Salarial')
ax1.set_xlabel('Contagem')
ax1.set_ylabel('Faixa Salarial')
st.pyplot(fig1)

# Gráfico de Cargo Atual
st.subheader('Distribuição de Cargo Atual')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.countplot(y=df['Cargo Atual'], order = df['Cargo Atual'].value_counts().index, ax=ax2)
ax2.set_title('Distribuição de Cargo Atual')
ax2.set_xlabel('Contagem')
ax2.set_ylabel('Cargo Atual')
st.pyplot(fig2)

# Gráfico de Linguagem Principal
st.subheader('Distribuição de Linguagem Principal')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.countplot(y=df['Linguagem Principal'], order = df['Linguagem Principal'].value_counts().index, ax=ax3)
ax3.set_title('Distribuição de Linguagem Principal')
ax3.set_xlabel('Contagem')
ax3.set_ylabel('Linguagem Principal')
st.pyplot(fig3)

# Gráfico de Modalidade de Trabalho
st.subheader('Distribuição de Modalidade de Trabalho')
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.countplot(x=df['Modalidade de Trabalho'], order = df['Modalidade de Trabalho'].value_counts().index, ax=ax4)
ax4.set_title('Distribuição de Modalidade de Trabalho')
ax4.set_xlabel('Modalidade de Trabalho')
ax4.set_ylabel('Contagem')
st.pyplot(fig4)

# Heatmap de Cargo vs. Salário
st.subheader('Relação entre Cargo Atual e Faixa Salarial')
cargo_salario = pd.crosstab(df['Cargo Atual'], df['Faixa Salarial'])
fig5, ax5 = plt.subplots(figsize=(12, 8))
sns.heatmap(cargo_salario, annot=True, cmap="YlGnBu", fmt='g', ax=ax5)
ax5.set_title('Cargo Atual vs. Faixa Salarial')
ax5.set_xlabel('Faixa Salarial')
ax5.set_ylabel('Cargo Atual')
st.pyplot(fig5)