import json
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np
import plotly.graph_objects as go
from docutils import nodes
from docutils.parsers.rst import Directive
from plotly.offline import plot

# Note: this import relies on the fact that conf.py puts the repository root on sys.path,
# so this resolves as a namespace package needing any __init__.py.
from scripts.translation.stats import (
    get_po_files,
    get_translation_stats,
)

if TYPE_CHECKING:
    from sphinx.application import Sphinx


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
        # Declare the dependency on .po files explicitly so incremental
        # builds (nox -s docs, docs-live) do not use the cached
        # doctree with stale numbers in it.
        env = self.state.document.settings.env
        for po_file in get_po_files():
            env.note_dependency(str(po_file))

        # English is the reference row (100% by definition); the script adds it.
        data = get_translation_stats(include_english=True)

        # Sort data by locale and module
        data = {
            locale: dict(sorted(loc_stats.items()))
            for locale, loc_stats in sorted(data.items())
        }

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

        # plotly only lets us use css variables for colors in some places,
        # and plotly otherwise inlines a lot of CSS itself.
        # so colors are partially specified here, and partially (forcefully)
        # overridden in _static/pyos.css
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
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


def write_translation_stats(app: "Sphinx", exception: Exception | None) -> None:
    from sphinx.util import logging

    logger = logging.getLogger("_ext.translation_graph")

    if app.builder.name != "html":
        logger.info("Skipping translation stats for non-HTML build")
        return

    if exception is not None:
        logger.info("Skipping translation stats because the build raised an exception")
        return

    stats = get_translation_stats()
    if not stats:
        logger.info("Skipping translation stats because no .po files were found")
        return

    out_path = Path(app.outdir) / "_static" / "translation_stats.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
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
