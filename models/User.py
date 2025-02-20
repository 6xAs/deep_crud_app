import pandas as pd
import streamlit as st

class UserModel:
    def __init__(self):
        if 'users' not in st.session_state:
            st.session_state.users = pd.DataFrame(columns=['id', 'name', 'email', 'age'])
    
    def create_user(self, name, email, age):
        # Gera um novo ID único para o novo usuário
        new_id = len(st.session_state.users) + 1
        # Cria um novo DataFrame com os dados do novo usuário
        new_user = pd.DataFrame([[new_id, name, email, age]], columns=['id', 'name', 'email', 'age'])
        # Adiciona o novo usuário ao DataFrame existente
        st.session_state.users = pd.concat([st.session_state.users, new_user], ignore_index=True)
        return new_user
    
    def read_users(self):
        return st.session_state.users
    
    def update_user(self, user_id, name=None, email=None, age=None):
        if user_id in st.session_state.users['id'].values:
            idx = st.session_state.users.index[st.session_state.users['id'] == user_id].tolist()[0]
            if name:
                st.session_state.users.at[idx, 'name'] = name
            if email:
                st.session_state.users.at[idx, 'email'] = email
            if age:
                st.session_state.users.at[idx, 'age'] = age
            return True
        return False
    
    def delete_user(self, user_id):
        if user_id in st.session_state.users['id'].values:
            st.session_state.users = st.session_state.users[st.session_state.users['id'] != user_id]
            st.session_state.users.reset_index(drop=True, inplace=True)
            return True
        return False