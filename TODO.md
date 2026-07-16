# Project TODO

## Scientific plotting standard — 2026-07-16

- [x] Install the mandatory repository plotting skill at
  `.agents/skills/abd-master-scientific-plots/SKILL.md`.
- [x] Install the canonical NumPy/Matplotlib template at
  `analysis/plotting/scientific_plot_template.py`.
- [x] Record the distinct fresh one-million-step validation and extended
  Leonardo restart parameter sets, including the non-twin-reference caveat.
- [x] Run the plotting template locally and confirm vector PDF and 300-dpi PNG
  outputs; keep the generated example files outside Git.
- [ ] Confirm the wall-normal stretching factor for a fresh validation run
  from the actual approved input files.
- [ ] Check the actual BRINE flags, input-line values, and initial-condition
  selectors before configuring or launching a thermal case.
- [ ] Determine whether a future reproduction is a fresh run or a restart
  before choosing between $\Delta t=3\times10^{-4}$ and
  $\Delta t=5\times10^{-4}$.

## 2026-07-14 advisor-meeting follow-up

### Newly answered

- [x] Use the project convention: $x$ streamwise, $y$ spanwise, and $z$
  wall-normal, with velocity components $u$, $v$, and $w$, respectively.
- [x] Confirm the editable flag region in `main.f90` around lines 69--74 and
  keep salinity and melting disabled for the current Master Project.
- [x] Confirm that the first three lines of `module.f90` define `nx`, `ny`, and
  `nz`; `input.inp` contains runtime and physical parameters; and `IC.inp`
  controls velocity and temperature initial conditions.
- [x] Record the Poseidon workflow: `poseidon.sh` compiles and runs, with about
  128 points per direction as an approximate practical maximum.
- [x] Record the Leonardo workflow: use a clean copied folder, compile with
  `leo.sh`, and submit `go_leo.sh` through `sbatch` with one process per GPU.
- [x] Record the cluster safety rules: no computation on the login node, no AI
  autopilot, and manual approval before every cluster-changing command.
- [x] Confirm the nondimensional relations $h=L_z/2$,
  $u_\tau=\sqrt{\tau_w/\rho}$, and $Re_\tau=u_\tau h/\nu$. For $L_z=2$,
  $|\Pi|=1$, and $\rho=1$, use $h=\tau_w=u_\tau=1$ and
  $\nu=\mu=1/Re_\tau$.
- [x] Record that the time step must satisfy both diffusion and CFL
  restrictions, use the more restrictive value with a safety margin, and
  account for the smallest spacing in the stretched wall-normal grid.
- [x] Record the planned benchmark sequence: unstratified channel at
  $Re_\tau=590$; passive scalar at $Re_\tau=550$, $Pr=1$; and stable
  stratification at $Re_\tau=180$, $Pr=0.7$, $Ri_\tau=120$.

### Outstanding from the meeting

- [ ] Obtain and adopt the official TU Wien thesis template.
- [ ] Confirm the final thesis title and complete TISS registration.
- [ ] Obtain the Kleandro thermal test input and post-processing scripts.
- [ ] Confirm the exact stable wall-temperature arrangement and gravity/sign
  convention.
- [ ] Obtain the exact Garcia-Villalba benchmark input and comparison data.
- [ ] Confirm the exact spelling of the buoyancy variable in the relevant code
  version.
- [ ] Resolve the setup/path issue that caused the previous $16^3$ Poseidon
  attempt to fail before considering another run.
- [ ] Confirm whether the passive-scalar benchmark should use $Re_\tau=550$ or
  $Re_\tau=500$; do not run it until the supplementary-document inconsistency
  is resolved.

## Immediate setup tasks

- [ ] Restart VS Code and terminal so newly installed Git, Perl, MiKTeX, and PATH updates are fully available.
- [ ] Open this repository folder in VS Code.
- [ ] Keep the reference thesis PDF outside Git; use it only as private structural guidance.
- [x] Keep all credentials, SSH config entries, usernames, passwords, private keys, IP addresses, and host details outside Git.
- [ ] Practice terminal basics: `cd`, `ls`/`dir`, `pwd`, `mkdir`, copy, move, and remove temporary files.
- [ ] Update `PROJECT_LOG.md` after each meaningful work session.

## SSH / VS Code Remote SSH tasks

- [ ] Install or confirm VS Code extension `Remote - SSH`.
- [ ] Learn the structure of `.ssh/config`.
- [x] Configure remote SSH aliases locally, but do not commit the config file or any login data.
- [x] Test SSH connection using private credentials supplied outside this repository.
- [ ] Connect with VS Code Remote SSH.
- [ ] Open a remote terminal through VS Code after connection.
- [x] Work only in the advisor-approved shared-machine project folder.
- [x] Keep the exact remote path outside Git; use `[REDACTED_REMOTE_PATH]` if a placeholder is needed.

