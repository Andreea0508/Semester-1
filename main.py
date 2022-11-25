#1.Easy to use;More compact;Can be added more information

#2. 


######2
#numbers=input(" type 5 numbers divided by comma ")


#####3
#file=open("numList.csv","w")
#file.write(input(" type 5 numbers divided by comma "))
#file.close()

# ####4
#file=open("numList.csv","r")
# dataIn=file.read()
 #file.close()

 #print(dataIn)

# ####5
# numbers=dataIn.split(",")
 #numbers=[int(item) for item in numbers]

######6
# print(numbers)

# ######7
# numbers.sort()

######8
# print(numbers)

# #####9
# print(numbers[0])
# print(numbers[-1])


# ######10
# import statistics
# average=statistics.mean(numbers)
# print(average)

######11

# names=[]

#####12
 #pets=[]

####13-14
# names=input(" type the name of the owners, divided by a comma ")
 #names=names.split(",")

# pets=input(" type the numbers of the pets for each owner, divided by a comma ")
# pets=pets.split(",")
# pets=[int(item) for item in pets]

# #########15

 #import matplotlib.pyplot as ply

# ply.bar(names,pets)
# ply.xlabel("owners")
 #ply.xlabel("number of pets")
 #ply.show()
######  Q3. 

##Anagrams are words that contain the same letters. Eg. car and arc are anagrams of each other 

 

def is_anagram(w1, w2): 

  if sorted(w1) == sorted(w2): 

    return True 

  else: 

    return False 

 

word1 = input("Enter the first word:") 

word2 = input("Enter the second word:") 



 

##Test whether the sorted strings are the same as each other 

##If the sorted strings are the same as each other then they must be anagrams 

 

if(sorted(word1) == (sorted(word2))):

  
  print("YES")
  
  print(word1, "is anagram to" ,word2) 
else:
  print(word1, "is not anagram of" ,word2)



  phrase = input("Enter a phrase:")

if(sorted(phrase)):
  print(word1,"is not anagram of" ,phrase)

  print(word2, "is not anagram of" ,phrase)




  

