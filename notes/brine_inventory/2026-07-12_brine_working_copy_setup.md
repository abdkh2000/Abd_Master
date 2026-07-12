# BRINE Working Copy Setup

Date: 2026-07-12

## Purpose

Create one separate remote working copy of `BRINE36` for future safe inspection and edits, while keeping the clean `BRINE36` baseline untouched.

## Remote Status

- Remote connection status: yes
- Advisor-approved folder used: `[REDACTED_REMOTE_PATH]`
- Advisor-approved folder accessible: yes
- Clean baseline folder: `BRINE36`
- Clean baseline exists after copy: yes
- Working copy name: `BRINE36_abd_work_20260712_153935`

## Copy Method

- Copy method: `rsync`
- `rsync` available: yes
- Copy created: yes
- No raw file list was copied into this repository.
- No source code was copied into this repository.

Exclusions used:

- `channel/output/*`
- `*/output/*`
- `*.out`
- `*.err`
- `*.log`
- `cuDecomp/build/*`

Output/build artifacts excluded: yes

## Expected Working-Copy Files Present

- `channel/input.inp`: yes
- `channel/IC.inp`: yes
- `channel/module.f90`: yes
- `channel/main.f90`: yes

## Expected Working-Copy Scripts Present

- `channel/go_leo.sh`: yes
- `make_lib_leo.sh`: yes

## Safety Result

- Clean baseline modified: no
- Files edited: no
- BRINE compiled: no
- BRINE run: no
- Jobs submitted: no
- BRINE `.sh` scripts executed: no
- Source copied into GitHub: no
- Remote files copied into this repository: no

## Recommended Next Step

Inspect selected working-copy files before edits, prepare a tiny grid/flag edit plan, ask the advisor which script is approved for the first tiny test, and do not compile or run until the workflow is confirmed.
