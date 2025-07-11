
# Hotel Booking API System

An AI-powered hotel booking system built with FastAPI and LangChain that provides natural language query processing and RESTful API endpoints.

## 🏗️ Project Structure

```
hotel-booking-system/
├── main.py              # Main application entry point
├── hotel_data.py        # Hotel data storage
├── hotel_tools.py       # LangChain tools for hotel operations
├── llm_service.py       # LLM service layer
├── api_models.py        # Pydantic models for API validation
├── api_endpoints.py     # FastAPI endpoints
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## 🚀 Features

- **Natural Language Processing**: Ask questions in plain English about hotels
- **RESTful API**: Clean, documented API endpoints
- **Hotel Search**: Find hotels by location and price range
- **Cost Calculation**: Calculate booking costs with taxes
- **Multiple Locations**: Support for 5 major cities (NYC, Paris, Tokyo, London, Dubai)
- **Interactive Documentation**: Auto-generated API docs with Swagger UI

## 📋 Requirements

- Python 3.8+
- OpenAI API Key
- Required packages (see requirements.txt)

## 🛠️ Installation

1. **Clone or create the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```
   
   Or create a `.env` file:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## 🎯 Usage

### Start the API Server
```bash
python main.py api
```

The server will start on `http://localhost:8000`

### Test Functionality
```bash
python main.py test
```

### Access API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🌐 API Endpoints

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API information and available endpoints |
| `POST` | `/query` | Process natural language hotel queries |
| `POST` | `/search-hotels` | Search hotels by location and price |
| `POST` | `/hotel-details` | Get specific hotel details |
| `POST` | `/calculate-cost` | Calculate booking costs with taxes |
| `GET` | `/locations` | Get all available locations |
| `GET` | `/health` | Health check endpoint |

### Example API Calls

#### Natural Language Query
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "What hotels are available in Tokyo under $300 per night?"}'
```

#### Search Hotels
```bash
curl -X POST "http://localhost:8000/search-hotels" \
  -H "Content-Type: application/json" \
  -d '{"location": "tokyo", "max_price": 300}'
```

#### Get Hotel Details
```bash
curl -X POST "http://localhost:8000/hotel-details" \
  -H "Content-Type: application/json" \
  -d '{"location": "london", "hotel_name": "The Savoy"}'
```

#### Calculate Booking Cost
```bash
curl -X POST "http://localhost:8000/calculate-cost" \
  -H "Content-Type: application/json" \
  -d '{"price_per_night": 450, "nights": 5, "tax_rate": 0.12}'
```

## 🏨 Available Locations

The system includes sample data for:
- **New York** (new_york)
- **Paris** (paris)
- **Tokyo** (tokyo)
- **London** (london)
- **Dubai** (dubai)

## 🧠 AI-Powered Features

The system uses OpenAI's GPT-4 to understand natural language queries and automatically:
- Choose appropriate tools based on the query
- Extract relevant parameters
- Provide conversational responses
- Handle complex multi-step requests

### Example Natural Language Queries
- "What hotels are available in Tokyo under $300 per night?"
- "Show me details for The Savoy hotel in London and calculate the cost for 5 nights"
- "Find me a luxury hotel in Dubai with spa facilities"
- "What's the cheapest hotel in Paris?"

## 🔧 Development

### Project Structure Details

- **`hotel_data.py`**: Contains all hotel information and availability
- **`hotel_tools.py`**: LangChain tools that define available operations
- **`llm_service.py`**: Handles LLM initialization and query processing
- **`api_models.py`**: Pydantic models for request/response validation
- **`api_endpoints.py`**: FastAPI route definitions
- **`main.py`**: Application entry point with CLI interface

### Adding New Features

1. **Add new hotel data**: Modify `hotel_data.py`
2. **Create new tools**: Add functions to `hotel_tools.py`
3. **Add API endpoints**: Extend `api_endpoints.py`
4. **Update models**: Add validation models to `api_models.py`

## 🚦 Error Handling

The system includes comprehensive error handling:
- Invalid location names
- Missing hotel information
- API key configuration issues
- Tool execution errors
- HTTP status codes for API responses

## 📝 License

This project is provided as-is for educational and development purposes.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the system.

---

**Note**: Make sure to set up your OpenAI API key before running the system. The API key is required for the natural language processing features.#
