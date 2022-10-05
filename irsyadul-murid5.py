import math
from datetime import datetime
now=datetime.now()

print("       _____{___Hisab Awal Waktu Sholat___}____")
print(" ")
print("           [  metode Irsyadul Murid cet-5  ]  ")
print(" ")
print("Masukkan tanggal, bulan, tahun contoh 01 12 2022 satu per satu diikuti enter")
print(" ")
print("! sementara hanya bisa untuk daerah Kota Ngawi !")
print(" ")
Tanggal=int(input('Tanggal= '))
Bulan=int(input('Bulan= '))
Tahun=int(input('Tahun= '))

#Tinggi Tempat
TT=150
#TT=10
#Time Zone
TZ=7
Lintang=-7.4333333333337
Bujur=111.4333333333337
'''Lintang=-7.25
Bujur=112.75
Lintang=-7.570138889
Bujur=111.3102528'''

#Ihthiyat 2 menit
#Ihthiyat=2/60

if Bulan<3:
    G=Bulan+12
else :
    G=Bulan
if Bulan<3:
    KT=Tahun-1
else :
    KT=Tahun
#koreksi Gregorius
krg = 2-int(Tahun/100)+int(int(Tahun/100)/4)

#Julian Day
JD = round(int(365.25*(KT+4716))+int(30.6001*(G+1))+Tanggal+((10+23/60)/24)+krg-1524.5,3)

#Juz Asal Miladiyah
JAM=(JD-2451545)/36525

#Data Matahari Wasathus Syams
S=280.46645+36000.76983*JAM
FrS=(S/360-int(S/360))*360

#Khooshotus Syams
m=357.52910+35999.05030*JAM
Frm=(m/360-int(m/360))*360

#'Uqdatus Syams
N=125.04-1934.136*JAM
FrN=(N/360-int(N/360))*360

#Tahshishul Awwal/ Koreksi pertama
K1 = (17.264/3600)*math.sin(math.radians(FrN))+(0.206/3600)*math.sin(math.radians(2*FrN))

#Tahshishus Tsani/ Koreksi kedua
K2 = (-1.264/3600)*math.sin(math.radians(2*FrS))

#Tahshishus Tsaalist/ Koreksi ketiga
R = (9.23/3600)*math.cos(math.radians(FrN))-(0.090/3600)*math.cos(math.radians(2*FrN))

#Tahshishur Roobi'/ Koreksi keempat
R1 = (0.548/3600)*math.cos(math.radians(2*FrS))

#Mail Kulli
Q = 23.43929111+R+R1-(46.8150/3600)*JAM

#Ta'diilus Syams
E = (6898.06/3600)*math.sin(math.radians(Frm))+(72.095/3600)*math.sin(math.radians(2*Frm))+(0.966/3600)*math.sin(math.radians(3*Frm))

#Thuulus Syams
S1 = FrS+E+K1+K2-(20.47/3600)

#Mail Syams/ Deklinasi Matahari
Dek = math.degrees(math.asin(math.sin(math.radians(S1))*math.sin(math.radians(Q))))

#Ta'diluz Zaman/ Equation of Time
e = (-1.915*math.sin(math.radians(Frm))+(-0.02)*math.sin(math.radians(2*Frm))+2.466*math.sin(math.radians(2*S1))+(-0.053)*math.sin(math.radians(4*S1)))/15

#deklinasi matahari
D1=int(Dek)
D2=(Dek-D1)*60
D3=int(D2)
D4=(D2-D3)*60
D5=round(D4)

#Equation of time
E1=int(e)
E2=(e-E1)*60
E3=int(E2)
E4=(E2-E3)*60
E5=round(E4)

#Semidiameter
SD = 0.267/(1-0.017*math.cos(math.radians(Frm)))
SD1=int(SD)
SD2=(SD-SD1)*60
SD3=int(SD2)
SD4=(SD2-SD3)*60
SD5=int(SD4)

#Dzuhur
DZ = 12-e+((TZ*15)-Bujur)/15+(2/60)
DZ1=int(DZ)
DZ2=(DZ-DZ1)*60
DZ3=int(DZ2)
DZ4=(DZ2-DZ3)*60
DZ5=int(DZ4)

#Ashar
H = math.degrees(math.atan(1/(math.tan(math.radians(abs(Lintang-Dek)))+1)))

F = -math.tan(math.radians(Lintang))*math.tan(math.radians(Dek))

Ge = math.cos(math.radians(Lintang))*math.cos(math.radians(Dek))

AS = 12+math.degrees(math.acos(F+math.sin(math.radians(H))/Ge))/15+(2/60)

#Ashar WIS
AS1=int(AS)
AS2=(AS-AS1)*60
AS3=int(AS2)
AS4=(AS2-AS3)*60
AS5=int(AS4)

