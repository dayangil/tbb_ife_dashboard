# -*- coding: utf-8 -*-
"""
data.py
-------
TBB - İFE stratejik ortaklık sunumunun içerik verisi.

Bu dosya SADECE veriyi tutar; hiçbir görüntüleme (Streamlit/terminal)
mantığı içermez. Arayüz tarafı değişse bile (Streamlit, Flask, CLI vb.)
bu modül olduğu gibi kullanılabilir.

Yeni bir sunum bölümü eklemek için:
1) Aşağıdaki SECTIONS sözlüğüne yeni bir "key" ekleyin.
2) "title" ve "icon" belirleyin.
3) "items" içine {"baslik": "...", "detay": "..."} formatında maddeler ekleyin.
"""

SECTIONS = {
    "tbb_gundem": {
        "title": "TBB Gündemi ve İFE Tam Uyumu",
        "icon": "🎯",
        "menu_desc": "TBB Güncel Gündemi, Kapsam 3 ve Sektörel Uyum",
        "items": {
            "1": {
                "baslik": "Finansal Olmayan Veri Krizi (The Data Ghost) ve İFE Çözümü",
                "detay": (
                    "Durum Tespiti: Bankalar bilanço okumayı çok iyi bilir. Ancak "
                    "TSRS/ISSB ile ilk kez finansal olmayan (karbon emisyonu, iklim "
                    "riski) verilerle karşı karşıyalar.\n\n"
                    "Önerilen Çözüm: TBB'nin düzenlediği farkındalık zirveleri, "
                    "sektörde bu dönüşümün gerekliliğini anlatma konusunda önemli "
                    "bir işlev görmektedir. İFE, bu farkındalığı bir adım öteye "
                    "taşıyarak risk ve kredi ekiplerine bu yapı dışı verinin "
                    "finansal modele nasıl entegre edileceğini uygulamalı olarak "
                    "aktarır."
                ),
            },
            "2": {
                "baslik": "Kapsam 3 (Scope 3) Sızıntısı ve Kredi Portföy Riski",
                "detay": (
                    "Durum Tespiti: Bankanın asıl emisyon riski, kendi binaları "
                    "değil kredi verdiği büyük holdingler ve KOBİ'lerdir.\n\n"
                    "Önerilen Çözüm: Bankalar kurumsal müşterilerinden karbon verisi "
                    "toplayamazsa uluslararası piyasada Greenwashing damgası yer ve "
                    "sendikasyon kredileri tehlikeye girer. TBB-İFE ortaklığıyla "
                    "bankaların kredi verdiği müşterilere bir eğitim havuzu açarak "
                    "bu riski kökten çözmeyi teklif ediyoruz."
                ),
            },
            "3": {
                "baslik": "TBB Yapay Zeka Hamlesi ve Algoritmik Risk Yönetimi",
                "detay": (
                    "Durum Tespiti: TBB, üye bankalar için yapay zeka eğitimleri "
                    "organize etmektedir. Bu çalışmaların tamamlayıcısı olarak "
                    "sektörde Algoritmik Uyum alanında ek bir ihtiyaç "
                    "bulunmaktadır.\n\n"
                    "Önerilen Çözüm: İFE'nin Bankacılıkta Yapay Zeka ve FinTech "
                    "müfredatı, TBB ortak eğitim takvimine entegre edilerek yeni "
                    "nesil risk modellemesi ihtiyaçlarını karşılayabilir."
                ),
            },
        },
    },
    "sektorel_handikaplar": {
        "title": "Bankacılık Sektörel Handikapları ve Kritik Körlükler",
        "icon": "⚠️",
        "menu_desc": "Bankacılık Sektörel Handikapları ve Kritik Körlükler",
        "items": {
            "1": {
                "baslik": "Yeşil Varlık Oranı Çıkmazı (The Green Ratio Trap)",
                "detay": (
                    "Durum Tespiti: BDDK tebliği uyarınca bankalar kredilerin ne "
                    "kadarının gerçekten yeşil olduğunu raporlamak zorunda. Ancak "
                    "kredi yazılımları bu ayrımı otomatik yapamıyor.\n\n"
                    "Önerilen Çözüm: Bankalar şu an verileri manuel ayırmaya "
                    "çalışıyor. İFE olarak kredi ve hazine ekiplerine bu ayrımı "
                    "sistemsel ve matematiksel olarak nasıl yapacaklarını "
                    "öğretiyoruz. Raporlamayı değil, varlık yönetimini "
                    "sağlamlaştırıyoruz."
                ),
            },
            "2": {
                "baslik": "Bilanço Zamanlaması Krizi (The Time Gap)",
                "detay": (
                    "Durum Tespiti: KGK kurallarına göre TSRS Uyumlu "
                    "Sürdürülebilirlik Raporu, yıl sonu finansal tablolarıyla "
                    "birebir aynı anda yayınlanmak zorunda. Eskiden bu raporlar 6 "
                    "ay sonra keyfi hazırlanırdı.\n\n"
                    "Önerilen Çözüm: Finansal tablolarla sürdürülebilirlik verisini "
                    "aynı gün basmak bankalar için operasyonel bir kabustur. Biz "
                    "banka ekiplerine bu zaman krizini aşacak entegre raporlama "
                    "mimarisini anlatıyoruz."
                ),
            },
            "3": {
                "baslik": "Yapay Zekada Veri Zehirlenmesi ve ESG Manipülasyonu",
                "detay": (
                    "Durum Tespiti: ESG verileri büyük oranda manipülasyona açık "
                    "metinlerden oluşuyor. Yapay zeka bu kirli verilerle "
                    "beslendiğinde yanlış risk skorları üretiyor.\n\n"
                    "Önerilen Çözüm: Yapay zekanın sağladığı fayda ve vizyon "
                    "sektörde geniş biçimde ele alınırken, risk modellerine "
                    "yansıyan veri zehirlenmesi riski görece daha az konuşulan bir "
                    "alandır. İFE, bu riske karşı kurulacak risk filtreleme "
                    "metodolojisini uygulamalı olarak aktarır."
                ),
            },
        },
    },
    "stratejiler": {
        "title": "TBB Ekibini İkna Edecek Çözümler",
        "icon": "🧭",
        "menu_desc": "Sürdürülebilirlik ve TSRS Nokta Atışı Argümanlar",
        "items": {
            "1": {
                "baslik": "Sertifika Enflasyonunu Bitirmek (The Noise Filter)",
                "detay": (
                    "Durum Tespiti: Piyasada kısa süreli kurslarla verilen "
                    "sertifikaların sayısının artması, ESG uzmanlığı alanında "
                    "belirsizlik ve standart karmaşası yaratmaktadır.\n\n"
                    "Önerilen Çözüm: Üye bankalara yetkisiz kurumlardan alınan "
                    "dağınık eğitimler yerine, küresel standart koyucu IFRS "
                    "Foundation'ın resmi müfredatıyla TBB çatısı altında tek bir "
                    "referans standardın oluşturulması önerilir."
                ),
            },
            "2": {
                "baslik": "Raporu Denetleyenleri Değil, Parayı Yönetenleri Eğitiyoruz",
                "detay": (
                    "Durum Tespiti: KGK akreditasyonu yerel bağımsız denetçilere "
                    "imza yetkisi verir. Ancak bankanın parasını yöneten ekiplerin "
                    "imza yetkisiyle işi yoktur.\n\n"
                    "Önerilen Çözüm: Bankacının ihtiyacı raporu denetlemek değil, "
                    "projenin küresel fonlanma şartlarını analiz etmektir. Biz işi "
                    "doğrudan küresel kaynağından öğreterek analitik güç "
                    "sağlıyoruz."
                ),
            },
            "3": {
                "baslik": "Küresel Sendikasyon ve Londra/New York Piyasası Dili",
                "detay": (
                    "Durum Tespiti: Türk bankaları küresel piyasalardan "
                    "borçlanırken yabancı yatırımcı küresel IFRS Sustainability "
                    "Alliance standartlarına bakar.\n\n"
                    "Önerilen Çözüm: Banka personelinin TBB-İFE ortaklığıyla IFRS "
                    "lisanslı eğitim alması, bankaların yurt dışı borçlanma "
                    "süreçlerinde sunabileceği en büyük teknik ESG taahhüdüdür."
                ),
            },
        },
    },
    "modeller": {
        "title": "Önerilen B2B İş Birliği Modelleri",
        "icon": "🤝",
        "menu_desc": "Önerilen 3 Farklı B2B İş Birliği Modeli",
        "items": {
            "1": {
                "baslik": "Model A - TBB Eğitim Merkez Ortak Takvimi (Gelir Paylaşımı)",
                "detay": (
                    "İFE eğitimleri TBB Eğitim Merkezi takviminde yayınlanır. Gelir "
                    "ortaklaşa paylaşılarak TBB'ye sıfır maliyetle ek gelir "
                    "yaratılır."
                ),
            },
            "2": {
                "baslik": "Model B - Bankalara Özel Paket Dağıtım (Hacim Odaklı B2B)",
                "detay": (
                    "TBB, üye bankalara programı duyurur. Toplu katılım havuzu "
                    "sayesinde bankalara hacim indirimi sağlanarak bütçeler "
                    "optimize edilir."
                ),
            },
            "3": {
                "baslik": "Model C - Co-Branded (Ortak Markalı) Sektörel Sertifikasyon",
                "detay": (
                    "İFE - IFRS Foundation ve TBB logolu ortak uzmanlık sertifikası "
                    "verilerek sektörde tek altın standart oluşturulur."
                ),
            },
        },
    },
    "cross_sell": {
        "title": "İFE Geniş Portföyü (Uyum, Hazine ve Gelecek Vizyonu)",
        "icon": "🚀",
        "menu_desc": "Sürdürülebilirlik Sonrası Cross-Sell Yol Haritası",
        "items": {
            "1": {
                "baslik": "Finansal Suçlar ve Mevzuat Uyum (ICA ve CAMS Ortaklığı)",
                "detay": (
                    "Sürdürülebilirlikle giriş yaptıktan sonra bankaların AML "
                    "(Kara Para Aklama) ve uyum eğitimlerini TBB-İFE ortaklığıyla "
                    "standartlaştıracağız."
                ),
            },
            "2": {
                "baslik": "Hazine ve Kredi Ekipleri İçin İleri Finans (CFA ve FRM Giriş)",
                "detay": (
                    "Bankaların MT ve hazine ekiplerinin yurt dışından yüksek "
                    "maliyetle aldığı CFA eğitimlerini TBB çatısı altında "
                    "yerelleştiriyoruz."
                ),
            },
        },
    },
    "tbb_onerilen_egitimler": {
        "title": "TBB'ye Önerilen Eğitim Portföyü",
        "icon": "🎓",
        "menu_desc": "Bankalara Uygunluğu Teyit Edilmiş Master Liste ve Öncelikli 3 Eğitim",
        "items": {
            # ------------------------------------------------------------
            # ÖNCELİKLİ 3 EĞİTİM — One-shot satış için en yüksek olasılıklı
            # ------------------------------------------------------------
            "1": {
                "baslik": "[ÖNCELİK 1] Sürdürülebilirlik Raporlama ve İklim Riskleri",
                "detay": (
                    "Durum Tespiti: KGK kuralı gereği TSRS uyumlu sürdürülebilirlik "
                    "raporu artık yıl sonu finansal tablolarla aynı anda "
                    "yayınlanmak zorunda; bankalar bu zamanlama krizine ve ilk kez "
                    "karşılaştıkları finansal olmayan veri setine hazır değil.\n\n"
                    "Önerilen Çözüm: Bu eğitim, TBB gündeminizdeki 'Bilanço "
                    "Zamanlaması Krizi' ve 'Data Ghost' argümanlarının doğrudan "
                    "çözümü olduğu için satış anlatısı hazır durumda — mevzuat "
                    "baskısı zaten TBB tarafından hissediliyor.\n\n"
                    "Önerilen Eğitmen: Hasan Sarıçiçek (Dr.) — Sürdürülebilir "
                    "Finans ve ESG, İklim Teknolojileri alanında 20+ yıl deneyim."
                ),
            },
            "2": {
                "baslik": "[ÖNCELİK 2] Bankalar ve Finansal Kurumlar İçin MASAK Düzenlemeleri",
                "detay": (
                    "Durum Tespiti: MASAK uyumu her bankada zorunlu, tekrarlayan "
                    "ve geniş katılımcı tabanına (uyum, şube, hazine) yayılan bir "
                    "ihtiyaç — bütçe onayı diğer eğitimlere göre çok daha az "
                    "dirençle karşılanır.\n\n"
                    "Önerilen Çözüm: 1 günlük yoğunlaştırılmış format ve geniş "
                    "katılımcı tabanı sayesinde tek bir oturumda yüksek hacimli "
                    "satış potansiyeli taşır — 'one-shot' pitch için ideal giriş "
                    "ürünü.\n\n"
                    "Önerilen Eğitmen: Alpaslan Çakır (CAMS) veya Ali Ekber Polat "
                    "(Av., LL.M.) — ikisi de MASAK mevzuatı ve uyum programı "
                    "uzmanlığına sahip."
                ),
            },
            "3": {
                "baslik": "[ÖNCELİK 3] CAMS — Sertifikalı AML Uzmanı Sınav Hazırlık Programı",
                "detay": (
                    "Durum Tespiti: CAMS, dünyada AML alanında en çok tanınan "
                    "sertifika; banka uyum direktörleri için kariyer değeri "
                    "yüksek, bu da bireysel/kurumsal bütçe onayını kolaylaştırır.\n\n"
                    "Önerilen Çözüm: Sertifika prestiji üzerinden hem kurumsal "
                    "toplu satış hem de bireysel kayıt kanalını aynı anda "
                    "açar — çapraz satış potansiyeli en yüksek kalemlerden "
                    "biri.\n\n"
                    "Önerilen Eğitmen: Alpaslan Çakır (CAMS) — Denizbank AML&CFT "
                    "Bölüm Müdürü, TBB Bankacılar Dergisi yazarı."
                ),
            },
            # ------------------------------------------------------------
            # MASTER LİSTE — Bankacılık ve Sigortacılık
            # ------------------------------------------------------------
            "4": {
                "baslik": "Banka Sermaye ve Risk Yönetimi",
                "detay": "Önerilen Eğitmen: Ahmet Burak Emel (Dr.) veya Gürcan Avcı (Dr., CCM).",
            },
            "5": {
                "baslik": "Banka ve Finansal Kurumların Analizi",
                "detay": "Önerilen Eğitmen: Deniz Parlak (Prof. Dr.).",
            },
            "6": {
                "baslik": "Kurumsal Derecelendirme ve Ülke Kredi Riski",
                "detay": "Önerilen Eğitmen: Ertan Akbulut (Aktüer, CFO).",
            },
            "7": {
                "baslik": "Sorunlu Krediler ve Yeniden Yapılandırma",
                "detay": "Önerilen Eğitmen: Ertan Akbulut (Aktüer, CFO).",
            },
            "8": {
                "baslik": "Sigorta Şirketlerinde Mali Tablolar ve Analiz",
                "detay": "Önerilen Eğitmen: Neşe Varna Uğurkan (Dr., Aktüer).",
            },
            "9": {
                "baslik": "Banka Şube Yönetimi",
                "detay": (
                    "Önerilen Eğitmen: Ahmet Burak Emel (Dr.) — UniCredit'in "
                    "'En İyi Eğitim Uygulaması' seçtiği Şube Simülasyonu'nun "
                    "geliştiricisi."
                ),
            },
            "10": {
                "baslik": "Sigorta Şirketi Analizi ve Solvency II",
                "detay": "Önerilen Eğitmen: Neşe Varna Uğurkan (Dr., Aktüer).",
            },
            "11": {
                "baslik": "Bankalarda Hazine Yönetimi",
                "detay": "Önerilen Eğitmen: Temur Kayhan (Ph.D.) — Kuveyt Türk Quantitative Treasury Analyst geçmişi.",
            },
            "12": {
                "baslik": "Açık Bankacılık ve Dijital Ödeme Sistemleri",
                "detay": "Önerilen Eğitmen: Ramazan Küçük — BDDK geçmişi, Açık Bankacılık ve BaaS uzmanlığı.",
            },
            "13": {
                "baslik": "Dijital Bankacılık ve Müşteri Deneyimi",
                "detay": "Önerilen Eğitmen: TBD — kadroda net bir uzman görünmüyor, IFE ile teyit edilmeli.",
            },
            # ------------------------------------------------------------
            # MASTER LİSTE — Sürdürülebilirlik & ESG
            # ------------------------------------------------------------
            "14": {
                "baslik": "Sürdürülebilir Finans ve ESG Yatırımları",
                "detay": "Önerilen Eğitmen: Hasan Sarıçiçek (Dr.).",
            },
            "15": {
                "baslik": "İklim Risk Yönetimi ve Karbon Piyasaları",
                "detay": "Önerilen Eğitmen: Hasan Sarıçiçek (Dr.).",
            },
            "16": {
                "baslik": "Yeşil Tahvil ve Yenilenebilir Enerji Finansmanı",
                "detay": "Önerilen Eğitmen: Hasan Sarıçiçek (Dr.).",
            },
            "17": {
                "baslik": "Döngüsel Ekonomi ve Yeşil Yenilik",
                "detay": "Önerilen Eğitmen: TBD — IFE ile teyit edilmeli.",
            },
            "18": {
                "baslik": "Etki Yatırımı Prensipleri",
                "detay": "Önerilen Eğitmen: TBD — IFE ile teyit edilmeli.",
            },
            "19": {
                "baslik": "Sürdürülebilirlik Raporlama ve İklim Riskleri",
                "detay": "Önerilen Eğitmen: Hasan Sarıçiçek (Dr.) — bkz. Öncelik 1.",
            },
            "20": {
                "baslik": "Doğal Sermaye ve Biyoçeşitlilik Yatırımları",
                "detay": "Önerilen Eğitmen: TBD — IFE ile teyit edilmeli.",
            },
            "21": {
                "baslik": "Kurumsal ESG Stratejileri ve Raporlama",
                "detay": "Önerilen Eğitmen: TBD — IFE ile teyit edilmeli.",
            },
            # ------------------------------------------------------------
            # MASTER LİSTE — AML ve Uyum
            # ------------------------------------------------------------
            "22": {
                "baslik": "AML/CFT — Kara Para Aklama ve Terörizmin Finansmanı ile Mücadele",
                "detay": "Önerilen Eğitmen: Alpaslan Çakır (CAMS).",
            },
            "23": {
                "baslik": "Sınır Ötesi Suçlar ve Ticarete Dayalı Kara Para Aklama (TBML)",
                "detay": "Önerilen Eğitmen: Eyyüp Ensari Şahin (Doç. Dr.).",
            },
            "24": {
                "baslik": "Ödeme Kuruluşları, KVHS, Döviz Büroları için İleri Düzey AML/CFT",
                "detay": "Önerilen Eğitmen: Eyyüp Ensari Şahin (Doç. Dr.) veya Ramazan Küçük.",
            },
            "25": {
                "baslik": "MASAK Uyum Görevlisi Yetkilendirme Sınavı Hazırlık Eğitimi",
                "detay": "Önerilen Eğitmen: Ali Ekber Polat (Av., LL.M.).",
            },
            "26": {
                "baslik": "Küresel Uyum Trendleri Işığında Stratejik Yönetişim",
                "detay": "Önerilen Eğitmen: Gürcan Avcı (Dr., CCM).",
            },
            "27": {
                "baslik": "Bütünleşik Müşteri Kabulü ve İleri Düzey KYC Uzmanlığı",
                "detay": "Önerilen Eğitmen: Alpaslan Çakır (CAMS).",
            },
        },
    },
    "tbb_toplanti_pitch": {
        "title": "TBB Toplantı Sunumu — Ekim/Kasım Swissotel One-Shot Teklifi",
        "icon": "🎯🔥",
        "menu_desc": "1 Saatlik Toplantıda Satılacak 3 Kritik Eğitim — Öncelik Sırasına Göre",
        "items": {
            "1": {
                "baslik": "[0-15 dk] Sürdürülebilirlik Raporlama ve İklim Riskleri — Açılış Vuruşu",
                "detay": (
                    "Neden ilk sırada: Mevzuat baskısı (TSRS + yıl sonu tablo eşzamanlılığı) "
                    "hâlihazırda TBB gündeminde. Satış anlatısı hazır — biz sorunu "
                    "icat etmiyoruz, zaten var olan bir acil ihtiyaca çözüm sunuyoruz.\n\n"
                    "Toplantıda vurgu: 'Bu yıl sonu artık ertelenemez bir zamanlama krizi. "
                    "Ekim-Kasım'da Swissotel'de yapacağımız eğitim, yıl sonu raporlama "
                    "öncesi son hazırlık penceresi.'\n\n"
                    "Kapanış cümlesi önerisi: 'Bu eğitimi yıl sonu raporlama takviminize "
                    "göre planladık, bu yüzden Ekim veya Kasım'da yer ayırmanızı öneriyoruz.'\n\n"
                    "Eğitmen: Hasan Sarıçiçek (Dr.) — Sürdürülebilir Finans ve ESG, "
                    "İklim Teknolojileri alanında 20+ yıl deneyim."
                ),
            },
            "2": {
                "baslik": "[15-30 dk] MASAK Düzenlemeleri — Geniş Tabanlı Zorunlu Eğitim",
                "detay": (
                    "Neden ikinci sırada: Zorunlu ve tekrarlayan bir ihtiyaç, bütçe onayı "
                    "diğer eğitimlere göre çok daha az dirençle karşılanır. Toplantıda "
                    "birinci maddeden sonra 'işte kolay onaylanacak olan' diyerek geçiş "
                    "yapılabilir.\n\n"
                    "Toplantıda vurgu: '1 günlük yoğunlaştırılmış format, geniş katılımcı "
                    "tabanı (uyum, şube, hazine) ile tek oturumda yüksek hacimli satış.'\n\n"
                    "Kapanış cümlesi önerisi: 'Bu eğitimi aynı Swissotel programının "
                    "ikinci günü olarak planlayabiliriz, ekstra organizasyon maliyeti "
                    "olmadan.'\n\n"
                    "Eğitmen: Alpaslan Çakır (CAMS) veya Ali Ekber Polat (Av., LL.M.)."
                ),
            },
            "3": {
                "baslik": "[30-45 dk] CAMS Sertifika Programı — Prestij Odaklı Upsell",
                "detay": (
                    "Neden üçüncü sırada: İlk iki madde kurumu ikna ettikten sonra, "
                    "CAMS bireysel kariyer değeri üzerinden hem kurumsal toplu satışı "
                    "hem de bireysel kaydı aynı anda tetikler — toplantıyı 'tek eğitim "
                    "satışından' 'çoklu gelir kanalına' çevirir.\n\n"
                    "Toplantıda vurgu: 'Dünyada en çok tanınan AML sertifikası. Katılımcılar "
                    "hem TBB üzerinden hem bireysel olarak kayıt yaptırabilir.'\n\n"
                    "Kapanış cümlesi önerisi: 'CAMS'i üçüncü modül olarak ekleyip, "
                    "Swissotel programını 3 günlük bütünleşik bir sertifika serisine "
                    "dönüştürebiliriz.'\n\n"
                    "Eğitmen: Alpaslan Çakır (CAMS) — Denizbank AML&CFT Bölüm Müdürü."
                ),
            },
            "4": {
                "baslik": "[45-60 dk] Kapanış — Swissotel Ekim/Kasım Teklif Paketi",
                "detay": (
                    "Önerilen paket: 3 eğitim, Swissotel'de arka arkaya günlerde "
                    "(veya iki hafta arayla), TBB Eğitim Merkezi takvimine entegre.\n\n"
                    "Model önerisi: Model A (Gelir Paylaşımı) veya Model B (Hacim Odaklı "
                    "Paket) — TBB'ye sıfır maliyetle ek gelir vurgusu tekrar edilmeli.\n\n"
                    "Kapanış sorusu: 'Ekim mi Kasım mı sizin için daha uygun, ve hangi "
                    "sırayla ilerlemek istersiniz?' — bu, toplantıyı 'evet/hayır' "
                    "değil 'hangi tarih' sorusuna çevirir."
                ),
            },
        },
    },
    "flash_sale_pitch_strategy": {
        "title": "Flash Sale Stratejisi — Satış Pitch Notları (SADECE İÇ EKİP)",
        "icon": "🎯💬",
        "menu_desc": "Satış & Pazarlama bundle'ının TBB'ye nasıl sunulacağına dair iç notlar",
        "items": {
            "1": {
                "baslik": "Neden 'Flash Sale' Yaklaşımı Kullanıyoruz",
                "detay": (
                    "Ana 3 programın satışı kapandıktan sonra, toplantının son "
                    "dakikalarında hızlıca 'bir fırsat daha var' diyerek bu 2 eğitimi "
                    "sunuyoruz. Amaç: TBB'nin 'evet' modundayken ek bir karar almasını "
                    "kolaylaştırmak. Uzun bir sunum değil, 2-3 cümlelik bir teklif "
                    "olarak konumlandırılmalı.\n\n"
                    "Dip not: Bu asla ana teklifin önüne geçmemeli — sadece kapanışta "
                    "hızlı bir ek kazanç fırsatı olarak sunulmalı."
                ),
            },
            "2": {
                "baslik": "Satış Pitch Önerisi — Finans Dışı Çalışanlar",
                "detay": (
                    "Önerilen açılış cümlesi: 'Bir de aklınızda bulunsun — bu 3 "
                    "programın dışında, tüm banka genelinde finans dışı çalışanlarınız "
                    "için çok uygun maliyetli, 1 günlük bir temel finans okuryazarlığı "
                    "eğitimimiz var. İsterseniz aynı Swissotel takvimine ekleyebiliriz.'\n\n"
                    "Dip not: Bu eğitim ucuz ve düşük riskli olduğu için 'evet' almak "
                    "kolay olabilir — bütçe onayı gerektirmeyecek kadar küçük bir kalem "
                    "olarak sunulabilir."
                ),
            },
            "3": {
                "baslik": "Satış Pitch Önerisi — Satış ve Pazarlama Ekibi Bundle",
                "detay": (
                    "Önerilen açılış cümlesi: 'Bankanızın satış ve pazarlama "
                    "ekibinin TAMAMINI bu eğitimden geçirmenizi öneriyoruz — tek "
                    "kişilik değil, ekip çapında bir yatırım olarak düşünün. Bu "
                    "şekilde eğitim gerçek bir davranış değişikliğine dönüşüyor.'\n\n"
                    "Dip not: Toplu katılım (10+ kişi) için kurumsal indirim "
                    "önerilebilir — fiyat esnekliği İFE ile teyit edilmeli, TBB'ye "
                    "somut bir % rakamı verilmeden önce onay alınmalı."
                ),
            },
            "4": {
                "baslik": "Fiyat / Bundle Pazarlık Alanı (İç Not)",
                "detay": (
                    "Ana 3 program + bu 2 ek eğitim birlikte alınırsa toplu bir "
                    "paket indirimi önerilebilir mi? Bu konuda İFE finans ekibiyle "
                    "netleştirilmesi gereken bir esneklik payı var — toplantıda "
                    "rakam verilmeden önce onay alınmalı.\n\n"
                    "Not (TBB Broşür ile çelişmesin diye): TBB'ye gösterilen broşürde "
                    "bu bundle artık 'Müşteri Güveni ve Ticari Yetkinlik' stratejik "
                    "sütunu altında, etik/güven odaklı bir çerçevede sunuluyor. "
                    "Klasik satış teknikleri (ikna, itiraz yönetimi, kapanış "
                    "stratejileri) fikri sadece burada, iç ekip pazarlık notu olarak "
                    "kalmalı — broşürde bu dille bahsedilmemeli."
                ),
            },
            "5": {
                "baslik": "Zamanlama ve Sunum Sırası (İç Not)",
                "detay": (
                    "1 saatlik toplantının 55. dakikasında, kapanış sorusundan "
                    "hemen önce 30 saniyelik bir 'bir de şunu ekleyelim' anı olarak "
                    "sunulmalı. Detaya girmeden, broşürü bırakıp 'bunu da "
                    "değerlendirin' demek yeterli — toplantının odağını ana 3 "
                    "programdan kaydırmamak kritik."
                ),
            },
        },
    },
}

