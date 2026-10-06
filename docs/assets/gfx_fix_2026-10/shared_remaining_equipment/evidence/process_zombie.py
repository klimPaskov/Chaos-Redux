from pathlib import Path
from PIL import Image
import hashlib,json
ROOT=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
src=ROOT/'source_png/zombie_cure_bomb_equipment_v1.png';out=ROOT/'processed_png/zombie_cure_bomb_equipment_v1_131x52.png';target=(131,52)
if not src.is_file():raise FileNotFoundError(src)
if out.exists():raise FileExistsError(out)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bbox(alpha,t):return alpha.point(lambda a:255 if a>=t else 0).getbbox()
def astats(im):
 a=im.getchannel('A');v=list(a.getdata());return {'min':min(v),'max':max(v),'transparent':sum(x==0 for x in v),'partial':sum(0<x<255 for x in v),'opaque':sum(x==255 for x in v),'bbox_gt_0':a.getbbox(),'bbox_ge_16':bbox(a,16)}
raw=Image.open(src).convert('RGBA');a=raw.getchannel('A');b=bbox(a,8)
if b is None:raise ValueError('No native-alpha subject')
pad=max(8,round(max(raw.size)*.008));x0,y0,x1,y1=b;crop_box=(max(0,x0-pad),max(0,y0-pad),min(raw.width,x1+pad),min(raw.height,y1+pad));crop=raw.crop(crop_box);margin=2;max_w,max_h=target[0]-4,target[1]-4;scale=min(max_w/crop.width,max_h/crop.height);size=(round(crop.width*scale),round(crop.height*scale));res=crop.convert('RGBa').resize(size,Image.Resampling.LANCZOS).convert('RGBA');canvas=Image.new('RGBA',target,(0,0,0,0));offset=((target[0]-size[0])//2,(target[1]-size[1])//2);canvas.alpha_composite(res,offset);out.parent.mkdir(parents=True,exist_ok=True);canvas.save(out,format='PNG',optimize=True)
report={'candidate_id':'zombie_cure_bomb_equipment_v1','source_path':src.as_posix(),'source_sha256':sha(src),'source_size':list(raw.size),'source_alpha':astats(raw),'source_bbox_alpha_ge_8':b,'source_crop_padding_px':pad,'source_crop_box':crop_box,'target_size':list(target),'resized_subject_size':list(size),'offset':offset,'processed_path':out.as_posix(),'processed_sha256':sha(out),'processed_alpha':astats(Image.open(out).convert('RGBA')),'background_mode':'native_transparent','fallback_used':False,'processing':'threshold-8 subject crop with transparent margin, premultiplied-alpha Lanczos downsample, centered on exact target canvas'}
path=ROOT/'evidence/zombie_processing.json';path.write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report,indent=2))
