"""Вы работаете над формой регистрации на веб-сайте. 
Форма принимает имя пользователя и его возраст. 
Имя пользователя должно быть длиной не менее 5 символов и не более 20 
символов. Возраст должен быть больше 0 и меньше 120. 
Ваша задача - написать программу, которая будет проверять 
введенные данные на правильность."""

username = 'aJDLRrWWYmuAGhusQdzqDofb'
age = 68

quantity = len(username)
name_length = (quantity >= 5) and (quantity <= 20)
age_verification = (age > 0) and (age < 120)
print(name_length and age_verification)

hours = 15
minutes = 51
seconds = 35
test_hours = (hours >= 0) and (hours < 24)
test_minutes = (minutes >= 0) and (minutes < 60)
test_econds = (seconds >= 0) and (seconds < 60)

print(test_hours and test_minutes and test_econds)