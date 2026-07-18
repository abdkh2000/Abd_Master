# Project Log

## 2026-07-18

### Theory Statistics Refinement and Provisional Front Matter

- Found and preserved the completed condensed theory on local `main` at
  `f6b48df` (`Condense and complete project theory chapter`). After fetching
  `origin`, that clean local branch was one commit ahead of `origin/main`; the
  correction therefore continued from the completed local work rather than
  from the older remote chapter.
- Refined subsection 2.2, *Turbulence Statistics and Wall Scaling*, from five
  to three displayed equation environments. The subsection now contains only
  the Reynolds decomposition, the combined validation statistics, and the
  combined wall quantities needed for the planned plots. It occupies about one
  typeset page across physical PDF pages 6--7.
- Reduced `chapters/theory.tex` from 360 to 306 source lines. The complete
  theory chapter spans physical PDF pages 5--11 (Arabic pages 3--9), or seven
  actual pages.
- Added a provisional, logo-free title page in `frontmatter/titlepage.tex` and
  replaced the generic `\maketitle` sequence. The final arrangement is an
  unnumbered cover on physical page 1, a standalone Roman-numbered contents
  page on physical page 2, the introduction beginning at Arabic page 1 on
  physical page 3, and the bibliography on physical page 12.
- Compiled successfully with
  `& 'C:\Users\abdul\AppData\Local\Programs\MiKTeX\miktex\bin\x64\latexmk.exe' -pdf main.tex`.
  The repository configuration invoked XeLaTeX and produced a 12-page PDF.
  The document log contains no undefined references or citations, multiply
  defined labels, LaTeX/package warnings, overfull or underfull boxes, or
  compilation errors. The rendered document was inspected visually; only the
  environmental MiKTeX update-check notice remains in command output.

### Project-Level Theoretical Background Rewrite

- Rebuilt the theoretical background around five project-specific subsections:
  governing equations, turbulence statistics and wall scaling, scalar transport
  and buoyancy, stable stratification, and minimum DNS requirements.
- Removed the geometry figure, full internal-wave derivation and detection
  workflow, DNS--LES--RANS comparison, dissipative-scale derivations, detailed
  grid/stretching and time-step theory, sampling formulas, and convergence
  campaign checklists. Closely related definitions were merged into 13 compact
  displayed equation blocks, and the three planned cases were connected in a
  concluding paragraph.
- Reduced `chapters/theory.tex` from 1,175 to 360 source lines and the compiled
  theory span from PDF pages 3--29 (27 pages) to pages 3--10 (8 pages), without
  changing the document typography or layout settings.
- Compiled successfully with `latexmk -pdf main.tex` through the installed
  MiKTeX executable. The final log contains no undefined references or
  citations, duplicate labels, overfull or underfull boxes, or compilation
  errors; all eight theory pages were rendered and inspected visually.
- Kept the passive-scalar Reynolds number, exact stable wall-temperature and
  gravity/sign convention, and BRINE buoyancy-variable and coefficient mapping
  unresolved in `TODO.md` rather than assigning unverified values.

## 2026-07-16

### Portable LaTeX Font Selection

- Added a `fontspec` availability check that retains Times New Roman where it
  is installed and otherwise uses TeX Gyre Termes with an explicit build-log
  warning for non-final builds.
- Made the XeLaTeX selection explicit in the GitHub Actions build; the final
  font requirement remains subject to the official TU Wien template.

### DNS Resolution, Time-Step Restrictions, and Statistical Convergence

- Added the DNS-resolution framework covering turbulent and scalar dissipative
  scales, wall-unit grid spacing, domain size, stretching, and caveated
  project setup records.
- Defined generic advective and diffusive time-step measures while leaving all
  stability constants and BRINE numerical-method details scheme-dependent and
  unverified.
- Distinguished temporal stability, physical sampling, statistical
  stationarity, statistical convergence, grid convergence, time-step
  convergence, and agreement with reference DNS for the planned benchmarks.

### Internal Gravity Waves in Stably Stratified Channel Flow

- Added the ideal linear internal-wave equations, dispersion relation, and
  mean-flow Doppler shift using the existing gravity-explicit sign convention.
- Documented channel confinement, wave--turbulence interaction, and the
  evidence required to distinguish internal waves from visually wave-like
  turbulent or sampling behaviour.
- Connected the theory to the planned $Re_\tau=180$, $Pr=0.7$,
  $Ri_\tau=120$ benchmark without claiming a completed simulation or wave
  detection, and recorded the future spectral-analysis and plotting-standard
  requirements.

### Boussinesq Approximation and Stable Stratification

- Added the coupled Boussinesq density, buoyancy, momentum, buoyancy-frequency,
  and Richardson-number theory using an explicit physical gravity-vector sign
  convention.
- Documented the planned $Re_\tau=180$, $Pr=0.7$, $Ri_\tau=120$ stable
  benchmark as future work and retained the unresolved BRINE gravity, wall,
  coefficient, and normalization conventions.
- Added the verified García-Villalba--del Álamo 2011 primary reference
  and reused Pope and Armenio--Sarkar for the governing theory.

### Passive Scalar and Temperature Transport

- Added the focused theory subsection defining passive and active scalars, the
  advection--diffusion equation, Prandtl number, scalar statistics, general
  wall boundary conditions, scalar wall scaling, and a generic scalar log law.
- Kept the planned internally heated $Re_\tau=550$ benchmark separate from the
  opposed-wall $Re_\tau=150$ Kleandro working reference and retained the
  documented benchmark-value and input-convention uncertainties.
- Reused the existing Pope reference; no unverified passive-scalar citation or
  external academic file was added to the repository.

### Wall Scaling, Friction Reynolds Number, and Law of the Wall

- Added the focused theory subsection defining wall shear stress, friction
  velocity, friction Reynolds number, viscous scaling, wall units, near-wall
  regions, and the viscous and logarithmic laws of the wall.
- Documented the planned project normalization and distinguished it explicitly
  from a completed simulation result.
- Clarified BRINE's wall-normal $z,w$ convention relative to conventional
  literature notation and connected the definitions to the planned
  $Re_\tau=590$ unstratified validation benchmark.
- Added the verified Moser--Kim--Mansour 1999 benchmark citation and compiled
  the thesis successfully with XeLaTeX.

### Scientific Plotting Standard and Thermal Reference Setup

- Installed the repository-local scientific plotting skill and canonical
  NumPy/Matplotlib template, and made the skill the mandatory plotting house
  style in `AGENTS.md`.
- Added the sanitized Kleandro thermal reference setup with separate fresh-run
  and extended-restart parameters and explicit limitations on using it for a
  future reproduction.
- Ran the plotting template locally and verified that it creates a vector PDF
  and a 300-dpi PNG with the required line hierarchy, legend order, and no
  grid. The generated example directory is ignored and is not part of Git.

## 2026-07-14

### Advisor Meeting Documentation and Coordinate Correction

- Added a sanitized meeting record covering the confirmed coordinate system,
  editable code areas, guarded Poseidon and Leonardo workflows,
  nondimensionalization, time-step criteria, and planned benchmark cases.
- Corrected the thesis and supporting theory note to use $x$ streamwise, $y$
  spanwise, and $z$ wall-normal, with $u$, $v$, and $w$ as the corresponding
  velocity components.
- Recorded the unresolved benchmark-value inconsistency and the remaining
  template, registration, thermal-input, convention, benchmark-data, and
  variable-spelling questions in `TODO.md`.
- Compiled the corrected thesis with the configured XeLaTeX workflow and
  visually checked the updated diagram and statistics equations.

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
