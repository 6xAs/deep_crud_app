import streamlit as st
from views.UserView import UserView

st.title("Criar Usuário")
# Cria uma instância da classe UserView
view = UserView()
# Chamada ao método create_user_form do controlador
view.create_user_form()
