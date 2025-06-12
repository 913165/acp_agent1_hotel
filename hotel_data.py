# hotel_data.py
"""
Hotel data storage module
Contains sample hotel data for different locations
"""

HOTEL_DATA = {
    "new_york": [
        {
            "name": "The Plaza Hotel",
            "rating": 4.5,
            "price_per_night": 450,
            "amenities": ["WiFi", "Pool", "Spa", "Gym", "Restaurant"],
            "availability": True
        },
        {
            "name": "The Standard High Line",
            "rating": 4.2,
            "price_per_night": 320,
            "amenities": ["WiFi", "Bar", "Gym", "Pet-friendly"],
            "availability": True
        },
        {
            "name": "Pod Hotel Brooklyn",
            "rating": 4.0,
            "price_per_night": 180,
            "amenities": ["WiFi", "Restaurant", "Rooftop Bar"],
            "availability": False
        }
    ],
    "paris": [
        {
            "name": "Hotel Plaza Athenee",
            "rating": 4.8,
            "price_per_night": 680,
            "amenities": ["WiFi", "Spa", "Restaurant", "Concierge", "Bar"],
            "availability": True
        },
        {
            "name": "Le Marais Hotel",
            "rating": 4.1,
            "price_per_night": 280,
            "amenities": ["WiFi", "Restaurant", "Historic Building"],
            "availability": True
        },
        {
            "name": "Hotel des Grands Boulevards",
            "rating": 4.3,
            "price_per_night": 350,
            "amenities": ["WiFi", "Restaurant", "Bar", "Garden"],
            "availability": True
        }
    ],
    "tokyo": [
        {
            "name": "The Ritz-Carlton Tokyo",
            "rating": 4.7,
            "price_per_night": 520,
            "amenities": ["WiFi", "Spa", "Pool", "Multiple Restaurants", "City View"],
            "availability": True
        },
        {
            "name": "Shibuya Excel Hotel Tokyu",
            "rating": 4.2,
            "price_per_night": 290,
            "amenities": ["WiFi", "Restaurant", "City Center", "Shopping Access"],
            "availability": True
        },
        {
            "name": "Capsule Hotel Shinjuku 510",
            "rating": 3.8,
            "price_per_night": 80,
            "amenities": ["WiFi", "Shared Bath", "Lockers"],
            "availability": False
        }
    ],
    "london": [
        {
            "name": "The Savoy",
            "rating": 4.6,
            "price_per_night": 590,
            "amenities": ["WiFi", "Spa", "Multiple Restaurants", "Theatre District", "River View"],
            "availability": True
        },
        {
            "name": "Premier Inn London City",
            "rating": 4.0,
            "price_per_night": 120,
            "amenities": ["WiFi", "Restaurant", "24/7 Reception"],
            "availability": True
        },
        {
            "name": "The Zetter Townhouse",
            "rating": 4.4,
            "price_per_night": 380,
            "amenities": ["WiFi", "Bar", "Boutique Style", "Historic"],
            "availability": True
        }
    ],
    "dubai": [
        {
            "name": "Burj Al Arab Jumeirah",
            "rating": 4.9,
            "price_per_night": 1200,
            "amenities": ["WiFi", "Multiple Pools", "Spa", "Private Beach", "Butler Service"],
            "availability": True
        },
        {
            "name": "Atlantis The Palm",
            "rating": 4.5,
            "price_per_night": 480,
            "amenities": ["WiFi", "Water Park", "Aquarium", "Multiple Restaurants", "Beach"],
            "availability": True
        },
        {
            "name": "Rove Downtown Dubai",
            "rating": 4.1,
            "price_per_night": 150,
            "amenities": ["WiFi", "Pool", "Gym", "Restaurant", "City Center"],
            "availability": False
        }
    ]
}