#!/usr/bin/env bash
# A vendored temat szinkronizalja a forkbol (forrashiteles repo):
#   https://gitlab.com/bozsikarmand/hugo-theme-armands-blog
# Minden tema-modositas ELOBB a forkba menjen (kulon repo), utana ez a script.
set -euo pipefail
cd "$(dirname "$0")/.."
TMP=$(mktemp -d)
git clone --depth 1 https://gitlab.com/bozsikarmand/hugo-theme-armands-blog.git "$TMP/theme"
rsync -a --delete --exclude '.git' "$TMP/theme/" themes/armands-blog/
rm -rf "$TMP"
echo "OK - theme synced from fork. Commit: git add themes/armands-blog && git commit -m 'Sync theme from fork'"
