from unicodedata import name
import customer as entity
import sqlite_manager as con
import rabbit_listener as pms
import constant
import json

def initAPI():
  con.createSqliteDatabase("", constant.DATABASE_SQLITE)
  l = pms.Listener()
  l.initConnection('amqp://guest:guest@localhost/%2f')
  l.openChannel(constant.QUEUE_NAME)
  l.listenerMessage(getMessage, constant.QUEUE_NAME)
  l.startConsuming()

def insert(msg): #Função pré-setada com parâmetro
  print(msg)
  customerData = json.loads(msg)
  c = entity.Customer(customerData['nome'], customerData['cpf'], 0, customerData['telefone'])
  con.insert("clientes", [["name", "Wiu"], ["identifationCode", "12321"]] )
  print(c)
  return;

# create a function which is called on incoming messages
def getMessage(ch, method, properties, body):
  insert(body)

initAPI()
print(1)