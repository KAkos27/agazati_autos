import bevezetes
import sorozat
import autom

lista = sorozat.szam_gen()
kiirando = sorozat.egyjegyuek_szama(lista)
auto_lista = autom.file_belovas()

bevezetes.elso_feladat()

sorozat.konzol_kiir(kiirando)
sorozat.file_kiir(kiirando)

autom.flotta(auto_lista)
autom.legfiatalabb(auto_lista)
autom.atlag(auto_lista)
