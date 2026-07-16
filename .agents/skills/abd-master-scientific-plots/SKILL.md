---
name: abd-master-scientific-plots
description: Use the Abd_Master/Kleandro Matplotlib house style for all thesis figures, especially simulation-versus-reference and cross-laboratory validation plots.
---

# Abd_Master Scientific Plot Skill

## Purpose

Apply one consistent visual language to every scientific figure produced for the Abd_Master project. The uploaded `scientific_plot_template.py` is the canonical starting point. Do not introduce a different plotting theme merely because a new dataset, script, chapter, or external laboratory is involved.

Use this skill for:

- present-simulation versus literature/reference comparisons;
- comparisons with THTLab, Moser, Costa, García-Villalba, Pirozzoli, or other laboratories;
- mean velocity and temperature profiles;
- RMS velocity and scalar fluctuations;
- Reynolds stresses and turbulent kinetic energy;
- full-channel, half-channel, inner-scaled, and outer-scaled profiles;
- convergence histories and validation metrics;
- thesis-ready PDF figures and review PNGs.

## Canonical Implementation

Use Python, NumPy, and Matplotlib. Do not use Seaborn or a style package that changes the established appearance.

Start from the project template module whenever possible:

- `FULL_PROFILE_FIGSIZE = (6.4, 4.8)`
- `COMPACT_FIGSIZE = (6.4, 4.2)`
- white figure and axes backgrounds;
- no grid;
- DejaVu Sans for plot text and DejaVu Sans mathtext;
- base font size 10 pt;
- axis labels 11 pt;
- tick labels 9.5 pt;
- legend 9 pt;
- framed legend with approximately 0.9 opacity;
- 300 dpi review PNG;
- vector PDF for the thesis.

### Primary hierarchy

The present Abd_Master result is always visually dominant:

```python
PRESENT_STYLE = {
    "color": "#1f77b4",
    "linestyle": "-",
    "linewidth": 1.8,
    "label": "Present simulation",
}
```

The main external reference is secondary:

```python
REFERENCE_STYLE = {
    "color": "#ff7f0e",
    "linestyle": "--",
    "linewidth": 1.4,
    "label": "Reference data",
}
```

Do not reverse this order in either plotting calls or the legend.

## Thesis Figure Rules

1. Use physical or nondimensional symbols in the axis labels, preferably with Matplotlib mathtext.
2. Do not place a long explanatory title inside a thesis plot. Put the explanation in the LaTeX caption. Add a short title only when the plot would otherwise be ambiguous outside the thesis.
3. Do not use a grid unless the user explicitly approves an exception for a diagnostic plot.
4. Do not use background shading, 3D effects, decorative palettes, or unnecessary markers.
5. Use `fig.tight_layout()` and save with `bbox_inches="tight"`.
6. Save both:
   - `<name>.pdf` for inclusion in LaTeX;
   - `<name>.png` at 300 dpi for review.
7. Close the figure after saving.
8. Keep figure dimensions consistent within the same chapter.
9. Place units in axis labels when quantities are dimensional.
10. Use concise legend labels that identify the actual source, for example:
    - `Present simulation`
    - `Moser et al. (1999)`
    - `THTLab CH12_PG.WL7`
    - `García-Villalba & del Álamo (2011)`

## Multiple External Laboratories

When more than one reference dataset is shown:

- keep the present simulation as the blue solid line with linewidth 1.8;
- keep the principal benchmark as the orange dashed line with linewidth 1.4;
- assign additional references restrained line styles or markers;
- avoid changing the present-simulation style;
- do not use a rainbow palette;
- order the legend as: present simulation, primary reference, additional references, theoretical laws;
- identify every dataset precisely in the caption and processing metadata.

Theoretical relations such as the viscous law or logarithmic law should use thin neutral black/gray dotted or dash-dotted lines so they do not compete with the simulation and reference datasets.

## Multiple Components

For plots containing several components, such as \(u_{\mathrm{rms}}^+\), \(v_{\mathrm{rms}}^+\), and \(w_{\mathrm{rms}}^+\):

