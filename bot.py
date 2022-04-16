import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import os
import datetime

client = discord.Client()
@client.event
async def on_ready():
    print('logged in')

engdap = {"조랭봇 따라하면 모가지 날아가붕께":"따라하지 말라 그랬죠?\n차단!... 아 권한 없구나","조랭봇 세노":"데모 손난쟈 다메\n모오 손냔자 호랴\n코코로와 신카스루요 못토못토","조랭봇 고자라니":"https://tenor.com/view/impotent-gif-10223685","조랭봇 :thinking:":"흠터","조랭봇 무야호":"https://cdn.discordapp.com/attachments/963061416791773214/964460800133722122/ezgif.com-gif-maker_1.gif","조랭봇 릭롤":"https://cdn.discordapp.com/attachments/955354056216416270/964405371290669066/ezgif.com-gif-maker_4.gif","조랭봇 조랭이떡":"비슷한 유튜버가 있죠","조랭봇 와":"https://tenor.com/view/sans-dance-goosebones-literally-no-one-gif-18776666","조랭봇 서버소개":"조랭의 서버인데 뭐 더 설명할게 있나요?","조랭봇 서버 소개":"조랭의 서버인데 뭐 더 설명할게 있나요?","조랭봇 아직 모르는 단어예요!":"따라하면 모가지 날아가붕께\nhttps://tenor.com/view/smirk-don-lee-ma-dong-seok-gif-23962224","조랭봇 던져":"던질까 말까","조랭봇 뭐 먹어":"찌리찌리 짜라짜라\nhttps://tenor.com/view/electric-super-powers-controlling-electricity-streaks-flashes-gif-14629796","조랭봇 동무":"안녕하십네까","조랭봇 hi":":wave:","조랭봇 조바랭보":"백번 옳은 말씀입니다","조랭봇 잼민이":"어쩔티비 ㅋ","조랭봇 마술":"못함 ㅅㄱ","조랭봇 그에터스이":"그에터스이스터에그","조랭봇 빠뀨":"어쩔팁이","조랭봇 사랑해":"전 구독자만 사랑해요","조랭봇 부활절 달걀":"곧 부활절이네요. 아니면 이미 지났을 수도 있지만,\n이 메시지를 발견하신 분에게 약간의 이스터에그 힌트를 드릴게요.\n**영타**","조랭봇 안녕":"안녕하세요!","조랭봇 안녕하세요":"안녕하세요!","조랭봇 하이":"안녕하세요!","조랭봇 잘가":"안녕히 가세요 :wave:","조랭봇 조랭":"||내가 존재하는 이유||","조랭봇 뭐해":"저는 사실 기계 안에서 노동을 하고 ㅇ... 살려주세요!!!","조랭봇 사귀자":"에?","조랭봇 꺼져":"싫어요 켜져있을거예요","조랭봇 랭조":"||어쩔티비||","조랭봇 mrpdjxmtld":"축하합니다! 당신은 이스터에그를 발견하셨습니다!\n고로 당신은 크리님의 서버에 들어올 수 있을 예정이였으나 홍보 금지로 제작자한테 철퇴맞음","조랭봇 크리멍청이":"아 님 멍청이라고요?","조랭봇 ㅎㅇ":"안녕하세요.","조랭봇 ㅂㅇ":"안녕히계세요.","조랭봇 이스터에그":"그걸 알려줄것 같냐? ㅋㅋㅋ.","조랭봇 조랭봇":"저는 발달된 인공지능은 아니고 그냥 커맨드형식으로 만들어진 봇입니다","조랭봇 자기소개":"저는 크리님에 의해 만들어진 응답 봇이랍니다.","조랭봇 크리":"저를 만드신 분이예요!","조랭봇 kri":"저를 만드신 분이예요!","조랭봇 kri#1896":"저를 만드신 분이예요!","조랭봇 파이썬":"저의 동력원이랍니다","조랭봇 python":"저의 동력원이랍니다","조랭봇 node.js":"어떤 봇들은 node.js를 동력원으로 움직인대요!"}

ope=["+","-","*","/","1","2","3","4","5","6","7","8","9","0"]

#조랭봇 멤버 개발하기
#for member in message.guilds.members: 써서

@client.event
async def on_message(message):
    if message.content.startswith('조랭봇 '):
        if message.content.startswith('조랭봇 계산 '):
            calcstr = message.content[7:]
            checkope = 0
            for i in ope:
                checkope = checkope + calcstr.count(i)
            if checkope == len(calcstr):
                try:
                    await message.channel.send("정답은 "+str(eval(calcstr))+"이에요!")
                except:
                    await message.channel.send("올바르지 못한 형식이에요!")
            else:
                await message.channel.send("연산자와 숫자만 입력할 수 있어요!")
        if message.content.startswith('조랭봇 글자길이 '):
            msg = message.content[9:]
            await message.channel.send(msg+"의 글자길이는 "+str(len(msg))+"글자에요!\n코드 출처: 누가 보고 있긴#1433")
        elif message.content == "조랭봇 도움말" or message.content == "조랭봇 명령어" or message.content == "조랭봇 커맨드":
            now = "-----------------------------------\n"
            for key,value in engdap.items():
                if not key == "조랭봇 mrpdjxmtld":
                    now = now + key+": "+value+"\n-----------------------------------\n"
            schan = await message.author.create_dm()
            await schan.send(now)
        elif message.content == "조랭봇 내정보":
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            await message.channel.send(f"{message.author.mention}\n가입일: {date.year}/{date.month}/{date.day}\n닉네임: {user.name}\n서버 닉네임: {user.display_name}\n아이디: {user.id}")
            await message.channel.send(message.author.avatar_url)
            await message.channel.send("코드 출처: 제이크#2214")
        elif message.content.startswith("조랭봇 유저정보 "):
            await message.channel.send("유저정보 호출 감지")
            try:
                userid = int(message.content[9:].replace("<","").replace(">","").replace("@",""))
                await message.channel.send(userid)
            except:
                await message.channel.send("정확히 멘션을 해주세요!")
            await message.channel.send(message)
            await message.channel.send(message.guild)
            user = get(client.get_all_members(), id=str(userid))
            await message.channel.send(user)
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            await message.channel.send(f"{message.author.mention}\n가입일: {date.year}/{date.month}/{date.day}\n닉네임: {user.name}\n서버 닉네임: {user.display_name}\n아이디: {user.id}")
            await message.channel.send(message.author.avatar_url)
            await message.channel.send("코드 출처: 제이크#2214 & 수많은 스택오버플로와 이름 모를 블로그")
        else:
            try:
                await message.channel.send(engdap[message.content])
            except:
                await message.channel.send("아직 모르는 단어예요! \n조랭봇에게 단어를 가르치고 싶으시다면 <#963061416791773214>에서 문의해 주세요!\n(사소한 거라도 괜찮으니 제발 문의해 주세요...)")
    elif message.content == "조랭봇":
        await message.channel.send("부르셨나요?")

client.run(os.environ['token'])