# -*- coding: utf-8 -*-

import requests

class RequestHit:
    __session = None

    @staticmethod
    def getSession():
        if RequestHit.__session == None:
            RequestHit()
        return RequestHit.__session


    def __init__(self):
        # 싱글톤
        # if RequestHit.__session != None:
        #     raise Exception("This class is a singleton")
        # else:
        # RequestHit.__session = requests.session()

        # session
        self.sess = requests.session()

    def close_session(self):
        self.sess.close()

    #############################
    # Requests
    #############################
    # request Post
    def request_post(self, url, info, header):
        try:
            resp = self.sess.post(url, data=info, headers=header)
            # print('##', resp.text)
            if resp.status_code == 200:
                print(resp.status_code)
                pass
            else:
                print('ERROR : req_post')
                resp = ''
            return resp
        except ConnectionError as ex:
            print('Requestlib - req_post')
            print(ex.__cause__)
            print(ex.__class__)
            print(ex.__context__)


    def request_post_noheader(self, url, info):
        try:
            resp = self.sess.post(url, data=info)
            if resp.status_code == 200:
                pass
                # print(resp.status_code)
            else:
                print('ERROR : req_post_noheader')
                resp = ''
            return resp
        except ConnectionError as ex:
            print('Requestlib - req_post_noheader')
            print(ex.__cause__)
            print(ex.__class__)
            print(ex.__context__)

    # request Get
    def request_get(self, url, header):
        try:
            # print('####')
            resp = self.sess.get(url, headers=header)
            # print('req : ', resp.text)
            if resp.status_code == 200:
                pass
                # print(resp.status_code)
            else:
                print('ERROR : req_get')
                resp = ''
            return resp
        except ConnectionError as ex:
            print('Requestlib - req_get')
            print(ex.__cause__)
            print(ex.__class__)
            print(ex.__context__)


    #####################################
    # request Get
    def request_get_noheader(self, url):
        resp = None
        try:
            resp = self.sess.get(url, timeout=30)
            if resp.status_code == 200:
                pass
                print(resp.status_code)
            else:
                print('ERROR : req_get_noheader')
                resp = ''
            return resp
        except ConnectionError as ex:
            print('Requestlib - req_get_noheader')
            print(ex.__cause__)
            print(ex.__class__)
            print(ex.__context__)
            return resp

    # request OPTIONS
    def request_option(self, url, header):
        try:
            resp = self.sess.options(url, headers=header, timeout=30)
            if resp.status_code == 204:
                pass
                # print(resp.status_code)
            else:
                print('ERROR: request_option')
                resp = ''
            return resp
        except ConnectionError as ex:
            print('Requestlib - request_option')
            print(ex.__cause__)
            print(ex.__class__)
            print(ex.__context__)

    #######################
    # cookie
    #######################
    def print_cookie_value(self):
        cookie = None
        print('# : ', self.sess.cookies)
        print('# : ', type(self.sess.cookies))
        # session value
        for c in self.sess.cookies:
            # cookie = c.name +'='+ c.value
            print(c.name)
            print(c.value)
        return cookie

