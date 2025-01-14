"""Mad Libs"""

print("\nBienvenido a Mad Libs, debes completar los espacios en blanco ¿Comenzamos?\n", flush=True)

print("Ada Lovelace fue una _______ matemática que logró _______ conceptos fundamentales para la programación. A través de su visión, ideó algoritmos que pudieron ser implementados en las primeras máquinas de cálculo, y sus estudios sobre los mecanismos de la computación inspiraron a futuras generaciones de científicos y _______.\n", flush=True) 

adjective = input("Escribe un adjetivo: ")
verb = input("Escribe un verbo: ")
plural_noun = input("Escribe un sustantivo (plural): ")

madlib = f"\nAda Lovelace fue una {adjective} matemática que logró {verb} conceptos fundamentales para la programación. A través de su visión, ideó algoritmos que pudieron ser implementados en las primeras máquinas de cálculo, y sus estudios sobre los mecanismos de la computación inspiraron a futuras generaciones de científicos y {plural_noun}.\n"

print(madlib)