- keep component identity consistent by line style and/or restrained color choice;
- distinguish source identity consistently across all components;
- do not create an unreadable six-entry legend when direct component labels or a carefully grouped legend is clearer;
- preserve the coordinate mapping:
  - \(x\): streamwise;
  - \(y\): spanwise;
  - \(z\): wall-normal;
  - \(u\): streamwise velocity;
  - \(v\): spanwise velocity;
  - \(w\): wall-normal velocity.
- when comparing with a source that uses \(y\) as wall-normal, explicitly remap the components and state it in the caption.

For Abd_Master, the streamwise–wall-normal Reynolds stress is normally \(-\langle u'w'\rangle\). A reference may label the same physical quantity as \(-\langle u'v'\rangle\). Never overlay these without documenting the coordinate-convention conversion.

## Profile Conventions

### Inner scaling

- use a logarithmic horizontal axis when plotting versus \(y^+\) or conventional wall distance in wall units;
- retain conventional literature notation \(y^+\) when appropriate, even though the solver coordinate is \(z\), but explain that it denotes distance from the nearest wall;
- do not include zero on a logarithmic axis;
- state how wall quantities were calculated.

### Full-channel profiles

- plot the physical wall-normal coordinate \(z\) or a clearly defined normalized coordinate;
- preserve the lower/upper-wall orientation;
- do not silently fold or symmetrize the profile;
- when a folded half-channel profile is used, state the folding procedure.

### Time histories

- use the same fonts, export settings, and visual hierarchy;
- present one ordered line per quantity;
- avoid markers on every point when the history is dense;
- use a horizontal reference line only when it represents a documented analytical or target value.

## Comparison Integrity

Before plotting:

1. Verify units and nondimensionalization.
2. Verify coordinate conventions and component mapping.
3. Verify whether each profile is full-channel, half-channel, folded, or symmetrized.
4. Verify the averaging window.
5. Verify whether ghost points are present.
6. Verify whether interpolation is required.

Never:

- silently extrapolate reference data;
- silently normalize two datasets differently;
- hide a mismatch in Reynolds number, Prandtl number, boundary conditions, forcing, or wall scaling;
- label a non-twin thermal reference as exact validation;
- compare arrays only because their column positions match.

When interpolation is needed, restrict it to the common overlap, preserve the original data, and record the interpolation method.

## Metrics

Where suitable, compute comparison metrics separately from the plotting function:

- absolute difference;
- relative difference only where the denominator is safely nonzero;
- \(L_2\) difference over a documented common domain;
- maximum absolute difference;
- maximum relative difference with an explicit masking rule.

Do not place many metrics inside the figure. Put them in the thesis text, caption, a table, or a sidecar metrics file.

## Reproducibility

Each final plotting script should record or make clear:

- source data files;
- dataset names and literature source;
- coordinate mapping;
- normalization;
- averaging window;
- symmetrization/folding;
- interpolation;
- output filenames.

Keep raw data unchanged. Write derived profiles and metrics to separate processed-data files when practical.

## File Organization

Recommended structure:

```text
analysis/
  plotting/
    scientific_plot_template.py
    plot_<quantity>.py
data/
  raw/
  processed/
figures/
  validation/
    <quantity>.pdf
    <quantity>.png
```

Use descriptive stems such as:

- `mean_velocity_inner_comparison`
- `velocity_rms_comparison`
- `reynolds_shear_stress_comparison`
- `mean_temperature_full_channel`
- `temperature_rms_full_channel`

## Review Checklist

Before accepting a figure:

- [ ] Present simulation is blue, solid, and visually primary.
- [ ] Main reference is orange and dashed.
- [ ] No unintended grid or plotting theme is active.
- [ ] Labels, notation, and coordinate conventions are correct.
- [ ] Reference source is named accurately.
- [ ] Reynolds number, Prandtl number, boundary conditions, and scaling are compatible or the mismatch is disclosed.
- [ ] Averaging window and folding/symmetrization are documented.
- [ ] Legend order is correct.
- [ ] PDF and 300-dpi PNG are saved.
- [ ] The LaTeX caption explains the comparison without relying on a plot title.
