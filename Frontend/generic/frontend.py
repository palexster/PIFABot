import yaml
import os
import pika




class Frontend():

    necessary_information = [
        "FE_CLASS",
        "ACTIONS_QUEUE_ADDRESS",
        "ACTIONS_QUEUE_TYPE",
        "ACTIONS_EXCHANGE_NAME"
    ]

    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv("ACTIONS_QUEUE_ADDRESS")))
        self.channel = connection.channel()
        exchange_name = os.getenv("ACTIONS_EXCHANGE_NAME")
        self.channel.exchange_declare(exchange='logs',exchange_type=os.getenv("ACTIONS_QUEUE"))
        result = self.channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange='logs',
                   queue=queue_name)
        self.channel.basic_consume(self.callback,queue=queue_name,no_ack=True)
        self.channel.start_consuming()

    @staticmethod
    def instantiateFE() -> 'Frontend':
        F = None
        for param in Frontend.necessary_information:
            if not os.getenv(param):
                raise EnvironmentError("The %s parameter is missing", param)

        type = os.getenv("FE_CLASS")

        if type == "Telegram":
            from telegram import TelegramFrontend
            F = TelegramFrontend()

        return F


    def callback(self, ch, method, properties, body):
        print(" [x] %r" % body)
