from fastapi import FastAPI

student ={
    1:{
        "name":"Deep",
        "age":20,
        "city":"Porbandar"
    }
}
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def get_item(item_id):
    return {"item_id": item_id}


@app.get("/get-by-name/")
def get_by_name(name:str):
    for student_id in student:
        if student[student_id]["name"] == name:
            return student[student_id]
    return {"Data":"Item not found"}

