# Intermediará a comunicação entre a View e o Model
from models.User import User

class UserController:
    #  Inicializa o modelo User
    def __init__(self):
        # Instancia o modelo User
        self.user_model = User()
    
    # Métodos para interagir com o modelo User
    def create_user(self, name, email):
        # Chama o método create_user do modelo User
        return self.user_model.create_user(name, email)
    
    def read_users(self):
        # Chama o método read_users do modelo User
        return self.user_model.read_users()

    def update_user(self, user_id, name=None, email=None):
        return self.user_model.update_user(user_id, name, email)

    def delete_user(self, user_id):
        return self.user_model.delete_user(user_id)
        