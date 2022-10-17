# -*- coding: utf-8 -*-

# from elasticsearch import Elasticsearch
# # import data.onch_info as Info
# from elasticsearch import helpers
# class libes:
#     def __init__(self):
#         self.man = 10000
#         self.esip = '192.168.0.41:9200'
#         self.es = Elasticsearch(self.esip)
#
#     def insertbulk_newprod(self, np,indexname):
#         newDoc = []
#         for linedat in np:
#             onedoc = linedat.get_data_dict12()
#             doc = {'_index': indexname, '_source': onedoc}
#             newDoc.append(doc)
#         helpers.bulk(self.es, newDoc, index=indexname)