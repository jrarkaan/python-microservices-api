from pydantic import (
    BaseModel,
)

class SalesQueue(BaseModel):
    outletBridgingID: int
    startDate: int
    endDate: int