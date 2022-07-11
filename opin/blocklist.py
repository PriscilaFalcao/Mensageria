
from unicodedata import name
import pika, os
import sqlite3
import json
cnt = sqlite3.connect("Clientes.db")  

def check(msg):
  cur = cnt.cursor()
  print(msg)
  teste = json.loads(msg)
  cur.execute("SELECT CPF FROM Blocklist WHERE CPF = ?"), (teste['cpf'])
  #if block == 
  #   register(body)
  return;