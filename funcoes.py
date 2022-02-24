from os import system
from time import sleep


def menu_inicial():
    while True:
        try:
            print("------Menu de opções------\n")
            print("Opção 1: Atualiza banco de dados do antivírus;")
            print("Opção 2: Executa varredura no diretório principal;")
            print("Opção 3: Encerra o programa.\n")
            opc = int(input("Digite sua opção e tecle ENTER: "))
            system("clear")
            if opc == 1:
                system("sudo systemctl stop clamav-freshclam")
                system("sudo freshclam")
                system("sudo systemctl start clamav-freshclam")
                print("\nBanco de dados atualizado. ", end='')
                while True:
                    try:
                        print("Escolha uma opção:\n")
                        print("Opção 1: Retorna ao menu inicial;")
                        print("Opção 2: Encerra o programa.\n")
                        opc_int = int(input("Digite sua opção e tecle ENTER: "))
                        system("clear")
                        if opc_int == 1:
                            menu_inicial()
                        elif opc_int == 2:
                            print("Obrigado por utilizar o sistema. Aguarde 5 segundos pelo seu encerramento.")
                            sleep(5)
                            exit(0)
                        else:
                            print("Opção inválida. Tente novamente!\n")
                    except ValueError:
                        system("clear")
                        print("Entrada inválida. Tente novamente!\n")
            elif opc == 2:
                system("sudo clamscan -r $HOME")
                print("Varredura completa.")
                aux_int = True
                while aux_int:
                    try:
                        opc_int = int(input("Digite 1 e tecle ENTER para encerrar o programa: "))
                        system("clear")
                        if opc_int == 1:
                            print("Obrigado por utilizar o sistema. Aguarde 5 segundos pelo seu encerramento.")
                            exit(0)
                        else:
                            print("Opção inválida. Tente novamente!\n")
                    except ValueError:
                        system("clear")
                        print("Entrada inválida. Tente novamente!\n")
            elif opc == 3:
                print("Obrigado por utilizar o sistema. Aguarde 5 segundos pelo seu encerramento.")
                sleep(5)
                exit(0)
            else:
                print("Opção inválida. Tente novamente!\n")
        except ValueError:
            system("clear")
            print("Entrada inválida. Tente novamente!\n")
