'''css selector - 한정자?
한정자 예시
 * 모든 노드들
 div, p = div 와 p 노드들
 div p  div 안에 있는 p 노드들
 div > p div 바로 안에 있는 p 노드들
 div ~ p p 옆에 (앞)에 있는 div 노드들
 div + p div옆(뒤)_에 있는  p 노드들

'''
from PIL import Image

'''고급 한정자 22강
'''
# 고급 한정자 관련 예시
image = Image.open("CSS.png")

''' : <- 들어가는 순간부터 div.sale: 이런식으로 붙게 됩니다. :은 고급한정자라고 생각하시면됩니다.
:enabled - 활성화된 상태
:checked - 체크 되어있는 상태
:empty - 값이 비어있는 상태 
:first-child - 첫번째 자식
:last-child - 마지막 자식
:first-of-type - 해당 타입의 첫번째 노드
:last-of-type - 해당 타입의 마지막 노드
:hover - 마우스가 올라간 상태
:not - 다음 조건이 거짓일 경우
:nth-chiuld - n 번째 자식
:"nth-of-type - n번째 타입 
'''


# 고급한정자 관련 예시 2번째 23강

from bs4 import BeautifulSoup as BS

html = """
        <head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div>안녕하세요 </div>

</body>
"""
soup = BS(html,"html.parser")
div = soup.select("title")
print(div[0].get_text(strip=True))

'''
##checked
arr = soup.select("input:checked")
print(arr)

#disabled
arr = soup.select("input:disabled")

empty
arr = soup.select("label_input:empty")
first=child
arr = soup.select(b:first-child")
last-child
arr = soup.select("table tbody tr:last-child")
print(arr)

first-of-type
arr =  soup.sleect("table tbody td:first-of-type")
tbody 안에 td중에 제일 먼저 나온  td 사이즈 

not 
arr = soup.select("b:not(:first-of-type)")
b가 first-of-type 이 아닌거 즉 첫번째 타입 외에 b의 값을 보여줘 이런거임

nth-child
arr= soup.select("table tbody tr:nth-child(2)")

nth-of-type
arr= soup.select("table tbody tr:nth-of-type(2)")

둘의 값은 같다 (nth-child,nth-type-child)
'''
import re
text= """
1. Introduction to the course
6분
재생
2. Introduction to Elasticsearch
7분
재생
3. Overview of the Elastic Stack
18분
시작
퀴즈 1: Understanding of the Elastic Stack
재생
4. Walkthrough of common architectures
11분
시작
5. Guidelines for the course Q&A
2분
재생
6. Overview of installation options
3분
재생
7. Running Elasticsearch & Kibana in Elastic Cloud
6분
재생
8. Setting up Elasticsearch & Kibana on macOS & Linux
8분
재생
9. Setting up Elasticsearch & Kibana on Windows
7분
재생
10. Understanding the basic architecture
7분
재생
11. Inspecting the cluster
8분
재생
12. Sending queries with cURL
8분
재생
13. Sharding and scalability
9분
시작
퀴즈 2: Sharding
재생
14. Understanding replication
18분
시작
퀴즈 3: Replication
재생
15. Adding more nodes to the cluster
12분
재생
16. Overview of node roles
10분
재생
17. Wrap up
1분
재생
18. Creating & deleting indices
3분
재생
19. Indexing documents
4분
재생
20. Retrieving documents by ID
1분
재생
21. Updating documents
4분
재생
22. Scripted updates
8분
재생
23. Upserts
3분
재생
24. Replacing documents
1분
재생
25. Deleting documents
1분
재생
26. Understanding routing
5분
재생
27. How Elasticsearch reads data
3분
재생
28. How Elasticsearch writes data
8분
재생
29. Understanding document versioning
3분
재생
30. Optimistic concurrency control
7분
재생
31. Update by query
9분
재생
32. Delete by query
2분
재생
33. Batch processing
14분
재생
34. Importing data with cURL
7분
재생
35. Wrap up
1분
재생
36. Introduction to this section
1분
재생
37. Introduction to analysis
6분
재생
38. Using the Analyze API
5분
재생
39. Understanding inverted indices
7분
재생
40. Introduction to mapping
2분
재생
41. Overview of data types
9분
재생
42. How the "keyword" data type works
4분
재생
43. Understanding type coercion
6분
재생
44. Understanding arrays
5분
재생
45. Adding explicit mappings
6분
재생
46. Retrieving mappings
2분
재생
47. Using dot notation in field names
2분
재생
48. Adding mappings to existing indices
2분
재생
49. How dates work in Elasticsearch
6분
재생
50. How missing fields are handled
2분
재생
51. Overview of mapping parameters
15분
재생
52. Updating existing mappings
4분
재생
53. Reindexing documents with the Reindex API
13분
재생
54. Defining field aliases
4분
재생
55. Multi-field mappings
7분
재생
56. Index templates
8분
재생
57. Introduction to the Elastic Common Schema (ECS)
6분
재생
58. Introduction to dynamic mapping
9분
재생
59. Combining explicit and dynamic mapping
2분
재생
60. Configuring dynamic mapping
8분
재생
61. Dynamic templates
13분
재생
62. Mapping recommendations
5분
재생
63. Stemming & stop words
4분
정지
64. Analyzers and search queries
4분
재생
65. Built-in analyzers
8분
재생
66. Creating custom analyzers
10분
재생
67. Adding analyzers to existing indices
6분
재생
68. Updating analyzers
7분
재생
69. Wrap up
1분
시작
70. A word on document types
1분
재생
71. Search methods
2분
재생
72. Searching with the request URI
4분
재생
73. Introducing the Query DSL
3분
재생
74. How searching works
4분
재생
75. Understanding query results
2분
재생
76. Understanding relevance scores
11분
재생
77. Debugging unexpected search results
2분
재생
78. Query contexts
3분
재생
79. Full text queries vs term level queries
6분
시작
퀴즈 4: Basics of searching
재생
80. Introduction to term level queries
1분
재생
81. Searching for a term
2분
재생
82. Searching for multiple terms
2분
재생
83. Retrieving documents based on IDs
1분
재생
84. Matching documents with range values
4분
재생
85. Working with relative dates (date math)
8분
재생
86. Matching documents with non-null values
2분
재생
87. Matching based on prefixes
1분
재생
88. Searching with wildcards
3분
재생
89. Searching with regular expressions
3분
시작
과제 1: Term Level Queries
재생
90. Introduction to full text queries
2분
재생
91. Flexible matching with the match query
5분
재생
92. Matching phrases
2분
재생
93. Searching multiple fields
3분
시작
과제 2: Full Text Queries
재생
94. Introduction to compound queries
1분
재생
95. Querying with boolean logic
11분
재생
96. Debugging bool queries with named queries
3분
재생
97. How the “match” query works
6분
재생
98. Introduction to this section
3분
재생
99. Querying nested objects
6분
재생
100. Nested inner hits
4분
재생
101. Mapping document relationships
3분
재생
102. Adding documents
7분
재생
103. Querying by parent ID
3분
재생
104. Querying child documents by parent
5분
재생
105. Querying parent by child documents
6분
재생
106. Multi-level relations
10분
재생
107. Parent/child inner hits
2분
재생
108. Terms lookup mechanism
6분
재생
109. Join limitations
2분
재생
110. Join field performance considerations
4분
재생
111. Specifying the result format
3분
재생
112. Source filtering
4분
재생
113. Specifying the result size
2분
재생
114. Specifying an offset
2분
재생
115. Pagination
5분
재생
116. Sorting results
5분
재생
117. Sorting by multi-value fields
2분
재생
118. Filters
4분
재생
119. Introduction to aggregations
3분
재생
120. Metric aggregations
10분
재생
121. Introduction to bucket aggregations
6분
재생
122. Document counts are approximate
6분
재생
123. Nested aggregations
6분
재생
124. Filtering out documents
3분
재생
125. Defining bucket rules with filters
3분
재생
126. Range aggregations
8분
재생
127. Histograms
8분
재생
128. Global aggregation
3분
재생
129. Missing field values
2분
재생
130. Aggregating nested objects
2분
재생
131. Introduction to this section
1분
재생
132. Proximity searches
7분
재생
133. Affecting relevance scoring with proximity
6분
재생
134. Fuzzy match query (handling typos)
9분
재생
135. Fuzzy query
3분
재생
136. Adding synonyms
12분
재생
137. Adding synonyms from file
6분
재생
138. Highlighting matches in fields
6분
재생
139. Stemming
5분
# """
# text=text.replace(" *")



