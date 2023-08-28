import pika
from pydantic import BaseModel
from typing import Union

""" 
    @desc: for more detail about documentation about RabbitMQ and Python. please
    check PIKA https://pika.readthedocs.io/en/stable/modules/adapters/blocking.html?highlight=arguments#pika.adapters.blocking_connection.BlockingChannel.queue_bind
"""


class Exchange(BaseModel):
    Name: str
    KindOfExchange: str
    BindingKey: str
    ConsumerTag: str
    Durable: bool
    AutoDelete: bool
    Internal: bool
    NoWait: bool
    Arguments: Union[dict, None]
    Mandatory: bool
    Immediate: bool


class Queue(BaseModel):
    Name: str
    Durable: bool
    AutoDelete: bool
    Exclusive: bool
    NoWait: bool
    Arguments: Union[dict, None]
    PrefetchCount: int
    PrefetchSize: int
    PrefetchGlobal: bool


class Consume(BaseModel):
    AutoAck: bool
    Exclusive: bool
    NoLocal: bool
    NoWait: bool
    Arguments: Union[dict, None]


class RabbitMQ(BaseModel):
    exchange: Exchange
    queue: Queue
    consume: Consume
