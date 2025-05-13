import os
from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

async def save_file(file: UploadFile) -> str:
    path = UPLOAD_DIR / file.filename
    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)
    return str(path)

def delete_file(path: str):
    os.remove(path)
