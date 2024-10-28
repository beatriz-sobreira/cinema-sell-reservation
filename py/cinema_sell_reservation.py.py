# Programa feito em equipe: Beatriz Sobreira, Brenda Evelyn, Gisliane Kelly e Maria Eduarda

A1 = A2 = A3 = A4 = A5 = True
locador1 = locador2 = locador3 = locador4 = locador5 = ">>ASSENTO LIVRE<<"
contador = 0

def poltrona():
    escolha_poltrona = input("\nEscolha uma poltrona disponível (A1, A2, A3, A4, A5): ").upper()
    return escolha_poltrona

def nome():
    nome_locador = input("\nDigite o nome do locador: ")
    return nome_locador

def reservas():
    global A1, A2, A3, A4, A5
    global locador1, locador2, locador3, locador4, locador5
    
    escolha = poltrona()
    
    if escolha == "A1":
         if A1:
            locador1 = nome()
            print("Reserva concluída! Poltrona: A1 / Nome: {}".format(locador1))
            A1 = False
            return True
         else:
            print("Poltrona já foi reservada por {}".format(locador1))
            return False
    elif escolha == "A2":
    
     if A2:
            locador2 = nome()
            print("Reserva concluída! Poltrona: A2 / Nome: {}".format(locador2))
            A2 = False
            return True
     else:
            print("Poltrona já foi reservada por {}".format(locador2))
            return False

    elif escolha == "A3":
        if A3:
            locador3 = nome()
            print("Reserva concluída! Poltrona: A3 / Nome: {}".format(locador3))
            A3 = False
            return True
        else:
            print("Poltrona já foi reservada por {}".format(locador3))
            return False
        
    elif escolha == "A4":
        if A4:
            locador4 = nome()
            print("Reserva concluída! Poltrona: A4 / Nome: {}".format(locador4))
            A4 = False
            return True
        else:
            print("Poltrona já foi reservada por {}".format(locador4))
            return False

    elif escolha == "A5":
        if A5:
            locador5 = nome()
            print("Reserva concluída! Poltrona: A5 / Nome: {}".format(locador5))
            A5 = False
            return True
        else:
            print("Poltrona já foi reservada por {}".format(locador5))
            return False

    else:
        print("Poltrona inválida")
        return False
    
def menu():
    global contador
    global locador1, locador2, locador3, locador4, locador5
    print("Esse é o menu principal. Digite o número da opção desejada para utilizar o sistema:\n\n[1] para >>VISUALIZAR O CATÁLOGO DE FILMES<<\n[2] para >>RESERVAS<<\n[3] para >>CANCELAMENTO DE RESERVA<<\n[4] para >>VISUALIZAR A DISPONIBILIDADE DO CINEMA<<\n[5] para >>SAIR<<")
    escolha_menu = int(input("\nA sua escolha é: "))

    if escolha_menu == 1:
        print(print("\nEsse é o >>CATÁLOGO DE FILMES<<\n\n1. Aos DOMINGOS, o cinema transmite: >>ANATOMIA DE UMA QUEDA<<\nGênero: Crime/Thriller\nSinopse: Durante o último ano, Sandra, uma escritora alemã, e Samuel, seu marido francês, viveram juntos com Daniel, o filho de 11 anos do casal, em uma pequena e isolada cidade nos Alpes. Quando Samuel é encontrado morto, a polícia passa a tratar o caso como um suposto homicídio, e Sandra se torna a principal suspeita.\n\n2. Nas SEGUNDAS-FEIRAS, o cinema transmite: >>OLDBOY<< \nGênero: Thriller/Ação \nSinopse: Dae-Su é raptado e mantido em cativeiro por 15 anos num quarto de hotel, sem qualquer contato com o mundo externo. Quando ele é inexplicavelmente solto, descobre que é acusado pelo assassinato da esposa e embarca numa missão obsessiva por vingança.\n\n3. Nas TERÇAS-FEIRAS, o cinema transmite: >>O MENINO E A GARÇA<< \nGênero: Fantasia/Aventura \nSinopse: Mahito, um menino de 12 anos, luta para se estabelecer em uma nova cidade após a morte de sua mãe. Quando uma garça falante conta para Mahito que sua mãe ainda está viva, ele entra em uma torre abandonada em busca dela, o que o leva para outro mundo.\n\n4. Nas QUARTAS-FEIRAS, o cinema transmite: >>ADORÁVEIS MULHERES<<\nGênero: Romance/Drama\nSinopse: Nos anos seguintes à Guerra de Secessão, Jo March e suas duas irmãs voltam para casa quando Beth, a tímida irmã caçula, desenvolve uma doença devastadora que muda para sempre a vida delas.\n\n5. Nas QUINTAS-FEIRAS, o cinema transmite: >>DUNA<<\nGênero: Ficção científica/Aventura\nSinopse: Paul Atreides é um jovem brilhante, dono de um destino além de sua compreensão. Ele deve viajar para o planeta mais perigoso do universo para garantir o futuro de seu povo.\n\n6. Nas SEXTAS-FEIRAS, o cinema transmite: >>ATÉ O ÚLTIMO HOMEM<<\nGênero: Guerra/Drama \nSinopse: Acompanhe a história de Desmond T. Doss, um médico do exército americano que, durante a Segunda Guerra Mundial, se recusa a pegar em armas. Durante a Batalha de Okinawa ele trabalha na ala médica e salva cerca de 75 homens.\n\n7. Aos SÁBADOS, o cinema transmite: >>A SOCIEDADE DA NEVE<<\nGênero: Aventura/Thriller\nSinopse: Em 1972, um voo vindo do Uruguai colide com uma geleira nos Andes. Apenas 29 dos seus 45 passageiros sobreviveram ao acidente. Presos em um dos ambientes mais hostis do planeta, eles são forçados a lutar pelas suas vidas."))
        escolha()

    if escolha_menu == 2:
        if contador < 5:
            pessoas = int(input("\nVamos iniciar o processo. Quantas poltronas você deseja reservar? Lembrando que a capacidade máxima do cinema são >>5 POLTRONAS<<: "))
            if contador + pessoas > 5:
                print("O número de pessoas ultrapassa a capacidade máxima. Você pode reservar para até {} pessoas.".format(5 - contador))
                escolha()
            else:
                reserva_necessarias = pessoas

                while reserva_necessarias >  0:
                    if reservas():
                        contador += 1
                        reserva_necessarias -=1
                escolha()
        else:
            print("\n>>>>>>>CINEMA CHEIO.<<<<<<<< \n Não há poltronas disponíveis.")
            escolha() 
    
    if escolha_menu == 3:
        cancelamento()
        escolha()

    if escolha_menu == 4:
        print("\nDisponibilidade dos assentos: \nA1 está com {}\nA2 está com {}\nA3 está com {}\nA4 está com {}\nA5 está com {}".format(locador1, locador2, locador3, locador4, locador5))
        escolha()

    if escolha_menu == 5:
        print("\nObrigada por utilizar o sistema! \n>>ENCERRANDO A APLICAÇÃO...<<")

