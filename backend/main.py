
from fastapi import FastAPI, File, UploadFile
from backend.ingest import process_file
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# ✅ Allow requests from React (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    result = process_file(file.filename, content)
    return {"chunks": result}
