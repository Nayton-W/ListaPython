from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('O Ângulo de {} tem o Seno de {:.2f}'.format(ang, seno))
print('O Ângulo de {} tem o Cosseno de {:.2f}'.format(ang, cosseno))
print('O Ângulo de {} tem a Tangente de {:.2f}'.format(ang, tangente))
