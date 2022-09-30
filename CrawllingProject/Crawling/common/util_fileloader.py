# -*- coding: utf-8 -*-

import xlrd
import common.util_common as cu
import pandas as pd
import platform
import codecs
import os
import time
import glob
# import data.onch_info as Info

################
# Directory
################
# gubun path
GUBUN = 'onch'
GUBUN_NEW = 'onch_new'

# path
PATH_PROD = 'prod'
PATH_PRODLIST = 'prodlist'
PATH_URL = 'URL'
PATH_DETAIL = 'detail'
PATH_FILEINFO = 'fileinfo'
PATH_IMG = 'prod_detail_image'
PATH_DETAIL_IMG = 'prod_detail_image'


PATH_PROD_EXCEL = 'prod_excel'
PATH_PROD_HTML = 'prod_html'
PATH_PROD_DETAIL = 'prod_detail'
PATH_RESEARCH = 'prod_research'
PATH_PROD_CHID = 'prod_chid'
PATH_OPEN_MAR = 'prod_open'
PATH_SODLOUT = 'soldout'
PATH_WINNER = 'winner'

# 확장자
EFILE_TXT = '.txt'
EFILE_HTML = '.html'
EFILE_EXCEL = '.xls'
EFILE_JPG = '.jpg'

#sheet
SHEET_NAME = 'onchExcel'
SHEET_KEY = 'keyword'

ONCH_URL = 'https://image.onch3.co.kr/'

# config = OnchConfig()
# IS_HOME = config.is_home()
# IS_HOME = Info.homeip

def createFolder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print('commonutil - createFolder')
        # print(ex.__class__)

def getDirectoryFileList(path):
    try:
        flist = os.listdir(path)
        return flist
    except :
        print('commonutil - getDirectoryFileList')
        # print(ex.__class__)

# EXIST FILE
def is_in_file(fnam):
    # return os.path.isdetail("/home/ubuntu/test_a.txt")
    # return os.path.isdetail(fnam)
    return os.path.isfile(fnam)

# EXIST Directory
def isDirectory(pth):
    return os.path.exists(pth)

# 최신 파일 가져오기
def get_latest_file(fpath, file_type):
    latest_file = None
    files = glob.glob(fpath + file_type)
    if files != []:
        latest_file = max(files, key=os.path.getctime)
    return latest_file

# delete - file
def delete_file(myfile):
    if os.path.isfile(myfile):
        os.remove(myfile)
        print('delete file')
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)

def delete_onch_excel_download():
    path_down = getDownloadPath()
    excel_file_name = 'ej4012.xls'
    is_key = is_in_file(path_down + excel_file_name)
    if is_key == True:
        delete_file(path_down + excel_file_name)

################
# file path
################
def windowDataPath(path=None):
    if path is None:
        winPath = 'd://data/'
    else:
        winPath = 'd://data/' + path + '/'
    createFolder(winPath)
    return winPath

def getDataPath(path):
    plat = platform.system()
    if plat == 'Windows':
        filePath = 'd://data/' + path + '/'
        createFolder(filePath)
    else:
        filePath = '/Users/SON/data/' + path + '/'
    return filePath


def getDownloadPath():
    filePath = 'c://Users/nurier/Downloads/'
    # plat = platform.system()
    # filePath = ''
    # if IS_HOME == 'HOME':
    #     filePath = get_home_download_path()
    # else:
    #     if plat == 'Windows':
    #         filePath = 'c://Users/nurier/Downloads/'
    #         createFolder(filePath)
    #     else:
    #         filePath = '/Users/SON/Downloads/'
    return filePath

def get_home_download_path():
    plat = platform.system()
    filePath = ''
    if plat == 'Windows':
        # filePath = 'C://Users/song/Downloads/'
        filePath = 'C://Users/nurier/Downloads/'
        createFolder(filePath)
    return filePath

def getFilePath(gubun, path):
    plat = platform.system()
    if plat == 'Windows':
        filePath = getDataPath(gubun) + path + '/'
        createFolder(filePath)
    else:
        filePath = getDataPath(gubun) + path + '/'
        # filePath = '/Users/SON/Dropbox/HitHit/jabsc/data/list/'
    return filePath

def get_file_path_code_mall(gubun, path):
    return gubun + path

def getFileName(gubun, path, fnam, efile):
    # file path/ name
    fpath = getFilePath(gubun, path)
    fpathnam = fpath + fnam + efile
    return fpathnam

