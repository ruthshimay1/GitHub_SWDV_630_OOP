import useCases as u

#Enter the number of the use case you want to run when prompted:

while True:
    try:
        userInput = int(input("Enter Use Case number between 1 and 6: "))
    
        if userInput == 0:
            break
        elif userInput == 1:
            u.testCase1()
        elif userInput == 2:
            u.testCase2()
        elif userInput == 3:
            u.testCase3()
        elif userInput == 4:
            u.testCase4()
        elif userInput == 5:
            u.testCase5()       
                       
    except ValueError:
        print('Invalid Input(s), try again.')
        continue
  
   
            
            
            
        