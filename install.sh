#!/bin/sh

set -eu

if [ "$(id -u)" -ne 0 ]; then
    echo "Run this installer with sudo." >&2
    exit 1
fi

if [ "$#" -eq 0 ]; then
    echo "Usage: sudo ./install.sh USER [USER ...]" >&2
    exit 2
fi

for account in "$@"; do
    case "$account" in
        ''|*[!a-zA-Z0-9_-]*)
            echo "Invalid account name: $account" >&2
            exit 2
            ;;
    esac

    if ! id "$account" >/dev/null 2>&1; then
        echo "Account does not exist: $account" >&2
        exit 2
    fi
done

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
users_file=$(mktemp)
trap 'rm -f "$users_file"' EXIT HUP INT TERM

printf '%s\n' "$@" | sort -u >"$users_file"

install -d -o root -g root -m 0755 /usr/local/lib/powerhell
install -o root -g root -m 0755 "$script_dir/powerhell.py" \
    /usr/local/lib/powerhell/powerhell.py
install -o root -g root -m 0644 "$script_dir/powerhell-login.sh" \
    /etc/profile.d/99-powerhell.sh
install -o root -g root -m 0644 "$users_file" /etc/powerhell-users

echo "Powerhell enabled for: $(tr '\n' ' ' </etc/powerhell-users)"
echo "It will appear on each account's next interactive SSH login."