def getTodayFileName(gubun, path, fnam, date, efile):
    # file path/ name
    fpath = getFilePath(gubun, path)

    # today
    if date == '':
        today = cu.getDateTodayNoDash()
    else:
        today = date
    fpathnam = fpath + fnam + '_' + today + efile
    return fpathnam

################
# create file
################
'''
gubun = 'onch'
path = 'production'
fname = 'ej4012'
efile = 'xls'
'''
def createOpenFile(gubun, path, fnam, efile):
    f = None
    try:
        fName = getFileName(gubun, path, fnam, efile)

        f = codecs.open(fName, 'w', 'utf-8')
        return f
    except Exception as ex:
        print(ex.__cause__); print(ex.__class__); print(ex.__context__)
        print('fileloader - createOpenFile :', ex)
        return f

def  createTodayOpenFile(resp, gubun, path, fnam, efile, decode = None):
    try:
        date = ''
        fName = getTodayFileName(gubun, path, fnam, date, efile)

        fopen = codecs.open(fName, 'w', decode)
        # fopen = codecs.open(fName, 'w', 'euc-kr')
        fopen.write(resp)
        fopen.close()
        # return fopen
    except Exception as ex:
        print(ex.__cause__); print(ex.__class__); print(ex.__context__)
        print('fileloader - createTodayOpenFile :', ex)
        # return fopen

def  createTodayOpenFile_utf8(resp, gubun, path, fnam, efile, decode = None):
    try:
        date = ''
        fName = getTodayFileName(gubun, path, fnam, date, efile)

        fopen = codecs.open(fName, 'w', 'utf-8')
        # fopen = codecs.open(fName, 'w')
        fopen.write(resp)
        fopen.close()

    except Exception as ex:
        print(ex.__cause__); print(ex.__class__); print(ex.__context__)
        print('fileloader - createTodayOpenFile :', ex)
        # return fopen

def  createTodayOpenFile_nonecode(resp, gubun, path, fnam, efile, decode = None):
    try:
        date = ''
        fName = getTodayFileName(gubun, path, fnam, date, efile)

        # fopen = codecs.open(fName, 'w', 'utf-8')
        fopen = codecs.open(fName, 'w')
        fopen.write(resp)
        fopen.close()

    except Exception as ex:
        print(ex.__cause__); print(ex.__class__); print(ex.__context__)
        print('fileloader - createTodayOpenFile :', ex)
        # return fopen

def createRespOpenFile(resp, gubun, path, fnam, efile):
    fName = getFileName(gubun, path, fnam, efile)
    print('fName : ', fName)

    fopen = codecs.open(fName, 'w', 'utf-8')
    # fopen = codecs.open(fName, 'w')
    # fopen = codecs.open(fName, 'w', "ms949")
    # fopen = codecs.open(fName, 'w', "euc-kr")
    # fopen = codecs.open(fName, 'w', 'cp949')

    fopen.write(resp)
    fopen.close()

def create_resp_nodecode(resp, gubun, path, fnam, efile):
    fName = getFileName(gubun, path, fnam, efile)
    print('fName : ', fName)

    # fopen = codecs.open(fName, 'w', 'utf-8')
    # fopen = codecs.open(fName, 'w')
    fopen = codecs.open(fName, 'w', "ms949")
    # fopen = codecs.open(fName, 'w', "euc-kr")
    # fopen = codecs.open(fName, 'w', 'cp949')

    fopen.write(resp)
    fopen.close()

################
# read file
################

'''
gubun = 'onch'
path = 'production'
fname = 'ej4012'
efile = '.xls'
'''
def readTodayFile(gubun, path, fnam, date, efile):
    data = None
    try:
        fName = getTodayFileName(gubun, path, fnam, date, efile)
        print('readTodayFile : ', fName)

        with codecs.open(fName, 'r', 'utf-8') as file:
        # with codecs.open(fName, 'r') as file:
            data = file.read()
        return data
    except Exception as ex:
        print(ex.__cause__);print(ex.__class__);print(ex.__context__)
        print('fileloader readHtmlFile :', ex)
        return data

def readTodayFile_nonecode(gubun, path, fnam, date, efile):
    data = None
    try:
        fName = getTodayFileName(gubun, path, fnam, date, efile)
        print('readTodayFile : ', fName)

        # with codecs.open(fName, 'r', 'utf-8') as file:
        with codecs.open(fName, 'r') as file:
            data = file.read()
        return data
    except Exception as ex:
        print(ex.__cause__);print(ex.__class__);print(ex.__context__)
        print('fileloader readHtmlFile :', ex)
        return data

