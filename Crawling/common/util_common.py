# -*- coding: UTF-8 -*-

# import data.onch_info as Info
import json
from datetime import date
from datetime import datetime
from pytz import timezone
import math
import numpy as np
import random
from bs4 import BeautifulSoup
import re
from itertools import combinations
import inspect
# import src.coupang.data.shipcode as Scode
# import data.brand_kr_en as br
# from src.lib.lib_login_info import Login_info

# login_info = Login_info()

man = 10000

no_except_word_list = ['짭', '다이소', '쿠팡', '네이버', '명품', '재고정리', '고객만족', '빠른배송', '오너클랜',
               '온채널', '마감세일', '할인쿠폰', '추가', '당일출고', '되세요', '감사합니다', '필수',
                '매입', '쇼핑몰', '리뷰', '추첨', '기획', '추천', '스마트스토어', '도매콜']

def get_vendorId(cp_no):
    return login_info.get_cp_vendorid(cp_no)

def getSoupHtml(resp):
    soup = None
    try:
        soup = BeautifulSoup(resp.text, 'html.parser')
        return soup
    except Exception as ex:
        print('Requestsinsang getSoupSinsing:', ex)
        print(ex.__cause__)
        print(ex.__class__)
        print(ex.__context__)
        return soup

# BeautifulSoup - html parser
def setBeautifulSoupParserNoText(resp):
    soup = None
    try:
        # soup = BeautifulSoup(resp, 'html.parser')
        soup = get_soup_bs_content(resp)
        return soup
    except Exception as ex:
        print('Requestsinsang getSoupSinsing:', ex)
        print(ex.__cause__)
        print(ex.__class__)
        print(ex.__context__)
        return soup

def get_soup_bs_content(resp):
    soup = BeautifulSoup(resp.content, 'lxml')
    return soup

def get_soup_bs_text(resp):
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup

def get_soup_bs_no_text(resp):
    soup = BeautifulSoup(resp, 'lxml')
    return soup

def setPretty(soup):
    return soup.prettify()

def set_bs_decode(resp):
    soup = None
    try:
        soup = BeautifulSoup(resp.content.decode('utf-8'), 'lxml')
        return soup
    except Exception as ex:
        print('set_bs_decode :', ex)
        print(ex.__cause__)
        print(ex.__class__)
        print(ex.__context__)
        return soup

################

# random - sleep
def getRandom(fint = 1, tint = 5):
    np.random.seed(1)
    ran = int(random.randint(fint, tint))
    return ran

###################
# 우편코드
###################
def get_ship_code(shipnm):
    if shipnm == '롯데택배(구현대택배)송장복사':
        shipnm = '롯데택배'
    return Scode.ship_code[shipnm]


###################
# Date
###################
# 2021-11-13
def getDateToday():
    today = date.today()
    return today.strftime('%Y-%m-%d')

def getDateMonth():
    today = date.today()
    return today.strftime('%Y-%m')

# 20210615
def getDateTodayNoDash():
    today = date.today()
    return today.strftime('%Y%m%d')

#%H:%M:%S
def getTodayTime():
    today = date.today()
    return today.strftime('%y-%m-%d-%H-%M-%S')

def getNowDay():
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%y%m%d")

def getNowDayTime():
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%y%m%d_%H%M%S")

def get_today_timeTime(today):
    import datetime
    now = datetime.datetime.now()
    today_time = today + now.strftime("_%H%M%S")
    return today_time

def get_timeTime():
    import datetime
    now = datetime.datetime.now()
    time = now.strftime("_%H%M%S")
    return time

def get_now_cp_time():
    import datetime
    now = datetime.datetime.now()
    format_iso_now = now.isoformat()
    return now.strftime("%Y-%m-%dT%H:%M:%S")

def get_today_from_month(today):
    if today != '*':
        to_split = today.split('-')
        to_tmp = to_split[:-1]
        today = to_tmp[0] + '-' + to_tmp[1]
        # print(today)
    else:
        today = getDateMonth()
    return today

