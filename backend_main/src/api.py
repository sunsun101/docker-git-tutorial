"""
Author: Sunsun Kasajoo
Date: March 18, 2023

This module contains apis.
"""

from fastapi import FastAPI, Request, UploadFile
import requests
from PIL import Image, ImageDraw
import io
import base64

app = FastAPI()


# Task 1
@app.post("/convert-to-csv")
async def convert_to_csv(file: UploadFile):

    """
    This function converts the input tsv file and return array of csv lines.

    Parameters:
    file (UploadFile): The file passed to the API.

    Returns:
    array: The array containing csv lines.
    """

    if not file.filename.endswith(".tsv"):
        return {"message": "Invalid file format. Please pass TSV file only."}

    contents = await file.read()
    lines = contents.decode("utf-8").split("\n")

    csv_lines = []
    for line in lines:

        csv_line = ','.join(line.strip().split('\t'))
        csv_lines.append(csv_line)

    print(csv_lines)
    return {"data": csv_lines, "message": "File converted successfully"}


# Task 2
@app.post("/bounding-box")
async def draw_bounding_box(image_file: UploadFile, x_topleft: float, y_topleft: float, width: float, height: float):

    """
    This function takes image as input and draws bounding box according to the data provided.

    Parameters:
    image_file (UploadFile): The image passed to the api.
    x_topleft: coordinate of x axis start point.
    y_topleft: coordinate of y axis start point.
    width: width of the bounding box.
    height: height of the bounding box.

    Returns:
    string: base64 encode string of image.
    """

    image_bytes = await image_file.read()
    img = Image.open(io.BytesIO(image_bytes)).convert("RGBA")

    if x_topleft + width < img.width or y_topleft + height < img.height:
        return "Invalid bounding box"

    draw = ImageDraw.Draw(img)

    draw.rectangle((x_topleft, y_topleft, x_topleft + width,
                   y_topleft + height), outline="red")

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_str = base64.b64encode(img_byte_arr.getvalue()).decode("ascii")

    return {"image": img_str, "message": "Successfully drawn a bounding box"}


# Task 3
@app.get("/name-to-base64")
def name_to_base64(name: str):
    """
    This function takes name as input and checks if it is 'Sunsun' and calls api in another container.

    Parameters:
    name (str): The name field passes as query param.

    Returns:
    string: base64 encode string of name.
    """
    if (name.lower() == "sunsun"):
        try:
            response = requests.get(
                'http://backend_base64:8000/convert_to_base64?term=' + name.lower())
            return response.json()
        except Exception as e:
            return {"error": f"Error calling API: {str(e)}"}

    else:
        return {"error": "Give name is incorrect. My name is Sunsun."}
