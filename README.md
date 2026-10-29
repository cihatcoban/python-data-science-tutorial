# Python for Data Science Mastery 🚀
### Sıfırdan İleri Seviyeye ve Üretim Standartlarına Veri Bilimi

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Architecture: Keystone](https://img.shields.io/badge/Architecture-Keystone%20Framework-orange.svg)](https://github.com/cihatcoban/keystone)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI Pipeline](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

Bu depo, temel Python programlama kavramlarından başlayarak modern veri analitiği, istatistik, makine öğrenmesi ve üretime hazır (production-grade) MLOps pratiklerine uzanan kapsamlı bir **Veri Bilimi ve Mühendisliği Müfredatıdır**. 

Geliştirme süreci ve mimari tasarım, [cihatcoban/keystone](https://github.com/cihatcoban/keystone) mühendislik çerçevesinin (Keystone Engineering Framework) **"Clean Code, Modular Architecture, Rigorous Testing and No Silent Failures"** ilkeleri rehberliğinde baştan aşağı yeniden yapılandırılmıştır.

---

## 📌 İçindekiler
1. [Müfredat Mimarisi (3 Seviye)](#-müfredat-mimarisi-3-seviye)
2. [Keystone Mühendislik İlkeleri](#-keystone-mühendislik-ilkeleri)
3. [Dizin ve Dosya Yapısı](#-dizin-ve-dosya-yapısı)
4. [Hızlı Başlangıç & Kurulum](#-hızlı-başlangıç--kurulum)
5. [src/ Reusable Toolbox Kütüphanesi](#-src-reusable-toolbox-kütüphanesi)
6. [Test, Kalite Kontrol ve Otomasyon (Makefile)](#-test-kalite-kontrol-ve-otomasyon-makefile)
7. [Katkıda Bulunma & Lisans](#-katkıda-bulunma--lisans)

---

## 🎓 Müfredat Mimarisi (3 Seviye)

Müfredat, öğrencinin bilişsel yükünü optimize eden ve her adımda bir önceki bilginin üzerine inşa edilen 3 ana kademeden oluşmaktadır:

```mermaid
flowchart LR
    A[Seviye 1: Giriş / Foundations] --> B[Seviye 2: Orta / Data Analytics & Stats]
    B --> C[Seviye 3: İleri / ML & Production Pipelines]
    style A fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px
    style B fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
    style C fill:#fff3e0,stroke:#ff9800,stroke-width:2px
```

### 1. Seviye 1: Giriş (Foundations - Python & Temel Veri Yapıları)
* **01_data_types_and_structures.ipynb**: Sayısal tipler, string manipülasyonu, listeler, tuple'lar, sözlükler, kümeler ve bellek/zaman karmaşıklığı ($O(1)$ vs $O(n)$ aramalar).
* **02_control_flow_and_loops.ipynb**: Karşılaştırma ve mantıksal operatörler, `if-elif-else`, döngüler (`for`, `while`), `enumerate`, `zip`, list/dict comprehensions.
* **03_functions_and_functional_python.ipynb**: Modüler fonksiyon tasarımı, `*args`, `**kwargs`, lambda fonksiyonları, `map`/`filter`, jeneratörler (`yield`) ve dekoratörler.
* **04_oop_and_dataclasses.ipynb**: Nesne Tabanlı Programlama, kalıtım, soyutlama, sihirli metodlar (`__repr__`, `__len__`, `__eq__`) ve modern `@dataclass` kullanımı.
* **05_exceptions_and_debugging.ipynb**: Hata ve istisna yönetimi (`try-except-else-finally`), özel istisna sınıfları (`CustomException`), savunmacı programlama ve `logging`.
* **06_file_io_and_serialization.ipynb**: Context manager (`with`), metin dosyaları, CSV, JSON, Parquet formatları ve modüler öğrenci not hesaplama vaka analizi.
* **exercises/foundation_exercises.ipynb**: Pekiştirme ödevleri, algoritma bulmacaları (Fibonacci, Asal Sayılar, ATM Simülatörü, İstatistiksel Veri Ayrıştırıcı) ve unit testleri.

### 2. Seviye 2: Orta (Intermediate - Veri Analizi, İstatistik & Görselleştirme)
* **01_numpy_numerical_computing.ipynb**: N-boyutlu diziler (`ndarray`), broadcasting kuralları, vektörizasyon, lineer cebir ve saf Python ile performans kıyaslaması.
* **02_pandas_data_wrangling.ipynb**: Series ve DataFrame yapıları, indeksleme (`.loc`, `.iloc`), filtreleme, eksik veri (`NaN`) yönetimi, `groupby`, aggregations ve tablo birleştirmeleri (`merge`, `join`, `concat`).
* **03_eda_and_data_cleaning.ipynb**: Keşifçi Veri Analizi (EDA) iş akışı, uç değer (outlier) tespiti (IQR, Z-score), veri tipi dönüşümleri ve veri tutarlılık denetimleri.
* **04_data_visualization.ipynb**: Matplotlib Object-Oriented API mimarisi, Seaborn ile istatistiksel dağılımlar/ilişkiler, Plotly ile interaktif grafikler ve yayına hazır görselleştirme standartları.
* **05_statistical_foundations.ipynb**: Betimsel istatistik, olasılık dağılımları, Merkezi Limit Teoremi, hipotez testleri ($t$-test, Mann-Whitney U, Ki-Kare) ve korelasyon analizleri.
* **06_data_acquisition_and_apis.ipynb**: Modern ve etik Web Scraping (BeautifulSoup, Requests, başlık ve hız yönetimi), REST API tüketimi ve yapılandırılmış JSON verisinin DataFrame'e dönüştürülmesi.

### 3. Seviye 3: İleri (Advanced - Makine Öğrenmesi & Keystone MLOps)
* **01_feature_engineering.ipynb**: Kategorik kodlama (One-Hot, Ordinal, Target), özellik ölçekleme (StandardScaler, RobustScaler), polinom özellikler ve özellik seçimi.
* **02_supervised_learning.ipynb**: Uçtan uca regresyon ve sınıflandırma modelleri (Linear/Ridge/Lasso, Random Forest, XGBoost/LightGBM), hiperparametre optimizasyonu (`GridSearchCV`, `Optuna` felsefesi).
* **03_unsupervised_learning.ipynb**: K-Means kümeleme, Dirsek Yöntemi (Elbow Method), Siluet Skoru, Boyut İndirgeme (PCA) ve Anomali Tespiti (Isolation Forest).
* **04_model_evaluation_metrics.ipynb**: Karışıklık matrisi, Precision, Recall, F1, ROC-AUC, PR-Curves, k-katlamalı çapraz doğrulama (StratifiedKFold) ve **Veri Sızıntısını (Data Leakage)** önleme prensipleri.
* **05_end_to_end_mlops_pipeline.ipynb**: Scikit-Learn `Pipeline` ve `ColumnTransformer` entegrasyonu, model serileştirme (`joblib`), konfigürasyon yönetimi, çıkarım (inference) betiği ve Keystone mühendislik standartları.

---

## 🏛 Keystone Mühendislik İlkeleri

Bu depodaki kodlama standartları, [cihatcoban/keystone](https://github.com/cihatcoban/keystone) framework'ünün temel direklerine dayanır:

1. **Önce Kısıtlar ve Şartname (`/constraints` & `/spec`)**: Kod yazılmadan önce girdiler, çıktılar, tip sözleşmeleri ve olası sınır durumlar belirlenir.
2. **Sessiz Hatalara Son (No Silent Failures)**: Hataları sessizce yutan (`except: pass`) bloklar yasaktır. İstisnalar açıkça tanımlanır, loglanır ve kontrollü bir şekilde yönetilir.
3. **Modülerlik ve Yeniden Kullanılabilirlik**: Notebook'larda doğrulanan mantık, `src/datascience_toolbox/` altındaki test edilebilir Python paketlerine taşınır.
4. **Test Odaklılık (High-Signal Unit Testing)**: Tüm veri dönüştürme ve temizleme fonksiyonları, deterministik `pytest` testleri ile güvence altına alınır.
5. **Tip Güvenliği ve Temiz Kod (PEP 8 & Type Hints)**: Fonksiyonlar ve sınıflar `typing` (`Union`, `Optional`, `Dict`, `List`, `DataFrame`) ile tip güvenliğine sahiptir.

---

## 📂 Dizin ve Dosya Yapısı

```text
python-data-science/
├── .github/
│   └── workflows/
│       └── ci.yml                     # Otomatik test, linting ve tip denetimi CI hattı
├── configs/
│   └── config.yaml                    # Merkezi konfigürasyon dosyası (veri yolları, tohumlar)
├── data/
│   ├── raw/                           # Değiştirilemez ham veriler (sample_students.csv, sample_housing.csv)
│   └── processed/                     # Modeller için temizlenmiş ve işlenmiş veri havuzu
├── docs/
│   ├── ROADMAP.md                     # 12 haftalık detaylı müfredat ve öğrenme yol haritası
│   ├── ARCHITECTURE.md                # Yazılım ve veri mimarisi dokümantasyonu
│   └── CONSTRAINTS.md                 # Keystone mühendislik ve kod standartları
├── notebooks/
│   ├── 01_foundations/                # Giriş Seviyesi (Python & Veri Temelleri)
│   │   ├── 01_data_types_and_structures.ipynb
│   │   ├── 02_control_flow_and_loops.ipynb
│   │   ├── 03_functions_and_functional_python.ipynb
│   │   ├── 04_oop_and_dataclasses.ipynb
│   │   ├── 05_exceptions_and_debugging.ipynb
│   │   ├── 06_file_io_and_serialization.ipynb
│   │   └── exercises/
│   │       └── foundation_exercises.ipynb
│   ├── 02_intermediate/               # Orta Seviye (Veri Analitiği, İstatistik & Görselleştirme)
│   │   ├── 01_numpy_numerical_computing.ipynb
│   │   ├── 02_pandas_data_wrangling.ipynb
│   │   ├── 03_eda_and_data_cleaning.ipynb
│   │   ├── 04_data_visualization.ipynb
│   │   ├── 05_statistical_foundations.ipynb
│   │   └── 06_data_acquisition_and_apis.ipynb
│   └── 03_advanced/                   # İleri Seviye (Makine Öğrenmesi & Üretim Hattı)
│       ├── 01_feature_engineering.ipynb
│       ├── 02_supervised_learning.ipynb
│       ├── 03_unsupervised_learning.ipynb
│       ├── 04_model_evaluation_metrics.ipynb
│       └── 05_end_to_end_mlops_pipeline.ipynb
├── src/                               # Üretime Hazır Reusable Python Kütüphanesi
│   └── datascience_toolbox/
│       ├── __init__.py
│       ├── data/                      # Veri yükleme ve temizleme bileşenleri
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   └── cleaner.py
│       ├── features/                  # Scikit-learn uyumlu özel transformer sınıfları
│       │   ├── __init__.py
│       │   └── transformers.py
│       ├── models/                    # Model eğitme ve metrik değerlendirme motoru
│       │   ├── __init__.py
│       │   ├── trainer.py
│       │   └── evaluator.py
│       └── utils/                     # Loglama ve konfigürasyon yardımcıları
│           ├── __init__.py
│           ├── config.py
│           └── logger.py
├── tests/                             # Kapsamlı Pytest Test Paketi
│   ├── __init__.py
│   ├── test_loader.py
│   ├── test_cleaner.py
│   ├── test_transformers.py
│   └── test_evaluator.py
├── .dockerignore
├── .gitignore
├── .pre-commit-config.yaml            # Kod kalitesi için pre-commit kancaları
├── Dockerfile                         # Tekrarlanabilir konteyner ortamı
├── LICENSE                            # MIT Açık Kaynak Lisansı
├── Makefile                           # Geliştirme ve test otomasyon komutları
├── pyproject.toml                     # Modern paket ve araç konfigürasyonu
├── requirements.txt                   # Sabitlenmiş ana kütüphane bağımlılıkları
└── requirements-dev.txt               # Geliştirme, test ve linting araçları
```

---

## ⚡ Hızlı Başlangıç & Kurulum

### 1. Depoyu Klonlama ve Sanal Ortam Oluşturma
```bash
git clone https://github.com/cihatcoban/python-data-science.git
cd python-data-science

# Sanal ortam oluşturma ve aktive etme
python3 -m venv .venv
source .venv/bin/activate  # Windows için: .venv\Scripts\activate
```

### 2. Bağımlılıkları Yükleme
```bash
# Makefile ile tek komutta kurulum
make install-dev

# Veya pip ile
pip install -r requirements.txt -r requirements-dev.txt
pip install -e .
```

### 3. Jupyter Lab / Notebook Başlatma
```bash
make jupyter
# Tarayıcınızda açılan arayüzden notebooks/ klasöründeki derslere erişebilirsiniz.
```

---

## 🧰 src/ Reusable Toolbox Kütüphanesi

Depo içerisinde sadece notebook'lar değil, gerçek dünyada projelerinizde içe aktarabileceğiniz (`import`) modüler bir kütüphane yer alır:

```python
from datascience_toolbox.data.loader import load_dataset
from datascience_toolbox.data.cleaner import DataCleaner
from datascience_toolbox.features.transformers import OutlierCapper
from datascience_toolbox.models.evaluator import evaluate_classification

# 1. Güvenli veri yükleme
df = load_dataset("data/raw/sample_students.csv")

# 2. Pipeline ile temizleme ve uç değer sınırlama
cleaner = DataCleaner(fill_missing=True)
df_clean = cleaner.transform(df)

capper = OutlierCapper(factor=1.5)
df_capped = capper.fit_transform(df_clean)
```

---

## 🧪 Test, Kalite Kontrol ve Otomasyon (Makefile)

Keystone mühendislik standartlarını korumak adına tüm iş akışları `Makefile` ile otomatikleştirilmiştir:

| Komut | Açıklama |
| :--- | :--- |
| `make test` | `tests/` klasöründeki tüm unit testleri çalıştırır. |
| `make coverage` | Test kapsamını (coverage report) ölçer ve HTML rapor üretir. |
| `make lint` | `ruff` ve `flake8` ile kod stili ve hataları denetler. |
| `make format` | `ruff format` ve `black` ile kodları otomatik formatlar. |
| `make clean` | `__pycache__`, `.pytest_cache` ve derleme artıklarını temizler. |
| `make docker-build` | İzole Docker konteyner imajını derler. |

---

## 📜 Katkıda Bulunma & Lisans

Katkıda bulunmak için lütfen [docs/CONSTRAINTS.md](docs/CONSTRAINTS.md) dosyasındaki kodlama ve test standartlarını inceleyiniz.

Bu proje **MIT Lisansı** altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