# Ana menüde bölümlerin görünme sırası (feedback ve kapatma ayrı ele alınır)
SECTION_ORDER = [
    "tbb_toplanti_pitch",
    "tbb_gundem",
    "sektorel_handikaplar",
    "stratejiler",
    "modeller",
    "cross_sell",
    "tbb_onerilen_egitimler",
    "flash_sale_pitch_strategy",
]

# ==============================================================================
# TBB DELIVERY — Resmi Broşür (Dış Sunum: TBB Sunum/Broşür görünümü)
# ------------------------------------------------------------------------------
# Anlatı çerçevesi: "TBB'nin sektörel eğitim kapasitesini uzmanlık programlarıyla
# güçlendiren stratejik iş birliği." İFE'nin TBB'ye eğitim sattığı bir katalog
# değil — dört stratejik sütun (pillars) altında, TBB'nin mevcut vizyonunu
# somut yetkinliğe çeviren bir uygulama ortaklığı olarak kurgulanmıştır.
#
# Her program bir "pillar_id" ile bir sütuna bağlanır; bir sütun birden fazla
# program içerebilir (bkz. "musteri_guveni"). Satış/pazarlama taktik dili
# (ikna, itiraz yönetimi, kapanış stratejileri vb.) burada YER ALMAZ — o dil
# yalnızca SECTIONS içindeki "flash_sale_pitch_strategy" (İç Ekip Görünümü)
# altında kalır.
# ==============================================================================
BROCHURE = {
    "event_info": {
        "title": "TBB – İFE Stratejik Eğitim İş Birliği",
        "opening_statement": (
            "İFE, TBB ile uzun vadeli bir paydaşlık kurmayı; ihtiyaç duyulan "
            "alanlarda somut çözümler ve sürdürülebilir eğitim kapasitesi "
            "desteğiyle bu birlikteliği kalıcı kılmayı hedefler."
        ),
        "ifrs_partnership": (
            "İFE İstanbul Finans Enstitüsü, IFRS Foundation tarafından Nisan 2026 "
            "itibarıyla \"IFRS Sürdürülebilirlik Eğitiminde Resmi Lisanslı Ortak\" "
            "olarak atanmıştır — ISSB S1/S2 standartları kapsamında IFRS Foundation "
            "kaynaklı içerikle eğitim, sertifikasyon ve yayın yetkisine sahip "
            "kurumlardan biridir."
        ),
        "positioning": (
            "IFRS Foundation'ın Türkiye'deki resmi lisanslı eğitim ortağı İFE "
            "İstanbul Finans Enstitüsü, TBB'nin sektörel eğitim ve dağıtım "
            "kapasitesini; düzenleyici uyum, sürdürülebilirlik, uluslararası "
            "sertifikasyon ve müşteri odaklı bankacılık alanlarında uzmanlık "
            "içeriği ve uygulama desteğiyle tamamlayan bir ortaktır."
        ),
        "credentials_line": (
            "169 IFRS Yargı Bölgesi · 37+ ISSB Benimseyen Ülke · Türkiye'de 300+ TSRS "
            "Zorunlu Şirket · IFRS Sustainability Alliance Üyesi (400+ Küresel Kuruluş) · "
            "EBTN Üyesi · 15+ Yıl Deneyim · 500+ Kurumsal Müşteri"
        ),
    },
    "accreditations": [
        {
            "name": "CFA",
            "full_name": "Chartered Financial Analyst",
            "tag": "Level I · II · III Hazırlık · 190+ Ülkede Geçerli",
        },
        {
            "name": "CAMS",
            "full_name": "Certified Anti-Money Laundering Specialist",
            "tag": "Dünyanın 1 Numaralı AML Sertifikası · MASAK Uyumlu",
        },
        {
            "name": "ICA",
            "full_name": "International Compliance Association Diploma",
            "tag": "150+ Ülkede Tanınan Diploma",
        },
        {
            "name": "GCI (CCM)",
            "full_name": "Global Compliance Institute — Certified Compliance Manager",
            "tag": "Türkçe Sınav Seçeneği Mevcut",
        },
        {
            "name": "IFRS Sustainability",
            "full_name": "IFRS Sustainability Alliance Üyeliği",
            "tag": "ISSB S1 / S2 Standartlarında Lisanslı İçerik ve Sertifikasyon Yetkisi",
        },
    ],
    "bridge_intro": (
        "TBB, yüz yüze eğitim, uzaktan öğrenme, mikro-öğrenme ve Finans ve "
        "Bankacılık Eğitim Portalı ile üye bankalara geniş kapsamlı bir eğitim "
        "altyapısı sunmaktadır. İFE bu altyapıyı yeni bir katalogla çoğaltmak "
        "yerine, dört uzmanlık alanında derinlemesine içerik ve uygulama "
        "desteğiyle tamamlar:"
    ),
    "pillars": [
        {
            "id": "duzenleyici_uyum",
            "label": "1",
            "name": "Düzenleyici Uyum ve Risk Kapasitesi",
            "rationale": (
                "Mevzuat bilgisinin günlük bankacılık işlemlerine, müşteri "
                "kabulüne, şüpheli işlem değerlendirmesine ve kurum içi kontrol "
                "davranışına aktarılması."
            ),
        },
        {
            "id": "surdurulebilir_bankacilik",
            "label": "2",
            "name": "Sürdürülebilir Bankacılık ve Raporlama",
            "rationale": (
                "TBB'nin sürdürülebilir ve sorumlu bankacılık vizyonunun "
                "uygulama ve raporlama yetkinliğine dönüştürülmesi."
            ),
        },
        {
            "id": "uluslararasi_yetkinlik",
            "label": "3",
            "name": "Uluslararası Mesleki Yetkinlik",
            "rationale": (
                "Üye bankaların uluslararası AML standartlarıyla uyumlu uzman "
                "insan kaynağı ve sertifikasyon kapasitesinin geliştirilmesi."
            ),
        },
        {
            "id": "musteri_guveni",
            "label": "4",
            "name": "Müşteri Güveni ve Ticari Yetkinlik",
            "rationale": (
                "Klasik satış teknikleri yerine; etik, şeffaf, müşteri "
                "ihtiyacına ve uzun vadeli güvene dayalı bankacılık "
                "yaklaşımının güçlendirilmesi."
            ),
        },
    ],
    "programs": [
        {
            "id": "masak",
            "pillar_id": "duzenleyici_uyum",
            "title": "MASAK Uyum Görevlisi Yetkilendirme Sınavı Hazırlık Eğitimi",
            "tagline": (
                "Mevzuat bilgisini şube ve merkez ekiplerinin günlük karar "
                "davranışına dönüştüren kapsamlı hazırlık programı"
            ),
            "summary": (
                "5549 sayılı Kanun, Terörizmin Finansmanı yükümlülükleri ve uyum "
                "programı mevzuatı çerçevesinde MASAK Uyum Görevlisi "
                "Yetkilendirme Sınavı'na yönelik kapsamlı hazırlık programı. "
                "Teorik anlatım, yoğun soru çözüm pratiği ve vaka çalışmalarıyla "
                "desteklenir."
            ),
            "outcomes": [
                "Şüpheli işlem değerlendirmesinde özgüvenli karar verme",
                "Müşteri kabul süreçlerinde risk bazlı yaklaşım uygulama",
                "Yetkilendirme sınavına somut ve ölçülebilir hazırlık",
            ],
            "modules": [
                "Modül 1 — Hukuki Çerçeve ve AML/CFT Temel Kavramlar",
                "MASAK ve Uyum Mevzuatı, Suç Gelirlerinin Aklanması (5549 Sayılı Kanun)",
                "Terörizmin Finansmanı ve Malvarlığının Dondurulması",
                "Kitle İmha Silahlarının Finansmanı",
                "Temel Hukuki Kavramlar ve Sınav Soru Çözümü",
                "Modül 2 — Uyum Yönetimi, KYC ve Uygulama Pratikleri",
                "Uyum Programı ve Risk Bazlı Yaklaşım",
                "Müşterini Tanı (KYC) ve Müşteri Risk Değerlendirmesi",
                "Şüpheli İşlem Bildirimi (ŞİB)",
                "Sınav Formatına Uygun Soru Çözüm Teknikleri, Deneme Testleri ve Vaka Analizleri",
            ],
            "audience": [
                "Uyum Görevlisi Adayı",
                "AML / CFT Uyum Uzmanı",
                "İç Denetim ve İç Kontrol Uzmanı",
                "Finansal Suçlarla Mücadele Uzmanı",
                "Avukatlar ve Mali Müşavirler",
                "Regülasyon & Uyumluluk Danışmanı",
            ],
            "format": "Sınıf İçi (Swissotel The Bosphorus) + Canlı Sanal Sınıf (Zoom)",
            "duration": "2 Gün (Toplam 12 Saat)",
            "authority": "SPL (Sermaye Piyasası Lisanslama Sicil ve Eğitim Kuruluşu) sınav formatına tam uyumlu içerik.",
            "source_url": "https://www.ife.com.tr/tr/courses/masak-egitimi-uyum-gorevlisi-yetkilendirme-sinavi-hazirlik-egitimi",
            "instructor": {
                "name": "Ali Ekber Polat",
                "title": "Av., LL.M.",
                "linkedin": "https://tr.linkedin.com/in/ali-ekber-polat-b55724316",
                "bio": (
                    "Marmara Üniversitesi Hukuk Fakültesi 2003 mezunu. 2004 yılında Polat Hukuk "
                    "Bürosu'nu kurmuştur. Okan Üniversitesi'nde hukuk dersleri vermektedir. İFE "
                    "bünyesinde finans profesyonellerine yönelik hukuki uyum eğitimleri "
                    "vermektedir."
                ),
                "expertise": [
                    "AML/MASAK — Suç Gelirlerinin Aklanmasının Önlenmesi",
                    "KVKK — Kişisel Verilerin Korunması Hukuku",
                ],
            },
            "level": "Başlangıç",
            "image": "https://amazing-prosperity-08faceb395.media.strapiapp.com/large_masak_yetkilendirme_resim_web_d9aabf5730.jpeg",
            "price_options": [
                {"label": "Canlı Sanal Sınıf", "price": "₺29.800", "duration": "2 Gün"},
                {"label": "Kendi Hızında (Online)", "price": "₺8.900", "duration": "Kayıt İzleme"},
            ],
        },
        {
            "id": "surdurulebilirlik",
            "pillar_id": "surdurulebilir_bankacilik",
            "title": "Sürdürülebilirlik Raporlama ve İklim Riskleri",
            "tagline": (
                "TBB'nin sürdürülebilir bankacılık vizyonunu uygulanabilir "
                "raporlama yetkinliğine dönüştüren program"
            ),
            "summary": (
                "Sürdürülebilirlik düzenlemeleri, ESG raporlama standartları (GRI, TCFD), "
                "karbon piyasaları ve iklim risk analizi konularında uzmanlık kazandırılır. "
                "Kurum içi ESG entegrasyonu ve uyum süreçleri programın merkezinde yer alır."
            ),
            "outcomes": [
                "TSRS çerçevesine ve ESG raporlama standartlarına hakimiyet",
                "Kurum içi ESG entegrasyonunda uygulama kapasitesi",
                "İklim risk senaryolarını kredi ve yatırım kararlarına yansıtabilme",
            ],
            "modules": [
                "Sürdürülebilirlik Düzenlemeleri ve TSRS Çerçevesi",
                "ESG Raporlama Standartları (GRI, TCFD)",
                "Karbon Piyasaları ve Emisyon Yönetimi",
                "İklim Risk Analizi ve Senaryo Çalışmaları",
                "Kurum İçi ESG Entegrasyonu ve Uyum Süreçleri",
            ],
            "audience": [
                "Sürdürülebilirlik ve ESG Birimi Çalışanları",
                "Kredi ve Risk Yönetimi Ekipleri",
                "Finansal Raporlama ve Muhasebe Uzmanları",
                "Yatırımcı İlişkileri Profesyonelleri",
                "İç Denetim ve Uyum Ekipleri",
            ],
            "format": "Sınıf İçi (Swissotel The Bosphorus) + Canlı Sanal Sınıf Seçeneği",
            "duration": "Önerilen Süre: 2 Gün",
            "authority": "IFRS Sustainability Alliance Türkiye üyeliği kapsamında hazırlanmıştır.",
            "source_url": "https://www.ife.com.tr/tr/courses/surdurulebilirlik-raporlama-ve-iklim-riskleri",
            "instructor": {
                "name": "Hasan Sarıçiçek",
                "title": "Dr.",
                "linkedin": "https://ife.com.tr/tr/instructors/hasan-saricicek",
                "bio": (
                    "İklim teknolojileri ve enerji dönüşümü yatırımları alanında 20 yılı aşkın "
                    "deneyim sahibi. Türkiye, Avrupa ve ABD'de sermaye tahsisi, M&A ve "
                    "yapılandırılmış finansman süreçlerinde aktif rol almaktadır. Hâlen Naturel "
                    "Holding bünyesinde İklim Teknolojileri ve E-Mobilite yatırımlarından "
                    "sorumlu direktör."
                ),
                "expertise": ["Sürdürülebilir Finans ve ESG", "İklim Teknolojileri ve E-Mobilite"],
            },
            "level": "Orta",
            "image": "https://amazing-prosperity-08faceb395.media.strapiapp.com/large_Chat_GPT_Image_Nov_6_2025_01_32_18_AM_751819e6e4.png",
            "price_options": [],
            "price_note": "Teklif Üzerine",
        },
        {
            "id": "cams",
            "pillar_id": "uluslararasi_yetkinlik",
            "title": "CAMS — Certified Anti-Money Laundering Specialist",
            "tagline": (
                "Üye bankaların uluslararası standartlarda uzman insan kaynağı "
                "geliştirmesini sağlayan küresel sertifikasyon"
            ),
            "summary": (
                "ACAMS tarafından verilen, kara para aklama ve terörün finansmanıyla "
                "mücadele alanındaki en prestijli uluslararası sertifika. Program, "
                "üye bankaların uluslararası AML standartlarıyla uyumlu uzman "
                "kapasitesini ve sertifikasyon oranını yükseltmeyi hedefler."
            ),
            "outcomes": [
                "100+ ülkede geçerli uluslararası sertifikasyon",
                "FATF, Basel ve Wolfsberg standartlarına hakimiyet",
                "2 tam mock sınav simülasyonuyla sınava somut hazırlık",
            ],
            "modules": [
                "Modül 0 — Sınav Genel Bakış ve Strateji",
                "Modül 1A — Domain I-A: ML/TF Tanımları ve Aşamaları",
                "Modül 1B — Domain I-B: Modern Aklama Yöntemleri ve Risk Kategorileri",
                "Modül 2A — FATF Sistemi ve 40 Tavsiye",
                "Modül 2B — Diğer Uluslararası Aktörler (Basel, Wolfsberg)",
                "Modül 2C — Bölgesel Mevzuatlar",
                "Modül 3A — AML Programının Beş Sütunu ve Risk Değerlendirmesi",
                "Modül 3B — CDD, SDD, EDD ve KYC Mimarisi",
                "Modül 3C — Raporlama, Monitoring ve Sanctions (STR/SAR)",
                "Modül 4A — İç Soruşturma Süreci",
                "Modül 4B — Kolluk ve Adli Süreçlerle Etkileşim",
            ],
            "audience": [
                "Banka Compliance Analisti → AML Officer → MLRO → Chief Compliance Officer (CCO)",
                "KYC/CDD Uzmanı → Senior CDD Analyst → FIU Lead → Head of Financial Crime",
                "Sanctions Screening Uzmanı → Sanctions Manager → Head of Sanctions",
                "Kripto Borsası Compliance Lead → Travel Rule & Sanctions Lead → VASP MLRO",
                "Denetim ve Danışmanlık Uzmanı → Manager → Director of Financial Crime Advisory",
                "Hukuk Bürosu AML Avukatı → Senior Compliance Counsel → Partner",
            ],
            "format": "Sınıf İçi (Swissotel) veya Canlı Sanal Sınıf — 2 Tam Gün (09:30–16:30), 12-15 Kişilik Sınıf, 2 Mock Sınav Simülasyonu",
            "duration": "Sınav: 3,5 Saat / 120 Soru · Geçme Barajı %62,5 (Pearson VUE Test Merkezleri)",
            "authority": "ACAMS Yetkili Hazırlık Merkezi — sertifika 3 yıl geçerli, yenileme için 60 saat CE puanı gerekir.",
            "source_url": "https://www.ife.com.tr/tr/courses/cams-sertifikali-aml-uzmani-sinav-hazirlik",
            "instructor": {
                "name": "Alpaslan Çakır",
                "title": "CAMS",
                "linkedin": "https://www.linkedin.com/in/alpaslan-cakir-7b0b1098/",
                "bio": (
                    "Türkiye'nin önde gelen AML ve Compliance uzmanlarından biri. Denizbank A.Ş. "
                    "bünyesinde AML & CFT Uyum Bölüm Müdürü. Türkiye Bankalar Birliği Bankacılar "
                    "Dergisi'nde aklama ve finansal suçlar üzerine makalelerin yazarı. CAMS "
                    "sertifikasına sahiptir."
                ),
                "expertise": [
                    "AML — Suç Gelirlerinin Aklanmasının Önlenmesi",
                    "CFT — Terörizmin Finansmanı ile Mücadele",
                ],
            },
            "level": "İleri",
            "image": "https://amazing-prosperity-08faceb395.media.strapiapp.com/large_ACAMS_Banner_full_good_aedb330910.jpg",
            "price_options": [
                {"label": "Sınıf İçi (Swissotel)", "price": "₺43.800", "duration": "2 Gün"},
                {"label": "Canlı Sanal Sınıf", "price": "₺29.800", "duration": "2 Gün"},
            ],
        },
        {
            "id": "finans-disi",
            "pillar_id": "musteri_guveni",
            "title": "Finans Dışı Yöneticiler için Finansal Okuryazarlık",
            "tagline": "Finans dilini bilmeyen yöneticiler için temel okuryazarlık",
            "summary": (
                "Finansçı olmayan yöneticilerin şirketin finansal yapısını doğru "
                "okuyabilmesini ve günlük iş kararlarını finansal bakış açısıyla "
                "değerlendirebilmesini sağlar. Finans jargonundan arındırılmış, "
                "iş hayatından örneklerle desteklenen bir anlatım kullanılır."
            ),
            "outcomes": [
                "Finansal tabloları doğru okuyup yorumlayabilme",
                "Günlük iş kararlarını finansal bakış açısıyla değerlendirme",
                "Finans ekipleriyle ortak bir dil kurma",
            ],
            "modules": [
                "Finansın İş Dünyasındaki Rolü",
                "Temel Finansal Kavramlar (Gelir, Gider, Kâr, Nakit, Maliyet)",
                "Finansal Tabloları Tanıyalım (Gelir Tablosu, Bilanço, Nakit Akış)",
                "Finansal Göstergeler ve Yorumlama",
                "Finansal Bakış Açısıyla Karar Alma",
            ],
            "audience": [
                "Satış ve Pazarlama Yöneticileri",
                "Operasyon ve Proje Yöneticileri",
                "İnsan Kaynakları Yöneticileri",
                "Finansla Birlikte Çalışan Tüm İş Birimi Yöneticileri",
            ],
            "format": "Sınıf İçi (Swissotel) / Canlı Sanal Sınıf / Kendi Hızında Online",
            "duration": "1 Gün",
            "authority": None,
            "source_url": "https://www.ife.com.tr/tr/courses/finans-disi-calisanlar-icin-temel-finans",
            "instructor": None,
            "level": "Başlangıç",
            "image": "https://amazing-prosperity-08faceb395.media.strapiapp.com/large_web_resim_238f9ca8ff.jpg",
            "price_options": [
                {"label": "Sınıf İçi (Swissotel)", "price": "₺29.800", "duration": "1 Gün"},
                {"label": "Canlı Sanal Sınıf", "price": "₺18.900", "duration": "1 Gün"},
                {"label": "Kendi Hızında (Online)", "price": "₺6.900", "duration": "Kayıt İzleme"},
            ],
        },
        {
            "id": "satis-pazarlama-finans",
            "pillar_id": "musteri_guveni",
            "title": "Müşteri İlişkileri ve Satış Yöneticileri için Finansal Sorumluluk Bilinci",
            "tagline": "Satışın sadece ciro değil, nakit, risk ve sorumluluk yarattığı bilinci",
            "summary": (
                "Satış ve pazarlama yöneticilerinin finansal tabloları anlamasını, "
                "satış süreçlerinin mali sonuçlarını değerlendirmesini ve finansal "
                "riskleri doğru yönetmesini sağlar. Belge düzeni, teslimin ispatı, "
                "ödeme araçları ve tahsilat riskleri gibi pratik konuları da kapsar."
            ),
            "outcomes": [
                "Satış süreçlerinin mali sonuçlarını değerlendirebilme",
                "Belge düzeni ve teslim ispatı konusunda hukuki farkındalık",
                "Tahsilat ve ödeme risklerini doğru yönetme",
            ],
            "modules": [
                "Satış ve Finans Arasındaki İlişki (Ciro–Kâr–Nakit Farkı)",
                "Temel Finansal Tablolar — Satış Perspektifiyle",
                "Satışta Belge Düzeni ve Teslimin İspatı",
                "Mali Sorumluluklar ve Riskler (Vergi, KDV, Tahsilat)",
                "Ödeme Araçları ve Tahsilat Yönetimi",
            ],
            "audience": [
                "Satış Yöneticileri",
                "Pazarlama Yöneticileri",
                "İş Geliştirme Yöneticileri",
                "Satışla Doğrudan Temas Eden Tüm Yöneticiler",
                "Ön Muhasebe Çalışanları",
            ],
            "format": "Sınıf İçi (Swissotel) / Canlı Sanal Sınıf",
            "duration": "1 Gün",
            "authority": None,
            "source_url": "https://www.ife.com.tr/tr/courses/satis-ve-pazarlama-yoneticileri-icin-finans",
            "instructor": None,
            "level": "Başlangıç",
            "image": "https://amazing-prosperity-08faceb395.media.strapiapp.com/large_satis_icin_temel_finans_web_rsim_a63c771bf4.jpeg",
            "price_options": [
                {"label": "Sınıf İçi (Swissotel)", "price": "₺23.800", "duration": "1 Gün"},
                {"label": "Canlı Sanal Sınıf", "price": "₺18.900", "duration": "1 Gün"},
            ],
        },
    ],
    "bespoke": {
        "pillar_id": "musteri_guveni",
        "status_label": "PLANLANAN",
        "title": "Müşteri Güveni ve Etik Bankacılık İletişimi",
        "note": (
            "Bu program şu anda İFE kataloğunda yer almamaktadır. TBB'nin talebi "
            "doğrultusunda İFE tarafından özel (bespoke) olarak geliştirilebilir. "
            "Müşteri ihtiyaç analizine dayalı danışmanlık yaklaşımı, şeffaf iletişim "
            "ve uzun vadeli güven inşasını içeren, bankacılık sektörüne özel bir "
            "müfredat önerilir — mevcut bir kurs değil, teklife bağlı bir "
            "geliştirmedir."
        ),
    },
    "closing": {
        "title": "Önerilen Takvim ve Yer",
        "text": (
            "Ekim–Kasım 2026 dönemi ve Swissotel The Bosphorus, İFE'nin hâlihazırda "
            "düzenli olarak organize ettiği ve yeterli katılımcı sayısının "
            "sağlanması durumunda hızla devreye alabileceği bir takvim ve mekan "
            "önerisidir. Bu dört program, TBB'nin mevcut eğitim takvimine entegre "
            "edilebilecek modüler bir iş birliği çerçevesinde kısa sürede hayata "
            "geçirilebilir; kesin tarih ve uygulama detayları TBB Eğitim Merkezi "
            "ile birlikte planlanır."
        ),
    },
}

# ==============================================================================
# LOGO (TBB Sunum/Broşür görünümünde kullanılır)
# ==============================================================================
IFE_LOGO_WHITE = "https://ife.com.tr/_next/image?url=%2Fife-logo-white.webp&w=384&q=75"
IFE_LOGO_COLOR = "https://ife.com.tr/_next/image?url=%2Fife-full-logo.png&w=750&q=75"
IFRS_LOGO = "https://ife.com.tr/_next/image?url=%2Fifrs.png&w=384&q=75"
TBB_LOGO = "https://www.tbb.org.tr/themes/custom/tbb/logo.svg"
