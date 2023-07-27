import streamlit as st

def main():
    st.title("Rundown Acara")
    st.write("Berikut adalah daftar acara yang akan diselenggarakan:")
    st.header("Day 1: Wednesday, 9 August 2023")

    events_day1 = [
        {"Time": "08:30 - 08:40", "Main Room": "Opening Day 1: traditional dance by UKM Sunda", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "08:40 - 08:50", "Main Room": "Speech by General Chair Representation", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "08:50 - 09:00", "Main Room": "Speech by IEEE IS Representative: Prof. Ir. Gamantyo Hendrantoro", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "09:00 - 09:10", "Main Room": "Opening Speech by Rector of Telkom University: Prof. Dr. Adiwijaya", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "09:10 - 09:20", "Main Room": "Photo Session", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "09:20 - 10:20", "Main Room": "Keynote Speech 1: Dr. Syed Zainudeen Mohd Shaid Dell, MY Topic: TBA Moderator: UTM - Dr. Hajar", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "10:20 - 10:30", "Main Room": "Coffee Break", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "10:30 - 12:00", "Main Room": "Workshop Session #1", "Room A (onsite)": "Parallel Sesion 1A Moderator: TBA", "Room B (onsite/online)": "Parallel Sesion 1B Moderator: TBA","Room C (online)": "Parallel Sesion 1C Moderator: TBA"},
        {"Time": "12:00 - 13:00", "Main Room": "Lunch Break", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "13:00 - 14:30", "Main Room": "Keynote Speech 2: Prof. Kamal Bechkoum Head of the School of Computing and Engineering, University of Gloucestershire, UK (60')Topic: TBA Moderator: Pak Rio Guntur", "Room A (onsite)": "Parallel Sesion 2A Moderator: TBA", "Room B (onsite/online)": "Parallel Sesion 2B Moderator: TBA","Room C (online)": "Parallel Sesion 2C Moderator: TBA"},
        {"Time": "14:30 - 14:40", "Main Room": "Coffee Break", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "14:40 - 16:10", "Main Room": "Keynote Speech #3: Dr. Owen Johnson Senior Fellow, University of Leeds, UK (60') Topic: TBA Moderator: Bu Ima","Room A (onsite)": "Parallel Sesion 3A Moderator: TBA", "Room B (onsite/online)": "Parallel Sesion 3B Moderator: TBA","Room C (online)": "Parallel Sesion 3C Moderator: TBA"},
        {"Time": "16:10 - 16:15", "Main Room": "Closing Day 1", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
    ]

    # Tampilkan daftar acara dalam bentuk tabel
    st.table(events_day1)

    st.header("Day 2: Thursday, 10 August 2023")
    events_day2 = [
        {"Time": "08:30 - 08:45", "Main Room": "Opening Day 2", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "08:45 - 10:15", "Main Room": "Keynote Speech 4: Prof. Ts. Dr. Rabiah Ahmad Professor of Computer Science, Universiti Tun Hussien Onn Malaysia, MY (60') Topic: TBA Moderator: UTM", "Room A (onsite)": "Parallel Sesion 4A Moderator: TBA", "Room B (onsite/online)": "Parallel Sesion 4B Moderator: TBA","Room C (online)": "Parallel Sesion 4C Moderator: TBA"},
        {"Time": "10:15 - 10:25", "Main Room": "Coffee Break", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "10:25 - 11:55", "Main Room": "Workshop Session #2 - Pak Putu", "Room A (onsite)": "Parallel Sesion 5A Moderator: TBA", "Room B (onsite/online)": "Parallel Sesion 5B Moderator: TBA","Room C (online)": "Parallel Sesion 5C Moderator: TBA"},
        {"Time": "11:55 - 12:05", "Main Room": "Closing Speech by Vice-Chancellor of UTM: Prof. Datuk Ir. Ts. Dr. Ahmad Fauzi bin Ismail", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "12:05 - 12:20", "Main Room": "Awards Ceremony and Closing", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        {"Time": "12:25 - 13:25", "Main Room": "Lunch", "Room A (onsite)": "","Room B (onsite/online)": "","Room C (online)": ""},
        ]
    st.table(events_day2)
if __name__ == "__main__":
    main()
