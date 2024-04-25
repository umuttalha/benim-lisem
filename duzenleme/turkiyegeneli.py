import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

def deger_ekle_tr_tablo(sayisal_2021_yeni,sayisal_2021_eski,sayisal_2020_yeni,sayisal_2020_eski,sayisal_2019_yeni,sayisal_2019_eski,sayisal_2018_yeni,sayisal_2018_eski,esit_2021_yeni,esit_2021_eski,esit_2020_yeni,esit_2020_eski,esit_2019_yeni,esit_2019_eski,esit_2018_yeni,esit_2018_eski,sozel_2021_yeni,sozel_2021_eski,sozel_2020_yeni,sozel_2020_eski,sozel_2019_yeni,sozel_2019_eski,sozel_2018_yeni,sozel_2018_eski,dil_2021_yeni,dil_2021_eski,dil_2020_yeni,dil_2020_eski,dil_2019_yeni,dil_2019_eski,dil_2018_yeni,dil_2018_eski,onlisans_2021_yeni,onlisans_2021_eski,onlisans_2020_yeni,onlisans_2020_eski,onlisans_2019_yeni,onlisans_2019_eski,onlisans_2018_yeni,onlisans_2018_eski):
    cursor.execute("Insert into tr_sayilar_tablo_2021 Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(sayisal_2021_yeni,sayisal_2021_eski,sayisal_2020_yeni,sayisal_2020_eski,sayisal_2019_yeni,sayisal_2019_eski,sayisal_2018_yeni,sayisal_2018_eski,esit_2021_yeni,esit_2021_eski,esit_2020_yeni,esit_2020_eski,esit_2019_yeni,esit_2019_eski,esit_2018_yeni,esit_2018_eski,sozel_2021_yeni,sozel_2021_eski,sozel_2020_yeni,sozel_2020_eski,sozel_2019_yeni,sozel_2019_eski,sozel_2018_yeni,sozel_2018_eski,dil_2021_yeni,dil_2021_eski,dil_2020_yeni,dil_2020_eski,dil_2019_yeni,dil_2019_eski,dil_2018_yeni,dil_2018_eski,onlisans_2021_yeni,onlisans_2021_eski,onlisans_2020_yeni,onlisans_2020_eski,onlisans_2019_yeni,onlisans_2019_eski,onlisans_2018_yeni,onlisans_2018_eski))
    con.commit()

sayisal_2021_sayi_yeni=0
sayisal_2020_sayi_yeni=0
sayisal_2019_sayi_yeni=0
sayisal_2018_sayi_yeni=0


esit_2021_sayi_yeni=0
esit_2020_sayi_yeni=0
esit_2019_sayi_yeni=0
esit_2018_sayi_yeni=0


sozel_2021_sayi_yeni=0
sozel_2020_sayi_yeni=0
sozel_2019_sayi_yeni=0
sozel_2018_sayi_yeni=0


dil_2021_sayi_yeni=0
dil_2020_sayi_yeni=0
dil_2019_sayi_yeni=0
dil_2018_sayi_yeni=0


onlisans_2021_sayi_yeni=0
onlisans_2020_sayi_yeni=0
onlisans_2019_sayi_yeni=0
onlisans_2018_sayi_yeni=0

sayisal_2021_sayi_eski=0
sayisal_2020_sayi_eski=0
sayisal_2019_sayi_eski=0
sayisal_2018_sayi_eski=0


esit_2021_sayi_eski=0
esit_2020_sayi_eski=0
esit_2019_sayi_eski=0
esit_2018_sayi_eski=0


sozel_2021_sayi_eski=0
sozel_2020_sayi_eski=0
sozel_2019_sayi_eski=0
sozel_2018_sayi_eski=0


dil_2021_sayi_eski=0
dil_2020_sayi_eski=0
dil_2019_sayi_eski=0
dil_2018_sayi_eski=0


onlisans_2021_sayi_eski=0
onlisans_2020_sayi_eski=0
onlisans_2019_sayi_eski=0
onlisans_2018_sayi_eski=0

for lise_il in range(1,83):

##################################Sayisal#################################

    cursor.execute("Select sayisal_2021_yeni,sayisal_2021_eski,sayisal_2020_yeni,sayisal_2020_eski,sayisal_2019_yeni,sayisal_2019_eski,sayisal_2018_yeni,sayisal_2018_eski,esit_2021_yeni,esit_2021_eski,esit_2020_yeni,esit_2020_eski,esit_2019_yeni,esit_2019_eski,esit_2018_yeni,esit_2018_eski,sozel_2021_yeni,sozel_2021_eski,sozel_2020_yeni,sozel_2020_eski,sozel_2019_yeni,sozel_2019_eski,sozel_2018_yeni,sozel_2018_eski,dil_2021_yeni,dil_2021_eski,dil_2020_yeni,dil_2020_eski,dil_2019_yeni,dil_2019_eski,dil_2018_yeni,dil_2018_eski,onlisans_2021_yeni,onlisans_2021_eski,onlisans_2020_yeni,onlisans_2020_eski,onlisans_2019_yeni,onlisans_2019_eski,onlisans_2018_yeni,onlisans_2018_eski From il_sayilar_tablo_2021 Where il_id =? ",(lise_il,))
    data = cursor.fetchall() 

    for i in data:

        sayisal_2021_sayi_yeni+=i[0]
        sayisal_2021_sayi_eski+=i[1]


    for i in data:

        sayisal_2020_sayi_yeni+=i[2]
        sayisal_2020_sayi_eski+=i[3]

    for i in data:

        sayisal_2019_sayi_yeni+=i[4]
        sayisal_2019_sayi_eski+=i[5]


    for i in data:

        sayisal_2018_sayi_yeni+=i[6]
        sayisal_2018_sayi_eski+=i[7]

    ##################################Eşit#################################

    for i in data:

        esit_2021_sayi_yeni+=i[8]
        esit_2021_sayi_eski+=i[9]


    for i in data:

        esit_2020_sayi_yeni+=i[10]
        esit_2020_sayi_eski+=i[11]


    for i in data:

        esit_2019_sayi_yeni+=i[12]
        esit_2019_sayi_eski+=i[13]

    for i in data:

        esit_2018_sayi_yeni+=i[14]
        esit_2018_sayi_eski+=i[15]

    ##################################Sozel#################################


    for i in data:

        sozel_2021_sayi_yeni+=i[16]
        sozel_2021_sayi_eski+=i[17]


    for i in data:

        sozel_2020_sayi_yeni+=i[18]
        sozel_2020_sayi_eski+=i[19]



    for i in data:

        sozel_2019_sayi_yeni+=i[20]
        sozel_2019_sayi_eski+=i[21]


    for i in data:

        sozel_2018_sayi_yeni+=i[22]
        sozel_2018_sayi_eski+=i[23]

    ##################################Dil#################################


    for i in data:

        dil_2021_sayi_yeni+=i[24]
        dil_2021_sayi_eski+=i[25]


    for i in data:

        dil_2020_sayi_yeni+=i[26]
        dil_2020_sayi_eski+=i[27]

    for i in data:

        dil_2019_sayi_yeni+=i[28]
        dil_2019_sayi_eski+=i[29]


    for i in data:

        dil_2018_sayi_yeni+=i[30]
        dil_2018_sayi_eski+=i[31]

    ##################################Onlisans#################################

    for i in data:

        onlisans_2021_sayi_yeni+=i[32]
        onlisans_2021_sayi_eski+=i[33]

    for i in data:

        onlisans_2020_sayi_yeni+=i[34]
        onlisans_2020_sayi_eski+=i[35]

    for i in data:

        onlisans_2019_sayi_yeni+=i[36]
        onlisans_2019_sayi_eski+=i[37]

    for i in data:

        onlisans_2018_sayi_yeni+=i[38]
        onlisans_2018_sayi_eski+=i[39]


deger_ekle_tr_tablo(sayisal_2021_sayi_yeni,sayisal_2021_sayi_eski,sayisal_2020_sayi_yeni,sayisal_2020_sayi_eski,sayisal_2019_sayi_yeni,sayisal_2019_sayi_eski,sayisal_2018_sayi_yeni,sayisal_2018_sayi_eski,esit_2021_sayi_yeni,esit_2021_sayi_eski,esit_2020_sayi_yeni,esit_2020_sayi_eski,esit_2019_sayi_yeni,esit_2019_sayi_eski,esit_2018_sayi_yeni,esit_2018_sayi_eski,sozel_2021_sayi_yeni,sozel_2021_sayi_eski,sozel_2020_sayi_yeni,sozel_2020_sayi_eski,sozel_2019_sayi_yeni,sozel_2019_sayi_eski,sozel_2018_sayi_yeni,sozel_2018_sayi_eski,dil_2021_sayi_yeni,dil_2021_sayi_eski,dil_2020_sayi_yeni,dil_2020_sayi_eski,dil_2019_sayi_yeni,dil_2019_sayi_eski,dil_2018_sayi_yeni,dil_2018_sayi_eski,onlisans_2021_sayi_yeni,onlisans_2021_sayi_eski,onlisans_2020_sayi_yeni,onlisans_2020_sayi_eski,onlisans_2019_sayi_yeni,onlisans_2019_sayi_eski,onlisans_2018_sayi_yeni,onlisans_2018_sayi_eski)






con.close()