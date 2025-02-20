import streamlit as st
from views.UserView import UserView

def main():
    st.sidebar.title("Menu de Navegação")
    page = st.sidebar.radio("Selecione a página:", ["Listar Usuários", "Cadastrar Usuário", "Editar Usuário", "Excluir Usuário"])
    
    view = UserView()
    
    if page == "Listar Usuários":
        st.title("📋 Lista de Usuários")
        view.show_users()
    
    elif page == "Cadastrar Usuário":
        st.title("➕ Cadastrar Novo Usuário")
        view.create_user_form()
    
    elif page == "Editar Usuário":
        st.title("✏️ Editar Usuário")
        view.update_user_form()
    
    elif page == "Excluir Usuário":
        st.title("🗑️ Excluir Usuário")
        view.delete_user_form()

if __name__ == "__main__":
    main()