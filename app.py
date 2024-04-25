from flask import Flask,render_template
import sqlite3
# import locale

# locale.setlocale(locale.LC_ALL, "")
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def index():
    return render_template("anasayfa.html")

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found():
    return render_template('500.html'), 500


#il********************************************************************************
@app.route("/il")
def ilk_il():
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()
        cursor1.execute("SELECT il_ad,il_url FROM il_tablo_alfabetik")
        data = cursor1.fetchall()
    
                    
        return render_template("il_secme.html",data=data,data_len=len(data))
    

#il********************************************************************************
@app.route("/il/<string:il>")
def il(il):
    url_il=il
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data2 = cursor1.fetchall()

        a=data2[0][0]

        cursor1.execute("SELECT ilce_ad,ilce_url FROM ilce_tablo_alfabetik WHERE il_id=  ?",(a,))
        data = cursor1.fetchall()
             
        
        il=data2[0][1]
        

        return render_template("ilce_secme.html",url_il=url_il,il=il,data=data,data_len=len(data))
                
                                                                  
#ilçe********************************************************************************

@app.route("/il/<string:il>/<string:ilce>")
def ilce(il,ilce):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data1 = cursor1.fetchall()
        il_id=data1[0][0]
        il_ad=data1[0][1]

        cursor1.execute("SELECT ilce_id,ilce_ad FROM ilce_tablo WHERE ilce_url=  ? AND il_id=  ?",(ilce,il_id,))
        data2 = cursor1.fetchall()
        ilce_id=data2[0][0]
        ilce_ad=data2[0][1]

#alfabetik olarak değiştir

        cursor1.execute("SELECT okul_ad,okul_url FROM okul_tablo WHERE ilce_id=  ? AND il_id=  ?",(ilce_id,il_id,))
        data3 = cursor1.fetchall()
    
        url_ilce=ilce
        url_il=il


        return render_template("okul_secme.html",url_il=url_il,url_ilce=url_ilce ,il_ad=il_ad,ilce_ad=ilce_ad,data3=data3,data3_len=len(data3))

#okul********************************************************************************

def ayar_func(data_num,result_num,hangisi):
    for t in data_num:
        a=str(t[4])
        a = a.replace("[", "")
        a = a.replace("]", "")
        a = a.replace("'", "")
        result_num.append(a)
        hangisi+=t[6]
        hangisi+=t[7]


@app.route("/il/<string:il>/<string:ilce>/<string:lise_ad>/2022")
def okul_ad_2022(il,ilce,lise_ad):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data1 = cursor1.fetchall()
        il_id=data1[0][0]
        il_ad=data1[0][1]

        cursor1.execute("SELECT ilce_id,ilce_ad FROM ilce_tablo WHERE ilce_url=  ? AND il_id=  ?",(ilce,il_id,))
        data2 = cursor1.fetchall()
        ilce_id=data2[0][0]
        ilce_ad=data2[0][1]

        cursor1.execute("SELECT okul_id,okul_ad FROM okul_tablo WHERE okul_url= ? AND ilce_id=  ? AND il_id=  ?",(lise_ad,ilce_id,il_id,))
        data3 = cursor1.fetchall()  
        okul_id=data3[0][0]
        okul_ad=data3[0][1]

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2022_siralama,uni_2022_puan,yeni_mezun,onceki_mezun FROM sayisal_2022 WHERE okul_adi=  ?",(okul_id,))
        data4 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2022_siralama,uni_2022_puan,yeni_mezun,onceki_mezun FROM esit_2022 WHERE okul_adi=  ?",(okul_id,))
        data5 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2022_siralama,uni_2022_puan,yeni_mezun,onceki_mezun FROM sozel_2022 WHERE okul_adi=  ?",(okul_id,))
        data6 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2022_siralama,uni_2022_puan,yeni_mezun,onceki_mezun FROM dil_2022 WHERE okul_adi=  ?",(okul_id,))
        data7 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2022_siralama,uni_2022_puan,yeni_mezun,onceki_mezun FROM onlisans_2022 WHERE okul_adi=  ?",(okul_id,))
        data8 = cursor1.fetchall()
    

