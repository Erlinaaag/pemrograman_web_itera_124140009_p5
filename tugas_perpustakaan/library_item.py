"""Modul item perpustakaan: abstract class LibraryItem beserta subclass Book dan Magazine."""
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Abstract base class untuk semua item perpustakaan."""

    def __init__(self, item_id: str, judul: str):
        self._item_id = item_id      # protected: id unik item
        self._judul = judul          # protected: judul item
        self.__dipinjam = False      # private: status peminjaman (name mangling)

    # --- Property (encapsulation) ---
    @property
    def item_id(self) -> str:
        """Id item (read-only)."""
        return self._item_id

    @property
    def judul(self) -> str:
        """Judul item (read-only)."""
        return self._judul

    @property
    def is_dipinjam(self) -> bool:
        """Status peminjaman item (read-only, diubah lewat pinjam/kembalikan)."""
        return self.__dipinjam

    # --- Method konkrit ---
    def pinjam(self) -> bool:
        """Meminjam item. Mengembalikan False jika sedang dipinjam."""
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self) -> bool:
        """Mengembalikan item. Mengembalikan False jika memang tidak dipinjam."""
        if not self.__dipinjam:
            return False
        self.__dipinjam = False
        return True

    def __str__(self) -> str:
        status = "Dipinjam" if self.__dipinjam else "Tersedia"
        return f"[{self._item_id}] {self.get_detail()} - {status}"

    # --- Abstract methods (wajib dioverride subclass) ---
    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda keterlambatan (rupiah)."""

    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan deskripsi singkat item."""


class Book(LibraryItem):
    """Buku: denda Rp 2.000 per hari."""
    DENDA_PER_HARI = 2000

    def __init__(self, item_id: str, judul: str, penulis: str, jumlah_halaman: int):
        super().__init__(item_id, judul)
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman

    def hitung_denda(self, hari_terlambat: int) -> float:
        return max(0, hari_terlambat) * self.DENDA_PER_HARI

    def get_detail(self) -> str:
        return f"Buku '{self._judul}' oleh {self.penulis} ({self.jumlah_halaman} hlm)"


class Magazine(LibraryItem):
    """Majalah: denda Rp 1.000 per hari."""
    DENDA_PER_HARI = 1000

    def __init__(self, item_id: str, judul: str, edisi: str, penerbit: str):
        super().__init__(item_id, judul)
        self.edisi = edisi
        self.penerbit = penerbit

    def hitung_denda(self, hari_terlambat: int) -> float:
        return max(0, hari_terlambat) * self.DENDA_PER_HARI

    def get_detail(self) -> str:
        return f"Majalah '{self._judul}' edisi {self.edisi} ({self.penerbit})"
