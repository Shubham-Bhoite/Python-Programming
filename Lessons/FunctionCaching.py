from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(4)
  return n*10
    

print(fx(15))
print("done for 15")
print(fx(5))
print("done for 5")
print(fx(7))
print("done for 7")
print("Thank You")

