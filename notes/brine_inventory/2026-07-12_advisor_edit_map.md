# Advisor BRINE Edit Map

Date: 2026-07-12

## Purpose

Connect the advisor-provided BRINE edit list to the actual discovered Linux filenames and record safe edit-point locations without copying source code, variable values, raw terminal output, or exact remote paths.

## Advisor-Provided File List

- `input.inp`
- `ic.inp`
- `module.fgo`: advisor said only change `nx`, `ny`, `nz`
- `main.fgo`: advisor said only flags

## Actual Discovered Filename Mapping

- `input.inp` -> `BRINE36/channel/input.inp`
- `ic.inp` -> `BRINE36/channel/IC.inp`
- `module.fgo` -> interpreted as `BRINE36/channel/module.f90`
- `main.fgo` -> interpreted as `BRINE36/channel/main.f90`

Case-sensitivity warning: use `IC.inp` exactly on Linux.

Extension warning: `fgo` is treated as likely shorthand or typo for `f90`; do not rename files.

## Advisor Instruction Summary

- `module.f90`: only `nx`, `ny`, `nz`
- `main.f90`: only flags or control switches
- Do not edit the clean `BRINE36` baseline directly.

## Remote Status

- Remote connection status: yes
- Advisor-approved folder used: `[REDACTED_REMOTE_PATH]`
- Advisor-approved folder accessible: yes
- Channel folder present: yes

## File Confirmation

- `BRINE36/channel/input.inp`: yes
- `BRINE36/channel/IC.inp`: yes
- `BRINE36/channel/module.f90`: yes
- `BRINE36/channel/main.f90`: yes

## Read-Only Location Map

### `input.inp`

Likely purpose: runtime/input control file for parameters such as restart, density, time, and time-step related controls.

Keyword presence only:

- `restart`: yes
- `buoy`: no
- `theta`: no
- `density`: yes
- `dt`: yes
- `time`: yes
- `nx`: no
- `ny`: no
- `nz`: no

### `IC.inp`

Likely purpose: initial-condition input file.

Keyword presence only:

- `strat`: no
- `temp`: no
- `theta`: yes
- `initial`: no
- `restart`: no

### `module.f90`

Advisor edit area: `nx`, `ny`, `nz` only.

Identifier locations, without values or source lines:

- `nx`: found, line `2`
- `ny`: found, line `3`
- `nz`: found, line `4`

These appear to be compile-time or grid-size parameters: yes.

### `main.f90`

Advisor edit area: flags or control switches only.

Keyword and identifier locations, without values or source lines:

- `flag`: not found
- `flags`: not found
- `restart`: lines `252`, `316`
- `buoy`: not found
- `bouss`: not found
- `strat`: not found
- `temp`: line `333`
- `theta`: lines `219`, `248`, `297-299`, `399`, `431`, `598-605`, `633-640`, `653`, `659-661`, `755`, `858`, `1174`
- `scalar`: not found
- `gravity`: not found
- `density`: not found
- `rho`: lines `910-912`, `1050-1055`
- `active`: line `855`
- `passive`: not found

Likely purpose from names only:

- `restart`: restart control
- `temp`, `theta`: thermal or scalar controls
- `rho`: buoyancy or density-related control
- `active`: control flag or activation marker

## Safety Result

- BRINE run: no
- BRINE compiled: no
- Jobs submitted: no
- BRINE `.sh` scripts executed: no
- Clean source modified: no
- Source copied into GitHub: no
- Raw source lines copied: no
- Variable values copied: no

## Recommended Next Step

Create a separate working copy before any edit, do not touch the clean `BRINE36` baseline, ask the advisor or confirm which tiny-test script/workflow to use, and only then edit the working-copy versions of `module.f90`, `main.f90`, `input.inp`, and `IC.inp`.
