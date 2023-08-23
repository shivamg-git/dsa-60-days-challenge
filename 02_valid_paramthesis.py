def valid_paramthesis(string_:str)->bool:
    stack_=[]
    for a in string_:
        if a == "(":
            stack_.append("(")
        else:
            if len(stack_) == 0:
                return False
            else:
                stack_.pop()

    return True if len(stack_) == 0 else False

print(valid_paramthesis("((()))()"))
print(valid_paramthesis("((())))"))
print(valid_paramthesis("((()))("))
print(valid_paramthesis(""))
print(valid_paramthesis(")"))