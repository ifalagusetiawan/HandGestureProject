import cv2
from detector import HandDetector
import gesture
import music

def main():
    # Inisialisasi kamera dan detektor tangan
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detection_con=0.7)
    
    music_status = "STOPPED"

    while True:
        success, img = cap.read()
        if not success:
            break

        # Balik gambar biar kayak cermin
        img = cv2.flip(img, 1)
        
        # Deteksi tangan
        img = detector.find_hands(img)
        lm_list = detector.get_position(img)

        if len(lm_list) != 0:
            # Hitung jumlah jari yang terbuka
            total_fingers = gesture.count_fingers(lm_list)

            # LOGIKA KONTROL MUSIK
            # Contoh: Jika 5 jari terbuka -> PLAY. Jika mengepal (0 jari) -> PAUSE
            if total_fingers == 5:
                music.play_music("music.mp3")
                music_status = "PLAYING"
            elif total_fingers == 0:
                music.pause_music()
                music_status = "PAUSED"

        # Tampilkan teks status di layar (Warna hijau: (0, 255, 0))
        cv2.putText(
            img, 
            f"Music : {music_status}", 
            (50, 80), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1.2, 
            (0, 255, 0), 
            3
        )

        # Tampilkan window aplikasi
        cv2.imshow("Hand Gesture Music Controller", img)

        # Tekan 'q' untuk keluar dari aplikasi
        if cv2.waitKey(1) & 0xFF == ord('q'):
            music.stop_music()
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()