# BRINE Discovery Notes

Date: 2026-07-12

## Purpose

Safely inspect the BRINE code location and workflow on the advisor remote system without running, compiling, copying, or modifying BRINE.

## Remote Status

- Remote connection status: yes
- Advisor-approved folder used: `[REDACTED_REMOTE_PATH]`
- Advisor-approved folder accessible: no
- BRINE run: no
- BRINE compiled: no
- Slurm jobs submitted: no
- Clean BRINE source modified: no
- BRINE source copied into GitHub: no

## Candidate BRINE Folders

- Candidate BRINE folder found: no
- Candidate folder names or relative paths: none
- Most likely clean baseline folder: unknown

## Expected Files Found

- `input.inp`: no
- `ic.inp`: no
- `module.F90`: no
- `main.F90`: no

## Build And Run Scripts

- Makefile or makefile found: no
- Shell scripts found: none

## Relative Folder Structure Summary

No folder structure was recorded because the advisor-approved remote work directory was not accessible from the checked session.

## Buoyancy/Temperature Keyword Search Summary

- Keyword search ran: no
- Buoyancy-related keyword files found: no
- Keywords planned for the next accessible inspection: `buoy`, `bouss`, `strat`, `temp`, `theta`, `scalar`, `gravity`, `density`, `rho`

## Sanitized Failure

The advisor SSH alias resolved and the remote connection worked, but the entered advisor-approved remote work directory was not accessible from that login session.

Sanitized failure label: `workdir_not_accessible`

## Open Questions For Advisor

- What exact advisor-approved remote work directory should be used for BRINE inspection?
- Is VPN required for all advisor-machine sessions?
- Which BRINE folder should be treated as the untouched clean baseline?
- Which working-copy location should be used for tiny tests after discovery succeeds?
- Which build and run scripts are safe to inspect first?

## Recommended Next Step

Confirm the advisor-approved remote work directory, then repeat sanitized BRINE discovery. After discovery succeeds, keep one untouched clean BRINE copy, make a separate working copy for a tiny test, review build/run scripts before compiling, do not run on a login node, and do not copy source code into GitHub.
