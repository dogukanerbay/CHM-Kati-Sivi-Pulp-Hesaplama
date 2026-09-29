# CHM – Katı-Sıvı Hesaplama Uygulaması

Cevher hazırlama tesislerinde pulp (katı + su karışımı) hesaplarını hızlıca yapmak için Python ve Tkinter ile hazırlanmış masaüstü uygulaması. Katı ve sıvı miktarını (kg) girince pulpun toplam ağırlığını, katı ve sıvı yüzdelerini ve katı/sıvı oranını hesaplar.

## Ne yapar?

Girdiler:

- Katı miktarı (kg)
- Sıvı miktarı (kg)

Çıktılar:

- Toplam pulp ağırlığı (kg)
- Pulpte katı oranı (%)
- Pulpte sıvı oranı (%)
- Katı/sıvı oranı (%)

Girdi hatalı olduğunda (harf, boş alan) veya katı ya da sıvı 0 olduğunda kullanıcıyı uyarır.

## Kullanılan formüller

Katı miktarı **K**, sıvı miktarı **S** (kg):

| Hesap | Formül |
|---|---|
| Toplam pulp ağırlığı | `P = K + S` |
| Pulpte katı oranı | `%Katı = K / P · 100` |
| Pulpte sıvı oranı | `%Sıvı = S / P · 100` |
| Katı/sıvı oranı | `K / S · 100` |

## Kurulum ve çalıştırma

Ek kütüphane gerekmez, Tkinter Python ile birlikte gelir.

```bash
git clone https://github.com/dogukanerbay/CHM-Kati-Sivi-Pulp-Hesaplama.git
cd CHM-Kati-Sivi-Pulp-Hesaplama
python "Katı Sıvı İşlemleri.py"
```

Gereksinim: Python 3.x

## Örnek kullanım

| Girdi | Değer |
|---|---|
| Katı miktarı | 30 kg |
| Sıvı miktarı | 70 kg |

| Çıktı | Değer |
|---|---|
| Toplam ağırlık | 100.00 kg |
| Pulpte katı oranı | %30.00 |
| Pulpte sıvı oranı | %70.00 |
| Katı/sıvı oranı | %42.86 |


## Geliştirici

**Doğukan Erbay** – Cevher Hazırlama Mühendisi
GitHub: [dogukanerbay](https://github.com/dogukanerbay)
