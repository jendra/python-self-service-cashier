# Python-Self-Service-Cashier
Aplikasi sederhana untuk Proyek Akhir - Pemrograman Python

# Latar Belakang
Seorang pemilik Supermarket besar merencanakan untuk perbaikan proses bisnis dengan membuat sistem self-service di supermarket miliknya. Sehingga customer bisa langsung memasukan item yang dibeli, jumlah item yang dibeli dan harga item yang dibeli, serta harga item yang dibeli dan fitur lainnya. Pemilik tersebut membutuhkan program yang dapat memenuhi kebutuhan tersebut.

# Requirements / Objective
- Aplikasi dapat digunakan secara intuitif dan dengan mudah.
- Aplikasi memudahkan Customer memasukan nama item, jumlah item dan harga barang.
- Aplikasi memberitahu jika ada kesalahan, tetapi tidak ingin menghapus itemnya, customer bisa update item atau update jumlah item dan atau update harga item.
- Aplikasi mempermudah jika pembeli batal membeli item belanjaan, customer bisa menghapus salah satu item dari nama item atau langsung menghapus semua transaksi atau reset transaksi
- Customer bisa melakukan check order untuk memeriksa pesanan yang di masukan sudah benar atau belum, Ketika sudah selesai belanja.
- Customer dapat menghitung total belanja yang sudah dipesan, kemudian terdapat ketentuan sebagai berikut :
    - Jika total belanja di atas Rp 200.000 maka akan mendapatkan diskon 5%
    - Jika total belanja di atas Rp 300.000 maka akan mendapatkan diskon 8%
    - Jika total belanja di atas Rp 500.000 maka akan mendapatkan diskon 10%
   
# Flowcart
![Logo](https://github.com/jendra/python-self-service-cashier/main/pictures/flowchart.png)

# Function dan Atribut
- ```Self.items``` : Atribut yang berupa dictionary yang berfungsi untuk menyimpan data transaksi yang dilakukan oleh customer
- ```add_item``` : Method yang berfungsi untuk menambahkan list produk yang telah dimasukkan oleh customer yang berisi nama item, jumlah item, dan harga item
- ```update_name``` : Method yang berguna untuk mengubah nama item yang ingin diganti
- ```update_qty``` : Method yang berguna untuk mengubah jumlah item yang di-order
- ```update_price``` : Method yang berfungsi untuk mengubah harga item yang dibeli
- ```remove_item``` : Method yang digunakan untuk menghapus item tertentu
- ```reset_transaction``` : Method yang digunakan untuk menghapus seluruh data transaksi
- ```check_order``` : Method yang berfungsi untuk menampilkan seluruh data transaksi yang telah dibuat
- ```total_harga``` : Method untuk menghitung total harga/item
- ```total_price``` : Method yang digunakan untuk menampilkan total harga seluruh produk
- ```Main_menu``` : Method menampilkan menu utama aplikasi kasir. Pada menu tersebut terdapat 9 pilihan seperti tambah pesanan, periksa pesanan, update nama pesanan dan sebagainya. Saat user memasukkan pilihannya, program akan mengeksekusi perintah sesuai dengan pilihan yang dipilih. 

# Test Case
* Test 1:

Customer ingin menambahkan item baru menggunakan method ```add_item()``` dan memeriksa item yang ditambahkan menggunakan method ```check_order()```,  dengan sebagai berikut:

    - Nama item Ayam Goreng, Qty: 2, Harga: 20000
    - Nama item Pasta Gigi. Qty: 3, Harga:15000

![Link](https://github.com/jendra/python-self-service-cashier/main/pictures/add-item.jpg)

- Test 2:

Ternyata customer salah membeli salah satu item dari belanjaannya, maka customer menggunakan method ```remove_item()```. Item yang ingin dihapus adalah Pasta Gigi.

![Link](https://github.com/jendra/python-self-service-cashier/main/pictures/remove-item.jpg)

- Test 3:

Setelah dipikir kembali customer salah memasukan semua item yang dibelanjakannya. Daripada menghapus satu-satu, maka customer cukup menggunakan method ```reset_transction()```.

![Link](https://github.com/jendra/python-self-service-cashier/main/pictures/reset-transaction.jpg)

- Test 4:

Setelah customer selesai belanja, maka akan menghitung total belanja yang harus dibayar menggunakan method ```total_price()```. Sebelum mengeluarkan total belanja yang dibayar, akan menampilkan semua item yang dibeli. 

![Link](https://github.com/jendra/python-self-service-cashier/main/pictures/total-price.jpg)

# Saran Perbaikan
Kita harus melakukan uji coba kepada customer sebagai user pertama yang memakai aplikasi cashier self-service ini. Kemudian membuat kuisoner untuk kritik dan saran untuk membuat cashier aplikasi ini menjadi lebih baik. Lalu diimplemntasi sehingga lebih memudahkan customer dalam bertransaksi.
