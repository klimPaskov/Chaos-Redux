# IW-030 Montenegro sourced portrait placeholders

Date: 2026-08-09.

This package implements the user-approved historical placeholder workflow: verified archival male photograph, explicit head-and-shoulders crop, direct 156x210 resize, DDS conversion, dedicated runtime wiring, and independent identity/framing review. No ImageGen repaint, advisor icon, high-command icon, dossier portrait, small portrait, fictional substitute, or relabelled likeness is present.

## Consumers

| Consumer | Source and rights | Crop | Runtime |
| --- | --- | --- | --- |
| `MNT_kristo_popovic` | Wikimedia Commons `File:Krsto Zrnov Popovic.jpg`; VRTS ticket `2010091210005142`; CC BY-SA 3.0; original source hash `15ba6d47fc7a2f2d14bfff953d0b9615167e78e7c5f7e6a0666c3fe84c44c363` | Exact crop `[120,40,675,785]`, hash `0a4308b6fe2cf659d86011d5881d7e0bfb2ca8b7632555510e3e8820e2a58fb4` | `GFX_portrait_MNT_independence_wave_kristo_popovic`; DDS hash `472289f3bceb147d37c9aad273606ba7ec6f93b696a454b7c5e60f893cc839bb` |
| `MNT_blazo_jovanovic` | Wikimedia Commons `File:Blazo Jovanovic.jpg`, sourced to Biblioteka Znaci / Muzej revolucije naroda Jugoslavije; Commons records public domain; original hash `919393b924cee9c6de3d1e1fd4e864b4ffed387a3fe60fd52c43bc58b6d682a4` | Tight head-and-shoulders crop `[1058,510,1344,895]`, hash `776faf19785e9b76726c2a448f8fe6b4ca17115aad1aa6710c8901db8e9b7d9d` | `GFX_portrait_MNT_independence_wave_blazo_jovanovic`; DDS hash `e1ab315118cf2a12725acfe769116e822f5e2b3ad2e86804f8ffc35dbe2ed57e` |
| `MNT_independence_wave_mitar_martinovic` | Wikimedia Commons `File:Brigadir Mitar Martinovic.jpg`, extracted from the 1912 Serbian collective work *Ilustrovana ratna kronika Prvog balkanskog rata*; `PD-collective-work|Serbia`; original hash `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76` | Exact crop `[80,90,610,760]`, hash `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e` | `GFX_portrait_MNT_independence_wave_mitar_martinovic`; DDS hash `4551b191f70c15853fd50f6543fd033bd751a88c2b3d714f030e38d42d3fafe0` |

## Review

Parent review PASS: all three images preserve the selected identities and are readable male military head-and-shoulders portraits. The first Jovanovic crop was rejected for excessive torso/background; the final crop above is the tightened replacement. The comparison sheets are `review/mnt_portraits_source_placeholder_native.png` and `review/mnt_portraits_source_placeholder_4x_nearest.png`.

The DDS files are uncompressed 156x210 BGRA surfaces with valid `DDS ` headers and 131168-byte payloads. The two vanilla characters receive the dedicated Event 006 sprites through character-scoped `set_portraits`; no shared generic or vanilla portrait sprite is globally overridden. Martinovic is a new, distinct Event 006 character and is never used to relabel Blazo Dukanovic.

Durable flat source archives, crops, candidates, and processing records are stored under `docs/assets/portraits/006_independence_wave/iw030_montenegro_source_placeholders_2026_08_09/`.