def getTodayyymm():
    today = date.today()
    return today.strftime('%Y.%m')

def getSplitYYMMDate(dat):
    tmp = dat.split('.')
    yy = tmp[0].strip()
    mm = tmp[1].strip()
    return yy, mm



def kst_time():
    # fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    # UTC = datetime.now(timezone('UTC'))
    KST = datetime.now(timezone('Asia/Seoul'))
    return KST

def get_yesterday(day=1):
    import datetime
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(day)
    return yesterday.strftime('%Y-%m-%d')



def get_someday_datetime(y, m, d):
    import datetime
    return datetime.datetime(y, m, d)

def get_tomorrowday(today, day=1):
    import datetime
    today = today + datetime.timedelta(day)
    return today.strftime('%Y-%m-%d')

def get_today_yesterday(today, day=1):
    import datetime
    today = today - datetime.timedelta(day)
    return today.strftime('%Y-%m-%d')

def get_someday(y, m, d):
    import datetime
    somday = datetime.datetime(y, m, d)
    return somday.strftime('%Y-%m-%d')

def normalize(s):
    if s == None:
        return 0
    elif s != None:
        return s.replace(',', '').strip()

def roundNum(num, n2):
    # print(round(num, n2))
    return round(num, n2)

def get_datetime_tiemzone(yy, mm, dd, hh, min, ss):
    import datetime
    return datetime.datetime(yy, mm, dd, hh, min, ss, tzinfo=timezone('Asia/Seoul') )

# from
def get_today_time():
    today = getDateToday()
    today_time = today + 'T' + '00:01'
    return today_time

# to
def get_today_before_one_hour():
    today = getDateToday()
    before_one_hour = get_minus_one_hour()
    today_before_one_hour = today + 'T' + before_one_hour
    return today_before_one_hour


def get_time_hour():
    from datetime import datetime, timedelta
    d = datetime.today()
    return d.strftime('%H:%M')

def get_minus_one_hour():
    from datetime import datetime, timedelta
    d = datetime.today() - timedelta(hours=1)
    return d.strftime('%H:%M')

def get_date_list(day, num):
    date_list = []
    day_split = day.split('-')
    print(day_split)
    today = get_someday_datetime(int(day_split[0]), int(day_split[1]), int(day_split[2]))
    # print(today)
    for day_num in range(0, num):
        today_m = get_tomorrowday(today, day_num)
        # print(day_num, today_m)
        date_list.append(today_m)
    return date_list

def get_before_date_list(day, num):
    date_list = []
    day_split = day.split('-')
    print(day_split)
    today = get_someday_datetime(int(day_split[0]), int(day_split[1]), int(day_split[2]))
    # print(today)
    for day_num in range(0, num):
        today_m = get_today_yesterday(today, day_num)
        # print(day_num, today_m)
        date_list.append(today_m)
    return date_list

# naver date
def dateutil_parser_date(date):
    from dateutil.parser import parse
    return parse(date)

def dateutil_parser_today(date):
    from dateutil.parser import parse
    return parse(date).date()

#########################
# 시간 비교
#########################
def today_in_date(in_date):
    is_old = False
    import datetime
    indate = in_date.split('-')
    indate = datetime.datetime(int(indate[0]), int(indate[1]), int(indate[2]))
    # print('indate: ', indate)

    today = kst_time()
    # date = today + datetime.timedelta(7)
    # print('date: ', date)
    td = today.day - indate.day
    # print(type(td))
    if td >= 25:
        is_old = True
    return is_old

###########################
# 소수점 올림
###########################
def get_result_count(total, num):
    remain = total / num
    return math.trunc(remain), total%num

def get_trunc_all_one(total, num):
    remain = total / num
    return math.trunc(remain), total%num

def getResultCount(total):
    return math.trunc(total/10000)

