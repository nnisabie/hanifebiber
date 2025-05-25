
#🌱 Akıllı Sulama Sistemi (Bulanık Mantık Tabanlı)
Bu proje, toprak nemi, hava sıcaklığı, rüzgar hızı, yağmur olasılığı ve bitki türüne göre sulama süresi ve sıklığını bulanık mantık ile hesaplayan, kullanıcı arayüzü (GUI) olan bir akıllı sulama sistemidir.

#📌 Proje Özellikleri
Bulanık Mantık Modeli kullanılarak sulama süresi ve sıklığı hesaplanır.

Kullanıcıdan giriş alınarak hesaplama yapılır.

Matplotlib ile girdi ve çıktı üyelik fonksiyonları grafiksel olarak gösterilir.

Tkinter ile sekmeli GUI arayüz sunar:

Giriş sekmesi

Girdi grafikler sekmesi

Çıktı grafikler sekmesi

#🧠 Kullanılan Değişkenler
Girdi Değişkenleri:
Toprak Nemi (%)

Hava Sıcaklığı (°C)

Rüzgar Hızı (km/h)

Yağmur Olasılığı (%)

Bitki Türü: Sebze, Meyve, Tahıl

Çıktı Değişkenleri:
Sulama Süresi (dk): Kısa, Orta, Uzun

Sulama Sıklığı (kez/gün): Az, Orta, Sık

#📐 Kurallar
Sistemde 5 temel bulanık kural bulunmaktadır. Örneğin:

Eğer toprak nemi düşük, hava sıcaklığı sıcak ve yağmur olasılığı düşükse;
sulama süresi uzun, sulama sıklığı sık olur.
