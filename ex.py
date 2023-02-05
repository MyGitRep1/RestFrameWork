from misesis import Person, Payment

user = Person('ru')

print(user.name())
print(user.surname())
print(user.political_views())
print(user.age())

a = Payment('ru')
print(a.credit_card_owner())