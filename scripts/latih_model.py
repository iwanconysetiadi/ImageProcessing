"""CLI: python scripts/latih_model.py --kasus tablet|warna|digit"""
from __future__ import annotations
import argparse
import json
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from pengolahan_citra_id.datasets import tablet_sintetis, kolorimetri_sintetis
from pengolahan_citra_id.features import fitur_tablet, fitur_kolorimetri
from pengolahan_citra_id.evaluation import split_berdasar_batch, metrik_klasifikasi


def jalankan(kasus: str):
    if kasus == "tablet":
        images, y, batch = tablet_sintetis()
        X = np.array([fitur_tablet(im) for im in images])
        train, test = split_berdasar_batch(y, batch)
    elif kasus == "warna":
        images, y, batch = kolorimetri_sintetis()
        X = np.array([fitur_kolorimetri(im, True) for im in images])
        train, test = split_berdasar_batch(y, batch)
    elif kasus == "digit":
        digits = load_digits()
        X, y = digits.data, digits.target
        train, test = train_test_split(np.arange(len(y)), test_size=0.25,
                                       random_state=42, stratify=y)
    else:
        raise ValueError("Kasus harus salah satu: tablet, warna, digit")
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1500, random_state=42))
    model.fit(X[train], y[train])
    pred = model.predict(X[test])
    return {"kasus": kasus, "jumlah_train": len(train), "jumlah_test": len(test),
            "metrik": metrik_klasifikasi(y[test], pred),
            "confusion_matrix": confusion_matrix(y[test], pred).tolist()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kasus", choices=["tablet", "warna", "digit"], required=True)
    args = parser.parse_args()
    print(json.dumps(jalankan(args.kasus), indent=2, ensure_ascii=False))
