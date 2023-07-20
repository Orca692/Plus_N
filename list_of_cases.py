# Список команд главного потока
# Прописывая аргументы Custom_Command[0], нужно прописывать и в 
# functions_of_cases.py такую функцию def НазваниеФункции(Custom_Command: list)

from cases import functions_of_cases # Для экономии места, функции операторов хранятся в другом файле

def read_input(Custom_Command: list, In_Flow, ): # Функция по исполнению команды
    # 
    # 
    # 
    # 
    # match Custom_Command[0][0] заменить на Custom_Command[index][0]
    #
    # 
    # 
    # 
    match Custom_Command[0][0]: # обращение к 1-му слову
        case 'nf': # Создать новый поток
            print()
        case 'exit': # Останавливает все потоки и выходит из программы
            return functions_of_cases.exit() # Присваивает новое значение для Power_Status
        case 'clear': # clear()
            functions_of_cases.clear() # Очищает консоль
        case 'flow': # 
            functions_of_cases.flow(In_Flow) # Показывает в каком потоке мы находимся
        case _: # case_
            functions_of_cases.case_(Custom_Command[0]) # Сообщение: not found 

# Сделать двойной цикл while
# Один цикл будет выполнять все опции и адреса оператора
# Другой цикл будет переключать на следующие операторы
# #
