# CSH flag source manifest

Status: parent-reviewed source and native format complete; fresh live warning-removal evidence remains pending.

The requested assets are for CSH, the stateless internal Scientific Office that holds the 29 dated CBRN scientists in history data. This package introduces no polity, political route, or flag-design history.

Source mode: fictional institutional design generated with the built-in native ImageGen tool on 2026-10-03. The first generated output and selected refined master are both archived under source_png/. The selected master was refined twice to remove shading and retain the same navy/olive field, brass border, and single flask emblem. The final master remains the source of all runtime sizes.

Generation prompt and refinement notes: prompts/csh_scientific_office_flag.md.
Selected full-size source: source_png/csh_scientific_office_master.png (SHA-256 403d2e09062825a33d36bdf09b77e0877ffc63e5e2fc2e3a66d5415391f83652).
Initial ImageGen source: source_png/csh_scientific_office_initial.png (SHA-256 4545a71a93572dd85b29ee3d76195c0652e893133546e6485e66cad4d214a939).
Contact sheet comparing the archived master with normal, medium, and small exports: contact_sheets/csh_flags_master_and_sizes.png.
Processed PNG previews for every runtime filename are under processed_png/normal/, processed_png/medium/, and processed_png/small/.

The no-suffix flag and the democratic, neutrality, fascism, and communism filename aliases intentionally share identical pixels because CSH is an internal scientific holder, not a playable polity with ideology-specific identity. This shared design is explicitly deliberate and preserves a stable internal office identity.

All 15 final files are uncompressed TGA type 2, truecolor 32-bit BGRA, descriptor 8 (8 alpha bits), bottom-left origin, no color map. Opaque RGB flag colors are retained with alpha 255. Each payload is 18-byte header plus width x height x 4 bytes. PNG previews were decoded from the same processed pixels. Every TGA was decoded with Pillow and compared pixel-for-pixel against its matching processed PNG after orientation interpretation.

## Reference evidence

- Canonical flat-flag family: .agents/skills/chaos-redux-event-assets/assets/gfx_references/README.md lines 44-46 and 58-61, CATALOG.md lines 107-129, and flags/contact_sheet.png, covering the complete normal, medium, and small ladder. The contact sheet labels 82x52, 41x26, and 10x7 exports.
- Offline country-creation reference: paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md, Flag section, lines 461-480, offline reference revision 0c0e57915a7d1eef9ddeebe91c7329e18f4f224af98ac33fac5edd35e3aaa35d. It specifies filename-based automatic flag assignment, uncompressed 32-bit ARGB TGA, bottom-left origin, and the three size requirements.
- Installed-game native definition: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/defines/00_graphics.lua, lines 938-945, SHA-256 dfdab0a5fad7319d7b5ac524d98af49d3a0c1f95772e6b7a76abce54836f3d86.
- Installed vanilla sample: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/small/USA.tga, type 2, 32 bpp, descriptor 0, bottom-left origin, 10x7, 298 bytes.
- Repository samples: CXT and KRG normal, medium, and small flags use type 2, 32 bpp, descriptor 8, bottom-left origin; 82x52 is 17,074 bytes, 41x26 is 4,282 bytes, and 10x7 is 298 bytes.
- HOI4 reference MCP tools were unavailable to this agent; the cited local offline and installed sources were read directly.

## Runtime files and hashes

- gfx/flags/CSH.tga: 82x52, 17074 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 8905a5cfaa1fe23c2cefba4ce3e8c2d6d206559b3ab8e6859c12ad2e952d776f.
- gfx/flags/CSH_communism.tga: 82x52, 17074 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 8905a5cfaa1fe23c2cefba4ce3e8c2d6d206559b3ab8e6859c12ad2e952d776f.
- gfx/flags/CSH_democratic.tga: 82x52, 17074 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 8905a5cfaa1fe23c2cefba4ce3e8c2d6d206559b3ab8e6859c12ad2e952d776f.
- gfx/flags/CSH_fascism.tga: 82x52, 17074 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 8905a5cfaa1fe23c2cefba4ce3e8c2d6d206559b3ab8e6859c12ad2e952d776f.
- gfx/flags/CSH_neutrality.tga: 82x52, 17074 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 8905a5cfaa1fe23c2cefba4ce3e8c2d6d206559b3ab8e6859c12ad2e952d776f.
- gfx/flags/medium/CSH.tga: 41x26, 4282 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 5511bd6cdb8c7073fedec9b08ae1c596c01d7d3895c9fa917b94475341c7a734.
- gfx/flags/medium/CSH_communism.tga: 41x26, 4282 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 5511bd6cdb8c7073fedec9b08ae1c596c01d7d3895c9fa917b94475341c7a734.
- gfx/flags/medium/CSH_democratic.tga: 41x26, 4282 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 5511bd6cdb8c7073fedec9b08ae1c596c01d7d3895c9fa917b94475341c7a734.
- gfx/flags/medium/CSH_fascism.tga: 41x26, 4282 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 5511bd6cdb8c7073fedec9b08ae1c596c01d7d3895c9fa917b94475341c7a734.
- gfx/flags/medium/CSH_neutrality.tga: 41x26, 4282 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 5511bd6cdb8c7073fedec9b08ae1c596c01d7d3895c9fa917b94475341c7a734.
- gfx/flags/small/CSH.tga: 10x7, 298 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 19ef01e4eaae2569639c859db738c4a7beb6a8a27cd95df777b6a68615f8dfe8.
- gfx/flags/small/CSH_communism.tga: 10x7, 298 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 19ef01e4eaae2569639c859db738c4a7beb6a8a27cd95df777b6a68615f8dfe8.
- gfx/flags/small/CSH_democratic.tga: 10x7, 298 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 19ef01e4eaae2569639c859db738c4a7beb6a8a27cd95df777b6a68615f8dfe8.
- gfx/flags/small/CSH_fascism.tga: 10x7, 298 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 19ef01e4eaae2569639c859db738c4a7beb6a8a27cd95df777b6a68615f8dfe8.
- gfx/flags/small/CSH_neutrality.tga: 10x7, 298 bytes, TGA type 2, 32 bpp, descriptor 8, bottom-left, SHA-256 19ef01e4eaae2569639c859db738c4a7beb6a8a27cd95df777b6a68615f8dfe8.

