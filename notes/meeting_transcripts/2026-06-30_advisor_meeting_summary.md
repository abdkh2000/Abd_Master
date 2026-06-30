# Advisor Meeting Summary - 2026-06-30

Source material: advisor meeting transcript PDF and handwritten meeting note provided by the user.

Sensitive data handling: any SSH credentials, usernames, passwords, hostnames, IP addresses, or private login details mentioned in the transcript must remain outside Git. If needed later, store them only in local/private credential tools, never in project notes. Credentials are represented here as `[REDACTED]`.

## Big Picture

The project is a DNS-based academic project on wall-bounded turbulent channel flow with heat transfer and buoyancy effects. The immediate goal is to become operational with the remote workflow, learn enough terminal and SSH usage to run code safely, obtain supercomputer access, and begin with lightweight local tests before moving final thesis simulations to the supercomputer.

The advisor emphasized avoiding idle waiting time: there are several independent tracks that can be worked on in parallel, including setup, code familiarization, access requests, and theory reading.

## Practical Setup

- Learn the basics of using a terminal on Windows, either Command Prompt or PowerShell.
- Practice simple navigation and file operations: changing directories, listing files, creating folders, copying folders/files, moving files, and removing temporary files.
- Learn the basics of SSH for remote login.
- Learn how the `.ssh/config` file works so repeated SSH connections can be made through aliases instead of typing full connection details.
- Do not commit SSH config entries, host details, usernames, passwords, private keys, or login commands containing private information.
- The shared-machine work area for this project is:

```text
/mnt/data/GUEST/ABDULLAH
```

Only work in that folder on the shared machine.

## VS Code Remote Workflow

- Install and use the VS Code extension named `Remote - SSH` from Microsoft.
- Configure remote hosts locally in `.ssh/config`, but keep the actual host/login details private and outside this repository.
- Use VS Code Remote SSH to open the remote machine as if it were a local workspace.
- Open a remote terminal inside VS Code after connecting.
- Use the remote workflow for code inspection, lightweight tests, and later supercomputer-related work.

## Supercomputer Access

- Create the required CINECA/UserDB account.
- After the account exists, email the advisor so he can add the account to the relevant project.
- After being added to the project, complete any required follow-up setup, including two-factor authentication and any connection software required by the supercomputer.
- Final thesis-scale simulations should be run on the supercomputer, not on the local laptop or shared lightweight machine.

## BRINE Code Usage

- The code/folder name must be verified on the server before relying on it in scripts or documentation. The transcript refers to `Brine`; the handwritten note appears to indicate something like `BRINE36` or a similar variant.
- Keep one untouched clean copy of the code.
- For each simulation, copy the code folder and work in the copy.
- Build the required libraries once after copying the folder.
- After libraries are built, go into the channel case folder and modify the simulation input/source files.
- Main files mentioned for modification:
  - `input.inp`: general simulation parameters.
  - `ic.inp`: initial conditions.
  - `module.F90`: grid-point settings, especially `nx`, `ny`, and `nz`.
  - `main.F90`: flags and switches.
- Use machine-specific build/run scripts only after confirming their names and purpose on the server.
- Stop accidental local test runs with `Ctrl+C` if needed.

## Local Testing Guidance

- Run only lightweight tests on the shared/local machine.
- Avoid large grids locally.
- Around `128` grid points per direction was mentioned as a practical upper limit for local/lightweight tests.
- Local tests are for learning the workflow, checking that the code runs, and understanding output structure.
- Local tests are not expected to be the final thesis simulations.

## Thesis Simulation Plan

The advisor described a staged plan:

1. Start from the known non-buoyant channel-flow setup.
2. Run a baseline simulation without stratification/buoyancy.
3. Check whether basic statistics are reasonable, especially velocity profile and temperature/passive-scalar behavior.
4. Switch on buoyancy.
5. Look for the stable-stratification physics:
   - warm/lighter fluid remaining near the top,
   - cold/denser fluid remaining near the bottom,
   - reduced vertical mixing,
   - suppression of turbulence,
   - formation of an interface-like structure,
   - internal gravity waves.
6. Compare the non-buoyant baseline against the buoyant case.

The goal is not to produce an overly broad validation campaign at the beginning. The core question is whether the expected buoyancy/stratification behavior appears when buoyancy is enabled.

## Theory To Study

- Wall-bounded turbulent flows.
- Direct Numerical Simulation (DNS) of turbulence.
- Basics of incompressible channel flow.
- Stephen B. Pope, `Turbulent Flows`, focusing on relevant basics rather than the whole book.
- Kolmogorov scales and turbulence cascade.
- Reynolds stresses and turbulent momentum transport.
- Shear/friction velocity.
- Shear Reynolds number.
- Basic turbulence statistics, including mean profiles, RMS fluctuations, and Reynolds shear stress.
- Kim and Moin / classic channel-flow DNS papers.
- Thermal stratification in channel flow.
- Stable temperature profiles.
- Buoyancy effects in the momentum equations.
- Internal gravity waves and turbulence suppression.

## Private Reference-Project Summary

The reference project PDF from the friend is similar in structure but not identical in physics. It validates a GPU-accelerated incompressible plane-channel solver with passive-scalar transport. It must be used only as a structural and conceptual reference, not as wording, figures, tables, or results to copy.

Short private summary:

- Thesis structure: introduction; methodology with governing equations and numerical method; laminar verification; turbulent validation; passive-scalar statistics; extended/post-processed run; conclusions and outlook.
- Baseline validation workflow: verify the solver first on laminar start-up Poiseuille flow with an analytical solution, then validate turbulent channel flow against reference DNS statistics, and finally treat passive-scalar statistics as a consistency check.
- Equations used: incompressible continuity, incompressible Navier-Stokes with streamwise forcing, passive-scalar advection-diffusion, no-slip/no-penetration walls, periodic streamwise/spanwise directions, fixed scalar values at the walls.
- Post-processing/statistics used: mean velocity profile in wall units and outer units, RMS velocity fluctuations, Reynolds shear stress, mean scalar/temperature profile, scalar RMS fluctuations, symmetry checks, stationarity checks, and comparison against reference DNS data.
- What must change for this project: the scalar/temperature field is not only passive. The buoyancy case must include a Boussinesq buoyancy term, stable thermal stratification, internal gravity waves, turbulence suppression, and a direct comparison between a non-buoyant baseline and a buoyant/stratified case.

## Open Questions

- What is the exact server-side code folder name: `Brine`, `BRINE36`, `BRINE3G`, or another variant?
- Which exact files and flags activate buoyancy in the current code version?
- What is the temperature/buoyancy sign convention?
- Which wall is hot and which wall is cold in the intended thesis configuration?
- What nondimensional buoyancy parameter should be used first?
- Which supercomputer project/account details are required after CINECA/UserDB registration?
- What minimum validation plots should be reproduced before enabling buoyancy?
- Which reference datasets should be used for baseline comparison?

