def relevan_konteks(db,pesan_user):
    kalimat=pesan_user.lower().split()

    hasil=[]
    for konteks in db:
        konteks=konteks.lower()
        for kata in kalimat:
            if kata in konteks:
                hasil.append(konteks)
                break
            
    return hasil
