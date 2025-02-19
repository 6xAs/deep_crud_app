# responsável por exibir os dados e interagir com o usuário:
import streamlit as st
from controllers.UserController import UserController

class UserView:
    def __init__(self):
        self.user_controller = UserController()
    
    def show_users(self):
        users = self.user_controller.read_users()
        st.write(users)
    
    def create_user_form(self):
        with st.form("create_user_form"):
            # Campos para criar um novo usuário
            name = st.text_input("Name")
            email = st.text_input("Email")
            # Botão para criar o usuário
            submit = st.form_submit_button("Criar Usuário")
            # Se o botão for clicado, cria o usuário
            if submit:
                self.user_controller.create_user(name, email)
                st.success("Usuário criado com sucesso!")
    
    def update_user_form(self):
        # Campos para atualizar um usuário existente pelo ID
        user_id = st.number_input("User ID to Update", min_value=1)
        name = st.text_input("Name")
        email = st.text_input("Email")
        # Botão para atualizar o usuário
        if st.button("Atualizar Usuário"):
            result = self.user_controller.update_user(user_id, name, email)
            if result is not None:
                st.success("Usuário atualizado com sucesso!")
            else:
                st.error("Usuário não encontrado!")
                
    def delete_user_form(self):
        # Campo para excluir um usuário pelo ID
        user_id     = st.number_input("User ID to Delete", min_value=1)
        if st.button("Deletar Usuário"):
            # Chamada ao método delete_user do controlador
            result      = self.user_controller.delete_user(user_id)
            if result:
                st.success("Usuário excluído com sucesso!")
            else:
                st.error("Usuário não encontrado!")
        