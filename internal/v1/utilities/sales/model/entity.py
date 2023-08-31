from pydantic import (
    BaseModel,
)

class SalesQueue(BaseModel):
    outlet_bridging_id: int
    start_date: int
    end_date: int