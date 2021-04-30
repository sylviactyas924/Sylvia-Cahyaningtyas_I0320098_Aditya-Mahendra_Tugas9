# mendefinisikan array dengan nilai awal
import array
A = array.array('i', [100, 200, 300, 400, 500])
print("Nilai awal sebelum diubah:", A)

#mengubah nilai dari elemen tertentu
A[1] = -700 #mengubah elemen kedua
A[4] = 800 #mengubah elemen kelima
print("Nilai akhir setelah diubah:", A)

# exercise 9.10
# nilai awal (sebelum dibalik)
print("Nilai awal sebelum dibalik:", A)

#membalik urutan elemen array
print("Nilai akhir setelah dibalik", A.reverse())