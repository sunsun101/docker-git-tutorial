from fastapi import FastAPI, Request
import requests

app = FastAPI()


#Task 1
@app.post("/convert-to-csv")
async def convert_to_csv(request: Request):
    form_data = await request.form()
    tsv_file = form_data.get("file")

    if not tsv_file.filename.endswith(".tsv"):
        return {"message": "Invalid file format. Please pass TSV file only."}

    contents = await tsv_file.read()
    lines = contents.decode("utf-8").split("\n")

    csv_lines = []
    for line in lines:

        csv_line = ','.join(line.strip().split('\t'))
        csv_lines.append(csv_line)

    print(csv_lines)
    return {"data": csv_lines, "message": "File converted successfully"}

#Task 2

#Task 3

@app.get("/name-to-base64")
def name_to_base64(name: str):
    if (name.lower() == "sunsun"):
        try:
            response = requests.get('http://backend_base64:8000/convert_to_base64?term=' + name.lower())
            return response.json()
        except Exception as e:
            return {"error": f"Error calling API: {str(e)}"}

    else:
        return {"error": "Give name is incorrect. My name is Sunsun."}