####################################################################################################################################################################################################

        url_ilce=ilce
        url_il=il

        result1 = []
        result2 = []
        result3 = []
        result4 = []
        result5 = []

        toplam_sayisal=0
        toplam_esit=0
        toplam_sozel=0
        toplam_dil=0
        toplam_onlisans=0

        ayar_func(data4,result1,toplam_sayisal)
        ayar_func(data5,result2,toplam_esit)
        ayar_func(data6,result3,toplam_sozel)
        ayar_func(data7,result4,toplam_dil)
        ayar_func(data8,result5,toplam_onlisans)

        print(len(data4))
        
        return render_template("son.html",toplam_sayisal=toplam_sayisal,toplam_esit=toplam_esit,toplam_sozel=toplam_sozel,toplam_dil=toplam_dil,toplam_onlisans=toplam_onlisans,url_ilce=url_ilce,url_il=url_il,il_ad=il_ad,ilce_ad=ilce_ad,lise_ad=lise_ad,okul_ad=okul_ad,result1=result1,result2=result2,result3=result3,result4=result4,result5=result5, yil="2022",data4=data4,len4=len(data4), data5=data5,len5=len(data5), data6=data6,len6=len(data6), data7=data7,len7=len(data7), data8=data8,len8=len(data8))



@app.route("/il/<string:il>/<string:ilce>/<string:lise_ad>/2021")
def okul_ad_2021(il,ilce,lise_ad):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data1 = cursor1.fetchall()
        il_id=data1[0][0]
        il_ad=data1[0][1]

        cursor1.execute("SELECT ilce_id,ilce_ad FROM ilce_tablo WHERE ilce_url=  ? AND il_id=  ?",(ilce,il_id,))
        data2 = cursor1.fetchall()
        ilce_id=data2[0][0]
        ilce_ad=data2[0][1]

        cursor1.execute("SELECT okul_id,okul_ad FROM okul_tablo WHERE okul_url= ? AND ilce_id=  ? AND il_id=  ?",(lise_ad,ilce_id,il_id,))
        data3 = cursor1.fetchall()  
        okul_id=data3[0][0]
        okul_ad=data3[0][1]

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2021_sıralama,uni_2021_puan,yeni_mezun,onceki_mezun FROM sayisal_2021 WHERE okul_adı=  ?",(okul_id,))
        data4 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2021_sıralama,uni_2021_puan,yeni_mezun,onceki_mezun FROM esit_2021 WHERE okul_adı=  ?",(okul_id,))
        data5 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2021_sıralama,uni_2021_puan,yeni_mezun,onceki_mezun FROM sozel_2021 WHERE okul_adı=  ?",(okul_id,))
        data6 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2021_sıralama,uni_2021_puan,yeni_mezun,onceki_mezun FROM dil_2021 WHERE okul_adı=  ?",(okul_id,))
        data7 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_2021_sıralama,uni_2021_puan,yeni_mezun,onceki_mezun FROM onlisans_2021 WHERE okul_adı=  ?",(okul_id,))
        data8 = cursor1.fetchall()
    

####################################################################################################################################################################################################

        url_ilce=ilce
        url_il=il

        result1 = []
        result2 = []
        result3 = []
        result4 = []
        result5 = []

        toplam_sayisal=0
        toplam_esit=0
        toplam_sozel=0
        toplam_dil=0
        toplam_onlisans=0

        ayar_func(data4,result1,toplam_sayisal)
        ayar_func(data5,result2,toplam_esit)
        ayar_func(data6,result3,toplam_sozel)
        ayar_func(data7,result4,toplam_dil)
        ayar_func(data8,result5,toplam_onlisans)
        
        return render_template("son.html",toplam_sayisal=toplam_sayisal,toplam_esit=toplam_esit,toplam_sozel=toplam_sozel,toplam_dil=toplam_dil,toplam_onlisans=toplam_onlisans,url_ilce=url_ilce,url_il=url_il,il_ad=il_ad,ilce_ad=ilce_ad,lise_ad=lise_ad,okul_ad=okul_ad,result1=result1,result2=result2,result3=result3,result4=result4,result5=result5, yil="2021",data4=data4,len4=len(data4), data5=data5,len5=len(data5), data6=data6,len6=len(data6), data7=data7,len7=len(data7), data8=data8,len8=len(data8))



