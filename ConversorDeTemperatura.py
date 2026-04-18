
def celsius_p_fah(celsius):
    return(celsius * 9/5) + 32

def fah_p_celsius(fahrenheit):
    return(fahrenheit -32) * 5/9

def menu():
    print("Conversor de graus!")
    print("Escolha uma das opções abaixo:")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converter Fahrenheit para Celsius")
    print("3 - Sair")

def conversor_graus():
    while True:
        menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            celsius = float(input("Digite a temperatura de Celsius: "))
            fahrenheit = celsius_p_fah(celsius)
            print(f"{celsius:.2f}Cº é equivalente a: {fahrenheit:.2f}Fº")
            print("Pressione Enter para finalizar!")
            input()

        elif opcao == "2":
            fahrenheit = float(input("Digite a temperatura de Fahrenheit: "))
            celsius = fah_p_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}Fº é equivalente a: {celsius:.2f}Cº")
            print("Pressione Enter para finalizar!")
            input()
        elif opcao == "3":
            print("Saindo do programa...")
            print("Pressione Enter para finalizar!")
            input()
        
        else:
            print("Comando inválido!")
            print("Escolha uma das opções (1, 2, 3)")

if __name__ == "__main__":
    conversor_graus()