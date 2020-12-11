from typing import Dict
from pydantic import BaseModel

## Bloque 1: definición de UserInDB
class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

# Bloque 2: definición de  la base de datos ficticia

database_users = Dict[str, UserInDB]

database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "balance":12000}),
                               
    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000}),
}

## Bloque 3: definición de funciones sobre la base de datos fictica
    #Obtener usuario

def get_user(username:str):
    if username in database_users.keys():
        return database_users[username]
    else : 
        return None
    #Actualizar usuario
def update_user(user_in_db:UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db