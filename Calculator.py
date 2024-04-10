flag = True
op_string = '+-*/^%'
def check(tokens):
    stack = [] # Stack for checking balanced parentheses
    previous_token = ""
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            if not stack or stack[-1] != '(':
                print('Unbalanced brackets')
                return False
            stack.pop()

        # Check for consecutive numbers
        if token.replace('.', '', 1).isdigit() and previous_token.replace('.', '', 1).isdigit():
            print('Consecutive numbers found')
            return False

        # Check for consecutive operators
        if token in op_string and previous_token in op_string:
            print('Consecutive operators found')
            return False
        previous_token = token
    if stack:
        print('brackets are unbalanced')
        return False
    return True

def tokenize(exp):
    global flag
    flag = True
    tokens = []
    number_buffer = []
    for char in exp:
        if char.isdigit() or char == '.':
            number_buffer.append(char)
        else:
            if number_buffer:
                tokens.append(''.join(number_buffer))
                number_buffer = []
            if char == ' ':
                continue  # Ignore spaces
            elif char in op_string:
                tokens.append(char)
            else:
                flag = False
                break  # Break on encountering an invalid character
    if number_buffer:
        tokens.append(''.join(number_buffer))
    return tokens

def cal(tokens):
    order = {'^':4,'*':3,'/':3,'%':3,'+':2,'-':2,'(':1}
    op_stack = []
    postfix_list = []
    for token in tokens:
        if '.' in token or token.isnumeric():
            postfix_list.append(token);
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            cur = op_stack.pop()
            while(cur != '('):
                postfix_list.append(cur)
                cur = op_stack.pop()
        else:
            while op_stack and order[op_stack[-1]] >= order[token]:
                postfix_list.append(op_stack.pop())
            op_stack.append(token)
    while(op_stack):
        postfix_list.append(op_stack.pop())

    cal_stack = []
    for token in postfix_list:
        if '.' in token or token.isnumeric():
            cal_stack.append(float(token))
        elif token == '+':
            right = cal_stack.pop()
            left = cal_stack.pop()
            cal_stack.append(left + right)
        elif token == '-':
            right = cal_stack.pop()
            left = cal_stack.pop()
            cal_stack.append(left - right)
        elif token == '*':
            right = cal_stack.pop()
            left = cal_stack.pop()
            cal_stack.append(left * right)
        elif token == '/':
            right = cal_stack.pop()
            left = cal_stack.pop()
            cal_stack.append(left / right)
        elif token == '^':
            right = cal_stack.pop()
            left = cal_stack.pop()
            cal_stack.append(float(left) ** float(right))
        elif token == '%':
            right = cal_stack.pop()
            left = cal_stack.pop()
            cal_stack.append(left % right)
    return cal_stack.pop()

if __name__ == '__main__':
    print('------------------GUI-------------------')
    print('Jyx Calculator:')
    print('Valid operators:',op_string)
    print('Type \'Exit\' to exit')
    print('----------------------------------------')
    while True:
        exp = input('expression:')
        if(exp == 'Exit'):
            break
        else:
            if exp:
                exp = tokenize(exp)
                if flag:
                    if(check(exp)):
                        try:
                            print(cal(exp))
                        except Exception as e:
                            print('invalid input')
                else:
                    print('invalid operators')
            else:
                print("Empty input?")
            print('-------------------------')
