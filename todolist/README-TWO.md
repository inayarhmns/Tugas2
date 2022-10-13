# TUGAS 6 

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronus programming berjalan secara serial dan single-thread, kode dijalankan satu persatu sehingga untuk melihat hasil modifikasi kode harus menunggu semua proses selesai. Sedangkan asynchronus programming berjalan secara paralel atau multi threaded yang berarti kodenya dapat dijalankan tanpa harus menunggu proses lain selesai. Asynchronus bekerja dengan mengirimkan banyak request ke server sekaligus, sedangkan synchronus hanya satu. 


--- 
## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven programming adalah paradigma programming dimana jalannya program dipengaruhi oleh sebuah event, misalnya action user atau message dari function lain. Salah satu contoh penerapannya dalam tugas ini adalah event yang terjadi ketika diklik button `Save` saat setelah menambahkan form dari modal bootstrap. Event tersebut akan memanggil fungsi ajax dan memanggil url `add_todolist` untuk kemudian isi form yang sudah diisi disimpan dan diupdate ke dalam tabel.

## Jelaskan penerapan asynchronous programming pada AJAX.

Asynchronous programming pada AJAX dengan jQuery dilakukan dengan memanggil fungsi `ajax()` atau `async function` untuk memanggil HTTP Requests. HTTP Request tersebut berisi data backend yang dapat diambil secara langsung tanpa memerlukan loading page setelah mengirim data. 

--- 
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Menambahkan script ajax jquery
- Menghapus context `todolist` pada show_todolist
1. AJAX GET
    - Menambahkan view `show_json` yang mengembalikan response dalam json
    - Menambahkan path `/todolist/json/` di todolist.py yang memanggil fungsi `show_json`
    - Menambahkan script ajax `get('/todolist/json/'` untuk memanggil `show_json` pada todolist.html lalu di map dalam bentuk table card. Dilakukan untuk mendapatkan data todolist dengan menggunakan json.

2. AJAX POST
    - Membuat tombol `Add Task` dan menghubungkannya dengan modal dari bootstrap, lalu mengisi modal tersebut dengan form title dan description todolist
    - Membuat view `add_todolist`
    - Membuat path `/todolist/add` yang memanggil `add_todolist`
    - Menambahkan function di todolist.html yang dijalankan setiap button `Save` di modal diklik, lalu memanggil fungsi `ajax()` untuk melakukan `post` ke `add_todolist`. Setelah dipost, akan di ambil `response` berdasarkan key nya lalu di update ke dalam tabel yang ada di `todolist.html`
    - Menutup modal setelah diklik tombol `Save` dengan syntax `$("#myModal").modal('hide');`
    
