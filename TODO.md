# Project TODO

## Immediate setup tasks

- [ ] Restart VS Code and terminal so newly installed Git, Perl, MiKTeX, and PATH updates are fully available.
- [ ] Open this repository folder in VS Code.
- [ ] Keep the reference thesis PDF outside Git; use it only as private structural guidance.
- [ ] Keep all credentials, SSH config entries, usernames, passwords, private keys, IP addresses, and host details outside Git.
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
- [ ] Keep the exact remote path outside Git; use `[REDACTED_REMOTE_WORKDIR]` if a placeholder is needed.

## Supercomputer access tasks

- [ ] Create CINECA/UserDB account.
- [ ] Email the advisor after the account exists so he can add the account to the project.
- [ ] Complete any required two-factor authentication setup.
- [ ] Follow the official connection procedure for the supercomputer.
- [ ] Confirm where thesis-scale runs should be launched and how job scripts should be written.
- [ ] Do not place supercomputer credentials, account names, project IDs, or login commands in Git.

## BRINE code usage tasks

- [x] Verify the exact server-side code/folder name: `Brine`, `BRINE36`, `BRINE3G`, or another variant.
- [ ] Keep one untouched clean copy of the code.
- [ ] For every simulation, copy the clean folder and work only in the copy.
- [ ] Build libraries once after copying the folder.
- [x] Identify the correct machine-specific build and run scripts.
- [x] Locate and document the purpose of `input.inp`.
- [x] Locate and document the purpose of `ic.inp`.
- [x] Locate where `module.F90` sets `nx`, `ny`, and `nz`.
- [x] Locate where `main.F90` controls flags.
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

- [ ] What is the exact server-side code folder name?
- [ ] Which code version should be treated as the clean baseline?
- [ ] Which flags in `main.F90` enable buoyancy?
- [ ] Which input parameters control the Boussinesq buoyancy term?
- [ ] What is the temperature/buoyancy sign convention?
- [ ] Which wall should be hot and which wall should be cold?
- [ ] Which nondimensional stratification or buoyancy parameter should be tested first?
- [ ] Which baseline validation plots are required before enabling buoyancy?
- [ ] Which reference DNS datasets should be used for the non-buoyant baseline?
- [ ] What grid and runtime should be used for the first supercomputer test?
- [ ] What final statistics and figures are expected for the thesis report?
