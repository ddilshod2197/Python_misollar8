# 1-XARAJATLAR JURNALI 💸
from datetime import datetime

xarajatlar = []

def qoshish(summa, kategoriya):
    sana = datetime.now().strftime("%Y-%m-%d")
    xarajatlar.append({
        "sana": sana,
        "summa": summa,
        "kategoriya": kategoriya
    })

def statistika():
    jami = {}
    for x in xarajatlar:
        jami[x["kategoriya"]] = jami.get(x["kategoriya"], 0) + x["summa"]

    print("📊 Kategoriya bo‘yicha:")
    for k, v in jami.items():
        print(k, ":", v)

def oylik_hisobot(oy):
    print(f"📅 {oy}-oy hisobot:")
    for x in xarajatlar:
        if x["sana"].startswith(oy):
            print(x)

# Ishlatish
qoshish(50000, "Ovqat")
qoshish(20000, "Transport")
qoshish(30000, "Ovqat")

# 2-SUDOKU TEKSHIRUVCHI 🧩
def tekshir(s):
    for i in range(9):
        if len(set(s[i])) != 9:
            return False
        if len(set(row[i] for row in s)) != 9:
            return False

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            blok = []
            for i in range(3):
                for j in range(3):
                    blok.append(s[x+i][y+j])
            if len(set(blok)) != 9:
                return False
    return True

sudoku = [
 [5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,8],
 [1,9,8,3,4,2,5,6,7],
 [8,5,9,7,6,1,4,2,3],
 [4,2,6,8,5,3,7,9,1],
 [7,1,3,9,2,4,8,5,6],
 [9,6,1,5,3,7,2,8,4],
 [2,8,7,4,1,9,6,3,5],
 [3,4,5,2,8,6,1,7,9]
]

print("To‘g‘ri ✅" if tekshir(sudoku) else "Noto‘g‘ri ❌")

# 3-MATN TAHLILCHISI 📖
from collections import Counter
import re

matn = input("Matn kiriting: ").lower()

sozlar = re.findall(r"\w+", matn)
jumlalar = re.split(r"[.!?]", matn)

ort_soz = sum(len(s) for s in sozlar) / len(sozlar)
ort_jumla = len(sozlar) / max(1, len(jumlalar)-1)

print("O‘rtacha so‘z uzunligi:", round(ort_soz, 2))
print("O‘rtacha jumla uzunligi:", round(ort_jumla, 2))

eng_kop = Counter(sozlar).most_common(5)
print("Eng ko‘p ishlatilgan so‘zlar:")
for s, n in eng_kop:
    print(s, ":", n)

# 4-MINI CHATBOT 🤖
javoblar = {
    "salom": "Salom! Qanday yordam beray?",
    "isming": "Men mini chatbotman 😊",
    "yordam": "Savol bering, javob beraman",
    "xayr": "Xayr! Yana ko‘rishamiz 👋"
}

while True:
    savol = input("Siz: ").lower()
    if savol in javoblar:
        print("Bot:", javoblar[savol])
        if savol == "xayr":
            break
    else:
        print("Bot: Tushunmadim 🤔")

# 5-O‘YIN: TIK-TAK-TOU (X-O) 🎮
taxta = [" "]*9

def chiz():
    print(taxta[0:3])
    print(taxta[3:6])
    print(taxta[6:9])

def golib(b):
    g = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    for a,b1,c in g:
        if b[a] == b[b1] == b[c] != " ":
            return True
    return False

oyinchi = "X"

for _ in range(9):
    chiz()
    joy = int(input(f"{oyinchi} joy tanlang (0-8): "))
    if taxta[joy] == " ":
        taxta[joy] = oyinchi
        if golib(taxta):
            chiz()
            print(oyinchi, "yutdi 🎉")
            break
        oyinchi = "O" if oyinchi == "X" else "X"
else:
    print("Durrang 🤝")


statistika()