def readFileData(gubun, path, fnam, efile):
    data = None
    try:
        fName = getFileName(gubun, path, fnam, efile)
        print('readTodayFile : ', fName)

        with codecs.open(fName, 'r', 'utf-8') as file:
        # with codecs.open(fName, 'r') as file:
            data = file.read()
        return data
    except Exception as ex:
        print(ex.__cause__);print(ex.__class__);print(ex.__context__)
        print('fileloader readHtmlFile :', ex)
        return data

def readFileName(path, fnam):
    data = None
    # try:
    fileName = path+fnam
    # print('readFileName : ',fileName)

    with codecs.open(fileName, 'r') as file:
    # with codecs.open(fileName, 'r', "utf-8") as file:
    # with codecs.open(fileName, 'r', "ms949") as file:
    # with codecs.open(fileName, 'r', "euc-kr") as file:
    # with codecs.open(fileName, 'r', 'cp949') as file:
        data = file.read()
    return data
    # except Exception as ex:
    #     print(ex.__cause__);print(ex.__class__);print(ex.__context__)
    #     print('fileloader readFileName :', ex)
    #     return data

def read_fila_name(file_name):
    data = None
    with codecs.open(file_name, 'r', "utf-8") as file:
        data = file.read()
    return data


def readTXTFile(path, fnam):
    data = None
    try:
        fileName = path+fnam
        # print(fileName)
        with codecs.open(fileName, 'r', 'utf-8') as file:
            data = file.readlines()
        return data
    except Exception as ex:
        print(ex.__cause__);print(ex.__class__);print(ex.__context__)
        print('fileloader readFileName :', ex)
        return data

def readTXTFile_nodecod(path, fnam):
    data = None
    try:
        fileName = path+fnam
        # print(fileName)
        with codecs.open(fileName, 'r') as file:
            data = file.readlines()
        return data
    except Exception as ex:
        print(ex.__cause__);print(ex.__class__);print(ex.__context__)
        print('fileloader readFileName :', ex)
        return data

def readExcelDf(gubun, path, fnam, efile, sheetName, usecols=None):
    data = None
    # try:
    fName = getFileName(gubun, path, fnam, efile)
    print('readExcelDf :', fName)

    data = pd.read_excel(fName, sheetName, header=None, usecols=usecols)
    return data
    # except Exception as ex:
    #     print(ex.__cause__);print(ex.__class__);print(ex.__context__)
    #     print('fileloader readExcelDf :', ex)
    #     return data

def read_excel_df(file_name, sheet_name, usecols=None):
    print('readExcelDf :', file_name)

    data = pd.read_excel(file_name, sheet_name, header=None, usecols=usecols)
    return data

def readFileNameExcelDF(fnam, sheetNam):
    workbook = xlrd.open_workbook(fnam, ignore_workbook_corruption=True)
    data = pd.read_excel(workbook)
    # data = pd.read_excel(fnam, sheetNam)
    return data

###############
# GET File All
###############
# GET function
def getDirAllFileList(gubun, path):
    # GET : ID, URL 파일 저장 경로
    fpath = getFilePath(gubun, path)
    # print('fpath : ', fpath)

    # GET : ID, URL 전체 파일명
    fileList = getDirectoryFileList(fpath)
    return fpath, fileList


# GET : prodlist - html
def getProdHtmlAllFile():
    # gubun = 'onch'
    # path_prodlist = 'prodlist'
    fpath, flist = getDirAllFileList(GUBUN, PATH_PRODLIST)
    return fpath, flist

# GET : prod excel - excel
def getProdExcelAllFile():
    # gubun = 'onch'
    # path_prod = 'prod'
    fpath, flist = getDirAllFileList(GUBUN, PATH_PROD)
    return fpath, flist

# GET : URL - txt file
def getURLTxtAllFile():
    # gubun = 'onch'
    # path_url = 'URL'
    fpath, flist = getDirAllFileList(GUBUN, PATH_URL)
    return fpath, flist

# GET : Detail - html
def getProdDetailAllFile():
    fpath, flist = getDirAllFileList(GUBUN, PATH_DETAIL)
    return fpath, flist

# GET : prod chid
def get_all_file_prod_chid(code_mall):
    fpath, flist = getDirAllFileList(get_path_onch_new_chid(), code_mall)
    return fpath, flist

# GET : open market
def get_all_file_open_mar(code_mall):
    fpath, flist = getDirAllFileList(get_path_onch_new_open(), code_mall)
    return fpath, flist

##############################################
# CREATE : URL - txt 파일 생성
def createUrlFile(fnam):
    # gubun = 'onch'
    # path_url = 'URL'
    # # fnam = 'DetailProductURL'
    # efile = '.txt'

    f = createOpenFile(GUBUN, PATH_URL, fnam, EFILE_TXT)
    return f

