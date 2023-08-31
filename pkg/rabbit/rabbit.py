import pika
from app.config.config import GetSettings
from typing import Any
import json

settings = GetSettings()


class RabbitMQPackage:

    def __init__(
            self,
            host: str,  # RabbitMQ server hostname or IP address
            port: int,  # RabbitMQ server port (default is 5672)
            virtual_host: str,  # RabbitMQ virtual host (default is '/')
            c_username: str,  # RabbitMQ username (default is 'guest')
            c_password: str,  # RabbitMQ password (default is 'guest')
            heartbeat: int,  # Heartbeat interval in seconds (0 disables)
            blocked_connection_timeout: int | float | None,  # Connection timeout for blocked resources
    ):
        self.__host: str = host
        self.__port: int = port
        self.__virtual_host: str = virtual_host
        self.__c_username: str = c_username
        self.__c_password: str = c_password
        self.__heartbeat: int = heartbeat
        self.__blocked_connection_timeout: int | float | None = blocked_connection_timeout

    def connection(self) -> pika.BlockingConnection:
        connection_params: pika.ConnectionParameters
        connection: pika.BlockingConnection

        connection_params = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            virtual_host=self.__virtual_host,
            credentials=pika.PlainCredentials(
                username=self.__c_username,
                password=self.__c_password,
            ),
            heartbeat=self.__heartbeat,
            blocked_connection_timeout=self.__blocked_connection_timeout,
        )

        # Establish a connection to RabbitMQ server
        connection = pika.BlockingConnection(connection_params)
        print(f"connection {connection}")
        return connection

    def publisher_rabbit(
            self,
            exchange_name: str,
            exchange_type: str,
            exchange_binding_key: str,
            exchange_consumer_tag: str,
            exchange_durable: bool,
            exchange_auto_delete: bool,
            exchange_internal: bool,
            queue_name: str,
            payload: bytes,
    ) -> Any:
        channel: pika.BlockingConnection = self.connection()
        channel_connection = channel.channel()
        print(f"on to send message Exchange: {exchange_name} with Routing key: {exchange_binding_key}, Queue: {queue_name}")
        channel_connection.exchange_declare(
            exchange=exchange_name,
            exchange_type=exchange_type,
            durable=exchange_durable,
            auto_delete=exchange_auto_delete,
            internal=exchange_internal,
        )
        channel_connection.queue_bind(
            queue=queue_name,
            exchange=exchange_name,
            routing_key=exchange_binding_key,
        )
        channel_connection.basic_publish(
            exchange=exchange_name,
            routing_key=exchange_binding_key,
            body=payload
        )
        print(f"Success to send message Exchange: {exchange_name} with Routing key: {exchange_binding_key}, Queue: {queue_name}")
        return True
