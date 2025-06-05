from pathlib import Path
import json
from typing import TypeAlias, TypedDict, Annotated as A

from docutils import nodes
from docutils.parsers.rst import Directive
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np


class ModuleStats(TypedDict):
    total: int
    translated: int
    fuzzy: int
    untranslated: int
    percentage: float

TranslationStats: TypeAlias = dict[A[str, "locale"], dict[A[str, "module"], ModuleStats]]


class TranslationGraph(Directive):
    # Tells Sphinx that this directive can be used in the document body
    # and has no content
    has_content = False

    def run(self):
        # Read the JSON file containing translation statistics
        json_path = Path(__file__).parent.parent / "_static" / "translation_stats.json"
        with json_path.open("r") as f:
            data: TranslationStats = json.load(f)

        # Collect all module names -- iterates over the JSON data in 2 levels
        all_modules = {module for stats in data.values() for module in stats}
        all_modules = sorted(all_modules)

        # Build one trace per locale with full hover info
        traces = []

        for locale, modules in data.items():
            y_vals = []
            hover_texts = []

            for module in all_modules:
                stats = modules.get(module)
                y_vals.append(stats["percentage"])

                hover_text = (
                    f"<b>{module}</b><br>"
                    f"Translated: {stats['translated']}<br>"
                    f"Fuzzy: {stats['fuzzy']}<br>"
                    f"Untranslated: {stats['untranslated']}<br>"
                    f"Total: {stats['total']}<br>"
                    f"Completed: {stats['percentage']}%"
                )
                hover_texts.append(hover_text)

            traces.append(go.Bar(
                name=locale,
                x=all_modules,
                y=y_vals,
                hovertext=hover_texts,
                hoverinfo="text"
            ))

        # Create figure
        fig = go.Figure(data=traces)
        fig.update_layout(
            barmode="group",
            title="Translation Coverage by Module and Locale",
            xaxis_title="Module",
            yaxis_title="Percentage Translated",
            height=600,
            margin=dict(l=40, r=40, t=40, b=40)
        )

        div = plot(fig, output_type="div", include_plotlyjs=True)
        return [nodes.raw("", div, format="html")]

def setup(app):
    app.add_directive("translation-graph", TranslationGraph)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
