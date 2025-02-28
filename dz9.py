import requests


url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data:
        usd_rate = data[0]["rate"]


        amount_uah = float(input("Введіть суму в гривнях: "))


        amount_usd = amount_uah / usd_rate


        print(f"{amount_uah} грн = {amount_usd:.2f} USD")
    else:
        print("Не вдалося отримати курс долара США.")
else:
    print("Помилка при отриманні даних з API НБУ")