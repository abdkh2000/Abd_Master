# BRINE Script Workflow Inventory

Date: 2026-07-12

## Purpose

Inspect BRINE build and run workflow metadata safely, without running, compiling, submitting, copying, or modifying BRINE.

## Remote Status

- Remote connection status: yes
- Advisor-approved folder used: `[REDACTED_REMOTE_PATH]`
- Advisor-approved folder accessible: yes
- BRINE baseline folder: `BRINE36`
- Channel case folder: `BRINE36/channel`

## Script Inventory

| Script | Executable | Shebang | Likely Role | `sbatch` | `srun` | MPI run | Modules | Make/CMake | Compiler/MPI keywords | CUDA/GPU keywords | Slurm directives | Slurm option names | Absolute path refs | Leonardo/Poseidon refs |
|---|---:|---:|---|---:|---:|---:|---:|---:|---|---|---:|---|---:|---:|
| `BRINE36/channel/binder.sh` | yes | yes | mapping/helper | no | no | no | no | no | none | none | no | none | no | no |
| `BRINE36/channel/go_leo.sh` | yes | yes | slurm_submit | yes | no | yes | yes | no | none | `gpu`, `cuDecomp` | yes | `job-name`, `qos`, `account`, `nodes`, `cpus-per-task`, `time`, `gres`, `output`, `error` | no | no |
| `BRINE36/channel/leo.sh` | yes | no | leonardo_run | no | no | no | yes | yes | none | none | no | none | no | yes |
| `BRINE36/channel/local.sh` | yes | no | local_run | no | no | yes | no | yes | `nvc` | `cuda`, `cuDecomp` | no | none | yes | no |
| `BRINE36/channel/poseidon.sh` | yes | no | poseidon_run | no | no | yes | no | yes | `nvc` | `cuda`, `cuDecomp` | no | none | yes | yes |
| `BRINE36/channel/restart_local.sh` | yes | no | restart | no | no | yes | no | no | `nvc` | `cuDecomp` | no | none | yes | no |
| `BRINE36/channel/testpush.sh` | yes | no | unknown | no | no | no | no | yes | none | none | no | none | no | no |
| `BRINE36/clean_lib.sh` | yes | no | cleanup | no | no | no | no | no | none | `cuDecomp` | no | none | no | no |
| `BRINE36/make_lib_git.sh` | yes | no | library_build | no | no | no | no | yes | none | `cuDecomp` | no | none | yes | no |
| `BRINE36/make_lib_leo.sh` | yes | no | library_build | no | no | no | yes | yes | none | `cuDecomp` | no | none | yes | no |
| `BRINE36/make_lib_local.sh` | yes | no | library_build | no | no | no | no | yes | `nvc` | `cuda`, `cuDecomp` | no | none | yes | no |
| `BRINE36/make_lib_mn5.sh` | yes | no | library_build | no | no | no | yes | yes | none | `cuDecomp`, `nccl` | no | none | yes | no |
| `BRINE36/make_lib_poseidon.sh` | yes | no | library_build | no | no | no | no | yes | `nvc` | `cuda`, `cuDecomp` | no | none | yes | yes |

## Makefile Summary

| Makefile | Target Names | Compiler/MPI Keywords | CUDA/GPU Keywords | Absolute Path Refs |
|---|---|---|---|---:|
| `BRINE36/channel/Makefile` | `clean`, `.f90.o`, `.SUFFIXES` | `mpif90`, `nvc` | `cuda`, `gpu`, `cuDecomp` | yes |

No Makefile recipes or command lines were copied into this repository.

## Likely Script Roles

- Leonardo-related scripts: `BRINE36/channel/go_leo.sh`, `BRINE36/channel/leo.sh`
- Poseidon-related scripts: `BRINE36/channel/poseidon.sh`, `BRINE36/make_lib_poseidon.sh`
- Local-related scripts: `BRINE36/channel/local.sh`, `BRINE36/channel/restart_local.sh`, `BRINE36/make_lib_local.sh`
- Library-build scripts: `BRINE36/make_lib_git.sh`, `BRINE36/make_lib_leo.sh`, `BRINE36/make_lib_local.sh`, `BRINE36/make_lib_mn5.sh`, `BRINE36/make_lib_poseidon.sh`
- Cleanup script: `BRINE36/clean_lib.sh`
- Mapping/helper script: `BRINE36/channel/binder.sh`
- Likely job-submit script: `BRINE36/channel/go_leo.sh`
- Unknown or needs advisor clarification: `BRINE36/channel/testpush.sh`

## Control-File Keyword Locations

| File | Exists | Keywords Present |
|---|---:|---|
| `BRINE36/channel/input.inp` | yes | `nz`, `dt`, `time`, `restart`, `buoy`, `theta`, `density` |
| `BRINE36/channel/IC.inp` | yes | `strat`, `temp`, `theta` |
| `BRINE36/channel/module.f90` | yes | `nx`, `ny`, `nz`, `dt`, `time`, `restart`, `temp`, `theta`, `scalar`, `rho` |
| `BRINE36/channel/main.f90` | yes | `nx`, `ny`, `nz`, `dt`, `time`, `restart`, `buoy`, `temp`, `theta`, `rho` |
| `BRINE36/channel/readinput.f90` | yes | `nx`, `ny`, `nz`, `dt`, `time`, `restart`, `temp`, `theta`, `rho` |
| `BRINE36/channel/initialize.f90` | yes | `nx`, `ny`, `nz`, `restart`, `strat`, `temp`, `theta` |

Only keyword presence by filename was recorded. No matching source lines, variable values, script contents, Makefile recipes, raw terminal output, or absolute paths were copied.

## Safety Result

- BRINE run: no
- BRINE compiled: no
- Slurm jobs submitted: no
- Clean source modified: no
- Source copied into GitHub: no
- Remote files copied into this repository: no

## Open Questions For Advisor

- Which script is approved for the first tiny test after a working copy is made?
- Should `BRINE36/channel/go_leo.sh` be treated as the Leonardo Slurm submission script?
- Should `BRINE36/make_lib_leo.sh` be used for library setup on Leonardo, and only after creating a working copy?
- Are absolute path references inside local, Poseidon, and library scripts expected to be edited in the working copy?
- What account/project setting should be handled privately outside Git for any future Slurm submission?
- Should `testpush.sh` be ignored for thesis workflow purposes?

## Recommended Next Step

Ask the advisor which script is approved for the first tiny test, keep `BRINE36` untouched, create a separate working copy only after script roles are reviewed, inspect selected script details locally or remotely without copying raw source into GitHub, and do not compile or run until the advisor confirms the workflow.
