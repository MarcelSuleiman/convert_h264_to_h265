#!/usr/bin/env python3

import sys, os, time, subprocess, re

koncovky_video = ['mkv', 'mp4', 'avi', 'mov', 'ts']
mkv_koncovka = ['mkv']

#seria = '04'

# ak mame viacero videii v jednom priecinku, priecinky v hlavom priecinku (root dir)
# do pola seria doplnime nazvy jednotlivych priecinkov na spracovanie

seria = ['22'] # list resp. zoznam serii (zloziek) ktore sa v danom sedeni budu spracovavat

# pripadne nazvy priecinkov su pomenovane sekvencne (S01, S02, S03... 01, 02, 03, ... )
# mozme dorobit generator nazvov
# to je ale asi zbytocne nakolko vieme zoznam a nazvy zloziek vycitat

for i in range(len(seria)):
	print(i)

	path = 'D:\\Serialy\\Simpsonovci\\S{}'.format(seria[i])
	#path = 'D:\\Serialy\\Griffinovi\\S{}'.format(seria[i])

	for root, dirs, files in os.walk(path, topdown=False):
		for name in files:
			subor = os.path.join(root, name)
			#print(subor)

			if "'" in subor or "'" in name: # ak sa v nazve ci ceste nachadza ' - robi problemy v cli tak sa upravi na pouzitelny tvar '\''
				name2 = name.replace('\'',"\'\\\'\'")
				subor2 = subor.replace('\'',"\'\\\'\'")
			else:
				name2 = name
				subor2 = subor
			
			nazov_list = name2.split('.')

			koncovka = ''.join(nazov_list[-1:]) # extrahujem poslednu polozku z LISTu do string formatu

			# ak sme natrafili na video...
			if koncovka in koncovky_video:
				cli_line = "ffmpeg -i" + " '" + subor2 + "' " + "-map 0:"

				subor3 = '.'.join(nazov_list[:-1]+mkv_koncovka)
				# nestastne riesenie, treba prepisat
				subor3 = os.path.join('D:\\Serialy\\Simpsonovci\\libx265\\S{}'.format(seria[i]), subor3)

				cli_line = "ffmpeg -i \"{}\" -vcodec libx265 \"{}\"".format(subor2, subor3)
				
				# vizualna kontrola, co spracuvame, kde sa nachadzame
				print(cli_line)

				subprocess.call(cli_line, shell=True)
				
				# vizualne oznamenie ze ak treba, mozeme skript manualne vypnut bez poskodenia video suboru
				print('Davam si pauzu na vychladenie CPU')
				time.sleep(45)


