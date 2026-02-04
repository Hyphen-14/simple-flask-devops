---
title: Cyber Code Breaker
emoji: 🔓
colorFrom: green
colorTo: indigo
sdk: docker
pinned: false
---

# Cyber Code Breaker 🔓

Aplikasi Sederhana berbasis Flask menggunakan Docker.
Project ini dibuat sebagai bagian dari tugas assignment untuk mendemonstrasikan kemampuan deployment aplikasi ke lingkungan Container.

## Fitur
- **Dockerized:** Aplikasi berjalan di dalam container yang terisolasi.
- **Flask Framework:** Menggunakan Python Flask yang ringan.
- **Interactive UI:** Mini game tebak kode dengan style terminal hacker.

## Cara Menjalankan (Lokal)
1. Build image: `docker build -t cyber-breaker .`
2. Run container: `docker run -p 7860:7860 cyber-breaker`