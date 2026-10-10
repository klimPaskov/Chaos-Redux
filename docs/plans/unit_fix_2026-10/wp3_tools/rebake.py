"""Re-project provider textures (sampled through the old Meshy UV) onto a new UV layout, per face by barycentric rasterisation.
Usage: python rebake.py bake.npz provider_textures_dir out_dir [size=1024] [ss=2]
Writes base_color.png, roughness.png, metallic.png, normal_xy.png (R=x,G=y,B=z in the NEW tangent frame), mask.png.
No colour or detail is invented: every texel is a bilinear sample of a provider texture at the exact surface point."""
import sys, json
from pathlib import Path
import numpy as np
from PIL import Image

def load(p, mode):
    return np.asarray(Image.open(p).convert(mode)).astype(np.float32)

def bilinear(img, uv):
    h, w = img.shape[:2]
    x = uv[:, 0] * w - 0.5; y = (1.0 - uv[:, 1]) * h - 0.5
    x0 = np.floor(x).astype(np.int64); y0 = np.floor(y).astype(np.int64)
    fx = (x - x0)[:, None]; fy = (y - y0)[:, None]
    x0c = np.clip(x0, 0, w - 1); x1c = np.clip(x0 + 1, 0, w - 1); y0c = np.clip(y0, 0, h - 1); y1c = np.clip(y0 + 1, 0, h - 1)
    a = img[y0c, x0c]; b = img[y0c, x1c]; c = img[y1c, x0c]; d = img[y1c, x1c]
    return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy

def frames(P, uv):
    """Orthonormal tangent frame (T, B, N) per face: T along +u, B along +v (v up), N = face normal."""
    e1 = P[:, 1] - P[:, 0]; e2 = P[:, 2] - P[:, 0]
    N = np.cross(e1, e2); N /= (np.linalg.norm(N, axis=1, keepdims=True) + 1e-20)
    du1 = uv[:, 1] - uv[:, 0]; du2 = uv[:, 2] - uv[:, 0]
    det = du1[:, 0] * du2[:, 1] - du1[:, 1] * du2[:, 0]
    det = np.where(np.abs(det) < 1e-14, 1e-14, det)
    r = 1.0 / det
    T = (e1 * du2[:, 1:2] - e2 * du1[:, 1:2]) * r[:, None]
    Bv = (e2 * du1[:, 0:1] - e1 * du2[:, 0:1]) * r[:, None]
    T -= N * (T * N).sum(1, keepdims=True); T /= (np.linalg.norm(T, axis=1, keepdims=True) + 1e-20)
    B = np.cross(N, T)
    sign = np.sign((B * Bv).sum(1)); sign[sign == 0] = 1
    B *= sign[:, None]
    return T, B, N, det

