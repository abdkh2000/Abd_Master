# Handwritten Notes Transcription

Date: 2026-06-30

Source material: handwritten note image provided by the user.

Sensitive data handling: the note refers to SSH and remote-machine work, but no private credentials are recorded here. If exact SSH login details, usernames, hostnames, IP addresses, private project IDs, or remote paths are needed later, keep them outside Git and use `[REDACTED]` in repository notes.

## Transcription

1. Learn basics of terminal.
   - Command Prompt or PowerShell.
   - Basics of navigating.
   - SSH.
   - `.ssh/config`.
   - Only work in the advisor-approved shared-machine project folder.
   - Keep the exact remote path outside Git.

2. Download/install VS Code extension:
   - `Remote - SSH`.

3. Get access to supercomputer.

4. Use the code.
   - Copy folder.
   - Make libraries.
   - Modify files.
   - Code/folder name appears to be something like `BRINE36`; verify exact name on the server.
   - Files mentioned:
     - `input.inp`
     - `ic.inp`
     - `module.F90`: likely where `nx`, `ny`, and `nz` are set.
     - `main.F90`: flags.

5. Theory.
   - Project: wall-bounded flows.
   - Pope, `Turbulent Flows`.
   - Kolmogorov scale.
   - Reynolds stresses.
   - Shear velocity / shear Reynolds number.
   - Basic statistics.
   - Kim and Moin.
   - Thermal stratification.

## Interpretation Notes

- The handwritten code name is not fully certain. Cross-check the exact folder name on the server before documenting commands.
- The sketch appears to represent a channel-flow setup and a stratified temperature profile.
- The project should differ from the passive-scalar reference by including buoyancy, stable thermal stratification, and internal gravity wave behavior.
