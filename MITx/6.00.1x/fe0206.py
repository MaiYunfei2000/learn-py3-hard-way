varA = -2
varB = 'goodbye'

typeVarA = str(type(varA))
typeVarB = str(type(varB))

if typeVarA == "<class 'str'>" or typeVarB == "<class 'str'>":
    print("string involved")
elif typeVarA != "<class 'str'>" and typeVarB != "<class 'str'>":
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")