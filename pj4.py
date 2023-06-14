from datetime import date
import requests
import urllib.parse
import xml.etree.ElementTree as ET
import psycopg2

# 관측지점별 정보 조회_실시간어장정보
url = 'http://apis.data.go.kr/1520635/OceanMensurationService/getOceanMesurationListrisa'
service_key = 'v4dEbTbzaVw6ae3OXS/qoWwKm08yb/0XbRAVa764U2VnQmgeUonlmYi5gBAVA9GSLxQrfYuxcvYu+J7pQ6Z9QQ=='

today = date.today()
formatted_date = today.strftime("%Y%m%d")

gru_nam_list = ['001', '002', '003']

conn = psycopg2.connect(database="database", user="user", password="password", host="123.123.123.123", port="1234")
cur = conn.cursor()

for gru_nam in gru_nam_list:
    params = {
        'serviceKey': urllib.parse.unquote(service_key),
        'GRU_NAM': gru_nam,
        'SDATE': formatted_date,
        'EDATE': formatted_date
    }

    response = requests.get(url, params=params)
    xml_content = response.content
    root = ET.fromstring(xml_content)
    items = root.findall('.//item')

    for item in items:
        gru_nam_value = item.findtext('gruNam')         # 해역
        cdt_1_value = item.findtext('cdt_1')            # 표층염분
        cdt_2_value = item.findtext('cdt_2')            # 중층염분
        cdt_3_value = item.findtext('cdt_3')            # 바닥염분
        dox_1_value = item.findtext('dox_1')            # 포층용존산소
        dox_2_value = item.findtext('dox_2')            # 중층용존산소
        dox_3_value = item.findtext('dox_3')            # 바닥용존산소
        obs_dtm_value = item.findtext('obsDtm')         # 관측일시
        sta_nam_kor_value = item.findtext('staNamKor')  # 관측소명
        sta_cde_value = item.findtext('staCde')         # 관측소코드
        wtr_tmp_1_value = item.findtext('wtrTmp_1')     # 표층수온
        wtr_tmp_2_value = item.findtext('wtrTmp_2')     # 중층수온
        wtr_tmp_3_value = item.findtext('wtrTmp_3')     # 바닥수온
        obs_tim_value = item.findtext('obsTim')         # 관측시간

        print(f"gruNam: {gru_nam_value}")
        print(f"staNamKor: {sta_nam_kor_value}")
        print(f"staCde: {sta_cde_value}")
        print(f"cdt_1: {cdt_1_value}")
        print(f"cdt_2: {cdt_2_value}")
        print(f"cdt_3: {cdt_3_value}")
        print(f"dox_1: {dox_1_value}")
        print(f"dox_2: {dox_2_value}")
        print(f"dox_3: {dox_3_value}")
        print(f"wtrTmp_1: {wtr_tmp_1_value}")
        print(f"wtrTmp_2: {wtr_tmp_2_value}")
        print(f"wtrTmp_3: {wtr_tmp_3_value}")
        print(f"obsTim: {obs_tim_value}")
        print(f"obsDtm: {obs_dtm_value}")
        print('-' * 30)

        cur.execute("""
                    INSERT INTO OBSERVE ("cdt1", "cdt2", "cdt3", "dox1", "dox2", "dox3",
                    "grunam", "obsdtm", "stanamkor", "stacde", "wtrtmp1", "wtrtmp2", "wtrtmp3", "obstim")
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
            cdt_1_value,
            cdt_2_value,
            cdt_3_value,
            dox_1_value,
            dox_2_value,
            dox_3_value,
            gru_nam_value,
            obs_dtm_value,
            sta_nam_kor_value,
            sta_cde_value,
            wtr_tmp_1_value,
            wtr_tmp_2_value,
            wtr_tmp_3_value,
            obs_tim_value
        ))

conn.commit()
cur.close()
conn.close()