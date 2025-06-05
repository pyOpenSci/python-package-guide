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
        # Read the JSON file containing translation statistics
        json_path = Path(__file__).parent.parent / "_static" / "translation_stats.json"
        with json_path.open("r") as f:
            data: TranslationStats = json.load(f)

        # Sort data by locale and module
        data = {locale: dict(sorted(loc_stats.items())) for locale, loc_stats in sorted(data.items())}

        # prepend english, everything set to 100%
        en = {module: ModuleStats(total=stats['total'], translated=stats['total'], fuzzy=stats['total'], untranslated=0, percentage=100) for module, stats in next(iter(data.values())).items()}
        data = {'en': en} | data

        # extract data to plot
        locales = list(data.keys())
        modules = list(data[locales[-1]].keys())
        values = [[stats['percentage'] for stats in loc_stats.values()] for loc_stats in data.values()]
        hoverdata = [[{'module': module} | stats for module, stats in loc_stats.items()] for loc_stats in data.values()]
        heatmap = go.Heatmap(
            x =modules,
            y=locales,
            z=values,
            xgap=5,
            ygap=5,
            customdata=np.array(hoverdata),
            hovertemplate=self.HOVER_TEMPLATE,
            colorbar={
                'orientation': 'h',
                'y': 0,
                "yanchor": "bottom",
                "yref": "container",
                "title": "Completion %",
                "thickness": 10,
            },
            colorscale="Plotly3",
        )
        # Create figure
        fig = go.Figure(data=heatmap)
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="var(--bs-body-color)",
            margin=dict(l=40, r=40, t=40, b=40),
            xaxis_showgrid=False,
            xaxis_side="top",
            xaxis_tickangle=-45,
            xaxis_tickfont = {
                "family": "var(--bs-font-monospace)",
                "color": "#fff"
            },
            yaxis_showgrid=False,
            yaxis_title="Locale",
            yaxis_autorange="reversed",
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
