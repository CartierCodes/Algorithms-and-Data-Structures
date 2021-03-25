def is_valid_expr(expr: str):
    pStack = []
    for item in expr:
        if item == '(' or item == ')':
            pStack.append(item)
    counter = 0
    for p in pStack:
        if p == '(':
            counter += 1
        elif p == ')':
            counter -= 1
        if counter < 0:
            return False
    if counter > 0:
        return False
    return True

def test(str):
    print("Testing:", str)
    print("Is Valid:", is_valid_expr(str))
    print("")

test("(")
test("()")
test(")")
test("()()(())")
test("(()")
test("())")