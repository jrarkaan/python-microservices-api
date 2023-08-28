from fastapi import (
    APIRouter, Depends, Query
)
import json
# Model/ DTO
from pkg.rabbit.model.entity import RabbitMQ
from pkg.http_response.response import error_response, success_response
from starlette.responses import JSONResponse
from internal.v1.utilities.sales.model.entity import SalesQueue

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

    sliceToQueue: list[SalesQueue] = [
        SalesQueue(outletBridgingID=14049, startDate=1626800400, endDate=1626800400).model_dump(),
        SalesQueue(outletBridgingID=6829, startDate=1626800400, endDate=1626800400).model_dump(),
        SalesQueue(outletBridgingID=1052, startDate=1626800400, endDate=1626800400).model_dump(),
        SalesQueue(outletBridgingID=19363, startDate=1626800400, endDate=1626800400).model_dump(),
        SalesQueue(outletBridgingID=13469, startDate=1626800400, endDate=1626800400).model_dump(),
        SalesQueue(outletBridgingID=1067, startDate=1626800400, endDate=1626800400).model_dump(),
        SalesQueue(outletBridgingID=19436, startDate=1626800400, endDate=1626800400).model_dump(),
    ]
    for value in sliceToQueue:
        print(f"sales to queue {value}")
        channel.basic_publish(
            exchange=salesRabbitMQ.exchange.Name,
            routing_key=salesRabbitMQ.exchange.BindingKey,
            body=json.dumps(value)
        )

    # print("exchange: ", salesRabbitMQ.Exchange.Name)

    # print(sliceToQueue)
    print("send queue")

    return success_response(None)