import streamlit as st

# Configuração da página
st.set_page_config(page_title="Deep CRUD App")

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Listar Usuários", "Criar Usuário", "Atualizar Usuário", "Deletar Usuário"])

if selection == "Listar Usuários":
    # Listar Usuários
    st.switch_page("pages/users/list_users")
    
elif selection == "Criar Usuário":
    # Criar Usuário
    st.switch_page("pages/users/create_user")
    
elif selection == "Atualizar Usuário":
    # Atualizar Usuário
    st.switch_page("pages/users/update_user")
    
elif selection == "Deletar Usuário":
    # Deletar Usuário
    st.switch_page("pages/users/delete_user")

