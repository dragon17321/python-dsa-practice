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
       