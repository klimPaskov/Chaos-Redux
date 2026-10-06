from pathlib import Path
from PIL import Image, ImageChops
import hashlib,json,struct
root=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
items=[
 ('livens_projector',root/'processed_png/livens_projector_single_tube_v1_94x45.png',root/'staged_dds/livens_projector.dds',root/'evidence/second_tranche_dds_decode/livens_projector.png',(94,45),(0,255)),
 ('livens_projector_improved',root/'processed_png/livens_projector_framed_battery_v1_94x45.png',root/'staged_dds/livens_projector_improved.dds',root/'evidence/second_tranche_dds_decode/livens_projector_improved.png',(94,45),(0,255)),
 ('livens_projector_advanced',root/'processed_png/livens_projector_carriage_battery_v1_94x45.png',root/'staged_dds/livens_projector_advanced.dds',root/'evidence/second_tranche_dds_decode/livens_projector_advanced.png',(94,45),(0,255)),
 ('zombie_cure_bomb_equipment',root/'processed_png/zombie_cure_bomb_equipment_v1_131x52.png',root/'staged_dds/zombie_cure_bomb_equipment.dds',root/'evidence/second_tranche_dds_decode/zombie_cure_bomb_equipment.png',(131,52),(0,255)),
 ('generic_livens_projector_blueprint',root/'processed_png/livens_projector_chassis_blueprint_v2_508x248.png',root/'staged_dds/generic_livens_projector_blueprint.dds',root/'evidence/second_tranche_dds_decode/generic_livens_projector_blueprint.png',(508,248),(255,255)),
 ('projectile_slot',root/'processed_png/projectile_slot_v1_508x248.png',root/'staged_dds/projectile_slot.dds',root/'evidence/second_tranche_dds_decode/projectile_slot.png',(508,248),(0,128)),
]
results=[]
for name,png,dds,decoded,expected,alpha_expected in items:
 data=dds.read_bytes()
 if data[:4]!=b'DDS ':raise ValueError(f'{name}: bad DDS magic')
 header=struct.unpack_from('<I',data,4)[0];height,width=struct.unpack_from('<II',data,12);mip=struct.unpack_from('<I',data,28)[0]
 pfsize,pfflags,fourcc,rgbbits,rmask,gmask,bmask,amask=struct.unpack_from('<8I',data,76);caps=struct.unpack_from('<I',data,108)[0]
 source=Image.open(png).convert('RGBA');roundtrip=Image.open(decoded).convert('RGBA')
 if (width,height)!=expected or source.size!=expected or roundtrip.size!=expected:raise ValueError(f'{name}: dimension mismatch')
 if header!=124 or len(data)!=128+width*height*4:raise ValueError(f'{name}: malformed BGRA DDS size')
 if (pfsize,pfflags,fourcc,rgbbits,rmask,gmask,bmask,amask)!=(32,65,0,32,0x00ff0000,0x0000ff00,0x000000ff,0xff000000):raise ValueError(f'{name}: unexpected pixel format')
 if caps & 0x1000 == 0:raise ValueError(f'{name}: DDSCAPS_TEXTURE absent')
 if mip not in (0,1):raise ValueError(f'{name}: unexpected mip count {mip}')
 diff=ImageChops.difference(source,roundtrip).getbbox()
 if diff is not None:raise ValueError(f'{name}: Texconv roundtrip differs at {diff}')
 alpha=source.getchannel('A').getextrema()
 if alpha!=alpha_expected:raise ValueError(f'{name}: alpha {alpha} != {alpha_expected}')
 results.append({'asset':name,'processed_png':png.as_posix(),'processed_sha256':hashlib.sha256(png.read_bytes()).hexdigest(),'staged_dds':dds.as_posix(),'staged_dds_sha256':hashlib.sha256(data).hexdigest(),'dds_bytes':len(data),'dimensions':[width,height],'header_size':header,'pixel_format':{'size':pfsize,'flags':pfflags,'fourcc':fourcc,'rgb_bit_count':rgbbits,'masks':[rmask,gmask,bmask,amask]},'caps':caps,'mip_count':mip,'alpha_minmax':list(alpha),'texconv_roundtrip':'pixel-identical'})
out=root/'evidence/second_tranche_dds_validation.json';out.write_text(json.dumps(results,indent=2),encoding='utf-8');print(json.dumps(results,indent=2))