#########################
# parsor
#########################
# 검색어를 URL에 사용할 수 있는 쿼리로 변환
def keyword_split(keyword):
    query = ''
    if ' ' in keyword:
        query_split = keyword.split(' ')
        for i, split in enumerate(query_split):
            if i != 0:
                query += '+'
            query += split
    else:
        query = keyword
    return query

# GET : URL
def getDetailProdUrl(dat):
    detailurl = None
    if dat is not None:
        hreftmp = dat.find('a')
        detailurl = hreftmp.get('href')
    return detailurl

def get_href_Url(dat):
    detailurl = None
    if dat is not None:
        # hreftmp = dat.find('a')
        detailurl = dat.get('href')
    return detailurl

def getImageUrl(dat):
    detailurl = None
    if dat is not None:
        hreftmp = dat.find('img')
        detailurl = hreftmp.get('src')
    return detailurl

def parsorPrice(dat):
    if dat is not None:
        dat = dat.replace(',', '')
        dat = dat.replace('원', '')
    return int(dat)


# ignore
def ignore1_name(name):
    new_name = ''
    name_split = name.split()
    for it in name_split:
        it = it.strip()

        # 한글자 제외
        if it not in Info.ignore1:
            new_name = new_name + ' ' + it
    return new_name




# 정규화 적용
def re_int_unit_blank(name):
    name_re = re.sub(Info.newregex, ' ', name)
    name_re = re.sub(Info.newregex2, ' ', name_re)
    name_re = re.sub(Info.newregex3, ' ', name_re)
    return name_re

def re_int_unit_newregex2_a_0(name):
    name_re = re.sub(Info.newregex2, ' ', name)
    return name_re

def re_int_unit_newregex2_a_0_blank(name):
    name_re = re.sub(Info.newregex2, '', name)
    return name_re

def re_int_unit_newregex4(name):
    name_re = re.sub(Info.newregex4, ' ', name)
    return name_re

# 한글제외
def re_int_unit_newregex5(name):
    name_re = re.sub(Info.newregex5, ' ', name)
    return name_re

def re_int_unit_newregex6(name):
    name_re = re.sub(Info.newregex6, ' ', name)
    return name_re

def re_int_unit_newregex6_none(name):
    name_re = re.sub(Info.newregex6, '', name)
    return name_re

# 영어제거, 공백제거
def reform_title(title):
    title = title.strip()
    # 영어 제거
    title = re_int_unit_newregex6_none(title)
    title = title.replace(' ', '')
    return title

# ignore
def ignore_name(name):
    new_name = ''
    name_split = name.split()
    for it in name_split:
        it = it.strip()
        # print(it)

        # 한글자 제외
        if len(it) != 1:
            if (it not in Info.ignore2) and (it not in Info.ignore3) and (it not in Info.ignore4) and (it not in Info.ignore5):
                # print(it)
                new_name = new_name + ' ' + it
    return new_name

# 특수문자
prod_special = r"[=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]"
def except_special_character(name):
    name_re = re.sub(prod_special, '', name)
    return name_re

# 특수문자
file_special = r"[=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\<\>`\'…》\n\r\t]"
def except_file_character(name):
    name_re = re.sub(file_special, '', name)
    return name_re

def except_file_character_space(name):
    name_re = re.sub(file_special, ' ', name)
    return name_re

# 조합
def combines(dat):
    # dat = ['냉동', '채식', '두개장', '오신채']
    if len(dat) > 3:
        dat_len = 3
    else:
        dat_len = len(dat)
    # print('data_len : ', dat_len)

    # 조합
    tot_list = []
    for it in range(dat_len):
        for i in combinations(dat, it+1):
            i = set(i)
            # print(it, i)
            tot_list.append(i)
    # print(tot_list)

    # str
    tot_str_list=[]
    for tot in tot_list:
        tmp_str = ''
        for it in tot:
            tmp_str = tmp_str + it + ' '
        tot_str_list.append(tmp_str.strip())
    # print(tot_list_str)

    # 중복제거
    tot_str_list = list_to_set_to_list(tot_str_list)
    return tot_str_list

