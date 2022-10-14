from chaesiknara import Chaesiknara
from Crawling.mall.lib.es_pordlist import DataMallProdlistES

if __name__ == '__main__':

    #######################
    # test = 'create_file'
    test = 'insert'
    # test = 'search_name'

    #######################
    code_mall = 'M0000002'
    # sta = '정상판매'
    sta = '품절'


    # class
    mall = Chaesiknara()

    #######################
    if test == 'create_file':
        mall.get_prodlist()

    # insert
    if test == 'insert':
        filename = 'CHAES_062_20220913.html'
        mall.parsor_one_file(filename)

    if test == 'search_name':
        malles = DataMallProdlistES()
        mall_code_res = malles.search_mall_code(code_mall, sta)
        print('mall_code : ', mall_code_res)
        all_data = malles.result_all_data(mall_code_res)

        for it in all_data:
            print(it.get_data_dict())
        print('len : ', len(all_data))

    #######################
    # sess close
    mall.close_session()