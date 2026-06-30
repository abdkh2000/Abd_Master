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

## Build

Use:

```powershell
latexmk -pdf main.tex
```

The PDF should be generated at `build/main.pdf`.

