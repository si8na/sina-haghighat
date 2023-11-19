def intelligent_search(target_number):
    upper_limit = 1000   
    
    while True:
        guess = upper_limit // 2  
        
        if guess == target_number:  
            return guess
        elif guess < target_number:  
            upper_limit = guess
        else:  
            upper_limit += guess // 2



target = int(input("please enter a three-digit number:"))


result = intelligent_search(target)

print("number found:", result)