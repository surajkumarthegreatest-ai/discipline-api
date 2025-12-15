# 🛡️ Discipline API

> "Discipline beats motivation."

A simple, robust REST API built with Flask that serves "hard truths" and quotes about discipline. This project demonstrates a production-ready CI/CD pipeline using Docker and Render.

## 🚀 Live Demo
**Base URL:** `https://discipline-api.onrender.com`

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

## 💻 Local Setup (For Users)

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

## 👨‍💻 Developer Workflow (For Maintainers)

### How to Update & Deploy
If you change the code, follow these steps to push changes to GitHub and trigger a new Render deployment.

1.  **Check Status**
    ```bash
    git status
    ```

2.  **Stage Changes**
    ```bash
    git add .
    ```

3.  **Commit Changes**
    ```bash
    git commit -m "Describe your change here"
    ```

4.  **Push to GitHub**
    ```bash
    git push
    ```
    *Render will automatically detect the push and redeploy.*

### Initial Setup (Reference)
These were the commands used to initialize the repo:
```bash
git init
git branch -M main
git remote add origin [https://github.com/surajkumarthegreatest-ai/discipline-api.git](https://github.com/surajkumarthegreatest-ai/discipline-api.git)

