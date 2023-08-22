from fastapi import (
    APIRouter, Depends, Query
)
from pydantic import EmailStr
from starlette import status
from starlette.responses import JSONResponse
from pkg.http_response.response import error_response, success_response

router = APIRouter()

@router.get("/v1/sales", response_model=success_response)
async def getSales() -> JSONResponse:
    print("raka")
    return success_response(None)