"""Gera dist/app.html a partir de src/src.html, src/data.json e src/assets.json."""
import pathlib
b = pathlib.Path(__file__).parent
s = (b / "src/src.html").read_text()
s = s.replace("__DATA__", (b / "src/data.json").read_text())
s = s.replace("__ASSETS__", (b / "src/assets.json").read_text())
(b / "dist").mkdir(exist_ok=True)
(b / "dist/app.html").write_text(s)
print("dist/app.html gerado")
