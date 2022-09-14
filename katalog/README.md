# Tugas 2 PBP
---

## Aplikasi Heroku : [django-app-inaya](https://django-app-inaya.herokuapp.com/)
---


## Bagan Django 
![alt text](https://github.com/inayarhmns/Tugas2Django/blob/main/katalog/bagan_django.png "Bagan Django")

Django menerima request dari user dan menjalankan manage.py. Pada manage.py, dipanggil settings.py dari folder project_django. File settings.py ini berupa informasi mengenai aplikasi yang dijalankan di keseluruhan projek, di dalamnya terdapat root config url yaitu project_django/urls.py untuk melakukan routing. Routing yang ada di urls.py ini akan menuju ke file views.py dari setiap folder aplikasi yang ingin dijalankan. Setiap views.py dari folder aplikasi ini memiliki fungsi yang meminta request dan mengembalikan return. Isinya berupa data dari models.py yang akan ditunjukkan serta me-return objek httpResponse dari templates (file-file html). 

--- 

## Mengapa menggunakan virtual environment?

Virtual environment digunakan untuk membuat environment yang terisolasi dari folder/projek lain agar dapat menggunakan package python secara individu. Virtual environment ini memperbolehkan kita untuk menggunakan package yang berbeda untuk setiap projek yang ada di komputer sehingga tidak perlu menginstall ulang package setiap kali menjalankan suatu projek. Tidak hanya berbeda dalam packagenya, versi package dari setiap projek juga dapat dibuat berbeda-beda sesuai dengan kebutuhan projeknya.

Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita tetap dapat membuat projek django tanpa menggunakan virtual environment mengingat virtual environment hanya berfungsi sebagai pemisah environment dan penggunaan package dari projek lain. Namun, praktiknya akan lebih baik jika menggunakan virtual environment, terlebih lagi ketika membuat projek lebih dari satu dan dengan package requirements yang berbeda-beda.  

---
## Implementasi poin 1-4 pada Deskripsi Tugas

1. Mengimplementasikan views.py dengan mengambil data dari CatalogItem dari katalog.models yang dimasukkan ke dalam data_katalog
2. Routing di katalog.urls dengan memanggil show_katalog yang ada pada katalog.views, lalu routing pada project_django.urls yang menyambungkan ke katalog.urls untuk halaman katalog/
3. Mengubah isi dari katalog.html berdasarkan list_katalog yang berisi data_katalog 
4. Melakukan deploy ke heroku dengan sebelumnya menambahkan konfigurasi di project_django/settings, menambahkan heroku api di github secret, dan push projek ke github