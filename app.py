from fastapi import FastAPI
from services.ingestion_service import ingest_document
from services.query_service import ask_question
#from services.drive_service import sync_drive


app = FastAPI()


from fastapi import FastAPI, UploadFile, File
import os
import shutil




@app.get("/")
def home():
    return {
        "message": "Enterprise RAG API Running"
    }

@app.post("/ingest")
def ingest(data: dict):

    return ingest_document(
        data["file_path"]
    )

@app.post("/upload-ingest")
async def upload_ingest(file: UploadFile = File(...)):

    os.makedirs("documents", exist_ok=True)

    file_path = os.path.join("documents", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = ingest_document(file_path)

    return result


@app.post("/query")
def query(data: dict):

    return ask_question(
        data["question"]
    )

'''
@app.post("/sync-drive")
def sync():

    return sync_drive()
'''
