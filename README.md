# **🤖 Chatbot API with FastAPI, PostgreSQL, and OpenAI**

> A chatbot API that integrates with OpenAI's GPT-4o-mini, stores user chat history, and provides authentication using JWT tokens. Uses **FastAPI, PostgreSQL, and Tortoise-ORM**.

![python](https://img.shields.io/badge/python-3.11-BLUE)  
🚀 This project is designed to **handle user authentication, chat requests, and store conversation history** efficiently.

---

## **📌 Table of Contents**
- [📦 Requirements](#-requirements)
- [🚀 Installation](#-installation)
- [⚙️ Setup](#-setup)
- [🐳 Running with Docker](#-running-with-docker)
- [🔄 Database Migrations](#-database-migrations)
- [🔧 Running the Chatbot](#-running-the-chatbot)

---

## **Requirements**
- **Ubuntu/Linux**
- **Python 3.11**
- **PostgreSQL**
- **Pydantic**
- **Tortoise**
- **Docker & Docker Compose**
- **Virtualenv**
- **OpenAI API Key** (required for chat responses)

---

## Installation
### Install Python 3.11 and Virtualenv
```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev virtualenv

#### Virtualenv
```shell script
$ sudo apt install virtualenv
```
## Clone
```
git clone https://github.com/yourusername/chatbot.git
cd chatbot
```

## Setup
Install virtualenv in project folder.
```shell script
virtualenv -p $(which python3.11) venv
source venv/bin/activate
```
**Don't change the name "venv", the path to the virtual environment is used when creating services.** 

**If you want to change the name, make the appropriate changes to the file `[project_folder]/services/install.sh`**

Activate virtualenv
```shell script
[project_folder]$ source venv/bin/activate
```
Install python packages from requirements.txt
```shell script
(venv)[project_folder]$ pip install -r requirements.txt
```
Create the .env in the following folder `[project_folder]/config/`
and enter the appropriate data for each service, example data in file .env_example:
```.env_example
# [project_folder]/config/.env_example

DATABASE_URL=database_url
SECRET_KEY=some_strong_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10 - time in minutes
OPENAI_API_KEY=your_openai_api_key

```

## Running with Docker
If you prefer running the project inside a Docker container, follow these steps:
### 1.Install Docker and Docker Compose
```commandline
sudo apt install -y docker.io docker-compose
```

### 2. Start the database and application using Docker Compose
```commandline
docker-compose up --build -d
```

### 3. Check running containers
```commandline
docker ps
```

Now the application should be running at http://localhost:8000.

## Database Migrations
Before running the chatbot, you need to initialize the database.
### Apply database migrations
```commandline
aerich init -t app.core.config.TORTOISE_ORM
aerich init-db
aerich migrate
aerich upgrade
```
Now the database is ready to store user data and chat history.

## Running the Chatbot
Once the environment is set up, you can start the chatbot.
### Run manually
```commandline
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API documentation will be available at:
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc
