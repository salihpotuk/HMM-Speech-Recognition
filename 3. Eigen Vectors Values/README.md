Laboratuvar III: Özdeğerler ve Özvektörler Üzerine Bir İncelemeBu çalışma, YZM212 Makine Öğrenmesi dersi kapsamında, verinin temel yapı taşlarını anlamamızı sağlayan matris operasyonlarını ve özvektör (eigenvector) / özdeğer (eigenvalue) kavramlarını hem teorik hem de pratik boyutta ele almaktadır .

1. Makine Öğrenmesi Neden Matrislere İhtiyaç Duyar?Makine öğrenmesi modelleri aslında devasa birer matematiksel makinedir ve bu makinelerin dili matrislerdir.

Matris Manipülasyonu: Veri setlerimizdeki her bir satır ve sütun aslında birer vektördür. Bu verileri işlemek, ölçeklendirmek veya başka bir uzaya taşımak için matris çarpımlarını (dot product) kullanırız.Özdeğerler ve Özvektörlerin Rolü: Bir matrisi bir "dönüşüm" olarak hayal edersek, özvektörler bu dönüşüm sırasında yönü değişmeyen, sadece boyu uzayan veya kısalan (özdeğer kadar) özel yönlerdir.

Kullanılan Yöntemler: En yaygın kullanım alanı Temel Bileşen Analizi (PCA) ile boyut indirgemedir. Ayrıca PageRank algoritmasında ve görüntü sıkıştırma gibi işlemlerde de bu karakteristik değerlerden faydalanılır.

Okuma Notlarım: Çalışma sırasında Machine Learning Mastery üzerindeki temel rehberlerden faydalandım. Özellikle lineer cebirin ML pratiklerine nasıl döküldüğünü anlamak için faydalı kaynaklar.

2. İşin Mutfağı: numpy.linalg.eig Analizi

Numpy kütüphanesini her gün kullansak da, arka planda işlerin nasıl yürüdüğü bazen gözden kaçabiliyor. linalg.eig fonksiyonunun dökümanlarını ve kaynak kodlarını incelediğimde şu detaylar dikkatimi çekti

LAPACK Bağlantısı: Numpy, bu hesaplamaları doğrudan Python ile yapmaz. Arka planda çok daha hızlı olan ve Fortran/C ile yazılmış LAPACK kütüphanesindeki _geev rutinlerini çağırır.

QR Algoritması: Fonksiyon, özdeğerleri bulmak için genellikle matrisi önce üst üçgen forma getirir ve ardından iteratif bir QR algoritması uygular.

Girdi-Çıktı: Fonksiyonun karesel bir matris alması zorunludur ve sonuç olarak bize özdeğerleri içeren bir dizi ile özvektörlerin sütunlar halinde dizildiği bir matris döndürür.

3. Uygulama: Manuel Hesaplama vs. NumpyBu bölümde, Numpy'ın hazır fonksiyonunu kullanmadan, "Power Iteration" mantığıyla özdeğer hesaplaması yapılmıştır.

Yaklaşım: LucasBN'nin çalışması referans alınarak, matrisi rastgele bir vektörle defalarca çarparak en büyük özdeğere yakınsaması sağlandı.

Karşılaştırma: Kendi yazdığım manuel fonksiyonun sonucu ile np.linalg.eig fonksiyonunun verdiği sonuçları karşılaştırdığımda, hassasiyetin (precision) virgülden sonraki birçok basamağa kadar aynı olduğunu gözlemledim.

Hazırlayan: Salih Potuk

Öğrenci No: 24290101

Tarih: 29.03.2026
