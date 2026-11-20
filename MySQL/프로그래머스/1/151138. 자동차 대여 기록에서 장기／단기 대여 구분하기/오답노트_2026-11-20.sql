/*
[오답노트] 2026-11-20

문제: 151138 자동차 대여 기록에서 장기/단기 대여 구분하기
유형: SQL 날짜 차이 + CASE WHEN
걸린 시간: 8분, 힌트 1개
막힌 지점:
  1. DATEDIFF(END_DATE, START_DATE) >= 30 으로 써서 실패
     → DATEDIFF는 날짜 사이 간격이라 시작일이 빠짐
       (9/29~10/28 = DATEDIFF 29, 실제 대여 30일)
     → 대여일수 = DATEDIFF(끝, 시작) + 1
원인: 날짜 계산 개념

다음에 같은 유형을 만나면:
* "대여일수/보호일수"처럼 시작일을 포함하는 기간이면 DATEDIFF + 1
* 실패하면 결과 표에서 경계값(딱 30일 근처) 행을 먼저 확인한다
* 날짜끼리 차이는 '-' 대신 DATEDIFF / TIMESTAMPDIFF
  (DATEDIFF(끝, 시작), TIMESTAMPDIFF(단위, 시작, 끝) — 인자 순서 반대)

다시 풀 날짜: 다음 코테 전

* 아래 쿼리는 2026-11-20 통과 제출 사본.
  BaekjoonHub가 재제출 시 원본을 덮어써도 이 파일은 남는다.
*/

SELECT
       HISTORY_ID,
       CAR_ID,
       START_DATE,
       END_DATE,
       CASE
           WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여'
           ELSE '단기 대여'
       END AS RENT_TYPE
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
 WHERE YEAR(START_DATE) = 2022 AND MONTH(START_DATE) = 9
 ORDER
    BY HISTORY_ID DESC
