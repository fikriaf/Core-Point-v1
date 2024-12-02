import MemoryCoreFlash as cf

def PostCoreFlash(inp):
    for cek in cf.memori:
        if inp == cek:
            return "[Failed! You Have Been Submitted This Parameters]"
    sementara = []
    for i in cf.memori:
        sementara.append(i.lower())
    sementara.append(inp)
    open("MemoryCoreFlash.py", "w", encoding="utf-8").write(f"memori = {sementara}")
    return "[Submit Into Memory Is Successful]"

def GetCoreFlash(query):
    list_hasil = []
    for urut in query.split():
        for s in cf.memori:
            if urut in s and s not in list_hasil:
                list_hasil.append(s)

    return list_hasil
