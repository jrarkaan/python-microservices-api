from pydantic import (
    BaseModel,
)

class SalesQueue(BaseModel):
    OutletBridgingID: int
    StartDate: int
    EndDate: int