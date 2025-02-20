import streamlit as st
from views.UserView import UserView

st.title("Atualizar Usuário")
# Cria uma instância da classe UserView
view = UserView()
# Chamada ao método update_user_form do controlador
view.update_user_form()