# 📝 Grammar Corrector API

A lightweight REST API that automatically detects and corrects grammatical errors in English text — powered by **FastAPI** and **Llama 3** via **Ollama**.

---

## 🚀 Features

- ✅ Corrects grammar, spelling, punctuation, and capitalization
- ✅ Fixes subject-verb agreement errors
- ✅ Preserves the original meaning, facts, and intent
- ✅ Returns only the corrected text — no explanations or extra output
- ✅ Input validation (length limits, alphabet checks)
- ✅ Runs locally **and** inside Docker with no configuration changes
- ✅ Interactive API docs via Swagger UI (`/docs`)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| API Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| LLM Runtime | [Ollama](https://ollama.com/) |
| LLM Model | Llama 3 (`llama3`) |
| Validation | Pydantic v2 |
| Server | Uvicorn |
| Containerization | Docker |

---

## 📁 Project Structure

```
grammar-corrector/
├── head.py           # Main FastAPI application
├── schema.py         # Pydantic request validation model
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker image definition
├── .env              # Environment variables (Ollama URL)
└── README.md         # Project documentation
```

---

## ⚙️ Prerequisites

Before running this project, make sure you have:

- **Python 3.11+** installed
- **[Ollama](https://ollama.com/download)** installed and running
- **Llama 3** model pulled in Ollama:
  ```bash
  ollama pull llama3
  ```
- **Docker** (optional, for containerized deployment)

---

## 🏃 Running Locally (Terminal)

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/grammar-corrector.git
cd grammar-corrector
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Make sure Ollama is running:**
```bash
ollama serve
```

**4. Start the API server:**
```bash
uvicorn head:app --reload
```

The API will be available at: `http://localhost:8000`

---

## 🐳 Running with Docker

**1. Build the Docker image:**
```bash
docker build -t grammar-corrector .
```

**2. Run the container:**
```bash
docker run -p 8002:8002 grammar-corrector
```

The API will be available at: `http://localhost:8002`

> **Note:** Ollama must still be running on your host machine. The app automatically detects when it's running inside Docker and routes requests to your host machine correctly — no configuration changes needed.

---

## 📡 API Endpoints

### `GET /`
Returns a welcome message and API overview.

**Response:**
```json
{
  "message": "Welcome to the Grammar Corrector API!",
  "description": "This API uses the Llama 3 Large Language Model (LLM) through Ollama to automatically detect and correct grammatical errors in English text while preserving the original meaning.",
  "features": [
    "Corrects grammatical mistakes",
    "Fixes spelling errors",
    "Corrects punctuation",
    "Corrects capitalization",
    "Preserves the original meaning",
    "Does not add explanations",
    "Returns only the corrected text",
    "Powered by FastAPI and Ollama"
  ],
  "endpoints": {
    "POST /correct": "Submit English text and receive the grammatically corrected version."
  },
  "version": "1.0.0"
}
```

---

### `POST /correct`
Submits text for grammar correction.

**Request Body:**
```json
{
  "text": "she don't like coffee"
}
```

**Response:**
```
She doesn't like coffee.
```

**Validation Rules:**

| Rule | Detail |
|---|---|
| Minimum length | 3 characters |
| Maximum length | 1000 characters |
| Content | Must contain at least one alphabetic character |

**Error Responses (422 Unprocessable Entity):**

| Condition | Error Message |
|---|---|
| Text shorter than 3 characters | `Please enter a large sentence .so that i can correct it grmmatically.` |
| Text longer than 1000 characters | `Please enter the text in small amount.Maximum allowed length of text is 1000.` |
| No alphabetic characters | `Please enter a sentence with enough content for grammar correction.` |

---

## 💡 Example Usage

### Using `curl`
```bash
curl -X POST "http://localhost:8000/correct" \
     -H "Content-Type: application/json" \
     -d '{"text": "i has a car and she dont like it"}'
```

**Output:**
```
I have a car and she doesn't like it.
```

### Using Python `requests`
```python
import requests

response = requests.post(
    "http://localhost:8000/correct",
    json={"text": "they was playing football yesterday"}
)
print(response.json())
# Output: They were playing football yesterday.
```

### Using Swagger UI
Visit `http://localhost:8000/docs` in your browser for an interactive API interface.

---

## 🔧 Environment Variables

The app reads configuration from the `.env` file:

| Variable | Default | Description |
|---|---|---|
| `ollama_url` | `http://localhost:11434/api/generate` | Ollama API endpoint |

> The app **automatically** switches from `localhost` to `host.docker.internal` when running inside a Docker container, so you don't need separate `.env` files for local vs Docker environments.

---

## 📦 Dependencies

```
uvicorn
fastapi
pydantic
requests
python-dotenv
```
