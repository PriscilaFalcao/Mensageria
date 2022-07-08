from unicodedata import name
import pika, os
import sqlite3
import json
cnt = sqlite3.connect("f.db")  

def pdf_process_function(msg): #Função pré-setada com parâmetro
  print(msg)
  teste = json.loads(msg)
  cur = cnt.cursor()
  cur.execute("INSERT INTO Clientes (Nome, CPF, Telefone) VALUES(?,?,?)", (teste['nome'], teste['cpf'], teste['telefone'],))
  cnt.commit()
  return;
  
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

def check(body):
  cur = cnt.cursor()
  cur.execute("SELECT * FROM Bloquilisti")
  print(body)
  return;

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  check(body)

# set up subscription on the queue
channel.basic_consume('hello',
  callback,
  auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()