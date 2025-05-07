user_input = "abc"

try:
    number = int(user_input)
except ValueError:
    number = 0

print(number)  # 0