## Supercomputer access tasks

- [x] Create CINECA/UserDB account.
- [x] Email the advisor after the account exists so he can add the account to the project.
- [x] Complete any required two-factor authentication setup.
- [x] Follow the official connection procedure for the supercomputer.
- [x] Confirm that thesis-scale runs use Leonardo and are submitted with
  `go_leo.sh` through `sbatch` after compilation with `leo.sh`.
- [x] Do not place supercomputer credentials, account names, project IDs, or login commands in Git.

## BRINE code usage tasks

- [x] Verify the exact server-side code/folder name: `Brine`, `BRINE36`, `BRINE3G`, or another variant.
- [x] Keep one untouched clean copy of the code.
- [x] For every simulation, copy the clean folder and work only in the copy.
- [ ] Build libraries once after copying the folder.
- [x] Identify the correct machine-specific build and run scripts.
- [x] Locate and document the purpose of `input.inp`.
- [x] Locate and document the purpose of `IC.inp`.
- [x] Locate where `module.f90` sets `nx`, `ny`, and `nz`.
- [x] Locate where `main.f90` controls flags.
- [x] Confirm that the `main.f90` flag region includes temperature, salinity,
  and melting controls, with salinity and melting disabled for this project.
- [x] Prepare tiny edit plan for the BRINE working copy.
- [x] Apply first tiny grid edit in the BRINE working copy.
- [x] Attempt first tiny compile/run smoke test.
- [x] Diagnose first tiny-grid run failure from sanitized remote log.
- [ ] Identify the exact buoyancy/thermal-stratification flags.
- [ ] Never commit the full external codebase unless the advisor explicitly permits it and it is legally appropriate.

## Simulation plan

- [ ] Run tiny local/shared-machine tests only to learn the workflow.
- [ ] Keep local grids small.
- [ ] Avoid large local simulations, with about `128` points per direction as an approximate local upper limit.
- [ ] First reproduce a non-buoyant baseline channel-flow case.
- [ ] Check baseline mean velocity profile and core turbulence statistics.
- [ ] Check passive-scalar or temperature behavior in the non-buoyant baseline.
- [ ] Add the Boussinesq buoyancy term or enable the existing buoyancy implementation.
- [ ] Run a stable thermal stratification case.
- [ ] Compare non-buoyant baseline against buoyant/stratified case.
- [ ] Look for suppression of turbulence and reduced vertical mixing.
- [ ] Look for internal gravity waves or interface-like behavior between warmer upper fluid and colder lower fluid.
- [ ] Move final thesis-scale simulations to the supercomputer.
- [ ] Define required post-processing plots before launching expensive runs.

## Theory reading list

- [x] Start theory notes on turbulent channel flow basics.
- [ ] Wall-bounded turbulent flows.
- [ ] Direct Numerical Simulation of turbulence.
- [ ] Pope, `Turbulent Flows`, focusing on core turbulence concepts.
- [ ] Kolmogorov scales and turbulence cascade.
- [ ] Reynolds stresses and turbulent momentum transport.
- [ ] Shear/friction velocity.
- [ ] Shear Reynolds number.
- [ ] Basic statistics: means, RMS fluctuations, Reynolds shear stress, stationarity, averaging windows.
- [ ] Kim and Moin / classic DNS channel-flow papers.
- [ ] Boussinesq approximation and buoyancy force.
- [ ] Stable thermal stratification.
- [ ] Internal gravity waves.
- [ ] Turbulence suppression by stable density/temperature stratification.

## Open questions for advisor

- [x] What is the exact server-side code folder name?
- [ ] Which code version should be treated as the clean baseline?
- [ ] Which flags in `main.F90` enable buoyancy?
- [ ] Which input parameters control the Boussinesq buoyancy term?
- [ ] What is the temperature/buoyancy sign convention?
- [ ] Which wall should be hot and which wall should be cold?
- [x] Which nondimensional stratification or buoyancy parameter should be
  tested first? Current plan: $Re_\tau=180$, $Pr=0.7$, and $Ri_\tau=120$ for
  the stable benchmark.
- [ ] Which baseline validation plots are required before enabling buoyancy?
- [ ] Which reference DNS datasets should be used for the non-buoyant baseline?
- [ ] What grid and runtime should be used for the first supercomputer test?
- [ ] What final statistics and figures are expected for the thesis report?
