# İFE - TBB Stratejik Ortaklık Dashboard'u

Terminal tabanlı sunum script'inin (`tbb_proje.py`) Streamlit ile web
dashboard'una dönüştürülmüş hâli.

## Klasör Yapısı

```
tbb_ife_dashboard/
├── app.py               # Streamlit arayüzü (görüntüleme mantığı)
├── data.py               # Sunum içeriği (TBB gündemi, stratejiler, modeller vb.)
├── feedback_store.py     # Geri bildirim notlarının JSON'a kalıcı kaydı
├── requirements.txt
└── README.md
```

Veri (`data.py`) ile arayüz (`app.py`) birbirinden ayrıldığı için:
- Sunum içeriğini güncellemek için sadece `data.py` düzenlenir.
- Yeni bir bölüm eklemek için `SECTIONS` sözlüğüne yeni bir `key`
  eklemek yeterlidir; arayüz otomatik olarak yeni bölümü menüye ekler.

## Kurulum

```bash
cd tbb_ife_dashboard
pip install -r requirements.txt
```

## Çalıştırma

```bash
streamlit run app.py
```

Tarayıcıda otomatik olarak `http://localhost:8501` açılır.

## Özellikler

- **Ana Sayfa**: Tüm bölümlerin kart görünümünde özeti.
- **5 Sunum Bölümü**: TBB Gündemi, Sektörel Handikaplar, Stratejiler,
  İş Birliği Modelleri, Cross-Sell — her madde tıklanarak (expander)
  detaylı stratejik argüman açılır (orijinal script'teki "detay okuma"
  akışının web karşılığı).
- **Geri Bildirim / Notlar**: İFE ekibi canlı sunum sırasında not
  ekleyebilir; notlar `feedback_log.json` dosyasında kalıcı olarak
  saklanır (script kapatılsa/tekrar açılsa bile silinmez).
- **Kurumsal tema**: Lacivert + altın renk paleti ile bankacılık
  sektörüne uygun sade tasarım.

## Notlar

- Orijinal script'teki `[G] Ana Menüye Dön` ve numara girme akışı,
  web arayüzünde sol menü (sidebar) ve genişletilebilir kartlarla
  (expander) karşılanmıştır.
- `exit_program()` fonksiyonuna web arayüzünde ihtiyaç yoktur;
  tarayıcı sekmesi kapatılarak sunum sonlandırılır.
# tbb_ife_dashboard
