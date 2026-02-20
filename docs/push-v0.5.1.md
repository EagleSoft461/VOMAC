# v0.5.1'i GitHub'a Push Etme

## Seçenek 1: Yeni Branch Oluştur (Önerilen)

v0.5.1 için yeni bir branch oluşturup push et:

```powershell
cd "C:\Users\Alior\OneDrive\Masaüstü\VOMAC"

# Tüm değişiklikleri commit'le
git add .
git commit -m "Release v0.5.1: Snapshot Provider System, README and roadmap update"

# Yeni branch oluştur ve geç
git checkout -b v0.5.1-snapshot-providers

# Remote'u kontrol et (zaten varsa)
git remote -v

# Eğer remote yoksa ekle
git remote add origin https://github.com/EagleSoft461/VOMAC.git

# Branch'i push et
git push -u origin v0.5.1-snapshot-providers
```

## Seçenek 2: Mevcut Branch'e Push Et

Eğer gerçekten v0.4.1-task-routing branch'ine push etmek istiyorsan:

```powershell
cd "C:\Users\Alior\OneDrive\Masaüstü\VOMAC"

# Değişiklikleri commit'le
git add .
git commit -m "Release v0.5.1: Snapshot Provider System"

# v0.4.1-task-routing branch'ine geç (eğer yoksa oluştur)
git checkout -b v0.4.1-task-routing

# Veya mevcut branch'i pull et
git fetch origin
git checkout v0.4.1-task-routing
git pull origin v0.4.1-task-routing

# Push et
git push origin v0.4.1-task-routing
```

⚠️ **Not:** v0.4.1-task-routing eski bir branch. v0.5.1'i oraya push etmek geriye gidiş olur. Yeni branch oluşturman önerilir.
