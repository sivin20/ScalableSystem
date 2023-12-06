import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
async def read_item(weekday, time, weather):
    return {"price": random.randint(0, 10000)}


@app.get("/some")
async def read_item():
    return {"msg": 'ok'}