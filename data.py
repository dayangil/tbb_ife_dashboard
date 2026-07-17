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
}

# Ana menüde bölümlerin görünme sırası (feedback ve kapatma ayrı ele alınır)
SECTION_ORDER = [
    "tbb_gundem",
    "sektorel_handikaplar",
    "stratejiler",
    "modeller",
    "cross_sell",
    "tbb_onerilen_egitimler",
]
