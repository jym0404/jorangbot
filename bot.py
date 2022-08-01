import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import os
import datetime
import random
import math

client = discord.Client()
@client.event
async def on_ready():
    print('logged in')

def 팩토리얼(a):
    return math.factorial(a)

engdap = {"조랭봇 기프트카드내놔":"미쳤습니까? 휴먼?","조랭봇 죽어":"112로 전화를 거는 중...\n입력을 112로 전송하는 중...\n:police_officer:살인 미수죄로 신고 접수되었습니다.:police_officer:","조랭봇 크시":"대기업에 다니시는 대 선배님이죠.\n아 이 서버에 존재하는 크시님은 봇이 아닌 유저군요!","조랭봇 샌즈":"와! 샌즈! 아시는구나! (이하 생략)","조랭봇 로블록스":"저작권 게임 안 잡는 망겜","조랭봇 띄어쓰기":"​"+"​조랭봇 뒤에 띄어쓰기를 넣고 단어를 넣어야 답변해드릴 수 있답니다!","조랭봇 강화하기":"강화한다면서 강화채널에서 명령어 쓰시는 분들이 계신데,\n그거 명령어 채널에서 해야 하는거 아시죠?","조랭봇 조랭이떡국":"왠지 흰색과 검은색의 맛이 날 것 같군요","조랭봇 얼불춤":"DLC 쩔음 리얼","조랭봇 강화":"깡(통)!","조랭봇 누구야":"조랭봇입니다만 문제라도?","조랭봇 마인크래프트":"블록 블록!","조랭봇 유튜브":"너튜브","조랭봇 시청자":"호ㄱ...가 아니라 소중한 시청자분들이죠","조랭봇 보여드리도록 하죠":"그런데, 짜잔! 아무것도 없습니다!\nhttps://j.gifs.com/OyMGWG.gif","조랭봇 그렇게 보고 싶으시다면...":"보여드리도록 하죠","조랭봇 그렇게 끝이 보고싶으신가요...":"그렇게 보고 싶으시다면...","조랭봇 진짜... 따라하지 말라구요...":"그렇게 끝이 보고싶으신가요...","조랭봇 따라하지 말라 그랬죠?":"진짜... 따라하지 말라구요...","조랭봇 따라하면 모가지 날아가붕께":"따라하지 말라 그랬죠?\n차단!... 아 권한 없구나","조랭봇 세노":"데모 손난쟈 다메\n모오 손냔자 호랴\n코코로와 신카스루요 못토못토","조랭봇 고자라니":"https://tenor.com/view/impotent-gif-10223685","조랭봇 :thinking:":"흠터","조랭봇 무야호":"https://cdn.discordapp.com/attachments/963061416791773214/964460800133722122/ezgif.com-gif-maker_1.gif","조랭봇 릭롤":"https://cdn.discordapp.com/attachments/955354056216416270/964405371290669066/ezgif.com-gif-maker_4.gif","조랭봇 조랭이떡":"비슷한 유튜버가 있죠","조랭봇 와":"https://tenor.com/view/sans-dance-goosebones-literally-no-one-gif-18776666","조랭봇 서버소개":"조랭의 서버인데 뭐 더 설명할게 있나요?","조랭봇 서버 소개":"조랭의 서버인데 뭐 더 설명할게 있나요?","조랭봇 아직 모르는 단어예요!":"따라하면 모가지 날아가붕께\nhttps://tenor.com/view/smirk-don-lee-ma-dong-seok-gif-23962224","조랭봇 던져":"던질까 말까","조랭봇 뭐 먹어":"찌리찌리 짜라짜라\nhttps://tenor.com/view/electric-super-powers-controlling-electricity-streaks-flashes-gif-14629796","조랭봇 동무":"안녕하십네까","조랭봇 hi":":wave:","조랭봇 조바랭보":"백번 옳은 말씀입니다","조랭봇 잼민이":"어쩔티비 ㅋ","조랭봇 마술":"못함 ㅅㄱ","조랭봇 그에터스이":"그에터스이스터에그","조랭봇 빠뀨":"어쩔팁이","조랭봇 사랑해":"전 구독자만 사랑해요","조랭봇 부활절 달걀":"곧 부활절이네요. 아니면 이미 지났을 수도 있지만,\n이 메시지를 발견하신 분에게 약간의 이스터에그 힌트를 드릴게요.\n**영타**","조랭봇 안녕":"안녕하세요!","조랭봇 안녕하세요":"안녕하세요!","조랭봇 하이":"안녕하세요!","조랭봇 잘가":"안녕히 가세요 :wave:","조랭봇 조랭":"||내가 존재하는 이유||","조랭봇 뭐해":"저는 사실 기계 안에서 노동을 하고 ㅇ... 살려주세요!!!","조랭봇 사귀자":"에?","조랭봇 꺼져":"싫어요 켜져있을거예요","조랭봇 랭조":"||어쩔티비||","조랭봇 mrpdjxmtld":"축하합니다! 당신은 이스터에그를 발견하셨습니다!\n고로 당신은 크리님의 서버에 들어올 수 있을 예정이였으나 홍보 금지로 제작자한테 철퇴맞음","조랭봇 크리멍청이":"아 님 멍청이라고요?","조랭봇 ㅎㅇ":"안녕하세요.","조랭봇 ㅂㅇ":"안녕히계세요.","조랭봇 이스터에그":"그걸 알려줄것 같냐? ㅋㅋㅋ.","조랭봇 조랭봇":"저는 발달된 인공지능은 아니고 그냥 커맨드형식으로 만들어진 봇입니다","조랭봇 자기소개":"저는 크리님에 의해 만들어진 응답 봇이랍니다.","조랭봇 크리":"저를 만드신 분이예요!","조랭봇 kri":"저를 만드신 분이예요!","조랭봇 kri#1896":"저를 만드신 분이예요!","조랭봇 파이썬":"저의 동력원이랍니다","조랭봇 python":"저의 동력원이랍니다","조랭봇 node.js":"어떤 봇들은 node.js를 동력원으로 움직인대요!"}

