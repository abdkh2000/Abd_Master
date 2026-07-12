# BRINE Working Copy Tiny Edit Plan

Date: 2026-07-12

## Purpose

Inspect the BRINE working-copy edit files in read-only mode and prepare a sanitized tiny edit plan before any changes are made.

## Scope

- Clean baseline folder: `BRINE36`
- Working copy name: `BRINE36_abd_work_20260712_153935`
- Advisor-approved folder used: `[REDACTED_REMOTE_PATH]`
- Channel case folder: `[WORKING_COPY]/channel`

## Safety Status

- Working copy only: yes
- Clean baseline untouched: yes
- Files edited: no
- BRINE compiled: no
- BRINE run: no
- Jobs submitted: no
- Scripts executed: no
- Source copied into GitHub: no

## Baseline Comparison

The four working-copy edit files still match the clean baseline:

- `channel/input.inp` match baseline: yes
- `channel/IC.inp` match baseline: yes
- `channel/module.f90` match baseline: yes
- `channel/main.f90` match baseline: yes

## `module.f90` Edit Plan

Advisor instruction: only edit `nx`, `ny`, and `nz`.

Location map, without values or source lines:

- `nx`: line `2`, near beginning: yes
- `ny`: line `3`, near beginning: yes
- `nz`: line `4`, near beginning: yes

These look like grid-size parameters: yes.

Tiny grid values still need advisor confirmation before editing.

## `main.f90` Flag/Control Candidate Map

Exact buoyancy/thermal flag unambiguous: no.

Candidate identifiers and locations, without values or source lines:

- `restart`: lines `252`, `316`; likely restart control
- `temp`: line `333`; likely thermal or scalar control
- `theta`: lines `219`, `248`, `297-299`, `399`, `431`, `598-605`, `633-640`, `653`, `659-661`, `755`, `858`, `1174`; likely thermal or scalar control
- `rho`: lines `910-912`, `1050-1055`; likely buoyancy or density-related control
- `active`: line `855`; possible control candidate
- `enable`: lines `69`, `71`, `73`, `78`, `104`; possible control candidate
- `use`: lines `4-16`, `78`, `344`; possible control candidate, but may include ordinary Fortran module imports

Identifiers not found in `main.f90` during this keyword scan:

- `passive`
- `scalar`
- `buoy`
- `bouss`
- `density`
- `gravity`
- `flag`
- `switch`
- `mode`

## `input.inp` Planning Notes

Keyword locations only, without values:

- `restart`: line `1`
- `density`: line `11`
- `dt`: line `9`
- `time`: line `3`
- `theta`: not found
- `buoy`: not found
- `nx`: not found
- `ny`: not found
- `nz`: not found

## `IC.inp` Planning Notes

Keyword locations only, without values:

- `theta`: line `29`
- `strat`: not found
- `temp`: not found
- `restart`: not found
- `initial`: not found

## Proposed Tiny-Test Plan

1. Edit only files in the working copy.
2. Reduce grid size only through `nx`, `ny`, and `nz` in `module.f90`.
3. Adjust only advisor-approved flags in `main.f90`.
4. Keep `input.inp` and `IC.inp` changes minimal and documented.
5. Ask the advisor which build/run script to use before compiling or running.

## Open Questions

- What exact tiny grid values should be used for `nx`, `ny`, and `nz`?
- Which exact `main.f90` flag or control should be changed for the first tiny test?
- Does the first tiny test require any `input.inp` change?
- Does the first tiny test require any `IC.inp` change?
- Which script is approved for the first tiny test workflow?

## Recommended Next Step

Ask the advisor to confirm tiny-test settings, then create a patch plan for working-copy edits only. Do not compile or run until the build/run script and tiny-test workflow are confirmed.
