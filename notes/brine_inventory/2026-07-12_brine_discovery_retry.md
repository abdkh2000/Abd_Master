# BRINE Discovery Retry Notes

Date: 2026-07-12

## Purpose

Retry sanitized BRINE discovery after confirming that the advisor-approved remote work directory is accessible.

## Remote Status

- Remote connection status: yes
- Advisor-approved folder used: `[REDACTED_REMOTE_PATH]`
- Advisor-approved folder accessible: yes
- BRINE run: no
- BRINE compiled: no
- Slurm jobs submitted: no
- Clean BRINE source modified: no
- BRINE source copied into GitHub: no

## Candidate BRINE Folders

Candidate folders or relative paths found:

- `BRINE36`
- `BRINE36/channel`
- `BRINE36/post/dropcount_channel`
- `BRINE36/post/flow_stats_channel`
- `BRINE36/post/paraview_channel`
- `BRINE36/post/temp_stats_channel`
- `BRINE36/cuDecomp/build`
- `BRINE36/cuDecomp/docs`
- `BRINE36/cuDecomp/utils`
- `BRINE36/post/compute_diss_hit`
- `BRINE36/post/dropcount_hit`
- `BRINE36/post/paraview_hit`
- `BRINE36/post/unionfind_hit`

Most likely clean baseline folder: `BRINE36`

Most likely channel-flow case folder: `BRINE36/channel`

## Expected Files Found

- `input.inp`: yes
- `ic.inp`: no exact lowercase match; `IC.inp` was found in `BRINE36/channel`
- `module.F90`: no exact uppercase-extension match; `module.f90` was found in `BRINE36/channel`
- `main.F90`: no exact uppercase-extension match; `main.f90` was found in `BRINE36/channel`

## Build And Run Scripts

Build and run script names found:

- `binder.sh`
- `bind.sh`
- `clean_lib.sh`
- `compile.sh`
- `dgxa100_map.sh`
- `dgxh100_map.sh`
- `go_leo.sh`
- `go.sh`
- `leonardo_map.sh`
- `leo.sh`
- `local.sh`
- `make_lib_git.sh`
- `make_lib_leo.sh`
- `make_lib_local.sh`
- `make_lib_mn5.sh`
- `make_lib_poseidon.sh`
- `marconi100_map.sh`
- `pm_map.sh`
- `poseidon.sh`
- `restart_local.sh`
- `runleo.sh`
- `sbatcher.sh`
- `summit_map.sh`
- `testpush.sh`

Makefile or makefile found: yes

## Relative Folder Structure Summary

Short relative structure observed:

- `BRINE36`
- `BRINE36/channel`
- `BRINE36/channel/output`
- `BRINE36/cuDecomp`
- `BRINE36/cuDecomp/benchmark`
- `BRINE36/cuDecomp/build`
- `BRINE36/cuDecomp/cmake`
- `BRINE36/cuDecomp/docs`
- `BRINE36/cuDecomp/examples`
- `BRINE36/cuDecomp/include`
- `BRINE36/cuDecomp/src`
- `BRINE36/cuDecomp/tests`
- `BRINE36/cuDecomp/utils`
- `BRINE36/jupyter_notebooks`
- `BRINE36/post`
- `BRINE36/post/compute_diss_hit`
- `BRINE36/post/dropcount_channel`
- `BRINE36/post/dropcount_hit`
- `BRINE36/post/flow_stats_channel`
- `BRINE36/post/paraview_channel`
- `BRINE36/post/paraview_hit`
- `BRINE36/post/temp_stats_channel`
- `BRINE36/post/unionfind_hit`

## Buoyancy/Temperature Keyword Search Summary

Buoyancy-related keyword files found: yes

Keyword summary by filename only:

- `buoy`: `BRINE36/channel/input.inp`, `BRINE36/channel/main.f90`
- `strat`: `BRINE36/channel/IC.inp`, `BRINE36/channel/initialize.f90`
- `temp`: `BRINE36/channel/IC.inp`, `BRINE36/channel/initialize.f90`, `BRINE36/channel/main.f90`, `BRINE36/channel/module.f90`, `BRINE36/channel/readinput.f90`, `BRINE36/channel/readwrite.f90`, `BRINE36/post/temp_stats_channel/read_fields.f90`
- `theta`: `BRINE36/channel/IC.inp`, `BRINE36/channel/initialize.f90`, `BRINE36/channel/input.inp`, `BRINE36/channel/main.f90`, `BRINE36/channel/module.f90`, `BRINE36/channel/readinput.f90`, `BRINE36/channel/readwrite.f90`, `BRINE36/post/paraview_channel/input_par.inp`, `BRINE36/post/paraview_channel/main.f90`, `BRINE36/post/paraview_channel/module.f90`, `BRINE36/post/paraview_channel/read_fields.f90`, `BRINE36/post/temp_stats_channel/module.f90`, `BRINE36/post/temp_stats_channel/read_fields.f90`
- `scalar`: `BRINE36/channel/module.f90`
- `density`: `BRINE36/channel/input.inp`
- `rho`: `BRINE36/channel/main.f90`, `BRINE36/channel/module.f90`, `BRINE36/channel/readinput.f90`

No raw source-code lines were copied into this repository.

## Open Questions

- Should `BRINE36` be treated as the untouched clean baseline?
- Is `BRINE36/channel` the intended starting case for the thesis workflow?
- Which script should be used only for library setup after creating a working copy?
- Which script should be used for the first tiny scheduler test after the workflow is reviewed?
- Should the filename case variants `IC.inp`, `module.f90`, and `main.f90` be used exactly as found?
- Which buoyancy or temperature flag should be inspected first in the working copy?

## Recommended Next Step

Keep one untouched clean BRINE copy, make a separate working copy for a tiny test, review build/run scripts before compiling, do not run on a login node, and do not copy source code into GitHub.
