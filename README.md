# web-app-python-starter-kit

Template Project Repo for a strongly opinionated web based Python Application with Python Poetry, Docker, FastAPI, Uvicorn and Pydantic.

## What is Python Poetry ?
Python Poetry is a dependency management tool for Python projects. It provides several key features that help streamline the management of project dependencies such as dependency resolution and management, reproducibility, environment management, environment isolation including the provisioning of virtual environments for managing project dependencies.

## What is Uvicorn Server ?
Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation, primarily used for running Python web applications and frameworks like FastAPI and Starlette. It enables high-performance asynchronous handling of requests and responses, making it ideal for building efficient and scalable web services. 

## What is FastAPI ?
FastAPI is a modern, high-performance Python web framework for building APIs that leverages type hints and asynchronous capabilities to deliver fast development, automatic documentation generation, and efficient performance. It is known for its ease of use, speed, and built-in support for best practices.

## What is Docker ? 
Docker is a platform that simplifies the process of creating, deploying, and running applications using containers. Containers package an application and its dependencies into a standardized unit that can run consistently across different environments, promoting portability and efficiency.

## What is Multistage Docker ? 
Multistage Docker builds are a feature that allows you to use multiple FROM statements within a single Dockerfile, effectively creating different build stages. Each stage can use a different base image and serve a specific purpose like building the application, running tests, or preparing the final runtime environment.

## What is Pydantic ?
Pydantic is a Python library that uses type hints to define data schemas, enabling data validation, serialization, and documentation generation, leading to more robust and maintainable code. It's a popular choice in FastAPI projects for input/output validation and data handling.

---
# Steps

### Install Poetry
```
curl -sSL https://install.python-poetry.org | python3
```

### Set PATH
```
export PATH="/Users/sushantjoshi/.local/bin:$PATH"
```

### Check Poetry version
```
poetry --version
```

### Create poetry env
```
poetry new demo_app --name src
```

### Add dependencies
```
poetry add Uvicorn FastAPI
```

### Add Dev Dependencies
```
poetry add pytest httpx isort black --group dev
```

### Get into Poetry Shell
```
poetry shell
```

### Run server
```
cd src
uvicorn main:app --reload
```

### Run unit tests
```
poetry run pytest
```

### Reformat code
```
poetry run black .
```

### orgranize imports code
```
poetry run isort .
```

### Docker Commands
```
docker build -t demo .
docker build --no-cache -t demo --target test .
docker images demo
docker run -p 8000:8000 demo
```
http://localhost:8000/docs 
![Swagger](https://github.com/user-attachments/assets/4f9f823f-75e1-4ec1-92a2-6650fd3b0905)


