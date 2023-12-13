import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Weather
from price.getPrice import calculatePrice


# weekday: number = 1-7
# time : number = 0-24
# weather : 'rain' | 'clear' | 'cloudy' | 'foggy' 

# params: weekDay=1&time=12&weather=rain



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/price")
async def getPrice(start:int, duration: int, distance: int):
    return calculatePrice(start, duration, distance)


@app.get("/some")
async def read_item():
    return {"msg": 'ok'}