#모듈 1
import practice_54
practice_54.price(3) # 3명이서 영화 보러 갔을 때 가격
practice_54.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 
practice_54.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때 

# 모듈 2
import practice_54 as p5
p5.price(3)
p5.price_morning(4)
p5.price_soldier(5)

# 모듈 3
from practice_54 import *
price(3)
price_morning(4)
price_soldier(5)

# 모듈 4
from practice_54 import price,price_morning
price(5)
price_morning(6)

# 모듈 5 - 별명으로 쓰기 
from practice_54 import price_morning as pm
pm(6)
