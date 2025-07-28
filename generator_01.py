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
