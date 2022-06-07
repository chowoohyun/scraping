import sqlite3

#데이터 베이스 생성 명령

conn = sqlite3.connect('test.db',isolation_level=None)
#isolation_level = auto commit 설정값

#파일 오픈 - 데이터 전달 위한 커서 생성 - 쿼리문 제작 - 적용 - 데이터 베이스 닫기


#커서 제작
c = conn.cursor()



#테이블 생성 user (id, name, age)
c.execute('CREATE TABLE IF NOT EXISTS user (id integer PRIMARY KEY,'
          'name test,'
          'age integer)')

#user 테이블에 값을 집어 넣기
#c.execute(('INSERT INTO user(id, name, age) VALUES (?,?,?)')
#          ,(2, '헐크', 35))

#데이터 불러오기
# c.execute("SELECT * FROM user")
# print(c.fetchall())


#데이서 수정
# c.execute("UPDATE user SET name ='토르' WHERE ID = 1")

#데이터 삭제
# c.execute('DELETE FROM user WHERE id = 2')


#쿼리문이 끝나면 종료를 시켜야 한다.
conn.close()