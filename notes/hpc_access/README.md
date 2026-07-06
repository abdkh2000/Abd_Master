# CINECA Leonardo HPC Access Notes

This note documents the local setup for CINECA Leonardo access. It intentionally avoids storing passwords, OTP secrets, recovery codes, private keys, advisor-host login details, or project-private credentials.

## Recommended Terminal

Use Windows PowerShell with the built-in OpenSSH client.

Reason: Windows OpenSSH is already installed, Git Bash is available but not needed, and WSL is not installed. CINECA's Windows instructions are written for PowerShell plus Smallstep.

## Installed / Configured

- Smallstep CLI (`step`) installed with Winget.
- Smallstep bootstrapped to CINECA's SSH certificate authority.
- Windows OpenSSH client already existed.
- A minimal local SSH alias `leonardo` was added to the user-level SSH config outside this repository.

No passwords or OTP values were saved.

## One-Time SSH Agent Setup

CINECA's certificate workflow needs the Windows OpenSSH Authentication Agent. If it is disabled, open PowerShell as Administrator and run:

```powershell
Set-Service -Name ssh-agent -StartupType Automatic
Start-Service -Name ssh-agent
Get-Service -Name ssh-agent
```

The final command should show `Running`.

## Renew / Generate the CINECA SSH Certificate

Certificates are temporary and normally valid for 12 hours. Generate a fresh one with:

```powershell
step ssh login <CINECA_SSO_EMAIL> --provisioner cineca-hpc
```

A browser window should open. Sign in with CINECA SSO and complete OTP/2FA. Do not save OTP codes or recovery codes in this repository.

Check whether a certificate is loaded:

```powershell
step ssh list
ssh-add -L
```

## Log In To Leonardo

Using the local SSH alias:

```powershell
ssh leonardo
```

Or without the alias:

```powershell
ssh <CINECA_USERNAME>@login.leonardo.cineca.it
```

## Check Budget / Account Access

After logging in to Leonardo, run safe account-check commands only, for example:

```bash
saldo -b <CINECA_USERNAME>
```

Do not run simulations or heavy computations on the login node.

## Advisor-Provided SSH Host

For the advisor-provided host, connect manually using the command provided privately by the advisor. Type the password interactively when prompted. Do not save the password in SSH config, scripts, terminal notes, Git, or this repository.

## What Not To Do On The Login Node

- Do not run simulations or heavy computations.
- Do not compile large jobs unless the advisor or system documentation says it is acceptable.
- Do not launch long-running processes directly on the login node.
- Do not store passwords, OTP secrets, recovery codes, private keys, or project-private login data in Git.
- Use the scheduler or advisor-approved workflow for real thesis simulations.

## Official Reference

CINECA access documentation: https://docs.hpc.cineca.it/general/access.html
