"""Smoke test: jalankan semua sel Python pada notebook 00–12, tanpa kernel Jupyter.

Tidak menggantikan uji interaktif melalui JupyterLab. Opsional CNN nomor 13
bisa diuji dengan `--cnn` ketika torch tersedia.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import os
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")
import matplotlib.pyplot as plt  # noqa: E402
import nbformat  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]


def main(include_cnn: bool = False):
    files = sorted((ROOT / "notebooks").glob("*.ipynb"))
    if not include_cnn:
        files = [p for p in files if not p.name.startswith("13_")]
    for file in files:
        ns = {"__name__": "__main__"}
        notebook = nbformat.read(file, as_version=4)
        for n, cell in enumerate(notebook.cells):
            if cell.cell_type != "code":
                continue
            try:
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    exec(compile(cell.source, f"{file.name}:cell{n}", "exec"), ns)
            except Exception as exc:
                raise RuntimeError(f"Gagal: {file.name}, sel {n}") from exc
            finally:
                plt.close("all")
        print("PASS", file.name)
    print(f"{len(files)} notebook berhasil dieksekusi (kode Python)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cnn", action="store_true", help="Termasuk notebook CNN opsional jika torch ada")
    args = parser.parse_args()
    main(args.cnn)
