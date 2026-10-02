from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.presentation.pptx_export import build_default_presentation


if __name__ == "__main__":
    output = ROOT / "output" / "Accenture_employer_reputation.pptx"
    result = build_default_presentation(output)
    print(f"PowerPoint generado correctamente en: {result}")
