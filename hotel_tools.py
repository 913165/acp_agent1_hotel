# hotel_tools.py
"""
LangChain tools for hotel booking operations
"""

from langchain_core.tools import tool
from typing import List, Dict, Any
from hotel_data import HOTEL_DATA


@tool
def search_hotels(location: str, max_price: int = None) -> dict[str, str] | dict[str, str | int | list[Any]]:
    """
    Search for available hotels in a specific location.

    Args:
        location: The city/location to search for hotels (e.g., 'new_york', 'paris', 'tokyo', 'london', 'dubai')
        max_price: Optional maximum price per night filter

    Returns:
        List of available hotels with details
    """
    location_key = location.lower().replace(" ", "_")

    if location_key not in HOTEL_DATA:
        return {
            "error": f"No hotels found for location: {location}. Available locations: {', '.join(HOTEL_DATA.keys())}"
        }

    hotels = HOTEL_DATA[location_key]
    available_hotels = [hotel for hotel in hotels if hotel["availability"]]

    if max_price is not None:
        available_hotels = [hotel for hotel in available_hotels if hotel["price_per_night"] <= max_price]

    return {
        "location": location,
        "total_available": len(available_hotels),
        "hotels": available_hotels
    }


@tool
def get_hotel_details(location: str, hotel_name: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific hotel.

    Args:
        location: The city/location of the hotel
        hotel_name: The name of the hotel

    Returns:
        Detailed hotel information
    """
    location_key = location.lower().replace(" ", "_")

    if location_key not in HOTEL_DATA:
        return {"error": f"Location '{location}' not found"}

    hotels = HOTEL_DATA[location_key]
    for hotel in hotels:
        if hotel["name"].lower() == hotel_name.lower():
            return {
                "location": location,
                "hotel_details": hotel,
                "estimated_weekly_cost": hotel["price_per_night"] * 7,
                "estimated_monthly_cost": hotel["price_per_night"] * 30
            }

    return {"error": f"Hotel '{hotel_name}' not found in {location}"}


@tool
def calculate_booking_cost(price_per_night: int, nights: int, tax_rate: float = 0.12) -> Dict[str, float]:
    """
    Calculate the total cost of a hotel booking including taxes.

    Args:
        price_per_night: Price per night in USD
        nights: Number of nights
        tax_rate: Tax rate (default 12%)

    Returns:
        Breakdown of booking costs
    """
    subtotal = price_per_night * nights
    tax = subtotal * tax_rate
    total = subtotal + tax

    return {
        "price_per_night": price_per_night,
        "nights": nights,
        "subtotal": subtotal,
        "tax": round(tax, 2),
        "total_cost": round(total, 2)
    }


@tool
def get_available_locations() -> dict[str, list[Any] | int]:
    """
    Get all available booking locations.

    Returns:
        List of available cities/locations
    """
    return {
        "available_locations": list(HOTEL_DATA.keys()),
        "total_locations": len(HOTEL_DATA)
    }


# Export tools list
TOOLS = [search_hotels, get_hotel_details, calculate_booking_cost, get_available_locations]