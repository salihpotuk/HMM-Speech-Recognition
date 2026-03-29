# HMM-Speech-Recognition

## 1. Problem Tanımı [cite: 1, 2]
Bu proje, HMM kullanarak izole kelime tanıma (EV ve OKUL) simülasyonudur[cite: 20].

## 2. Teorik Hesaplama (Viterbi) [cite: 17]
$[High, Low]$ gözlemi için yapılan Viterbi hesaplaması:
- $t=1$: $\delta_1(e) = 0.7$, $\delta_1(v) = 0.0$ [cite: 15, 18]
- $t=2$: $\delta_2(e) = 0.126$, $\delta_2(v) = 0.252$ [cite: 12, 16]
- **Sonuç:** En olası fonem dizisi 'e-v'dir[cite: 17].

## 3. Analiz Yanıtları [cite: 37]
- **Gürültü:** Emisyon olasılıklarının belirsizleşmesine (dağılmasına) neden olur[cite: 38].
- **Derin Öğrenme:** Binlerce kelimelik sistemlerde uzun vadeli bağlamı (context) HMM'den daha iyi yakalar[cite: 39].

## 4. Dosya Yapısı [cite: 44-52]
- `src/recognizer.py`: Python kodları[cite: 48].
- `report/cozum_anahtari.pdf`: El hesaplamaları raporu[cite: 50].
