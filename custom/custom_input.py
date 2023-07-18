def cusinput(): # cusinput от custom_input() - функция для ввода и чтения команд
    Custom_Print = input('+N ') # Ввод для пользователя
    if Custom_Print == []: # Если пользовательская строка пуста, то:
        Skip == False
    else:
        Custom_Print = Custom_Print.split() # Разбитие строки на слова
        Custom_Command = [] # Массив, в котором будут храниться команды
        index = 0 # Индекс для перебора команд
        Count_Operators = -1 # Индекс для разделения строки на массивы по операторам
        while index < len(word): # Перебор всех команд в строке
            Custom_Word = list(Custom_Print[index][0]) # Переменная на проверку первого символа
            if Custom_Word[0] == '@': # Проверка команды на адрес
                Custom_Command[Count_Operators].append(Custom_Print[index]) # Присваивает адрес к массиву 
                # внутри списка
            elif Custom_Word[0] == '+': # Проверка команды на опцию
                if list(Custom_Command[Count_Operators][len(Custom_Command[Count_Operators]) - 1])[0] == '@': # проверка массива на
                    # ошибку который внутри списка. Перед опцией не может стоять адрес
                    print('syntax err') # сообщение об ошибке
                    Custom_Command.pop() # Удаление ошибочного элемента с ошибочным оператором
                    break # Выход из чтения команды
                else: # если ошибки нет, то опция присваивается к текущему массиву внутри списка
                    Custom_Command[Count_Operators].append(Custom_Print[index]) # Присваивает опцию к массиву
            else: # если слово не является адресом или опцией, то оно читается как оператор
                Custom_Command.append([Custom_Word[index]]) # Добавления нового массива в конец списка
                Count_Operators += 1 # Счётчик массивов внутри списка 
            index += 1 # Переход к следующему слову
        
        print(Custom_Command)
        return Custom_Command # Итог функции
