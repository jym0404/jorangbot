import discord
from discord.ext import commands
import asyncio
import os
client = discord.Client()
@client.event
async def on_ready():
    print('logged in')

engdap = {"조랭봇 안녕":"안녕하세요!","조랭봇 뭐해":"저는 사실 기계 안에서 노동을 하고 ㅇ... 살려주세요!!!","조랭봇 사랑해":"에?","조랭봇 사귀자":"에?","조랭봇 꺼져":"싫어요 켜져있을거예요","조랭봇 랭조":"||어쩔티비||","조랭봇 mrpdjxmtld":"축하합니다! 당신은 이스터에그를 발견하셨습니다!\n고로 당신은 크리님의 서버에 들어올 수 있습니다\nhttps://discord.gg/gSuSAN2","조랭봇 크리멍청이":"아 님 멍청이라고요?","조랭봇 ㅎㅇ":"안녕하세요.","조랭봇 ㅂㅇ":"안녕히계세요.","조랭봇 이스터에그":"그걸 알려줄것 같냐? ㅋㅋㅋ.","조랭봇 조랭봇":"저는 발달된 인공지능은 아니고 그냥 커맨드형식으로 만들어진 봇입니다","조랭봇 자기소개":"저는 크리님에 의해 만들어진 응답 봇이랍니다.","조랭봇 크리":"저를 만드신 분이예요!"}

#조랭봇 멤버 개발하기
#for member in message.guilds.members: 써서

@client.event
async def on_message(message):
    if message.content.startswith('조랭봇'):
        if message.content == "조랭봇":
            await message.channel.send("부르셨나요?")
        elif message.content == "조랭봇 도움말":
            now = "-----------------------------------\n"
            for key,value in engdap.items():
                if not key == "조랭봇 mrpdjxmtld":
                    now = now + (key+": "+value+"\n-----------------------------------\n")
            await message.channel.send(now)
        else:
        	try:
        		await message.channel.send(engdap[message.content])
        	except:
        		await message.channel.send("아직 모르는 단어예요!")

client.run(os.environ['token'])