# Mimari Tasarım Dokümantasyonu (ARCHITECTURE.md)

Bu doküman, deponun yazılım mimarisini, dizin organizasyonunu ve veri akış prensiplerini detaylandırır.

---

## 📐 Mimari Prensipler

Bu depo, tipik "sadece notebook içeren" veri bilimi depolarından farklı olarak, **yazılım mühendisliği disiplini** ile **veri bilimi keşif süreçlerini** harmanlar:

1. **İki Katmanlı Çalışma Modeli:**
   * **Keşif Katmanı (`notebooks/`):** Hipotezlerin test edildiği, görselleştirmelerin yapıldığı ve interaktif denemelerin yürütüldüğü Jupyter Notebook'lar.
   * **Üretim Katmanı (`src/datascience_toolbox/`):** Notebook'larda olgunlaşan, temizlenen ve tekrar kullanılabilir hale getirilen saf Python modülleri.
2. **Tek Yönlü Bağımlılık Kuralı:**
   * Notebook'lar `src/` altındaki fonksiyonları içe aktarabilir (`from datascience_toolbox import ...`).
   * `src/` altındaki kodlar asla notebook'lara veya dış kontrolsüz betiklere bağımlı olamaz.
3. **Konfigürasyon Bağımsızlığı:**
   * Sabit yollar (hardcoded paths) ve rastgele parametreler kod içine gömülmez; `configs/config.yaml` üzerinden yönetilir.

---

## 🔄 Veri ve Model İşleme Hattı (Data Pipeline)

```text
[ data/raw/ ] 
      │
      ▼ (src.data.loader)
[ Ham Veri Yükleme & Şema Doğrulama ]
      │
      ▼ (src.data.cleaner)
[ Eksik Veri & Uç Değer Temizliği ]
      │
      ▼ (data/processed/)
[ Temiz Veri Kümesi ]
      │
      ▼ (src.features.transformers)
[ Scikit-Learn ColumnTransformer / Feature Pipeline ]
      │
      ▼ (src.models.trainer)
[ Model Eğitimi & Çapraz Doğrulama ]
      │
      ▼ (src.models.evaluator)
[ Performans Metrikleri & ROC/PR Raporu ]
      │
      ▼
[ Model Artifaktı (.joblib) ]
```

---

## 🧩 Modül Bileşenleri (`src/datascience_toolbox`)

* `data/loader.py`: Veriyi güvenli şekilde okur, dosya varlığını denetler, dosya biçimini (CSV, Parquet) doğrular.
* `data/cleaner.py`: Belirlenen stratejilere göre eksik verileri tamamlar, sütun adlarını standartlaştırır.
* `features/transformers.py`: Scikit-Learn `BaseEstimator` ve `TransformerMixin` miras alan özel dönüştürücüler (`OutlierCapper`, vb.).
* `models/trainer.py`: Model eğitim döngülerini, hiperparametre aramalarını ve çapraz doğrulamayı yürütür.
* `models/evaluator.py`: Regresyon ve sınıflandırma için eksiksiz metrik sözlüğü ve rapor üretir.
* `utils/logger.py`: Konsola ve dosyaya yapılandırılmış, renkli ve seviyelendirilmiş loglama sağlar.
* `utils/config.py`: YAML konfigürasyonunu okuyup Python nesnesine dönüştürür.
