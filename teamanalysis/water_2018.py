import pandas as pd;
import numpy as np;
import json
from confing.settings import DATA_DIRS

df = pd.read_excel(DATA_DIRS[0] + '//health_2018.xlsx', engine='openpyxl');
dfh = df.copy();
# 행같은경우 1~18까지 데이터가 광역시별,도의 총통계로 되어있고,
# 열같은경우 물과 관련된 특정 데이터를 추출해야하는데, 특정값을 몰라서 (colunm1~colunm4)로함
#dfc1 = dfc.loc[1:18,['colunm1','colunm2','colunm3','colunm4']];
dfh1 = dfh.loc[1:7,['시도','대형교통사고_사망자수','총인구수','일본뇌염_발생자수']];
dfh2 = dfh.loc[9:17,['시도','대형교통사고_사망자수','총인구수','일본뇌염_발생자수']];
#세종시에 데이터를 제외시키기 위해서, 세종시 위,아래 데이터(dfc1과 dfc2를 concat하였음)
dfh3 = pd.concat([dfh1, dfh2], ignore_index=True,join='outer');
# 특정값(column1)에 대해서 NaN안 경우 값을 0.0으로하였음
dfh3['대형교통사고_사망자수'].replace(np.nan,0.0,inplace=True);
#print(dfh3);

#--------------------------------------------------------------------------------#

df2 = pd.read_excel(DATA_DIRS[0] + '//water_2018.xlsx', engine='openpyxl');
#print(df2);
dfw = df2.copy();
# 데이터를 가져올때, 수자원공사,세종시 데이터는 뺴고 가져옴
# 비교대상 ex)시설용량(㎥/일) 별 과망간산칼륨소비량(기준:10/ 단위:(mg/L)),
# 잔류염소(기준:4/ 단위:(mg/L))으로진행
# 서울,부산,대구,인천,광주,대전,울산

class water:
    def p1(self,x):
        #<수도 사업자가 서울특별시인 지역에, 잔류염소의 평균값 구하기>
        dfw1 = dfw[dfw['수도사업자'].str.contains(x)];
        dfwc1 = dfw1['시설용량(㎥/일)'] * dfw1['잔류염소(기준:4/ 단위:(mg/L))'] * 1000 ;
        dfwc2 = dfw1['시설용량(㎥/일)'].sum();
        dfwc3 = dfwc1.sum();
        dfwc4 = (dfwc3 / dfwc2) *  0.001
        #2018년도의 서울특별시의 잔류염소 평균값 = 0.46615449~
        return(print(dfwc4));
        #람다를 써야하나..?ㅠ

dataw = {
        '서울특별시' : [0.46615449628127115],
        '부산광역시' : [0.6888034488826325],
        '대구광역시' : [0.5711069651741293],
        '인천광역시' : [0.8074644634880428],
        '광주광역시' : [0.6113274336283185],
        '대전광역시' : [0.6110416666666666],
        '울산광역시' : [0.5801515151515151],
        };
dfwc2 = pd.DataFrame(dataw,['2018 광역시별 잔류염소']);
dfwc3 = dfwc2.T;
dfwc4 = dfwc3.reset_index();


#print(dfh3.head(7));
#print(dfwc4);
dfco_18 = pd.concat([dfh3.head(7),dfwc4],ignore_index=False,join='inner',axis=1);
as18 = dfco_18.drop('index', axis=1);
print(as18);
#concat,merge 해봤는데, 겹치는 부분이 안사라짐...


# if __name__ == '__main__':
#     water().p1('서울특별시');
#     water().p1('부산광역시');
#     water().p1('대구광역시');
#     water().p1('인천광역시');
#     water().p1('광주광역시');
#     water().p1('대전광역시');
#     water().p1('울산광역시');