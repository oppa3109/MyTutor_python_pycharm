import chien
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_file_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_file_name)

download_web_image("http://imgnews.naver.net/image/001/2017/01/17/PYH2017011719910001300_P2_99_20170117161030.jpg?type=w540")
chien.chien()

x = random.randrange(1, 1000)
print(x)
print('\n' * 3)

##########################################################
