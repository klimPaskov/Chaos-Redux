"""Multi-scale Y-convention probe.

Test 1 (curl): corr(d nx/drow, d ny/dcol) after Gaussian smoothing; < 0 -> Y-up as stored.
Test 2 (diffuse cavity): with luminance L as a height proxy (cavities dark),
  sx = corr(nx, -dL/dcol), sy = corr(ny, +dL/drow).  Y-up as stored when sx and sy share a sign.
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from ddsscan import load_rgba  # noqa: E402


def blur(ch, s):
    if s == 0:
        return ch.astype(np.float64)
    from scipy.ndimage import gaussian_filter
    return gaussian_filter(ch.astype(np.float64), s)


def corr(a, b, m):
    return float(np.corrcoef(a[m], b[m])[0, 1])


def run(npath, xc, yc, dpath):
    img = load_rgba(npath)
    ci = "RGBA"
    xr = img[..., ci.index(xc)].astype(np.float64) / 127.5 - 1
    yr = img[..., ci.index(yc)].astype(np.float64) / 127.5 - 1
    d = load_rgba(dpath).astype(np.float64) if dpath else None
    out = []
    for s in (0, 1, 2, 4):
        x = blur(xr, s)
        y = blur(yr, s)
        dxr = x[1:, :-1] - x[:-1, :-1]
        dyc = y[:-1, 1:] - y[:-1, :-1]
        m = (np.abs(dxr) < 0.3) & (np.abs(dyc) < 0.3)
        c1 = corr(dxr, dyc, m)
        line = f"s={s} curl={c1:+.3f}"
        if d is not None:
            L = blur(0.299 * d[..., 0] + 0.587 * d[..., 1] + 0.114 * d[..., 2], s)
            dLc = L[:-1, 1:] - L[:-1, :-1]
            dLr = L[1:, :-1] - L[:-1, :-1]
            m2 = np.ones_like(dLc, dtype=bool)
            sx = corr(x[:-1, :-1], -dLc, m2)
            sy = corr(y[:-1, :-1], dLr, m2)
            line += f" lum sx={sx:+.3f} sy={sy:+.3f} ({'Y-up' if sx * sy > 0 else 'Y-down'})"
        out.append(line)
    print(npath.split("/")[-1], f"X={xc} Y={yc}")
    for line in out:
        print("   ", line)


if __name__ == "__main__":
    for spec in sys.argv[1:]:
        parts = spec.split("|")
        run(parts[0], parts[1], parts[2], parts[3] if len(parts) > 3 else None)
