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
from pkg.rabbit.rabbit import RabbitMQPackage
from app.config.config import GetSettings

router = APIRouter()
salesRabbitMQConfig: RabbitMQ = SalesRabbitMQ()

settings = GetSettings()
rabbitMQConfig = RabbitMQPackage(
    host=settings.Rabbitmq.Host,
    port=settings.Rabbitmq.Port,
    virtual_host="/",
    c_username=settings.Rabbitmq.User,
    c_password=settings.Rabbitmq.Password,
    heartbeat=0,
    blocked_connection_timeout=None,
)
rabbitMQConfig.connection()

@router.get("/v1/sales", response_model=success_response)
async def getSales() -> JSONResponse:
    print("raka")
    return success_response(None)

@router.post("/v1/sales/send-queue", response_model=success_response)
async def postSendSalesQueue() -> JSONResponse:

    sliceToQueue: list[SalesQueue] = [
        SalesQueue(outlet_bridging_id=14049, start_date=1626800400, end_date=1626800400).model_dump(),
        SalesQueue(outlet_bridging_id=6829, start_date=1626800400, end_date=1626800400).model_dump(),
        SalesQueue(outlet_bridging_id=1052, start_date=1626800400, end_date=1626800400).model_dump(),
        SalesQueue(outlet_bridging_id=19363, start_date=1626800400, end_date=1626800400).model_dump(),
        SalesQueue(outlet_bridging_id=13469, start_date=1626800400, end_date=1626800400).model_dump(),
        SalesQueue(outlet_bridging_id=1067, start_date=1626800400, end_date=1626800400).model_dump(),
        SalesQueue(outlet_bridging_id=19436, start_date=1626800400, end_date=1626800400).model_dump(),
    ]
    for value in sliceToQueue:
        print(f"sales to queue {value}")
        rabbitMQConfig.publisher_rabbit(
                salesRabbitMQConfig.exchange.Name,
                salesRabbitMQConfig.exchange.KindOfExchange,
                salesRabbitMQConfig.exchange.BindingKey,
                salesRabbitMQConfig.exchange.ConsumerTag,
                salesRabbitMQConfig.exchange.Durable,
                salesRabbitMQConfig.exchange.AutoDelete,
                salesRabbitMQConfig.exchange.Internal,
                salesRabbitMQConfig.queue.Name,
                json.dumps(value)
        )

    # print("exchange: ", salesRabbitMQ.Exchange.Name)

    # print(sliceToQueue)
    print("send queue")

    return success_response(None)