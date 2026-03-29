# 🔍 NmapScanner

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-0E83CD?style=for-the-badge&logoColor=white)
![Kali](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-a78bfa?style=for-the-badge)

*Nmap'i terminal menüsüyle kolayca kullanan Python pentest aracı.*

</div>

---

## Nedir?

NmapScanner, nmap komutlarını ezberlemek zorunda kalmadan hızlıca tarama yapmanı sağlayan bir Python wrapper'ıdır. Hedefi gir, tarama türünü seç — gerisini halleder.

## Özellikler

```
[*] 6 farklı tarama modu
[*] Renkli terminal çıktısı
[*] IP veya domain desteği
[*] Hızlı / Agresif / UDP / OS Detection modları
```

## Kurulum

```bash
git clone https://github.com/HargosAktif/nmap-scanner
cd nmap-scanner
pip install -r requirements.txt
sudo apt install nmap   # eğer yoksa
```

## Kullanım

```bash
python3 nmap_scanner.py <hedef>

# Örnek
python3 nmap_scanner.py 192.168.1.1
python3 nmap_scanner.py scanme.nmap.org
```

```
[?] Tarama türü seçin:
  [1] Hızlı Tarama
  [2] Servis & Versiyon
  [3] OS Tespiti
  [4] Tam Port Tarama
  [5] Agresif Tarama
  [6] UDP Tarama
```

## ⚠️ Yasal Uyarı

Bu araç yalnızca **izinli sistemlerde** ve **eğitim amaçlı** kullanım içindir. İzinsiz sistemlerde kullanmak yasa dışıdır.

---

<div align="center">

*by [LatenT](https://github.com/HargosAktif)*

</div>