#Ashar WIB
ASW = AS-e-(Bujur-(TZ*15))/15
ASW1=int(ASW)
ASW2=(ASW-ASW1)*60
ASW3=int(ASW2)
ASW4=(ASW2-ASW3)*60
ASW5=int(ASW4)

#Maghrib
Dip = (1.76/60)*math.sqrt(TT)
#ho Maghrib
HM = -(SD+(34.5/60)+Dip)-0.0024
#Maghrib WIS
TM = 12+math.degrees(math.acos(F+math.sin(math.radians(HM))/Ge))/15+(2/60)
#Maghrib WIB
MW = TM-e-(Bujur-(TZ*15))/15
MW1=int(MW)
MW2=(MW-MW1)*60
MW3=int(MW2)
MW4=(MW2-MW3)*60
MW5=int(MW4)
#h Isya'
HI = -18
#Isya' WIS
IS = 12+math.degrees(math.acos(F+math.sin(math.radians(HI))/Ge))/15+(2/60)
#Isya' WIB
IW = IS-e-(Bujur-(TZ*15))/15
IW1=int(IW)
IW2=(IW-IW1)*60
IW3=int(IW2)
IW4=(IW2-IW3)*60
IW5=int(IW4)
#h Shubuh
Hs = -20
#Shubuh WIS
SI = 12-math.degrees(math.acos(F+math.sin(math.radians(Hs))/Ge))/15+(2/60)
#Shubuh WIB
SW = SI-e-(Bujur-(TZ*15))/15
SW1=int(SW)
SW2=(SW-SW1)*60
SW3=int(SW2)
SW4=(SW2-SW3)*60
SW5=int(SW4)
#Imsak
IM = SW-(10/60)
IM1=int(IM)
IM2=(IM-IM1)*60
IM3=int(IM2)
IM4=(IM2-IM3)*60
IM5=int(IM4)
#h Thulu'
hT = -(SD+(34.5/60)+Dip)-0.0024
#Thulu' WIS
TI = 12-math.degrees(math.acos(F+math.sin(math.radians(hT))/Ge))/15-(2/60)
#Thulu' WIB
TW = TI-e-(Bujur-(TZ*15))/15
TW1=int(TW)
TW2=(TW-TW1)*60
TW3=int(TW2)
TW4=(TW2-TW3)*60
TW5=int(TW4)
#Dluha
hd = 4.5
#Dluha WIS
dl = 12-math.degrees(math.acos(F+math.sin(math.radians(hd))/Ge))/15+(2/60)
#Dluha WIB
hW = dl-e-(Bujur-(TZ*15))/15
hW1=int(hW)
hW2=(hW-hW1)*60
hW3=int(hW2)
hW4=(hW2-hW3)*60
hW5=int(hW4)
#Nishful Lail
Ns = MW+((SW+24-MW)/2)-(2/60)
Ns1=int(Ns)
Ns2=(Ns-Ns1)*60
Ns3=int(Ns2)
Ns4=(Ns2-Ns3)*60
Ns5=int(Ns4)

#Arah Qiblat
#lintang dan bujur Ka'bah'
LK = 21.42191389
BK = 39.82951944

#Selisih Bujur

A = 360-BK+Bujur-360

h = math.degrees(math.asin(math.sin(math.radians(Lintang))*math.sin(math.radians(LK))+math.cos(math.radians(Lintang))*math.cos(math.radians(LK))*math.cos(math.radians(A))))

#Azimuth U-B
AQ = math.degrees(math.acos((math.sin(math.radians(LK))-math.sin(math.radians(Lintang))*math.sin(math.radians(h)))/math.cos(math.radians(Lintang))/math.cos(math.radians(h))))

A1 = int(AQ)
A2 = (AQ-A1)*60
A3 = int(A2)
A4 = (A2-A3)*60
A5 = round(A4,2)

#Azimuth B-U

BU = 90-AQ
BU1 = int(BU)
BU2 = (BU-BU1)*60
BU3 = int(BU2)
BU4 = (BU2-BU3)*60
BU5 = round(BU4,2)

#Azimuth UTSB

P = 360-AQ
P1 = int(P)
P2 = (P-P1)*60
P3 = int(P2)
P4 = (P2-P3)*60
P5 = round(P4,2)

#Roshdul Qiblat

B = 90-Lintang

PR = math.degrees(math.atan(1/(math.cos(math.radians(B))*math.tan(math.radians(P)))))

CA = math.degrees(math.acos(math.tan(math.radians(Dek))*math.tan(math.radians(B))*math.cos(math.radians(PR))))

#Roshdul Qiblat 1

RQ = -(PR-CA)/15+12

#Roshdul Qiblat 1 TZ

RW = RQ-e-(Bujur-(TZ*15))/15

