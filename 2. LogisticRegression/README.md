# MLE ile Akıllı Şehir Planlaması

Bu proje, bir caddeden geçen araç sayısını **Poisson Dağılımı** kullanarak modellemektedir. [cite_start]Parametre tahmini için **Maximum Likelihood Estimation (MLE)** yöntemi uygulanmıştır[cite: 4].

## Kullanılan Yöntemler
- [cite_start]**Teorik Türetme:** Log-likelihood fonksiyonunun türevi alınarak $\hat{\lambda}_{MLE}$ değerinin aritmetik ortalamaya eşit olduğu kanıtlanmıştır[cite: 11].
- [cite_start]**Sayısal Çözüm:** `scipy.optimize` kütüphanesi ile negatif log-olabilirlik fonksiyonu minimize edilmiştir[cite: 18].
- [cite_start]**Görselleştirme:** Elde edilen model ile gerçek veri histogramı karşılaştırılmıştır[cite: 40].

## Sonuçlar ve Tartışma
- [cite_start]**MLE Parametresi:** $\lambda = 12.1429$[cite: 35].
- [cite_start]**Outlier Analizi:** Veri setine eklenen aykırı değerlerin (200 araç) model tahminini ciddi oranda saptırdığı ve şehir planlamasında hatalı kararlara yol açabileceği tartışılmıştır[cite: 44, 45].
