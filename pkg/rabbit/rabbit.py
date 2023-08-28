import pika
from app.config.config import GetSettings

settings = GetSettings()


def RabbitMQConnection() -> pika.BlockingConnection:
    connection_params = pika.ConnectionParameters(
        host=settings.Rabbitmq.Host,  # RabbitMQ server hostname or IP address
        port=settings.Rabbitmq.Port,  # RabbitMQ server port (default is 5672)
        virtual_host='/',  # RabbitMQ virtual host (default is '/')
        credentials=pika.PlainCredentials(
            username=settings.Rabbitmq.User,  # RabbitMQ username (default is 'guest')
            password=settings.Rabbitmq.Password  # RabbitMQ password (default is 'guest')
        ),
        heartbeat=0,  # Heartbeat interval in seconds (0 disables)
        blocked_connection_timeout=None,  # Connection timeout for blocked resources
    )
    # Establish a connection to RabbitMQ server
    connection = pika.BlockingConnection(connection_params)
    return connection
