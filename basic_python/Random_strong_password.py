#Tạo password mạnh ngẫu nhiên
import random

#Tạo 4 list chứa chữ số, chữ thường, chữ hoa, kí tự đặc biệt
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

#Đảm bảo password có chứa cả 4 loại kí tự trên
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
temp_pass = [rand_digit, rand_upper, rand_lower, rand_symbol] 

#Chọn ngẫu nhiên các kí tự còn lại
MAX_LEN = 12
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
for x in range(MAX_LEN - 4):
    temp_pass.append(random.choice(COMBINED_LIST))

#Trộn các kí tự đã chọn tạo password ngẫu nhiên
random.shuffle(temp_pass)
password = ""
for x in temp_pass:
        password = password + x

print("Password generated: " + password)