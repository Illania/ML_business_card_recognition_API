import os
import uvicorn
from fastapi import FastAPI, File, UploadFile, Request, Response
from os.path import isfile
import shutil
from pathlib import Path
from PIL import Image
import jsonpickle
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from contact_recognizer import get_contact_from_card
from werkzeug.utils import secure_filename
from starlette.responses import RedirectResponse, FileResponse

UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg'}

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/test_data", StaticFiles(directory="test_data"), name="test_data")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")


@app.get("/")
async def docs_redirect():
    '''Launchs start page. Just redirects to API documentation.
    '''
    return RedirectResponse(url='/docs')


@app.post("/upload")
async def upload_file(upload_file: UploadFile = File(...)):
    '''Uploads file upload_file to the server UPLOAD_FOLDER using form data.
    '''
    try:
        if(not allowed_file(upload_file.filename)):
            return {"message": f"Not allowed file format: only .jpg, .jpeg and .png files are allowed."}
        filename = secure_filename(upload_file.filename)
        destination = Path(UPLOAD_FOLDER, filename)
        with destination.open('wb') as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    except Exception as e:
        return {"message": f"There was an error uploading the file:{str(e)}"}
    finally:
        upload_file.file.close()
    return {"message": f"Successfully uploaded {upload_file.filename}"}

def allowed_file(filename):
    '''Checks whether uploaded filename has an allowed extension.
    '''
    return Path(filename).suffix in ALLOWED_EXTENSIONS
     
               
@app.get("/view/{filename}")
def view(request: Request, filename):
    '''Gets specified file from UPLOAD_FOLDER, and if it exists,
    performs card recognition, then text recognition and returns html page containing
    parsed contact information and business card image.
    '''
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    if not isfile(file_path):
        return Response(status_code=404)
    
    contact = get_contact_from_card(file_path)
        
    context = {
        "request": request,
        "folder": UPLOAD_FOLDER,
        "filename": filename,
        "contact": contact
    }
    return templates.TemplateResponse("card.html", context)


@app.get("/test")
def view(request: Request):
    '''Launchs test on a test business card, just to show how this works.
    '''
    
    file_path = os.path.join("test_data/", "card.jpg")
    
    if not isfile(file_path):
        return Response(status_code=404)
    
    contact = get_contact_from_card(file_path)
        
    context = {
        "request": request,
        "folder": "test_data/",
        "filename": "card.jpg",
        "contact": contact
    }
    return templates.TemplateResponse("card.html", context)


@app.get("/contact/json/{filename}")
def get_contact_json(filename):
    '''Recognizes the contact from the business card image and returns contact object data in json format.
    '''
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not isfile(file_path):
        return Response(status_code=404)

    contact = get_contact_from_card(file_path)         
    return jsonpickle.encode(contact)


@app.get('/download/{filename}')
def download_file(filename):
    '''Downloads file with file name filename from UPLOAD_FOLDER if exists'''
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(file_path):
            return FileResponse(file_path, media_type='application/octet-stream',filename=filename)
    except Exception as e:
        return {"message": f"There was an error downloading the file:{str(e)}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)