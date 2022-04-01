import discord
import from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
    print('logged in')

engdap = {"랭조봇 안녕":"안녕하세요!","랭조봇 뭐해":"저는 사실 기계 안에서 노동을 하고 ㅇ... 살려주세요!!!","랭조봇 사랑해":"에?","랭조봇 사귀자":"에?","랭조봇 꺼져":"싫어요 켜져있을거예요","랭조봇 랭조":"||어쩔티비||","랭조봇 mrpdjxmtld":"축하합니다! 당신은 이스터에그를 발견하셨습니다!\n고로 당신은 크리님의 서버에 들어올 수 있습니다\nhttps://discord.gg/gSuSAN2","랭조봇 크리멍청이":"아 님 멍청이라고요?","랭조봇 ㅎㅇ":"안녕하세요.","랭조봇 ㅂㅇ":"안녕히계세요.","랭조봇 이스터에그":"그걸 알려줄것 같냐? ㅋㅋㅋ.","랭조봇 랭조봇":"저는 발달된 인공지능은 아니고 그냥 커맨드형식으로 만들어진 봇입니다","랭조봇 자기소개":"저는 크리님에 의해 만들어진 응답 봇이랍니다.","랭조봇 크리":"저를 만드신 분이예요!"}

#랭조봇 멤버 개발하기
#for member in message.guilds.members: 써서

@client.event
async def on_message(message):
    if message.content.startswith('랭조봇'):
        if message.content == "랭조봇":
            await message.channel.send("부르셨나요?")
        elif message.content == "랭조봇 도움말":
            now = "-----------------------------------\n"
            for key,value in engdap.items():
                if not key == "랭조봇 mrpdjxmtld":
                    now = now + (key+": "+value+"\n-----------------------------------\n")
            await message.channel.send(now)
        elif message.content == "랭조봇 서버멤버":
            for member in message.guilds.members:
                await message.channel.send("--------------------")
                await message.channel.send(member)
            await message.channel.send("--------------------")
        else:
        	try:
        		await message.channel.send(engdap[message.content])
        	except:
        		await message.channel.send("아직 모르는 단어예요!")
        '''elif message.content == "랭조봇 안녕":
            await message.channel.send("안녕하세요.")
        elif message.content == "랭조봇 뭐해":
            await message.channel.send("게임하... 아니 님하고 채팅하고 있었지요.")
        elif message.content == "랭조봇 사랑해":
            await message.channel.send("에?")
        elif message.content == "랭조봇 사귀자":
            await message.channel.send("에?")
        elif message.content == "랭조봇 꺼져":
            await message.channel.send("어떻게 그렇게 심한 말을!")
        elif message.content == "랭조봇 둠피는?":
            await message.channel.send("상향해야죠!")
        elif message.content == "랭조봇 화":
            await message.channel.send("||려한 조명이 나를 감싸네~||")
        elif message.content == "랭조봇 존":
            await message.channel.send("||시나||")
        elif message.content == "랭조봇 ㅋㅋ":
            await message.channel.send("루ㅋㅋ")
        elif message.content == "랭조봇 mrpdjxmtld":
            await message.channel.send("축하합니다! 당신은 이스터에그를 발견하셨습니다!\n고로 당신은 크리님의 서버에 들어올 수 있습니다\nhttps://discord.gg/gSuSAN2")
        elif message.content == "랭조봇 크리멍청이":
            await message.channel.send("아 숙녀 멍청이라고요?")
        elif message.content == "랭조봇 ㅎㅇ":
            await message.channel.send("안녕하세요.")
        elif message.content == "랭조봇 ㅂㅇ":
            await message.channel.send("안녕히계세요.")
        elif message.content == "랭조봇 이스터에그":
            await message.channel.send("그걸 알려줄 것 같냐? ㅋㅋㅋ.")
        else:
            await message.channel.send("아직 모르는 단어예요!")'''
client.run(os.environ['token'])

