from fastapi import APIRouter

from internal.v1.routes import sales

apiRouter = APIRouter()
apiRouter.include_router(sales.router, tags=["sales"])