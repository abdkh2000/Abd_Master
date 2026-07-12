# BRINE Tiny Grid Test Attempt

Date: 2026-07-12

## Purpose

Create a reversible tiny-grid test in the BRINE working copy and make one minimal compile/run workflow attempt without touching the clean baseline.

## Scope

- Clean baseline: `BRINE36`
- Working copy: `BRINE36_abd_work_20260712_153935`
- Advisor-approved folder used: `[REDACTED_REMOTE_PATH]`
- Channel case folder: `[WORKING_COPY]/channel`

## Pre-Edit Safety Check

Before editing, the four editable working-copy files still matched the clean baseline:

- `input.inp` match baseline: yes
- `IC.inp` match baseline: yes
- `module.f90` match baseline: yes
- `main.f90` match baseline: yes

Backup created: yes

## Tiny Grid Edit

Edited files:

- `module.f90`: yes
- `input.inp`: no
- `IC.inp`: no
- `main.f90`: no

Tiny grid test values used:

- `nx = 16`
- `ny = 16`
- `nz = 16`

Post-edit verification:

- `module.f90` changed relative to baseline: yes
- `input.inp` unchanged relative to baseline: yes
- `IC.inp` unchanged relative to baseline: yes
- `main.f90` unchanged relative to baseline: yes
- Only `module.f90` was edited among the four advisor edit files: yes

## Shell Syntax Checks

| Script | Exists | `bash -n` |
|---|---:|---:|
| `channel/local.sh` | yes | pass |
| `channel/poseidon.sh` | yes | pass |
| `channel/go_leo.sh` | yes | pass |
| `channel/leo.sh` | yes | pass |
| `make_lib_poseidon.sh` | yes | pass |
| `make_lib_leo.sh` | yes | pass |

## Compile/Run Attempt Summary

- Script attempted: `poseidon.sh`
- Attempt limit: `10m`
- Compile started: yes
- Run started: yes
- Completed within timeout: yes
- Exit code: `132`
- Obvious error category: `path_issue`
- Raw remote log stored: yes
- Raw remote log path committed: no
- Raw remote log content committed: no

## Safety Result

- Clean baseline modified: no
- Source copied into GitHub: no
- Raw source lines committed: no
- Raw terminal output committed: no
- Old variable values committed: no
- Jobs submitted: no
- Leonardo Slurm script used: no
- Scripts executed: yes, exactly one timed working-copy `poseidon.sh` attempt

## Next Step

Because the attempt completed with `path_issue`, inspect the remote log privately and summarize only the error category or missing private setup detail. After that, either fix the working-copy path/setup issue or ask the advisor which script is approved for the first tiny test. In parallel, start theory notes on channel turbulence and buoyancy.
