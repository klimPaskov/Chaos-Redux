from pathlib import Path
from PIL import Image
import hashlib,json
ROOT=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
ASSETS=[
 ('livens_projector_single_tube_v1','source_png/livens_projector_single_tube_v1.png','processed_png/livens_projector_single_tube_v1_94x45.png',(94,45)),
 ('livens_projector_framed_battery_v1','source_png/livens_projector_framed_battery_v1.png','processed_png/livens_projector_framed_battery_v1_94x45.png',(94,45)),
 ('livens_projector_carriage_battery_v1','source_png/livens_projector_carriage_battery_v1.png','processed_png/livens_projector_carriage_battery_v1_94x45.png',(94,45)),
 ('zombie_cure_bomb_equipment_v1','source_png/zombie_cure_bomb_equipment_v1.png','processed_png/zombie_cure_bomb_equipment_v1_131x52.png',(131,52)),
]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bbox(alpha,t):return alpha.point(lambda a:255 if a>=t else 0).getbbox()
def alpha_stats(im):
 a=im.getchannel('A');v=list(a.getdata());return {'min':min(v),'max':max(v),'transparent':sum(x==0 for x in v),'partial':sum(0<x<255 for x in v),'opaque':sum(x==255 for x in v),'bbox_gt_0':a.getbbox(),'bbox_ge_16':bbox(a,16)}
reports=[]
for cid,src_rel,out_rel,target in ASSETS:
 src=ROOT/src_rel;out=ROOT/out_rel
 if not src.is_file():raise FileNotFoundError(src)
 if out.exists():raise FileExistsError(out)
 raw=Image.open(src).convert('RGBA');alpha=raw.getchannel('A');b=bbox(alpha,8)
 if b is None:raise ValueError(f'no native-alpha content {src}')
 pad=max(8,round(max(raw.size)*.008));x0,y0,x1,y1=b;crop_box=(max(0,x0-pad),max(0,y0-pad),min(raw.width,x1+pad),min(raw.height,y1+pad));crop=raw.crop(crop_box)
 margin=2;max_w,max_h=target[0]-2*margin,target[1]-2*margin;scale=min(max_w/crop.width,max_h/crop.height);size=(max(1,round(crop.width*scale)),max(1,round(crop.height*scale)))
 resized=crop.convert('RGBa').resize(size,Image.Resampling.LANCZOS).convert('RGBA');canvas=Image.new('RGBA',target,(0,0,0,0));offset=((target[0]-size[0])//2,(target[1]-size[1])//2);canvas.alpha_composite(resized,offset);out.parent.mkdir(parents=True,exist_ok=True);canvas.save(out,format='PNG',optimize=True)
 reports.append({'candidate_id':cid,'source_path':src.as_posix(),'source_sha256':sha(src),'source_size':list(raw.size),'source_alpha':alpha_stats(raw),'source_bbox_alpha_ge_8':b,'source_crop_padding_px':pad,'source_crop_box':crop_box,'target_size':list(target),'resized_subject_size':list(size),'offset':offset,'processed_path':out.as_posix(),'processed_sha256':sha(out),'processed_alpha':alpha_stats(Image.open(out).convert('RGBA')),'background_mode':'native_transparent','fallback_used':False,'processing':'threshold-8 subject crop with transparent margin, premultiplied-alpha Lanczos downsample, centered on exact target canvas'})
(ROOT/'evidence/second_tranche_processing.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
print(json.dumps(reports,indent=2))
