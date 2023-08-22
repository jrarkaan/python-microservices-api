from enum import Enum
from functools import lru_cache
from typing import Any
import yaml
from pydantic import (
    Field,
)
from pydantic_settings import BaseSettings
import os

class LogLevels(str, Enum):
    """ Enum of permitted log levels. """
    Debug = "debug"
    Info = "info"
    Warning = "warning"
    Error = "error"
    Critical = "critical"

class ServerConfig(BaseSettings):
    """ Settings for server running """
    Host: str
    Port: int = Field(ge=0, le=65535)
    Log_level: LogLevels
    Reload: bool
    Mode: str
    NameService: str

class RabbitMQ(BaseSettings):
    """ Settings for RabbitMQ Server """
    Host: str
    Port: int
    User: str
    Password: str
    Exchange: str
    Queue: str
    RoutingKey: str
    ConsumerTag: str
    WorkerPoolSize: int

class ApiConfigSettings(BaseSettings):
    """ Settings for FastAPI Server """
    Title: str = ""
    Description: str = ""
    Version: str
    Docs_url: str

class Settings(BaseSettings):
    Api_config: ApiConfigSettings
    Rabbitmq: RabbitMQ
    Server: ServerConfig
def LoadFromYAML() -> Any:
    configFileLocation = os.path.join(os.getcwd(), "config/config.yaml")
    with open(configFileLocation) as fp:
        config = yaml.safe_load(fp)
    return config
@lru_cache()
def GetSettings() -> Settings:
    yaml_config = LoadFromYAML()
    settings = Settings(**yaml_config)
    return settings