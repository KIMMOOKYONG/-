# Query 함수 사용법
- Pandas에서 조건에 부합하는 데이터를 추출할 때 가장 많이 사용하는 Query 함수
- 장점은 가독성과 편의성이 최대 장점
- 단점은 .loc[ ] 로 구현한 것보다 속도가 느림

## Query 함수는 아래 6가지 기능
- 1) 비교 연산자( ==, >, >=, <, <=, != )
- 2) in 연산자( in, ==, not in, != )
- 3) 논리 연산자(and, or, not)
- 4) 외부 변수(또는 함수) 참조 연산
- 5) 인덱스 검색
- 6) 문자열 부분검색( str.contains, str.startswith, str.endswith )

