#테이블 생성
CREATE TABLE Users(
  name VARCHAR(128),
  email VARCHAR(128)
)
#데이터 입력
INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
#데이터 삭제
DELETE FROM Users WHERE email='ted@umich.edu'
#데이터 갱신
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'
#데이터 추출
SELECT * FROM Users WHERE email='csev@umich.edu'
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name DESC
