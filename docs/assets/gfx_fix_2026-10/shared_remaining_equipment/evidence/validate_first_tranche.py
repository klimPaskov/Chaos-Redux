from pathlib import Path
from PIL import Image, ImageChops
import hashlib, json, struct
root=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
items=[
 ('coal_golem_equipment',root/'processed_png/coal_golem_equipment_v5_131x52.png',root/'staged_dds/coal_golem_equipment.dds',root/'evidence/first_tranche_dds_decode/coal_golem_equipment.png',(131,52)),
 ('tabun_projectile',root/'processed_png/tabun_projectile_v1_56x42.png',root/'staged_dds/tabun_projectile.dds',root/'evidence/first_tranche_dds_decode/tabun_projectile.png',(56,42)),
 ('archetype_livens_projector_equipment',root/'processed_png/archetype_livens_projector_v1_58x40.png',root/'staged_dds/archetype_livens_projector_equipment.dds',root/'evidence/first_tranche_dds_decode/archetype_livens_projector_equipment.png',(58,40)),
]
results=[]
for name,png,dds,decoded,expected in items:
 data=dds.read_bytes()
 if data[:4]!=b'DDS ': raise ValueError(f'{name}: bad magic')
 header=struct.unpack_from('<I',data,4)[0]
 height,width=struct.unpack_from('<II',data,12)
 mip=struct.unpack_from('<I',data,28)[0]
 pfsize,pfflags,fourcc,rgbbits,rmask,gmask,bmask,amask=struct.unpack_from('<8I',data,76)
 caps=struct.unpack_from('<I',data,108)[0]
 pixels=Image.open(png).convert('RGBA')
 rt=Image.open(decoded).convert('RGBA')
 if (width,height)!=expected or pixels.size!=expected or rt.size!=expected: raise ValueError(f'{name}: dimension mismatch')
 if header!=124 or len(data)!=128+width*height*4: raise ValueError(f'{name}: malformed legacy BGRA size')
 if (pfsize,pfflags,fourcc,rgbbits,rmask,gmask,bmask,amask)!=(32,65,0,32,0x00ff0000,0x0000ff00,0x000000ff,0xff000000): raise ValueError(f'{name}: unexpected pixel format')
 if caps & 0x1000 == 0: raise ValueError(f'{name}: no DDSCAPS_TEXTURE')
 if mip not in (0,1): raise ValueError(f'{name}: unexpected mip count {mip}')
 diff=ImageChops.difference(pixels,rt).getbbox()
 if diff is not None: raise ValueError(f'{name}: Texconv roundtrip pixel difference {diff}')
 alpha=pixels.getchannel('A')
 results.append({'asset':name,'dds_path':dds.as_posix(),'dds_sha256':hashlib.sha256(data).hexdigest(),'dds_bytes':len(data),'dimensions':[width,height],'header_size':header,'pixel_format':{'size':pfsize,'flags':pfflags,'fourcc':fourcc,'rgb_bit_count':rgbbits,'masks':[rmask,gmask,bmask,amask]},'caps':caps,'mip_count':mip,'alpha_minmax':list(alpha.getextrema()),'texconv_roundtrip':'pixel-identical','decoded_png':decoded.as_posix()})
out=root/'evidence/first_tranche_dds_validation.json'
out.write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
