import random 

def create_array():
  return random.sample(range(1, 20001), 20000) 

array = create_array()
print(array)