# Sonraki sürüm: v0.6.0 — Intelligence Abstraction

Bu belge, v0.5.1 sonrası hedeflenen **v0.6.0** için yapılacakları özetler.

---

## Hedef

**Intelligence abstraction**: Karar verme mantığını “kural listesi”nden çıkarıp, ileride farklı “akıllı” bileşenlerin (kurallar, politika motoru, hatta ileride AI) takılabilmesi için soyut bir katman tanımlamak.

---

## Yapılması Gerekenler (önerilen sıra)

1. **DecisionEngine soyutlaması**
   - `DecisionEngine` şu an sadece “kural listesi + first-match-wins” biliyor.
   - Bir **DecisionStrategy** veya **DecisionProvider** arayüzü tanımla: “context al → DecisionResult döndür”.
   - Mevcut kural motoru bu arayüzün ilk implementasyonu olsun; böylece ileride “ikinci bir strateji” (örn. politika tabanlı, skorlama) eklenebilsin.

2. **Strategy / provider seçimi**
   - Config veya Core üzerinden “hangi strateji kullanılsın?” seçilebilsin (örn. `rule_based`, ileride `policy` veya `scoring`).
   - Varsayılan: mevcut rule-based davranış.

3. **Arayüzün dokümante edilmesi**
   - Hangi metodların hangi imzayla çağrılacağı, DecisionContext / DecisionResult’ın nasıl kullanılacağı `docs/architecture` altında yazılsın.
   - Böylece v0.6.0 “intelligence abstraction” mimari adımı netleşir.

4. **Testler**
   - Mevcut rule-based senaryolar (örn. EXAMPLE_READY, ilk 3 event) aynen çalışmaya devam etmeli.
   - Yeni arayüz için en az bir birim test (mock strategy ile) eklenmesi iyi olur.

5. **Roadmap / README**
   - README ve roadmap’te v0.6.0 “Intelligence abstraction” olarak işaretli kalabilir; bu doküman implementasyon tamamlandıkça “Completed” maddelere dönüştürülebilir.

---

## Yapılmayacaklar (v0.6.0 kapsamı dışı)

- Gerçek AI/LLM entegrasyonu (v0.7.0)
- Yeni modül türleri veya donanım köprüsü (roadmap’e göre sonraki adımlar)
- Veritabanı veya kalıcı persistence (şimdilik out of scope)

---

## Kısa özet

| Ne yapılacak? | Neden? |
|---------------|--------|
| Decision “strateji” arayüzü | İleride farklı karar motorları takılabilsin |
| Config ile strateji seçimi | Rule-based’den politika/skorlamaya geçiş kolaylaşsın |
| Dokümantasyon + test | Mimari net kalsın, geri dönüşüm kırılmasın |

Bu adımlar tamamlandığında proje “v0.6.0 — Intelligence abstraction” olarak etiketlenebilir ve CHANGELOG/README güncellenebilir.
