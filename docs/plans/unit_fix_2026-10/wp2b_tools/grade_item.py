"""python grade_item.py <bake_dir> <cfg.json> <out_dir>
cfg: {"luma_target": 70, "normal_strength": 1.2, "rules": [{"class":"steel","s_max":0.25,"v_min":0.2}, ...], "default":"leather"}
Provider colour is only re-toned by a global per-item curve; classes come from colour rules; specular uses the vanilla-calibrated recipes."""
import sys, json, colorsys
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
import grade as G
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'.tools/3d_pipeline'))
from textures.conventions import build_pdx_specular_from_provider, gate_specular

def main(bake, cfgp, out):
    cfg=json.load(open(cfgp)); bake=Path(bake); out=Path(out); out.mkdir(parents=True, exist_ok=True)
    rgb=np.asarray(Image.open(bake/'base_color.png')).astype(np.float32); mask=np.asarray(Image.open(bake/'mask.png'))>0
    rough=np.asarray(Image.open(bake/'roughness.png')).astype(np.float32); metal=np.asarray(Image.open(bake/'metallic.png')).astype(np.float32)
    nxyz=np.asarray(Image.open(bake/'normal_xyz.png')).astype(np.float32)/255*2-1
    L=G.luma(rgb); low=G.norm_blur(L,mask,cfg.get('detail_sigma',4.0)); detail=L-low
    if cfg.get('compress'):
        kn,kr=cfg['compress']; Lc=np.where(low>kn,kn+(low-kn)*kr,low)+detail*cfg.get('detail_gain',1.0)
    else:
        med=np.median(L[mask]); g=np.log(cfg['luma_target']/255)/np.log(max(med,1)/255)
        Lc=255*np.power(np.clip(low,1,255)/255,g)+detail*cfg.get('detail_gain',1.4)
    ratio=rgb/np.maximum(L,1.0)[...,None]
    out_rgb=np.clip(ratio*np.clip(Lc,4,250)[...,None],0,255)
    # classes
    mx=rgb.max(-1)/255; mn=rgb.min(-1)/255; sat=(mx-mn)/np.maximum(mx,1e-3)
    hue=np.zeros_like(mx)
    r,gc,b=rgb[...,0]/255,rgb[...,1]/255,rgb[...,2]/255
    d=np.maximum(mx-mn,1e-6)
    hue=np.where(mx==r,((gc-b)/d)%6,np.where(mx==gc,(b-r)/d+2,(r-gc)/d+4))*60
    cls=np.full(L.shape,cfg.get('default','leather'),dtype=object)
    done=np.zeros(L.shape,bool)
    for rule in cfg['rules']:
        m=mask&~done
        if 's_max' in rule: m&=sat<=rule['s_max']
        if 's_min' in rule: m&=sat>=rule['s_min']
        if 'v_min' in rule: m&=mx>=rule['v_min']
        if 'v_max' in rule: m&=mx<=rule['v_max']
        if 'h_min' in rule: m&=hue>=rule['h_min']
        if 'h_max' in rule: m&=hue<=rule['h_max']
        m=ndi.binary_opening(m,iterations=1)|(m&ndi.binary_closing(m,iterations=2))
        m&=~done
        cls[m]=rule['class']; done|=m
    names=sorted(set([r['class'] for r in cfg['rules']]+[cfg.get('default','leather')]))
    masks={n:(mask&(cls==n)) for n in names}
    # smooth class regions: majority filter
    for n in names: masks[n]=ndi.gaussian_filter(masks[n].astype(np.float32),1.0)>0.5
    # make exclusive and complete
    claimed=np.zeros(L.shape,bool)
    for n in names:
        masks[n]&=~claimed; claimed|=masks[n]
    masks[cfg.get('default','leather')]|=mask&~claimed
    def im(m): return Image.fromarray((m*255).astype(np.uint8),'L')
    mi={n:im(v) for n,v in masks.items() if v.any()}
    occ=im(mask)
    spec,rep=build_pdx_specular_from_provider(Image.fromarray(rough.astype(np.uint8),'L'),Image.fromarray(metal.astype(np.uint8),'L') if cfg.get('use_metal') else Image.fromarray((metal*0).astype(np.uint8),'L'),mi,occ)
    gate=gate_specular(spec,occ,mi)
    s=cfg.get('normal_strength',1.2); nx=nxyz[...,0]*s; ny=nxyz[...,1]*s; nz=np.sqrt(np.clip(1-nx**2-ny**2,0,1))
    X=np.clip((nx*0.5+0.5)*255,0,255); Y=np.clip((ny*0.5+0.5)*255,0,255)
    pdxn=np.stack([X,X,np.zeros_like(X),Y],-1); pdxn[~mask]=(128,128,0,128)
    Image.fromarray(np.where(mask[...,None],out_rgb,0).astype(np.uint8),'RGB').save(out/'diffuse.png')
    spec.save(out/'specular.png'); Image.fromarray(pdxn.astype(np.uint8),'RGBA').save(out/'normal.png'); occ.save(out/'occupancy.png')
    for k,v in mi.items(): v.save(out/f'class_{k}.png')
    L2=G.luma(out_rgb); sp=np.asarray(spec)
    print(json.dumps(dict(classes={k:int(v.sum()) for k,v in masks.items()},luma_p50=float(np.percentile(L2[mask],50)),spec_gate=gate['status'],spec_failures=gate['failures'],
        normal_G_std=float(X[mask].std()),normal_A_std=float(Y[mask].std()),spec_A_mean=float(sp[...,3][mask].mean())),indent=1))
if __name__=='__main__': main(*sys.argv[1:4])
