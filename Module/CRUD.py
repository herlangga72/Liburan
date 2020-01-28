import mysql.connector as sql
class sql():
    def connect(self,users,hosts,databases):
        global koneksi,perintah
        try :
            for i in range(3):
                koneksi 	= sql.connect(user=users,host=hosts,database=databases)
                perintah 	= koneksi.cursor()
                if i==4:
                    break
        except :
            print("Server Connection Time Out")
            raise SystemExit

    def Tampilkan_data(self):
        global koneksi,perintah
        Line="SELECT * FROM `spesifikasi`"
        perintah.execute(Line)
        for n in perintah:
            print (n)

    def create(self,Nama,NIM,Judul,Pembimbing,Program):
        global koneksi,perintah
        Line        = ("INSERT INTO `spesifikasi` (`NM_Mahasiswa`, `NIM_MHS`, `Judul_TA`, `PEMBIMBING`, `NM_PROG`) VALUES ('{a}', {e}, '{b}', '{c}', '{d}');").format(a=Nama,b=Judul,c=Pembimbing,d=Program,e=NIM)
        perintah.execute(Line)
        koneksi.commit()

    def Delete_data(self,Kolom,WildCard):
        global koneksi,perintah,Script
        Line        ="DELETE FROM `spesifikasi` WHERE 'spesifikasi'.'{a}' LIKE '{b}+';".format(a=Kolom,b=WildCard)
        
        perintah.execute(Line)
        koneksi.commit()

    def Update_data(self,Nama,NIM,Judul,Pembimbing,Program):
        global koneksi,perintah,Script
        Line        =("""UPDATE `spesifikasi` SET `NM_Mahasiswa`="{a}",`Judul_TA`="{b}",`PEMBIMBING`="{c}",`NM_PROG`="{d}" WHERE `NIM_MHS`={e}""").format(a=Nama,b=Judul,c=Pembimbing,d=Program,e=NIM)
        perintah.execute(Line)
        koneksi.commit()
