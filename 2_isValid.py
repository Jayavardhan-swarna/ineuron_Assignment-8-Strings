def isValid(s):
    stack = []  # Use a stack to keep track of parentheses and asterisks
    
    for char in s:
        if char == '(' or char == '*':
            stack.append(char)
        else:
            if not stack:
                return False  # Unmatched closing parenthesis
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                elif stack[-1] == '*':
                    stack.pop()
                    if stack and stack[-1] == '(':
                        stack.pop()
                else:
                    return False  # Unmatched closing parenthesis
    
    # At this point, we have scanned the entire string
    # Now, we need to check if there are any unmatched opening parentheses
    while stack:
        if stack[-1] == '(' or stack[-1] == '*':
            stack.pop()
        else:
            return False  # Unmatched opening parenthesis
    
    return True

s = "()"
result = isValid(s)
print(result)  # Output: True 
