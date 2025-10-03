from fastapi import FastAPI
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

db = []
app = FastAPI()

@app.get("/")
def read_root():
    return {"Actividad": "CRUD de Usuarios + Prueba controlada de fuerza bruta contra tu propia API"}

@app.post("/users")
def crear_usuario(username: str, password: str):
    user = Hero(id=len(db) + 1, username=username, password=password)
    db.append(user)
    return user

@app.get("/users")
def get_users():
    return {"users": db}

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in db:
        if user.id == user_id:
            return user
    return {"error": "Usuario no encontrado"}

@app.put("/users/{user_id}")
def update_user(user_id: int, username: str):
    for user in db:
        if user.id == user_id:
            user.username = username
            return user
    return {"error": "Usuario no encontrado"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, username: str):
    for i, user in enumerate(db):
        if user.id == user_id and user.username == username:
            db.pop(i)
            return {"success": "Usuario eliminado"}
    return {"error": "Usuario no encontrado"}

@app.post("/login")
def login(username: str, password: str):
    for user in db:
        if user.username == username and user.password == password:
            return {"message": "Login successful"}
    return {"message": "Invalid credentials"}