h1=int(RW)
h2=(RW-h1)*60
h3=int(h2)
h4=(h2-h3)*60
h5=round(h4,2)

#Roshdul Qiblat 2

Rq1 = (-(PR+CA)/15+12)%24

#Roshdul Qiblat 2 TZ
Rq=Rq1-e-(Bujur-(TZ*15))/15

pr1 = int(Rq)
pr2 = (Rq-pr1)*60
pr3 = int(pr2)
pr4 = (pr2-pr3)*60
pr5 = round(pr4,2)

#untuk ditampilkan di consol
#Lintang
L1 = int(Lintang)
L2 = (Lintang-L1)*60
L3 = int(L2)
L4 = (L2-L3)*60
L5 = round(L4,2)
#Bujur
B1 = int(Bujur)
B2 = (Bujur-B1)*60
B3 = int(B2)
B4 = (B2-B3)*60
B5 = round(B4,2)

# mengetahui jarak antara 2 tempat
selisih = Bujur - BK

M = math.degrees(math.acos(math.sin(math.radians(Lintang))*math.sin(math.radians(LK))+math.cos(math.radians(Lintang))*math.cos(math.radians(LK))*math.cos(math.radians(selisih))))
KM = M / 360 * 6.283185307 * 6378.388

# mengetahui selisih jam Makkah - Markaz

sJ = (Bujur - BK) / 15

sJ1 = int(sJ)
sJ2 = (sJ - sJ1) * 60
sJ3 = int(sJ2)
sJ4 = (sJ2 - sJ3) * 60
sJ5 = round(sJ4, 2)

# selisih deklinasi dengan Lintang Ka'bah

SL = Dek - LK

SL1 = int(SL)
SL2 = (SL - SL1) * 60
SL3 = int(SL2)
SL4 = (SL2 - SL3) * 60
SL5 = round(SL4, 2)

# selisih deklinasi dengan Lintang Tempat

ST = Dek - Lintang

ST1 = int(ST)
ST2 = (ST - ST1) * 60
ST3 = int(ST2)
ST4 = (ST2 - ST3) * 60
ST5 = round(ST4, 2)



print(" ")
print("_______________________________________________________")
print("")
print("--------------Waktu Sholat Kota NGAWI------------------")
print(" ")
print("   ",L1,"°",L3,"'",L5,'"'," ~ ",B1,"°",B3,"'",B5,'" ',TT,"mdpl")
print(" ")
print("Tanggal: ", Tanggal," ",Bulan," ",Tahun)
print(" ")
print(" ")
print('Deklinasi= ',D1,'°',D3,"'",D5,'"')
print("Equation of Time= ",E1,"°",E3,"'",E5,'"')
print(" ")
print("Dzuhur  = ",DZ1,":",DZ3,":",DZ5,'WIB')
print("Ashar   = ",ASW1,":",ASW3,":",ASW5,'WIB')
print("Maghrib = ",MW1,":",MW3,":",MW5,'WIB')
print("Isya'   = ",IW1,":",IW3,":",IW5,'WIB')
print("Shubuh  =  ",SW1,":",SW3,":",SW5,'WIB')
print("Imsak   =  ",IM1,":",IM3,":",IM5,'WIB')
print("Thulu'  =  ",TW1,":",TW3,":",TW5,"WIB")
print("Dluha   =  ",hW1,":",hW3,":",hW5,"WIB")
print("Tengah Malam= ",Ns1,":",Ns3,":",Ns5,"WIB")
print(" ")
print("Jadwal diatas sudah ditambah Ihthiyat 2 menit kecuali Thulu'/Terbit dikurangi 2 menit")
print(" ")
print("Azimuth Qiblat = ",A1,"°",A3,"'",A5,'"',"U-B")
print(" ")
print("Azimuth Qiblat = ",BU1,"°",BU3,"'",BU5,'"',"B-U")
print(" ")
print("Azimuth UTSB = ",P1,"°",P3,"'",P5,'"', "UTSB")
print("-------------------------------------------------------\n")
print("Bayang Qiblat 1= ",h1,":",h3,":",h5," ","WIB")
print(" ")
print("Bayang Qiblat 2= ",pr1,":",pr3,":",pr5," ","WIB")
print(" ")
print("Jarak antara Markaz dengan Makkah= ", KM, "Km")
print(" ")
print("Selisih Jam Markaz dengan Makkah =", sJ1,":",sJ3,":",sJ5)
print(" ")
print("Selisih Deklinasi dengan Lintang Ka'bah =", SL1,"°",SL3,"`",SL5,'"')
print(" ")
print("Selisih Deklinasi dengan Lintang Markaz =", ST1,"°",ST3,"`",ST5,'"')
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
print("version: 0.1.2-beta")