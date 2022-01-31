## SQL 정리
- ORDER BY: 순으로 정렬
- ORDER BY __ DESC: 역순으로 정렬 
- WHERE: 중 ...한
- WHERE NOT: 중 ...하지 않은
- ORDER BY __1__, __2__: 1기준으로 정렬, 1이 같으면 2기준으로 정렬
- LIMIT __: __ 까지만 출력
  - 첫번째 것만 출력하려면 LIMIT 1, MIN()
  - 마지막 것만 출력하려면 MAX()
- COUNT(): 갯수 세기
- DISTINCT: NULL인 경우 집계하지 않으며 중복되는 이름은 한개로 취급

<b>단순히 COUNT 함수로 데이터를 조회하면 전체갯수를 가져옴 그대신 유형별로 갯수를 알고 싶을 때</b>
```
  - GROUP BY: 특정 컬럼을 그룹화
  - HABING: 특정 컬럼을 그룹화한 결과에 조건을 검 
```  
<b>날짜 데이터에서 일부만 추출하기</b>
```
  - YEAR: 연도 추출
  - MONTH: 월 추출
  - DAY: 일 추출
  - HOUR: 시 추출
  - MINUTE: 분 추출
  - SECOND: 초 추출
```
- BETWEEN A AND B: A, B 포함 그 사이 모든 값
- IS NULL: 특정 컬럼이 NULL 일때 WHERE __ IS NULL 이렇게 사용가능
- IS NOT NULL: 특정 컬럼이 있을때 WHERE __ IS NOT NULL 이렇게 사용가능
- IFNULL: IFNULL(Column명, "Null일 경우 대체 값")
- COALESCE(Column명1, Column명2, Column명3, Column명4): Column1 ~ 4 중 NULL이 아닌 첫 번째 Column을 출력

<b>LEFT JOIN</b>
첫번째 테이블을 기준으로, 두번째 테이블을 조합하는 JOIN
```
첫번째 테이블 이름 LEFT JOIN 두번째 테이블 이름 ON 조건
```
<img src="https://user-images.githubusercontent.com/60960130/151730186-b215aa6b-c830-4335-bb07-9381ca62354a.png" width="350" height="200"/>

예를들어 조건이 첫번째 테이블 이름.NAME = 두번째 테이블 이름.NAME <br />
이 경우 두개의 NAME값이 일치하지 않는 경우에 테이블의 모든 필드 NULL

<b>RIGHT JOIN</b>
두번째 테이블을 기준으로, 첫번째 테이블을 조합하는 JOIN
```
첫번째 테이블 이름 LEFT JOIN 두번째 테이블 이름 ON 조건
```
<img src="https://user-images.githubusercontent.com/60960130/151759606-72c1582d-e56b-4646-9e87-4820233c25f9.png" width="350" height="200"/>

<b>INNER JOIN</b>
INNER JOIN = JOIN = CROSS JOIN
```
첫번째 테이블 이름 INNER JOIN 두번째 테이블 이름 ON 조건
```
<img src="https://user-images.githubusercontent.com/60960130/151760791-ab0b3dd5-851a-45eb-8322-ea7dc623cdf5.png" width="350" height="200"/>

JOIN문제여도 JOIN을 사용하지 않아도 해결 가능 - 두가지 버전으로 연습하기!
```
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I LEFT JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME IS NULL
ORDER BY I.DATETIME
LIMIT 3;

SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
ORDER BY DATETIME
LIMIT 3;

```
- 같지 않음을 표현하는 연산자
  - !=
  - ^=
  - <>
  - NOT 칼럼명 = 
- 특정 문자열에서 찾고자 하는, 특정문자가 포함되어 있는지 확인 
  - 특정문자열 LIKE "%찾고자 하는 문자열%" 
  - INSTR(특정문자열, 찾고자하는 문자열): 있으면 위치 반환 없으면 0반환
