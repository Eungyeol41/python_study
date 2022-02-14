#리스트를 선언합니다.
list_a = ['가', '나', '다', '라']
list_b = [1, 2, 3, 4]
list_c = ['a', 'b', 'c', 'd']

# 리스트 연산자 사용하기
print("# 리스트 연산자 사용하기")
print(list_b)
print(list_c)
print(list_b + list_c)
print(list_b * 2)
print("list_b의 길이는: ", len(list_b))
print("list_c의 길이는: ", len(list_c))
print()

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(1)
list_a.append(2)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 'A')
list_a.insert(5, 'B')
print(list_a)
print()

# 리스트 요소의 변화 확인하기
print("# 리스트 요소의 변화 확인하기")
print(list_a)
print(list_b)
print(list_c)