"""Modul Library: pengelola koleksi item perpustakaan."""
from library_item import LibraryItem


class Library:
    """Menyimpan dan mengelola koleksi LibraryItem."""

    def __init__(self, nama: str):
        self.nama = nama
        self.__koleksi = []  # private: daftar seluruh item

    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambah item; menolak id duplikat."""
        if self.cari_id(item.item_id) is not None:
            print(f"Gagal: id {item.item_id} sudah terdaftar.")
            return False
        self.__koleksi.append(item)
        print(f"Berhasil menambahkan: {item.get_detail()}")
        return True

    def tampilkan_tersedia(self):
        """Menampilkan item yang belum dipinjam."""
        print(f"\n=== Katalog Tersedia - {self.nama} ===")
        tersedia = [i for i in self.__koleksi if not i.is_dipinjam]
        if not tersedia:
            print("(tidak ada item tersedia)")
        for item in tersedia:
            print(item)  # polimorfik: get_detail() berbeda tiap subclass

    def tampilkan_semua(self):
        """Menampilkan seluruh item beserta statusnya."""
        print(f"\n=== Semua Koleksi - {self.nama} ===")
        for item in self.__koleksi:
            print(item)

    def cari_id(self, item_id: str):
        """Mencari item berdasarkan id; None jika tidak ada."""
        for item in self.__koleksi:
            if item.item_id == item_id:
                return item
        return None

    def cari_judul(self, kata_kunci: str) -> list:
        """Mencari item yang judulnya mengandung kata kunci (tidak case-sensitive)."""
        k = kata_kunci.lower()
        return [i for i in self.__koleksi if k in i.judul.lower()]
