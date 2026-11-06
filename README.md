# kalfinsetiawan.com

Portofolio Kalfin Agus Setiawan (Jurkon Studio). Situs statis dua bahasa untuk GitHub Pages.

| Bahasa | Beranda | Studi kasus |
|---|---|---|
| Indonesia | `/` | `/jurkon/`, `/boombastis/`, `/game/`, `/berita/`, `/landing/` |
| English | `/en/` | `/en/jurkon/`, `/en/boombastis/`, `/en/game/`, `/en/news/`, `/en/landing/` |

Semua halaman dibuat oleh `build.py` (konten dua bahasa ada di dalamnya).
Ubah teks di `build.py`, lalu jalankan `python3 build.py` untuk membuat ulang HTML dan `sitemap.xml`.

- `assets/`: CSS, JS, gambar pratinjau, logo
- `CNAME`: kalfinsetiawan.com

© 2026 Kalfin Agus Setiawan. Logo, wordmark, dan ikon adalah karya orisinal.

## Logo & ikon
Logo adalah kepala **Titik**, maskot Jurkon Studio (badan gradien indigo → pink, visor gelap, antena berujung titik kuning).
Titik kuning di antena juga menjadi titik pada wordmark “kalfinsetiawan.”.
Semua aset dibuat ulang dengan `python3 make_assets.py`; sumber bentuknya ada di `icons.py`.
