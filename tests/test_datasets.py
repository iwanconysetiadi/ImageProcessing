import numpy as np
import pytest
from pengolahan_citra_id.datasets import tablet_sintetis, kolorimetri_sintetis
from pengolahan_citra_id.features import fitur_tablet, fitur_kolorimetri, FITUR_TABLET, FITUR_WARNA
from pengolahan_citra_id.evaluation import metrik_klasifikasi, split_berdasar_batch


def test_tablet_shape_reproducibility():
    a, y, g = tablet_sintetis(8, 6, seed=8)
    b, y2, g2 = tablet_sintetis(8, 6, seed=8)
    assert a.shape == (48, 96, 96) and a.dtype == np.uint8
    assert set(np.unique(y)) == {0, 1} and len(set(g)) == 8
    assert np.array_equal(a, b) and np.array_equal(y, y2) and np.array_equal(g, g2)


def test_tablet_features_finite():
    images, _, _ = tablet_sintetis(3, 4)
    feats = np.array([fitur_tablet(x) for x in images])
    assert feats.shape == (12, len(FITUR_TABLET))
    assert np.isfinite(feats).all()


def test_kolorimetri_shapes_and_features():
    images, y, batches = kolorimetri_sintetis(4, 6)
    assert images.shape == (24, 64, 96, 3)
    assert set(y) == {0, 1} and len(set(batches)) == 4
    a = fitur_kolorimetri(images[0], False)
    b = fitur_kolorimetri(images[0], True)
    assert a.shape == b.shape == (len(FITUR_WARNA),)
    assert np.isfinite(b).all() and np.isclose(b[-3:].sum(), 1)


def test_no_group_leakage():
    _, y, g = kolorimetri_sintetis(12, 6)
    train, test = split_berdasar_batch(y, g)
    assert not set(g[train]) & set(g[test])
    assert len(train) + len(test) == len(y)


def test_metrics_perfect():
    out = metrik_klasifikasi([0, 1, 0, 1], [0, 1, 0, 1])
    assert out["f1_macro"] == 1.0


def test_validation_errors():
    with pytest.raises(ValueError):
        tablet_sintetis(1, 2)
    with pytest.raises(ValueError):
        fitur_tablet(np.ones((2, 2, 2)))
    with pytest.raises(ValueError):
        fitur_kolorimetri(np.ones((32, 32, 3)))
