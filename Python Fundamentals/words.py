'''2.2: Occurance of words'''

#  Get an arbitrary piece of text from internet
#  Create a python script that reads the complete tekst with s = input()
s: str = input('Enter the text: ')

#  Convert to lowercase and remove dots and commas
text: str = s.lower().replace('.', '').replace(',', '')

#  Split the text into words with text.split()
#  Create a set of unique words
words: set[str] = set(text.split())

#  For each unique word count the number of occurances
d: dict[str, int] = {}
for word in words:
    #  Store the results in a dictionary: d[word] = n
    d[word] = text.count(word)

#  Print the results: for word, n in d.items()
for word, n in d.items():
    print(word, ':', n)

# Output:
# > python .\words.py
# Enter the text: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Suspendisse ac nisi porttitor, feugiat nunc et, aliquam dolor. Vivamus
# sodales venenatis lorem et porta. Quisque tellus est, bibendum quis
# hendrerit in , egestas vel libero. Aliquam suscipit nisl vitae mauris
# rutrum elementum. Suspendisse sed dignissim nulla. Donec pharetra
# consectetur velit, id tincidunt ligula tincidunt vel. Curabitur aliquet
# orci magna, vel tristique mi convallis eu. Fusce pretium posuere leo
# eget tincidunt. Suspendisse pellentesque arcu quis metus varius
# ultricies. Nunc viverra, enim ultricies consequat sagittis, dui est
# vestibulum augue, at tempor enim diam ac justo. Vestibulum ornare et
# sem eu convallis. Curabitur imperdiet consequat nisi sit amet
# scelerisque. Mauris placerat lobortis metus, quis pharetra nibh viverra
# ut. Curabitur sit amet luctus metus, vitae laoreet purus. Phasellus
# mattis tincidunt ipsum, eu imperdiet augue fermentum nec. Donec mollis
# turpis enim, in lobortis quam suscipit ornare. Donec vulputate bibendum
# felis ac congue. Aliquam efficitur eu lorem et tincidunt. Sed a justo
# vitae dui aliquet tincidunt. Ut dapibus urna nisl, nec malesuada lectus
# accumsan vitae. Proin non rhoncus odio. Suspendisse diam diam, malesuada
# id nisl in , pretium malesuada nunc. Nunc rutrum justo arcu, in
# scelerisque tellus blandit in . Ut ligula lectus, maximus in ante eu,
# accumsan suscipit purus. In scelerisque est mauris, ut imperdiet dolor
# fermentum vel. Curabitur metus leo, malesuada nec mollis quis, blandit
# in nulla. Suspendisse varius erat in neque mattis tempus. Nunc a ligula
# ligula. Nam gravida sollicitudin fringilla. Pellentesque gravida risus
# in diam vestibulum ultrices. Fusce ut dui nec lacus hendrerit tincidunt.
# Sed fringilla metus nec aliquam pulvinar. Aenean aliquet id libero ut
# laoreet. Quisque vehicula, sapien vel cursus efficitur, lectus est
# consectetur odio, quis tristique dui dolor luctus tortor. Donec eu
# dictum nisi. Quisque elit libero, luctus sed varius lobortis, ornare ac
# dui. Ut sed tortor quis neque finibus tincidunt. Sed sed malesuada
# metus. Vivamus quis est aliquam, maximus turpis vel, venenatis lacus.
# Fusce laoreet leo dignissim nulla aliquet, vitae faucibus ex blandit.
# Proin cursus nulla ac leo dapibus posuere. Nullam ac ornare neque.
# Curabitur in tempor velit. Vivamus sed tortor magna. Maecenas vel
# condimentum lectus. Phasellus placerat, eros ac venenatis sagittis,
# mi nunc egestas neque, ac iaculis libero orci eu ligula. Maecenas
# sollicitudin facilisis elit, sed semper tortor finibus ac. Sed ornare
# blandit massa, quis ultrices mauris faucibus ac. Nunc auctor augue quis
# laoreet lobortis. Nullam facilisis sapien lacinia elit varius, sit amet
# luctus mi egestas. Nam vitae tempor purus, et euismod nisi. Nulla sed
# leo venenatis, eleifend dolor at, faucibus augue. Ut a nisl aliquet,
# viverra dui quis, accumsan tellus. Aenean facilisis porttitor nulla ac
# pharetra. Vestibulum at dolor malesuada, elementum erat quis, pretium
# orci. Morbi semper vitae nisi vitae scelerisque.
# nulla: 8
# justo: 3
# dictum: 1
# amet: 4
# eget: 1
# donec: 4
# tincidunt: 8
# lacus: 2
# hendrerit: 2
# venenatis: 4
# vivamus: 3
# fermentum: 2
# suspendisse: 5
# maecenas: 2
# efficitur: 2
# et: 37
# turpis: 2
# mi: 3
# nibh: 1
# pretium: 3
# tempus: 1
# consectetur: 3
# nam: 2
# leo: 5
# placerat: 2
# imperdiet: 3
# morbi: 1
# lacinia: 1
# elit: 6
# nisi: 5
# pharetra: 3
# bibendum: 2
# dapibus: 2
# purus: 3
# phasellus: 2
# adipiscing: 1
# ex: 1
# sollicitudin: 2
# consequat: 2
# proin: 2
# ligula: 5
# posuere: 2
# sagittis: 2
# tortor: 4
# porttitor: 2
# luctus: 4
# euismod: 1
# sodales: 1
# viverra: 3
# nullam: 2
# sem: 3
# lectus: 4
# libero: 4
# aliquet: 5
# suscipit: 3
# condimentum: 1
# porta: 1
# varius: 4
# ipsum: 2
# neque: 4
# egestas: 3
# in: 30
# sapien: 2
# eros: 1
# rhoncus: 1
# felis: 1
# finibus: 2
# tempor: 3
# mattis: 2
# rutrum: 2
# fusce: 3
# feugiat: 1
# arcu: 2
# vestibulum: 4
# maximus: 2
# quis: 14
# erat: 4
# aenean: 2
# sit: 4
# est: 12
# auctor: 1
# a: 202
# aliquam: 5
# tellus: 3
# vehicula: 1
# orci: 3
# ultricies: 2
# nec: 9
# mollis: 2
# nisl: 4
# metus: 6
# lorem: 3
# quam: 6
# ac: 23
# ornare: 5
# dignissim: 2
# velit: 2
# cursus: 2
# semper: 2
# eu: 9
# odio: 2
# convallis: 2
# tristique: 2
# laoreet: 4
# blandit: 4
# diam: 4
# congue: 1
# accumsan: 3
# lobortis: 4
# dui: 6
# quisque: 3
# vel: 9
# sed: 11
# non: 1
# risus: 1
# vulputate: 1
# massa: 1
# vitae: 8
# pulvinar: 1
# facilisis: 3
# malesuada: 6
# iaculis: 1
# id: 13
# ut: 11
# gravida: 2
# urna: 1
# faucibus: 3
# nunc: 7
# scelerisque: 4
# magna: 2
# eleifend: 1
# pellentesque: 2
# fringilla: 2
# mauris: 4
# ultrices: 2
# curabitur: 5
# augue: 4
# at: 17
# dolor: 6
# elementum: 2
# enim: 3
# ante: 1