@app.route("/il/<string:il>/<string:ilce>/<string:lise_ad>/2020")
def okul_ad_2020(il,ilce,lise_ad):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data1 = cursor1.fetchall()
        il_id=data1[0][0]
        il_ad=data1[0][1]

        cursor1.execute("SELECT ilce_id,ilce_ad FROM ilce_tablo WHERE ilce_url=  ? AND il_id=  ?",(ilce,il_id,))
        data2 = cursor1.fetchall()
        ilce_id=data2[0][0]
        ilce_ad=data2[0][1]

        cursor1.execute("SELECT okul_id,okul_ad FROM okul_tablo WHERE okul_url= ? AND ilce_id=  ? AND il_id=  ?",(lise_ad,ilce_id,il_id,))
        data3 = cursor1.fetchall()  
        okul_id=data3[0][0]
        okul_ad=data3[0][1]


        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2020_siralama,uni_2020_puan,yeni_mezun,onceki_mezun FROM sayisal_2020 WHERE okul_id=  ?",(okul_id,))
        data4 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2020_siralama,uni_2020_puan,yeni_mezun,onceki_mezun FROM esit_2020 WHERE okul_id=  ?",(okul_id,))
        data5 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2020_siralama,uni_2020_puan,yeni_mezun,onceki_mezun FROM sozel_2020 WHERE okul_id=  ?",(okul_id,))
        data6 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2020_siralama,uni_2020_puan,yeni_mezun,onceki_mezun FROM dil_2020 WHERE okul_id=  ?",(okul_id,))
        data7 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2020_siralama,uni_2020_puan,yeni_mezun,onceki_mezun FROM onlisans_2020 WHERE okul_id=  ?",(okul_id,))
        data8 = cursor1.fetchall()
    

####################################################################################################################################################################################################

        url_ilce=ilce
        url_il=il


        result1 = []
        result2 = []
        result3 = []
        result4 = []
        result5 = []

        toplam_sayisal=0
        toplam_esit=0
        toplam_sozel=0
        toplam_dil=0
        toplam_onlisans=0

        ayar_func(data4,result1,toplam_sayisal)
        ayar_func(data5,result2,toplam_esit)
        ayar_func(data6,result3,toplam_sozel)
        ayar_func(data7,result4,toplam_dil)
        ayar_func(data8,result5,toplam_onlisans)
        
        
        return render_template("son.html",toplam_sayisal=toplam_sayisal,toplam_esit=toplam_esit,toplam_sozel=toplam_sozel,toplam_dil=toplam_dil,toplam_onlisans=toplam_onlisans,url_ilce=url_ilce,url_il=url_il,il_ad=il_ad,ilce_ad=ilce_ad,lise_ad=lise_ad,okul_ad=okul_ad,result1=result1,result2=result2,result3=result3,result4=result4,result5=result5, yil="2020",data4=data4,len4=len(data4), data5=data5,len5=len(data5), data6=data6,len6=len(data6), data7=data7,len7=len(data7), data8=data8,len8=len(data8))

@app.route("/il/<string:il>/<string:ilce>/<string:lise_ad>/2019")
def okul_ad_2019(il,ilce,lise_ad):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data1 = cursor1.fetchall()
        il_id=data1[0][0]
        il_ad=data1[0][1]

        cursor1.execute("SELECT ilce_id,ilce_ad FROM ilce_tablo WHERE ilce_url=  ? AND il_id=  ?",(ilce,il_id,))
        data2 = cursor1.fetchall()
        ilce_id=data2[0][0]
        ilce_ad=data2[0][1]

        cursor1.execute("SELECT okul_id,okul_ad FROM okul_tablo WHERE okul_url= ? AND ilce_id=  ? AND il_id=  ?",(lise_ad,ilce_id,il_id,))
        data3 = cursor1.fetchall()  
        okul_id=data3[0][0]
        okul_ad=data3[0][1]

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2019_siralama,uni_2019_puan,yeni_mezun,onceki_mezun FROM sayisal_2019 WHERE okul_id=  ?",(okul_id,))
        data4 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2019_siralama,uni_2019_puan,yeni_mezun,onceki_mezun FROM esit_2019 WHERE okul_id=  ?",(okul_id,))
        data5 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2019_siralama,uni_2019_puan,yeni_mezun,onceki_mezun FROM sozel_2019 WHERE okul_id=  ?",(okul_id,))
        data6 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2019_siralama,uni_2019_puan,yeni_mezun,onceki_mezun FROM dil_2019 WHERE okul_id=  ?",(okul_id,))
        data7 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2019_siralama,uni_2019_puan,yeni_mezun,onceki_mezun FROM onlisans_2019 WHERE okul_id=  ?",(okul_id,))
        data8 = cursor1.fetchall()
    

