#포켓몬 파일이름 변경
import os

for i in os.listdir("포켓몬"):
    A = i.split(".")
    번호 = A[0].zfill(3) 
    이름 = A[1].strip()
    바꿀이름 = f"{번호}_{이름}.png"
    os.rename(f"포켓몬/{i}",f"포켓몬/{바꿀이름}")


    #포켓몬500 이라는 폴더 생성 > 모든 포켓몬을 500x500으로 저장하세요. 

from PIL import Image
import os
from tqdm import tqdm

if os.path.isdir("포켓몬500"):
    pass
else:
    os.mkdir("포켓몬500")

for i in tqdm(os.listdir("포켓몬")):

    img = Image.open(f"포켓몬/{i}")
    img = img.resize((500,500))  #img의 크기를 500x500 으로 세팅!!
    img.save(f"포켓몬500/{i}") #현재 img의 상태를 저장(상대경로) 

#각각의 픽셀의 값을 읽어서 해당 이미지를 검정색으로 색칠하기

from PIL import Image
import os
from tqdm import tqdm

img = Image.open("포켓몬500/001_이상해씨.png")

for i in range(500):
    for j in range(500):
        rgb = img.getpixel((i,j))
        if rgb != (0,0,0,0):
            img.putpixel((i,j), (0,0,0,255))

img.show()

#포켓몬그림자 폴더(폴더생성)에 애들 전체검은색으로 색칠하기

from PIL import Image
import os
from tqdm import tqdm

if os.path.isdir('포켓몬그림자'):
    pass
else:
    os.mkdir('포켓몬그림자')

for k in tqdm(os.listdir("포켓몬500")):
    img = Image.open(f"포켓몬500/{k}")
    for i in range(500):
        for j in range(500):
            rgb = img.getpixel((i,j))
            if rgb[3] > 20:
                img.putpixel((i,j), (0,0,0,255))
    img.save(f"포켓몬그림자/{k}")

