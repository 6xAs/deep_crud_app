import streamlit as st
from views.UserView import UserView

st.title("Deletar Usuário")
# Cria uma instância da classe UserView
view = UserView()
# Chamada ao método delete_user_form do controlador
view.delete_user_form()