# 숫자만
def only_int(dat):
    # string = 'aaa1234, ^&*2233pp'
    res = re.sub(r'[^0-9]', '', dat)
    return res

def except_int(dat):
    # string = 'aaa1234, ^&*2233pp'
    res = re.sub(r'[0-9]', '', dat)
    return res

# # except brand kr
# def except_brand_kr_list(key_list):
#     new_split_keyword = []
#     for it in key_list:
#         iskey = except_brand_kr(it)
#         if iskey == False:
#             new_split_keyword.append(it)
#     return new_split_keyword
#
# def except_brand_kr(keyword):
#     iskey = False
#     for brand_list in br.brand_kr:
#         for brand in brand_list:
#             if brand in keyword:
#                 print('# 제외 브랜드명 : ', brand, keyword)
#                 iskey = True
#                 return iskey
#     return iskey

# brand_kr 는 동일한 것만 제외한다.
# 브랜드와 동일한 것
def except_equal_brand_kr_list(key_list):
    new_split_keyword = []
    for it in key_list:
        iskey = except_equal_brand_kr(it)
        if iskey == False:
            new_split_keyword.append(it)
    return new_split_keyword

def except_equal_brand_kr(keyword):
    iskey = False
    for brand_list in br.brand_kr:
        for brand in brand_list:
            if brand == keyword:
                print('# 제외 브랜드명 : ', brand, keyword)
                iskey = True
                return iskey
    return iskey

def except_brand_en(keyword):
    iskey = False
    for brand_list in br.brand_en:
        for brand in brand_list:
            if brand in keyword:
                # print(brand, keyword)
                iskey = True
                return iskey
    return iskey

# except word
def except_word_list(key_list):
    new_split_keyword = []
    for it in key_list:
        iskey = except_word(it)
        if iskey == False:
            new_split_keyword.append(it)
    return new_split_keyword

def except_word(keyword):
    iskey = False
    for brand in no_except_word_list:
        if brand in keyword:
            # print('brand : ', brand)
            # print('keyword : ', keyword)
            iskey = True
            return iskey
    return iskey

# def info_except_word():
#     print(no_except_word_list)
#     for brand in no_except_word_list:
#         print(brand)

def is_except_word(key):
    is_key = False
    if key in no_except_word_list:
        is_key = True
    return is_key

def cut_list(cut_num, tmp_key):
    all_list = []
    for num, it in enumerate(tmp_key):
        all_list.append(it)
        if num > cut_num:
            break
    return all_list

def get_brand_list_only_two_word():
    tmp_list = []
    for brand_list in br.brand_kr:
        for brand in brand_list:
            if len(brand) == 2:
                tmp_list.append(brand)
    return tmp_list

def get_brand_list_all():
    tmp_list = []
    for brand_list in br.brand_kr:
        for brand in brand_list:
            tmp_list.append(brand)
    return tmp_list
#################
# json
#################
def json_pretty(parsed):
    return json.dumps(parsed, indent=4, sort_keys=True, ensure_ascii=False)

#################
# List, Dict
#################
def print_list(listdat):
    if listdat !=[]:
        for it in listdat:
            print(it)

def list_to_str(listdat):
    strdat = ''
    for it in listdat:
        strdat += it + ' '
    return strdat

def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))

def list_to_str_comma(s):
    res_str = ', '.join(s)
    return res_str

def dict_to_str(dictdat):
    tmpstr = ''
    for key, value in dictdat.items():
        for it in value:
            tmpstr = tmpstr + it + '|' + key + '\n'
    return tmpstr

