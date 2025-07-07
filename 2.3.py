def investment_decision():
    X = int(input("7"))
    A = int(input("3"))
    B = int(input("5"))
    
    mike_can_invest = A >= X
    ivan_can_invest = B >= X

    if mike_can_invest and ivan_can_invest:
        print(2)  
    elif mike_can_invest:
        print("Mike")  
    elif ivan_can_invest:
        print("Ivan")  
    elif A + B >= X:
        print(1)  
    else:
        print(0) 

investment_decision()