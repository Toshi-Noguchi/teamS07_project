import sqlite3

con = sqlite3.connect('test.db')

#con.execute("CREATE TABLE プロフィール情報(id INTEGER PRIMARY KEY, name STRING, password STRING)")
#検証のため具体的にユーザを登録
con.execute("INSERT INTO プロフィール情報(id,name,password) values(1,'y','yuchifuji')")
con.commit()
print("ぱいそん")