def train():
    print("Существующие кружки: Python, English")
    #кружки

def schedule():
    print("""Расписание занятий: 
    Понедельник: 10:00 - 12:00
    Среда: 10:00 - 12:00
    Пятница: 10:00 - 12:00""")
    #вывод расписания

def coach_info():
    print("""Контактные данные тренера:
    Python: Олег Юрьевич - +7 111 111 11 11;
    English: Kto-to - +7 000 000 00 00.
    """)
    #контактные данные тренера

def payment():
    print("""Стоимость занятий:
    Python: 500 - одно занятие, 10000 - месяц;
    English: 300 - одно занятие, 8000 - месяц.
    """)
    #ыводд суммы оплаты

def reply():
    print("Способы оплаты: наличный, безналичный, в рассрочку")

def auto(request):
    if "круж" in request:
        train()
    elif "расп" in request:
        schedule()
    elif "трен" in request:
        coach_info()
    elif "цена" in request:
        payment()
    elif "стоим" in request:
        payment()
    elif "способ" in request:
        reply()
    else:
        print("Извините, я не понимаю ваш запрос.")