import json
from pathlib import Path
from typing import TYPE_CHECKING, TypeAlias, TypedDict
from typing import Annotated as A

import numpy as np
import plotly.graph_objects as go
from babel.messages import pofile
from docutils import nodes
from docutils.parsers.rst import Directive
from plotly.offline import plot

if TYPE_CHECKING:
    from sphinx.application import Sphinx


BASE_DIR = Path(__file__).resolve().parent.parent  # Repository base directory
LOCALES_DIR = BASE_DIR / "locales"  # Locales directory
STATIC_DIR = BASE_DIR / "_static"  # Static directory


class ModuleStats(TypedDict):
    total: int
    translated: int
    fuzzy: int
    untranslated: int
    percentage: float


TranslationStats: TypeAlias = dict[
    A[str, "locale"], dict[A[str, "module"], ModuleStats]
]


class TranslationGraph(Directive):
    # Tells Sphinx that this directive can be used in the document body
    # and has no content
    has_content = False

    # oddly, this is evaluated in the js not python,
    # so we treat customdata like a json object
    HOVER_TEMPLATE = """
    <b>%{customdata.module}</b><br>
    Translated: %{customdata.translated}<br>
    Fuzzy: %{customdata.fuzzy}<br>
    Untranslated: %{customdata.untranslated}<br>
    Total: %{customdata.total}<br>
    Completed: %{customdata.percentage}%
    """

    def run(self):
        data = get_translation_stats()

        # Sort data by locale and module
        data = {
            locale: dict(sorted(loc_stats.items()))
            for locale, loc_stats in sorted(data.items())
        }

        # prepend english, everything set to 100%
        en = {
            module: ModuleStats(
                total=stats["total"],
                translated=stats["total"],
                fuzzy=stats["total"],
                untranslated=0,
                percentage=100,
            )
            for module, stats in next(iter(data.values())).items()
        }
        data = {"en": en} | data

        # Calculate average completion percentage for each locale and sort locales
        locale_completion = {
            locale: np.mean([stats["percentage"] for stats in loc_stats.values()])
            for locale, loc_stats in data.items()
        }
        sorted_locales = sorted(
            locale_completion.keys(),
            key=lambda locale: locale_completion[locale],
            reverse=True,
        )

        # Reorder data based on sorted locales
        data = {locale: data[locale] for locale in sorted_locales}

        # Update locales list after sorting
        locales = list(data.keys())
        modules = list(next(iter(data.values())).keys())

        # Extract data to plot
        values = [
            [stats["percentage"] for stats in loc_stats.values()]
            for loc_stats in data.values()
        ]
        hoverdata = [
            [{"module": module} | stats for module, stats in loc_stats.items()]
            for loc_stats in data.values()
        ]

        # Add text to display percentages directly in the heatmap boxes
        text = [
            [f"{int(stats['percentage'])}%" for stats in loc_stats.values()]
            for loc_stats in data.values()
        ]

        heatmap = go.Heatmap(
            x=modules,
            y=locales,
            z=values,
            text=text,  # Add text to the heatmap
            texttemplate="%{text}",  # Format the text to display directly
            textfont={"size": 15},  # Adjust font size for better readability
            xgap=5,
            ygap=5,
            customdata=np.array(hoverdata),
            hovertemplate=self.HOVER_TEMPLATE,
            name="",  # Set the trace name to an empty string to remove "trace 0" from hoverbox
            colorbar={
                "orientation": "h",
                "y": 0,
                "yanchor": "bottom",
                "yref": "container",
                "title": "Completion %",
                "thickness": 10,
                "tickvals": [12.5, 50, 87.5, 100],  # Midpoints for each category
                "ticktext": [
                    "0-25%",
                    "25-75%",
                    "75-<100%",
                    "100%",
                ],  # Labels for categories
            },
            colorscale=[
                [0.0, "rgb(254, 255, 231)"],  # 0-25%
                [0.25, "rgb(254, 255, 231)"],
                [0.25, "rgb(187, 130, 176)"],  # 25-75%
                [0.75, "rgb(187, 130, 176)"],
                [0.75, "rgb(129, 192, 170)"],  # 75-<100%
                [0.99, "rgb(129, 192, 170)"],
                [1.0, "rgb(78,  112, 100)"],  # 100%
            ],
        )
        # Create figure
        fig = go.Figure(data=heatmap)
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            hoverlabel_bgcolor="var(--bs-body-bg)",
            hoverlabel_font_color="rgba(255, 255, 255, 1)",
            font_color="var(--bs-body-color)",
            margin=dict(l=40, r=40, t=40, b=40),
            xaxis_showgrid=False,
            xaxis_side="top",
            xaxis_tickangle=-45,
            xaxis_tickfont={
                "family": "var(--bs-font-monospace)",
            },
            yaxis_showgrid=False,
            yaxis_title="Locale",
            yaxis_autorange="reversed",
        )
        div = plot(
            fig,
            output_type="div",
            include_plotlyjs=True,
            config={"displayModeBar": False},
        )
        return [nodes.raw("", div, format="html")]


