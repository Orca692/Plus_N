from custom import custom_input # Библиотека input от пользователя с переводом под синтаксис +N
import list_of_cases # Библиотека с списком команд

Power_Button = True # Ключ активации терминала
while Power_Button: # Запуск терминала
    Main_Flow = True # Ключ активации главного потока
    while Main_Flow: # Запуск главного потока
        In_Flow = 'Main_Flow' # Название потока в котором находимся
        Custom_Command = custom_input.cusinput() # Создаем командную строку от пользователя
        if Custom_Command: # Проверка команды на []
            Power_Status = list_of_cases.read_input(Custom_Command, In_Flow) # Функция исполняющие пользовательские команды
            match Power_Status: # Power_Status нужен для выполнения операций, которые находятся во вне потоков
                case 'exit': # Выйти из программы
                    Power_Button = False # Выход из программы
                    Main_Flow = False # Выход из главного потока
                case _: # Если неизвестный индекс
                    continue # Продолжить --> Сделать сообщение об ошибке, потому что сюда прога не
                    # должна заходить естественным путем
        else: # Сохранение пропуска, если нету команды
            continue # Далее