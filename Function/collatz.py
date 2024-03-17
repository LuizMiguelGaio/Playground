#Sequencia de collatz

def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3 * number +1


if __name__ == '__main__':
    #number = int(input("Digite um numero."))
    while True:
        number = int(input("Digite um numero."))
        while number != 1:
            number =  collatz(number)
            print(number)
        break

