n_pokebolas = int(input())

n_ratatas = int(input())
pokebolas_ratata = 1
if n_pokebolas - (n_ratatas * pokebolas_ratata) >= 0:
    ratatas_capturados = n_ratatas
    n_pokebolas -= (n_ratatas * pokebolas_ratata)
else:
    ratatas_capturados = n_pokebolas // pokebolas_ratata
    n_pokebolas -= (ratatas_capturados * pokebolas_ratata)

n_eevees = int(input())
pokebolas_eevee = 5
if n_pokebolas - (n_eevees * pokebolas_eevee) >= 0:
    eevees_capturados = n_eevees
    n_pokebolas -= (n_eevees * pokebolas_eevee)
else:
    eevees_capturados = n_pokebolas // pokebolas_eevee
    n_pokebolas -= (eevees_capturados * pokebolas_eevee)

n_pikachus = int(input())
pokebolas_pikachu = 10
if n_pokebolas - (n_pikachus * pokebolas_pikachu) >= 0:
    pikachus_capturados = n_pikachus
else:
    pikachus_capturados = n_pokebolas // pokebolas_pikachu
n_pokebolas -= (pikachus_capturados * pokebolas_pikachu)

n_bulbasaur = int(input())
pokebolas_bulbasaur = 25
if n_pokebolas - (n_bulbasaur * pokebolas_bulbasaur) >= 0:
    bulbasaur_capturados = n_bulbasaur
else:
    bulbasaur_capturados = n_pokebolas // pokebolas_bulbasaur
n_pokebolas -= (bulbasaur_capturados * pokebolas_bulbasaur)

n_squirtle = int(input())
pokebolas_squirtle = 50
if n_pokebolas - (n_squirtle * pokebolas_squirtle) >= 0:
    squirtle_capturados = n_squirtle
else:
    squirtle_capturados = n_pokebolas // pokebolas_squirtle
n_pokebolas -= (squirtle_capturados * pokebolas_squirtle)

n_charmanders = int(input())
pokebolas_charmander = 100
if n_pokebolas - (n_charmanders * pokebolas_charmander) >= 0:
    charmander_capturados = n_charmanders
else:
    charmander_capturados = n_pokebolas // pokebolas_charmander
n_pokebolas -= (charmander_capturados * pokebolas_charmander)

print(n_pokebolas)
print(f'''Rattata {ratatas_capturados}
Eevee {eevees_capturados}
Pikachu {pikachus_capturados}
Bulbasaur {bulbasaur_capturados}
Squirtle {squirtle_capturados}
Charmander {charmander_capturados}''')