# ImageGen prompts

All prompts used the built-in ImageGen tool on 2026-08-01. Flag prompts used the `logo-brand` use case and requested a flat orthographic HOI4 flag source master with no fabric, folds, perspective, scene, text, watermark, lighting, or UI. Emblem prompts used the same use case and requested a centered transparent UI seal source on a perfectly flat `#00ff00` chroma-key background with no shadows, gradients, text, watermark, or UI frame.

## Flag masters

- `AFRICA_CHARTER_FEDERATION_flag_source.png`: deep indigo-blue field, broad warm ivory horizontal band, copper-gold protective arch over three linked civic pillars, small green baobab leaf; federal protection and continental covenant.
- `AFRICA_CONTINENTAL_REPUBLIC_flag_source.png`: forest-green field, muted gold diagonal band, ivory medallion with dark bronze rising sun behind an open civic book and five linked stars; civic republicanism.
- `AFRICA_UNITED_KINGDOMS_flag_source.png`: deep burgundy field, midnight-blue hoist panel, ivory shield edged antique gold, three stylized crowns linked by a ring and a small red-gold sun; decorated sovereign compact.
- `AFRICA_PEOPLES_UNION_flag_source.png`: warm terracotta-red field, charcoal-blue horizontal band edged in cream, ivory roundel with gold gear around three green leaf-and-sun forms and a linked-ring base; popular solidarity and shared labor.
- `AFRICA_CONTINENTAL_COMMAND_flag_source.png`: dark slate-blue field, ochre-gold hoist stripe, ivory shield with copper command baton crossed with a compass rose and small green starburst; unified command and strategic discipline, no fascist symbols.
- `AFRICA_CONFEDERATION_flag_source.png`: deep teal field with muted sand and rust-red horizontal bands, ivory lozenge with six interlocking copper rings around a dark-green river diamond; linked regions and negotiated autonomy.
- `AFRICA_COVENANT_UNION_flag_source.png`: near-black indigo field, moss-green horizontal band and pale-gold border, ivory seal with a luminous green baobab-like tree, roots interlocked with a crescent river and branches forming a subtle six-point star; supernatural nature pact, dignified not horror.

## Emblem masters

- `012_africa_charter_federalism_emblem_source.png`: copper protective arch enclosing three linked civic pillars, green baobab leaf, ivory shield outline.
- `012_africa_continental_republic_emblem_source.png`: open ivory civic book beneath a rising copper sun disk, five linked green stars, thin gold laurel arc.
- `012_africa_council_of_crowns_emblem_source.png`: three distinct copper-and-gold stylized crowns around a burgundy ring, joined by an ivory circlet and small crimson sun disk.
- `012_africa_peoples_union_emblem_source.png`: ivory gear around three terracotta-and-green rising leaves, two small interlocking rings, charcoal outline; no people or portraits.
- `012_africa_military_continentalism_emblem_source.png`: copper command baton crossed with dark steel compass rose inside an ivory shield, ochre starburst and slate ring; no real insignia.
- `012_africa_continental_confederation_emblem_source.png`: six copper rings interlocked around a dark-green river diamond, ivory lozenge and thin teal ring.
- `012_africa_high_chaos_covenant_emblem_source.png`: impossible living baobab tree in moss green, roots around a pale river crescent, branches forming a six-point star, cyan ring and copper seed marks; mysterious nature pact without horror.

## Mechanical processing

Flags: `ImageOps.fit` to each target ladder size using centered cover crop and LANCZOS, then RGB PNG preview plus RGBA TGA export.

Emblems: chroma-key removal with the installed `remove_chroma_key.py`, alpha-bounds crop, LANCZOS thumbnail to 56x56, centered on a 64x64 transparent RGBA canvas, then repository DDS converter.