def keyword_dic_to_str(dicdat):
    tmp_str = ''
    list_str = ''
    for key, value in dicdat.items():
        if key == 'rel_keywords':
            for it in value:
                list_str += it + '|'
            tmp_str += key + '|' + list_str + '\n'
        else:
            tmp_str += key + '|' + str(value) + '\n'
    return tmp_str

def dict_to_rel_keyword_list(rel_dict):
    data_all_list = []
    for key, value in rel_dict.items():
        for it in value:
            data_all_list.append(it)
    return data_all_list

# 중복제거
def list_to_set_to_list(data_list):
    tmp_list = []
    if data_list != []:
        tmp_set = set(data_list)
        tmp_list = list(tmp_set)
    return tmp_list

# list 값 중 '' 제거
def except_list_empty(data_list):
    new_list = []
    if data_list != []:
        for it in data_list:
            if it.strip() != '':
                new_list.append(it)
    return new_list

# list에 특정 단어 있는 경우 추출 - list
def add_list_word(data_list, word):
    new_list = []
    if data_list != []:
        for it in data_list:
            chid = it.strip()
            if len(chid) == 9 and chid not in 'CHA':
                if chid.startswith(word):
                    new_list.append(it)
    return new_list

# list에 특정 단어 있는 경우 추출 - list
def except_list_word(data_list, word):
    new_list = []
    if data_list != []:
        for it in data_list:
            if word not in it.strip() :
                new_list.append(it)
    return new_list

def except_list_to_str_word(data_list, word):
    new_list = []
    if data_list != []:
        for it in data_list:
            val = str(it)
            if word not in val.strip():
                new_list.append(it)
    return new_list

def print_list_len(tmp):
    len = 0
    if tmp != []:
        len = len(tmp)

        return len
    return len


# dict의 키와 유사한 값으로 values를 꺼낸다.
def get_dict_val_from_like_key(tmp_dict, like_key):
    # print(like_key)
    # print(tmp_dict.keys())
    val = None
    for num, key in enumerate(tmp_dict.keys()):
        # print(num, key)
        if like_key in key:
            val = tmp_dict.get(key)
            # print(val)
    return val

# dict의 키와 유사한 값으로 values를 꺼낸다.
def get_delivery_dict_val_from_like_key(tmp_dict, like_key):
    val = None
    for num, key in enumerate(tmp_dict.keys()):

        print(num, key)
        if like_key == key:
            val = tmp_dict.get(key)
            print(val)
            break
        # elif like_key in key:
        #     val = tmp_dict.get(key)
        #     print(val)
        #     break
        # else:
        #     val = 'EPOST'
        # print(val)
    return val

############################
# print
############################
def print_result(gbn, tmp_list):
    if tmp_list == []:
        print('#######', gbn, ' 연관키워드 없음', '\n')
    else:
        print('#######', gbn, '연관키워드 : ', len(tmp_list), '\n')

def print_val_name(tmp):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    name = [var_name for var_name, var_val in callers_local_vars if var_val is tmp]

    if type(tmp) == type([]):
        print(name, len(tmp), tmp)
    elif type(tmp) == type('str'):
        print(name, tmp)
    elif type(tmp) == type('int'):
        print(name, tmp)
    else:
        print(name, tmp)

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

# 오픈마켓 count
def print_item_count(item_count):
    if item_count == -1:
        print('item count: 0')
    else:
        print('item count: ', item_count)


############################
# es
############################
def is_res_data(res):
    is_key = False
    if res != []:
        result = res['hits']['hits']
        # print(len(result))
        if len(result) > 0:
            is_key = True
    return is_key

def is_res_data_len(list):
    if len(list) != 0:
        return 1
    else:
        return 0

# parser  : today rename
def get_es_id_list(res):
    delete_list = []
    hits = res['hits']['hits']
    for it in hits:
        delete_list.append(it['_id'])
    return delete_list


#######################
# string
#######################
def word_count(word, tmp):
    total = 0
    tmp_split = tmp.split()

    for it in tmp_split:
        if word in it:
            # print(it)
            total += 1
    return total

