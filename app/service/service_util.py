import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from .llm.llm_integration import LLM_Integration
import json
from .aws.aws_integration import extract_data_from_pdf_aws

def is_text_based(filename):
    """
    Check if the file have any extractable text

    Args:
        filename (str) : Name of document file.

    Returns:
        bool : True if file contains extractable text
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    fetch_dir = os.path.abspath(os.path.join(base_dir,f"../datastore/{filename}"))
    print(fetch_dir)
    

    reader = PdfReader(fetch_dir)
    fields_list = reader.get_fields()
    if not fields_list:
        return False
    return True

def extract_text_from_pdf(filename):
    """
    Extract feilds from the file as key value pair.

    Args:
        filename (str) : Name of the document file

    Returns:
        dict : dictionary of key-value pair
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fetch_dir = os.path.abspath(os.path.join(base_dir,f"../datastore/{filename}"))
    print(fetch_dir)
    reader = PdfReader(fetch_dir)
    fields_list = reader.get_fields()
    if fields_list :
        return fields_list
    return None

def extract_text_from_pdf_ocr(filename):
    """
    Extract text from the document act like ocr but using llm

    Args:
        filename (str): Name of document file

    Returns: A List of JSON response fetched from document using llm

    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fetch_dir = os.path.abspath(os.path.join(base_dir,f"../datastore/{filename}"))

    images = convert_from_path(fetch_dir)

    extracted_data = []
    for image in images:
        llm = LLM_Integration("openai")
        details = llm.fetch_details_from_image(image)
        extracted_data.append(details)

    return extracted_data

def convert_to_json(json_data):
    """
    Converts a JSON response to provided schema

    Args:
        json_data (JSON) : json data that you need to parse in schema

    Returns:
        A JSON response with fixed schema
    """
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        fetch_dir = os.path.abspath(os.path.join(base_dir,"../schema/"))
        
        json_list = []
        for name in os.listdir(fetch_dir):
            if name.endswith(".json"):
                path  = os.path.join(fetch_dir, name)
                with open(path, "r") as f:
                    content = json.load(f)

                    json_list.append(content)
        
        llm = LLM_Integration("openai")
        response = llm.convert_data_to_json(json_list,json_data)
        return json.loads(response)
    except Exception as e:
        print(e)


def extract_text_from_pdf_aws(filename):
    """
    Extract text from pdf file using aws service

    Args:
        filename (str): Name of document file

    Returns:
        Data fetched from the file.
    """
    return extract_data_from_pdf_aws(filename=filename)

def convert_text_to_json(text_data):
    """
    Convert text information to JSON object

    Args:
        text_data : Text information to be parsed
    
    Return:
        Paresed JSON object
    """
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        fetch_dir = os.path.abspath(os.path.join(base_dir,"../schema/"))
        
        json_list = []
        for name in os.listdir(fetch_dir):
            if name.endswith(".json"):
                path  = os.path.join(fetch_dir, name)
                with open(path, "r") as f:
                    content = json.load(f)

                    json_list.append(content)
        
        llm = LLM_Integration("openai")
        response = llm.convert_text_data_to_json(json_list,text_data)
        return json.loads(response)
    except Exception as e:
        print(e)
