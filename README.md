# 🛡️ Discipline API

> "Discipline beats motivation."

A simple, robust REST API built with Flask that serves "hard truths" and quotes about discipline. This project demonstrates a production-ready CI/CD pipeline using Docker and Render.

## 🚀 Live Demo
**Base URL:** `https://discipline-api.onrender.com`  
*(Replace with your actual Render URL)*

## 🛠️ Tech Stack
* **Framework:** Flask (Python)
* **Server:** Gunicorn (WSGI)
* **Containerization:** Docker
* **Deployment:** Render Cloud

## 🔌 API Endpoints

### 1. Health Check
Checks if the API is running.
* **URL:** `/`
* **Method:** `GET`
* **Response:** `200 OK`
    ```text
    Hello! The Discipline API is running.
    ```

### 2. Get Truth
Returns a random discipline quote in JSON format.
* **URL:** `/truth`
* **Method:** `GET`
* **Response:** `200 OK`
    ```json
    {
      "id": 4,
      "text": "Nothing is permanent in this world, every thing is temporary.",
      "author": "Unknown"
    }
    ```

## 💻 Local Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/surajkumarthegreatest-ai/discipline-api.git](https://github.com/surajkumarthegreatest-ai/discipline-api.git)
    cd discipline-api
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Locally**
    ```bash
    python app.py
    ```
    Access at: `http://127.0.0.1:5000`

## 🐳 Docker Support

Build and run the container locally to simulate production.

```bash
# Build the image
docker build -t discipline-api .

# Run the container (Maps port 5000 to 5000)
docker run -p 5000:5000 discipline-api

