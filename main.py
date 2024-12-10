import pandas as pd 
import streamlit as st 

base = pd.read_csv("titanic_train.csv")

df = pd.DataFrame(base)

st.title("Selecionar lista")
st.dataframe(df)



# nome = st.chat_input("1 ou 0")


opcoes = st.multiselect(
    "Escolha várias opções:",
    base["Name"].tolist()
)
if opcoes:  # Verificar se há opções selecionadas
    st.dataframe(base[base["Name"].isin(opcoes)])
    st.write(f"{opcoes}")
else:
    st.write("Nenhuma opção selecionada.")