def up_price(price):
    price_len = len(str(price))
    if price_len > 3:
        new_price = round(price, -2)
    elif price_len == 3:
        new_price = round(price, -1)
    elif price_len == 2 or price_len == 3:
        new_price = round(price, -1)
    else:
        new_price = price
    return new_price

#######################
# cookie
#######################
def get_cookie_value(self):
    cookie = None
    # session value
    for c in self.sess.cookies:
        cookie = c.name +'='+ c.value
    return cookie

#####################
# onch
#####################
# https://www.onch3.co.kr/onch_view.html?num=9567185&stxt=CH1843956
# https://www.onch3.co.kr/onch_view.html?num=9565494&stxt=CH1840600

def check_durl(url, chid):
    onch_url = 'https://www.onch3.co.kr/'
    if '&stxt' not in url:
        url_split = url.split('/')
        all_url = onch_url + url_split[1] + '&stxt=' + chid

    elif 'onch3' not in url:
        url_split = url.split('/')
        all_url = onch_url + url_split[1]
    else:
        all_url = url
    return all_url

def new_check_durl(url, chid):
    onch_url = 'https://www.onch3.co.kr/onch_view.html?num={}&stxt={}'
    # onch_url = 'https://www.onch3.co.kr/dbcenter_renewal/'

    all_url = ''
    if '=' in url:
        url_split = url.split('=')
        all_url = onch_url.format(url_split[1], chid)
    return all_url

def check_add_stxt_durl(durl, chid):
    if 'http' in durl:
        durl = durl.replace('http', 'https')
    return durl

    # if '&stxt' not in durl:
    #     url = durl + '&stxt=' + chid
    #     return url
    # else:
    #     return durl

def get_address_info():
    number = Info.companyContactNumber
    zip_code = Info.returnZipCode
    re_addr = Info.returnAddress
    addr_detail = Info.returnAddressDetail
    return number, zip_code, re_addr, addr_detail

def get_brand_info(cp_no):
    phone_val = None
    if cp_no == '2':
        phone_val = '하이트렌드'
    elif cp_no == '1':
        phone_val = '하늘고래'
    return phone_val

def get_phone_info(cp_no):
    phone_val = None
    if cp_no == '2':
        phone_val = '하이트렌드 010-4046-5194'
    elif cp_no == '1':
        phone_val = '하늘고래 010-4046-5194'
    return phone_val

