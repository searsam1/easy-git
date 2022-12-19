# By AS
import math
def fact(n):
  """
  n! = n × (n-1) × (n-2) × …1  
  Return n!
  example: n = 3
    n! = 1 * 2 * 3
    n! = 6 
  """
  prod = 1
  for i in range(2, n+1):
    prod *= i
  return prod 

def main():
  for i in range(100):
    assert math.factorial(i) == fact(i)
  print("Tests Passed")

if __name__ == "__main__":
  main()
