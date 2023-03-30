from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def users():
    users = [
        {
            "name": "Clement Lumumba",
            "age": 25,
            "city": "Eldoret, Kenya"
        },

        {
            "name": "Victor Omondi",
            "age": 23,
            "city": "Nakuru, Kenya"
        },

        {
            "name": "Lawrence Moruye",
            "age": 30,
            "city": "Kisii, Kenya"
        }
    ]

    return users