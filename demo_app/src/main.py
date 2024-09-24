from fastapi import FastAPI

app = FastAPI()


# GET /hello?name={name}
# Returns a JSON object with a message saying hello to the name passed as query parameter
#
# Http status codes returned:
#   200 OK - Success
#   422 Unprocessable Entity - Missing required query parameter 'name'
#   500 Internal Server Error - Unhandled exception
#   404 Not Found - Invalid endpoint
@app.get("/hello")
async def say_hello(name: str):
    return {"message": "Hello " + name}
