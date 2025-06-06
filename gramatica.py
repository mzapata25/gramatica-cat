import nltk
from nltk import CFG

# La gramática que será la base del programa
gramatica_cat = CFG.fromstring("""
    F -> Suj0 Pre Suj0 | Suj0 Pre | Pre Suj0
    Suj0 -> Suj | Suj Conj
    Suj -> ProN | Ar No | No
    Pre -> 'tinc' | 'es' | 'soc' | 'menjo' | 'tens' | 'ets' | 'menges' | 'te' | 'menja'
    ProN -> 'jo' | 'tu' | 'ell' | 'ella'
    Ar -> 'un' | 'una' | 'uns' | 'unes' | 'el' | 'la' | 'els' | 'les'
    No -> 'cotxe' | 'finestra' | 'pomes' | 'monedes' | 'estudiant' | 'llibres' | 'taronges'
    Conj -> 'i' F | 'i' Suj0
""")

# Este será el parser con base a la gramática
cat_parser = nltk.ChartParser(gramatica_cat)



frases = [
    "jo menjo",
    "jo tinc un cotxe",
    "jo menjo pomes",
    "jo tinc unes monedes",
    "tu ets estudiant",
    "jo tinc finestra una",
    "ell te uns libros",
    "ell te uns llibres",
    "ella menja pomes i taronges",
    "jo soc estudiant i tinc llibres i tinc un cotxe",
    "ella cotxe es",
    "ell finestra"
]

print("Árbol de la gramática del catalán")
print("------------")
print("El test de manera automática, pulse 1 para desplegarlo")
print("------------")

while True:
        try:
            comienzo = int(input("Pulse 1 para empezar: "))
        except ValueError:
            print("\nPor favor, pulse 1.\n")
            continue
        if comienzo <= 0 or comienzo >= 2:
            print("\nPor favor, pulse 1.\n")
            continue
        else:
            break

if comienzo == 1:
  for frase in frases:
    try:
      tokens = frase.split()
      parsed_trees = list(cat_parser.parse(tokens))
      if parsed_trees:
          for arbol in parsed_trees:
              print("\nLa frase" + "\033[1m" + frase + "\033[0m" + " tiene este árbol: ")
              arbol.pretty_print()
              print()
      else:
          print("La frase " + "\033[1m" + frase + "\033[0m" + " no es correcta. \n" +
                "No se ha podido parsear de acuerdo a la gramática.\n")
    except Exception as e:
        print("Ha ocurrido un error:", e)
