from io import BytesIO
import base64
import ollama
from openai import OpenAI
import requests
import os
import time

class LLM_Integration():

    """
    This class creates a object to integrate llm to the system.

    Args:
        model_name : Name of model you need to integrate.
    """

    def __init__(self, model_name):
        self.model_name = model_name

    def fetch_details_from_image(self, path_to_image):

        if self.model_name == "Olama":
            encode_image = self.encode_image(path_to_image)
            res = ollama.chat(
                model= "llava:7b",
                message=[
                        {
                            "role":"system",
                            "content" : "Act like a image processing system."
                        },
                        {
                            'role': 'user',
                        'content': 'Extract all the user written information from the form ',
                        'images': [encode_image]
                        }
                ]
            )
            return res["message"]["content"]
        elif self.model_name == "openai":
            start = time.time()
            encode_image = self.encode_image(path_to_image)
            client = OpenAI()
            
            
            response = client.responses.create(
                model="gpt-4.1",
                input=[{
                            "role":"system",
                            "content" : "Act like a image processing system."
                        },
                        {
                            "role": "user",
                            "content": [
                                {"type": "input_text", "text": """
                                    Instructions :
                                    1. Process the image of scanned form carefully.
                                    2. Fetch all the information from the form.
                                    3. Return the extracted information in JSON format
                                    5. Extract the details exactly as it appears in the document, preserving the text case.
                                """},
                                {
                                    "type": "input_image",
                                    "image_url": f"data:image/jpeg;base64,{encode_image}",
                                },
                            ],
                        }],
                    )
            end = time.time()
            
            return response.output_text
        elif self.model_name == "openrouter":

            API_URL = 'https://openrouter.ai/api/v1/chat/completions'

            headers = {
                'Authorization': f'Bearer {os.getenv("OPEN_ROUTER_API_KEY")}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "google/gemini-2.0-flash-exp:free",
                "messages": [{"role": "user", "content": "Extract all information from the form and return information in JSON format"},
                                {
                            "type": "input_image",
                            "image_url": path_to_image,
                                }
                            ]
            }

            response = requests.post(API_URL, json=data, headers=headers)
            return response
    
    
    def encode_image(self,image_path):
                buffered = BytesIO()
                image_path.save(buffered, format="PNG")
                return base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    def convert_data_to_json(self,json_schema, json_data):
        client = OpenAI()
        response = client.responses.create(
                model="gpt-4.1",
                input=[{
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": f"""
                            
                            Instructions :
                            1. Provided json data and json schema as list 
                            2. Return a python dictionary response
                            3. The key in dictionary should be the schema title and schema is filled with appropriate data from json object.
                            5. If any data is missing and its type in schema is boolean return false as value
                            6. For privacy related information contextually check the json data and fill appropriate data in defined section
                            7. For date specific field use YYYY-MM-DD format.
                            8. Extract the details exactly as it appears in the json_data, preserving the case.
                                Json Schema :
                                {json_schema}

                                Json Data:
                                {json_data}

                            Ensure:
                            1. Strick to the given instruction.
                            2. Need just dictionary response so it can directly converted to JSON object without processing.
                            3. If any field is empty and associated data is not present return the empty schema.
                            4. Dont add any comments, text, statement, instructions before or after the list.
                            5. Make sure the dictionary is JSON parseable.
                            """},
                    ],
                }],
            )
        
        return response.output_text
    def convert_text_data_to_json(self, json_schema, data):
        
        client = OpenAI()
        response = client.responses.create(
                model="gpt-4.1",
                input=[{
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": f"""
                            Instructions :
                            1. Provided text data and json schemas as list.
                            2. Return a python dictionary response taking account into json schema.
                            3. Read the text data carefully.
                            4. Fill the return response with appropriate information from the text read in step 3.
                            5. Extract the details exactly as it appears in the json_data, preserving the case.
                                Json Schema :
                                {json_schema}

                                Text Data:
                                {data}

                            Ensure:
                            1. Strick to the given instruction.
                            2. Need just dictionary response so it can directly converted to JSON object without processing.
                            3. If any field is empty and associated data is not present return the empty schema.
                            4. Dont add any comments, text, statement, instructions before or after the list.
                            5. Make sure the dictionary is JSON parseable.
                            6. Most important follow instruction carefully.
                            """},
                    ],
                }],
            )
        
        return response.output_text