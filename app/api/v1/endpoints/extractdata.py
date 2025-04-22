from fastapi import APIRouter, UploadFile, HTTPException
import logging 
import os
from app.service import extractservice ,evalservice
import time

import json

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/upload/")
def upload(file : UploadFile):
    try:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only .pdf files accepted")
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        save_dir = os.path.abspath(os.path.join(base_dir, "../../../datastore/"))

        with open(save_dir+f"/{file.filename}", 'wb') as f:
            content = file.file.read()
            f.write(content)
        
        return {
            "data" : "upload successful"
        }
    except Exception as e:
        logger.error(e)


@router.post("/extract/")
def extract(algo:str , filename:str, write_to_file:bool = False):
    start = time.time()
    if not algo:
        raise HTTPException(status_code=400, detail="fetching algorithm not defined")
    
    if not filename:
        raise HTTPException(status_code=400, detail="file name not defined")
    
    if not filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="file should be of pdf format")
    
    response = extractservice.extract_data_from_pdf(algo,filename)
    if write_to_file:
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            write_dir = os.path.abspath(os.path.join(base_dir,"../../../responses/actual_data_response.json"))
            with open(write_dir,"w") as f:
                f.write(str(response).replace("'","\"").lower())
        except Exception as e:
            print(e)
    end = time.time()
    

    return {
        "data" : response
    }

@router.get("/eval/")
def evaluation(data_type:str):
    return evalservice.evaluationService(data_type)