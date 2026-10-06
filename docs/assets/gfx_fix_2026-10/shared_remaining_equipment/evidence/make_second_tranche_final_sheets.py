from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json
ROOT=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
ASSETS=[
 {'id':'GFX_livens_projector_equipment_medium / _1_medium / GFX_livens_projector_tech_medium','target':(94,45),'before':ROOT/'originals/png/livens_projector.png','source':ROOT/'source_png/livens_projector_single_tube_v1.png','processed':ROOT/'processed_png/livens_projector_single_tube_v1_94x45.png','dds':ROOT/'evidence/second_tranche_dds_decode/livens_projector.png','source_note':'ImageGen source'},
 {'id':'GFX_livens_projector_equipment_2_medium / GFX_improved_livens_projector_medium','target':(94,45),'before':ROOT/'originals/png/livens_projector_improved.png','source':ROOT/'source_png/livens_projector_framed_battery_v1.png','processed':ROOT/'processed_png/livens_projector_framed_battery_v1_94x45.png','dds':ROOT/'evidence/second_tranche_dds_decode/livens_projector_improved.png','source_note':'ImageGen source'},
 {'id':'GFX_livens_projector_equipment_3_medium / GFX_advanced_livens_projector_medium','target':(94,45),'before':ROOT/'originals/png/livens_projector_advanced.png','source':ROOT/'source_png/livens_projector_carriage_battery_v1.png','processed':ROOT/'processed_png/livens_projector_carriage_battery_v1_94x45.png','dds':ROOT/'evidence/second_tranche_dds_decode/livens_projector_advanced.png','source_note':'ImageGen source'},
 {'id':'GFX_zombie_cure_bomb_equipment / _medium','target':(131,52),'before':ROOT/'originals/png/zombie_cure_bomb_equipment.png','source':ROOT/'source_png/zombie_cure_bomb_equipment_v1.png','processed':ROOT/'processed_png/zombie_cure_bomb_equipment_v1_131x52.png','dds':ROOT/'evidence/second_tranche_dds_decode/zombie_cure_bomb_equipment.png','source_note':'ImageGen source'},
 {'id':'GFX_livens_projector_chassis_blueprint','target':(508,248),'before':ROOT/'originals/png/generic_livens_projector_blueprint.png','source':ROOT/'source_png/livens_projector_chassis_blueprint_v2.png','processed':ROOT/'processed_png/livens_projector_chassis_blueprint_v2_508x248.png','dds':ROOT/'evidence/second_tranche_dds_decode/generic_livens_projector_blueprint.png','source_note':'ImageGen source'},
 {'id':'GFX_livens_projectile_slot','target':(508,248),'before':ROOT/'originals/png/projectile_slot.png','source':ROOT/'source_png/projectile_slot_source_overlay_v2.png','processed':ROOT/'processed_png/projectile_slot_v2_508x248.png','dds':ROOT/'evidence/second_tranche_v2_dds_decode/projectile_slot_v2.png','source_note':'Delineated source mask; technical derivative'},
]
COLS=[('Before: exact current DDS','before'),('Source art / source mask','source'),('Processed PNG','processed'),('DDS round-trip','dds')]
CELL_W,CELL_H=650,310;ROW_H=30;HEADER_H=38
GRID_A='#c8c8c4';GRID_B='#e3e3df';DARK='#21262d';FONT=ImageFont.load_default()
def checker(w,h,step=12):
 im=Image.new('RGB',(w,h),GRID_A);d=ImageDraw.Draw(im)
 for y in range(0,h,step):
  for x in range(0,w,step):
   if (x//step+y//step)%2:d.rectangle((x,y,x+step-1,y+step-1),fill=GRID_B)
 return im
def draw_sheet(scale,name):
 w=4*CELL_W;h=HEADER_H+len(ASSETS)*(CELL_H+ROW_H);canvas=Image.new('RGB',(w,h),'#efefed');d=ImageDraw.Draw(canvas)
 for col,(label,key) in enumerate(COLS):
  x=col*CELL_W;d.rectangle((x,0,x+CELL_W-1,HEADER_H-1),fill=DARK);d.text((x+12,12),label,fill='white',font=FONT)
 for ri,item in enumerate(ASSETS):
  y0=HEADER_H+ri*(CELL_H+ROW_H);d.rectangle((0,y0,w-1,y0+ROW_H-1),fill='#d6d6d2');d.text((10,y0+8),f"{item['id']} | target {item['target'][0]}x{item['target'][1]}",fill='#191919',font=FONT)
  for ci,(_,key) in enumerate(COLS):
   x0=ci*CELL_W;tile=checker(CELL_W-16,CELL_H-16);im=Image.open(item[key]).convert('RGBA')
   if key=='source':
    view=im.copy();view.thumbnail((CELL_W-42,CELL_H-55),Image.Resampling.LANCZOS)
   elif scale==1:view=im
   else:view=im.resize((im.width*4,im.height*4),Image.Resampling.BICUBIC)
   max_size=(CELL_W-32,CELL_H-56)
   if view.width>max_size[0] or view.height>max_size[1]:view.thumbnail(max_size,Image.Resampling.LANCZOS)
   ox=(tile.width-view.width)//2;oy=(tile.height-view.height)//2+7
   tile.paste(view,(ox,oy),view);canvas.paste(tile.convert('RGB'),(x0+8,y0+ROW_H+8))
   note=f"{im.width}x{im.height} | {item['source_note']}" if key=='source' else f"{im.width}x{im.height}"+(f' | {scale}x smooth review' if scale>1 else '')
   d.text((x0+12,y0+ROW_H+CELL_H-2),note,fill='#242424',font=FONT)
 out=ROOT/'contact_sheets'/name
 if out.exists():raise FileExistsError(out)
 canvas.save(out,optimize=True);return out.as_posix()
paths={'native':draw_sheet(1,'second_tranche_final_native.png'),'smooth_4x':draw_sheet(4,'second_tranche_final_smooth_4x.png')}
print(json.dumps(paths,indent=2))

