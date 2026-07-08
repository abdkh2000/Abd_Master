# Leonardo Slurm Smoke Test Log

Date: 2026-07-08

## Purpose

Run a minimal Leonardo Slurm smoke test to confirm login, environment checks, and scheduler access before any BRINE inspection or simulation work.

## Security Handling

- Authentication used the existing Smallstep SSH certificate flow.
- No passwords, OTP codes, private keys, real usernames, private hostnames, private IP addresses, exact remote paths, project/account IDs, SSH config contents, or raw scheduler paths were written to this repository.
- Remote usernames, hostnames, job IDs, and paths are represented only with placeholders such as `[REDACTED_USER]`, `[REDACTED_HOST]`, `[REDACTED_REMOTE_PATH]`, and `[JOB_ID]`.

## Commands Run

Local checks:

- `git status`
- `git log -3 --oneline`

Remote connection:

- `ssh [REDACTED_HOST_ALIAS] "bash -s"`

Remote login-node checks:

- `hostname`
- `whoami`
- `pwd`
- `echo "$HOME"`
- `echo "$WORK"`
- `echo "$SCRATCH"`
- `squeue -u "$USER"`
- `sinfo -s`

Remote smoke-test setup and submission:

- Created a timestamped smoke-test folder under `[REDACTED_REMOTE_PATH]`.
- Created `smoke_job.sh`.
- Submitted the job with `sbatch --parsable smoke_job.sh`.
- Checked the queue with `squeue`.
- Checked accounting with `sacct`.
- Checked for `smoke_[JOB_ID].out` and `smoke_[JOB_ID].err`.

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
- Existing `abd_smoke` job in queue before submission: no
- `sbatch` worked: yes
- Job final queue state from the submission script: left_queue
- Accounting follow-up: `COMPLETED|0:0|00:00:06`
- Output file created in the expected smoke-test folder: no
- Error file created in the expected smoke-test folder: no
- Smoke finished line present: no
- Output filename placeholder: `smoke_[JOB_ID].out`
- Error filename placeholder: `smoke_[JOB_ID].err`

## Sanitized Failure

The scheduler accepted the smoke job and accounting later reported a completed job with exit code `0:0`, but the expected stdout/stderr files were not found in the checked smoke-test folder. Because the repository must not store raw job IDs or remote paths, the output-file lookup was kept sanitized.

Sanitized failure label: `output_files_not_created_after_followup`

## Next Recommended Step

Before inspecting or running BRINE, repeat the Slurm smoke test with an explicitly controlled output directory on Leonardo and confirm that `smoke_[JOB_ID].out` contains `Smoke test finished`. Do not run BRINE on a login node, and do not copy BRINE source code into this GitHub repository.
