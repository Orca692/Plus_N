# Список команд главного потока
# Прописывая аргументы arg[0], нужно прописывать и в 
# functions_of_cases.py такую функцию def НазваниеФункции(arg: list)

from cases import functions_of_cases # Для экономии места, функции операторов хранятся в другом файле

def read_input(arg: list, In_Flow): # Функция по исполнению команды
    match arg[0]: # обращение к 1-му слову
        case 'clear': # clear()
            return functions_of_cases.clear() # Очищает консоль
        case 'flow': # 
            return functions_of_cases.flow(In_Flow) # Показывает в каком потоке мы находимся
        case _: # case_
            return functions_of_cases.case_(arg[0]) # Сообщение: not found 

# Сделать двойной цикл while
# Один цикл будет выполнять все опции и адреса оператора
# Другой цикл будет переключать на следующие операторы
# #
