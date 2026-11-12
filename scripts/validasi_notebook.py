"""Validasi format dan sintaks sel kode notebook tanpa menjalankan sel."""
from pathlib import Path
import ast
import nbformat

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "notebooks").glob("*.ipynb"))
assert files, "Folder notebooks kosong"
for file in files:
    nb = nbformat.read(file, as_version=4)
    nbformat.validate(nb)
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == "code":
            try:
                ast.parse(cell.source)
            except SyntaxError as exc:
                raise SyntaxError(f"{file.name} sel {idx}: {exc}") from exc
    print("OK", file.name)
print(f"{len(files)} notebook valid")
