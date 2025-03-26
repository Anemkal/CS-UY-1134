def postfix_calculator():
    ops = "+-*/"
    variables = {}
    stack = []
    done = False
    while not done:
        expression = input("--> ")
        if expression == "done()":
            done = True
        else:
            tokens = expression.split()
            if len(tokens) >= 3 and tokens[1] == "=":
                var_name = tokens[0]
                expr_tokens = tokens[2:]
                for token in expr_tokens:
                    if token.isdigit():
                        stack.append(int(token))
                    elif token in variables:
                        stack.append(variables[token])
                    elif token in ops:
                        arg2 = stack.pop()
                        arg1 = stack.pop()
                        if token == '+':
                            result = arg1 + arg2
                        elif token == '-':
                            result = arg1 - arg2
                        elif token == '*':
                            result = arg1 * arg2
                        elif token == '/':
                            if arg2 == 0:
                                print("Error: Division by zero")
                                return
                            result = arg1 / arg2
                        stack.append(result)
                variables[var_name] = stack.pop()
                print(var_name)

            else:
                for token in tokens:
                    if token.isdigit():
                        stack.append(int(token))
                    elif token in variables:
                        stack.append(variables[token])
                    elif token in ops:
                        arg2 = stack.pop()
                        arg1 = stack.pop()
                        if token == '+':
                            result = arg1 + arg2
                        elif token == '-':
                            result = arg1 - arg2
                        elif token == '*':
                            result = arg1 * arg2
                        elif token == '/':
                            if arg2 == 0:
                                print("Error: Division by zero")
                                return
                            result = arg1 / arg2
                        stack.append(result)
                    elif token == "=":
                        if stack:
                            print(stack.pop())
                if len(stack) == 1:
                    print(stack.pop())


postfix_calculator()
