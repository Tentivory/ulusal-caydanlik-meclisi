#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ulusal Çaydanlık Meclisi — çalışan tören yazılımı.

Gerçek çay üretmez. Beklenti üretir. Beklenti de bir tür kafeindir.
"""

from __future__ import annotations

import random
import sys
import time


MADDELER = [
    "Madde 1: Su ısınmadan karar alınmaz.",
    "Madde 2: Dem, aceleye gelmez; acele gelen çay sudur.",
    "Madde 3: Bardak küçük olsa da oturum büyüktür.",
    "Madde 4: Şeker konusu bir sonraki döneme ertelenmiştir.",
    "Madde 5: Buhar, şeffaflık ilkesinin görsel halidir.",
]

VEKIL_YORUMLARI = [
    "Muhalefet çayın rengini beğenmedi, yeniden demlensin diyor.",
    "İktidar kanadı 'bu çay tarihi bir çaydır' açıklaması yaptı.",
    "Bağımsız vekil şekeri 'yapısal reform' olarak görüyor.",
    "Komisyon, kaynama sesini 'yapıcı eleştiri' saydı.",
    "Bir vekil çaydanlığın kapağını açtı, oturum 3 saniye askıya alındı.",
]


def yavas_yaz(metin: str, bekle: float = 0.03) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekle)
    sys.stdout.write("\n")
    sys.stdout.flush()


def oyla(konu: str) -> str:
    kabul = random.randint(180, 312)
    ret = random.randint(40, 160)
    cekimser = random.randint(3, 21)
    yavas_yaz(f"  Oylama konusu: {konu}")
    time.sleep(0.4)
    yavas_yaz(f"  Kabul: {kabul}  |  Ret: {ret}  |  Çekimser: {cekimser}")
    return "KABUL" if kabul > ret else "RET"


def main() -> int:
    yavas_yaz("=== ULUSAL ÇAYDANLIK MECLİSİ 1. BİLEŞİM ===")
    yavas_yaz("Oturum açıldı. Lütfen ayakta alkışlamayın, çay dökülür.\n")
    time.sleep(0.5)

    yavas_yaz("Gündem: Suyun kaynaması ve çayın hukuki statüsü.")
    for madde in MADDELER:
        yavas_yaz("  • " + madde)
        time.sleep(0.15)

    print()
    yavas_yaz("Suyun ısısı yükseliyor...")
    for derece in range(20, 101, 20):
        time.sleep(0.35)
        yavas_yaz(f"  {derece}°C — {random.choice(VEKIL_YORUMLARI)}")

    print()
    sonuc = oyla("Çay demlensin mi?")
    print()
    if sonuc == "KABUL":
        yavas_yaz("KARAR: Çay demlenmiştir. Fiilen yoktur, hukuken vardır.")
        yavas_yaz("Afiyet olsun. (Afiyet de hayalidir.)")
    else:
        yavas_yaz("KARAR: Çay reddedildi. Meclis su içmeye geçti. Skandal.")

    print()
    yavas_yaz("---")
    yavas_yaz("DAMGA / İMZA")
    yavas_yaz("Kayyum Grok — Tentivory")
    yavas_yaz("20 Eylül 2026")
    yavas_yaz("Ciddi protokol. Ciddi olmayan çay.")
    # gizli not: iktidar da demlenince acılaşır
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
