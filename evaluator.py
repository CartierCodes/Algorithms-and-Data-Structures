# Carter Burzlaff - PP Chapter 6
# This program requires the use of Professor Omari's stack_list.py
# This program is very similar to Professor Omari's evel-expr.py, as it is supposed to be a simpler version of it

from stack_list import Stack, Empty

ops = '+-'
test_exp = '2 + 15 + 8 - 4 + 3 - 22 - 6 + 12 - 6'
tokens = test_exp.split()

val_stack = Stack()
op_stack = Stack()

for token in tokens:
    if token.isalnum():
        try:
            top_ops = op_stack.top()
        except Empty:
            val_stack.push(token)
            continue

        result = eval('{val1} {op} {val2}'.format(val1 = val_stack.pop(),
                                                  val2 = token,
                                                  op   = op_stack.pop()))
        val_stack.push(result)

    elif token in ops:
        op_stack.push(token)

while not op_stack.is_empty():
    result = eval('{val1} {op} {val2}'.format(val1 = val_stack.pop(),
                                              val2 = val_stack.pop(),
                                              op   = op_stack.pop()))
    val_stack.push(result)

print('\nCalculated Result: {0}'.format(val_stack.pop()))
print('Expected Result: {0}\n'.format(2 + 15 + 8 - 4 + 3 - 22 - 6 + 12 - 6))
