# Pertemuan 5 - OOP Python

## Identitas Mahasiswa
- **Nama Lengkap**: Erlin Agesti Risadi
- **NIM**: 124140009
- **Kelas Praktikum**: (isi: RA / RB)

## Deskripsi Program
Sistem manajemen perpustakaan sederhana. `main.py` menambahkan buku dan majalah ke `Library`, menampilkan katalog, mencari item berdasarkan id/judul, lalu mendemonstrasikan peminjaman, status ketersediaan, dan denda.

Penerapan pilar OOP:
- **Class**: `LibraryItem`, `Book`, `Magazine`, `Member`, `Library`.
- **Inheritance**: `Book` dan `Magazine` mewarisi abstract class `LibraryItem`.
- **Encapsulation**: atribut protected (`_item_id`, `_judul`), private (`__dipinjam`, `__koleksi`, `__pinjaman`), dan `@property` (`item_id`, `judul`, `is_dipinjam`).
- **Polymorphism**: `get_detail()` dan `hitung_denda()` diimplementasikan berbeda di tiap subclass, dipanggil seragam lewat `LibraryItem`.
- **Abstraction**: `LibraryItem(ABC)` dengan `@abstractmethod`.

## Cara Menjalankan
```bash
cd tugas_perpustakaan
python main.py
```

## Screenshot Output

![Hasil](Praktikum-paw5/assets/Gambar.png)
