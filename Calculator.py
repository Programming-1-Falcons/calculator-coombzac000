while True:  
    Sym = input("Adding, Subtracting, Multiplying, Dividing, or Exponentiation?: ")  
    Num1 = float(input("What is the first number?: "))    
    Num2 = float(input("What is the second number?: "))    
  
    if Sym == "+":  
        print(Num1 + Num2)  
    elif Sym == "-":  
        print(Num1 - Num2)  
    elif Sym == "*":  
        print(Num1 * Num2)  
    elif Sym == "X":  
        print(Num1 * Num2)  
    elif Sym == "/":  
        print(Num1 / Num2)  
    elif Sym == "^":  
        print(Num1 ** Num2)  
