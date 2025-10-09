#Start modulo erklärung

geld = 500
marcel = 0
ali = 0
jo = 0

restgeld = geld % 3
teilbaresgeld = geld - restgeld
marcel = teilbaresgeld / 3  
print(f'Marcel bekommt {marcel} Euro')