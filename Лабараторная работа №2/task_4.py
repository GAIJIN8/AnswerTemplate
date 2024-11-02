money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
total = money_capital + salary - spend
cur_spend = spend
while True:
    total += salary - cur_spend
    if total <= 0:
        break
    cur_spend += spend * increase
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
