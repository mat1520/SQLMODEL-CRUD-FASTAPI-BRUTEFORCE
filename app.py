from fastapi import FastAPI
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

db = []
id_counter = 1
app = FastAPI()

@app.get("/")
def read_root():
    return {"Actividad: CRUD de Usuarios + Prueba controlada de fuerza bruta contra tu propia API"}

@app.post("/users")
def crear_usuario(username: str, password: str):
    global id_counter
    id = id_counter
    id_counter += 1
    user = Hero(id=id, username=username, password=password)
    db.append(user)
    return user

@app.get("/users")
def get_users():
    return {"users": db}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((user for user in db if user.id == user_id), None)
    if user:
        return user
    return {"Usuario no encontrado"}

@app.put("/users/{user_id}")
def update_user(user_id: int, username: str | None = None):
    user = next((user for user in db if user.id == user_id), None)
    if user:
        if username:
            user.username = username
        return user
    return {"Usuario no encontrado"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, username: str):
    global db
    user = next((user for user in db if user.id == user_id and user.username == username), None)
    if user:
        db = [u for u in db if u.id != user_id]
        return {"Usuario eliminado": user}
    return {"Usuario no encontrado o credenciales incorrectas"}

@app.post("/login")
async def login(username: str, password: str):
    user = next((user for user in db if user.username == username and user.password == password), None)
    if user:
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}