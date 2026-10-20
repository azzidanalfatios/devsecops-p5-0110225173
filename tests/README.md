# TaskTrack — DevSecOps Project

## 1. Deskripsi Aplikasi
TaskTrack adalah aplikasi berbasis Python untuk mencatat, melihat, dan menyelesaikan daftar tugas. Data tugas disimpan dalam format JSON.

## 2. Teknologi
- Bahasa pemrograman: Python
- Unit testing: unittest
- SAST: Bandit
- CI/CD: GitHub Actions
- Runner: ubuntu-latest

## 3. Cara Menjalankan
Pastikan Python telah terpasang.

```bash
python -m unittest discover -s tests -v
python -m app.cli
```

## 4. Overview Pipeline DevSecOps
Pipeline berjalan ketika terdapat push ke branch `main` atau pull request menuju branch `main`.

Pipeline memiliki dua job:
1. **build** — memeriksa kompilasi Python dan menjalankan unit test.
2. **sast-scan** — menjalankan Bandit untuk menganalisis keamanan source code dan menerapkan Quality Gate.

Quality Gate pada proyek ini menetapkan bahwa tidak boleh ada temuan dengan tingkat severity HIGH. Jika ditemukan temuan HIGH, job SAST dinyatakan gagal.

## 5. Tujuan
Proyek ini mendemonstrasikan integrasi pengujian fungsional dan analisis keamanan statis ke dalam proses pengembangan perangkat lunak.
