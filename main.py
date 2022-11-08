from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, FileResponse
import requests
import json
import random
from pyrogram import *
import secrets
from dateutil import parser
import requests
import os
from pymongo import MongoClient

MONGO_URL = "mongodb+srv://logesh:logesh@cluster0.z75dh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" # https://www.mongodb.com/ 

API_ID = "27764668" # telegram api I'd my.telegram.org
API_HASH = "2d544dd7bb51500fbd8eb557b78d200a" # telegram api hash my.telegram.org
TOKEN = "5735293052:AAEY-ilho-VG3Z86csYnC1in_kDsR9aRkHc" # telegram bot token 
hosturl = "kuki-api-two.vercel.app"
CHAT_ID = -1001151980503 # telegram channel id

async def clientbot():
    bot = Client(
        ':memory:',
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=TOKEN
    )
    await bot.start()
    return bot

app = FastAPI()

@app.get('/api/apikey={api}/{botname}/{owner}/message={msg}')
async def chatbot(api, botname, owner, msg):
    leveldb = MongoClient(MONGO_URL)    
    toggle = leveldb["myFirstDatabase"]["jsons"]
    is_token = toggle.find_one({"ID": api})     
    result = f"https://{hosturl}/chatbot/{botname}/{owner}/message={msg}"
    result = requests.get(result)
    result = result.json() 
    if not is_token:
        url = f"https://{hosturl}/api/apikey={api}/{botname}/{owner}/message={msg}"
        bot = await clientbot()
        await bot.send_message(CHAT_ID, f"Invalid Token\n - {url}")
        ret = {
            "reply": "Invalid Token Please Ask @Awesome_RJ"        
        }    
        return ret
    if is_token:        
        ret = {
            "reply": result["reply"]           
        }
        return ret      


@app.get('/api/apikey={api}/message={msg}')
async def simplechatbot(api, msg):
    leveldb = MongoClient(MONGO_URL)    
    toggle = leveldb["myFirstDatabase"]["jsons"]
    is_token = toggle.find_one({"ID": api})     
    result = f"https://{hosturl}/chatbot/kuki/moezilla/message={msg}"
    result = requests.get(result)
    result = result.json()
    if not is_token:
        url = f"https://{hosturl}/api/apikey={api}/message={msg}"
        bot = await clientbot()
        await bot.send_message(CHAT_ID, f"Invalid Token\n - {url}")
        ret = {
            "reply": "Invalid Token Please Ask @metavoidsupport"        
        }    
        return ret
    if is_token:        
        ret = {
            "reply": result["reply"]           
        }
        return ret      
