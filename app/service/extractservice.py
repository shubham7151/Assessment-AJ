import os
import app.service.service_util as su
from dotenv import load_dotenv

def extract_data_from_pdf(algo:str, filename:str):
    """
    Extract data from pdfs files provided the algorithm to fetch data

    Args:
        algo (str) : The type of algorithm used for fetching data from pdfs i.e. llm || aws
        filename (str) : Name of document file
    
    Return :
        A JSON response of extracted data
    """
    load_dotenv()
    if algo == "llm":
        if su.is_text_based(filename=filename):
            return su.extract_text_from_pdf(filename=filename)
        else:
            ocr_response = su.extract_text_from_pdf_ocr(filename=filename)
            json_response = su.convert_to_json(ocr_response)
            return json_response
    elif algo == "aws":
        aws_presponse = su.extract_text_from_pdf_aws(filename=filename)
        json_response = su.convert_text_to_json(aws_presponse)
        return json_response