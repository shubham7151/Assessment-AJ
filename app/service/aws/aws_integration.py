import os
import boto3
from pdf2image import convert_from_path
import io


def extract_data_from_pdf_aws(filename):

    """
    Extract data from pdf using aws textract (managed OCR service)

    Args:
        filename (str): Name of document file

    Returns:
        Extracted information from file.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fetch_dir = os.path.abspath(os.path.join(base_dir, f"../../datastore/{filename}"))

    textract = boto3.client(service_name='textract', aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
                                aws_secret_access_key=os.environ["AWS_SECRET_KEY"], region_name='us-east-1')
    images = convert_from_path(fetch_dir)
    print("just before aws cline")
    extracted_data = []
    for image in images:
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            image_bytes = img_byte_arr.getvalue()
            response = textract.analyze_document(Document={'Bytes': image_bytes},FeatureTypes=["FORMS"])
            text = ''
            
            for item in response['Blocks']:
                if item['BlockType'] == 'LINE':
                    text += item['Text'] + '\n'

            extracted_data.append(text)

    
    return ' '.join(extracted_data)