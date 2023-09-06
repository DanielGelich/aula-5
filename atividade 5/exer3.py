
def converter_massa_lunar(massa_terrestre):
  return massa_terrestre / 6

def converter_distancia_marte(distancia_terrestre):
  return distancia_terrestre * 1.028

def test_converter_massa_lunar():
  assert converter_massa_lunar(10) == 1.6666666666666667

def test_converter_distancia_marte():
  
  assert converter_distancia_marte(1000) == 1028

massa_lunar = converter_massa_lunar(10)
print(massa_lunar) 

distancia_marte = converter_distancia_marte(1000)
print(distancia_marte)