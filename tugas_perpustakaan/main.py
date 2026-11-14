"""Skrip uji sistem perpustakaan sederhana."""
from library_item import Book, Magazine
from library import Library
from member import Member


def main():
    lib = Library("Perpustakaan ITERA")

    print("--- Menambahkan item ---")
    lib.tambah_item(Book("B001", "Pemrograman Python", "Andi Wijaya", 320))
    lib.tambah_item(Book("B002", "Basis Data Dasar", "Siti Aminah", 250))
    lib.tambah_item(Magazine("M001", "Teknologi Masa Kini", "Nov 2026", "Media Tek"))
    lib.tambah_item(Magazine("M002", "Sains Populer", "Okt 2026", "Sains Press"))
    lib.tambah_item(Book("B001", "Duplikat", "-", 1))  # id duplikat

    lib.tampilkan_tersedia()

    print("\n--- Pencarian ---")
    print("Cari id 'M001':", lib.cari_id("M001"))
    print("Cari judul 'python':")
    for i in lib.cari_judul("python"):
        print(" ", i)
    print("Cari id 'X999':", lib.cari_id("X999"))

    print("\n--- Peminjaman & status ketersediaan ---")
    erlin = Member("124140009", "Erlin Agesti Risadi")
    print("Pinjam B001:", erlin.pinjam(lib.cari_id("B001")))
    print("Pinjam B001 lagi:", erlin.pinjam(lib.cari_id("B001")))
    print("Status B001 dipinjam?", lib.cari_id("B001").is_dipinjam)
    lib.tampilkan_tersedia()

    print("\n--- Denda keterlambatan 5 hari (polimorfisme) ---")
    for item in (lib.cari_id("B002"), lib.cari_id("M001")):
        print(f"{item.judul}: Rp {item.hitung_denda(5):,.0f}")

    print("\n--- Pengembalian ---")
    print("Kembalikan B001:", erlin.kembalikan(lib.cari_id("B001")))
    print(erlin)
    lib.tampilkan_semua()


if __name__ == "__main__":
    main()
