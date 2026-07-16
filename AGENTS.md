# Instructions for Future Codex Sessions

Work inside this project folder only unless the user explicitly authorizes a specific outside file or folder.

## Workflow

- Inspect `git status` before making changes.
- Keep commits small and meaningful.
- Compile `main.tex` before committing and before pushing when LaTeX files change.
- Record meaningful session changes in `PROJECT_LOG.md`.
- Never overwrite user work. If unexpected edits appear, preserve them and ask when needed.
- Never commit secrets, passwords, API keys, browser profiles, private system files, or unrelated personal documents.
- Summarize what changed, what checks ran, and what remains after each session.

## Mandatory Scientific Plotting House Style

Before creating or modifying any thesis plot, read and follow:

`.agents/skills/abd-master-scientific-plots/SKILL.md`

This is the mandatory plotting house style for simulation-versus-reference
comparisons, comparisons with other laboratories, velocity and temperature
profiles, RMS statistics, Reynolds stresses, convergence histories, and all
validation figures.

- Use NumPy and Matplotlib only; do not use Seaborn.
- Plot the present simulation first as the visually primary blue solid line.
- Plot the primary reference second as an orange dashed line.
- Do not use a grid or silently substitute another plotting theme for an
  external laboratory dataset.
- Keep typography and figure sizes consistent, and export both a vector PDF
  and a 300-dpi PNG.
- Keep the present simulation first in the legend.
- Explicitly disclose coordinate remapping, interpolation, folding,
  symmetrization, normalization, and non-twin reference cases.

## Build

Use:

```powershell
latexmk -pdf main.tex
```

The PDF should be generated at `build/main.pdf`.
