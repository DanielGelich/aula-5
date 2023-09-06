## Teste 1 

def test_vetor_size():
  numbers = create_array()

  quantity = len(numbers)
  assert quantity == 20000

## Teste 2

def test_is_sorted():
  numbers = create_array()

  assert all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))