import numpy as np

# Deneme amaçlı basit bir karesel matris tanımlayalım
# Ödev dökümanındaki karesel matris şartına uygun [cite: 66]
A = np.array([[4, 2], 
              [1, 3]])

def manuel_ozdeger_hesapla(matris, iterasyon=100):
    """
    Numpy eig fonksiyonunu kullanmadan, Power Iteration yöntemiyle 
    en büyük özdeğeri hesaplar. Referans: LucasBN repository[cite: 73].
    """
    # Rastgele bir başlangıç vektörü (özvektör adayı)
    n = matris.shape[1]
    v = np.random.rand(n)
    
    for _ in range(iterasyon):
        # Matris ile vektörü çarpıp yönü buluyoruz
        v_yeni = np.dot(matris, v)
        # Vektörü normalize ederek (boyunu 1 yaparak) taşmaları önlüyoruz
        v = v_yeni / np.linalg.norm(v_yeni)
        
    # Rayleigh quotient formülü ile özdeğeri bulma
    ozdeger = np.dot(np.dot(matris, v), v) / np.dot(v, v)
    return ozdeger, v

# 1. Kendi yazdığımız fonksiyonla hesaplama
manuel_val, manuel_vec = manuel_ozdeger_hesapla(A)

# 2. Numpy'ın hazır linalg.eig fonksiyonu ile hesaplama [cite: 66, 74]
numpy_vals, numpy_vecs = np.linalg.eig(A)

print("--- Özdeğer ve Özvektör Karşılaştırması ---")
print(f"Manuel Hesaplama (En Büyük Özdeğer): {manuel_val:.5f}")
print(f"Numpy eig Sonuçları: {numpy_vals}")

# Sonuçların karşılaştırılması [cite: 74]
en_buyuk_np = np.max(numpy_vals)
fark = abs(manuel_val - en_buyuk_np)

print(f"\nİki yöntem arasındaki fark: {fark:.10f}")
if fark < 1e-5:
    print("Sonuçlar tutarlı, manuel hesaplama başarılı!")
else:
    print("Sonuçlar arasında fark var, iterasyon sayısı artırılabilir.")
