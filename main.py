def display_parameter(parameter):
    print(parameter)

def display_name_check(name):
    list_nom = ["sanogo", "coulibaly"]
    if name in list_nom:
        print(name)
    else:
        print("Erreur: Vous n'avez fourni un nom acceptable!")
def display_complete_username(nom, prenom):
    print("Mon nom est {0} et mon prénom est {1}.".format(nom, prenom))

def get_age(annee):
    return 2021 - annee

def suis_je_vieille(age):
    if age > 18:
        return "vieille"
    else:
        return "jeunette"

if __name__ == '__main__':
    #print('PyCharm12334432')
    display_parameter("""def display_parameter(parameter):
    print(parameter) """)
    display_complete_username("Coulibaly", "Tchalagnon Alimata")
    print("Mon âge est {0} ans et je pense que je suis une {1}.".format(get_age(1986), suis_je_vieille(get_age(1986))))