## Processed PNG hashes

- docs/assets/cbrn_scientist_holder_flags/processed_png/medium/CSH.png: SHA-256 40496115cb588117c9353b6547d6ec477234a1f4e9f4e579b19b35f29ffbe66c.
- docs/assets/cbrn_scientist_holder_flags/processed_png/medium/CSH_communism.png: SHA-256 40496115cb588117c9353b6547d6ec477234a1f4e9f4e579b19b35f29ffbe66c.
- docs/assets/cbrn_scientist_holder_flags/processed_png/medium/CSH_democratic.png: SHA-256 40496115cb588117c9353b6547d6ec477234a1f4e9f4e579b19b35f29ffbe66c.
- docs/assets/cbrn_scientist_holder_flags/processed_png/medium/CSH_fascism.png: SHA-256 40496115cb588117c9353b6547d6ec477234a1f4e9f4e579b19b35f29ffbe66c.
- docs/assets/cbrn_scientist_holder_flags/processed_png/medium/CSH_neutrality.png: SHA-256 40496115cb588117c9353b6547d6ec477234a1f4e9f4e579b19b35f29ffbe66c.
- docs/assets/cbrn_scientist_holder_flags/processed_png/normal/CSH.png: SHA-256 09eff347da5ee1d0f93904aaf72343e392cdf956deaada99aef0b3b79a102255.
- docs/assets/cbrn_scientist_holder_flags/processed_png/normal/CSH_communism.png: SHA-256 09eff347da5ee1d0f93904aaf72343e392cdf956deaada99aef0b3b79a102255.
- docs/assets/cbrn_scientist_holder_flags/processed_png/normal/CSH_democratic.png: SHA-256 09eff347da5ee1d0f93904aaf72343e392cdf956deaada99aef0b3b79a102255.
- docs/assets/cbrn_scientist_holder_flags/processed_png/normal/CSH_fascism.png: SHA-256 09eff347da5ee1d0f93904aaf72343e392cdf956deaada99aef0b3b79a102255.
- docs/assets/cbrn_scientist_holder_flags/processed_png/normal/CSH_neutrality.png: SHA-256 09eff347da5ee1d0f93904aaf72343e392cdf956deaada99aef0b3b79a102255.
- docs/assets/cbrn_scientist_holder_flags/processed_png/small/CSH.png: SHA-256 7809517229d9f9cd1b5d5fa3c8f243bb7cda8297c8186bacc8c952f1e4875656.
- docs/assets/cbrn_scientist_holder_flags/processed_png/small/CSH_communism.png: SHA-256 7809517229d9f9cd1b5d5fa3c8f243bb7cda8297c8186bacc8c952f1e4875656.
- docs/assets/cbrn_scientist_holder_flags/processed_png/small/CSH_democratic.png: SHA-256 7809517229d9f9cd1b5d5fa3c8f243bb7cda8297c8186bacc8c952f1e4875656.
- docs/assets/cbrn_scientist_holder_flags/processed_png/small/CSH_fascism.png: SHA-256 7809517229d9f9cd1b5d5fa3c8f243bb7cda8297c8186bacc8c952f1e4875656.
- docs/assets/cbrn_scientist_holder_flags/processed_png/small/CSH_neutrality.png: SHA-256 7809517229d9f9cd1b5d5fa3c8f243bb7cda8297c8186bacc8c952f1e4875656.

Parent review approved the source/size comparison sheet and independently validated all fifteen native files; the stored bottom-left pixel and full decoded PNG equality are recorded in `docs/testing/2026-10-03_csh_flag_load_repair/flag_format_validation.json`.
No game was launched by the coding agents, and no fresh clean-error-log claim is made.
