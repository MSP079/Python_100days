#Data types
print("Hello" [0])  #substring
print("Hello"[4])
print("Hello"[-1])

#String
print("123"+"456")
      
#interger = whole number
print(123 + 456)

#Larger number
print(123_456_789)
print(123456789)


#Float = Floating point number
print(3.14)

#Boolean
print(True) 
print(False)

print(len("Hello"))
print(type("hello"))
print(type(123))
print(type(3.14))
print(type(True))


#Type casting
print(int("123")+int("345"))
#print(int("abd")+int("fgh"))  #Error ValueError: invalid literal for int() with base 10: 'abd'

#Q: print("Number of letters in your name: "+  len(input("Enter you name"))) #TypeError: can only concatenate str (not "int") to str
#Ans: print("Number of letters in your name: ", len(input("Enter you name")))
#name_of_the_user = input("Enter your name")
#length_of_name = len(name_of_the_user)
#print(length_of_name)
#print(type("Number of letters in your name: ")) #String
#print(type(length_of_name)) #int
#Ans: print("Number of letters in your name: "+str(len(input("Enter you name"))))


#Mathematical operations
print("My age: " + str(12))
print(123+456)
print(7-3)
print(3*2)
print(6/2)
print(type(6//2), (6//2))
print(6/3) #give float number
print(5//3) #give round to neareat interger
print(2**6)
print(3*(3+(3/3-3)))
print(3*(3+3)/3-3)


#user scores a point
score = 0
score +=1
print(score)


# f-string

print("Your score is " + str(score))

score1 = 0
height1 = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. Your are winning is= {is_winning}")