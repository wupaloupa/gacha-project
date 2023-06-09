import random
import asyncio

multiply2 = Element("multiply2")
multiply3 = Element("multiply3")
multiply5 = Element("multiply5")
multiply10 = Element("multiply10")
multiply20 = Element("multiply20")
currentscore = Element("score")
log=Element("log")
imgbox = Element("imgbox")
score=100


async def gamestart(*args):
    global score
    mp2=0
    mp3=0
    mp5=0
    mp10=0
    mp20=0
    log.element.innerText=""
    imgbox.element.innerHTML = ""
   
    if multiply2.value != "":
        mp2=int(multiply2.value)
    if multiply3.value != "":
        mp3=int(multiply3.value)
    if multiply5.value != "":
        mp5=int(multiply5.value)
    if multiply10.value != "":
        mp10=int(multiply10.value)
    if multiply20.value != "":
        mp20=int(multiply20.value)
    

    
    x = random.randrange(1,100)
    print(x)



    if mp2==0 and mp3==0 and mp5==0 and mp10==0 and mp20==0:
        log.element.innerText="값을 입력하세요"
    elif mp2+mp3+mp5+mp10+mp20>score:
        log.element.innerText="입력한 값이 보유점수보다 높습니다"
    else:
        score=score-mp20-mp10-mp5-mp3-mp2
        if x<=4:
            result = mp20*20
            imgbox.element.innerHTML = "<video src=\"20.webm\" id=\"video\" autoplay></video>"
        elif x<=12:
            result = mp10*10
            imgbox.element.innerHTML = "<video src=\"10.webm\" id=\"video\" autoplay></video>"
        elif x<=28:
            result = mp5*5
            imgbox.element.innerHTML = "<video src=\"5.webm\" id=\"video\" autoplay></video>"
        elif x<=52:
            result = mp3*3
            imgbox.element.innerHTML = "<video src=\"3.webm\" id=\"video\" autoplay></video>"
        elif x<=100:
            result = mp2*2
            imgbox.element.innerHTML = "<video src=\"2.webm\" id=\"video\" autoplay></video>"
        score=score+result
    await asyncio.sleep(6.5)
    currentscore.element.innerText=f"현재점수:{score}"
    
    
    multiply2.clear()
    multiply3.clear()
    multiply5.clear()
    multiply10.clear()
    multiply20.clear()
