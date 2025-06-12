# api_endpoints.py
"""
FastAPI endpoints for hotel booking API
"""

from fastapi import FastAPI, HTTPException
from datetime import datetime
from api_models import (
    QueryRequest, QueryResponse, SearchHotelsRequest,
    HotelDetailsRequest, BookingCostRequest, HealthResponse, RootResponse
)
from llm_service import process_hotel_query
from hotel_tools import search_hotels, get_hotel_details, calculate_booking_cost, get_available_locations

# Initialize FastAPI app
app = FastAPI(
    title="Hotel Booking API",
    description="AI-powered hotel booking system with LangChain tools",
    version="1.0.0"
)


@app.get("/", response_model=RootResponse)
async def root():
    """Root endpoint with API information"""
    return RootResponse(
        message="Hotel Booking API",
        version="1.0.0",
        endpoints={
            "POST /query": "Process natural language hotel queries",
            "POST /search-hotels": "Search hotels by location and price",
            "POST /hotel-details": "Get specific hotel details",
            "POST /calculate-cost": "Calculate booking costs",
            "GET /locations": "Get available locations",
            "GET /health": "Health check endpoint"
        }
    )


@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Process a natural language hotel query using AI

    Example queries:
    - "What hotels are available in Tokyo under $300 per night?"
    - "Show me details for The Savoy hotel in London"
    - "Calculate cost for 5 nights at $200 per night"
    """
    try:
        response = process_hotel_query(request.query)
        return QueryResponse(
            query=request.query,
            response=response,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@app.post("/search-hotels")
async def search_hotels_endpoint(request: SearchHotelsRequest):
    """
    Search for available hotels in a specific location
    """
    try:
        result = search_hotels.invoke({
            "location": request.location,
            "max_price": request.max_price
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching hotels: {str(e)}")


@app.post("/hotel-details")
async def get_hotel_details_endpoint(request: HotelDetailsRequest):
    """
    Get detailed information about a specific hotel
    """
    try:
        result = get_hotel_details.invoke({
            "location": request.location,
            "hotel_name": request.hotel_name
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting hotel details: {str(e)}")


@app.post("/calculate-cost")
async def calculate_cost_endpoint(request: BookingCostRequest):
    """
    Calculate the total cost of a hotel booking including taxes
    """
    try:
        result = calculate_booking_cost.invoke({
            "price_per_night": request.price_per_night,
            "nights": request.nights,
            "tax_rate": request.tax_rate
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating cost: {str(e)}")


@app.get("/locations")
async def get_locations_endpoint():
    """
    Get all available booking locations
    """
    try:
        result = get_available_locations.invoke({})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting locations: {str(e)}")


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat()
    )