# 회의 내용 정리

## 작업 시 확인 사항

1. 정수장 데이터 전처리 할 때 단위 확인

   - 시설용량(m^3/일)과 수질평가지표 농도(mg/L)로 부피 단위가 다르기 때문에 바로 곱하면 안됨!
     - 1m^3 = 1000L

   <br>

2. 건강지표 데이터 사용할 때 '조율' 아니라 '표준화율' 컬럼 사용

   <br>

3. Multiple Linear Regression에 넣을 x, y 데이터는 여러 조합 사용해서 오차가 적은 것 찾는 방향으로

   <br>

4. 정수장 데이터에서 '수자원공사' 제외

   <br>

5. 정수장 데이터와 건강지표 데이터 중 한쪽에만 '세종시'가 포함된 경우 --> 제외

   <br>

6. 분석은 "2018년 지역별 수질과 건강지표의 linear regression"을 먼저 수행

   이후 시간이 되면 다른 연도도 진행하여서 "연도별 XX의 농도 변화와 XX지표의 변화 추이" 등을 추가로 확인 



## Git 사용할 때

1. 작업 시작전에 pull을 하여서 가장 최신 버전을 받고 시작하기

   <br>

2. Commit Message 작성할 때 '<동사> <작업파일>' 형식으로 통일하기

```bash
$ git commit -m 'Add analysis.py'
$ git commit -m 'Update anlysis.py'

# 추가 메세지 작성이 필요할 때
$ git commit -m 'Update anlysis_KBH.py
>
>준웅님 작업하셨던 파일에 일부 수정하였습니다'  
```

<br>

2. 파일명은 최종으로 합쳐지기 전까지 '<파일명_KSR.py>'처럼 이니셜을 붙여서 따로 관리하기

   
