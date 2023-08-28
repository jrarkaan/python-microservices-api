from fastapi import (
    APIRouter, Depends, Query
)

from pydantic import EmailStr
from starlette import status
from starlette.responses import JSONResponse
from pkg.http_response.response import error_response, success_response
from app.rabbit.utilities.sales.sales import SalesRabbitMQ
from pkg.rabbit.rabbit import RabbitMQConnection

router = APIRouter()

@router.get("/v1/sales", response_model=success_response)
async def getSales() -> JSONResponse:
    print("raka")
    return success_response(None)

@router.post("/v1/sales/send-queue", response_model=success_response)
async def postSendSalesQueue() -> JSONResponse:
    salesRabbitMQ = SalesRabbitMQ()
    print(f"Exchange name: {salesRabbitMQ.exchange.Name}")
    # channel = RabbitMQConnection().channel()
    # channel.exchange_declare()
    # print("exchange: ", salesRabbitMQ.Exchange.Name)
    print("send queue")

    return success_response(None)