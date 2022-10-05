# -*- coding: UTF-8 -*-

# class
from oasismall import Oasismall

if __name__ == '__main__':

    test = 'create_prod_list'
    test = 'insert_prod_list'
    test = 're_prod_name'

    ##########################
    # 오아시스몰
    code_mall = 'M0000001'
    name_mall = '오아시스몰'
    name_code_mall = 'OASIS'
    sta = "정상판매"

    # mall class
    mall = Oasismall()

    ##########################
    if test == 'create_prod_list':
        mall.get_prodlist()

    if test == 'insert_prod_list':
        mall.insert_prodlist_es()

    if test == 're_prod_name':
        # test, 여기서 중단
        pass

    #######################
    # sess close
    mall.close_sess_es()
    print('END : ', test)