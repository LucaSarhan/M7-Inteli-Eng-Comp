#Library Imports
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

#Instantiating FastAPI to use the server
app = FastAPI()

#Route for using files in the html page
app.mount("/css", StaticFiles(directory="css"), name="css")

#Route to the curriculum
@app.get("/")
def render_curriculum():
    return FileResponse("Curriculo.html")