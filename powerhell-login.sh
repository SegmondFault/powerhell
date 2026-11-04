# Start Powerhell once for explicitly enabled interactive SSH users.

case $- in
    *i*) ;;
    *) return 0 ;;
esac

[ -n "${SSH_TTY:-}" ] || return 0
[ -z "${POWERHELL_EGG_SHOWN:-}" ] || return 0
[ -r /etc/powerhell-users ] || return 0
/usr/bin/grep -Fxq -- "${USER:-}" /etc/powerhell-users || return 0

export POWERHELL_EGG_SHOWN=1
/usr/bin/python3 /usr/local/lib/powerhell/powerhell.py
