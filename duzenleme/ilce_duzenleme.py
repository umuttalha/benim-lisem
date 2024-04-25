import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

def deger_ekle_ilce_tablo(ilce_id,sayisal_2021_yeni,sayisal_2021_eski,sayisal_2020_yeni,sayisal_2020_eski,sayisal_2019_yeni,sayisal_2019_eski,sayisal_2018_yeni,sayisal_2018_eski,esit_2021_yeni,esit_2021_eski,esit_2020_yeni,esit_2020_eski,esit_2019_yeni,esit_2019_eski,esit_2018_yeni,esit_2018_eski,sozel_2021_yeni,sozel_2021_eski,sozel_2020_yeni,sozel_2020_eski,sozel_2019_yeni,sozel_2019_eski,sozel_2018_yeni,sozel_2018_eski,dil_2021_yeni,dil_2021_eski,dil_2020_yeni,dil_2020_eski,dil_2019_yeni,dil_2019_eski,dil_2018_yeni,dil_2018_eski,onlisans_2021_yeni,onlisans_2021_eski,onlisans_2020_yeni,onlisans_2020_eski,onlisans_2019_yeni,onlisans_2019_eski,onlisans_2018_yeni,onlisans_2018_eski):
    cursor.execute("Insert into ilce_sayilar_tablo_2021 Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(ilce_id,sayisal_2021_yeni,sayisal_2021_eski,sayisal_2020_yeni,sayisal_2020_eski,sayisal_2019_yeni,sayisal_2019_eski,sayisal_2018_yeni,sayisal_2018_eski,esit_2021_yeni,esit_2021_eski,esit_2020_yeni,esit_2020_eski,esit_2019_yeni,esit_2019_eski,esit_2018_yeni,esit_2018_eski,sozel_2021_yeni,sozel_2021_eski,sozel_2020_yeni,sozel_2020_eski,sozel_2019_yeni,sozel_2019_eski,sozel_2018_yeni,sozel_2018_eski,dil_2021_yeni,dil_2021_eski,dil_2020_yeni,dil_2020_eski,dil_2019_yeni,dil_2019_eski,dil_2018_yeni,dil_2018_eski,onlisans_2021_yeni,onlisans_2021_eski,onlisans_2020_yeni,onlisans_2020_eski,onlisans_2019_yeni,onlisans_2019_eski,onlisans_2018_yeni,onlisans_2018_eski))
    con.commit()

def verileri_al(lise_ilce):
    cursor.execute("Select * From ilce_sayilar_tablo Where ilce_id =? ",(lise_ilce,))
    data = cursor.fetchall() 
    print(data[0])


for lise_ilce in range(1,978):

##################################Sayisal#################################

    cursor.execute("Select yeni_mezun,onceki_mezun From sayisal_2021 Where lise_ilce =? ",(lise_ilce,))
    data = cursor.fetchall() 

    sayisal_2021_sayi_yeni=0
    sayisal_2021_sayi_eski=0

    for i in data:

        sayisal_2021_sayi_yeni+=i[0]
        sayisal_2021_sayi_eski+=i[1]

    ##################################Eşit#################################

    cursor.execute("Select yeni_mezun,onceki_mezun From esit_2021 Where lise_ilce =? ",(lise_ilce,))
    data = cursor.fetchall() 

    esit_2021_sayi_yeni=0
    esit_2021_sayi_eski=0

    for i in data:
        esit_2021_sayi_yeni+=i[0]
        esit_2021_sayi_eski+=i[1]

    ##################################Sozel#################################

    cursor.execute("Select yeni_mezun,onceki_mezun From sozel_2021 Where lise_ilce =? ",(lise_ilce,))
    data = cursor.fetchall() 

    sozel_2021_sayi_yeni=0
    sozel_2021_sayi_eski=0

    for i in data:
        sozel_2021_sayi_yeni+=i[0]
        sozel_2021_sayi_eski+=i[1]

    ##################################Dil#################################

    cursor.execute("Select yeni_mezun,onceki_mezun From dil_2021 Where lise_ilce =? ",(lise_ilce,))
    data = cursor.fetchall() 

    dil_2021_sayi_yeni=0
    dil_2021_sayi_eski=0

    for i in data:
        dil_2021_sayi_yeni+=i[0]
        dil_2021_sayi_eski+=i[1]

    ##################################Onlisans#################################

    cursor.execute("Select yeni_mezun,onceki_mezun From onlisans_2021 Where lise_ilce =? ",(lise_ilce,))
    data = cursor.fetchall() 

    onlisans_2021_sayi_yeni=0
    onlisans_2021_sayi_eski=0

    for i in data:
        onlisans_2021_sayi_yeni+=i[0]
        onlisans_2021_sayi_eski+=i[1]


    cursor.execute("Select * From ilce_sayilar_tablo Where ilce_id = ? ",(lise_ilce,))
    data = cursor.fetchall() 
    veri=data[0]
    deger_ekle_ilce_tablo(veri[0],sayisal_2021_sayi_yeni,sayisal_2021_sayi_eski,veri[1],veri[2],veri[3],veri[4],veri[5],veri[6],esit_2021_sayi_yeni,esit_2021_sayi_eski,veri[7],veri[8],veri[9],veri[10],veri[11],veri[12],sozel_2021_sayi_yeni,sozel_2021_sayi_eski,veri[13],veri[14],veri[15],veri[16],veri[17],veri[18],dil_2021_sayi_yeni,dil_2021_sayi_eski,veri[19],veri[20],veri[21],veri[22],veri[23],veri[24],onlisans_2021_sayi_yeni,onlisans_2021_sayi_eski,veri[25],veri[26],veri[27],veri[28],veri[29],veri[30])


con.close()