def calculate_translation_percentage(po_path: Path, locale: str) -> ModuleStats:
    """
    Calculate the translation percentage for a given .po file.

    Parameters
    ----------
    po_path : Path
        Path to the .po file.
    locale : str
        Locale code (e.g., 'es', 'fr').

    Returns
    -------
    dict
        A dictionary containing the total number of strings, translated strings,
        fuzzy strings, untranslated strings, and the translation percentage.
    """
    with open(po_path, "r", encoding="utf-8") as f:
        catalog = pofile.read_po(f, locale=locale)

    total = 0
    translated = 0
    fuzzy = 0

    for message in catalog:
        if message.id:
            total += 1
            # Check if the message is fuzzy
            # Fuzzy messages are not considered translated
            if message.fuzzy:
                fuzzy += 1
                break
            # Check if the message is translated
            if message.string:
                translated += 1

    percentage = (translated / total * 100) if total > 0 else 0

    return {
        "total": total,
        "translated": translated,
        "fuzzy": fuzzy,
        "untranslated": total - translated - fuzzy,
        "percentage": round(percentage, 2),
    }


def get_translation_stats() -> TranslationStats:
    # Get all .po files in the locales directory
    po_files = list(LOCALES_DIR.rglob("*.po"))

    # Let's use a dictionary to store the results
    #
    # We will store the info as
    # {
    #    "es": {
    #        "file1": {
    #            "total": 100,
    #            "translated": 50,
    #            "fuzzy": 0,
    #            "untranslated": 50,
    #            "percentage": 50.0
    #        },
    #        ...
    #    },
    #    "fr": {
    #        "file1": {
    #            "total": 100,
    #            "translated": 50,
    #            "fuzzy": 0,
    #            "untranslated": 50,
    #            "percentage": 50.0
    #        },
    #        ...
    # }
    results = {}

    # Calculate translation percentages for each file
    for po_file in po_files:
        # Get the locale from the file path
        locale = po_file.parent.parent.name
        stats = calculate_translation_percentage(po_file, locale)

        # Store the results in the dictionary
        if locale not in results:
            results[locale] = {}

        results[locale][po_file.stem] = stats

    return results


def write_translation_stats(app: "Sphinx", exception: Exception | None) -> None:
    from sphinx.util import logging

    logger = logging.getLogger("_ext.translation_graph")

    if app.builder.name != "html":
        logger.info("Skipping translation stats for non-HTML build")
        return

    stats = get_translation_stats()
    out_path = app.outdir / "_static" / "translation_stats.json"
    with open(out_path, "w") as f:
        json.dump(stats, f, indent=2)

    logger.info("Wrote translation stats to %s", out_path)


def setup(app):
    app.add_directive("translation-graph", TranslationGraph)
    app.connect("build-finished", write_translation_stats)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
