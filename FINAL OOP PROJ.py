import random

names_h=[]
hs_h=[]
class Highscores_h:
    def highscore(self):
        n_h=str(len(names_h))
        h_h=str(len(hs_h))
        print("Highscores are")
        print('Names \t\t\t Scores')
        for n_h, h_h in zip(names_h, hs_h):
            print(n_h ,'\t\t\t' ,h_h)
            
class Play_h():
    def playing(self):
        words=["website","programming","android","machine","technology","gaming","storage","application","software","network","hardware"]
        word_to_guess= random .choice(words)
        board= "*" * len(word_to_guess)
        alreadysaid = [None]
        chances=5
        
        guessed = False
        name=input("Enter your name\t\t\t")
        names_h.append(name)
        print(board)
        while not guessed and chances > 0:
            player_guess=input("What is your guess: ")

            if chances==5:
                score=50
            elif chances==4:
                score=40
            elif chances==3:
                score=30
            elif chances==2:
                score=20
            elif chances==1:
                score=10
        
            if player_guess in alreadysaid:
                print("You've already guessed that")
            
                                  
            if player_guess in word_to_guess:    
                alreadysaid+=player_guess
                board = "".join([char if char  in alreadysaid else "*" for char in word_to_guess])
                if board==word_to_guess:
                    guessed= True
                    print("CORRECT GUESS!")
            else:                    
                if player_guess in alreadysaid:
                    chances+=1
                alreadysaid+=player_guess
                chances -=1
                print("Nope.",chances,"guesses left")
            print(board)
            if chances==0:
                score=0
                print("YOU LOSE\nCorrect word is\t",word_to_guess)
                hs_h.append(score)
            elif chances>0 and board == word_to_guess:
                print("CONGRATULATIONS {0} you have guessed the word correctly\nYour score is {1} ".format(name,score))
                hs_h.append(score)
            
class Hangman(Play_h,Highscores_h):
    def __init__(self):
        ch1='y'
        while(ch1=='y'):
            choice2=int(input("1.Play Hangman\n2.Highscores of Hangman\n3.Go Back \n"))
            if choice2 == 1:
                super().playing()
            elif choice2 == 2:
                super().highscore()
            elif choice2 ==3:
                Basic.__init__(self)
            ch1=input("Do you want to continue in hangman game (y/n)?\n")
             
hs_q=[]
names_q=[]
class Play:
    def playing(self):
        name=input("Enter you name\t\t")
        names_q.append(name)
        global score
        score=0
        print("Q1-We can't make an object of ")
        q1=input("\ta.Base class\n\tb.Abstract class\n\tc.Parent class\n\td.Both a & c\n")
        a1=("b")
        if q1==a1:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a1))        
        print("Q2-Constructors are used to ")
        q2=input("\ta.Initialize a newly created object\n\tb.Free memory\n\tc.To build a user interface\n\td.To create a sub class\n")
        a2=("a")
        if q2==a2:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a2))
        print("Q3-The process by which one object can acquire the properties of another object is")
        q3=input("\ta.Polymorphism\n\tb.Inheritance\n\tc.Encapsulation\n\td.Abstraction\t\n")
        a3=("b")
        if q3==a3:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a3))
        print("Q4-By default everything in java is")
        q4=input("\ta.Protected\n\tb.Private\n\tc.Public\n\td.None of these\n")
        a4=("c")
        if q4==a4:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a4))
        print("Q5-Pointers to object of the ____ class are type compatible with pointers of the ____ class")
        q5=input("\ta.Base , Abstract\n\tb.Derived , Abstract\n\tc.Derived , Base\n\td.Base , Derived\n")
        a5=("c")
        if q5==a5:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a5))
        print("Q6-The keyword private restricts the access of class or struct members to")
        q6=input("\ta.Const functions\n\tb.Static functions\n\tc.Member functions\n\td.Clients\n")
        a6=("c")
        if q6==a6:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a6))
        print("Q7-An object that has more than one form is reffered to as")
        q7=input("\ta.Abstract class\n\tb.Interface\n\tc.Inheritance\n\td.Polymorphism\n")
        a7=("d")
        if q7==a7:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a7))
        print("Q8-In python double underscore before any data member means that the data member is ")
        q8=input("\ta.Private\n\tb.Protected\n\tc.Public\n\td.None of these\n")
        a8=("a")
        if q8==a8:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a8))
        print("Q9-Composition have a ____ relationship between two classes")
        q9=input("\ta.'Kind of'\n\tb.'Consist of'\n\tc.'Has a'\n\td.'Part of'\n")
        a9=("b")
        if q9==a9:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a9))
        print("Q10-Choosing functions in the normal way during compilation is called")
        q10=input("\ta.Early binding\n\tb.Static binding\n\tc.Dynamic binding \n\td.Both a & b\n")
        a10=("d")
        if q10==a10:
            score+=1
            print("Correct answer\n")
        else:
            print("Incorrect answer\nCorrect option is {0}".format(a10))
        if score>5:
            print("Congratulations {0},You have completed the quiz\nYour score is {1}".format(name,score))
            hs_q.append(score)
        else:
            print("Poor performance {0},You have completed the quiz\nYour score is {1}".format(name,score))
        hs_q.append(score)
class Highscores:
    def highscore(self):
        n_q=str(len(names_q))
        h_q=str(len(hs_q))
        print("Highscores are")
        print('Names \t\t\t Scores')
        for n_q, h_q in zip(names_q, hs_q):
            print(n_q ,'\t\t\t' ,h_q)
class Quiz(Play,Highscores):
    def __init__(self):
        ch1='y'
        while(ch1=='y'):
            choice2=int(input("1.Take Quiz\n2.Highscores of Quiz \n3.Go Back\n"))
            if choice2 == 1:
                super().playing()
            elif choice2 == 2:
                super().highscore()
            elif choice2 ==3:
                Basic.__init__(self)
            ch1=input("Do you want to continue in Quiz(y/n)?\n")
class Basic(Quiz,Hangman):
    def __init__(self):
        ch='n'
        while(ch=='n'):
            print("\n\t\tWELCOME TO THE QUIZ\n")
            print("\nChoose from the following options\n")
            choice=int(input("1.Quiz\n2.Hangman\n3.Exit\n"))
            if choice == 1:
                Quiz.__init__(self)
                                    
                  
            elif choice == 2:
                Hangman.__init__(self)
                
            elif choice == 3:
                exit
            ch=input("Are you sure you want to exit? (y/n)\n")
p1=Basic()

