import random as r

def dice(min, max):
  return r.randrange(min, max)


def roll():
  number = (dice(1,7))
  if number == 1:
    print("-----")
    print("--0--")
    print("-----")
  elif number == 2:
    print("----0")
    print("-----")
    print("0----")  
  elif number == 3:
    print("----0")
    print("--0--")
    print("0----") 
  elif number == 4:
    print("0---0")
    print("-----")
    print("0---0") 
  elif number == 5:
    print("0---0")
    print("--0--")
    print("0---0") 
  elif number == 6:
    print("0---0")
    print("0---0")
    print("0---0")    
  
def main():

  answer = input("Do you want to roll a dice?""\n")
  print("\n")
  if answer == "yes":
    roll()
    print("\n")
    main()
  elif answer == "Yes":
    roll()
    print("\n")
    main()
  else:
    print("bye") 

# call the function
main()
