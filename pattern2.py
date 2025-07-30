#patternn printing2
n=int(input()
    )
for row in range(n):
      for num in range(n):
          if num<=row:
              print(num+1, end="")
          else:
              break                      
      print("")
       
for currRow in range(n):
     for currNum in range(n):
         if(currNum<n-(currRow+1)):
            print(" ",end=" ")
         else:
            print("*", end=" ")
     print("")
                   