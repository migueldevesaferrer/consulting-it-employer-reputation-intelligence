from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "output"
FIGURES_DIR = OUTPUT_DIR / "figures"


def ensure_directories() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    FIGURES_DIR.mkdir(exist_ok=True)


def create_rating_chart(path: Path) -> None:
    companies = ["Accenture", "Capgemini", "Deloitte", "Cognizant", "Infosys"]
    ratings = [4.1, 4.0, 4.2, 3.9, 3.8]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(companies, ratings, color=["#163E6C", "#2D7D8D", "#F0B429", "#7E6FDD", "#C75D5D"])
    ax.set_ylim(0, 5)
    ax.set_title("Rating medio por empresa", fontsize=14, weight="bold")
    ax.set_ylabel("Puntuación media")
    ax.grid(axis="y", linestyle="--", alpha=0.2)

    for bar, value in zip(bars, ratings):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.05, f"{value:.1f}", ha="center", va="bottom")

    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def create_topic_chart(path: Path) -> None:
    topics = ["Trabajo / carga", "Salario", "Formación", "Liderazgo", "Balance vida-trabajo"]
    balance = [6, 2, 8, -3, -5]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(topics, balance, color=["#2E8B57" if value >= 0 else "#C94F4F" for value in balance])
    ax.axvline(0, color="black", linewidth=1)
    ax.set_title("Balance neto por dimensión", fontsize=14, weight="bold")
    ax.set_xlabel("Pros - Cons (%)")
    ax.set_xlim(-10, 12)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def add_title_slide(prs: Presentation, title: str, subtitle: str) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle


def add_summary_slide(prs: Presentation, rating_chart: Path, narrative: Iterable[str]) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Resumen ejecutivo"

    text_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(3.5), Inches(3.2))
    tf = text_box.text_frame
    tf.word_wrap = True
    for idx, line in enumerate(narrative):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = line
        p.level = 0
        p.bullet = True
        p.font.size = Pt(18)

    slide.shapes.add_picture(str(rating_chart), Inches(4.2), Inches(1.3), Inches(7.5), Inches(4.5))


def add_topics_slide(prs: Presentation, topic_chart: Path) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "Fortalezas y debilidades comparativas"

    box = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(3.4), Inches(4.7))
    tf = box.text_frame
    tf.word_wrap = True

    for line in [
        "Fortalezas:",
        "• Desarrollo profesional y aprendizaje.",
        "• Marca y prestigio de la empresa.",
        "• Ambición y proyectos internacionales.",
        "",
        "Debilidades:",
        "• Carga de trabajo y presión.",
        "• Riesgos de burocracia y procesos.",
        "• Percepción de liderazgo y balance vida-trabajo."
    ]:
        p = tf.paragraphs[0] if line == "Fortalezas:" else tf.add_paragraph()
        p.text = line
        p.level = 0
        if line.startswith("•") or line.startswith("Debilidades:"):
            p.bullet = True
        p.font.size = Pt(18)

    slide.shapes.add_picture(str(topic_chart), Inches(4.3), Inches(1.4), Inches(7.8), Inches(4.2))


def add_recommendations_slide(prs: Presentation) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "Recomendaciones para RRHH"

    box = slide.shapes.add_textbox(Inches(0.7), Inches(1.5), Inches(10.5), Inches(4.5))
    tf = box.text_frame
    tf.word_wrap = True

    suggestions = [
        "1. Mejorar la experiencia de trabajo y el equilibrio vida-trabajo.",
        "2. Reducir la burocracia y acelerar decisiones de promoción.",
        "3. Potenciar liderazgo más cercano y comunicación interna.",
        "4. Diseñar estrategias de retención para perfiles clave y empleados actuales.",
        "5. Comunicar mejor los beneficios del crecimiento profesional y la marca empleadora."
    ]

    for idx, text in enumerate(suggestions):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = text
        p.level = 0
        p.bullet = True
        p.font.size = Pt(22)


def build_default_presentation(output_path: str | Path = ROOT / "output" / "Accenture_employer_reputation.pptx") -> Path:
    ensure_directories()

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rating_path = FIGURES_DIR / "rating_mean.png"
    topic_path = FIGURES_DIR / "topic_balance.png"

    create_rating_chart(rating_path)
    create_topic_chart(topic_path)

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    add_title_slide(prs, "Accenture: reputación empleadora y comparativa con peers", "Caso práctico de employer reputation intelligence")
    add_summary_slide(
        prs,
        rating_chart=rating_path,
        narrative=[
            "Accenture combina prestigio de marca y desarrollo profesional como fortalezas clave.",
            "Los peores indicadores aparecen en carga de trabajo, sentido de liderazgo y balance personal.",
            "Los empleados actuales valoran la marca, mientras que los antiguos destacan factores de presión y avance profesional."
        ]
    )
    add_topics_slide(prs, topic_chart=topic_path)
    add_recommendations_slide(prs)

    prs.save(output_path)
    return output_path


if __name__ == "__main__":
    out = build_default_presentation()
    print(f"Presentation created at: {out}")
