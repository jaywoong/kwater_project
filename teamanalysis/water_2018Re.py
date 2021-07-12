import pandas as pd;
import numpy as np;
import json
from confing.settings import DATA_DIRS

df = pd.read_excel(DATA_DIRS[0] + '//health_2018.xlsx', engine='openpyxl');
df2 = pd.read_excel(DATA_DIRS[0] + '//water_2018.xlsx', engine='openpyxl');
dfh = df.copy();
dfw = df2.copy();

class function():
        #장티푸스발생률, 스트레스인지율, 우울감경험률, 삶의 질
        def reh(self):
            dfh1 = dfh.loc[1:7, ['시도','장티푸스_발생률','스트레스인지율_조율','우울감경험률_조율','삶의질지수(EQ5D)_조율']];
            dfh2 = dfh.loc[9:17, ['시도','장티푸스_발생률','스트레스인지율_조율','우울감경험률_조율','삶의질지수(EQ5D)_조율']];
            # 세종시에 데이터를 제외시키기 위해서, 세종시 위,아래 데이터(dfc1과 dfc2를 concat하였음)
            dfh3 = pd.concat([dfh1, dfh2], ignore_index=True, join='outer');
            print(dfh3);

        #서울, 부산, 대구, 인천, 광주, 대전, 울산
        #질산성질소, 잔류염소, 황산이온, 클로로포름
        def rew(self,x,y):
            dfw1 = dfw[dfw['수도사업자'].str.contains(x)];
            dfwc1 = dfw1['시설용량(㎥/일)'] * dfw1[y] * 1000;
            dfwc2 = dfw1['시설용량(㎥/일)'].sum();
            dfwc3 = dfwc1.sum();
            dfwc4 = ((dfwc3 / dfwc2) * 0.001).round(2);
            print(dfwc4);
            # 2018년도의 서울특별시의 잔류염소 평균값 = 0.46615449~

        def co(self):
            dfh1 = dfh.loc[1:7, ['시도', '장티푸스_발생률', '스트레스인지율_조율', '우울감경험률_조율', '삶의질지수(EQ5D)_조율']];
            dfh2 = dfh.loc[9:17, ['시도', '장티푸스_발생률', '스트레스인지율_조율', '우울감경험률_조율', '삶의질지수(EQ5D)_조율']];
            # 세종시에 데이터를 제외시키기 위해서, 세종시 위,아래 데이터(dfc1과 dfc2를 concat하였음)
            dfh3 = pd.concat([dfh1, dfh2], ignore_index=True, join='outer');
            #print(dfh3);
        #----------------------------------------------------------------------------
            dataw = {
                '서울특별시': [2.0,0.47,13.15,0.01],
                '부산광역시': [1.92,0.69,46.89,0.02],
                '대구광역시': [2.04,0.57,24.93,0.02],
                '인천광역시': [1.94,0.81,13.73,0.02],
                '광주광역시': [0.5,0.61,5.27,0.02],
                '대전광역시': [1.1,0.61,10.67,0.03],
                '울산광역시': [1.37,0.58,47.76,0.0],
                '경기도':[1.93,0.74,13.99,0.02],
                '강원도':[1.58,0.59,7.99,0.01],
                '충청북도':[1.97,0.71,13.56,0.01],
                '충청남도':[2.08,0.7,25.96,0.02],
                '전라북도':[1.65,0.88,8.71,0.02],
                '잔리님도': [0.92,0.6,5.65,0.02],
                '경상북도': [1.98,0.76,26.87,0.02],
                '경상남도': [1.69,0.57,31.96,0.01],
                '제주특별자치도':[2.32,0.45,3.85,0.0],
            };
            dfco = pd.DataFrame(dataw,index=['질산성질소','잔류염소','황산이온','클로로포름']);
            dfco1 = dfco.T
            dfco2 = dfco1.reset_index();
            #print(dfco2);

            dfco3 = pd.concat([dfh3,dfco2],ignore_index=False, join='outer', axis=1);
            dfco4 = dfco3.drop('index', axis=1);

            dfco4.to_excel('./test.xlsx');






#서울특별시, 부산광역시, 대구광역시, 인천광역시, 광주광역시, 대전광역시, 울산광역시
#경기도,강원도,충청북도, 충청남도, 전라북도, 전라남도, 경상북도, 경상남도, 제주특별자치도
if __name__ == '__main__':
        function().co();
          # function().rew('경상남도', '질산성질소(기준:10/ 단위:(mg/L))');
          # function().rew('경상남도', '잔류염소(기준:4/ 단위:(mg/L))');
          # function().rew('경상남도', '황산이온(기준:200/ 단위:(mg/L))');
          # function().rew('경상남도', '클로로포름(기준:0.08/ 단위:(mg/L))');
          # function().rew('제주특별자치도', '질산성질소(기준:10/ 단위:(mg/L))');
          # function().rew('제주특별자치도', '잔류염소(기준:4/ 단위:(mg/L))');
          # function().rew('제주특별자치도', '황산이온(기준:200/ 단위:(mg/L))');
          # function().rew('제주특별자치도', '클로로포름(기준:0.08/ 단위:(mg/L))');




