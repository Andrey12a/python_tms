def calculator():
    while True:
        num_input1 = input('Введите первое число: ')
        if 'exit' in num_input1:
            quit()
        num_input2 = input('Введите второе число: ')
        if 'exit' in num_input2:
            quit()
        numerical_action = input('Введите ваше действие (+, -, *, /, **): ')
        if 'exit' in numerical_action:
            quit()

        if numerical_action == '+':
            resul = int(num_input1) + int(num_input2)
            print(resul)
        elif numerical_action == '-':
            resul = int(num_input1) - int(num_input2)
            print(resul)
        elif numerical_action == '*':
            resul = int(num_input1) * int(num_input2)
            print(resul)
        elif numerical_action == '/':
            while True:
                try:
                    int(num_input1) / int(num_input2)
                except ZeroDivisionError:
                    print('Деление на ноль невозможно, попробуйте снова!')
                    return calculator()
                else:
                    break
            resul = int(num_input1) / int(num_input2)
            print(resul)
        elif numerical_action == '**':
            resul = int(num_input1) ** int(num_input2)
            print(resul)


calculator()