####################################################################################################################################################################################################

        url_ilce=ilce
        url_il=il


        result1 = []
        result2 = []
        result3 = []
        result4 = []
        result5 = []

        toplam_sayisal=0
        toplam_esit=0
        toplam_sozel=0
        toplam_dil=0
        toplam_onlisans=0

        ayar_func(data4,result1,toplam_sayisal)
        ayar_func(data5,result2,toplam_esit)
        ayar_func(data6,result3,toplam_sozel)
        ayar_func(data7,result4,toplam_dil)
        ayar_func(data8,result5,toplam_onlisans)
        
        
        return render_template("son.html",toplam_sayisal=toplam_sayisal,toplam_esit=toplam_esit,toplam_sozel=toplam_sozel,toplam_dil=toplam_dil,toplam_onlisans=toplam_onlisans,url_ilce=url_ilce,url_il=url_il,il_ad=il_ad,ilce_ad=ilce_ad,lise_ad=lise_ad,okul_ad=okul_ad,result1=result1,result2=result2,result3=result3,result4=result4,result5=result5, yil="2019",data4=data4,len4=len(data4), data5=data5,len5=len(data5), data6=data6,len6=len(data6), data7=data7,len7=len(data7), data8=data8,len8=len(data8))

@app.route("/il/<string:il>/<string:ilce>/<string:lise_ad>/2018")
def okul_ad_2018(il,ilce,lise_ad):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data1 = cursor1.fetchall()
        il_id=data1[0][0]
        il_ad=data1[0][1]

        cursor1.execute("SELECT ilce_id,ilce_ad FROM ilce_tablo WHERE ilce_url=  ? AND il_id=  ?",(ilce,il_id,))
        data2 = cursor1.fetchall()
        ilce_id=data2[0][0]
        ilce_ad=data2[0][1]

        cursor1.execute("SELECT okul_id,okul_ad FROM okul_tablo WHERE okul_url= ? AND ilce_id=  ? AND il_id=  ?",(lise_ad,ilce_id,il_id,))
        data3 = cursor1.fetchall()  
        okul_id=data3[0][0]
        okul_ad=data3[0][1]

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2018_siralama,uni_2018_puan,yeni_mezun,onceki_mezun FROM sayisal_2018 WHERE okul_id=  ?",(okul_id,))
        data4 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2018_siralama,uni_2018_puan,yeni_mezun,onceki_mezun FROM esit_2018 WHERE okul_id=  ?",(okul_id,))
        data5 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2018_siralama,uni_2018_puan,yeni_mezun,onceki_mezun FROM sozel_2018 WHERE okul_id=  ?",(okul_id,))
        data6 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2018_siralama,uni_2018_puan,yeni_mezun,onceki_mezun FROM dil_2018 WHERE okul_id=  ?",(okul_id,))
        data7 = cursor1.fetchall()

        cursor1.execute("SELECT uni_adi,uni_bolum,uni_etiket,uni_fakulte,uni_2018_siralama,uni_2018_puan,yeni_mezun,onceki_mezun FROM onlisans_2018 WHERE okul_id=  ?",(okul_id,))
        data8 = cursor1.fetchall()
    

####################################################################################################################################################################################################

        url_ilce=ilce
        url_il=il


        result1 = []
        result2 = []
        result3 = []
        result4 = []
        result5 = []

        toplam_sayisal=0
        toplam_esit=0
        toplam_sozel=0
        toplam_dil=0
        toplam_onlisans=0

        ayar_func(data4,result1,toplam_sayisal)
        ayar_func(data5,result2,toplam_esit)
        ayar_func(data6,result3,toplam_sozel)
        ayar_func(data7,result4,toplam_dil)
        ayar_func(data8,result5,toplam_onlisans)
        
        return render_template("son.html",toplam_sayisal=toplam_sayisal,toplam_esit=toplam_esit,toplam_sozel=toplam_sozel,toplam_dil=toplam_dil,toplam_onlisans=toplam_onlisans,url_ilce=url_ilce,url_il=url_il,il_ad=il_ad,ilce_ad=ilce_ad,lise_ad=lise_ad,okul_ad=okul_ad,result1=result1,result2=result2,result3=result3,result4=result4,result5=result5, yil="2018",data4=data4,len4=len(data4), data5=data5,len5=len(data5), data6=data6,len6=len(data6), data7=data7,len7=len(data7), data8=data8,len8=len(data8))


#il********************************************************************************
@app.route("/secenek")
def secenek():

        return render_template("secenek.html")


@app.route("/il_siralama_secme")
def secenek_il():

    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()
        cursor1.execute("SELECT il_ad,il_url FROM il_tablo_alfabetik")
        data1 = cursor1.fetchall()
                    
        return render_template("il_siralama_1.html", data1=data1 ,len1=len(data1))