def main(npz, tex, out, size=1024, ss=2):
    d = np.load(npz)
    pos, uvo, uvn = d['pos'], d['uv_old'], d['uv_new']
    tex = Path(tex); out = Path(out); out.mkdir(parents=True, exist_ok=True)
    base = load(tex / 'base_color.png', 'RGB'); rough = load(tex / 'roughness.png', 'L')[..., None]
    metal = load(tex / 'metallic.png', 'L')[..., None]; normal = load(tex / 'normal.png', 'RGB')
    To, Bo, No, deto = frames(pos, uvo); Tn, Bn, Nn, detn = frames(pos, uvn)
    # rotation old->new in the face plane (x,y components)
    c11 = (To * Tn).sum(1); c12 = (Bo * Tn).sum(1); c21 = (To * Bn).sum(1); c22 = (Bo * Bn).sum(1)
    S = size * ss
    acc = np.zeros((S, S, 8), np.float32); cnt = np.zeros((S, S), np.int32)   # rgb(3) rough metal nx ny nz
    lab_map = np.full((S, S), 255, np.uint8); z_map = np.zeros((S, S), np.float32); labels = d['labels']
    valid_old = np.abs(deto) > 1e-12
    nf = len(pos)
    for f in range(nf):
        if not valid_old[f]: continue
        t = uvn[f] * S
        xmin = max(int(np.floor(t[:, 0].min())), 0); xmax = min(int(np.ceil(t[:, 0].max())), S - 1)
        ymin = max(int(np.floor(t[:, 1].min())), 0); ymax = min(int(np.ceil(t[:, 1].max())), S - 1)
        if xmax < xmin or ymax < ymin: continue
        xs, ys = np.meshgrid(np.arange(xmin, xmax + 1), np.arange(ymin, ymax + 1))
        px = xs.ravel() + 0.5; py = ys.ravel() + 0.5
        (x0, y0), (x1, y1), (x2, y2) = t
        den = (y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2)
        if abs(den) < 1e-12: continue
        l0 = ((y1 - y2) * (px - x2) + (x2 - x1) * (py - y2)) / den
        l1 = ((y2 - y0) * (px - x2) + (x0 - x2) * (py - y2)) / den
        l2 = 1 - l0 - l1
        eps = -0.02
        m = (l0 >= eps) & (l1 >= eps) & (l2 >= eps)
        if not m.any(): continue
        l = np.stack([l0[m], l1[m], l2[m]], 1)
        src = l @ uvo[f]
        c = bilinear(base, src); r = bilinear(rough, src); mt = bilinear(metal, src)
        nv = bilinear(normal, src) / 255.0 * 2 - 1
        nx = nv[:, 0] * c11[f] + nv[:, 1] * c21[f]; ny = nv[:, 0] * c12[f] + nv[:, 1] * c22[f]; nz = nv[:, 2]
        # c11 etc: components of old T/B along the new T/B; (x_new,y_new) = x*(To.Tn,To.Bn) + y*(Bo.Tn,Bo.Bn)
        nx = nv[:, 0] * c11[f] + nv[:, 1] * c12[f]; ny = nv[:, 0] * c21[f] + nv[:, 1] * c22[f]
        val = np.concatenate([c, r, mt, nx[:, None], ny[:, None], nz[:, None]], 1)
        ix = xs.ravel()[m]; iy = ys.ravel()[m]
        acc[iy, ix] += val; cnt[iy, ix] += 1
        lab_map[iy, ix] = labels[f]; z_map[iy, ix] = (l @ pos[f][:, 2])
    cov = cnt > 0
    avg = np.where(cov[..., None], acc / np.maximum(cnt, 1)[..., None], 0)
    # downsample supersampled (average over covered samples)
    def down(a, w):
        a = a.reshape(size, ss, size, ss, -1); w = w.reshape(size, ss, size, ss, 1)
        return (a * w).sum((1, 3)) / np.maximum(w.sum((1, 3)), 1e-6), w.sum((1, 3))[..., 0]
    wgt = cov.astype(np.float32)[..., None]
    low, wsum = down(avg, np.broadcast_to(wgt, avg.shape[:2] + (1,)).copy())
    mask = wsum > 0
    # image row 0 = top = v=1
    def save(name, arr, mode):
        Image.fromarray(np.clip(arr[::-1], 0, 255).astype(np.uint8), mode).save(out / name)
    save('base_color.png', low[..., 0:3], 'RGB'); save('roughness.png', low[..., 3], 'L'); save('metallic.png', low[..., 4], 'L')
    nxy = low[..., 5:8]; nrm = np.linalg.norm(nxy, axis=-1, keepdims=True) + 1e-9; nxy = nxy / nrm
    save('normal_xyz.png', (nxy * 0.5 + 0.5) * 255, 'RGB')
    save('mask.png', mask * 255, 'L')
    sub = lab_map.reshape(size, ss, size, ss)[:, 0, :, 0]; Image.fromarray(sub[::-1].copy(), 'L').save(out / 'label.png')
    np.save(out / 'zmap.npy', z_map.reshape(size, ss, size, ss)[:, 0, :, 0][::-1].copy())
    print(json.dumps(dict(size=size, coverage=float(mask.mean()), faces=int(nf), skipped_noUV=int((~valid_old).sum()))))

if __name__ == '__main__':
    a = sys.argv
    main(a[1], a[2], a[3], int(a[4]) if len(a) > 4 else 1024, int(a[5]) if len(a) > 5 else 2)
