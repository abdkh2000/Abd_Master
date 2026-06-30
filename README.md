# Abd_Master

LaTeX-based academic project workspace.

## Compile the PDF

From the project root:

```powershell
latexmk -pdf main.tex
```

The generated PDF is written to `build/main.pdf`.

To remove generated build files:

```powershell
latexmk -C
```

## VS Code

Open this folder in VS Code and use the LaTeX Workshop extension. Build with the extension's build command or by saving the file if auto-build is enabled.

If `latexmk` is not recognized after installing MiKTeX, restart VS Code and your terminal. If it still is not found, add this folder to your user PATH:

```text
C:\Users\abdul\AppData\Local\Programs\MiKTeX\miktex\bin\x64
```

## Project Layout

- `main.tex`: main LaTeX entry point
- `chapters/`: document chapters and sections
- `figures/`: figure assets
- `tables/`: table source files or exports
- `references.bib`: bibliography database
- `notes/meeting_transcripts/`: advisor meeting transcripts
- `notes/advisor_feedback/`: advisor feedback notes
- `scripts/`: scripts for figures, tables, and analysis
- `data/`: project data; keep sensitive or large raw data out of Git unless intentionally approved
- `build/`: generated LaTeX outputs
