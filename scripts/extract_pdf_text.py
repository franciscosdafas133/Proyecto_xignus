import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except Exception:
    raise SystemExit("pypdf no está instalado. Ejecuta: python -m pip install pypdf")

if len(sys.argv) < 3:
    print("Uso: python extract_pdf_text.py <input-pdf> <output-txt>")
    raise SystemExit(1)

input_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])

if not input_path.exists():
    print(f"Archivo no encontrado: {input_path}")
    raise SystemExit(2)

reader = PdfReader(str(input_path))
text_parts = []
for page in reader.pages:
    try:
        text = page.extract_text()
    except Exception:
        text = None
    if text:
        text_parts.append(text)

full_text = "\n\n".join(text_parts)
output_path.write_text(full_text, encoding="utf-8")
print(f"Texto extraído guardado en: {output_path}")
