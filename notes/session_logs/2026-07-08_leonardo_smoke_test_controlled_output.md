# Leonardo Controlled-Output Slurm Smoke Test Log

Date: 2026-07-08

## Purpose

Repeat the Leonardo Slurm smoke test with an explicitly controlled output directory.

## Reason

The previous smoke job was accepted by Slurm and later reported as completed with exit code `0:0`, but the expected stdout/stderr files were not found in the checked folder.

## Authentication

- Authentication used the existing Smallstep SSH certificate flow.
- No passwords, OTP codes, private keys, real usernames, private hostnames, private IP addresses, exact remote paths, CINECA project/account IDs, SSH config contents, raw job IDs, or raw scheduler paths were written to this repository.
- Placeholders used: `[REDACTED_USER]`, `[REDACTED_HOST]`, `[REDACTED_REMOTE_PATH]`, and `[JOB_ID]`.

## Commands Run

Local checks:

- `git status`
- `git log -3 --oneline`

Remote connection:

- `ssh [REDACTED_HOST] "bash -s"`

Remote login-node checks:

- `hostname`
- `whoami`
- `pwd`
- `echo "$HOME"`
- `echo "$WORK"`
- `echo "$SCRATCH"`
- `squeue -u "$USER"`
- `sinfo -s`

Remote controlled-output smoke test:

- Checked for an existing pending/running `abd_smoke` job.
- Created a fresh timestamped smoke-test folder under `[REDACTED_REMOTE_PATH]`.
- Created an explicit Slurm output folder under `[REDACTED_REMOTE_PATH]`.
- Created `smoke_job.sh`.
- Submitted one tiny Slurm job with `sbatch`.
- Used explicit Slurm output and error targets:
  - `smoke_[JOB_ID].out`
  - `smoke_[JOB_ID].err`
- Waited for the job to leave the queue.
- Checked Slurm accounting with `sacct`.
- Checked for the controlled stdout/stderr files.
- Checked whether the stdout file contained `Smoke test finished`.

## Sanitized Results

- Remote script ran: yes
- Login-node hostname check: yes
- User check: yes
- Working-directory check: yes
- `$HOME` set: yes
- `$WORK` set: yes
- `$SCRATCH` set: yes
- `squeue` check: yes
- `sinfo` check: yes
- Existing `abd_smoke` job before submission: no
- Submitted new job: yes
- `sbatch` worked: yes
- Job final queue state: left_queue
- `sacct` sanitized state/exit/elapsed: `COMPLETED|0:0|00:00:06`
- Controlled output directory worked: yes
- Output file created: yes
- Error file created: yes
- Smoke finished line present: yes
- Output filename placeholder: `smoke_[JOB_ID].out`
- Error filename placeholder: `smoke_[JOB_ID].err`

## Sanitized Failure

None.

## Next Step

Now that the controlled-output Slurm smoke test succeeded, the next safe step is to inspect the BRINE location and workflow on the remote system without running BRINE on a login node and without copying external BRINE source code into this GitHub repository.
