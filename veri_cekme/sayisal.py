from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import sqlite3 
#Kütüphaneyi oluştur ve fonksiyonları yaz
con = sqlite3.connect("database.db")

cursor = con.cursor() 

def tablo_oluştur_2023_sayisal():
    cursor.execute("""CREATE TABLE IF NOT EXISTS sayisal_2023 (
    uni_adi TEXT,
    uni_bolum TEXT,
    uni_etiket TEXT,
    uni_fakülte TEXT,
    uni_sehir TEXT,
    uni_tur TEXT,
    uni_ucret TEXT,
    uni_ogretim_turu TEXT,
    uni_2023_kontenjan INT,
    uni_2023_sıralama INT,
    uni_2023_puan FLOAT,
    okul_adı TEXT,
    lise_il TEXT,
    lise_ilce TEXT,
    yeni_mezun INT,
    onceki_mezun INT,
    PRIMARY KEY (uni_adi, uni_bolum, uni_etiket, uni_fakülte, uni_sehir, uni_tur, uni_ucret, uni_ogretim_turu, uni_2023_kontenjan, uni_2023_sıralama, uni_2023_puan, okul_adı, lise_il, lise_ilce, yeni_mezun, onceki_mezun)
);""") 
    con.commit()

def deger_ekle_2023_sayisal(uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_sehir,uni_tur,uni_ucret,uni_ogretim_turu,uni_2023_kontenjan,uni_2023_sıralama,uni_2023_puan,okul_adı,lise_il,lise_ilce,yeni_mezun,onceki_mezun):
    cursor.execute("INSERT INTO sayisal_2023 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(uni_adi,uni_bolum,uni_etiket,uni_fakülte,uni_sehir,uni_tur,uni_ucret,uni_ogretim_turu,uni_2023_kontenjan,uni_2023_sıralama,uni_2023_puan,okul_adı,lise_il,lise_ilce,yeni_mezun,onceki_mezun))
    con.commit()#23

def il_deger_ekle(il_id,il_ad,il_url):
    cursor.execute("INSERT INTO il_tablo VALUES(?,?,?)",(il_id,il_ad,il_url))
    con.commit()

def ilce_deger_ekle(ilce_id,ilce_ad,ilce_url,il_id):
    cursor.execute("INSERT INTO ilce_tablo VALUES(?,?,?,?)",(ilce_id,ilce_ad,ilce_url,il_id))
    con.commit()

def okul_deger_ekle(okul_id, okul_ad, okul_url, il_id, ilce_id):
    cursor.execute("INSERT INTO okul_tablo (okul_id, okul_ad, okul_url, il_id, ilce_id) VALUES (?, ?, ?, ?, ?)",(okul_id, okul_ad, okul_url, il_id, ilce_id))
    con.commit()

tablo_oluştur_2023_sayisal()

#selenium sitesini ayarla

driver = webdriver.Chrome()

driver.maximize_window()#tam ekran yapma



url = "https://yokatlas.yok.gov.tr/tercih-sihirbazi-t4-tablo.php?p=say"

driver.get(url)


time.sleep(5)

select_element = driver.find_element("name","mydata_length")

# Seçim kutusunu kullanarak Select nesnesi oluştur
select = Select(select_element)

# Seçimi yap
select.select_by_value("100") 

time.sleep(60)

element = driver.find_element("xpath","//ul[@class='pagination']/li[last()-1]/a")

# Öğenin metnini alın
sayfa_sayısı = element.text

time.sleep(2)

# a=3
sayfa_sayac=1


# sayfa 50 e kaldı

while sayfa_sayac!=sayfa_sayısı:
        # try:
                print("sayfa sayaç")
                print(sayfa_sayac)
                
                time.sleep(5)

                uniadi_list=[]
                unibolum_list=[]
                unisehir_list=[]
                unitur_list=[]
                uniucret_list=[]
                uniogretimturu_list=[]
                uni2023kontenjan_list=[]
                uni2023sıralama_list=[]
                uni2023puan_list=[]

                uni_sayac=0

                #UNİADİ
                uniadi=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[3]/strong')
                uniadi_list=[]

                    
                for lise_ad in uniadi:      
                    try:
                        txt=lise_ad.text
                        uniadi_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)

                #UNİBÖLÜM
                unibolum=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[4]/strong')
                unibolum_list=[]
                    
                for lise_ad in unibolum:      
                    try:
                        txt=lise_ad.text
                        unibolum_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)
                #UNİETİKET
                unietiket=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[4]/font')
                unietiket_list=[]
                    
                for lise_ad in unietiket:      
                    try:
                        txt=lise_ad.text
                        unietiket_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)
                #UNİFAKÜLTE
                unifakülte=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[3]/font')
                unifakülte_list=[]
                    
                for lise_ad in unifakülte:      
                    try:
                        txt=lise_ad.text
                        unifakülte_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)
                #UNİŞEHİR
                unisehir=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[5]')
                unisehir_list=[]
                    
                for lise_ad in unisehir:      
                    try:
                        txt=lise_ad.text
                        unisehir_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)
                #UNİTÜR
                unitur=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[6]')
                unitur_list=[]
                    
                for lise_ad in unitur:      
                    try:
                        txt=lise_ad.text
                        unitur_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)
                #UNİÜCRET
                uniucret=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[7]')
                uniucret_list=[]
                    
                for lise_ad in uniucret:      
                    try:
                        txt=lise_ad.text
                        uniucret_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)
                #UNİÖĞRETİMTÜRÜ
                uniogretimturu=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[8]')
                uniogretimturu_list=[]
                    
                for lise_ad in uniogretimturu:      
                    try:
                        txt=lise_ad.text
                        uniogretimturu_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)
                #2023KONTEJYAN
                uni2023kontenjan=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[11]/font[1]')
                uni2023kontenjan_list=[]
                    
                for lise_ad in uni2023kontenjan:      
                    try:
                        txt=lise_ad.text
                        uni2023kontenjan_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)

                #2023SIRA
                uni2023sıralama=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[12]/font[1]')
                uni2023sıralama_list=[]
                    
                for lise_ad in uni2023sıralama:      
                    try:
                        txt=lise_ad.text
                        txt="['"+txt+"']"
                        uni2023sıralama_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)

                #2023PUAN
                uni2023puan=driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[13]/font[1]')
                uni2023puan_list=[]
                    
                for lise_ad in uni2023puan:      
                    try:
                        txt=lise_ad.text
                        uni2023puan_list.append(txt)
                    except Exception as e:
                        print("An error occurred:", e)     
                
                #liste son
                meci = driver.find_elements("xpath", '//*[@id="mydata"]/tbody/tr/td[2]/a[1]')
                for items in meci:
                    href = items.get_attribute('href')
                    if len(href)==69:
                        continue
                    
                    tab_url = href
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(tab_url)

                    #popup ı kapatma


                    try:
                        popup=driver.find_element("xpath",'/html/body/div[4]/div/span')

                        if popup:
                            popup.click()
                            time.sleep(1)
                    
                    except:
                        pass
                    
                    try:
                        popup=driver.find_element("xpath",'/html/body/div[3]/div/span')

                        if popup:
                            popup.click()
                            time.sleep(1)
                    
                    except:
                        pass


                    #SAYFAYI AÇTIK SAFYA İÇİ İŞLEM BURADA
                    #2023 işlemler burada

                    # Getting current URL source code 
                    get_title = driver.title 
                    
                    driver.find_element("xpath",'//*[@id="h1060"]/a/h4').click()
                    time.sleep(2)
                    sayac=1
                    try:
                            #LİSE
                        i=driver.find_elements("xpath", '//*[@id="icerik_1060"]/table/tbody/tr/td[1]')
                        lise_list=[]
                        
                        for lise_ad in i:
                            
                            try:
                                txt=lise_ad.text
                                lise_list.append(txt)
                            except Exception as e:
                                print("An error occurred:", e)
                        #TOPLAM KİŞİ SAYISI
                        i=driver.find_elements("xpath", '//*[@id="icerik_1060"]/table/tbody/tr/td[2]')
                        toplam_list=[]

                        for lise_ad in i:
                            try:
                                txt=lise_ad.text
                                txt=int(txt)
                                toplam_list.append(txt)
                            except Exception as e:
                                print("An error occurred:", e)
                        #YENİ MEZUN SAYISI
                        i=driver.find_elements("xpath", '//*[@id="icerik_1060"]/table/tbody/tr/td[3]')
                        yeni_mezun_list=[]
                        
                        for lise_ad in i:
                            try:
                                txt=lise_ad.text
                                if txt=="---":
                                    txt=0
                                txt=int(txt)
                                yeni_mezun_list.append(txt)
                            except Exception as e:
                                print("An error occurred:", e)
                            
                        #ÖNCEKİ MEZUN SAYISI
                        i=driver.find_elements("xpath", '//*[@id="icerik_1060"]/table/tbody/tr/td[4]')
                        onceki_mezun_list=[]

                        for lise_ad in i:
                            
                            try:
                                txt=lise_ad.text
                                if txt=="---":
                                    txt=0
                                txt=int(txt)
                                onceki_mezun_list.append(txt)
                            except Exception as e:
                                print("An error occurred:", e)
                        genel_toplam_list=[]   
                        genel_toplam_list=zip(lise_list,toplam_list,yeni_mezun_list,onceki_mezun_list)
                        genel_toplam_list=list(genel_toplam_list)
                        
                        time.sleep(1)
                        #listeyi veritabanına ekliyoruz
                        
                        lise_ad_liste_ici=[]
                        lise_il_liste_ici=[]
                        lise_ilçe_liste_ici=[]
                        lise_toplam_kisi_liste_ici=[]
                        lise_yeni_mezun_kisi_liste_ici=[]
                        lise_eski_mezun_liste_ici=[]
                        genel_toplam_list.pop(0)

                        time.sleep(1)

                        for i in genel_toplam_list:
                            i=str(i)
                            i = i.replace("(", "")
                            i = i.replace(")", "")
                            i = i.replace("'", "")
                            i=i.split(", ")
                            lise_parca=i[0].replace("- ","")
                            lise_parca=lise_parca.split()
                            lise_ilçe_liste_ici.append(lise_parca[-1])    
                            lise_il_liste_ici.append(lise_parca[-2])
                            lise_parca.pop()
                            lise_parca.pop()
                            lise_parca = ' '.join([str(elem) for elem in lise_parca])   
                            
                            lise_ad_liste_ici.append(lise_parca)
                            lise_eski_mezun_liste_ici.append(i[-1])
                            lise_yeni_mezun_kisi_liste_ici.append(i[-2])
                            lise_toplam_kisi_liste_ici.append(i[-3])
                            
                            #üni_bilgi ilk sayfadaki üniversitelerin bilgileri
                            üni_bilgi = list(zip(uniadi_list,unibolum_list,unietiket_list,unifakülte_list,unisehir_list,unitur_list,uniucret_list,uniogretimturu_list,uni2023kontenjan_list,uni2023sıralama_list,uni2023puan_list))
                            lise_bilgi = list(zip(lise_ad_liste_ici,lise_il_liste_ici,lise_ilçe_liste_ici,lise_yeni_mezun_kisi_liste_ici,lise_eski_mezun_liste_ici))
                        
                        x=list(üni_bilgi)[uni_sayac]         
                        b=list(lise_bilgi)

                        uni_sayac+=1


                        for k in b:

                            cursor.execute("Select il_id From il_tablo where il_ad  = ?",(k[1],))
                            data = cursor.fetchall()
                            il_id=""
                            # try:
                            for i in data:
                                il_id=int(i[0])
                            # except:
                            #     pass


                            cursor.execute("SELECT il_id FROM il_tablo ORDER BY il_id DESC LIMIT 1;")

                            data = cursor.fetchall()
                            en_son_il_id=data[0][0]+1


                            if il_id=="":
                                il_adi=k[1]

                                il_adi_url=il_adi

                                il_adi_url=il_adi_url.lower()
                                il_adi_url=il_adi_url.replace("ş","s")
                                il_adi_url=il_adi_url.replace("ç","c")
                                il_adi_url=il_adi_url.replace("ö","o")
                                il_adi_url=il_adi_url.replace("ğ","g")
                                il_adi_url=il_adi_url.replace("ı","i")
                                il_adi_url=il_adi_url.replace("i̇","i")
                                il_adi_url=il_adi_url.replace("ü","u")
                                il_adi_url=il_adi_url.replace(" ","-")
                                
                                il_deger_ekle(en_son_il_id,il_adi,il_adi_url)
                                

                            #*************ilçe******************

                            cursor.execute("Select ilce_id From ilce_tablo where il_id = ? AND ilce_ad = ?",(il_id,k[2],))
                            data = cursor.fetchall()
                            ilce_id=""
                            try:
                                for i in data:
                                    ilce_id=int(i[0])
                            except:
                                pass

                            #ilçe yoksa

                            #ilce_id,ilce_ad,ilce_url,il_id):

                            #en son 978 ilce_id
                            cursor.execute("SELECT ilce_id FROM ilce_tablo ORDER BY ilce_id DESC LIMIT 1;")

                            data = cursor.fetchall()
                            en_son_ilce_id=data[0][0]+1

                            if ilce_id=="" or None:
                                ilce_adi=k[2]

                                ilce_adi_url=ilce_adi

                                ilce_adi_url=ilce_adi_url.lower()
                                ilce_adi_url=ilce_adi_url.replace("ş","s")
                                ilce_adi_url=ilce_adi_url.replace("ç","c")
                                ilce_adi_url=ilce_adi_url.replace("ö","o")
                                ilce_adi_url=ilce_adi_url.replace("ğ","g")
                                ilce_adi_url=ilce_adi_url.replace("ı","i")
                                ilce_adi_url=ilce_adi_url.replace("i̇","i")
                                ilce_adi_url=ilce_adi_url.replace("ü","u")
                                ilce_adi_url=ilce_adi_url.replace(" ","-")
                                
                                ilce_deger_ekle(en_son_ilce_id,ilce_adi,ilce_adi_url,il_id)


                            cursor.execute("Select okul_id From okul_tablo where il_id = ? AND ilce_id = ? AND okul_ad= ?",(il_id,ilce_id,k[0]))
                            data = cursor.fetchall()
                            okul_id=""
                            try:
                                for i in data:
                                    okul_id=int(i[0])
                            except:
                                pass


                            if okul_id=="" or None:
                                cursor.execute("SELECT okul_id FROM okul_tablo ORDER BY okul_id DESC LIMIT 1;")

                                data = cursor.fetchall()
                                en_son_okul_id=data[0][0]+1

                                okul_adi=k[0]
                                okul_adi_url=okul_adi

                                okul_adi_url=okul_adi_url.lower()
                                okul_adi_url=okul_adi_url.replace("ş","s")
                                okul_adi_url=okul_adi_url.replace("ç","c")
                                okul_adi_url=okul_adi_url.replace("ö","o")
                                okul_adi_url=okul_adi_url.replace("ğ","g")
                                okul_adi_url=okul_adi_url.replace("ı","i")
                                okul_adi_url=okul_adi_url.replace("i̇","i")
                                okul_adi_url=okul_adi_url.replace("ü","u")
                                okul_adi_url=okul_adi_url.replace(" ","-")


                                okul_deger_ekle(en_son_okul_id,okul_adi,okul_adi_url,il_id,ilce_id)

                                try:
                                    deger_ekle_2023_sayisal(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],en_son_okul_id,il_id,ilce_id,k[3],k[4])
                                except:
                                    pass
                            else:    
                                
                                try:
                                    deger_ekle_2023_sayisal(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],okul_id,il_id,ilce_id,k[3],k[4])
                        
                                except:
                                    pass
                    except:
                        uni_sayac+=1
                        pass   
                    
                    #SAYFAYI KAPATIYORUZ
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                time.sleep(1)
                sayfa_sayac+=1
                ana_sayfa=driver.find_element("xpath",'//*[@id="mydata_next"]')
                
                ana_sayfa.click()
        
driver.quit()