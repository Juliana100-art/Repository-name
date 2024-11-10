objom=1.44*1024*1024
stranic=100
strok = 50
sim=25
kod=4

kniga = stranic*strok*sim*kod
kol = objom//kniga
print("Количество книг, помещающихся на дискету:", int(kol))
