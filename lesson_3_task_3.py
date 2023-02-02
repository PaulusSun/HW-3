from Address import Address
from Address import Mailing

a=Address(140400, 'г. Москва', 'ул. Иванова', 20, 1)

example=Mailing(a.my_return(), a.my_return(), 200, '122144455-5225')

example.my_print()