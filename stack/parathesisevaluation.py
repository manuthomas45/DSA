def is_valid_parentheses(s):
    stack=[]
    mapping={"}":"{","]":"[",")":"("}
    for i in s:
        if i in mapping:
            top=stack.pop() if stack else "*"
            if top!=mapping[i]:
                return False
        else:
            stack.append(i)
    return not stack
     
print(is_valid_parentheses("()[]{}"))  # True
# print(is_valid_parentheses("(]"))      # False
# print(is_valid_parentheses("([])"))    # True

# stack=["("]
# if not stack:
    # print("True")
# print(not stack)