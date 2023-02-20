# -*- coding: utf-8 -*-

from tabulate import tabulate
import pandas as pd

class Transaction:
    def __init__ (self):
        """
        Inisialisasi dictionary
        """ 
        self.data_transc = dict()
     
    
    def add_item (self, item_name, total_item, price_per_item):
        """
        Fungsi untuk menambah item baru yang mengambil input dari customer seperti 
        item_name(str), jumlah (int), dan harga (int).
    
        Hasil return Tabel list item yang ingin dibeli
        """
        # Menambah data ke dalam atribut dictrionary
        self.data_transc.update({item_name : [total_item, price_per_item, (total_item * price_per_item)]})

        # Menampilkan list item
        return self.check_order()
     
        
    def update_item_name (self, item_name, update_item_name):
        """
        Fungsi untuk update nama item yang sudah ada di dalam transaksi yang mengambil input dari
        customer sebagai nama item yang ingin diupdate dan nama baru yang ingin digunakan.
        Jika nama item ditemukan, maka nama item tersebut akan diupdate.
        Menggunakan parameter: item_name (str)
        
        Hasil return berupa Tabel list item yang telah di-update.
        """
        try: 
            # Update nama item
            self.data_transc[update_item_name] = self.data_transc.pop(item_name)

            # Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    
    def update_item_qty (self, item_name, update_total_item):
        """
        Fungsi untuk update jumlah item yang sudah ada di dalam transaksi yang mengambil input dari
        customer sebagai nama item yang ingin diupdate dan jumlah terbaru yang ingin digunakan.
        Menggunakan parameter item_name (str), update_total_item (int).
        
        Hasil return berupa Tabel list item yang telah di-update.
        """
        try: 
            # Update jumlah item
            self.data_transc[item_name][0] = update_total_item 
            
            # Update data total harga 
            self.data_transc[item_name][2] = update_total_item * self.data_transc[item_name][1]

            #Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
      
    
    def update_item_price (self, item_name, update_price_item):
        """
        Fungsi update harga item yang sudah ada di dalam transaksi yang mengambil input dari
        customer sebagai nama item yang ingin diupdate dan harga baru yang ingin digunakan.
        Jika nama item ditemukan, maka harga item tersebut akan diupdate.
        Menggunakan parameters item_name (str), update_price_item (int)
        
        Hasil return Tabel list item yang telah di-update.
        """
        try:
            # Update harga item
            self.data_transc[item_name][1] = update_price_item
            # Update data total harga
            self.data_transc[item_name][2] = update_price_item * self.data_transc[item_name][0]

            #Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    
    def remove_item (self, item_name):
        """
        Fungsi menghapus item dari transaksi yang mengambil dari input customer sebagai nama item yang ingin dihapus.
        Menggunakan parameters item_name (str).
        
        Hasil return berupa Tabel list item terbaru
        """
        try:
            # Delete item tertentu
            self.data_transc.pop(item_name)
            
            # Menampilkan list item terbaru
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    
    def reset_transaction (self):
        """
        Fungsi untuk menghapus semua data transaksi menjadi kosong kembali.
        
        Hasil return berupa pesan : "Semua item berhasil di-delete!"
        """
        # Delete semua data transaksi
        self.data_transc.clear()
        
        return print("Semua item berhasil di-delete!")
    
    
    def check_order(self):
        """
        fungsi untuk menampilkan semua data transaksi yang sudah dibuat
        """
        try: 
            table = []
            
            # Add data dictionary transaksi ke dalam nested list table
            for key, val in self.data_transc.items():
                tmp = []
                tmp.append(key)

                for i in val:
                    tmp.append(i)

                table.append(tmp) 

            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
            print("Transaksi Anda")
            print("")
            print(tabulate(table, headers, tablefmt='psql')) 
            
        except:
            raise exception("Terjadi kesalahan input! data nama item, jumlah item, dan harga per item tidak boleh kosong! Silahkan input ulang!")
     
    
    def total_price (self):
        """
        fungsi untuk menampilkan total harga transaksi dan memberikan diskon apabila memenuhi syarat
        """
        # Menampilkan list item
        self.check_order()
        print("")
        
        # Menjumlahkan total harga
        total = 0
        for key, val in self.data_transc.items():
            total += self.data_transc[key][2]
            
        # pengecekan diskon
        if total > 500_000:
            new_total = total * 0.90
            print(f'Total belanja Anda setelah diskon 10% adalah {new_total}')
        elif total > 300_000:
            new_total = total * 0.92
            print(f'Total belanja Anda setelah diskon 8% adalah {new_total}')
        elif total > 200_000:
            new_total = total * 0.95
            print(f'Total belanja Anda setelah diskon 5% adalah {new_total}')
        else:
            print(f'Total belanja Anda adalah Rp {total}')


