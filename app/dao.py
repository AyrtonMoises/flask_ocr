from ext.database import mongo 
from bson.objectid import ObjectId


STATUS_PENDENTE = 'pendente'
STATUS_SUCESSO = 'sucesso'
STATUS_FALHA = 'falha'

leituras = mongo.db.leituras

def insert_leitura(arquivo):
    return leituras.insert_one({'arquivo': arquivo, 'status': STATUS_PENDENTE })

def atualizar_leitura(id_leitura, cpf, novo_status):
    leituras.update_one(
        {'_id': ObjectId(id_leitura)},
        {"$set": { 'status': novo_status, 'cpf': cpf }}
    , upsert=False)

def get_leitura(id_leitura):
    return leituras.find_one({"_id": ObjectId(id_leitura)})

def all_leituras():
    return leituras.find()