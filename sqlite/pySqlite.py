import sqlite3
import qrcode

db = sqlite3.connect("C:/Users/Administrator/Desktop/user.db")
cu = db.cursor()

result = db.execute("""SELECT saveTime FROM User WHERE pos_curr = 1 AND "offset" = 0""")
# print(result.fetchall())
# print(result.fetchone()[0])

restartList = []
for i in range(1, 3000):
    result = db.execute("""SELECT saveTime FROM User WHERE pos_curr = """ + str(i) + """ AND "offset" = 0""")
    result2 = db.execute("""SELECT saveTime FROM User WHERE pos_curr = """ + str(i+1) + """ AND "offset" = 0""")
    time = result2.fetchone()[0] - result.fetchone()[0]
    if time > 30000:
        print(str(i) + "\t\t\t\t" + str(time))
        restartList.append(i - 1)
        restartList.append(i)
        restartList.append(i + 1)
        restartList.append(i + 2)

for i in restartList:
    qr = db.execute("""SELECT qr_str FROM User WHERE pos_curr = """ + str(i) + """ AND "offset" = 0""")
    img = qrcode.make(qr.fetchone()[0])
    img.save(str(i) + ".jpg")

