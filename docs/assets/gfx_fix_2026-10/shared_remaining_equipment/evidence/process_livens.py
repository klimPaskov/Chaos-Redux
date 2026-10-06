from pathlib import Path
from PIL import Image
import hashlib,json
ROOT=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
ASSETS=[
 ('livens_projector_single_tube_v1','source_png/livens_projector_single_tube_v1.png','processed_png/livens_projector_single_tube_v1_94x45.png'),
 ('livens_projector_framed_battery_v1','source_png/livens_projector_framed_battery_v1.png','processed_png/livens_projector_framed_battery_v1_94x45.png'),
 ('livens_projector_carriage_battery_v1','source_png/livens_projector_carriage_battery_v1.png','processed_png/livens_projector_carriage_battery_v1_94x45.png'),
]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bbox(alpha,t):return alpha.point(lambda a:255 if a>=t else 0).getbbox()
def alpha_stats(im):
 a=im.getchannel('A');v=list(a.getdata());return {'min':min(v),'max':max(v),'transparent':sum(x==0 for x in v),'partial':sum(0<x<255 for x in v),'bbox_gt_0':a.getbbox(),'bbox_ge_16':bbox(a,16)}
reports=[]
for cid,src_rel,out_rel in ASSETS:
 src=ROOT/src_rel;out=ROOT/out_rel
 if out.exists():raise FileExistsError(out)
 im=Image.open(src).convert('RGBA');a=im.getchannel('A');b=bbox(a,8)
 if b is None:raise ValueError(f'no alpha content {src}')
 pad=max(8,round(max(im.size)*.008));x0,y0,x1,y1=b;crop_box=(max(0,x0-pad),max(0,y0-pad),min(im.width,x1+pad),min(im.height,y1+pad));crop=im.crop(crop_box)
 target=(94,45);margin=2;content=(target[0]-4,target[1]-4);scale=min(content[0]/crop.width,content[1]/crop.height);size=(round(crop.width*scale),round(crop.height*scale))
 res=crop.convert('RGBa').resize(size,Image.Resampling.LANCZOS).convert('RGBA');canvas=Image.new('RGBA',target,(0,0,0,0));offset=((target[0]-size[0])//2,(target[1]-size[1])//2);canvas.alpha_composite(res,offset);out.parent.mkdir(parents=True,exist_ok=True);canvas.save(out,format='PNG',optimize=True)
 reports.append({'candidate_id':cid,'source_path':src.as_posix(),'source_sha256':sha(src),'source_size':list(im.size),'source_alpha':alpha_stats(im),'source_bbox_ge_8':b,'crop_padding_px':pad,'crop_box':crop_box,'target_size':list(target),'resized_subject_size':list(size),'offset':offset,'processed_path':out.as_posix(),'processed_sha256':sha(out),'processed_alpha':alpha_stats(Image.open(out).convert('RGBA')),'background_mode':'native_transparent','fallback_used':False,'processing':'threshold-8 subject crop with transparent margin, premultiplied-alpha Lanczos resize and centered placement'})
(ROOT/'evidence/livens_processing.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
print(json.dumps(reports,indent=2))
