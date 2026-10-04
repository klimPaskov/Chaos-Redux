"""Read-only DDS header and channel statistics scanner (scratch evidence tool)."""
import hashlib
import struct
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def header(path):
    b = Path(path).read_bytes()[:148]
    assert b[:4] == b"DDS ", path
    size, flags, h, w, pitch, depth, mips = struct.unpack_from("<7I", b, 4)
    pf_size, pf_flags, fourcc, bits, rm, gm, bm, am = struct.unpack_from("<2I4s5I", b, 76)
    caps1, caps2 = struct.unpack_from("<2I", b, 108)
    dx10 = None
    if fourcc == b"DX10":
        dx10 = struct.unpack_from("<I", b, 128)[0]
    return dict(w=w, h=h, mips=mips, flags=hex(flags), pf_flags=hex(pf_flags), fourcc=fourcc.decode("latin1"), bits=bits,
                masks=(hex(rm), hex(gm), hex(bm), hex(am)), caps1=hex(caps1), dx10=dx10)


def load_rgba(path):
    hd = header(path)
    if hd["fourcc"].strip("\0") == "" and hd["bits"] == 32:
        raw = Path(path).read_bytes()[128:128 + hd["w"] * hd["h"] * 4]
        a = np.frombuffer(raw, dtype=np.uint8).reshape(hd["h"], hd["w"], 4)
        masks = [int(m, 16) for m in hd["masks"]]
        order = {0x00FF0000: 2, 0x0000FF00: 1, 0x000000FF: 0, 0xFF000000: 3}
        # channel index in byte order for each of R,G,B,A
        idx = [order[m] if m in order else None for m in masks]
        out = np.zeros_like(a)
        for c, i in enumerate(idx):
            out[..., c] = a[..., i] if i is not None else 255
        return out
    img = Image.open(path)
    img.load()
    return np.asarray(img.convert("RGBA"))


def stats(path):
    a = load_rgba(path).astype(np.float64)
    res = []
    for c in range(4):
        ch = a[..., c]
        res.append((ch.mean(), ch.std(), np.percentile(ch, 1), np.percentile(ch, 99)))
    return res


if __name__ == "__main__":
    for p in sys.argv[1:]:
        try:
            hd = header(p)
            st = stats(p)
            sha = hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
            print(Path(p).name, f"{hd['w']}x{hd['h']} mips={hd['mips']} fourcc={hd['fourcc']!r} bits={hd['bits']} masks={hd['masks']} pf={hd['pf_flags']} dx10={hd['dx10']}")
            print("   mean RGBA", tuple(round(s[0], 1) for s in st), " std", tuple(round(s[1], 1) for s in st))
            print("   p1..p99 ", tuple(f"{s[2]:.0f}-{s[3]:.0f}" for s in st), " sha", sha[:16])
        except Exception as e:  # noqa
            print(Path(p).name, "ERROR", e)
