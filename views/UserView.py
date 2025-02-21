# views/user_view.py
import streamlit as st
from controllers.UserController import UserController

class UserView:
    # Inicializa o controlador
    def __init__(self):
        self.controller = UserController()
    
    def show_users(self):
        users = self.controller.read_users()
        if not users.empty:
            st.dataframe(users)
        else:
            st.info("Nenhum usuário cadastrado!")
    
    def create_user_form(self):
        with st.form("create_user_form"):
            name = st.text_input("Nome completo")
            email = st.text_input("E-mail")
            age = st.number_input("Idade", min_value=0, max_value=120)
            submitted = st.form_submit_button("Cadastrar")
            
            if submitted:
                # Validação simples (exemplo)
                if not name or not email:
                    st.error("Preencha nome e e-mail!")
                else:
                    self.controller.create_user(name, email, age)
                    st.success("Usuário cadastrado com sucesso!")
        
    def update_user_form(self):
        with st.form("update_user_form"):
            user_id = st.number_input("ID do usuário", min_value=1)
            name = st.text_input("Novo nome")
            email = st.text_input("Novo e-mail")
            age = st.number_input("Nova idade", min_value=0, max_value=120)
            submitted = st.form_submit_button("Atualizar")
            
            if submitted:
                success = self.controller.update_user(user_id, name, email, age)
                if success:
                    st.success("Usuário atualizado!")
                    #st.rerun()
                else:
                    st.error("ID não encontrado!")
    
    def delete_user_form(self):
        with st.form("delete_user_form"):
            user_id = st.number_input("ID do usuário", min_value=1)
            submitted = st.form_submit_button("Excluir")
            
            if submitted:
                success = self.controller.delete_user(user_id)
                if success:
                    st.success("Usuário excluído!")
                    #st.rerun()
                else:
                    st.error("ID não encontrado!")
