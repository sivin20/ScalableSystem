import random
from models import Weather
from price.mockData import mockdata

async def getPrice(weekday: int, time: int, weather: Weather):
    price = mockdata['dailyPrices'][weekday][time]['price']
    weatherFactor = mockdata['weatherAffection'][weather.value]
    return {"price":price * weatherFactor }