try:
    bil1 = int(input('Masukkan bilangan bulat pertama: '))
except:
    bil1 = 1
    print("Input bukan bilangan bulat sehingga diganti menjadi nilai default 1")

try:
    bil2 = int(input('Masukkan bilangan bulat kedua: '))
    hasil = bil1 / bil2
except ZeroDivisionError as X:
    print(X)
    exit
except:
    bil2 = 1
    print("Input bukan bilangan bulat sehingga diganti menjadi nilai default 1")
    hasil = bil1 / bil2
    print("Hasil pembagian adalah", hasil)
else:
    print("Hasil pembagian adalah", hasil)
