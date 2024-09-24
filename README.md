# web-app-python-starter-kit

Template Project Repo for Web Based Python Application with Poetry, Docker, FastAPI and Pydantic.

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

