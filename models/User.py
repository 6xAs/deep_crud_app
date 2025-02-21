import pandas as pd
import streamlit as st
import sqlite3
import os

class UserModel:
    def __init__(self):
        self.csv_path   = "data/users.csv"
        self.db_path    = "data/users.db"
        self._init_storage()
    
    def _init_storage(self):
        # Inicializa o SQLite 
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                age INTEGER
            )
            ''')
        self.conn.commit()
   
        
        # Inicializa o CSV
        if not os.path.exists(self.csv_path):
            df = pd.DataFrame(columns=['id', 'name', 'email', 'age'])
            df.to_csv(self.csv_path, index=False)
            
    def _sync_to_csv(self):
        # Atualiza o CSV com dados do banco 
        df = pd.read_sql('SELECT * FROM users', self.conn)
        df.to_csv(self.csv_path, index=False)
    
    def create_user(self, name, email, age):
        # SQLite
        self.cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
        self.conn.commit()
        
        # CSV
        # Gera um novo ID único para o novo usuário
        new_id = self.cursor.lastrowid
        # Cria um novo DataFrame com os dados do novo usuário
        new_user = pd.DataFrame([[new_id, name, email, age]], columns=['id', 'name', 'email', 'age'])
        # Adiciona o novo usuário ao DataFrame existente
        df = pd.read_csv(self.csv_path)
        # Adiciona o novo usuário ao DataFrame existente
        df = pd.concat([df, new_user], ignore_index=True)
        # Salva o DataFrame atualizado no arquivo CSV
        df.to_csv(self.csv_path, index=False)
        
        return new_id
    
    def read_users(self):
        return pd.read_sql('SELECT * FROM users', self.conn)
    
    def update_user(self, user_id, name, email, age):
        # SQLite
        self.cursor.execute('''
                            
            UPDATE users
            SET name=?, email=?, age=?
            WHERE id=?
        ''', (name, email, age, user_id))
        self.conn.commit()
        
        # CSV
        df = pd.read_csv(self.csv_path)
        mask = df['id'] == user_id
        if mask.any():
            df.loc[mask, 'name']    = name
            df.loc[mask, 'email']   = email
            df.loc[mask, 'age']     = age
            df.to_csv(self.csv_path, index=False)
        
        return self.cursor.rowcount > 0
    
    def delete_user(self, user_id):
        # SQLite
        self.cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
        self.conn.commit()

        # CSV
        df = pd.read_csv(self.csv_path)
        df = df[df['id'] != user_id]
        df.to_csv(self.csv_path, index=False)
        
        return self.cursor.rowcount > 0
    
    def __del__(self):
        self.conn.close()
    
    