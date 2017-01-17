# coding=utf-8

# 한줄 주석
"""
여러줄 주석
"""

Myname = '에이미'
print("je m'allelle " + Myname)
print('je m"allelle ' + Myname)
print(Myname * 2)
name = Myname * 3
print(name)
print('\n' * 3)

print('%d' %(7/2))
print('%f' %(7/2))
print('%f' %(7./2.))
print('\n' * 3)

qu = "\"%d Etre ou ne pas etre" % 1
m_qu = ''' telle
est las
question %s\"''' % '---Shakespeare'
new_string = qu + m_qu
print(new_string)
print('\n' * 3)

la_semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', "dimanche"]
print('monday', la_semaine[0])
la_semaine[0] = 'monday'
print("monday", la_semaine[0])
print(la_semaine[1:3])
days = ['mon', 'tue', 'wed']
week = [days, la_semaine]
print(week)
print(week[1][1])
print(week[0][0])
la_semaine.append('Bonjour')
print(week)
la_semaine.insert(1, "aujourdi'hui")
print(week)
la_semaine.remove('jeudi')
la_semaine.sort()
print(week)
la_semaine.reverse()
print(week)
week2 = days + la_semaine;
print(week2)
print(len(la_semaine))
print(max(la_semaine))
print(min(la_semaine))
print('\n' * 3)

pi_tuple = (3, 1, 4, 1, 5, 9)
print(pi_tuple)
new = list(pi_tuple)
print(new)
new_tuple = tuple(new)
print(new_tuple)
i = len(pi_tuple)
print(i)
i = max(pi_tuple)
print(i)
i = min(pi_tuple)
print(i)
print(pi_tuple[1])
print(pi_tuple[-2])
print(pi_tuple[1:3])
print(pi_tuple[3:])
print(pi_tuple + pi_tuple)
print(pi_tuple * 3)
print('\n' * 3)

french_week = {'Monday' : 'lundi', 'Tuesday' : 'mardi', 'Wednesday' : 'mercredi',
'Thursday' : 'jeudi', 'Friday' : 'vendredi', 'Saturday' : 'samedi', 'Sunday' : 'dimanche'}
print(french_week['Friday'])
#del(french_week['Friday'])
print(french_week.keys())
print(french_week.values())
print(french_week.get('Monday'))
print(len(french_week))
print('\n' * 3)

###############################################################################
# if elif else: 스페이스 주의
age = 25
if age > 16:
    print("운전 가능하세요")
else:
    print("운전 불가능하세요")

if age >= 21:
    print("트럭도 운전 가능하세요")
elif age >= 16:
    print("자동차만 운전하세요")
else:
    print("아직 운전 못합니다")

if age > 1 and age <= 18:
    print("생일이 있습니다")
elif age == 21 or age >= 65:
    print("역시 생일이 있군요")
elif not age == 30:
    print("하하하")
else:
    print("생일파티해요")
print('\n' * 3)

#for i in range(10):
#    print(i)
for i in range(0,10):
    print(i),
print('\n' * 3)

###############################################################################
an_en_list = ['dans', "un chant", 'le vent', 'lent', 'des gants', 'un banc',
'le menton', 'enfiler', 'content']
# tuple도 가능
for y in an_en_list:
    print(y)

for x in [2, 4, 6, 8, 10]:
    print(x),
print('\n' * 3)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, 3):
    print(num_list[x])

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])
print('\n' * 3)

i = 0
while i <= 10:
    if i == 9:
        break
    print(i),
    i += 1
print('\n' * 3)

i = 0
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i)
print('\n' * 3)

###############################################################################
def add(f, l):
    sum2 = f + l
    return sum2

print(add(7, 2))
print('\n' * 3)

###############################################################################
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[0:3])
print(alphabet[-3:])
print(alphabet[:-3])
print(alphabet[:3] + " Bonjour")

print('\n' * 3)
print("나는 %d살 이고요, 몸무게는 %.1fkg 이구요, 취미는 %s 입니다." %(19, 67, 'piano'))
print(alphabet.capitalize())
print(len(alphabet))
print(alphabet.replace("A", "B"))
print('\n' * 3)

###############################################################################
t_file = open("t.txt", "wb")
print(t_file.mode)
print(t_file.name)
t_file.write(bytes("안녕하세요\n", 'utf8'))
t_file.close()

tr_file = open('t.txt', 'r')
pp = tr_file.read()
print(pp)
tr_file.close()
print('\n' * 3)

###############################################################################
class Duck_Hunting:
    ducks = 13
    def hunting(self):
        print('Catch!')
        self.ducks -= 1
    def CheckDucks(self):
        if self.ducks <= 0:
            print('Good Dog!')
        else:
            print(str(self.ducks) + "Ducks left.")

print("[dog1]")
dog1 = Duck_Hunting()
dog1.hunting()
dog1.CheckDucks()
print('\n')

print("[dog2]")
dog2 = Duck_Hunting()
dog2.CheckDucks()
for i in range(0, 15):
    dog2.hunting()
    dog2.CheckDucks()
print('\n' * 3)

##########################################################
import sys
print(sys.version)
print('\n' * 3)

##########################################################
class Dog:
#    def __init__(self):
#        print('wowwow')
#    def swim(self):
#        print('I am swimming')
#Amy = Dog()
#Amy.swim()
    def __init__(self, x):
        self.power = x
    def check_power(self):
        print(self.power)

amy = Dog(15)
lex = Dog(1)
lex.check_power()
amy.check_power()
print('\n' * 3)



























print('\n' * 3)
