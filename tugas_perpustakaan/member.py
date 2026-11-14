"""Modul anggota perpustakaan."""


class Member:
    """Anggota perpustakaan yang dapat meminjam item."""

    def __init__(self, member_id: str, nama: str):
        self.member_id = member_id
        self.nama = nama
        self.__pinjaman = []  # private: daftar item yang sedang dipinjam

    @property
    def pinjaman(self) -> list:
        """Salinan daftar item yang sedang dipinjam."""
        return list(self.__pinjaman)

    def pinjam(self, item) -> bool:
        """Meminjam item jika tersedia."""
        if item.pinjam():
            self.__pinjaman.append(item)
            return True
        return False

    def kembalikan(self, item) -> bool:
        """Mengembalikan item yang dipinjam."""
        if item in self.__pinjaman and item.kembalikan():
            self.__pinjaman.remove(item)
            return True
        return False

    def __str__(self) -> str:
        return f"Member {self.nama} ({self.member_id}) - {len(self.__pinjaman)} pinjaman"
