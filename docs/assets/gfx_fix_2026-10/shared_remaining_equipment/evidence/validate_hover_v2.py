from pathlib import Path
from PIL import Image, ImageChops
import cv2, hashlib, json, numpy as np, struct
ROOT=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
png=ROOT/'processed_png/projectile_slot_v2_508x248.png';dds=ROOT/'staged_dds/projectile_slot_v2.dds';decoded=ROOT/'evidence/second_tranche_v2_dds_decode/projectile_slot_v2.png'
data=dds.read_bytes();w,h=struct.unpack_from('<II',data,16)[0],struct.unpack_from('<I',data,12)[0]
header=struct.unpack_from('<I',data,4)[0];mip=struct.unpack_from('<I',data,28)[0];pf=struct.unpack_from('<8I',data,76);caps=struct.unpack_from('<I',data,108)[0]
source=Image.open(png).convert('RGBA');rt=Image.open(decoded).convert('RGBA');diff=ImageChops.difference(source,rt).getbbox()
if data[:4]!=b'DDS ' or (w,h)!=(508,248) or len(data)!=128+508*248*4 or header!=124:raise ValueError('DDS container/dimensions/header invalid')
if pf!=(32,65,0,32,0x00ff0000,0x0000ff00,0x000000ff,0xff000000) or caps&0x1000==0 or mip not in (0,1):raise ValueError('DDS format/caps/mip invalid')
if source.size!=(508,248) or rt.size!=(508,248) or diff is not None:raise ValueError(f'DDS roundtrip mismatch: {diff}')
a=np.asarray(source.getchannel('A'));amin,amax=int(a.min()),int(a.max())
if (amin,amax)!=(0,128):raise ValueError(f'Unexpected alpha range {(amin,amax)}')
binary=(a>=64).astype('uint8');count,labels,stats,_=cv2.connectedComponentsWithStats(binary,8);comps=[]
for i in range(1,count):
 x,y,cw,ch,area=map(int,stats[i])
 if area>50:comps.append({'bbox':[x,y,cw,ch],'area':area})
if len(comps)!=3:raise ValueError(f'Expected three connected silhouettes, got {comps}')
holes=0
for i in range(1,count):
 x,y,cw,ch,area=map(int,stats[i])
 if area>50:
  crop=(labels[y:y+ch,x:x+cw]==i).astype('uint8')
  contours,hierarchy=cv2.findContours(crop,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
  if hierarchy is not None:
   holes += sum(1 for q in hierarchy[0] if q[3]>=0)
if holes!=0:raise ValueError(f'Unexpected internal mask holes: {holes}')
report={'asset':'projectile_slot_v2','processed_png':png.as_posix(),'processed_png_sha256':hashlib.sha256(png.read_bytes()).hexdigest(),'staged_dds':dds.as_posix(),'staged_dds_sha256':hashlib.sha256(data).hexdigest(),'dimensions':[w,h],'header_size':header,'pixel_format':{'size':pf[0],'flags':pf[1],'fourcc':pf[2],'rgb_bit_count':pf[3],'masks':list(pf[4:])},'caps':caps,'mip_count':mip,'alpha_minmax':[amin,amax],'four_connected_silhouettes':comps,'internal_holes':holes,'texconv_roundtrip':'pixel-identical','decoded_png':decoded.as_posix()}
(ROOT/'evidence/second_tranche_v2_dds_validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report,indent=2))
