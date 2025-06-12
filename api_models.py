# api_models.py
"""
Pydantic models for FastAPI request/response validation
"""

from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    """Request model for natural language queries"""
    query: str

class QueryResponse(BaseModel):
    """Response model for query results"""
    query: str
    response: str
    status: str = "success"

class SearchHotelsRequest(BaseModel):
    """Request model for hotel search"""
    location: str
    max_price: Optional[int] = None

class HotelDetailsRequest(BaseModel):
    """Request model for hotel details"""
    location: str
    hotel_name: str

class BookingCostRequest(BaseModel):
    """Request model for booking cost calculation"""
    price_per_night: int
    nights: int
    tax_rate: float = 0.12

class HealthResponse(BaseModel):
    """Response model for health check"""
    status: str
    timestamp: str

class RootResponse(BaseModel):
    """Response model for root endpoint"""
    message: str
    version: str
    endpoints: dict