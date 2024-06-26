def recomendar_planos(consumo_medio, PLANO_ESSENCIAL, PLANO_PRATA, PLANO_PREMIUM):
    if consumo_medio <= PLANO_ESSENCIAL:
        print("Plano Essencial Fibra - 50Mbps")
        
    elif PLANO_ESSENCIAL < consumo_medio <= PLANO_PRATA:
        print("Plano Prata Fibra - 100Mbps")
        
    elif consumo_medio > PLANO_PRATA:
        print("Plano Premium Fibra - 300Mbps")
    
    else:
        print("digite um valor valido!")

def main():
    PLANO_ESSENCIAL = 10
    PLANO_PRATA = 20
    PLANO_PREMIUM = 21

    while True:
        consumo_medio = float(input())
        if consumo_medio <= 0:
            print("Digite um valor valido")
            break
        else:
             recomendar_planos(consumo_medio, PLANO_ESSENCIAL, PLANO_PRATA, PLANO_PREMIUM)
        break
    else:
        print("Você não digitou nada. Por favor, insira um valor.")
main()