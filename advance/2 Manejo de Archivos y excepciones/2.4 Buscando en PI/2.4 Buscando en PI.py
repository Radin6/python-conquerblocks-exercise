'''BUSCANDO EN PI
Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y
en que posición. Puedes usar find()).
Puedes usar el archivo pi_10000.txt'''

def search_on_pi(filename, number):

    with open(filename) as file:
        content = file.read()
        _search = content.find(number)
    
    return _search
        
numberToSearch = input("Insert number to search for: ")

search = search_on_pi("pi_10000.txt", numberToSearch)

if search == -1:
    print(f"'{numberToSearch}' is no included")
else:
    print(f"'{numberToSearch}' is on the position {search}")