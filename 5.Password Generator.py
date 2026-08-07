import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','&',"*",'+']
pg_letter=int(input("How many letters you need in password?"))
pg_number=int(input("How many numbers you need in password?"))
pg_symbol=int(input("How many symbols you need in password?"))
password=[]
for let in range(pg_letter):
    password.append(random.choice(letters))
for num in range(pg_number):
    password.append(random.choice(numbers))
for symb in range(pg_symbol):
    password.append(random.choice(symbols))
random.shuffle(password)
final_password=""
for char in password:
    final_password +=char
print(final_password)
