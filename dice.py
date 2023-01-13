# Write your solution here
def roll(die):
    from random import choice
    if die == "A":
        roll = [3, 3, 3, 3, 3, 6]
    if die == "B":
        roll = [2, 2, 2, 5, 5, 5]
    if die == "C":
        roll = [1, 4, 4, 4, 4, 4]
    
    return(choice(roll))

def play(die1: str, die2: str, times: int):
    from random import choice
    die_assign = {die1: 0, die2: 0}
    
    for item in die_assign:
        if item == "A":
            die_assign[item] = [3, 3, 3, 3, 3, 6]
        if item == "B":
            die_assign[item] = [2, 2, 2, 5, 5, 5]
        if item == "C":
            die_assign[item] = [1, 4, 4, 4, 4, 4]
    
    return_value = [0,0,0]
    
    while times > 0:
        first = choice(die_assign[die1]) 
        second = choice(die_assign[die2])
        
        if first > second:
            return_value[0] += 1
        elif first < second:
            return_value[1] += 1
        elif first == second:
            return_value[-1] += 1
        first = 0
        second = 0
        times -= 1
    
    return(return_value[0],return_value[1],return_value[-1])
        


if __name__=="__main__":
    
    for i in range(20):
        print(roll("A"), " ", end="")
    
    print(play("A", "C", 5))

    