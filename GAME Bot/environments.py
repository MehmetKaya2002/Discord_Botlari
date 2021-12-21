from datetime import datetime

import discord

TOKEN = "BURAYA DİSCORD BOT TOKENİ GELİR"
TIME_STAMP_PATTERN = "%d/%m/%Y, %H:%M:%S"

def is_more_than_ten_minute(time: str):
    datetime_obj = datetime.strptime(time,TIME_STAMP_PATTERN)
    now = datetime.now()

    hesaplanan_time = now - datetime_obj

    return bool(hesaplanan_time.seconds // 600)
def meslek_adi(job):
    if job == "0":
        return "İşsiz"
    if job == "1":
        return "CEO"
    if job == "2":
        return "Cerrah"
    if job == "3":
        return "Diş Hekimi"
    if job == "4":
        return "Bilgisayar Mühendisi"
    if job == "5":
        return "Avukat"
    if job == "6":
        return "Polis"
    if job == "7":
        return "İtfaye Eri"
    if job == "8":
        return "Memur"
    if job == "9":
        return "Astronot Jeff Bezos"

def meslek_secim_fonksiyonu(secilen_meslek_numarasi,id,mention,para,tarih):
    try:
        if secilen_meslek_numarasi == 2: #cerrah 250.000 coin
            print("meslek numarası 2")
            if para - 250000 >= 0:
                print("parası var")

                para -= 250000
                sayi = "2"
                meslek_name =meslek_adi(sayi)
                print(meslek_name)

                file = open(f"{id}.txt", "w")
                file.write(f"{mention}//{para}//{tarih}//{sayi}")
                file.close()
                print("dosya kapandı")

                return f"Artık mesleğiniz : {meslek_name}"
            else:
                print("eksik bakiye")
                return f"Yeterli Bakiyeniz Bulunmamakta !\n Güncel Bakiyeniz : {para}\n {250000 - para} Coine ihtiyacınız var"
        if secilen_meslek_numarasi == 3: #diş hekimi 190.000 coin
            if para - 190000 >= 0:

                para -= 190000
                sayi = "3"
                meslek_name =meslek_adi(sayi)
                print(meslek_name)

                file = open(f"{id}.txt", "w")
                file.write(f"{mention}//{para}//{tarih}//{sayi}")
                file.close()
                print("dosya kapandı")

                return f"Artık mesleğiniz : {meslek_name}"
            else:
                print("eksik bakiye")
                return f"Yeterli Bakiyeniz Bulunmamakta !\n Güncel Bakiyeniz : {para}\n {190000 - para} Coine ihtiyacınız var"
        if secilen_meslek_numarasi == 4: #bilg müh 150.000 coin
            if para - 150000 >= 0:

                para -= 150000
                sayi = "4"
                meslek_name =meslek_adi(sayi)

                file = open(f"{id}.txt", "w")
                file.write(f"{mention}//{para}//{tarih}//{sayi}")
                file.close()


                return f"Artık mesleğiniz : {meslek_name}"
            else:
                print("eksik bakiye")
                return f"Yeterli Bakiyeniz Bulunmamakta !\n Güncel Bakiyeniz : {para}\n {150000 - para} Coine ihtiyacınız var"
        if secilen_meslek_numarasi == 5: #avukat 60.000 coin
            if para - 60000 >= 0:
                para -= 60000
                sayi = "5"
                meslek_name =meslek_adi(sayi)
                print(meslek_name)

                file = open(f"{id}.txt", "w")
                file.write(f"{mention}//{para}//{tarih}//{sayi}")
                file.close()
                print("dosya kapandı")

                return f"Artık mesleğiniz : {meslek_name}"
            else:
                print("eksik bakiye")
                return f"Yeterli Bakiyeniz Bulunmamakta !\n Güncel Bakiyeniz : {para}\n {60000 - para} Coine ihtiyacınız var"
        if secilen_meslek_numarasi == 6: #polis 25.000 coin
            if para - 25000 >= 0:

                para -= 25000
                sayi = "6"
                meslek_name =meslek_adi(sayi)
                print(meslek_name)

                file = open(f"{id}.txt", "w")
                file.write(f"{mention}//{para}//{tarih}//{sayi}")
                file.close()
                print("dosya kapandı")

                return f"Artık mesleğiniz : {meslek_name}"
            else:
                print("eksik bakiye")
                return f"Yeterli Bakiyeniz Bulunmamakta !\n Güncel Bakiyeniz : {para}\n {25000 - para} Coine ihtiyacınız var"
        if secilen_meslek_numarasi == 7: #itfaye 25.000 coin
            if para - 25000 >= 0:


                para -= 25000
                sayi = "7"
                meslek_name =meslek_adi(sayi)
                print(meslek_name)

                file = open(f"{id}.txt", "w")
                file.write(f"{mention}//{para}//{tarih}//{sayi}")
                file.close()
                print("dosya kapandı")

                return f"Artık mesleğiniz : {meslek_name}"
            else:
                print("eksik bakiye")
                return f"Yeterli Bakiyeniz Bulunmamakta !\n Güncel Bakiyeniz : {para}\n {25000 - para} Coine ihtiyacınız var"
        if secilen_meslek_numarasi == 8: #memur 10.000 coin
            if para - 10000 >= 0:

                para -= 10000
                sayi = "8"
                meslek_name =meslek_adi(sayi)
                print(meslek_name)

                file = open(f"{id}.txt", "w")
                file.write(f"{mention}//{para}//{tarih}//{sayi}")
                file.close()
                print("dosya kapandı")

                return f"Artık mesleğiniz : {meslek_name}"
            else:
                print("eksik bakiye")
                return f"Yeterli Bakiyeniz Bulunmamakta !\n Güncel Bakiyeniz : {para}\n {10000 - para} Coine ihtiyacınız var"
        if secilen_meslek_numarasi == 9: #cerrah 200.000.000.000 coin
            if para - 200000000000 >= 0:

                para -= 200000000000
                sayi = "9"
                meslek_name =meslek_adi(sayi)
                print(meslek_name)

                file = open(f"{id}.txt", "w")
                file.write(f"{mention}//{para}//{tarih}//{sayi}")
                file.close()
                print("dosya kapandı")

                return f"Artık mesleğiniz : {meslek_name}"
            else:
                print("eksik bakiye")
                return f"Yeterli Bakiyeniz Bulunmamakta !\n Güncel Bakiyeniz : {para}\n {200000000000 - para} Coine ihtiyacınız var"
        if secilen_meslek_numarasi == 1:
            if id != 343051107788128256:
                return f"Yetkiniz yok"
            else:
                return "Mehmet BEY siz zaten CEO'sunuz"
        else:
            return f"Lütfen 1-9 arasında bir seçim yapın"

    except:
        return "BİR HATA OLUŞTU LÜTFEN DEVELOPER İLE İLETİŞİME GEÇİN MehmetK#6655"



def create_embed(title = "",description = "",color1 = 0,color2 = 0,color3 = 0,url = "https://www.com"):
    embed = discord.Embed(title=title,description=description,colour=discord.Colour.from_rgb(color1,color2,color3),url=url)

    return embed



