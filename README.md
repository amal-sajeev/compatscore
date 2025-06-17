# ConvoScore API

A conversation quality evaluation API that analyzes dating app conversations using AI-powered scoring across multiple dimensions.

## Overview

ConvoScore evaluates conversations between two users by analyzing their profiles and messages, providing detailed scores and feedback to help improve conversation quality and connection potential.

## Features

- **Multi-dimensional Scoring**: Evaluates conversations across 4 key metrics
- **Profile-based Analysis**: Compares conversation content against user profiles
- **Personalized Feedback**: Provides specific advice for each participant
- **Flexible Detail Levels**: Quick or detailed analysis options
- **REST API**: Easy integration with FastAPI

## Scoring Dimensions

### 1. Engagement Quality (0-10)
- Measures active participation and question-asking
- Evaluates response building and curiosity
- Predicts conversation sustainability

### 2. Authenticity (0-10)
- Assesses genuine self-expression vs scripted responses
- Analyzes personal story sharing and voice consistency
- Identifies real connection potential

### 3. Connection (0-10)
- Measures alignment between shared details and partner preferences
- Identifies compatibility indicators
- Evaluates mutual interest and empathy

### 4. Truthfulness (0-10)
- Verifies consistency between conversation claims and profile data
- Checks accuracy of stated locations, ages, incomes, professions
- Detects contradictions and exaggerations

## Installation

### Prerequisites
- Python 3.8+
- Ollama with Gemma 3 model

### Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/convoscore-api.git
cd convoscore-api
```

2. Install dependencies:
```bash
pip install fastapi uvicorn ollama pydantic
```

3. Ensure Ollama is running with Gemma 3:
```bash
ollama pull gemma3:latest
ollama serve
```

## Usage

### Starting the API
```bash
uvicorn scorerapi:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoint

**POST** `/score`

#### Request Body
```json
{
  "profiles": [
    {
      "name": "John Doe",
      "gender": "Male",
      "age": 28,
      "location": "New York",
      "profession": "Software Engineer",
      "preferences": "Looking for someone who enjoys hiking and outdoor activities"
    },
    {
      "name": "Jane Smith", 
      "gender": "Female",
      "age": 26,
      "location": "New York",
      "profession": "Designer",
      "preferences": "Interested in creative people who love art and music"
    }
  ],
  "messages": [
    {
      "sender": "John",
      "message": "Hi! I noticed you're into design. I love creative work too!",
      "timestamp": "2024-01-01T10:00:00Z"
    },
    {
      "sender": "Jane",
      "message": "That's great! What kind of creative work do you do?",
      "timestamp": "2024-01-01T10:05:00Z"
    }
  ],
  "detail": true
}
```

#### Response Format
```json
{
  "engagement_quality": 7,
  "authenticity": 6,
  "connection": 8,
  "truthfulness": 9,
  "general_trend": "positive",
  "m_comments": "You're showing good interest in her profession, but try sharing more personal details about your own creative interests to build deeper connection.",
  "f_comments": "You're engaging well with follow-up questions, continue exploring his interests while sharing your own experiences.",
  "contradictions": "No significant contradictions found between profiles and conversation content."
}
```

### Parameters

- **profiles**: User profile data (list, dict, or string format)
- **messages**: Conversation messages (list, dict, or string format)  
- **detail**: Boolean flag for analysis depth
  - `true`: Detailed analysis with contradictions report (slower)
  - `false`: Quick analysis (faster)

## File Structure

```
convoscore-api/
├── scorerapi.py          # FastAPI application
├── convoscore.py         # Core scoring logic
├── tests/                # Test data
│   ├── pos_R&P_test.json
│   ├── neg_R&P_test.json
│   └── R&P_profile.json
└── README.md
```

## Development

### Running Tests
```bash
python convoscore.py
```

This runs example conversations and displays scoring results for both positive and negative conversation examples.

### Model Configuration
The system uses Gemma 3 by default. You can modify the model in the `chat_parser` function:

```python
result = chat_parser(profiles, messages, detail=True, model="your-model:latest")
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


**Note**: This API requires Ollama to be running locally with the Gemma 3 model installed. Ensure your system has sufficient resources for AI model inference.