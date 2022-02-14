# 정수
ouput_a = "{:d}".format(52)

# 특정 칸에 출력하기
ouput_b = "{:5d}".format(52)
ouput_c = "{:10d}".format(52)

# 빈칸을 0으로 채우기
ouput_d = "{:05d}".format(52)
ouput_e = "{:05d}".format(-52)

# 출력하기
print("# 기본")
print(ouput_a)
print("# 특정 칸에 출력하기")
print(ouput_b)
print(ouput_c)
print("# 빈칸을 0으로 채우기")
print(ouput_d)
print(ouput_e)