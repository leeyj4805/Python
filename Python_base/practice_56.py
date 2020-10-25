# import travel.thailand # .thailand ->모듈이나 패키지만 가능하다
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import * # travel 패키지에 모든것을 가지고 오겠다
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) # 랜덤 파일
print(inspect.getfile(thailand)) # thailand 파일