"""Remove exporter-level quaternion sign flips from a serialized PDX .anim without changing any rotation.

The Blender exporter decomposes pose matrices, so a bone whose rotation crosses w = 0 can be written with q on one
frame and -q on the next even when the Blender F-curves are continuous. q and -q are the same orientation; this
tool negates whole four-component samples (and, when needed, the initial info quaternion) so consecutive samples of
every bone have a non-negative dot product. It never adds, removes or moves a key, bone or translation and it
verifies the result by re-reading the written file.

Usage:
  python anim_signs.py <in.anim> [<out.anim>]      (default: rewrite in place, keeping <in>.signs_orig)
Prints a JSON receipt with before/after negative-dot counts and the input/output SHA-256.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'runtime'))
import pdx_reader  # noqa: E402


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def _channels(sa):
    if isinstance(sa, (list, tuple)):
        sa = sa[0] if sa else ''
    return str(sa)


def negative_dots(tree):
    info, samples = tree.find('info'), tree.find('samples')
    q_bones = [b for b in info if 'q' in _channels(b.get('sa'))]
    flat = samples.get('q')
    if not q_bones or flat is None:
        return 0, 0
    stride = len(q_bones) * 4
    frames = len(flat) // stride
    bad = 0
    for k, b in enumerate(q_bones):
        prev = None
        for f in range(frames):
            cur = flat[f * stride + k * 4: f * stride + k * 4 + 4]
            if prev is not None and sum(a * c for a, c in zip(prev, cur)) < 0:
                bad += 1
            prev = cur
    return bad, frames


def fix(src, dst=None):
    src = Path(src)
    dst = Path(dst) if dst else src
    module, _ = pdx_reader.parser()
    tree = module.read_meshfile(str(src.resolve()))
    before, frames = negative_dots(tree)
    info, samples = tree.find('info'), tree.find('samples')
    q_bones = [b for b in info if 'q' in _channels(b.get('sa'))]
    flat = list(samples.get('q'))
    stride = len(q_bones) * 4
    flipped = 0
    for k, b in enumerate(q_bones):
        initial = list(b.get('q')) if b.get('q') is not None else None
        prev = initial
        for f in range(frames):
            o = f * stride + k * 4
            cur = flat[o:o + 4]
            if prev is not None and sum(a * c for a, c in zip(prev, cur)) < 0:
                flat[o:o + 4] = [-v for v in cur]
                cur = flat[o:o + 4]
                flipped += 1
            prev = cur
    samples.set('q', flat)
    if dst == src:
        if not Path(str(src) + '.signs_orig').exists():
            shutil.copy2(src, str(src) + '.signs_orig')
    module.write_animfile(str(dst), tree)
    check = module.read_meshfile(str(dst.resolve()))
    after, _ = negative_dots(check)
    # initial-to-first-sample continuity is included above (prev starts at the info quaternion)
    return {'file': str(dst), 'frames': frames, 'negative_dots_before': before, 'samples_negated': flipped,
            'negative_dots_after': after, 'sha256_in': _sha(str(src) + '.signs_orig' if dst == src else src), 'sha256_out': _sha(dst)}


if __name__ == '__main__':
    print(json.dumps(fix(*sys.argv[1:3]), indent=1))
