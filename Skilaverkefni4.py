# Skilaverkefni 4
# Gísli Hrafn Halldórsson & Brynhildur

# þurfum að gera forrit sem tekur við 4 mismunandi skipunum frá notenda
# 1. þau inputa skjal og sýna kjördæmi og kosningabærra manna
# 2. sýna flokkanaa
# 3. sýna niðurstöður
# 9. forritið hættir


def get_choice():
    user_input = int(input())
    dick = {}

    if user_input == 1:
        file_name = input()
        # If dick dictionary is empty
        if bool(dick) == False:
            # Then it gets that gosh darn data from that file and stuffs it in the dict! ☺
            dick = read_file_contents(file_name)

        show_constituencies_1(dick)
    elif user_input == 2:
        show_parties_2()
    elif user_input == 3:
        show_results_3()
    elif user_input == 9:
        quit_9()


def read_file_contents(file_name):
    """Here we make a function to open the file so we dont have to open it seperately"""
    cock = {}
    try:
        with open(file=file_name, mode="r") as file:
            file_contents_list = file.readlines()
            for line in file_contents_list:
                keyy, valuee = line.split(";")
                cock[keyy] = valuee

    except FileNotFoundError:
        print("File not found!")
        return {}  # Returns an empty dict if no file is found


def table_time(file_name):
    read_line = open(file_name, "r")
    template = "{0:<10}{1:10}"
    print(template.format())


def show_constituencies_1(file_name):
    read_line = open(file_name, "r")
    template = "{0:<10}{1:10}"
    print(template.format())


def show_parties_2():
    pass


def show_results_3():
    pass


def quit_9():
    pass


def main():
    get_choice()


main()


# HAAAAAAAAAA
# land = int(input("Lansfjarhaed: "))
# ars = 11.3
# lant = 6300
# faer = 405

# hofudstoll = land + lant

# print("Lansfjarhead", land, "kr")
# print("Arsvextir: ", ars, "%")
# print("Lantokugjald: ", lant, "kr")
# print("faerslegjuald: ", faer, "kr")

# afb = round(hofudstoll / 12)
# eftir = hofudstoll -afb
# vex = round((hofudstoll * 0.113)/12)

# vextir_samtals = vex
# afborgun = afb * 12
# faerslugjald = faer * 12
# greidsla = afb + vex + faer

# print("Lanid thitt skiptist svona: ")
# template = "{0:<10}{1:10}{2:>10}{3:>15}{4:>12}{5:>18}{6:>15}"

# print(template.format("#", "Hofudstoll", "Afborgun", "Eftirstöðvar", "Vextir", "Faerslugjald", "Greidsla"))

# for x in range(1, 13):
#     print(template.format(x, hofudstoll, afb, eftir, vex, faer, greidsla))
#     hofudstoll = hofudstoll - afb
#     eftir = hofudstoll - afb
#     vex = round((hofudstoll * 0.113)/12)
#     vextir_samtals = vextir_samtals + vex
#     greidsla = afb + vex + faer


# summ = vextir_samtals + faerslugjald + afborgun

# print("Samtals afborgun: ", afborgun)
# print("Samtals vextir: ", vextir_samtals)
# print("Samtals faerslugjöld: ", faerslugjald)
# print("Samtals endurgreiðsla: ", summ)
# {}