# text=text.replace('재생','')
# text=text.replace('정지','')
# text=text.replace('과제','')
# text=text.replace('시작','')
# text=text.replace('퀴즈','')

# text=re.sub(r'[^0-9가-힣]',' ',text)
# text=re.sub(r'\n',' ',text)
# text=re.sub(r'  +','\n',text)
#
# # txt = text[1::2]
# text=re.sub(' ','',text)
# text=re.sub('\n',' ',text)
# # text=re.sub('[0-9]분','',text)
# # txt = text[::2]
# # print(txt)

text=re.sub(r'[^분0-9\s]','',text)
text=re.findall(r'(\w+)분?',text)
tt = [s for s in text if '분' in s]
# str=' '.join(tt)

print(*tt,sep='\n')










# tt ='''
#
# '6분', '7분', '18분', '11분', '2분', '3분', '6분', '8분', '7분', '7분', '8분', '8분', '9분', '18분', '12분', '10분', '1분',
# '3분', '4분', '1분', '4분', '8분', '3분', '1분', '1분', '5분', '3분', '8분', '3분', '7분', '9분', '2분', '14분', '7분', '1분',
# '1분', '6분', '5분', '7분', '2분', '9분', '4분', '6분', '5분', '6분', '2분', '2분', '2분', '6분', '2분', '15분', '4분', '13분',
# '4분', '7분', '8분', '6분', '9분', '2분', '8분', '13분', '5분', '4분', '4분', '8분', '10분', '6분', '7분', '1분', '1분', '2분',
# '4분', '3분', '4분', '2분', '11분', '2분', '3분', '6분', '1분', '2분', '2분', '1분', '4분', '8분', '2분', '1분', '3분', '3분', '2분',
# '5분', '2분', '3분', '1분', '11분', '3분', '6분', '3분', '6분', '4분', '3분', '7분', '3분', '5분', '6분', '10분', '2분', '6분', '2분',
# '4분', '3분', '4분', '2분', '2분', '5분', '5분', '2분', '4분', '3분', '10분', '6분', '6분', '6분', '3분', '3분', '8분', '8분', '3분', '2분',
# '2분', '1분', '7분', '6분', '9분', '3분', '12분', '6분', '6분', '5분'
#
#
# '''
#
# tt=re.sub(r'[^\uAC00-\uD7A30-9\s]','',tt)
# tt=re.sub(' ','\n',tt)
#
# print(tt)