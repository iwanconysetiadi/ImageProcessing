"""Pemisahan data, evaluasi, dan percobaan yang reproducible."""
from __future__ import annotations

import numpy as np
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.model_selection import GroupShuffleSplit


def split_berdasar_batch(y, groups, test_size: float = 0.25, seed: int = 42):
    """Indeks train/test tanpa batch bersama untuk menahan data leakage."""
    y, groups = np.asarray(y), np.asarray(groups)
    if len(y) != len(groups):
        raise ValueError("Panjang label dan batch harus sama")
    split = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
    train, test = next(split.split(np.zeros(len(y)), y, groups))
    if set(groups[train]) & set(groups[test]):
        raise AssertionError("Kebocoran batch antara train dan test")
    return train, test


def metrik_klasifikasi(y_true, y_pred):
    """Ringkasan metrik evaluasi (nilai, tidak otomatis dicetak)."""
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
    }
