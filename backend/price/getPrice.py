import random
from models import Weather


async def getPrice(weekday: int, time: int, weather: Weather):
    return {"price": random.randint(0, 10000)}