from Stack import Stack

def InfixToPrefix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1
    opStack = Stack()
    prefixList = []
    tokenList = infixexpr.split()
    tokenList.reverse()     #Ex: ( A + B ) * C => C * ( B + A )

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        elif token == ')':
            opStack.push(token)
        elif token == '(':
            topToken = opStack.pop()
            while topToken != ')':
                prefixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  prefixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        prefixList.append(opStack.pop())
    prefixList.reverse()    #Ex: C B A + * => * + A B C
    return " ".join(prefixList)

print(InfixToPrefix("A * B + C * D"))
print(InfixToPrefix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(InfixToPrefix("( A + B ) * C"))