def escolha():
    escolha_menu = input("\n>>Deseja voltar ao menu principal? [S]/[N]<<: ")
    if escolha_menu in "Ss":
        menu()
    else:
        print("\nObrigada por utilizar o sistema! \n>>ENCERRANDO A APLICAÇÃO...<<")

def cancelamento():
    global A1, A2, A3, A4, A5
    global locador1, locador2, locador3, locador4, locador5
    global contador
    
    cancelamento = input("Deseja fazer o cancelamento da reserva de qual cadeira? ").upper()
    
 
    
    if cancelamento == "A1":
        if not A1:
            locador1 = ">>ASSENTO LIVRE<<"
            contador -=1
            print("Cancelamento da poltrona A1 concluído.")
            A1 = True
            escolha()
            return True 
        else:
            print("Não há reservas nessa poltrona.")
    
    if cancelamento == "A2":
        if not A2:
            locador2 = ">>ASSENTO LIVRE<<"
            contador -=1
            print("Cancelamento da poltrona A2 concluído.")
            A2 = True
            escolha()
            return True
        else:
            print("Não há reservas nessa poltrona.")
    
    if cancelamento == "A3":
        if not A3:
            locador3 = ">>ASSENTO LIVRE<<"
            contador -=1
            print("Cancelamento da poltrona A3 concluído.")
            A3 = True
            escolha()
            return True 
        else:
            print("Não há reservas nessa poltrona.")
    
    if cancelamento == "A4":
        if not A4:
            locador4 = ">>ASSENTO LIVRE<<"
            contador -=1
            print("Cancelamento da poltrona A4 concluído.")
            A4 = True
            escolha()
            return True 
        else:
            print("Não há reservas nessa poltrona.")
    
    if cancelamento == "A5":
        if not A5:
            locador5 = ">>ASSENTO LIVRE<<"
            contador -=1
            print("Cancelamento da poltrona A5 concluído.")
            A5 = True
            escolha()
            return True 
        else:
            print("Não há reservas nessa poltrona.")
    

print("\n>>INICIANDO O SISTEMA DE RESERVAS<<")
print("\nCarregando o sistema... \n\n10%: █▒▒▒▒▒▒▒▒▒ \n20%: ██▒▒▒▒▒▒▒▒ \n30%: ███▒▒▒▒▒▒▒ \n40%: ████▒▒▒▒▒▒ \n50%: █████▒▒▒▒▒ \n60%: ██████▒▒▒▒ \n70%: ███████▒▒▒ \n80%: ████████▒▒ \n90%: █████████▒ \n100%: █████████ \n\nBem-vindo ao cinema! Prepare-se para uma experiência incrível e desfrute do seu filme!\n")

menu()