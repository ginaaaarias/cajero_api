# Bloque 1:definición de TransactionInDB

from datetime import datetime
from pydantic import BaseModel

class TransactionInDB(BaseModel):
    id_transaction:int=0
    username:str
    date:datetime=datetime.now()
    value:int
    actual_balance:int

# Bloque 2: definición de la base de datos ficticia y una función
database_transactions=[]
generator={"id":0}
    # Funcin para guardar transacción 
def save_transaction(transaction_in_db:TransactionInDB):
    generator["id"]=generator["id"]+1
    transaction_in_db.id_transaction=generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db