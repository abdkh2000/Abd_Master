# Project Log

## 2026-07-12

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
