# 🌱 Akıllı Sulama Sistemi (Bulanık Mantık Tabanlı)

Bu proje, **toprak nemi**, **hava sıcaklığı**, **rüzgar hızı**, **yağmur olasılığı** ve **bitki türüne** göre **sulama süresi** ve **sıklığını** bulanık mantık ile hesaplayan, kullanıcı dostu grafik arayüzüne (GUI) sahip bir **akıllı sulama sistemidir**.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![Fuzzy](https://img.shields.io/badge/FuzzyLogic-skfuzzy-purple.svg)

---
```bash
python sulama_sistemi.py
```

## 📌 Proje Özellikleri

- ✅ **Bulanık Mantık Modeli** ile sulama süresi ve sıklığı tahmini  
- ✅ Kullanıcıdan alınan verilerle **anında hesaplama**  
- ✅ **Matplotlib** ile girdi ve çıktı **üyelik fonksiyonu grafikleri**  
- ✅ **Tkinter tabanlı sekmeli GUI**:
---
  ### 📥 Giriş Sekmesi
  - ![  - 📥 Giriş Sekmesi ](https://github.com/nnisabie/hanifebiber/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-05-25%20231719.png?raw=true)

  ### 📊 Girdi Grafikler Sekmesi
  - ![📊 Girdi Grafikler Sekmesi ](https://github.com/nnisabie/hanifebiber/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-05-25%20231821.png?raw=true)

  ### 📈 Çıktı Grafikler Sekmesi
  - ![📈 Çıktı Grafikler Sekmesi](https://github.com/nnisabie/hanifebiber/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-05-25%20231844.png?raw=true)







---

## 🧠 Kullanılan Değişkenler

### 🔹 Girdi Değişkenleri

| Değişken           | Açıklama                  |
|--------------------|---------------------------|
| Toprak Nemi (%)    | 0 – 100 arası              |
| Hava Sıcaklığı (°C)| 0 – 50 arası               |
| Rüzgar Hızı (km/h) | 0 – 30 arası               |
| Yağmur Olasılığı (%) | 0 – 100 arası            |
| Bitki Türü         | Sebze, Meyve, Tahıl       |

### 🔸 Çıktı Değişkenleri

| Değişken            | Değer Aralığı  | Etiketler          |
|---------------------|----------------|---------------------|
| Sulama Süresi (dk)  | 0 – 60         | Kısa, Orta, Uzun    |
| Sulama Sıklığı (kez/gün)| 1 – 3     | Az, Orta, Sık       |

---

## 🧾 Kural Sistemi

Toplamda **5 adet bulanık kural** ile sistem davranışı belirlenmiştir.

### Örnek Kural:

> 🔸 **Eğer** toprak nemi düşük, hava sıcaklığı sıcak ve yağmur olasılığı düşükse  
> 🔸 **O zaman** sulama süresi uzun, sulama sıklığı sık olur.

---


---

## 🔧 Gereksinimler

```bash
pip install numpy matplotlib scikit-fuzzy