def menu(obj):
    """Fungsi untuk menampilkan daftar menu.
    
    parameter
    obj : object hasil instance class
    """
    print("-"*60)
    print("SELAMAT DATANG DI SUPERMARKET SELF-SERVICE")
    print("-"*60)
    print("1. Menambahkan item baru")
    print("2. Mengubah nama item")
    print("3. Mengubah jumlah item")
    print("4. Mengubah harga item")
    print("5. Menghapus item")
    print("6. Reset transaksi")
    print("7. Check order")
    print("8. Lihat total harga")
    print("9. Exit\n")
    
    # Input opsi menu
    choice = int(input('Masukan pilihan Anda : '))
    
    try:
        if choice == 1:
            # Input nama item
            item_name = input('Masukan nama item : ')
            
            # Looping sampai masukkan berupa angka
            while True:
                try:
                    # Input jumlah item
                    total_item = int(input('Masukan jumlah item : '))
                except ValueError:
                    print ("Masukan harus angka!")
                else:
                    break
            
            # Looping sampai masukkan berupa angka
            while True:
                try:
                    # Input harga item
                    harga_item = int(input('Masukan harga item : '))
                except ValueError:
                    print ("Masukan harus angka!")
                else:
                    break           
            
            # memanggil method yang ada di class Transaction
            obj.add_item(item_name, total_item, harga_item)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 2:
            
            # Input nama item
            item_name = input('Masukan nama item : ')
            
            # Input harga item yang baru
            item_name_baru =input('Masukan nama item yang baru : ') 
            
            # memanggil method yang ada di class Transaction
            obj.update_item_name(item_name, item_name_baru)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 3:
            # Input nama item
            item_name = input('Masukan nama item : ')
            
            # Looping sampai masukkan berupa angka
            while True:
                try:
                    # Input jumlah item yang baru
                    total_item_baru = int(input('Masukan jumlah item : '))
                except ValueError:
                    print ("Masukan harus angka!")
                else:
                    break
            
            # memanggil method yang ada di class Transaction
            obj.update_item_qty(item_name, total_item_baru)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 4:
            # Input nama item
            item_name = input('Masukan nama item : ')
            
            # Looping sampai masukkan berupa angka
            while True:
                try:
                    # Input harga item yang baru
                    harga_item_baru = int(input('Masukan harga item : '))
                except ValueError:
                    print ("Masukan harus angka!")
                else:
                    break 
            
            # memanggil method yang ada di class Transaction
            obj.update_item_price(item_name, harga_item_baru)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 5:
            # Input nama item
            item_name = input('Masukan nama item : ')
            
            # memanggil method yang ada di class Transaction
            obj.remove_item(item_name)
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 6:
            
            # memanggil method yang ada di class Transaction
            obj.reset_transaction()
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 7:
            # memanggil method yang ada di class Transaction
            obj.check_order()
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 8:
            # memanggil method yang ada di class Transaction
            obj.total_price()
            
            # kembali ke menu
            menu(obj)
            
        elif choice == 9:
            print("-"*60)
            print("Terima kasih telah mengunjungi Supermarket Self-Service.")
            print("-"*60)
            pass
        
        else:
            print("Anda salah input.\n")
            # kembali ke menu
            menu(obj)
            
    except:
        print("Input Anda salah.\n")
        # kembali ke menu
        menu(obj)

# Instance class Transaction    
trnsct_123 = Transaction()

# Memanggil function menu
menu(trnsct_123)