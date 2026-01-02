<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python" alt="Python 3.13+">
    <img src="https://img.shields.io/badge/FastAPI-0.100.0+-009688?style=for-the-badge&logo=fastapi" alt="FastAPI 0.100.0+">
    <img src="https://img.shields.io/badge/TextBlob-0.18.0+-fcba03?style=for-the-badge&logo=python" alt="TextBlob 0.18.0+">
    <img src="https://img.shields.io/badge/Locust-2.19.0+-green?style=for-the-badge&logo=locust" alt="Locust 2.19.0+">
  </a>
</p>

# devAi430 Sentiment Analysis API

This project provides a simple, high-performance API for performing sentiment analysis on text using FastAPI and the TextBlob library. It allows you to quickly determine the polarity (positive/negative/neutral) and subjectivity (objective/subjective) of any given text.

---

## 📚 Table of Contents

* [Features](#features)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [How to Use the API](#how-to-use-the-api)
    * [Running the API Server](#running-the-api-server)
    * [API Endpoints](#api-endpoints)
* [Dockerization](#dockerization)
    * [Understanding the Dockerfile](#understanding-the-dockerfile)
    * [Build the Docker Image](#build-the-docker-image)
    * [Run the Docker Container](#run-the-docker-container)
    * [Useful Docker Commands](#useful-docker-commands)
* [Load Testing with Locust](#load-testing-with-locust)
    * [Running Locust](#running-locust)

---

## ✨ Features

* **FastAPI Backend:** Built with FastAPI for robust and asynchronous API handling, ensuring high performance.
* **Sentiment Analysis:** Leverages the TextBlob library for accurate and efficient sentiment scoring.
* **Polarity & Subjectivity:** Returns both the sentiment's polarity (ranging from -1.0 for negative to +1.0 for positive) and subjectivity (ranging from 0.0 for objective to 1.0 for subjective).
* **Load Testing with Locust:** Includes a Locust script for simulating user traffic and assessing the API's performance under load.

---

## 🚀 Getting Started

Follow these steps to get your API up and running locally.

### Prerequisites

Before you begin, ensure you have Python 3.7+ installed.

```bash
python --version
````

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/MohsenRahbar/devAi430 devAi430 Sentiment Analysis API
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**

    All necessary dependencies are listed in `requirements.txt`. Install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Download TextBlob Corpora:** TextBlob requires specific data to perform its analysis.

    ```bash
    python -m textblob.download_corpora
    ```

-----

## 💡 How to Use the API

### Running the API Server

Navigate to your project directory and run the API using Uvicorn:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

  * `main:app`: Assumes your FastAPI application instance `app` is in a file named `main.py`. Adjust if your file name is different.
  * `--reload`: Automatically reloads the server on code changes (useful for development).
  * `--host 127.0.0.1 --port 8000`: Specifies the local host and port.

Once running, you can access the API documentation at `http://127.0.0.1:8000/docs` (Swagger UI) or `http://127.0.0.1:8000/redoc` (ReDoc).

### API Endpoints

1.  **Root Endpoint (Health Check):**

      * **GET `/`**
      * Returns a simple "Hello" message to confirm the API is running.
      * **Example:** `http://127.0.0.1:8000/`
      * **Response:** `{"text": "Hello"}`

2.  **Sentiment Analysis Endpoint:**

      * **GET `/sentiment/{text}`**
      * Performs sentiment analysis on the provided `text`.
      * **Parameters:**
          * `text` (path parameter): The string of text to analyze.
      * **Example:** `http://127.0.0.1:8000/sentiment/I love this product, it's amazing!`
      * **Response:**
        ```json
        {
          "orginal_text": "I love this product, it's amazing!",
          "polarity": 0.825,
          "subjectivity": 0.9
        }
        ```
      * **Example (Negative):** `http://127.0.0.1:8000/sentiment/This is the worst movie ever.`
      * **Response:**
        ```json
        {
          "orginal_text": "This is the worst movie ever.",
          "polarity": -1.0,
          "subjectivity": 1.0
        }
        ```
      * **Example (Neutral/Objective):** `http://127.0.0.1:8000/sentiment/The sky is blue.`
      * **Response:**
        ```json
        {
          "orginal_text": "The sky is blue.",
          "polarity": 0.0,
          "subjectivity": 0.0
        }
        ```

-----

## 🐳 Dockerization

Docker provides a way to package your application and all its dependencies into a single, portable container. This ensures your API runs consistently across different environments.

### Prerequisites for Dockerization

Ensure you have Docker installed and running on your system. You can check your Docker version with:

```bash
docker --version
```

### Understanding the Dockerfile

The `Dockerfile` in the root of this project defines the steps to build the Docker image for your API. It sets up the Python environment, installs dependencies from `requirements.txt`, downloads TextBlob corpora, and configures the API to run using Uvicorn.

### Build the Docker Image

Navigate to your project's root directory in your terminal and build the Docker image. This process might take some time, especially during the first build, as it downloads the base image and installs dependencies.

```bash
docker build -t sentiment-api .
```

  * `-t sentiment-api`: Tags your image with a readable name. You can choose any name you like.
  * `.`: Specifies that the `Dockerfile` is in the current directory.

### Run the Docker Container

Once the image is built, you can run a container from it. This command starts your API in the background and maps the container's port 8000 to your host machine's port 8000, making it accessible from your browser.

```bash
docker run -d -p 8000:8000 --name sentiment-app-container sentiment-api
```

  * `-d`: Runs the container in "detached" mode (in the background).
  * `-p 8000:8000`: Maps host port 8000 to container port 8000.
  * `--name sentiment-app-container`: Assigns a specific name to your container for easier management.
  * `sentiment-api`: The name of the image to run.

You can now access your API at `http://127.0.0.1:8000/` or `http://localhost:8000/` in your web browser.

### Useful Docker Commands

  * **List running containers:**
    ```bash
    docker ps
    ```
  * **List all containers (including stopped ones):**
    ```bash
    docker ps -a
    ```
  * **Stop a running container:**
    ```bash
    docker stop sentiment-app-container
    ```
  * **Remove a container (must be stopped first):**
    ```bash
    docker rm sentiment-app-container
    ```
  * **Remove an image:**
    ```bash
    docker rmi sentiment-api
    ```

-----

## 📈 Load Testing with Locust

Load testing is crucial for understanding how your API performs under expected and peak user traffic. This project includes a Locust script (`locustfile.py`) to simulate users hitting your sentiment analysis endpoint.

### Running Locust

1.  **Ensure your FastAPI server is running.** Locust will send requests to it. If you're using the Dockerized version, make sure the Docker container is running.

2.  **Open a new terminal** and navigate to your project directory.

3.  **Run Locust:**

    ```bash
    locust -f locustfile.py
    ```

4.  **Access the Locust Web UI:** Open your web browser and go to `http://localhost:8089`.

5.  **Start the Test:**

      * Enter the "Number of users to spawn" (e.g., 100).
      * Enter the "Spawn rate" (users per second, e.g., 10).
      * Enter the "Host" of your FastAPI application (e.g., `http://127.0.0.1:8000`).
      * Click "Start swarming".

Locust will then simulate users making requests to your API, and you'll see real-time statistics on response times, requests per second, and error rates in the web UI. This helps you identify performance bottlenecks and ensure your API can handle anticipated traffic.
