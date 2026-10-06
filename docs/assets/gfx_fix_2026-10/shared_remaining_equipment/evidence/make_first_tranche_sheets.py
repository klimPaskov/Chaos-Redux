from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json
ROOT = Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
ASSETS = [
 {'id':'GFX_coal_golem_equipment_medium + GFX_coal_golem_equipment_1_medium','size':(131,52),'before':ROOT/'originals/png/coal_golem_equipment.png','source':ROOT/'source_png/coal_golem_equipment_v5.png','processed':ROOT/'processed_png/coal_golem_equipment_v5_131x52.png','dds':ROOT/'evidence/first_tranche_dds_decode/coal_golem_equipment.png'},
 {'id':'GFX_EMI_livens_tabun_projectile','size':(56,42),'before':ROOT/'originals/png/phosgene_projectile.png','source':ROOT/'source_png/tabun_projectile_v1.png','processed':ROOT/'processed_png/tabun_projectile_v1_56x42.png','dds':ROOT/'evidence/first_tranche_dds_decode/tabun_projectile.png'},
 {'id':'GFX_archetype_livens_projector_equipment_medium','size':(58,40),'before':ROOT/'originals/png/archetype_livens_projector_equipment.png','source':ROOT/'source_png/archetype_livens_projector_v1.png','processed':ROOT/'processed_png/archetype_livens_projector_v1_58x40.png','dds':ROOT/'evidence/first_tranche_dds_decode/archetype_livens_projector_equipment.png'},
]
COLS=[('Before: exact current DDS', 'before'), ('ImageGen: native source', 'source'), ('Processed PNG', 'processed'), ('DDS round-trip', 'dds')]
BG='#efefed'; DARK='#21262d'; GRID1='#c8c8c4'; GRID2='#e3e3df'
font=ImageFont.load_default()

def checker(w,h,step=12):
 im=Image.new('RGB',(w,h),GRID1); d=ImageDraw.Draw(im)
 for y in range(0,h,step):
  for x in range(0,w,step):
   if (x//step+y//step)%2: d.rectangle((x,y,x+step-1,y+step-1),fill=GRID2)
 return im

def draw_sheet(scale, output):
 cell_w,cell_h=650,310
 header_h=38; row_label_h=28
 cols_w=cell_w*4
 canvas=Image.new('RGB',(cols_w,header_h+len(ASSETS)*(cell_h+row_label_h)),BG)
 d=ImageDraw.Draw(canvas)
 for c,(label,_) in enumerate(COLS):
  x=c*cell_w
  d.rectangle((x,0,x+cell_w-1,header_h-1),fill=DARK)
  d.text((x+12,12),label,fill='white',font=font)
 for ri,asset in enumerate(ASSETS):
  y0=header_h+ri*(cell_h+row_label_h)
  d.rectangle((0,y0,cols_w-1,y0+row_label_h-1),fill='#d6d6d2')
  d.text((10,y0+7),f"{asset['id']} | target {asset['size'][0]}x{asset['size'][1]}",fill='#191919',font=font)
  for ci,(_,key) in enumerate(COLS):
   x0=ci*cell_w
   tile=checker(cell_w-16,cell_h-16)
   src=Image.open(asset[key]).convert('RGBA')
   if key in ('processed','dds','before'):
    if scale==1:
     view=src
    else:
     view=src.resize((src.width*4,src.height*4),Image.Resampling.BICUBIC)
   else:
    view=src.copy()
    view.thumbnail((cell_w-40,cell_h-54),Image.Resampling.LANCZOS)
   max_w,max_h=cell_w-32,cell_h-52
   if view.width>max_w or view.height>max_h:
    view.thumbnail((max_w,max_h),Image.Resampling.LANCZOS)
   ox=(tile.width-view.width)//2; oy=(tile.height-view.height)//2+7
   tile.paste(view,(ox,oy),view)
   canvas.paste(tile.convert('RGB'),(x0+8,y0+row_label_h+8))
   dims=src.size
   note=f'{dims[0]}x{dims[1]}'+(f' | {scale}x review' if scale>1 and key!='source' else '')
   d.text((x0+12,y0+row_label_h+cell_h-2),note,fill='#242424',font=font)
 path=ROOT/'contact_sheets'/output
 if path.exists(): raise FileExistsError(path)
 canvas.save(path,optimize=True)
 return path.as_posix()

results={'native':draw_sheet(1,'first_tranche_native.png'),'smooth_4x':draw_sheet(4,'first_tranche_smooth_4x.png')}
print(json.dumps(results,indent=2))
