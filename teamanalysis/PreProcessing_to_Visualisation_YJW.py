import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kwater_project.config.settings import DATA_DIRS

# 출력 옵션 변경
pd.set_option('display.max_columns', 70)
pd.set_option('display.max_rows', 100)
#------------------------------------------------------------------------------------
# 2018년 수질 데이터
df_ = pd.read_excel(DATA_DIRS[0] + '//water_2018.xlsx', engine='openpyxl');
df = df_.copy()
#print(df);

#------------------------------------------------------------------------------------
# 2018년 건강 데이터
h_idx = ['시도', '비만율(신체계측)_표준화율', '삶의 질 지수(EQ-5D)_표준화율', '양호한 주관적 건강수준 인지율_표준화율',
         '행복감 지수_표준화율', '스트레스 인지율_표준화율', '우울감 경험률_표준화율', '인지장애 경험률(50세 이상)_표준화율',
         '주관적 구강건강이 나쁜 인구의 분율_표준화율', '스트레스로 인한 정신상담률_표준화율', '우울증상으로 인한 정신상담률_표준화율',
         '연간 보건기관 이용률_표준화율']
df1_ = pd.read_excel(DATA_DIRS[0] + '//health_2008_2018.xlsx', sheet_name=15, usecols=h_idx, nrows=18, engine='openpyxl');
df1 = df1_.copy()
#print(df1.head);
#print(type(df1);

#------------------------------------------------------------------------------------
# 수질데이터_2018
# 필요없는 컬럼 drop (시설명,소재지,수원,채수년원일,총대장균군,대장균,냄새,맛,탁도) 9개
df.drop(['시설명', '소재지', '수원', '채수년월일'], axis=1, inplace=True)
df.drop(['총대장균군(기준:0/ 단위:MPN)', '대장균/분원성대장균군(기준:0/ 단위:MPN)'], axis=1, inplace=True)
df.drop(['냄새(기준:0/ 단위:(mg/L))', '맛(기준:0/ 단위:(mg/L))'], axis=1, inplace=True)
df.drop('탁도(기준:0.5/ 단위:(NTU))', axis=1, inplace=True)
water = df.copy() #(drop한후의 물데이터)
water.rename({'수도사업자': '지역'}, axis=1, inplace=True)
#print(water)

#------------------------------------------------------------------------------------
# 건강데이터 2008~2018 drop
# 필요없는 컬럼 drop(index=0(전국데이터),세종시데이터(중복x)
df1.drop(index=0,inplace=True)   # index 다시 0부터 시작하도록 재설정
#df1.drop('세종특별자치시', axis=0, inplace=True) ==> Nonetype error
df1.drop(index=8,inplace=True);
df1.index = range(16);
health = df1.copy()

#------------------------------------------------------------------------------------
# 물 결측치 값 처리 ( 1.결측치 값 0치환, 2.결측치 행 drop, 3.평균으로...)
# 1 [4985 rows x 57 columns]
water.fillna(0, inplace=True);
#print(water);
# 2 [4657 rows x 57 columns]
# water.dropna(axis=0, inplace=True)
# print(water)
# 3 ~
#print(water)

#------------------------------------------------------------------------------------
#Analysis

class Fx:
    def waterQualByCity(self): #각 지역별 1년 평균 물질 농도를 계산하여 dataframe을 반환하는 함수

        lst = []  # Dataframe 만들기 위해서 준비
        cities = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도',
                  '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
        concs = water.columns[3:]

        for city in cities:
            ct_conc = [city]  # 하나의 도시에 대해, 이름과 모든 물질의 농도를 모은 리스트
            for conc in concs:
                ct_water = water[water['지역'].str.contains(city)]
                if conc == '일반세균(기준:100/ 단위:(CFU/mL))':
                        ct_water.loc[:,'월별물질농도(CFU/일)'] = ct_water.loc[:,'시설용량(㎥/일)'] * ct_water.loc[:,conc] * (10 ** 6)
                        t_conc = ct_water['월별물질농도(CFU/일)'].sum() / ct_water['시설용량(㎥/일)'].sum() * (10 ** -6)
                        # 2018년, xx지역, 일반세균 평균 농도(CFU/mL)
                elif conc == '수소이온농도(기준:5.8 ~ 8.5/ 단위:-)':
                        ct_water.loc[:,conc] = ct_water.loc[:,conc].apply(lambda x: 1 / 10 ** x)  # pH를 [H+](단위:mol/L)로 바꾸는 과정
                        ct_water.loc[:,'월별물질농도(mol/일)'] = ct_water.loc[:,'시설용량(㎥/일)'] * ct_water.loc[:,conc] * 1000
                        t_conc = ct_water.loc[:,('월별물질농도(mol/일)')].sum() / ct_water.loc[:,('시설용량(㎥/일)')].sum() * 0.001
                        # 2018년, xx지역, 수소이온 평균 농도(mol/L)
                        t_conc = -np.log10(t_conc)  # 원래대로 pH로 변환

                else:  # '색도'포함
                        ct_water.loc[:,'월별물질농도(mg/일)'] = ct_water.loc[:,'시설용량(㎥/일)'] * ct_water.loc[:,conc] * 1000
                        t_conc = ct_water.loc[:,'월별물질농도(mg/일)'].sum() / ct_water.loc[:,'시설용량(㎥/일)'].sum() * 0.001
                        # 2018년, xx지역, xx 물질 평균 농도(mg/L)

                ct_conc.append(t_conc)
            lst.append(ct_conc)
        result = pd.DataFrame(lst, columns=['지역'] + list(concs))
        return result
#RuntimeWarning: invalid value encountered in longlong_scalars
#RuntimeWarning: invalid value encountered in double_scalars....
if __name__ == '__main__':
    Fx().waterQualByCity()