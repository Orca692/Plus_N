from custom import custom_input # Библиотека input от пользователя с переводом под синтаксис +N
import list_of_cases # Библиотека с списком команд

Power_Button = True # Ключ активации терминала
while Power_Button: # Запуск терминала
    Main_Flow = True # Ключ активации главного потока
    while Main_Flow: # Запуск главного потока
        In_Flow = 'Main_Flow' # Название потока в котором находимся
        Custom_Command = custom_input.cusinput() # Создаем командную строку от пользователя
        if Custom_Command: # Проверка команды на []
            if Custom_Command[0] == 'exit': # Выполнение команды exit
                Main_Flow = False # Выход из главного потока
                Power_Button = False # Выход из программы
                Custom_Command[0] = 'clear' # Выполнение команды clear()
                list_of_cases.read_input(Custom_Command, In_Flow) # Очистка консоли
            else:
                list_of_cases.read_input(Custom_Command, In_Flow) # Функция исполняющие пользовательские команды
        else: # Сохранение пропуска, если нету команды
            continue # Далее