import pika

class Listener:
    def __init__(self):
        self.connection = None
        self.channel = None

    def initConnection(self, url):
        params = pika.URLParameters(url)
        self.connection = pika.BlockingConnection(params)

    def openChannel(self, queueName):
        self.channel = self.connection.channel() # start a channel
        self.channel.queue_declare(queue=queueName) # Declare a queue

    def listenerMessage(self, callback, queue):
        self.channel.basic_consume(queue,
            callback,
            auto_ack=True)

    def startConsuming(self):
        self.channel.start_consuming()

    def closeConnection(self):
        self.connection.close()

