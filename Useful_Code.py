# IDE에서 현재 경로를 잘못 가지고 오는 경우
# python $(FULL_CURRENT_PATH)
# 해당 함수를 사용하면 .py 의 경로를 구하는게 아니라 NotePad++ 실행 파일의 경로가 구해지는 문제가 생긴다
import os
os.chdir(os.path.dirname(__file__))

