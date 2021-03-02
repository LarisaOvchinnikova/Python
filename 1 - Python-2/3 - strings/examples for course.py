from random import randint, choice
def shifter(s):
    pass


arr = ['IN', 'SIN', 'SOS', 'MOM', 'WOW', 'ON', 'NO', 'NON', 'NOW', 'ION', 'OWN', 'SOON', 'SMS', 'MMS', 'WON', 'WIN', 'SWIM', 'ZOO', 'ZOOM', 'MISS', 'MOON', 'HI', 'SNOW', 'MS', 'SO', 'MONISH', 'SHOW', 'SIX', 'SHOWN', 'SIXMO', 'WHINS', 'WINOS', 'HIMS', 'HINS', 'HISN', 'HOWS', 'IONS', 'MONS', 'NOMS', 'OWNS', 'NOWS', 'SHIN', 'WHIM', 'WHIN', 'WHIZ', 'WHOM', 'WINO', 'WINS', 'WISH', 'WONS', 'ZINS', 'HIM', 'HIS', 'HOW', 'INS', 'ION', 'MIX', 'MOW', 'SOM', 'SON', 'SOW', 'WHO', 'HM', 'IS', 'MI', 'MO', 'OH', 'OI', 'OM', 'OS', 'OW', 'OX', 'SH', 'SI', 'XI', 'HIT', 'HOT', 'NEWS', 'NEW', 'HEX', 'NEXT', 'NICE', 'NOTE', 'SAID', 'SOME', 'SEEN', 'SIZE', 'ONE', 'ZINC', 'ZONE', 'MIND', 'MONDAY', 'OWE', 'OUT', 'KNOW', "GOOD", "THE", "BIG", "SMALL", "SCHOOL", 'BACK', 'BAKE', 'BALD', 'BEAD', 'BIDE', 'BIKE', 'CAFE', 'CAGE', 'CAKE', 'CALF', 'CALK', 'CHAD', 'CHAI', 'CHEF', 'CHIA', 'CHID', 'CLAD', 'DEAF', 'DEAL', 'DECK', 'DELI', 'DICE', 'EACH', 'FACE', 'FADE', 'FAIL', 'FAKE', 'FILE', 'FLAG', 'FLEA', 'GLAD', 'HACK', 'HAKE', 'HALF', 'HEAD', 'HELD', 'HIDE']
n = randint(1, 20)
s = []
for i in range(n):
    s.append(choice(arr))
s = " ".join(s)
print(s)

