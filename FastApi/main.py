from fastapi import FastAPI, Path, Query, status, Body, Cookie
from fastapi.responses import JSONResponse, RedirectResponse, FileResponse, Response
from datetime import datetime
import uuid

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())

people = [Person("Egor", 11), Person("Ilya", 52), Person("Eleonora", 46)]

def find_person(id):
    for person in people:
        if person.id == id:
            return person
    return None

app = FastAPI()

@app.get("/")
async def main():
    return FileResponse("public/index.html")

@app.get("/api/users")
def get_people():
    return people

@app.get("/api/users/{id}")
def get_person(id):
    person = find_person(id)
    print(person)
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден."}  # Исправлено messeage -> message
        )
    return person

@app.post("/api/users")
def create_person(data = Body()):
    person = Person(data["name"], data["age"])
    people.append(person)
    return person

@app.put("/api/users")
def edit_person(data = Body()):
    person = find_person(data["id"])
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}  # Исправлено messeage -> message
        )
    person.age = data["age"]
    person.name = data["name"]
    return person

@app.delete("/api/users/{id}")
def delete_person(id):
    person = find_person(id)

    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"} 
        )
    people.remove(person)
    return person

@app.get("/test/cookie")
def root():
    now = datetime.now()
    response = JSONResponse(content={"message": "куки установлены"})
    response.set_cookie(key="last_visit", value=now.isoformat())  
    return response

@app.get("/test/get/cookie")
def get_cookie(last_visit: str | None = Cookie(default=None)):
    if last_visit is None:  
        return {"message": "Это первый ваш визит на сайт"}  
    else:
        return {"message": f"Ваш последний визит {last_visit}"}  