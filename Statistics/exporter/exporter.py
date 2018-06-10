import pika
import os

class Exporter():

    necessary_information = [
        "EX_CLASS",
        "ACTIONS_QUEUE_ADDRESS",
        "ACTIONS_QUEUE_TYPE",
        "ACTIONS_EXCHANGE_NAME"
    ]

    def __init__(self):
        pass

    def initPublish(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=os.getenv("ACTIONS_EXCHANGE_NAME"),
                         exchange_type=os.getenv("ACTIONS_EXCHANGE_TYPE"))

    def publish(self, message):
        self.channel.basic_publish(exchange=os.getenv("ACTIONS_EXCHANGE_NAME"),
                              routing_key='',
                              body=message)
        #connection.close()


    @staticmethod
    def instantiateEX() -> 'EXPORTER':
        F = None
        for param in Exporter.necessary_information:
            if not os.getenv(param):
                raise EnvironmentError("The %s parameter is missing", param)

        type = os.getenv("FE_CLASS")

        if type == "Telegram":
            from statistics import StatisticsExporter
            F = TelegramFrontend()

        return F

