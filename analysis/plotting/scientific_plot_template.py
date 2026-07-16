#!/usr/bin/env python3
"""Portable Matplotlib template for clean scientific comparison plots.

The file is self-contained so it can be copied into another project. Replace
the synthetic arrays in ``main`` with data loaded from CSV, NumPy, or another
source, then adjust the labels and output name.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Figure sizes used for the validation plots.
FULL_PROFILE_FIGSIZE = (6.4, 4.8)
COMPACT_FIGSIZE = (6.4, 4.2)

# Main visual hierarchy: present data first, reference data second.
PRESENT_STYLE = {
    "color": "#1f77b4",
    "linestyle": "-",
    "linewidth": 1.8,
    "label": "Present simulation",
}
REFERENCE_STYLE = {
    "color": "#ff7f0e",
    "linestyle": "--",
    "linewidth": 1.4,
    "label": "Reference data",
}


def apply_plot_style() -> None:
    """Apply a consistent, publication-friendly Matplotlib style."""
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans"],
            "mathtext.fontset": "dejavusans",
            "font.size": 10.0,
            "axes.labelsize": 11.0,
            "axes.titlesize": 11.0,
            "xtick.labelsize": 9.5,
            "ytick.labelsize": 9.5,
            "legend.fontsize": 9.0,
            "axes.grid": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "legend.frameon": True,
            "legend.framealpha": 0.9,
            "savefig.dpi": 300,
        }
    )


def save_figure(fig: plt.Figure, output_stem: Path) -> tuple[Path, Path]:
    """Save a vector PDF for documents and a 300-dpi PNG for review."""
    output_stem.parent.mkdir(parents=True, exist_ok=True)
    pdf_path = output_stem.with_suffix(".pdf")
    png_path = output_stem.with_suffix(".png")

    fig.savefig(
        pdf_path,
        bbox_inches="tight",
        metadata={
            "Creator": "Matplotlib",
            "Producer": "Matplotlib",
            "CreationDate": None,
            "ModDate": None,
        },
    )
    fig.savefig(
        png_path,
        dpi=300,
        bbox_inches="tight",
        metadata={"Software": "Matplotlib"},
    )
    return pdf_path, png_path


def plot_comparison(
    x_present: np.ndarray,
    y_present: np.ndarray,
    x_reference: np.ndarray,
    y_reference: np.ndarray,
    *,
    xlabel: str,
    ylabel: str,
    output_stem: Path,
    title: str | None = None,
    xscale: str = "linear",
    yscale: str = "linear",
    figsize: tuple[float, float] = FULL_PROFILE_FIGSIZE,
) -> tuple[Path, Path]:
    """Create and save a two-source scientific comparison figure."""
    apply_plot_style()

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(x_present, y_present, **PRESENT_STYLE)
    ax.plot(x_reference, y_reference, **REFERENCE_STYLE)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    if title:
        ax.set_title(title)

    ax.grid(False)
    ax.legend()
    fig.tight_layout()

    paths = save_figure(fig, output_stem)
    plt.close(fig)
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("template_output"),
        help="Directory for the example PDF and PNG",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # ------------------------------------------------------------------
    # REPLACE THIS EXAMPLE SECTION WITH THE STUDENT'S OWN DATA.
    # For example:
    # data = np.loadtxt("profiles.csv", delimiter=",", skiprows=1)
    # x_present, y_present = data[:, 0], data[:, 1]
    # ------------------------------------------------------------------
    x_present = np.linspace(0.0, 1.0, 120)
    y_present = 1.0 - np.exp(-4.2 * x_present)
    x_reference = np.linspace(0.0, 1.0, 80)
    y_reference = 1.0 - np.exp(-4.0 * x_reference)

    pdf_path, png_path = plot_comparison(
        x_present,
        y_present,
        x_reference,
        y_reference,
        xlabel=r"$x/\delta$",
        ylabel=r"$U/U_\infty$",
        output_stem=args.output_dir / "example_comparison",
    )
    print(f"Saved {pdf_path}")
    print(f"Saved {png_path}")


if __name__ == "__main__":
    main()
