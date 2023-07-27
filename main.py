import streamlit as st

def main():
    st.title("Rundown Acara")
    st.write("Berikut adalah daftar acara yang akan diselenggarakan:")
    st.header("Day 1: Wednesday, 9 August 2023")

    events_day1 = [
        {"Time": "08:30 - 08:40", "Main Room": "Opening Day 1: traditional dance by UKM Sunda", "deskripsi": "Peserta tiba dan mendaftar."},
        {"Time": "08:40 - 08:50", "Main Room": "Speech by General Chair Representation", "deskripsi": "Pembukaan acara oleh panitia."},
        {"Time": "08:50 - 09:00", "Main Room": "Speech by IEEE IS Representative: Prof. Ir. Gamantyo Hendrantoro", "deskripsi": "Seminar tentang topik menarik."},
        {"Time": "09:00 - 09:10", "Main Room": "Opening Speech by Rector of Telkom University: Prof. Dr. Adiwijaya", "deskripsi": "Workshop dengan praktik langsung."},
        {"Time": "09:10 - 09:20", "Main Room": "Photo Session", "deskripsi": "Waktu untuk makan siang bersama."},
        {"Time": "09:20 - 10:20", "Main Room": "Keynote Speech 1: Dr. Syed Zainudeen Mohd Shaid Dell, MY Topic: TBA Moderator: UTM - Dr. Hajar", "deskripsi": "Diskusi tentang isu-isu terkini."},
        {"Time": "10:20 - 10:30", "Main Room": "Coffee Break", "deskripsi": "Lomba dengan hadiah menarik."},
        {"Time": "10:30 - 12:00", "Main Room": "Workshop Session #1", "deskripsi": "Penutupan acara."},
        {"Time": "12:00 - 13:00", "Main Room": "Lunch Break", "deskripsi": "Penutupan acara."},
        {"Time": "13:00 - 14:30", "Main Room": "Keynote Speech 2: Prof. Kamal Bechkoum Head of the School of Computing and Engineering, University of Gloucestershire, UK (60')Topic: TBA Moderator: Pak Rio Guntur", "deskripsi": "Penutupan acara."},
        {"Time": "14:30 - 14:40", "Main Room": "Coffee Break", "deskripsi": "Penutupan acara."},
        {"Time": "14:40 - 16:10", "Main Room": "Keynote Speech #3: Dr. Owen Johnson Senior Fellow, University of Leeds, UK (60') Topic: TBA Moderator: Bu Ima", "deskripsi": "Penutupan acara."},
        {"Time": "16:10 - 16:15", "Main Room": "Closing Day 1", "deskripsi": "Penutupan acara."},
    ]

    # Tampilkan daftar acara dalam bentuk tabel
    st.table(events_day1)

    st.header("Day 2: Thursday, 10 August 2023")
    events_day2 = [
        {"Time": "08:30 - 08:45", "Main Room": "Opening Day 2", "deskripsi": "Peserta tiba dan mendaftar."},
        {"Time": "08:45 - 10:15", "Main Room": "Keynote Speech 4: Prof. Ts. Dr. Rabiah Ahmad Professor of Computer Science, Universiti Tun Hussien Onn Malaysia, MY (60') Topic: TBA Moderator: UTM", "deskripsi": "Pembukaan acara oleh panitia."},
        {"Time": "10:15 - 10:25", "Main Room": "Coffee Break", "deskripsi": "Seminar tentang topik menarik."},
        {"Time": "10:25 - 11:55", "Main Room": "Workshop Session #2 - Pak Putu", "deskripsi": "Workshop dengan praktik langsung."},
        {"Time": "11:55 - 12:05", "Main Room": "Closing Speech by Vice-Chancellor of UTM: Prof. Datuk Ir. Ts. Dr. Ahmad Fauzi bin Ismail", "deskripsi": "Waktu untuk makan siang bersama."},
        {"Time": "12:05 - 12:20", "Main Room": "Awards Ceremony and Closing", "deskripsi": "Diskusi tentang isu-isu terkini."},
        {"Time": "12:25 - 13:25", "Main Room": "Lunch", "deskripsi": "Lomba dengan hadiah menarik."},
        ]
    st.table(events_day2)
if __name__ == "__main__":
    main()
