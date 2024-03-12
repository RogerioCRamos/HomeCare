from BackMaterial import *


qtatual = consulta_quantidade_material(1234, "frutaina")

if qtatual < 3:
    print('tudo certo')
else:
    print('tudo errado')