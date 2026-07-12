# Recovery Audit After Theory Commit

Date: 2026-07-12

Anchor commit: `6e9e2d7311789a4cdf50f7e017522799a71e9280`

## Purpose

Recover and document any safe project work completed after the turbulent channel-flow theory-note commit, without repeating remote BRINE work, overwriting local changes, or copying private/proprietary material into GitHub.

## Local Repository Audit

Safe local checks performed:

- `git status`
- `git diff`
- `git diff --cached`
- `git log --oneline -10`
- untracked-file check
- local-only commit check against `origin/main`

Audit result before this recovery documentation was created:

- Uncommitted tracked changes: no
- Staged changes: no
- Untracked repository files: no
- Local commits not on `origin/main`: no
- Remote commits missing locally: no

## Later Work Recovered

The safe BRINE and access work visible in the repository was already committed before the anchor theory-note commit. The relevant committed records are:

- Leonardo smoke-test logs
- advisor SSH alias setup note
- BRINE discovery retry note
- BRINE script workflow inventory
- advisor edit map
- BRINE working-copy setup note
- BRINE working-copy tiny edit plan
- BRINE tiny-grid test attempt note
- BRINE tiny-grid log diagnosis note
- turbulent channel-flow theory note

No additional uncommitted safe Markdown file or local-only commit was found after the anchor commit during this audit.

## Generated Local Helper Files

Local helper and sanitized result files were found outside the repository workspace. They were not committed directly because they are working artifacts, not project notes.

Audit conclusion:

- The helper/result files that matched the BRINE investigation predated the anchor commit.
- Their safe findings are already represented in committed Markdown notes.
- No post-anchor helper output requiring recovery into Git was found.

## Remote BRINE Working Copy Record

The advisor-owned source code was not copied into GitHub. The sanitized repository record shows:

- Clean baseline folder: `BRINE36`
- Working copy name: `BRINE36_abd_work_20260712_153935`
- Advisor-approved folder: `[REDACTED_REMOTE_PATH]`
- Clean baseline remained untouched: yes
- Source copied into GitHub: no
- Raw scripts, Makefiles, logs, and source lines copied into GitHub: no

Files changed only on the remote working copy:

- `[WORKING_COPY]/channel/module.f90`

Purpose of the remote working-copy change:

- Reduce the grid dimensions for a tiny workflow test.
- Leave `input.inp`, `IC.inp`, and `main.f90` unchanged for that first attempt.

Compile/run result recorded from sanitized metadata:

- Script attempted: `poseidon.sh`
- Jobs submitted: no
- Exit code: `132`
- Refined error category: `missing_file`
- Likely failing phase: `setup`
- Next required technical step: inspect or fix the working-copy path/reference privately, or ask the advisor which script should be used before rerunning.

## Remote Recheck Status

A read-only metadata recheck through `advisor-machine` was attempted without password entry. The alias required interactive authentication from this session, so no new remote metadata was collected during the recovery audit.

No password, username, host, IP address, exact remote path, SSH configuration, raw log, or source content was recorded.

## Buoyancy Keyword Scan Reconciliation

The first BRINE discovery note reported no keyword results because the advisor-approved work directory was not accessible and the keyword scan did not run.

The reliable scans are the later accessible notes:

- `2026-07-12_brine_discovery_retry.md`
- `2026-07-12_brine_script_workflow_inventory.md`
- `2026-07-12_advisor_edit_map.md`

Reason: those scans were run after the approved folder was accessible and after the expected BRINE files were found. They show buoyancy/temperature-related keywords by filename only. Therefore, the current project status is:

- Buoyancy/temperature keyword files found: yes
- Exact buoyancy or thermal-stratification control flag: not yet confirmed

## Current Status

- CINECA/UserDB account and 2FA setup are treated as complete because Leonardo authentication and Slurm smoke testing succeeded.
- Project access is treated as complete because a controlled Slurm smoke job was accepted and completed.
- Advisor SSH alias setup is complete locally and remains outside Git.
- BRINE clean baseline name is known as `BRINE36`.
- BRINE working copy exists according to committed sanitized notes.
- First tiny-grid attempt has been diagnosed as a setup/missing-file issue, not a validated BRINE physics run.

## Remaining Problems

- The correct script/path setup for the BRINE working copy still needs advisor-safe clarification.
- The exact buoyancy or thermal-stratification control flag is still not confirmed.
- No BRINE rerun should happen until the working-copy path/reference issue is fixed privately.
- No thesis-scale run should happen until the approved Slurm workflow and account/project handling are confirmed outside Git.

## Next Actions

- Keep `BRINE36` untouched.
- Keep all edits in a separate working copy.
- Privately resolve the `poseidon.sh` working-copy path/reference issue or ask the advisor which script to use.
- Confirm the exact buoyancy/temperature control flag before changing physics behavior.
- Do not copy proprietary BRINE source, scripts, Makefiles, raw logs, usernames, hosts, project IDs, or exact remote paths into GitHub.
