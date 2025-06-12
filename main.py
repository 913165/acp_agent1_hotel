# main.py
"""
Main application entry point
Handles both CLI testing and FastAPI server startup
"""

import sys
import uvicorn
from llm_service import process_hotel_query
from api_endpoints import app


def test_functionality():
    """Test the hotel booking functionality with sample queries"""
    try:
        print("Hotel Booking LLM System")
        print("=" * 50)

        # Test queries
        test_queries = [
            "What hotels are available in Tokyo under $300 per night?",
            "Show me details for The Savoy hotel in London and calculate the cost for 5 nights",
            "What are all the available booking locations?",
            "Find me a luxury hotel in Dubai with spa facilities"
        ]

        print("Testing process_hotel_query function:")
        print("=" * 50)

        for i, query in enumerate(test_queries, 1):
            print(f"\nQuery {i}: {query}")
            print("-" * 40)

            # Use the query processing function
            response = process_hotel_query(query)
            print(response)
            print("=" * 50)

        # Example of programmatic usage
        print("\nProgrammatic Usage Example:")
        print("-" * 30)
        user_query = "What's the cheapest hotel in Paris?"
        result = process_hotel_query(user_query)
        print(f"Query: {user_query}")
        print(f"Response: {result}")

    except Exception as e:
        print(f"Error: {e}")
        print("\nTo run this program, make sure to:")
        print("1. Set your OPENAI_API_KEY environment variable")
        print("2. Install required packages: pip install langchain langchain-openai fastapi uvicorn")


def start_api_server():
    """Start the FastAPI server"""
    print("Starting Hotel Booking API Server...")
    print("=" * 60)
    print("API Documentation will be available at:")
    print("📋 Swagger UI: http://localhost:8000/docs")
    print("📋 ReDoc: http://localhost:8000/redoc")
    print("🏠 Root: http://localhost:8000/")
    print("💚 Health Check: http://localhost:8000/health")
    print("=" * 60)
    print("Available endpoints:")
    print("POST /query - Natural language hotel queries")
    print("POST /search-hotels - Search hotels by location")
    print("POST /hotel-details - Get specific hotel details")
    print("POST /calculate-cost - Calculate booking costs")
    print("GET /locations - Get available locations")
    print("=" * 60)

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


def main():
    """Main function to handle command line arguments"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "api":
            # Start FastAPI server
            start_api_server()
        elif sys.argv[1] == "test":
            # Run functionality tests
            test_functionality()
        else:
            print("Usage:")
            print("  python main.py api    - Start FastAPI server")
            print("  python main.py test   - Run functionality tests")
            print("  python main.py        - Show this help message")
    else:
        print("Hotel Booking System")
        print("=" * 30)
        print("Usage:")
        print("  python main.py api    - Start FastAPI server")
        print("  python main.py test   - Run functionality tests")
        print("\nFor API usage, start the server and visit:")
        print("  http://localhost:8000/docs")


if __name__ == "__main__":
    main()