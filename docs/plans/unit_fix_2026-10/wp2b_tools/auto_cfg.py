"""python auto_cfg.py <bake_dir> <out cfg.json> <cloth_target> <skin_target> [normal_strength]"""
import sys, json, numpy as np
from PIL import Image
d=sys.argv[1]
rgb=np.asarray(Image.open(d+"/base_color.png").convert("RGB")).astype(float); m=np.asarray(Image.open(d+"/mask.png"))>0
L=0.299*rgb[...,0]+0.587*rgb[...,1]+0.114*rgb[...,2]
warm=(rgb[...,0]-rgb[...,2])/np.maximum(rgb[...,0],1)
Lm=L[m]; p50=np.percentile(Lm,50); p65=np.percentile(Lm,65)
cl=m&(L<p50); sk=m&(L>p65)&(warm>0.2)
def ratio(sel):
    if sel.sum()<100: sel=m
    c=rgb[sel].mean(0); l=0.299*c[0]+0.587*c[1]+0.114*c[2]; r=c/l; return [round(float(x),3) for x in r]
cfg={"skin_parts_extra":["l_foot","r_foot"],"cloth_target":float(sys.argv[3]),"skin_target":float(sys.argv[4]),"cloth_ratio":ratio(cl),"skin_ratio":ratio(sk),
 "cloth_mix":0.55,"skin_mix":0.6,"skin_luma":float(round(np.percentile(Lm,55))),"detail_gain":1.5,"skin_detail_gain":1.3,"normal_strength":float(sys.argv[5]) if len(sys.argv)>5 else 1.3}
json.dump(cfg,open(sys.argv[2],"w")); print(cfg)
