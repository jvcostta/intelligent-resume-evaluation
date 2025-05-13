from fastapi import APIRouter, File, UploadFile
from app.utils.fileHandler import save_file, delete_file
from app.services.extractor import extract_text
from app.services.analyzer import analyze_resume

router = APIRouter()

@router.post("/analisar") #a função que esta abaixo disso sera executada quando acessarem essa rota
async def analisar_curriculo(file: UploadFile = File(...)):
    path = await save_file(file) #salva temporareamente no servidor. precisam disso para serem analisados
    texto = extract_text(path)
    resultado = analyze_resume(texto)
    delete_file(path)
    return resultado

