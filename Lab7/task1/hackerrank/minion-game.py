def minion_game(string):
    string = string.lower()
    vowels = ["a", "e", "o", "u", "i"]
    stuart = []
    kevin = []

    for i in range(len(string)):
        if string[i] in vowels:
            for j in range(i + 1, len(string) + 1):
                kevin.append(string[i:j])
        else:
            for j in range(i + 1, len(string) + 1):
                stuart.append(string[i:j])
    
    if len(stuart) > len(kevin):
        print("Stuart", len(stuart))
        
    elif len(kevin) > len(stuart):
        print("Kevin", len(kevin))
    else:
        print("Tie", len(kevin))
    #print(stuart)
    #print(kevin)

minion_game(input())