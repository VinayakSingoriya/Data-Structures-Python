# Algorithm: 

# 1.Declare a character stack S.
# 2.Now traverse the expression string exp. 
#     A. If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
#     B. If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if the popped character is the matching starting bracket then fine else      parenthesis are not balanced.
# 3.After complete traversal, if there is some starting bracket left in stack then “not balanced”



def areParantehsisIsBalanced(expression):
    stack = [] 

    for char in expression:                 # Time Complexity = O(n), Auxiliary Space = O(n) for stack

        # Traversing the expression
        if char in ['(', '{', '[']:
            # Push the element in the stack
            stack.append(char)
        else:
            
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return False            
            if current_char == '{':
                if char != '}':
                    return False            
            if current_char == '[':
                if char != ']':
                    return False 
    # Check Empty Stack
    if stack:
        return False
    return True    

if __name__ == "__main__":
    expression = '{()}[]'
    result = areParantehsisIsBalanced(expression)
    if result == True:
        print("BALANCED")
    else:
        print("UNBALANCED")                                       