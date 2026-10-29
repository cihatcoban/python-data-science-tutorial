# 12 Haftalık Veri Bilimi ve Mühendisliği Yol Haritası (Curriculum Roadmap)

Bu yol haritası, sıfırdan başlayan bir öğrenciyi veya yazılımcıyı modern veri bilimi, istatistiksel modelleme ve üretime hazır makine öğrenmesi mühendisliği seviyesine taşımak üzere tasarlanmıştır.

---

## 🗓 Haftalık Müfredat Çizelgesi

```text
Hafta 01-04: Seviye 1 - Python & Veri Temelleri (Foundations)
Hafta 05-08: Seviye 2 - Veri Analitiği, İstatistik & Görselleştirme (Intermediate)
Hafta 09-12: Seviye 3 - Makine Öğrenmesi, Model Değerlendirme & MLOps (Advanced)
```

### 🔹 Hafta 1-4: Seviye 1 - Python & Veri Temelleri
* **Hafta 1: Python Sözdizimi, Bellek Modeli ve Veri Yapıları**
  - Temel veri tipleri (`int`, `float`, `str`, `bool`) ve tip dönüşümleri.
  - Koleksiyonlar (`list`, `tuple`, `dict`, `set`) ve aralarındaki algoritmik karmaşıklık farkları.
  - String formatlama (`f-string`) ve metin işleme pratikleri.
* **Hafta 2: Kontrol Akışı, Döngüler ve Fonksiyonel Yaklaşım**
  - Mantıksal operatörler ve koşul blokları (`if-elif-else`).
  - Döngü yapıları (`for`, `while`) ve performans optimizasyonları (`enumerate`, `zip`).
  - List & Dict Comprehension yapıları ile veri süzme.
* **Hafta 3: Fonksiyonel Programlama ve İleri Düzey Fonksiyonlar**
  - Birinci sınıf fonksiyonlar (First-Class Functions), `*args` ve `**kwargs`.
  - Lambda ifadeleri, `map`, `filter` fonksiyonları.
  - Dekoratörler (Decorators) ile loglama ve süre ölçümü; Jeneratörler (`yield`) ile bellek verimli veri akışı.
* **Hafta 4: Nesne Tabanlı Programlama (OOP), Hata Yönetimi ve Dosya I/O**
  - Sınıf (Class) ve Örnek (Instance) kavramları, kalıtım (inheritance) ve kapsülleme (encapsulation).
  - Modern `@dataclass` kullanımı ve tip ipuçları (`type hints`).
  - Savunmacı programlama: `try-except-else-finally` ve özel istisnalar (`CustomException`).
  - Dosya I/O: Metin, CSV, JSON ve Parquet formatlarında veri kaydetme/okuma.
  - **Dönüm Noktası Projesi 1:** Modüler Öğrenci Not Analiz ve İstatistik Motoru.

---

### 🔹 Hafta 5-8: Seviye 2 - Veri Analizi, İstatistik & Görselleştirme
* **Hafta 5: NumPy ile Nümerik Hesaplama ve Vektörizasyon**
  - `ndarray` mimarisi, bellek dizilimi (stride, contiguous memory).
  - Broadcasting mekanizması ve vektörize operasyonların döngülere karşı hız avantajı ($10x-50x$).
  - Matris işlemleri, lineer cebir temelleri (`np.linalg`) ve matematiksel fonksiyonlar.
* **Hafta 6: Pandas ile Veri Manipülasyonu ve Wrangling**
  - Series ve DataFrame nesneleri.
  - Hızlı indeksleme ve filtreleme (`.loc`, `.iloc`, boolean indexing).
  - Gruplama (`groupby`) ve çoklu toplulaştırma (`agg`), pivot tablolar.
  - Çoklu veri kümelerini birleştirme (`merge`, `join`, `concat`).
* **Hafta 7: Keşifçi Veri Analizi (EDA) ve Veri Temizleme**
  - Eksik veri stratejileri: Silme, medyan/ortalama atama (imputation), KNN imputer.
  - Uç değer (outlier) analizi: Tukey's IQR yöntemi, Z-score ve sınırlandırma (clipping/capping).
  - Veri tipi dönüşümleri, duplike kayıt ayıklama ve veri doğrulama.
* **Hafta 8: Veri Görselleştirme ve İstatistiksel Çıkarım**
  - Matplotlib Object-Oriented arayüzü ile yayına hazır grafikler.
  - Seaborn ile istatistiksel dağılımlar (KDE, Boxplot, Violin, Pairplot, Heatmap).
  - Plotly ile interaktif dashboard hazırlama.
  - Betimsel istatistik, olasılık dağılımları ve hipotez testleri ($t$-test, ANOVA, Ki-Kare).
  - Web scraping ve REST API'lardan yapılandırılmış veri çekme.
  - **Dönüm Noktası Projesi 2:** Uçtan Uca Konut/E-Ticaret Veri Analitiği ve Raporlama Paneli.

---

### 🔹 Hafta 9-12: Seviye 3 - Makine Öğrenmesi & Keystone MLOps
* **Hafta 9: Özellik Mühendisliği (Feature Engineering)**
  - Sayısal değişken ölçekleme: `StandardScaler`, `MinMaxScaler`, `RobustScaler`.
  - Kategorik değişken kodlama: One-Hot Encoding, Ordinal Encoding, Target Encoding.
  - Tarih-saat özellikleri, etkileşim terimleri ve polinom özellikler.
  - Boyut indirgeme: Temel Bileşen Analizi (PCA) ve varyans korunumu.
* **Hafta 10: Denetimli Öğrenme (Supervised Learning) Algoritmaları**
  - Regresyon: Lineer Regresyon, Ridge, Lasso, ElasticNet.
  - Sınıflandırma: Lojistik Regresyon, Destek Vektör Makineleri (SVM), Karar Ağaçları.
  - Topluluk Öğrenmesi (Ensemble): Random Forest, Gradient Boosting, XGBoost ve LightGBM.
* **Hafta 11: Model Değerlendirme, Doğrulama ve Veri Sızıntısı**
  - Metrikler: RMSE, MAE, $R^2$, Accuracy, Precision, Recall, F1-Score, ROC-AUC, PR-AUC.
  - Çapraz doğrulama stratejileri: $K$-Fold, Stratified $K$-Fold, TimeSeriesSplit.
  - **Veri Sızıntısını (Data Leakage)** engelleme kuralları ve `train/test split` bütünlüğü.
  - Hiperparametre optimizasyonu (`GridSearchCV`, `RandomizedSearchCV`).
* **Hafta 12: Denetimsiz Öğrenme ve Üretime Hazır Pipeline Mimarisi**
  - K-Means kümeleme, Silhouette Skoru analizi ve Isolation Forest ile anomali tespiti.
  - Scikit-Learn `Pipeline` ve `ColumnTransformer` ile modüler model hattı.
  - Model serileştirme (`joblib`) ve çıkarım betiği (`predict.py`).
  - Keystone mühendislik standartları: `src/` paketi, `pytest` birim testleri, CI/CD ve Docker.
  - **Bitirme Projesi (Capstone):** Üretime Hazır, Test Edilmiş ve Konteynerleştirilmiş Makine Öğrenmesi Servisi.
