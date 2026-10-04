"""Normal-map Y-convention probe via the curl (integrability) test.

For a tangent-space normal field derived from a height map h(row, col):
  Y-up (OpenGL, green up):   nx = -dh/dcol, ny = +dh/drow  => d(nx)/drow = -d(ny)/dcol  -> correlation < 0
  Y-down (DirectX):          nx = -dh/dcol, ny = -dh/drow  => d(nx)/drow = +d(ny)/dcol  -> correlation > 0
Image rows are counted top-down as stored in the file.
"""
import sys
import numpy as np
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from ddsscan import load_rgba  # noqa: E402


def curl_corr(x, y):
    x = x.astype(np.float64) / 127.5 - 1.0
    y = y.astype(np.float64) / 127.5 - 1.0
    dx_drow = x[1:, :-1] - x[:-1, :-1]
    dy_dcol = y[:-1, 1:] - y[:-1, :-1]
    m = (np.abs(dx_drow) < 0.5) & (np.abs(dy_dcol) < 0.5)  # ignore UV-seam jumps
    a = dx_drow[m]
    b = dy_dcol[m]
    return float(np.corrcoef(a, b)[0, 1])


if __name__ == "__main__":
    for spec in sys.argv[1:]:
        path, xc, yc = spec.rsplit(":", 2)
        img = load_rgba(path)
        ci = "RGBA"
        c = curl_corr(img[..., ci.index(xc)], img[..., ci.index(yc)])
        verdict = "Y-up (OpenGL)" if c < 0 else "Y-down (DirectX)"
        print(f"{path.split('/')[-1]}  X={xc} Y={yc}  curl corr={c:+.3f}  -> {verdict} as stored")
