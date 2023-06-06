# fungsi
def baca_file(nama_file):
    handle=open(nama_file)
    artikel=handle.read()
    handle.close
    return artikel
#  input nama file
nama_file=input("masukan nama file:")

# baca berita dari file
artikel=baca_file(nama_file)
# print(artikel)
# lakukan oprqasi regex
import re
# 1. cari semua kata yang diawali huruf besar
pattern=r"[A-Z]\w+"
hasil=re.findall(pattern,artikel)
print(hasil)
# 2. tampilkan tanggal
# pola2=r"\d( \w* \d+)"
pola_tgl2=r"\d/\d/\d+"
#  or \d\d?/\d\d?\d\d\d\d
hasil2=re.findall(pola_tgl2,artikel)
print(f"jumlah tanggal:{len(hasil2)}")
print(hasil2)
# 3. tampilkan semua kata yang panjangnya 7
pola3=r"\b\w{7}\b"
# r"\s\w{7}\s"
hasil3=re.findall(pola3,artikel)
print(hasil3)
# cari uang
# polarp=r"Rp.+{3,5} ribu|Rp .{3,5} juta"
# hasilrp=re.findall(polarp,artikel)
# print(hasilrp)
# ganti kata
kata_lama=input("masukan kata yang diganti:")
kata_baru=input("masukan kata prngganti:")

hasil=re.sub(kata_lama,kata_baru,artikel)
# simpan dalam file
handle=open(nama_file,"w")
handle.write(hasil)
handle.close()