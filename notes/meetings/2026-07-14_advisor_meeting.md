# Advisor Meeting Record

Date: 2026-07-14

This is a sanitized project record derived from the private meeting materials.
It contains no transcript excerpts, private infrastructure details, external
document text, or advisor-owned source code. No remote access or computation
was performed while preparing it.

## Coordinate Convention

The project coordinate and velocity convention is:

- $x$: streamwise direction, with velocity component $u$;
- $y$: spanwise direction, with velocity component $v$;
- $z$: wall-normal direction, with velocity component $w$.

The channel walls are therefore normal to $z$, and the statistically
homogeneous wall-parallel directions are $x$ and $y$.

## Confirmed Editable Code Areas

- In `main.f90`, the flag region around lines 69--74 contains the temperature,
  salinity, and melting flags.
- Salinity is disabled.
- Melting is disabled for the current Master Project.
- The first three lines of `module.f90` contain `nx`, `ny`, and `nz`.
- `input.inp` contains runtime and physical parameters.
- `IC.inp` controls the velocity and temperature initial conditions.

The exact confirmed spelling of the buoyancy-related variable remains open and
must be checked before any case is configured.

## Poseidon Workflow

- `poseidon.sh` compiles and runs the code on Poseidon.
- Approximately 128 points per direction is the practical maximum discussed
  for this workflow; it is a planning limit rather than a validated performance
  result.
- The previous $16^3$ attempt failed because of an unresolved setup or path
  issue. It did not produce a simulation result.

## Leonardo Workflow and Safety Rules

- Start from a clean copied folder and leave the clean source folder unchanged.
- Compile with `leo.sh`.
- Submit `go_leo.sh` through `sbatch`.
- Use one process per GPU.
- Do not perform computations on the login node.
- Do not use AI autopilot on the cluster.
- Obtain manual approval before every command that changes cluster state.

These points document the future workflow only. No cluster action was taken in
this documentation session.

## Nondimensional Channel Setup

With full wall-normal domain length $L_z$, the channel half-height is

\[
h=\frac{L_z}{2}.
\]

The friction velocity and friction Reynolds number are

\[
u_\tau=\sqrt{\frac{\tau_w}{\rho}},
\qquad
Re_\tau=\frac{u_\tau h}{\nu}.
\]

For $L_z=2$, $|\Pi|=1$, and $\rho=1$, the agreed normalization
gives

\[
h=1,
\qquad
\tau_w=1,
\qquad
u_\tau=1.
\]

It follows that

\[
\nu=\frac{1}{Re_\tau},
\qquad
\mu=\frac{1}{Re_\tau}
\]

when $\rho=1$, because $\mu=\rho\nu$.

## Time-Step Considerations

- Check the diffusion restriction using both viscosity and thermal
  diffusivity.
- Check the CFL restriction using the maximum velocity.
- Use the more restrictive time-step value and retain a safety margin.
- Base the spatial restriction on the smallest grid spacing, including the
  smallest spacing of the stretched wall-normal $z$ grid.

No numerical time step has yet been confirmed.

## Planned Master Project Benchmarks

| Stage | Planned parameters | Purpose |
| --- | --- | --- |
| Unstratified channel | $Re_\tau=590$ | Channel-flow validation |
| Passive scalar | $Re_\tau=550$, $Pr=1$ | Scalar/thermal validation without active buoyancy |
| Stable stratification | $Re_\tau=180$, $Pr=0.7$, $Ri_\tau=120$ | Active stable-stratification benchmark |

The supplementary document appears to use both $Re_\tau=550$ and
$Re_\tau=500$ for the passive-scalar benchmark. The intended value must be
confirmed before running; $Re_\tau=550$ is retained above as the current
planned value, not as a simulation result.

## Outstanding Items

- Obtain and adopt the official TU Wien thesis template.
- Confirm the final thesis title and complete TISS registration.
- Obtain the Kleandro thermal test input and post-processing scripts.
- Confirm the exact stable wall-temperature arrangement and gravity/sign
  convention.
- Obtain the exact Garcia-Villalba benchmark input and comparison data.
- Confirm the exact spelling of the buoyancy variable in the relevant
  code version.
