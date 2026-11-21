# Veri Seti Şeması ve Standartlar (`datasets_catalog_316.csv`)

## Alan Açıklamaları

| Sütun | Tür | Açıklama |
| :--- | :--- | :--- |
| `id` | `string (UUID)` | EVREN platformundaki benzersiz veri seti kimliği |
| `name` | `string` | Türkçe açıklayıcı veri seti başlığı ve aktif sınıf sayısı |
| `evren_url` | `string` | Doğrudan veri seti detay ve dışa aktarım sayfası |
| `tasks` | `string` | `object_detection`, `instance_segmentation` veya `image_classification` |
| `image_count` | `integer` | Toplam görsel sayısı |
| `annotation_count` | `integer` | Toplam Bounding Box / Poligon etiket sayısı |
| `class_count` | `integer` | Sıfır etiketli çöp sınıflar temizlendikten sonraki aktif sınıf sayısı |
| `license` | `string` | `CC-BY-4.0` |

## Bölütleme Standardı

Tüm veri setleri deterministik olarak **`%70 Eğitim (train) / %20 Doğrulama (val) / %10 Test`** oranıyla yapılandırılmıştır.
