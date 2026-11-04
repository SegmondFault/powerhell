#!/bin/sh

set -eu

if [ "$(id -u)" -ne 0 ]; then
    echo "Run this uninstaller with sudo." >&2
    exit 1
fi

rm -f /etc/profile.d/99-powerhell.sh
rm -f /etc/powerhell-users
rm -f /usr/local/lib/powerhell/powerhell.py
rmdir /usr/local/lib/powerhell 2>/dev/null || true

echo "Powerhell removed."
