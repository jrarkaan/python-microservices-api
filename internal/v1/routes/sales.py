from fastapi import (
    APIRouter, Depends, Query
)

# Model/ DTO
from pkg.rabbit.model.entity import RabbitMQ
from pkg.http_response.response import error_response, success_response
from starlette.responses import JSONResponse

from app.rabbit.utilities.sales.sales import SalesRabbitMQ
from pkg.rabbit.rabbit import RabbitMQConnection


router = APIRouter()

@router.get("/v1/sales", response_model=success_response)
async def getSales() -> JSONResponse:
    print("raka")
    return success_response(None)

@router.post("/v1/sales/send-queue", response_model=success_response)
async def postSendSalesQueue() -> JSONResponse:
    salesRabbitMQ: RabbitMQ = SalesRabbitMQ()
    print(f"Exchange name: {salesRabbitMQ.exchange.Name}")
    message = "hello consumer!!!!!"
    channel = RabbitMQConnection().channel()
    channel.exchange_declare(
        exchange=salesRabbitMQ.exchange.Name,
        exchange_type=salesRabbitMQ.exchange.KindOfExchange,
        durable=salesRabbitMQ.exchange.Durable,
        auto_delete=salesRabbitMQ.exchange.AutoDelete,
        internal=salesRabbitMQ.exchange.Internal,
    )
    channel.queue_bind(
        queue=salesRabbitMQ.queue.Name,
        exchange=salesRabbitMQ.exchange.Name,
        routing_key=salesRabbitMQ.exchange.BindingKey,
    )
    channel.basic_publish(
        exchange=salesRabbitMQ.exchange.Name,
        routing_key=salesRabbitMQ.exchange.BindingKey,
        body=message
    )
    # print("exchange: ", salesRabbitMQ.Exchange.Name)
    print("send queue")

    return success_response(None)