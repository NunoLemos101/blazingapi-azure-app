# Define your view functions here

from blazingapi.app import app
from blazingapi.response import Response


@app.get("/index")
def index(request):
    return Response(body={"message": "Hello, world!"})
