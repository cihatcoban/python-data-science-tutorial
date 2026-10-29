# Keystone Mühendislik Kısıtları ve Standartları (CONSTRAINTS.md)

Bu depo, [cihatcoban/keystone](https://github.com/cihatcoban/keystone) çerçevesinin kalite kapılarını (quality gates) uygular. Her geliştirme aşağıdaki kısıtlara uymak zorundadır:

---

## 🚫 Yasaklı Pratikler (Forbidden Patterns)
1. **Sessiz Hata Yutma (No Silent Errors):**
   ```python
   # YASAK:
   try:
       process_data()
   except:
       pass

   # ZORUNLU:
   try:
       process_data()
   except ValueError as e:
       logger.error(f"Veri işleme sırasında doğrulama hatası: {e}")
       raise DataProcessingError("Veri işlenemedi") from e
   ```
2. **Sabit Kodlanmış Dosya Yolları (No Hardcoded Paths):**
   * Dosya yolları doğrudan kod içine `"C:/Users/.../data.csv"` şeklinde yazılmaz.
   * `pathlib.Path` veya `configs/config.yaml` kullanılır.
3. **Veri Sızıntısı (No Data Leakage):**
   * Test verisi, eğitim aşamasındaki ön işleme (`fit_transform`) adımlarına asla dahil edilmez.
   * Ölçekleyiciler (`scaler`) yalnızca eğitim kümesine `fit()` edilir, test kümesine sadece `transform()` uygulanır.
4. **Notebook İçinde Karmaşık İş Mantığı (No God Notebooks):**
   * 20 satırdan uzun, tekrar kullanılabilir algoritmalar `src/` klasörüne fonksiyon/sınıf olarak taşınır ve notebook içinde çağrılır.

---

## ✅ Kodlama Standartları (Coding Standards)
1. **Tip İpuçları (Type Hints):** Tüm fonksiyon argümanları ve dönüş tipleri belirtilmelidir (`def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:`).
2. **Docstring:** Google formatında kapsamlı docstring zorunludur.
3. **Format ve Linting:** `ruff` ve `black` kurallarına tam uyum (maksimum satır uzunluğu 100 karakter).
4. **Test Kapsamı:** `src/` altındaki modüller için minimum %80 test kapsama oranı hedeflenir.
5. **Rastgelelik Tohumu (Reproducibility):** Stokastik modellerde `random_state=42` sabitlenmelidir.
