import Plagiarisme

def GetHasilPlag():
    global y_plagiarisme
    
    text="Arab Saudi semakin meningkatkan kehadirannya di dunia sepak bola dalam beberapa bulan terakhir, dimulai dengan pembelian Newcastle United dan penandatanganan Cristiano Ronaldo. Setelah itu, dana investasi negara PIF mendukung empat klub yang sangat aktif di bursa transfer musim panas."
    get_hasil = Plagiarisme.CekPlag(text)
    ngelist = get_hasil["highlight"]
    HighL=[]
    for i,x in enumerate(text.split()):
        status_HL = False
        for j in ngelist:
            a = int(j[0])
            b = int(j[1])
            if int(i)>=a and int(i)<=b:
                HighL.append(x.upper())
                status_HL = True
                break
        if not status_HL:
            HighL.append(x)

    if get_hasil["matches"]:
        for sumber in get_hasil["matches"]:
            print(sumber)
    if get_hasil["error_code"] == 0 and get_hasil["error"] == "":
        print(f"""
        Text : {text}
        Unik : {get_hasil["percent"].replace(".0", "")}%
        Plagiat : {100 - float(get_hasil["percent"]):.1f}%
        Highlight : {" ".join(HighL)}
        Matches : {get_hasil["matches"][0]}
        Jumlah kata : {len(text.split())}
        """)
    else:
        print("gagal")
    {
        "error":"",
        "error_code":0,
        "text":"azilul mengatakan hasil survei itu justru menjadi pelecut semangat kerja barisan anies-cak imin dikonfirmsi perihal dukungan anies-cak imin menurun karena belum maksimal bersosialisasi di pesantren di jawa timur2cjazilul bertutur itu akan terus dilakukan","percent":"84.2","highlight":[["1","3"],["6","7"]],"matches":[{"url":"https:\/\/news.detik.com\/pemilu\/d-6584016\/nasdem-tak-masalah-anies-merosot-di-survei-litbang-kompas-jadi-pelecut",
        "percent":"15.8",
        "highlight":[
            ["1","3"],
            ["6","7"]
        ]}],
        "title":"",
        "words_count":33
    }

GetHasilPlag()