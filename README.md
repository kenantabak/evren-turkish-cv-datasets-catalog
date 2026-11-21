# evren-turkish-cv-datasets-catalog

[![Hugging Face Catalog](https://img.shields.io/badge/Hugging_Face-Parquet_%26_Sample_Images-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/datasets/kenantabak/evren-turkish-computer-vision-316-datasets)
[![Interactive Explorer](https://img.shields.io/badge/HF_Space-Canlı_Veri_Seti_Gezgini-10b981?style=flat-square)](https://huggingface.co/spaces/kenantabak/EVREN-316-Datasets-Catalog)

**[EVREN](https://evren.ssyz.org.tr/users/u19979974710e)** platformunda `CC-BY-4.0` lisansıyla yayımlanan **316 adet bilgisayarlı görü veri setinin (`3.292.480` görsel · `31.363.042` etiket)** makine tarafından okunabilir `CSV`/`JSON` indeksi, CLI arama aracı ve keşif defteri (`Jupyter Notebook`).

> Tam görsel önizlemeli Parquet tabloları ve örnek YOLO etiket paketleri için **[Hugging Face Koleksiyonu](https://huggingface.co/datasets/kenantabak/evren-turkish-computer-vision-316-datasets)** ziyaret edilebilir.

## Sektörel Kümeler (Hugging Face)

| Sektör / Alan | Veri Seti | Görsel | Bağlantı |
| :--- | :---: | ---: | :--- |
| **İHA, Termal IR & Havacılık** | 45 | 566.068 | [HF Dataset](https://huggingface.co/datasets/kenantabak/evren-uav-aerial-defense-vision-suite) |
| **Tıbbi Görüntüleme & Radyoloji** | 62 | 282.813 | [HF Dataset](https://huggingface.co/datasets/kenantabak/evren-medical-imaging-radiology-vision-suite) |
| **Otonom Sürüş & Trafik** | 53 | 442.785 | [HF Dataset](https://huggingface.co/datasets/kenantabak/evren-autonomous-driving-traffic-vision-suite) |
| **Endüstriyel Kalite & İSG (KKD)** | 39 | 165.212 | [HF Dataset](https://huggingface.co/datasets/kenantabak/evren-industrial-safety-ppe-defect-suite) |
| **Akıllı Tarım & Orman Yangını** | 55 | 300.188 | [HF Dataset](https://huggingface.co/datasets/kenantabak/evren-smart-agriculture-forestry-vision-suite) |

## CLI ile Veri Seti Arama

```bash
python scripts/search_catalog.py --query drone --min-images 500 --limit 15
```

## Öne Çıkan En Büyük 25 Veri Seti (Tam Liste: `data/datasets_catalog_316.csv`)

| # | Veri Seti (EVREN) | Görev | Görsel | Etiket | Sınıf |
| :-: | :--- | :---: | ---: | ---: | ---: |
| 1 | [Sentetik Meyve ve Sebze Çeşitleri Nesne Tespiti (63 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/sentetik-meyve-ve-sebze-cesitleri-nesne-tespiti-63-sinif) | `object-detection` | **250,739** | 686,730 | 63 |
| 2 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 35, 312x312 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-35-312x312-79-sinif) | `image-segmentation` | **123,061** | 893,521 | 79 |
| 3 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 41, 312x312 (80 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-41-312x312-80-sinif) | `image-segmentation` | **123,061** | 894,109 | 80 |
| 4 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 36, 384x384 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-36-384x384-79-sinif) | `image-segmentation` | **123,030** | 893,165 | 79 |
| 5 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 32, 640x640 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-32-640x640-79-sinif) | `image-segmentation` | **123,019** | 893,098 | 79 |
| 6 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 34, 640x640 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-34-640x640-79-sinif) | `image-segmentation` | **123,019** | 893,098 | 79 |
| 7 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 37, 432x432 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-37-432x432-79-sinif) | `image-segmentation` | **122,326** | 887,675 | 79 |
| 8 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 38, 504x504 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-38-504x504-79-sinif) | `image-segmentation` | **119,627** | 869,610 | 79 |
| 9 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 39, 624x624 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-39-624x624-79-sinif) | `image-segmentation` | **118,411** | 858,190 | 79 |
| 10 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 40, 768x768 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-40-768x768-79-sinif) | `image-segmentation` | **117,889** | 856,420 | 79 |
| 11 | [MS COCO Günlük Nesne Segmentasyonu — Sürüm 6, 640x640 (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/ms-coco-gunluk-nesne-segmentasyonu-surum-6-640x640-79-sinif) | `image-segmentation` | **117,857** | 854,054 | 79 |
| 12 | [CCTV ve Çevre Nesne Tespiti (36 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/cctv-ve-cevre-nesne-tespiti-36-sinif) | `image-segmentation` | **104,726** | 524,798 | 36 |
| 13 | [Lojistik, Depo ve İş Güvenliği Nesne Tespiti (20 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/lojistik-depo-ve-is-guvenligi-nesne-tespiti-20-sinif) | `object-detection` | **94,560** | 362,808 | 20 |
| 14 | [Geniş Ölçekli Yol Çukuru ve Asfalt Çatlağı Tespiti (5 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/genis-olcekli-yol-cukuru-ve-asfalt-catlagi-tespiti-5-sinif) | `object-detection` | **64,752** | 100,073 | 5 |
| 15 | [Hava Görüntülerinden Tarla Ekim Sıraları ve Parsel Şeritleri Segmentasyonu (1 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/hava-goruntulerinden-tarla-ekim-siralari-ve-parsel-seritleri-segmentasyonu-1-sinif) | `image-segmentation` | **55,351** | 538,955 | 1 |
| 16 | [Çok Sınıflı Yemek ve İçecek Tespiti (17 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/cok-sinifli-yemek-ve-icecek-tespiti-17-sinif) | `object-detection` | **41,062** | 41,062 | 17 |
| 17 | [Bağlam İçinde Günlük ve İç Mekan Nesneleri Tespiti — 40K Kümesi (79 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/baglam-icinde-gunluk-ve-ic-mekan-nesneleri-tespiti-40k-kumesi-79-sinif) | `object-detection` | **40,669** | 292,417 | 79 |
| 18 | [Denizcilik ve Askeri Gemi Tespiti (13 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/denizcilik-ve-askeri-gemi-tespiti-13-sinif) | `object-detection` | **39,000** | 39,212 | 13 |
| 19 | [Hava Görüntülerinden Genç Tarla Bitkisi ve Fide Sayımı Tespiti (1 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/hava-goruntulerinden-genc-tarla-bitkisi-ve-fide-sayimi-tespiti-1-sinif) | `object-detection` | **30,897** | 9,171,966 | 1 |
| 20 | [Hava Görüntülerinden Bina, Yol, Ağaç ve Araç Segmentasyonu (4 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/hava-goruntulerinden-bina-yol-agac-ve-arac-segmentasyonu-4-sinif) | `image-segmentation` | **28,768** | 397,706 | 4 |
| 21 | [Hava Görüntülerinden Kule ve Direk Yapıları Tespiti (1 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/hava-goruntulerinden-kule-ve-direk-yapilari-tespiti-1-sinif) | `object-detection` | **26,088** | 26,939 | 1 |
| 22 | [Drone Görüntülerinden İnsan, Taşıt ve İniş Alanı Tespiti (4 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/drone-goruntulerinden-insan-tasit-ve-inis-alani-tespiti-4-sinif) | `object-detection` | **25,679** | 304,403 | 4 |
| 23 | [PCB Baskı Devre Kartı Kusur Tespiti (6 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/pcb-baski-devre-karti-kusur-tespiti-6-sinif) | `object-detection` | **24,896** | 53,707 | 6 |
| 24 | [İskambil Kartları Nesne Tespiti — Genişletilmiş (52 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/iskambil-kartlari-nesne-tespiti-genisletilmis-52-sinif) | `object-detection` | **24,233** | 96,909 | 52 |
| 25 | [Hava Görüntülerinden Küçük Ölçekli Taşıt Tespiti (2 Sınıf)](https://evren.ssyz.org.tr/datasets/u19979974710e/hava-goruntulerinden-kucuk-olcekli-tasit-tespiti-2-sinif) | `object-detection` | **24,127** | 563,353 | 2 |
