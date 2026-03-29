import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.stats import poisson

# 1. Gözlemlenen Trafik Verisi
traffic_data = np.array([12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15])

# 2. Negatif Log-Olabilirlik (NLL) Fonksiyonu
def negative_log_likelihood(lam, data):
    """
    Poisson dağılımı için Negatif Log-Likelihood hesaplar.
    log(k!) terimi sabit olduğu için ihmal edilmiştir.
    """
    n = len(data)
    # Formül: - ( -n*lambda + sum(k)*ln(lambda) )
    nll = -(-n * lam + np.sum(data) * np.log(lam))
    return nll

# 3. Sayısal Optimizasyon
initial_guess = 1.0
result = opt.minimize(negative_log_likelihood, initial_guess, args=(traffic_data,), bounds=[(0.001, None)])
mle_lambda = result.x[0]

# Sonuçları Yazdırma
print("-" * 30)
print(f"Sayısal Tahmin (MLE lambda): {mle_lambda:.4f}")
print(f"Analitik Tahmin (Ortalama): {np.mean(traffic_data):.4f}")
print("-" * 30)

# 4. Outlier (Aykırı Değer) Analizi - Raporun 4. Bölümü İçin
outlier_data = np.append(traffic_data, 200)
result_outlier = opt.minimize(negative_log_likelihood, initial_guess, args=(outlier_data,), bounds=[(0.001, None)])
new_lambda = result_outlier.x[0]

print(f"200 Araçlık Outlier Sonrası Yeni Lambda: {new_lambda:.4f}")
print(f"Sapma Miktarı: {new_lambda - mle_lambda:.4f}")
print("-" * 30)

# 5. Görselleştirme
plt.figure(figsize=(10, 6))
plt.hist(traffic_data, bins=range(min(traffic_data), max(traffic_data) + 2), 
         density=True, alpha=0.6, color='skyblue', label='Gerçek Trafik Verisi', align='left')

x_ekseni = np.arange(0, 25)
plt.plot(x_ekseni, poisson.pmf(x_ekseni, mle_lambda), 'ro--', label=f'Poisson PMF (λ={mle_lambda:.2f})')

plt.title('Trafik Yoğunluğu Poisson Model Uyumu')
plt.xlabel('Dakikadaki Araç Sayısı')
plt.ylabel('Olasılık Yoğunluğu')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()