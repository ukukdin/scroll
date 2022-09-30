text = '''70. A word on document types
71. Search methods
72. Searching with the request URI
73. Introducing the Query DSL
74. How searching works
75. Understanding query results
76. Understanding relevance scores
77. Debugging unexpected search results
78. Query contexts
79. Full text queries vs term level queries
퀴즈 4: Basics of searching
80. Introduction to term level queries
81. Searching for a term
82. Searching for multiple terms
83. Retrieving documents based on IDs
84. Matching documents with range values
85. Working with relative dates (date math)
86. Matching documents with non-null values
87. Matching based on prefixes
88. Searching with wildcards
89. Searching with regular expressions
과제 1: Term Level Queries
90. Introduction to full text queries
91. Flexible matching with the match query
92. Matching phrases
93. Searching multiple fields
과제 2: Full Text Queries
94. Introduction to compound queries
95. Querying with boolean logic
96. Debugging bool queries with named queries
97. How the “match” query works
98. Introduction to this section
99. Querying nested objects
100. Nested inner hits
101. Mapping document relationships
102. Adding documents
103. Querying by parent ID
104. Querying child documents by parent
105. Querying parent by child documents
106. Multi-level relations
107. Parent/child inner hits
108. Terms lookup mechanism
109. Join limitations
110. Join field performance considerations
111. Specifying the result format
112. Source filtering
113. Specifying the result size
114. Specifying an offset
115. Pagination
116. Sorting results
117. Sorting by multi-value fields
118. Filters
119. Introduction to aggregations
120. Metric aggregations
121. Introduction to bucket aggregations
122. Document counts are approximate
123. Nested aggregations
124. Filtering out documents
125. Defining bucket rules with filters
126. Range aggregations
127. Histograms
128. Global aggregation
129. Missing field values
130. Aggregating nested objects
131. Introduction to this section
132. Proximity searches
133. Affecting relevance scoring with proximity
134. Fuzzy match query (handling typos)
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
5avs분

5분'''


import re
# text= "들어갈 값"
#
# #re의 기능중 하나인 sub(자르기)로 정규표현식 사용
# text = re.sub(r'[^분0-9]','',text)
# '''text에서 분과 숫자를 제외한것을 잘라서 '' <- 즉 공백없게 만들어라
# 그리고 re에 다른 기능인 findall(은 정규식과 매치되는 모든 문자열을 리스트형식으로 리턴한다.)
# 사용하여서 '(\w+)분?' (\w+)는 숫자와 모든 언어를 포함하는것 분? 는 분을 포함하는 것
# 즉 모든숫자단어+분이 포함되는 것을 찾아주라는 기능입니다. '''
# text=re.findall(r'(\w+)분?',text)
# # 그 이후 for 문으로 만약 분이 포함된다면 값을리스트해주라는 얘기입니다.
# text = [s for s in text if '분' in s]
# '''그리고 print를 해주면되는데 여기서 리스트로 되어있는 text변수를 *text,sep='\n'을 해줌으로써
# 리스트의 세로출력이 완성이 됩니다. for 루프를 돌리거나 pprint 모듈을 임포트하지 않고도,
# 한 줄의 코드로 처리할 수 있어서 매우 편리하지 않나요?
# 우선 배열 앞에 * 연산자를 붙여서 함수를 호출하면 마치 여러 개의 인자를 넘긴 효과가 납니다.
# 그리고 print() 함수에는 가변 길이의 인자를 넘길 수 있는데요.
# 기본적으로는 공백을 구분자로 사용합니다.
# sep 옵션으로 이 구분자를 다른 문자로 바꿀 수가 있습니다.'''

text = re.sub(r'[^분0-9\s]','',text)



text=re.findall(r'(\w+)분?',text)




text = [s for s in text if '분' in s]
print(text)