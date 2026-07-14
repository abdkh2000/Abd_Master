# Project Log

## 2026-07-14

### End-of-Day Repository Closeout

- Verified that local `main` was clean and synchronized with the correct
  `Abd_Master` GitHub origin before making the closeout documentation change.
- Confirmed that an abandoned WhisperX packaging attempt created no repository
  files or commits; its empty local branch was removed with user approval.
- Confirmed that no relevant Python, FFmpeg, LaTeX, simulation, transfer, or
  continuing Git command was left active.
- Rechecked the documented LaTeX workflow with `latexmk -pdf main.tex`; the
  existing `build/main.pdf` target was up to date.
- Added `docs/CODEX_HANDOFF.md` with the current state, known issues, and the
  exact first step for the next session.

## 2026-07-13

### Reynolds Decomposition And Turbulence Statistics

- Added the theory subsection on Reynolds decomposition, channel-DNS
  averaging, Reynolds stresses, RMS velocity fluctuations, and turbulent
  kinetic energy.
- Identified the baseline statistics required for later non-buoyant channel-DNS
  validation before buoyancy effects are interpreted.
- Reorganised the existing theory into a concise engineering-thesis structure
  covering the physical configuration, governing equations, boundary
  conditions, and validation statistics.

### Introduction And Document Formatting

- Replaced the placeholder introduction with a project-specific motivation,
  planned BRINE workflow, and non-buoyant-to-buoyant comparison strategy.
- Configured XeLaTeX to use 12-point Times New Roman with one-and-a-half line
  spacing and placed the bibliography on a separate page.
- Added a verified reference on stably stratified turbulent channel flow.

## 2026-07-12

### Theory Chapter Drafting

- Added the first theory subsection on wall-bounded turbulent channel flow and
  the governing incompressible equations.
- Defined the channel geometry, boundary conditions, fully developed-flow
  assumptions, pressure-gradient forcing, and bulk nondimensionalization.
- Added verified foundational references for the governing theory and canonical
  turbulent-channel DNS configuration.

### Leonardo And Advisor Access

- Confirmed Leonardo login, environment checks, Slurm queue access, and a controlled-output smoke test.
- Confirmed the controlled-output smoke job completed successfully and created sanitized stdout/stderr file names.
- Confirmed no active Leonardo jobs were left at end of day.
- Configured and tested a local-only advisor SSH alias outside the repository; no SSH configuration or credentials were committed.

### BRINE Discovery And Workflow Notes

- Located the BRINE baseline folder name as `BRINE36` and the channel-flow case as `BRINE36/channel`.
- Recorded a safe inventory of expected files, script names, likely script roles, and keyword locations by filename only.
- Clarified that the first discovery attempt was not a reliable keyword scan because the approved work directory was inaccessible.
- Treated the later retry, workflow inventory, and edit-map scans as the reliable BRINE discovery records because the approved folder was accessible and expected files were found.
- Created a separate remote working copy named `BRINE36_abd_work_20260712_153935`, while keeping the clean baseline untouched.
- Prepared and attempted a tiny-grid working-copy test by changing only `module.f90` grid dimensions in the working copy.
- Diagnosed the first tiny-grid attempt from sanitized metadata: the compile/run attempt exited with code `132`, and the refined category is `missing_file` during setup, likely requiring a working-copy path-reference fix before any rerun.

### Theory And Recovery Audit

- Added the first theory note on turbulent channel-flow basics.
- Audited the repository after commit `6e9e2d7311789a4cdf50f7e017522799a71e9280` for missing local work, untracked files, staged changes, unpushed commits, and generated helper outputs.
- Found no uncommitted or unpushed safe project documentation after that anchor commit before this recovery note.
- Added a sanitized recovery audit so the repository records where the later BRINE investigation results were stored and what remains to do.

## 2026-07-08

### Leonardo Smoke Test

- Ran a minimal Leonardo Slurm smoke-test workflow with sanitized documentation.
- Repeated the smoke test with explicit output and error files after the first accepted job did not produce files in the checked folder.
- Confirmed the controlled-output smoke test completed successfully.
- Recorded that no remote jobs were left running or pending during end-of-day cleanup.

## 2026-06-30

### Repository Setup

- Created initial LaTeX academic project structure.
- Added a minimal compiling `main.tex` and first chapter file.
- Added `.gitignore`, `.latexmkrc`, README, future-agent instructions, VS Code settings, and GitHub Actions workflow.
- Confirmed MiKTeX tools are installed locally under the user MiKTeX folder.
- Installed Git and Strawberry Perl with user approval so Git workflows and `latexmk` work from this machine.
- Verified the project compiles with `latexmk -pdf main.tex`, producing `build/main.pdf`.
- Connected the local project to the existing GitHub repository and merged its initial README into the project README.

### Notes And Planning

- Added clean Markdown notes from the 2026-06-30 advisor meeting transcript and handwritten notes.
- Added `TODO.md` with setup, SSH, supercomputer, BRINE, simulation, theory, and advisor-question tasks.
- Used the friend's thesis PDF only as a private structural reference and recorded differences for the buoyancy/thermal-stratification project.
