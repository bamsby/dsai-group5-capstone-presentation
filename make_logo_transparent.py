"""Make black background of Operva AI logo transparent."""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow not installed. Run: pip install Pillow")
    raise SystemExit(1)

SRC = Path(__file__).parent / "operva_ai logo white.png"
DST = Path(__file__).parent / "operva_ai_logo_white_transparent.png"
# Pixels darker than this are treated as background and made transparent
BLACK_THRESHOLD = 40

def main():
    img = Image.open(SRC)
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    for item in data:
        r, g, b, a = item
        # Treat near-black pixels as background
        if r <= BLACK_THRESHOLD and g <= BLACK_THRESHOLD and b <= BLACK_THRESHOLD:
            new_data.append((r, g, b, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(DST, "PNG")
    print(f"Saved: {DST}")

if __name__ == "__main__":
    main()
