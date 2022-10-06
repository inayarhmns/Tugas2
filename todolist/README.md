# Tugas 4 dan 5

# Tugas 4 PBP
---

## Aplikasi Heroku /todolist : [django-app-inaya/todolist](https://django-app-inaya.herokuapp.com/todolist)
---

## Apa kegunaan {% csrf_token %} pada elemen forms? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?

{% csrf_token %} digunakan untuk melakukan generate token pada page yang dibuka oleh user. csrf_token ini diperlukan untuk membatasi request, yaitu hanya menerima dari page yang memiliki token yang sudah didaftarkan sebelumnya. csrf_token ada pada pembuatan form untuk menghindari request forgery atau request yang berasal dari form palsu yang dibuat oleh malicious user (penipu)


--- 

## Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
Bisa. Tanpa import forms kita bisa membuat form sendiri dengan tag `<form>` di HTML file, lalu diambil datanya menggunakan `request.POST.get('nama')` dimana nama tersebut adalah nama dari elemen yang ditambahkan ke `<form>` tag html. form tersebut dapat memuat label , button, dan lainnya seperti forms yang ada pada library django


--- 

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
kelas di forms.py yang merupakan child dari `ModelForm` terhubung dengan models melalui kode yang ada di dalam `class Meta:` yaitu berupa `model` dan `fields`. Setelah forms terhubung dengan model, dibuat attribute pada forms yang sesuai dengan `fields` (yang sebelumnya telah didefinisikan) dan sama dengan attribute pada models.py. Kemudian, setelah ditambahkan ke html file, form bisa mengambil masukan dari user. Masukan dari user kemudian divalidasi agar bisa disimpan tanpa error. Proses penyimpanan form menggunakan method `save()` yang menyimpan field dari form ke dalam database yaitu models yang sebelumnya sudah terhubung dengan forms.Lalu, dari database tersebutt, semua data bisa diakses dengan `Data.objects.all()` dan diiterasi di template HTML. 


---

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

1. Masuk ke direktori Tugas2Django lalu menjalankan ```python manage.py startapp todolist``` lalu akan terbentuk folder (app) baru bernama todolist.
 
2. Menambahkan path di urls.py di dalam project_django dengan include urls.py yang ada dalam mywatchlist:
```
path('todolist/', include('todolist.urls'))
```

3. Membuat class di models.py bernama `Task` yang inherit models.Model dan menambahkan:
```
user = models.ForeignKey(User, models.CASCADE)
date = models.DateField(auto_now_add=True)
title = models.CharField(max_length=255)
description = models.TextField(default = "")
```
lalu melakukan migration data.

4. Menambahkan fungsi `login_user`, `logout_user`, dan `register` di views.py dan mengimplementasikan penggunaan forms diantaranya `UserCreationForm()` untuk register, dan membuat form secara manual untuk login_user

5. Menambahkan fungsi `show_todolist`pada views.py yang mereturn response `todolist.html` yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task yang berasal dari kelas `Task` pada models.

6. Menambahkan fungsi `create_task`pada views.py dan membuat form `CreateTaskForm` sebagai child dari `ModelForm` yang menerima atribut
 ```
 title = forms.CharField(max_length=255)
 description = forms.TextInput()
 ```
lalu menghubungkan forms dengan models dan menyimpannya setiap kali user menambahkan data yang valid pada url  `/create-task` serta redirect ke `/todolist/` setelah selesai

7. Menambahkan path ke dalam `urls.py` yang ada di folder todolist dengan:
```
path('', views.show_todolist, name='show_todolist'),
path('login/', views.login_user, name = 'login'),
path('logout/', views.logout_user, name = 'logout'),
path('register/', views.register, name='register'),
path('create-task/', views.create_task, name='create_task'),

```
8. Melakukan deployment ke heroku dengan push projek ini ke github.

9. Menjalankan aplikasi heroku dan menambahkan dua akun (harrystyles dan zaynmalik) lalu menambahkan 3 Task setiap user.

--- 



# Tugas 5 PBP
---

## Aplikasi Heroku /todolist : [django-app-inaya/todolist](https://django-app-inaya.herokuapp.com/todolist)
---

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

- Inline: Memodifikai style css dari objek secara personal dengan menggunakan syntax `style=` di dalam objek yang ada di file html. 
Kekurangannya tidak efisien untuk jumlah banyak karena harus modifikasi objek satu-satu. 
Kelebihannya dapat digunakan jika ingin membuat custom style dari objek yang berbeda dengan style yang sudah ada.

- Internal: Memodifikasi style css per-class yang ada di satu file html. Dilakukan dengan membuat tag `<style>` pada file html. 
Kelebihannya dapat modifikasi objek yang berada di kelompok yang sama secara langsung, lebih cepat ketika mengoreksi style-nya, proses load website lebih cepat karena proses HTTP requestnya lebih sedikit.
Kekurangannya hanya bisa digunakan di satu file html saja, sehingga suatu file html tidak bisa menggunakan template style file html yang lain

- External: Memodifikasi style css dari file html dengan membuat file baru dengan extension `.css`. File external ini kemudian dapat digunakan oleh file html dengan cara meng-include tag `<link>` di bawah tag `<head>`
Kelebihannya dapat digunakan oleh banyak file html yang meng-include link file external tersebut, load website menjadi lebih cepat.
Kekurangannya webpage rentan menjadi berantakan jika file css external tidak berhasil dipanggil di file html saat jaringan internet yang kurang baik.

--- 

## Jelaskan tag HTML5 yang kamu ketahui.
- `<a>` : untuk menyimpan hyperlink
- `<body>` : untuk mendefinisikan body dari file html. (satu file html maksimal hanya bisa memiliki 1 body)
- `<button>` : membuat button yang bisa diklik
- `<form>` : membuat form untuk menerima informasi dari pengguna
- `<head>` : mendefinisikan bagian informasi tentang documen webpage, misalnya title
- `<link>` : membuat koneksi dengan sumber external, misalnya digunakan untuk css external file
- `<html>` : mendefinisikan root dari file html
- `<image>` : menyimpan data berupa gambar
- `<i>` : membuat text menjadi miring (italic)
- `<u>` : membuat text menjadi underlined
- `<meta>` : mendefinisikan meta data dari file html
- `<style>` : mendefinisikan style dari file html 
- `<ul>` : membuat unordered list
- `<ol>` : membuat ordered list
- `<nav>` : membuat link navigasi
- `<label>` : membuat label untuk suatu input control
- `<p>` : mendefinisikan paragraf
- `<q>` : mendefinisikan inline quote 
- `<h1> - <h6>` : mendefinisikan headings yang ada di html

--- 

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Universal selector: melakukan select untuk semua elemen. Syntax: `*`

- Type selector: melakukan select untuk tag elemen. Syntax: nama elemennya. misalnya tag `<h1>` dapat di select dengan Syntax: `h1`

- Class selector: melakukan select untuk class. Syntax: `.namaKelas`

- ID selector: melakukan select berdasarkan attribute id elemennya. Syntax: `#namaId`

- Attribute selector: melakukan select dengan attribute nya. Syntax: `[attribute]`. 
---

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

1. Membuat box untuk menu login, register, dan create-task, mengubah background color dari tiap-tiap halaman tersebut, Memodifikasi button dan font.

2. Menggunakan class `card` dari bootstrap untuk menunjukkan setiap task pada todolist dan menempatkannya di dalam tabel.

3. Menggunakan media query untuk mengubah background color menjadi putih ketika halaman windows dikecilkan

--- 
