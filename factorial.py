# By AS
def factorial(n):
  """
  Return n! (n factorial): 
  example: n = 3
    n! = 1 * 2 * 3
    n! = 6 
  """
  prod = 1
  for i in range(2, n+1):
    prod *= i
  return prod 

def main():
  assert factorial(3) == 6
  print("Tests Passed")

if __name__ == "__main__":
  main()
