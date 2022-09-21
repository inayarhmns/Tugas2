# Tugas 2 PBP
---

## Aplikasi Heroku /mywatchlist : [django-app-inaya/mywatchlist](https://django-app-inaya.herokuapp.com/mywatchlist)
## Aplikasi Heroku /mywatchlist/html : [django-app-inaya/mywatchlist/html ](https://django-app-inaya.herokuapp.com/mywatchlist/html)
## Aplikasi Heroku /mywatchlist/json : [django-app-inaya/mywatchlist/json](https://django-app-inaya.herokuapp.com/mywatchlist/json)
## Aplikasi Heroku /mywatchlist/xml : [django-app-inaya/mywatchlist/xml ](https://django-app-inaya.herokuapp.com/mywatchlist/xml)
---

## Perbedaan antara JSON, XML, dan HTML
XML adalah markup language yang berfungsi dalam pertukaran dan penyimpanan data, dapat melakukan display data karena dapat memuat banyak data type (image, graph, dll), harus menggunakan closing tag, dapat memuat comment, tag nya bersifat case sensitive.
HTML adalah markup language yang berfungsi untuk memformat data untuk ditunjukkan, tidak harus mengggunakan closing tag, dapat memuat comment, tagnya bersifat case insensitive.
JSON adalah sebuah data format untuk bertukar informasi dalam bentuk key-value yang dipisah dengan koma, tidak dibuat memiliki kemampuan untuk men-display data karena hanya support data type text dan angka saja, tidak menggunakan closing tag, tidak memuat comment, case sensitive.

--- 

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery digunakan untuk berinteraksi dan bertukar informasi antara client dengan server pada platform. Platform menerima data melalui request. Data tersebut diproses dan dikembalikan dalam bentuk response sesuai dengan request yang diminta. Misalnya request berupa halaman html akan mengembalikan file html yang ditampilkan ke client (browser) atau request dalam bentuk data akan dikeluarkan dalam bentuk data json atau xml.
  

--- 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

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
## Screenshot Postman 
### HTML App
![alt text](https://github.com/inayarhmns/Tugas2Django/blob/main/mywatchlist/Screenshot-mywatchlist-html.png "mywatchlist/html")
### JSON App
![alt text](https://github.com/inayarhmns/Tugas2Django/blob/main/mywatchlist/Screenshot-mywatchlist-json.png "mywatchlist/json")
### XML App
![alt text](https://github.com/inayarhmns/Tugas2Django/blob/main/mywatchlist/Screenshot-mywatchlist-xml.png "mywatchlist/xml")


