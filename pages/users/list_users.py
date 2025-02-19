import streamlit as st
from views.UserView import UserView

st.title("Lista de Usuários")
# Cria uma instância da classe UserView
view = UserView()
#  Chamada ao método show_users do controlador
view.show_users()