stack = []

s = "()"

for br in s:
    if len(stack) == 0:
        stack.append(br)
    
    if stack[-1] == '(' and br == ')':
        stack.pop()
    
    elif stack[-1] == '{' and br == '}':
        stack.pop()
    
    elif stack[-1] == '[' and br == ']':
        stack.pop()
    
    else:
        stack.append(br)

if len(stack) == 0:
    print(stack)
else:
    print(stack)
