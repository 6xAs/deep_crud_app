import pandas as pd

class UserModel:
    def __init__(self):
        self.users = pd.DataFrame(columns=['id', 'name', 'email'])
        
    def create_user(self, name, email):
        # Cria um novo usuário e adiciona ao DataFrame
        new_user = pd.DataFrame([[len(self.users), name, email]], columns=['id', 'name', 'email'])
        # Concatena o novo usuário ao DataFrame existente
        self.users = pd.concat([self.users, new_user], ignore_index=True)
        # Retorna o novo usuário criado
        return new_user
    
    def read_users(self):
        return self.users

    def update_user(self, user_id, name=None, email=None):
        if user_id in self.users['id'].values:
            if name:
                self.users.loc[self.users['id'] == user_id, 'name'] = name
            if email:
                self.users.loc[self.users['id'] == user_id, 'email'] = email
            return self.users.loc[self.users['id'] == user_id]
        return None
    
    def delete_user(self, user_id):
        # Verifica se o usuário existe antes de tentar excluir
        if user_id in self.users['id'].values:
            # Remove o usuário da lista de usuários
            self.users = self.users[self.users['id'] != user_id]
            return True
        return False
        