# CREATE : fileinfo - txt 파일 생성
def createFileInfoTxtFile(fnam):
    # gubun = 'onch'
    # path_fileinfo = 'fileinfo'
    # efile = '.txt'
    f = createOpenFile(GUBUN, PATH_FILEINFO, fnam, EFILE_TXT)
    return f

################
# Onch File Path
################
def getPathProdExcel():
    return getFilePath(GUBUN, PATH_PROD)

def getPathProdlistHtml():
    return getFilePath(GUBUN, PATH_PRODLIST)

def getPathURL():
    return getFilePath(GUBUN, PATH_URL)

def getPathDetail():
    return getFilePath(GUBUN, PATH_DETAIL)

############### new ###############
def get_path_onch_new_image():
    return GUBUN_NEW + '/' + PATH_IMG

def get_full_path_onch_new_image():
    return getFilePath(GUBUN_NEW, PATH_IMG)

def get_path_onch_new_excel():
    return GUBUN_NEW + '/' + PATH_PROD_EXCEL

def get_full_path_onch_new_excel():
    return getFilePath(GUBUN_NEW, PATH_PROD_EXCEL)

def get_path_onch_new_html():
    return GUBUN_NEW +'/'+ PATH_PROD_HTML

def get_full_path_onch_new_html():
    return getFilePath(GUBUN_NEW, PATH_PROD_HTML)

def get_path_onch_new_detail():
    return GUBUN_NEW + '/' + PATH_PROD_DETAIL

def get_full_path_onch_new_detail():
    return getFilePath(GUBUN_NEW, PATH_PROD_DETAIL)

# research
def get_path_onch_new_research():
    return GUBUN_NEW + '/' + PATH_RESEARCH

def get_full_path_onch_new_research():
    return getFilePath(GUBUN_NEW, PATH_RESEARCH)

# chid
def get_path_onch_new_chid():
    return GUBUN_NEW + '/' + PATH_PROD_CHID

def get_full_path_onch_new_chid():
    return getFilePath(GUBUN_NEW, PATH_PROD_CHID)

# open
def get_path_onch_new_open():
    return GUBUN_NEW + '/' + PATH_OPEN_MAR

def get_full_path_onch_new_open():
    return getFilePath(GUBUN_NEW, PATH_OPEN_MAR)

# soldout
def get_path_onch_new_soldout():
    return GUBUN_NEW + '/' + PATH_SODLOUT

def get_full_path_onch_new_soldout():
    return getFilePath(GUBUN_NEW, PATH_SODLOUT)

# winner
def get_path_onch_new_winner():
    return GUBUN_NEW + '/' + PATH_WINNER

def get_full_path_onch_new_winner():
    return getFilePath(GUBUN_NEW, PATH_WINNER)

################
# Onch File Attr
################
def getFileDate(fnam):
    ctime = time.ctime(os.path.getctime(fnam))
    t_obj = time.strptime(ctime)
    t_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    return t_stamp

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

###############
# dataFrame to File
###############
def dataFrameToExcel_multi_sheet(df, filename, sheetName):
    # Create a Pandas dataframe from some data.
    df = pd.DataFrame(df)
    # print(df)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(filename+'.xlsx', engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    # df.to_excel(writer, sheet_name = sheetName, encoding='utf-8')
    df.to_excel(writer, sheet_name=sheetName)
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    # writer.close()

def dataFrameToExcel(df, filename, sheetName):
    df = pd.DataFrame(df)
    # df['timestamp'] = df['timestamp'].apply(lambda a: pd.to_datetime(a).date())
    df['timestamp'] = df['timestamp'].apply(lambda a: pd.Timestamp(a).strftime('%Y-%m-%d'))
    df.to_excel(filename+'.xlsx', sheet_name=sheetName)

def dataFrameToExcel_notimestamp(df, filename, sheetName):
    df = pd.DataFrame(df)
    nam = filename + '.xlsx'
    print(nam)
    df.to_excel(nam, sheet_name=sheetName)



'''
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

ExcelWriter를 사용하여 기존 Excel 파일에 추가할 수도 있습니다.

with pd.ExcelWriter('output.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer, sheet_name='Sheet_name_3')
'''

################################
# function
################################
def delete_download_all_file():
    filepath = getDownloadPath()
    print(filepath)
    files = glob.glob(filepath + '\*.*', recursive=True)

    for f in files:
        print(f)
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

if __name__ == '__main__':
    pass
    delete_download_all_file()
