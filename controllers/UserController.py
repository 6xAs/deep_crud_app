# Intermediará a comunicação entre a View e o Model
from models.User import UserModel
import streamlit as st

class UserController:
    def __init__(self):
        self.model = UserModel()
    
    def create_user(self, name, email, age):
        return self.model.create_user(name, email, age)
    
    def read_users(self):
        return self.model.read_users()
    
    def update_user(self, user_id, name, email, age):
        return self.model.update_user(user_id, name, email, age)
    
    def delete_user(self, user_id):
        return self.model.delete_user(user_id)