def generate_numvers_1(max_number: int):
    print("called generate_numbers_1 function")
    numbers = []
    for i in range(1, max_number+1):
        numbers.append(i)
    return numbers

# 함수 내에서 yield는 Generate객체 만들어내는 함수
def generate_numbers_2(max_number: int):
    print("called generate_numbers_2 function")
    for i in range(1, max_number+1):
         yield i 

numbers_1 = generate_numvers_1(10)
numbers_2 = generate_numbers_2(10)
print(numbers_1)
print(numbers_2)

# gen1 = gen2 같은데 다른 방법
# gen1 = (i**2 for i in [1,2,3,4,5])  # 제너레이터 표현식

# # 함수 방식, class로도 구현 가능
# def make_numbers():
#     for i in [1,2,3,4,5]:
#         yield i

# gen2 = make_numbers()

