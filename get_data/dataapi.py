

#request parameter

#필수항목 : 
# ServiceKey
# sgId 선거아이디 ==> 우리는 20200415

#선택항목
# pageNo 페이지 번호
# numOfRows 페이지당 갯수
# 정당명
# resultType = xml or json

#response Ele
# resultCode ==> 00 :성공
# numOfRows 페이지당 갯수
# pageNo 페이지번호
# totalCount 전체 갯수
# num 결과순서
# partyName 정당명
# prmsCnt 공약갯수
# prmsOrd1 공약순번1
# prmsRealmName1 공약분야명1
# prmsTitle1 공약이름
# prmsCont1 공약내용

#10번까지 잇음
import requests
import json




URL = 'http://apis.data.go.kr/9760000/PartyPlcInfoInqireService/getPartyPlcInfoInqire'
DAY = "20200415"
API_KEY = '?serviceKey=1xchWYQzhGHEZWwvB6UCLFzMCUxgox9p4lZ%2Fbj8%2FaOTeSBZ0cA4NCQt%2BLMgPTljOOxFBjJA5CuFsDfynkT0HXw%3D%3D'
PARTY = ['더불어민주당','미래통합당','민생당','미래한국당','더불어시민당','정의당',
        '우리공화당','민중당','한국경제당','국민의당','친박신당','열린민주당','코리아',
        '가자!평화인권당','가자환경당','공화당','국가혁명배당금당','국민새정당','국민참여신당','기독당',
        '기독자유통일당','기본소득당','깨어있는시민연대당','남북통일당','노동당','녹색당','대한당','대한민국당',
        '미래당','미래민주당','미래자영업당','민중민주당','사이버모바일국민정책당','새누리당','시대전환','여성의당',
        '우리당','자유당','새벽당','정치개혁연합','자영업당','직능자영업당','충청의미래당','친박연대','통일민주당','통합민주당',
        '한국국민당','한국복지당','한나라당','한반도미래연합','홍익당']

# 아래는 정당생성
# for i in PARTY:
#     Party.objects.create(name= i)



# resp = requests.get(URL + API_KEY + '&sgId='+DAY +
#                     '&partyName=더불어시민당&resultType=json')
# print(type(resp))
# py_json = json.loads(resp.text)
# # print(py_json)
# target = py_json
# print(target)
# print(target['partyName'])
# for i in range(1,11):
#     print("============================================")
#     print("순번",target['prmsOrd'+str(i)])
#     print("제목, 분야 : ",target['prmsTitle'+str(i)], target['prmsRealmName'+str(i)])
#     print('내용 :',target['prmmCont'+str(i)])
#     print("====================================================")
#     print("  ")

# for i in PARTY:
#     for j in range(1, 11):
#         if target['prmsTitle'+str(i)] == "":
#             break
        
#         PartyPolicy.objects.create(
#             name=i, number=j, title=target['prmsTitle'+str(j)], 
#             category=target['prmsRealmName'+str(j)], 
#             desc=target['prmmCont'+str(j)])



# 선거구관련 정보수집 API 

# 기본적으로 URL은 api key 와 선거 type code, 그리고 선거 id(날짜)를 포함해둔다.

#추가 필요정보 :pageNo, numOfRows

# URL2 = 'http://apis.data.go.kr/9760000/CommonCodeService/getCommonSggCodeList?serviceKey=1xchWYQzhGHEZWwvB6UCLFzMCUxgox9p4lZ%2Fbj8%2FaOTeSBZ0cA4NCQt%2BLMgPTljOOxFBjJA5CuFsDfynkT0HXw%3D%3D&sgId=20200415&sgTypecode=2&resultType=json'

# pagenum_list = [1,2,3]
# list_cnt = 100


# resp = requests.get(URL2+'&pageNo=3&numOfRows=100')
# json_result = json.loads(resp.text)
# # print(json_result)

# city_list = json_result['getCommonSggCodeList']['item']

# index=0
# for i in city_list:
#     print(index)
#     print('',i['SGG_NAME'])
#     print('', i['SD_NAME'])
#     print('', i['WIW_NAME'])
#     print("========================================")
#     index +=1

#후보자 API

URL3 = 'http://apis.data.go.kr/9760000/PofelcddInfoInqireService/getPofelcddRegistSttusInfoInqire?serviceKey=1xchWYQzhGHEZWwvB6UCLFzMCUxgox9p4lZ%2Fbj8%2FaOTeSBZ0cA4NCQt%2BLMgPTljOOxFBjJA5CuFsDfynkT0HXw%3D%3D&pageNo=1&numOfRows=120&sgId=20200415&sgTypecode=2&resultType=json'

resp = requests.get(URL3)
json_result = json.loads(resp.text)
# print(json_result)
# 후보자 리스트
candi_list = json_result['getPofelcddRegistSttusInfoInqire']['item']


# 우리가 가져올 key값
# HUBOID
# SGG_NAME
# SD_NAME
# GENDER
# WIW_NAME
# GIHO

# JD_NAME
# NAME
#BIRTHDAY
#AGE
#ADDR
#JOB
#EDU
#CAREER1
#CAREER2
#STATUS
for i in candi_list:
    print(i['NAME'])
    print(i['HUBOID'])
    print(i['SGG_NAME'])
    print(i['GENDER'])
    print("===============")