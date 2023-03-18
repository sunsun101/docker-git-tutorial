"""
Author: Sunsun Kasajoo
Date: March 18, 2023

This module contains apis.
"""
from fastapi import FastAPI, Request
import base64

app = FastAPI()


@app.get("/convert_to_base64")
def convert_to_base64(term: str):
    """
    This function converts the input string to base64 encoded string.

    Parameters:
    term(str): The file passed to the API.

    Returns:
    string: base64 encoded string.
    """
    base64_bytes = base64.b64encode(bytes(term, 'utf-8'))
    return {"base64": base64_bytes.decode('utf-8'), "message": "Succefully converted the string"}