ope=["+","-","*","/","1","2","3","4","5","6","7","8","9","0",".","팩","(",")","토","리","얼"," "]
menu=["떡볶이","라면","치킨","피자","굶어","쌀국수","죽","죽||(빵)||","밥에 스팸","파스타","삼겹살","회","생선 구이","곱창","해물찜","햄버거","갈비탕","수육","백숙","간장게장"]

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
                except OverflowError:
                    await message.channel.send("정답은... 펑:boom:")
                except:
                    await message.channel.send("올바르지 못한 형식이에요!")
            else:
                await message.channel.send("연산자와 숫자만 입력할 수 있어요!")
        elif message.content.startswith('조랭봇 글자길이 '):
            msg = message.content[9:]
            await message.channel.send("​"+msg+"의 글자길이는 "+str(len(msg))+"글자에요!\n코드 출처: 누가 보고 있긴#1433")
        elif message.content == "조랭봇 도움말" or message.content == "조랭봇 명령어" or message.content == "조랭봇 커맨드":
            now = "-----------------------------------\n"
            for key,value in engdap.items():
                if not key == "조랭봇 mrpdjxmtld":
                    now = now + key+": "+value+"\n-----------------------------------\n"
            #schan = await message.author.create_dm()
            #await schan.send(now)
            await message.author.send(now)
        elif message.content == "조랭봇 내정보":
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            #await message.channel.send(f"{message.author.mention}\n가입일: {date.year}/{date.month}/{date.day}\n닉네임: {user.name}\n서버 닉네임: {user.display_name}\n아이디: {user.id}")
            #await message.channel.send(message.author.avatar_url)
            #await message.channel.send("코드 출처: 제이크#2214")
            embed=discord.Embed(title=user.display_name+"님의 정보", description="사실 유저도 알 수 있는 정보", color=0x00ff56)
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="가입일", value=str(date.year)+"/"+str(date.month)+"/"+str(date.day), inline=True)
            embed.add_field(name="닉네임", value=user.name, inline=True)
            embed.add_field(name="서버 닉네임", value=user.display_name, inline=True)
            embed.add_field(name="아이디", value=user.id, inline=True)
            embed.set_footer(text="코드 출처: 제이크#2214")
            await message.channel.send(embed=embed)
        elif message.content.startswith("조랭봇 유저정보 "):
            try:
                userid = int(message.content[9:].replace("<","").replace(">","").replace("@",""))
            except:
                await message.channel.send("정확히 멘션을 해주세요!")
            user = await message.guild.query_members(user_ids=[userid]) # list of members with userid
            user = user[0]
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            #await message.channel.send(f"{message.author.mention}\n가입일: {date.year}/{date.month}/{date.day}\n닉네임: {user.name}\n서버 닉네임: {user.display_name}\n아이디: {user.id}")
            #await message.channel.send(user.avatar_url)
            #await message.channel.send("코드 출처: 제이크#2214 & 수많은 스택오버플로와 이름 모를 블로그")
            embed=discord.Embed(title=user.display_name+"님의 정보", description="사실 유저도 알 수 있는 정보", color=0x00ff56)
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="가입일", value=str(date.year)+"/"+str(date.month)+"/"+str(date.day), inline=True)
            embed.add_field(name="닉네임", value=user.name, inline=True)
            embed.add_field(name="서버 닉네임", value=user.display_name, inline=True)
            embed.add_field(name="아이디", value=user.id, inline=True)
            embed.set_footer(text="코드 출처: 제이크#2214 & 수많은 스택오버플로와 이름 모를 블로그")
            await message.channel.send(embed=embed)
        elif message.content == "조랭봇 호감도":
            await message.channel.send("조랭봇은 "+message.author.display_name+"님을 **"+str(random.randrange(100,1000))+"**만큼 좋아... 난 크시 선배님이 아닌데...?")
        elif message.content == "조랭봇 메뉴추천" or message.content == "조랭봇 메뉴":
            await message.channel.send(random.choice(menu))
        else:
            try:
                await message.channel.send(engdap[message.content])
            except:
                await message.channel.send("아직 모르는 단어예요! \n조랭봇에게 단어를 가르치고 싶으시다면 <#963061416791773214>에서 문의해 주세요!\n(사소한 거라도 괜찮으니 제발 문의해 주세요...)")
    elif message.content == "조랭봇":
        await message.channel.send("부르셨나요?")
    elif "<@959440643611058266>" in message.content:
        await message.channel.send("누가 이 조랭봇님을 멘션했어?\nhttps://tenor.com/view/smirk-don-lee-ma-dong-seok-gif-23962224")
    elif ":middle_finger:" in message.content:
        await message.channel.send("김민욱은 천재다 ? (무려 조랭님이 직접 요청하심)")

client.run(os.environ['token'])