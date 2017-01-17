import chien
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_file_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_file_name)

download_web_image("http://image.chosun.com/sitedata/www/section_image/20151208094422041.jpg")

chien.chien()

x = random.randrange(1, 1000)
print(x)

print('\n' * 3)

##########################################################
