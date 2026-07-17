# -*- coding: utf-8 -*-
"""
feedback_store.py
------------------
İFE ekibinin dashboard üzerinden girdiği strateji notlarını / geri
bildirimlerini diske (JSON) kalıcı olarak kaydeder. Böylece dashboard
kapatılıp yeniden açılsa bile notlar kaybolmaz.

Streamlit tarafı bu modülü çağırır; dosya/format detaylarıyla
ilgilenmez. İleride kaynak değişirse (örn. veritabanına taşınırsa)
sadece bu dosya güncellenir, app.py aynı kalabilir.
"""

import json
import os
from datetime import datetime

FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), "feedback_log.json")


def load_feedback() -> list[dict]:
    """Kayıtlı tüm geri bildirimleri döndürür. Dosya yoksa boş liste döner."""
    if not os.path.exists(FEEDBACK_FILE):
        return []
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def add_feedback(isim: str, yorum: str) -> None:
    """Yeni bir geri bildirim ekler ve diske kaydeder."""
    entries = load_feedback()
    entries.append(
        {
            "isim": isim.strip() or "İsimsiz",
            "yorum": yorum.strip(),
            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M"),
        }
    )
    _save(entries)


def clear_feedback() -> None:
    """Tüm geri bildirimleri temizler."""
    _save([])


def _save(entries: list[dict]) -> None:
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
