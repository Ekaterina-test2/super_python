from address import Address
from mailing import Mailing
addr1 = Address(123356, "Калининград", "Мира", 10, 5)
addr2 = Address(569215, "Москва", "Ленина", 1, 9)
addr3 = Address(691890, "Казань", "Грибоедова", 61, 90)
addr4 = Address(702689, "Новосибирск", "Кутузова", 16, 7)
mail1 = Mailing(addr1, addr3, 500, 901010104)

print(mail1)