if __name__ == '__main__':

    test = 'test'
    if test == 'test':

        # ./dbcenter_view.html?num=9584634 codenum:CH1880705
        old_url = '../onch_view.html?num=9584332'
        url = './dbcenter_view.html?num=9584634'
        chid = 'CH1880705'
        url_s = check_durl(old_url, chid)
        print(url_s)
        url_d = check_add_stxt_durl(old_url, chid)
        print(url_d)

        #
        # from_day = '2022-05-17'
        # num = 38
        # day_list = get_date_list(from_day, num)
        # for today in day_list:
        #     print(today)






        # from dateutil.parser import parse
        #
        # print(parse("Apr 16, 2016 04:05:32 PM"))
        # print(parse("Tue, 10 May 2022 15:26:39 +0900"))
        # # datetime
        # mail_date = parse("Tue, 10 May 2022 15:26:39 +0900")
        # print(mail_date.date())



        # print(get_vendorId('1'))
        # chid = 'CH1811536'
        # durl = 'http://www.onch3.co.kr/onch_view.html?num=9550249'
        # url = check_add_stxt_durl(durl, chid)
        # print(url)

        # get_cp_id_info(1)
        # get_onch_id_info(1)

        # cn = getResultCount(10)
        # print(cn)
        # code = '일양로지스'
        # print(get_ship_code(code))


        # fromday = get_yesterday(1)
        # print(fromday)
        # fromday = get_today_time()
        # print(fromday)
        #
        # today = get_today_before_one_hour()
        # print(today)

        # day = 40
        # for it in range(54, 1, -1):
        #     print(get_yesterday(it))

        # t_list = get_brand_list()
        # print(t_list)

        # word = '듀퐁'
        # print(except_brand_kr(word))

        # today = '2021-12-21'
        # today_time = get_today_timeTime(today)
        # print(today_time)
        #
        # to_day = get_today_from_month(today)
        # print(to_day)
        #
        # price = 2700
        # price = up_price(price)
        # print(price)

        # day = 17
        # for it in range(day):
        #     it_day = it+1
        #     today = get_yesterday(it_day)
        #     print(today)



        # print(get_now_cp_time())
        #
        # pr = 350
        # pr = 1516
        # pre = up_price(pr)
        # print('pre :', pre)
        #
        # tmp = '추가 설치 총'
        # tmp1 = ignore1_name(tmp)
        # print(tmp1)
        # print(getNowDayTime())
        #
        # list_to_str()
        # key = 'HOKA ONE ONEon'
        # iskey = except_brand_en(key)
        # print(iskey)
        #
        # keyword = ['데일리운동화']
        # tmp_list = except_word_list(keyword)
        # print(tmp_list)

        # someday = get_someday(2021, 10, 18)
        # print(someday)

        # print(get_yesterday())
        # print(kst_time())
        # print(getDateMonth())

        # ignore1 = ('총', '각', '맛', '택', '약', '로', '년', '월', '시', '구', '홀', '씩', '소', '중')
        # for it in ignore1:
        #     print(it, len(it))

        # dicttmp = "{'네이버연관': ['삼양비건라면', '칼로리낮은라면', '다이어트라면', '다이어트라면', '건면'], '네이버쇼핑': ['맛있는라면', '들깨가루1kg', '배안아픈우유', '치즈선물세트', '소고기볶음고추장', '맛있는떡집', '우유1l', '락토프리우유', '납작당면', '식사대용떡', '붕어빵반죽', 'mre', '우유', '바람떡', '시리얼', '서울우유멸균우유', '생면', '소화가잘되는우유', '콘후레이크', '캠핑키트', '발열전투식량', '라면티백', '카놀라유900', '신앙촌간장선물세트', '무설탕딸기잼', '현미시리얼', '슈크림붕어빵', '콘푸라이트', '떡시루', '말돈소금'], '쿠팡': ['비건 라면 풀무원', '비건', '비건 빵', '비건 식품', '비건 콩고기', '라면', '비건 만두', '채식 라면', '비건 마요네즈', '건면']}"
        # dicttmp = eval(dicttmp)
        # dicttmp = dict(dicttmp)
        #
        # print(dicttmp.items())
        #
        #
        #
        # list = dict_to_rel_keyword_list(dicttmp)
        # print(list)

        # dat = ['비건아이스크림', '스웨디시', '글레이스', '아이스크림', '쵸코렛맛']
        # str = combines(dat)
        # print(str)
        #
        # dat1 = ('냉동', '채식', '냉동')
        # print(dat1)

        # dict = {'주문후 예상 배송기간 일반': '2500', '제주도': '3000', '도서산간': '3000'}
        # dict = {'상품정보제공고시 구분': '구두/신발', '제품소재': 'pu소가죽,pvc', 'KC 인증 필 유무': '인증 상품 아님', '색상': '머스타드,와인,올리브,인디핑크,브라운,차콜,네이비',
        #  '치수': '38호,40호,42호,44호', '제조자/수입자': '제이앤제이', '제조국': '중국(oem)', '취급시 주의사항': '소비자 부주의 요함',
        #  '품질보증기준': '공증거래위헌회에 따름', 'A/S 책임자와 전화번호': '상품등록시 개별 판매자 연락처 표기', '주문후 예상 배송기간': '2일'}
        #
        # key = '배송기간'
        # val = get_dict_val_from_like_key(dict, key)
        # print(val)