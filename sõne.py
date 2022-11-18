#1. Sõne-tüüpi muutujate deklareerimine
#Loo muutuja first_name, mille väärtus on "James", ja last_name, mille väärtus on "Bond".
#Muutuja kohta saad vajadusel samuti lugeda PyDocist.
first_name = "James"
last_name = "Bond"
#2. Sõnede kujundamine - names
#Loo muutuja full_name, mille väärtuseks on sõne järgmisel kujul: "first_name last_name", kus first_name ja last_name on eelmises ülesandes loodud muutujate väärtused. Kasuta selleks sõnede liitmist.
#Loo muutuja self_description_sentence, mille väärtus on sõne järgmisel kujul: "My name is last_name, first_name last_name.", kus first_name ja last_name on eelmises ülesandes loodud muutujate väärtused. Sõne kujundamiseks kasuta f stringi.
full_name = first_name + " " + last_name
self_description_sentence = "My name is " + last_name + ", " + first_name + " " + last_name
#3. Sõnede kujundamine - cake string
#Loo muutuja cake = "vahukoormarjadtäidispõhi".
cake = "vahukoormarjadtäidispõhi"
#See on meie kook, mille kihid on vaja
#printida ülevalt alla kindlas järjekorras: vahukoor, marjad, täidis,
#põhi. Kasuta selleks vaid ühte print() funktsiooni.
#Tulemus peaks välja nägema selline:
#vahukoor
#marjad
#täidis
#põhi
#Vihje: \n kasutamisel prinditakse sõne teisele reale.
print("vahukoor\nmarjad\ntäidis\npõhi")
#4. Sõnede tükeldamine
#Harjutame sõnede tükeldamist ehk slice notation'i kasutamist.
#Loo muutuja original_string = "Programming is fun!"
original_string = "Programming is fun!"
#Seda sõne hakkame edaspidi tükeldama slice notation'i abil.
#Loo muutuja backwards, mille väärtus on esialgne sõne tagurpidi (ehk "!nuf si gnimmargorP").
backwards = original_string[::-1]
print(backwards)
#Loo muutuja every_other, mille väärtus on esialgsest sõnest iga järgmine täht ehk esimene, kolmas, viies jne.
sliced_text = slice(0, 20, 2)
every_other = (original_string[sliced_text])
print(every_other)
#Loo muutuja first_word_reversed, mille väärtus on esialgse sõne esimene sõna (ehk Programming) tagurpidi.
sliced_first_text = slice(0, 11)
sliced_first_word = (original_string[sliced_first_text])
print(sliced_first_word)
first_word_reversed = sliced_first_word[::-1]
print(first_word_reversed)