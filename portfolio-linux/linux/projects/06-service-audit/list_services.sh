#!/usr/bin/env bash
set -euo pipefail
command -v systemctl >/dev/null || { echo "systemctl unavailable" >&2; exit 1; }
systemctl list-units --type=service --state=running --no-pager
