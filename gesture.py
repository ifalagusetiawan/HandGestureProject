def count_fingers(lm_list):
    """
    Fungsi sederhana untuk menghitung jumlah jari yang berdiri.
    Menggunakan koordinat ujung jari vs sendi di bawahnya.
    """
    if len(lm_list) == 0:
        return -1  # Tidak ada tangan terdeteksi

    fingers = []
    # ID Landmark ujung jari: Jempol (4), Telunjuk (8), Tengah (12), Manis (16), Kelingking (20)
    tip_ids = [4, 8, 12, 16, 20]

    # Jempol (Logikanya agak beda karena gerak horizontal, bandingkan koordinat X)
    # Ini asumsi untuk tangan kanan
    if lm_list[tip_ids[0]][1] > lm_list[tip_ids[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # 4 Jari lainnya (Bandingkan koordinat Y)
    for id in range(1, 5):
        if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)  # Mengembalikan total jari yang terbuka (0 - 5)