@app.route("/il_siralama_secme/<string:il>")
def il_secme(il):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data_il = cursor1.fetchall()#data_il = il_url
        il_ad=data_il[0][1]
        data_il=data_il[0][0]

        cursor1.execute("SELECT sayisal_2021_yeni,sayisal_2021_eski,sayisal_2020_yeni,sayisal_2020_eski,sayisal_2019_yeni,sayisal_2019_eski,sayisal_2018_yeni,sayisal_2018_eski,esit_2021_yeni,esit_2021_eski,esit_2020_yeni,esit_2020_eski,esit_2019_yeni,esit_2019_eski,esit_2018_yeni,esit_2018_eski,sozel_2021_yeni,sozel_2021_eski,sozel_2020_yeni,sozel_2020_eski,sozel_2019_yeni,sozel_2019_eski,sozel_2018_yeni,sozel_2018_eski,dil_2021_yeni,dil_2021_eski,dil_2020_yeni,dil_2020_eski,dil_2019_yeni,dil_2019_eski,dil_2018_yeni,dil_2018_eski,onlisans_2021_yeni,onlisans_2021_eski,onlisans_2020_yeni,onlisans_2020_eski,onlisans_2019_yeni,onlisans_2019_eski,onlisans_2018_yeni,onlisans_2018_eski FROM il_sayilar_tablo_2021 WHERE il_id=  ?",(data_il,))
        data1 = cursor1.fetchall()
        data1=data1[0]   

        return render_template("il_siralama_2.html",il_ad=il_ad,data1=data1)


@app.route("/ilce_siralama_secme")
def secenek_ilce():

    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()
        cursor1.execute("SELECT il_ad,il_url FROM il_tablo_alfabetik")
        data1 = cursor1.fetchall()
    
        return render_template("ilce_siralama_1.html", data1=data1 ,len1=len(data1))


@app.route("/ilce_siralama_secme/<string:il>")
def ilce_secme_1(il):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad,il_url FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data1 = cursor1.fetchall()
        il_url=data1[0][2]
        il_ad=data1[0][1]
        data1=data1[0][0]
        
        cursor1.execute("SELECT ilce_ad,ilce_url FROM ilce_tablo_alfabetik WHERE il_id=  ?",(data1,))
        data2 = cursor1.fetchall()
                
        return render_template("ilce_siralama_2.html", data2=data2 ,len2=len(data2),il_ad=il_ad,il_url=il_url)


@app.route("/ilce_siralama_secme/<string:il>/<string:ilce>")
def ilce_felan(il,ilce):
    with sqlite3.connect("database.db") as con1:
        cursor1 = con1.cursor()

        cursor1.execute("SELECT il_id,il_ad FROM il_tablo_alfabetik WHERE il_url=  ?",(il,))
        data_il = cursor1.fetchall()
        il_ad=data_il[0][1]
        data_il=data_il[0][0]

        cursor1.execute("SELECT ilce_id,ilce_ad FROM ilce_tablo WHERE il_id = ? AND ilce_url=?",(data_il,ilce,))
        data_ilce = cursor1.fetchall()
        ilce_ad=data_ilce[0][1]
        data_ilce=data_ilce[0][0]

        cursor1.execute("SELECT sayisal_2021_yeni,sayisal_2021_eski,sayisal_2020_yeni,sayisal_2020_eski,sayisal_2019_yeni,sayisal_2019_eski,sayisal_2018_yeni,sayisal_2018_eski,esit_2021_yeni,esit_2021_eski,esit_2020_yeni,esit_2020_eski,esit_2019_yeni,esit_2019_eski,esit_2018_yeni,esit_2018_eski,sozel_2021_yeni,sozel_2021_eski,sozel_2020_yeni,sozel_2020_eski,sozel_2019_yeni,sozel_2019_eski,sozel_2018_yeni,sozel_2018_eski,dil_2021_yeni,dil_2021_eski,dil_2020_yeni,dil_2020_eski,dil_2019_yeni,dil_2019_eski,dil_2018_yeni,dil_2018_eski,onlisans_2021_yeni,onlisans_2021_eski,onlisans_2020_yeni,onlisans_2020_eski,onlisans_2019_yeni,onlisans_2019_eski,onlisans_2018_yeni,onlisans_2018_eski FROM ilce_sayilar_tablo_2021 WHERE ilce_id=  ?",(data_ilce,))
        data1 = cursor1.fetchall()
        data1=data1[0]   

        return render_template("ilce_siralama_3.html",il_ad=il_ad,ilce_ad=ilce_ad,data1=data1)


if __name__ == "__main__":
    app.run(debug=False) 
