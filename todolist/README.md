# Tugas 4 PBP
---

## Aplikasi Heroku /mywatchlist : [django-app-inaya/mywatchlist](https://django-app-inaya.herokuapp.com/todolist)
---

## Apa kegunaan {% csrf_token %} pada elemen forms? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?

{% csrf_token %} digunakan untuk melakukan generate token pada page yang dibuka oleh user. csrf_token ini diperlukan pada pembuatan form di page. Tujuan adanya token pada webpage adalah untuk menjaga keamanan agar page hanya tidak bisa diakses oleh page yang tokennya berbeda dengan token yang sudah digenerate sebelumnya

--- 

## Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
Bisa. Tanpa import forms kita bisa membuat form sendiri dengan tag `<form>` di HTML file, lalu diambil datanya menggunakan `request.POST.get('nama')` dimana nama tersebut adalah nama dari elemen yang ditambahkan ke `<form>` tag html


--- 

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

---

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

1. Masuk ke direktori projek django lalu menjalankan ```python manage.py startapp mywatchlist``` lalu akan terbentuk folder (app) baru bernama mywatchlist
 
2. Menambahkan path di urls.py di dalam project_django dengan include urls.py yang ada dalam mywatchlist:
```
path('mywatchlist/', include('mywatchlist.urls'))
```
3. Membuat class di models.py bernama `WatchlistItem` yang inherit models.Model dan memiliki 5 attribute berikut: watched sebagai objek CharField, title sebagai objek CharField, rating sebagai objek IntegerField, release_date sebagai objek DateField, dan review sebagai objek TextField. Lalu melakukan migration dan loaddata.

4. Membuat folder fixtures dan menambahkan file `initial_watchlist_data.json` di dalamnya lalu menambahkan 10 data watchlist dalam format json

5. Menambahkan fungsi `show_mywatchlist_html`, `show_watchlist_json`, dan `show_watchlist_xml` di dalam views.py yang masing-masing menerima request dan me-return httpResponse sesuai dengan requestnya

6. Membuat path di urls.py dalam folder mywatchlist sesuai dengan url yang ingin dituju (xml/, json/, dan html/) pada fungsi views.py yang dibuat pada poin ke 5

7. Menambahkan file Procfile dengan:
````
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_watchlist_data.json'
````
lalu push projek ini ke github dan melakukan deploy ke heroku



--- 

