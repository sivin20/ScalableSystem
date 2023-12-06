import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Weather
from price.getPrice import getPrice


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
async def getPrice(weekday: int, time: int, weather: Weather):
    return await getPrice(weekday, time, weather)


@app.get("/some")
async def read_item():
    return {"msg": 'ok'}