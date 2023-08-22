import pika
from pydantic_settings import BaseSettings

""" 
    @desc: for more detail about documentation about RabbitMQ and Python. please
    check PIKA https://pika.readthedocs.io/en/stable/modules/adapters/blocking.html?highlight=arguments#pika.adapters.blocking_connection.BlockingChannel.queue_bind
"""


class Exchange(BaseSettings):
    Name: str
    KindOfExchange: str
    BindingKey: str
    ConsumerTag: str
    Durable: bool
    AutoDelete: bool
    Internal: bool
    NoWait: bool
    Arguments: dict
    Mandatory: bool
    Immediate: bool


class Queue(BaseSettings):
    Name: str
    Durable: bool
    AutoDelete: bool
    Exclusive: bool
    NoWait: bool
    Arguments: dict
    PrefetchCount: int
    PrefetchSize: int
    PrefetchGlobal: bool


class Consume(BaseSettings):
    AutoAck: bool
    Exclusive: bool
    NoLocal: bool
    NoWait: bool
    Arguments: dict


class RabbitMQ(BaseSettings):
    Exchange: Exchange
    Queue: Queue
    Consume: Consume
