def userdata(**kwargs):
    print(f"{firstName} {secondName} {yearBirth} {city} {email} {phone}")


firstName = input('Ваше имя?')
secondName = input('Ваша фамилия?')
yearBirth = input('Ваш год рождения?')
city = input('Город проживания?')
email = input('Ваша эл. почта?')
phone = input('Ваш телефон?')

userdata(firstName=firstName, secondName=secondName, yearBirth=yearBirth, city=city, email=email, phone=phone)