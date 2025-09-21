from address import Address
from mailing import Mailing
addr1 = Address(123356, "Калининград", "Мира", 10, 5)
addr2 = Address(569215, "Москва", "Ленина", 1, 9)
mail1 = Mailing(addr1, addr2, 500, 901010104)

print(mail1)
