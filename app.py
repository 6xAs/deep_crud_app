import streamlit as st
from views.UserView import UserView

# Configuração da página
st.set_page_config(page_title="Deep CRUD App")

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Listar Usuários", "Criar Usuário", "Atualizar Usuário", "Deletar Usuário"])


# Listar Usuários
if selection == "Listar Usuários":
    st.title("Lista de Usuários")
    # Cria uma instância da classe UserView
    view = UserView()
    #  Chamada ao método show_users do controlador
    view.show_users()
    
        
