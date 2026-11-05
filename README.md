# Powerhell

Software defined hijinks: MS-DOS login-shell that briefly convinces someone they
have SSHed into 1994.

Powerhell presents a tiny DOS-like prompt at the start of selected users'
interactive SSH sessions. `EXIT`, Ctrl-C, or Ctrl-D returns them to their real
Linux shell. Non-interactive SSH commands, Git, SCP, SFTP, and automation are
left alone.

## What it does

- Imitates an MS-DOS 6.22 prompt.
- Supports `DIR`, `CD`, `CLS`, `TYPE`, `VER`, `HELP`, and `EXIT`.
- Shows a totally trustworthy loading sequence on exit.
- Runs once per interactive SSH login for explicitly selected accounts.
- Never asks for a password or alters the user's files.

The DOS commands operate with the logged-in user's ordinary filesystem
permissions. Powerhell grants no additional access.

## Requirements

- Linux with `/etc/profile.d`
- Python 3
- Root access for installation

## Install

Clone the repository, then name the local accounts that should receive the
prank:

```sh
sudo ./install.sh alice bob
```

The account list is stored in `/etc/powerhell-users`. Running the installer
again replaces that list.

## Customise the exit

Edit `EXIT_STAGES`, `EXIT_ERROR`, and `EXIT_MESSAGE` near the top of
`powerhell.py`, then run the installer again.

## Remove

```sh
sudo ./uninstall.sh
```

## Sensible mischief

Keep the prank obvious and reversible. Do not add password prompts, claims of
real data loss, destructive commands, or anything that could be mistaken for
a genuine security incident.

Powerhell is not affiliated with or endorsed by Microsoft or GitHub.

## License

MIT
