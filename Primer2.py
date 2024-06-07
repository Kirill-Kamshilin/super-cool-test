age = 39
country = 'Италия'
age_verification = (age > 18) and (age <= 60)
allowed_countries = 'Россия, США, Канада, Австралия'
country_verification = country in allowed_countries
print(age_verification and country_verification)

username = 'aJDLRrWWYmuAGhusQdzqDofb'
age1 = 68

quantity = len(username)
name_length = (quantity >= 5) and (quantity <= 20)
age_verification1 = (age1 > 0) and (age1 < 120)
print(name_length and age_verification1)

hours = 15
minutes = 51
seconds = 35
test_hours = (hours >= 0) and (hours < 24)
test_minutes = (minutes >= 0) and (minutes < 60)
test_econds = (seconds >= 0) and (seconds < 60)

print(test_hours and test_minutes and test_econds)