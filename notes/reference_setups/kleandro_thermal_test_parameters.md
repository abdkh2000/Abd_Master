# Kleandro Thermal-Test Parameters Extracted from TUThesis.pdf

## Finding

The project PDF contains **two related working thermal/passive-scalar parameter sets**:

1. a fresh-start, one-million-step turbulent thermal validation run;
2. a longer Leonardo restart run used for extended post-processing.

They share the same physical channel setup but use different time steps, run intervals, output frequencies, and documented averaging windows.

## Common Physical Setup

- Solver case: incompressible turbulent plane channel with a passive scalar.
- Buoyancy: disabled; the scalar does not feed back into momentum.
- Coordinates:
  - \(x\): streamwise;
  - \(y\): spanwise;
  - \(z\): wall-normal.
- Velocity components:
  - \(u\): streamwise;
  - \(v\): spanwise;
  - \(w\): wall-normal.
- Physical walls: \(z=0\) and \(z=L_z\).
- Periodic directions: \(x\) and \(y\).
- Velocity wall condition: no slip/no penetration.
- Scalar wall conditions:
  - lower wall: \(\theta=+1\);
  - upper wall: \(\theta=-1\).
- Grid: \(N_x\times N_y\times N_z=256\times128\times200\).
- Domain: \(L_x\times L_y\times L_z=4\pi\times2\pi\times2\).
- Half-height: \(h=L_z/2=1\).
- Density normalization: \(\rho=1\).
- Constant pressure gradient: \(\partial p/\partial x=-1\).
- Friction velocity: \(u_\tau=1\).
- Friction Reynolds number: \(Re_\tau=150\).
- Kinematic viscosity: \(\nu=1/150\approx6.6667\times10^{-3}\).
- Thermal diffusivity: \(\kappa=\nu\).
- Prandtl number: \(Pr=\nu/\kappa=1\).
- Phase-field/ice module: inactive.

## Parameter Set A — Main One-Million-Step Validation

- Start mode: fresh start.
- Grid: \(256\times128\times200\).
- Domain: \(4\pi\times2\pi\times2\).
- \(\nu=1/150\).
- \(\kappa=1/150\).
- \(Pr=1\).
- Pressure gradient: \(-1\).
- Time step: \(\Delta t=3.0\times10^{-4}\).
- Final step: 1,000,000.
- Output interval: every 50,000 steps.
- Statistical window stated in the thesis: saved snapshots from step 50,000 through step 1,000,000, excluding step 0.
- Velocity benchmark: THTLab CH12_PG.WL7.
- Thermal comparison: THTLab CH122_PG.WL4, explicitly described as the closest available case rather than an exact twin.

## Parameter Set B — Extended Leonardo Run

- Restart calculation.
- Restart step: 4,000,000.
- Final step: 10,000,000.
- Grid: \(256\times128\times200\) physical points.
- Some stored/post-processed arrays may show 202 wall-normal locations because two ghost nodes are included.
- Domain: \(4\pi\times2\pi\times2\).
- Wall-normal stretching factor: \(\zeta=2.0\).
- \(\nu=6.6666667\times10^{-3}\).
- \(\kappa=6.6666667\times10^{-3}\).
- \(Pr=1\).
- Pressure gradient: \(-1\).
- Time step: \(\Delta t=5.0\times10^{-4}\).
- Output interval: every 100,000 steps.
- Final averaging window: steps 8,000,000 through 10,000,000.
- Wall scalar values: \(+1\) lower wall and \(-1\) upper wall.

## Post-Processing Conventions

- Plane averaging is performed over the homogeneous \(x\) and \(y\) directions.
- Time averaging is applied over the stated saved-snapshot window.
- One-point statistics were symmetrized about the channel centreline in the primary validation workflow.
- The solver uses \(w\) as wall-normal velocity.
- A reference using \(v\) as wall-normal must be remapped:
  - present \(v_{\mathrm{rms}}\) ↔ reference spanwise component;
  - present \(w_{\mathrm{rms}}\) ↔ reference wall-normal component;
  - present \(-\langle u'w'\rangle\) ↔ reference \(-\langle u'v'\rangle\).

## Reported Leonardo Comparison Metrics

- Mean velocity:
  - relative \(L_2\): 3.99%;
  - maximum relative difference: 4.68%.
- RMS velocity components:
  - \(u_{\mathrm{rms}}^+\): 6.66% relative \(L_2\);
  - \(v_{\mathrm{rms}}^+\): 9.96%;
  - \(w_{\mathrm{rms}}^+\): 9.06%.
- Reynolds shear stress:
  - relative \(L_2\): 8.20%;
  - maximum relative difference: 11.63%.
- Full-channel mean scalar shape:
  - maximum absolute difference: 0.081884;
  - \(L_2\) difference: 0.058024.
- Full-channel scalar RMS shape:
  - maximum absolute difference: 0.224848;
  - \(L_2\) difference: 0.109169.
- Wall-unit scalar RMS:
  - relative \(L_2\): 13.16%;
  - maximum relative difference: 21.27%.

## Important Caveats

- The thermal reference is not an exact twin case.
- The PDF does not provide every BRINE flag or input-line value, including the
  exact flag values, input-file line order, initial-condition selectors, or
  mixed-boundary-condition coefficients.
- The stretching factor for the fresh one-million-step run is not fully
  confirmed.
- The actual BRINE input files must still be checked before launching a new
  run.
- Do not choose between \(\Delta t=3\times10^{-4}\) and
  \(\Delta t=5\times10^{-4}\) without first determining whether the
  reproduction is a fresh run or a restart.
- The exact job-script settings are not fully specified.
