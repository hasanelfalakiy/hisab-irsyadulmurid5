from datetime import datetime
from function import *
from irsyadsholat import IrsyadSholat
now = datetime.now()



print("       _____{___Hisab Awal Waktu Sholat___}____")
print(" ")
print("           [  metode Irsyadul Murid cet-5  ]  ")
print(" ")
print("Masukkan tanggal, bulan, tahun contoh 01 12 2022 satu per satu diikuti enter")
print(" ")

tanggal = int(input('Tanggal : '))
bulan = int(input('Bulan : '))
tahun = int(input('Tahun : '))
# tinggi tempat
elev = eval(input('Elev : '))
# time zone
timeZ = eval(input('Timezone : '))
kota = input('Nama kota : ')
# lintang tempat
ld = int(input('Lintang derajat : '))
lm = int(input('Lintang menit : '))
ldd = eval(input('Lintang detik : '))
cek = input('Utara = y, Selatan = n : ').lower().strip() == 'y'
# bujur tempat
bd = int(input('Bujur derajat : '))
bm = int(input('Bujur menit : '))
bdd = eval(input('Bujur detik : '))
chek = input('Timur = y, Barat = n : ').lower().strip() == 'y'

ihti = int(input('Ihthiyat (int menit) : '))

Lintang = toDecimal(ld, lm, ldd, cek)
Bujur = toDecimal(bd, bm, bdd, chek)

# ihthiyat 2 menit = 2 / 60

# memanggil class
ir = IrsyadSholat(
	tanggal,
	bulan,
	tahun,
	Lintang,
	Bujur,
	timeZ,
	elev,
	ihti
	)
	
# deklinasi matahari
Dek = ir.deklinasi()
Deklinasi = toDegree2(Dek)

# equation of time
e = ir.equation()
Equation = toDegree2(e)

# semidiameter
SD = ir.semidiameter()
semidiameter = toTime2(SD)

# dzuhur
DZ = ir.dzuhurWd()
Dzuhur = toTime2(DZ)

# ashar WIB
ASW = ir.asharWd()
Ashar = toTime2(ASW)

# maghrib WIB
MW = ir.maghribWd()
Maghrib = toTime2(MW)

# isya' WIB
IW = ir.isyaWd()
Isya = toTime2(IW)

# shubuh WIB
SW = ir.shubuhWd()
Shubuh = toTime2(SW)
# imsak
IM = ir.imsakWd()
Imsak = toTime2(IM)

# thulu' WIB
TW = ir.thuluWd()
Thulu = toTime2(TW)

# dluha WIB
hW = ir.dluhaWd()
Dluha = toTime2(hW)

# nishful Lail
Ns = ir.nisfulLail()
tMalam = toTime2(Ns)

# azimuth U-B
AQ = ir.azUB()
Azub = toDegree2(AQ)

# azimuth B-U
BU = ir.azBU()
Azbu = toDegree2(BU)

# azimuth UTSB
P = ir.azUTSB()
Azutsb = toDegree2(P)

# roshdul Qiblat 1 TZ
Rq = ir.rashdu1Wd()
Rashdu1 = toTime2(Rq)

# toshdul Qiblat 2 TZ
RW = ir.rashdu2Wd()
Rashdu2 = toTime2(RW)

# jarak markaz ke Ka'bah'
KM = ir.markazKabah()

# mengetahui selisih jam Makkah - Markaz
sJ = ir.selisihWaktu()
sJam = toCounter2(sJ)

# selisih deklinasi dengan Lintang Ka'bah
SL = ir.selisihDekLK()
sDekLK = toDegree2(SL)

# selisih deklinasi dengan Lintang Tempat
ST = ir.selisihDekLT()
sDekLT = toDegree2(ST)



print(" ")
print("_______________________________________________________")
print("")
print("-------------- Waktu Sholat ",kota,"------------------")
print(" ")
print("   ", toDegree2(Lintang)," ~ ", toDegree2(Bujur)," ",elev,"mdpl")
print(" ")
print("Tanggal: ", tanggal," ",bulan," ",tahun)
print(" ")
print(" ")
print('Deklinasi = ', Deklinasi)
print("Equation of Time = ", Equation)
print("Semidiameter = ", semidiameter)
print(" ")
print("Dzuhur  = ", Dzuhur,'WIB')
print("Ashar   = ", Ashar,'WIB')
print("Maghrib = ", Maghrib,'WIB')
print("Isya'   = ", Isya,'WIB')
print("Shubuh  =  ", Shubuh,'WIB')
print("Imsak   =  ", Imsak,'WIB')
print("Thulu'  =  ", Thulu,"WIB")
print("Dluha   =  ", Dluha,"WIB")
print("T. Malam= ", tMalam,"WIB")
print(" ")
print("Jadwal diatas sudah ditambah Ihthiyat 2 menit kecuali Thulu'/Terbit dikurangi 2 menit")
print(" ")
print("Azimuth Qiblat = ", Azub,"U-B")
print(" ")
print("Azimuth Qiblat = ", Azbu,"B-U")
print(" ")
print("Azimuth UTSB = ", Azutsb, "UTSB")
print("-------------------------------------------------------\n")
print("Bayang Qiblat 1 = ", Rashdu1," ","WIB")
print(" ")
print("Bayang Qiblat 2 = ", Rashdu2," ","WIB")
print(" ")
print("Jarak antara Markaz dengan Makkah = ", KM, "Km")
print(" ")
print("Selisih Jam Markaz dengan Makkah =", sJam)
print(" ")
print("Selisih Deklinasi dengan Lintang Ka'bah =", sDekLK)
print(" ")
print("Selisih Deklinasi dengan Lintang Markaz =", sDekLT)
print("-------------------------------------------------------\n")
print(" ")
print("dihisab & diprogram oleh")
print(" ")
print("Andi Hasan A")
print(" ")
print("LF PCNU NGAWI")
print(" ")
print("dihisab pada: ",now)
print(" ")
print("version: 2.0")
