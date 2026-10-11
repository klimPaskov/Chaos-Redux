"""Grade re-baked provider maps into PDX diffuse / specular / normal plus class masks.
Usage: python grade.py <bake_dir> <config.json> <out_dir>
Nothing is synthesised: colour is the provider colour re-toned by a global per-class tone curve, local detail is the provider's own
high-pass, roughness/metalness/normal come straight from the bake. Class masks come from geometry (part label, world height) and colour."""
import sys, json
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

PARTS = ['head','l_arm','l_foot','l_hand','l_leg','r_arm','r_foot','r_hand','r_leg','torso']

def luma(a): return 0.299*a[...,0]+0.587*a[...,1]+0.114*a[...,2]

def norm_blur(x, m, sigma):
    w = ndi.gaussian_filter(m.astype(np.float32), sigma)
    if x.ndim == 3:
        return np.stack([ndi.gaussian_filter(x[...,c]*m, sigma) for c in range(x.shape[-1])], -1)/np.maximum(w, 1e-4)[...,None]
    return ndi.gaussian_filter(x*m, sigma)/np.maximum(w, 1e-4)

def smooth(x, a, b): 
    t = np.clip((x-a)/(b-a), 0, 1); return t*t*(3-2*t)

def retone(rgb, L_out, ratio_target, mix):
    L = np.maximum(luma(rgb), 1.0)
    ratio = rgb/L[...,None]
    r2 = ratio*(1-mix) + np.array(ratio_target)*mix
    r2 = r2/np.maximum(luma(r2), 1e-4)[...,None]
    return r2*L_out[...,None]

