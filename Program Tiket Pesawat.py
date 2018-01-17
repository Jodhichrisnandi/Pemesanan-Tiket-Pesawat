import os

loop = True


while loop:
	def menu() :
		print("\n===============================")
		print("Program Pemesanan Tiket Pesawat")
		print("===============================")
		print("1. Bandung")
		print("2. Jakarta")
		print("3. Medan")
		print("4. Makasar")
		print("5. Exit")
		print("\n===============================")
		
	def pesan():
		jmlh_tiket = int(input("Masukan jumlah tiket : "))
		num_array = list()
		num = input("Berapa orang yang ingin memesan tiket ? : ")
		print ("Nasukan nama Pemesan : ")
		for i in range (int(num)):
			i += 1
			n = input("orang ke {} :".format(i))
			num_array.append(str(n)) 
		total_tiket = jmlh_tiket*harga
		os.system('cls')
		print("\n----------------------------------------------")
		print("Anda telah berhasil melakukan pembelian tiket ")
		print("----------------------------------------------")
		print ("Nama Pemesan :".format(len(num_array)))
		for a in num_array:
			print (("- {}").format(a))
		print("Total Harga","Rp.",(total_tiket))
	

	menu()
	tujuan = int(input("Masukan Pilihan [1-5] : "))
		
	if ((tujuan) == 1):
		print("\n-------------------------------------------------------")
		print("\nKode  Nama\tKota\t\tHarga")
		print("\n      Pesawat\tTujuan\t\tTiket")
		print("\n-------------------------------------------------------")
		print("\n101.  Garuda\tBandung \tRp.1.500.000")
		print("\n102.  Lion Air\tBandung \tRp.800.000")
		print("\n103.  Sriwijaya\tBandung \tRp.750.000")
		print("\n-------------------------------------------------------")
		no_pesawat = int(input("Masukan kode penerbangan : "))
		
		
		if ((no_pesawat) == 101):
			harga = 1500000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
			
			
		elif ((no_pesawat) == 102):
			harga = 800000
			print("")
			print("---------------------------------")
			print("anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		elif ((no_pesawat) == 103):
			harga = 750000
			print("")
			print("---------------------------------")
			print("anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		else :
			os.system('cls')
			print("kode penerbangan tidak ada dalam daftar")
			
			
	elif ((tujuan) == 2):
		print("\n----------------------------------------------------------")
		print("\nKode  Nama\tKota\t\tHarga")
		print("\n      Pesawat\tTujuan\t\tTiket")
		print("\n----------------------------------------------------------")
		print("\n201. Citilink\tJakarta \tRp.2.000.000")
		print("\n202. NAM air\tJakarta \tRp.900.000")
		print("\n203. Garuda\tJakarta \tRp.1.200.000")
		print("\n----------------------------------------------------------")
		no_pesawat = int(input("Masukan kode penerbangan :"))
		
		if ((no_pesawat) == 201):
			harga = 2000000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		elif ((no_pesawat) == 202):
			harga = 900000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		elif ((no_pesawat) == 203):
			harga = 1200000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			e
		else :
			os.system('cls')
			print("Kode penerbangan tidak ada dalam daftar")
			
			
			
	elif ((tujuan) == 3):
		print("\n-------------------------------------------------------")
		print("\nKode  Nama\tKota\t\tHarga")
		print("\n      Pesawat\tTujuan\t\tTiket")
		print("\n-------------------------------------------------------")
		print("\n301. Citilink\tMedan \tRp.1.000.000")
		print("\n302. Lion Air\tMedan \tRp.800.000")
		print("\n303. Garuda\tMedan \tRp.1.600.000")
		print("\n-------------------------------------------------------")
		no_pesawat = int(input("Masukan kode penerbangan :"))
		
		if ((no_pesawat) == 301):
			harga = 1000000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		elif ((no_pesawat) == 302):
			harga = 800000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		elif ((no_pesawat) == 303):
			harga = 1600000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		else :
			os.system('cls')
			print("Kode penerbangan tidak ada dalam daftar")
			
			
			
	elif ((tujuan) == 4):
		print("\n-------------------------------------------------------")
		print("\nKode  Nama\tKota\t\tHarga")
		print("\n      Pesawat\tTujuan\t\tTiket")
		print("\n-------------------------------------------------------")
		print("\n401. Garuda\tMakkasar \tRp.1.200.000")
		print("\n402. Lion Air\tMakkasar \tRp.1.000.000")
		print("\n403. Merpati\tMakkasar \tRp.1.800.000")
		print("\n-------------------------------------------------------")
		no_pesawat = int(input("Masukan kode penerbangan :"))
		
	
		
		if ((no_pesawat) == 401):
			harga = 1000000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		elif ((no_pesawat) == 402):
			harga = 800000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		elif ((no_pesawat) == 403):
			harga = 800000
			print("")
			print("---------------------------------")
			print("Anda memilih kode penerbangan",+int(no_pesawat))
			print("---------------------------------")
			pesan()
			
		else :
			os.system('cls')
			print("Kode penerbangan tidak ada dalam daftar")
			
			
	elif ((tujuan) == 5):
		os.system('cls')
		exit()
		
	
	else :
		os.system('cls')
		print("***Pilihan tidak ada dalam daftar***")
		
		
			
			
		

			
			


