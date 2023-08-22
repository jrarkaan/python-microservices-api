import logging
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from app.config.config import GetSettings
from pkg.http_response.response import error_response

from internal.v1.routes import apiRouter

settings = GetSettings()

app = FastAPI(
    title=settings.Api_config.Title,
    description=settings.Api_config.Description,
    version=settings.Api_config.Version,
    docs_url=settings.Api_config.Docs_url,
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event() -> None:
    # setup logger
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    app.state.logger = logger


@app.on_event("shutdown")
async def shutdown_event() -> None:
    db_connection = app.state.db_connection
    db_connection.close()

# exception handling
@app.exception_handler(RequestValidationError)
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger = request.app.state.logger
    logger.error(f"{exc}")
    return error_response(errors=str(exc), status_code=status.HTTP_400_BAD_REQUEST)

app.include_router(apiRouter)

if __name__ == "__main__":
    settings = GetSettings()
    server = settings.Server
    uvicorn.run(
        app="main:app",
        host=server.Host,
        port=server.Port,
        log_level=server.Log_level,
        reload=server.Reload,
    )