# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.



def calcular_area_base ():
    
    raio = float(input("Digie o raio do cílindro: "))
    area = raio * raio * 3.14

    return area

aa= calcular_area_base()
print(aa)
def calcular_volume_cilindro ():
    
    altura=float(input("digite a altura do seu cilindro: "))
    volume = aa * altura

    return volume

vo = calcular_volume_cilindro()

print(vo)
