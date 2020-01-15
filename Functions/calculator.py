# add two numbers
# subtract one from another
# multiply
# divide
# modulo
# anythingelse

def add_numb(num1,num2):
    result = num1 + num2
    return print(result)

def sub_numb(num1,num2):
    result = num1 - num2
    return print(result)

def multi_numb(num1,num2):
    result = num1 * num2
    return print(result)

def divide_numb(num1,num2):
    result = num1 / num2
    return print(result)

def modulo_numb(num1,num2):
    result = num1 % num2
    return print(result)

def DNA_parse(string):
    As = 0
    Ts = 0
    Gs = 0
    Cs = 0
    for letter in string:
        if letter == "A":
            As += 1
        elif letter == "T":
            Ts += 1
        elif letter == "G":
            Gs += 1
        elif letter == "C":
            Cs += 1
        else:
            return "Wrong"

    return As, Ts, Gs, Cs
print(DNA_parse("AATTGGCCX"))