def main(bake, cfgp, out):
    cfg = json.load(open(cfgp)); bake = Path(bake); out = Path(out); out.mkdir(parents=True, exist_ok=True)
    rgb = np.asarray(Image.open(bake/'base_color.png')).astype(np.float32)
    mask = np.asarray(Image.open(bake/'mask.png')) > 0
    lab = np.asarray(Image.open(bake/'label.png')); z = np.load(bake/'zmap.npy')
    rough = np.asarray(Image.open(bake/'roughness.png')).astype(np.float32)
    metal = np.asarray(Image.open(bake/'metallic.png')).astype(np.float32)
    nxyz = np.asarray(Image.open(bake/'normal_xyz.png')).astype(np.float32)/255*2-1
    part = np.full(lab.shape, '', dtype=object)
    L = luma(rgb)
    warm = (rgb[...,0]-rgb[...,2])/np.maximum(rgb[...,0], 1)
    pid = {n:i for i,n in enumerate(cfg.get('parts', PARTS))}
    def isp(*names):
        m = np.zeros(lab.shape, bool)
        for n in names: m |= (lab == pid[n])
        return m
    helmet_z = cfg.get('helmet_z', 1e9)
    head = isp('head'); hands = isp('l_hand','r_hand')
    extra = isp(*cfg.get('skin_parts_extra', [])) if cfg.get('skin_parts_extra') else np.zeros(lab.shape, bool)
    hair = head & (L < cfg.get('hair_luma', 0))
    skin_hard = ((head & (z < helmet_z) & ~hair) | hands | extra)
    thr = cfg.get('skin_luma', 85)
    bright_warm = smooth(L, thr, thr+25) * smooth(warm, 0.18, 0.28)
    other = isp('l_arm','r_arm','torso','l_leg','r_leg','l_foot','r_foot') & ~skin_hard
    skin_soft = np.where(skin_hard, 1.0, np.where(other, bright_warm*cfg.get('other_skin', 1.0), 0.0))
    skin_soft = ndi.gaussian_filter(skin_soft.astype(np.float32), 1.2)*mask
    skin = skin_soft > 0.5
    wet = np.zeros(lab.shape, bool)
    if cfg.get('wet_parts'):
        wet = isp(*cfg['wet_parts']) & (L > cfg.get('wet_luma', 60)) & mask
        skin &= ~wet; skin_soft = skin_soft * (~wet)
    steel = (head & (z >= helmet_z) & ~skin) if 'helmet_z' in cfg else np.zeros(lab.shape, bool)
    leather = np.zeros(lab.shape, bool)
    if 'boot_z' in cfg: leather = isp('l_foot','r_foot') & (z < cfg['boot_z']) & ~skin
    cloth = mask & ~skin & ~steel & ~leather & ~wet
    # --- tone
    cl_med = np.median(L[cloth]); sk_med = np.median(L[skin]) if skin.any() else cl_med
    sigma = cfg.get('detail_sigma', 5.0)
    low = norm_blur(L, mask, sigma); detail = L - low
    def curve(Lv, med, target):
        g = np.log(target/255)/np.log(max(med,1)/255)
        return 255*np.power(np.clip(Lv,1,255)/255, g)
    Lc = curve(low, cl_med, cfg['cloth_target']) + detail*cfg.get('detail_gain', 1.5)
    Ls = curve(low, sk_med, cfg['skin_target']) + detail*cfg.get('skin_detail_gain', 1.3)
    cl_rgb = retone(rgb, np.clip(Lc, 4, 250), cfg['cloth_ratio'], cfg.get('cloth_mix', 0.7))
    sk_rgb = retone(rgb, np.clip(Ls, 4, 250), cfg['skin_ratio'], cfg.get('skin_mix', 0.8))
    out_rgb = cl_rgb*(1-skin_soft[...,None]) + sk_rgb*skin_soft[...,None]
    if steel.any():
        Lh = curve(low, np.median(L[steel]), cfg.get('steel_target', 62)) + detail*cfg.get('detail_gain', 1.5)
        st_rgb = retone(rgb, np.clip(Lh, 4, 250), cfg.get('steel_ratio', (0.98,1.0,0.94)), 0.6)
        out_rgb = np.where(steel[...,None], st_rgb, out_rgb)
    if wet.any():
        Lw = curve(low, np.median(L[wet]), cfg.get('wet_target', 100)) + detail*cfg.get('skin_detail_gain', 1.3)
        w_rgb = retone(rgb, np.clip(Lw, 4, 250), cfg.get('wet_ratio', (1.06,0.9,0.96)), cfg.get('wet_mix', 0.85))
        out_rgb = np.where(wet[...,None], w_rgb, out_rgb)
    if cfg.get('keep_gain'):
        out_rgb = rgb*cfg['keep_gain']
    if cfg.get('compress'):
        Lm = np.maximum(luma(rgb), 1.0); kn, kr = cfg['compress']
        Lo = np.where(Lm > kn, kn + (Lm-kn)*kr, Lm)
        out_rgb = rgb/Lm[...,None]*Lo[...,None]
    if cfg.get('keep_median'):
        Lm = np.maximum(luma(rgb), 1.0); med_ = float(np.median(Lm[mask]))
        gam = np.log(cfg['keep_median']/255.0)/np.log(med_/255.0)
        Lo = 255.0*np.power(np.clip(Lm, 1, 255)/255.0, gam)
        kn = cfg.get('knee', 140.0); kr = cfg.get('knee_ratio', 0.4)
        Lo = np.where(Lo > kn, kn + (Lo-kn)*kr, Lo)
        out_rgb = rgb/Lm[...,None]*Lo[...,None]
    out_rgb = np.clip(out_rgb, 0, 255)
    # --- specular via vanilla-calibrated classes
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'.tools/3d_pipeline'))
    from textures.conventions import build_pdx_specular_from_provider, gate_specular, MATERIAL_RECIPES
    S = rgb.shape[0]
    def im(m): return Image.fromarray((m*255).astype(np.uint8), 'L')
    cm = {'matte_cloth': cloth, 'dry_skin': skin, 'steel': steel}
    if wet.any(): cm['skin'] = wet
    if leather.any(): cm['leather'] = leather
    masks_img = {k: im(v) for k, v in cm.items()}
    occ = im(mask)
    spec, rep = build_pdx_specular_from_provider(Image.fromarray(rough.astype(np.uint8),'L'),
        Image.fromarray((metal*0).astype(np.uint8),'L'), masks_img, occ)
    gate = gate_specular(spec, occ, masks_img)
    # --- normal in PDX RRxG: R=G=x, A=y, B=0
    strength = cfg.get('normal_strength', 1.0)
    nx = nxyz[...,0]*strength; ny = nxyz[...,1]*strength; nz = np.sqrt(np.clip(1-nx**2-ny**2, 0, 1))
    nrm = np.stack([nx, ny, nz], -1)
    X = np.clip((nx*0.5+0.5)*255, 0, 255); Y = np.clip((ny*0.5+0.5)*255, 0, 255)
    pdxn = np.stack([X, X, np.zeros_like(X), Y], -1)
    pdxn[~mask] = (128,128,0,128)
    # outputs
    Image.fromarray(np.where(mask[...,None], out_rgb, 0).astype(np.uint8), 'RGB').save(out/'diffuse.png')
    spec.save(out/'specular.png'); Image.fromarray(pdxn.astype(np.uint8), 'RGBA').save(out/'normal.png')
    occ.save(out/'occupancy.png')
    for k, v in masks_img.items(): v.save(out/f'class_{k}.png')
    om = mask
    def st(x): return dict(mean=float(x.mean()), std=float(x.std()), p5=float(np.percentile(x,5)), p50=float(np.percentile(x,50)), p95=float(np.percentile(x,95)))
    L2 = luma(out_rgb)
    nt = np.arccos(np.clip(nz[om],0,1))
    rep2 = dict(coverage=float(om.mean()), classes={k:int(v.sum()) for k,v in cm.items()},
        diffuse_luma=st(L2[om]), diffuse_luma_cloth=st(L2[cloth]), diffuse_luma_skin=st(L2[skin]) if skin.any() else None,
        in_luma_median=dict(cloth=float(cl_med), skin=float(sk_med)),
        normal_G_std=float(X[om].std()), normal_A_std=float(Y[om].std()), mean_tangent_tilt=float(np.sin(nt).mean()),
        spec_gate=gate['status'], spec_failures=gate['failures'], spec_A_mean=float(np.asarray(spec)[...,3][om].mean()), spec_G_mean=float(np.asarray(spec)[...,1][om].mean()),
        spec_A_p95=float(np.percentile(np.asarray(spec)[...,3][om],95)))
    json.dump(rep2, open(out/'grade_report.json','w'), indent=1)
    print(json.dumps(rep2, indent=1))

if __name__ == '__main__':
    main(*sys.argv[1:4])
