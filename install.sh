
#!/data/data/com.termux/files/usr/bin/bash
set -eu

DIR="$(cd "$(dirname "$0")" && pwd)"
DEST="$PREFIX/bin/fvk"

if [ ! -f "$DIR/fvk.py" ]; then
    echo "Error: fvk.py not found."
    exit 1
fi

pkg install python -y
cp "$DIR/fvk.py" "$DEST"
chmod 755 "$DEST"

echo "FVK installed successfully!"
echo "Type fvk to start."
