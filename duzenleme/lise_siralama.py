import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

def tablo_oluştur_2021():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lise_ort_puan_2021 (
    
        lise_id INT PRIMARY KEY,
        lise_ort_sayisal_2021 FLOAT,
        lise_ort_esit_2021 FLOAT,
        lise_ort_dil_2021 FLOAT,
        lise_ort_sozel_2021 FLOAT,
        lise_ort_onlisans_2021 FLOAT
                    
);""") 
    con.commit()


tablo_oluştur_2021()


for i in range(1,16000):
            
        try:
        
            cursor.execute("Select * From okul_tablo Where okul_id =? ",(i,))
            data = cursor.fetchall()[0]

            lise_id = data[0]



            # sozel 2021

            cursor.execute("Select uni_2021_puan From sozel_2021 Where okul_adı =? ",(lise_id,))
            uni_2021_puan = cursor.fetchall()

            print(uni_2021_puan)

            toplam=0
            sayi=0
            toplam_ort_sozel=0
            for k in uni_2021_puan:

                if k[0] != "Dolmadı" :
                   if k[0] != "---":
                    sayi+=1
                    toplam += float(k[0].replace(',', '.'))


            try:   

                if sayi >= 10:
                    
                    toplam_ort_sozel=toplam/sayi
                    toplam_ort_sozel=round(toplam_ort_sozel, 2)

            except:
                  pass
            
            # eşit 2021

            cursor.execute("Select uni_2021_puan From esit_2021 Where okul_adı =? ",(lise_id,))
            uni_2021_puan = cursor.fetchall()

            print(uni_2021_puan)

            toplam=0
            sayi=0
            toplam_ort_esit=0
            for k in uni_2021_puan:

                if k[0] != "Dolmadı":
                   if k[0] != "---":
                    sayi+=1
                    toplam += float(k[0].replace(',', '.'))


            try:   
                if sayi >= 10:
                    toplam_ort_esit=toplam/sayi
                    toplam_ort_esit=round(toplam_ort_esit, 2)

            except:
                  pass
            

            # dil 2021

            cursor.execute("Select uni_2021_puan From dil_2021 Where okul_adı =? ",(lise_id,))
            uni_2021_puan = cursor.fetchall()

            print(uni_2021_puan)

            toplam=0
            sayi=0
            toplam_ort_dil=0
            for k in uni_2021_puan:

                if k[0] != "Dolmadı":
                   if k[0] != "---":
                    sayi+=1
                    toplam += float(k[0].replace(',', '.'))


            try:  
                if sayi >= 10: 
                    toplam_ort_dil=toplam/sayi
                    toplam_ort_dil=round(toplam_ort_dil, 2)

            except:
                  pass
            
            # sayisa 2021

            cursor.execute("Select uni_2021_puan From sayisal_2021 Where okul_adı =? ",(lise_id,))
            uni_2021_puan = cursor.fetchall()

            print(uni_2021_puan)

            toplam=0
            sayi=0
            toplam_ort_sayisal=0
            for k in uni_2021_puan:

                if k[0] != "Dolmadı":
                   if k[0] != "---":
                    sayi+=1
                    toplam += float(k[0].replace(',', '.'))


            try:   
                if sayi >= 10:
                    toplam_ort_sayisal=toplam/sayi
                    toplam_ort_sayisal=round(toplam_ort_sayisal, 2)

            except:
                  pass
            

            # onlisans 2021

            cursor.execute("Select uni_2021_puan From onlisans_2021 Where okul_adı =? ",(lise_id,))
            uni_2021_puan = cursor.fetchall()

            print(uni_2021_puan)

            toplam=0
            sayi=0
            toplam_ort_onlisans=0
            for k in uni_2021_puan:

                if k[0] != "Dolmadı":
                   if k[0] != "---":
                    sayi+=1
                    deger = float(k[0].replace(',', '.'))
                    print(deger)
                    toplam += deger

            try:   
                if sayi >= 10:
                    print(toplam)
                    print(sayi)
                    toplam_ort_onlisans=toplam/sayi
                    toplam_ort_onlisans=round(toplam_ort_onlisans, 2)

            except:
                  pass
            
            print(lise_id,toplam_ort_sayisal,toplam_ort_esit,toplam_ort_dil,toplam_ort_onlisans,toplam_ort_sozel)

            cursor.execute("INSERT INTO lise_ort_puan_2021 VALUES(?,?,?,?,?,?)",(lise_id,toplam_ort_sayisal,toplam_ort_esit,toplam_ort_dil,toplam_ort_onlisans,toplam_ort_sozel))
            con.commit()

            
        except:
            pass