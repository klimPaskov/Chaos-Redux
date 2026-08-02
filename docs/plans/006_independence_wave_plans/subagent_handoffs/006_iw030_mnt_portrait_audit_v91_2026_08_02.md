# IW-030 Mitar Martinovic independent portrait audit v91

Date: 2026-08-02.

Scope: independent asset review only. No gameplay, character, history, localisation, `.gfx`, DDS, tag, attestation, or runtime files were changed. The full evidence record is `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/review/mnt_mitar_martinovic_v91_v6_v7_independent_audit.md`.

## Evidence and verdict

The unchanged archival master is `source_masters/mnt_mitar_martinovic_1912_chronicle.jpg` (684x1135 RGB, SHA-256 `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76`). The exact head-and-shoulders crop is `source_crops/mnt_mitar_martinovic_1912_head_shoulders.png` (530x670 RGB, SHA-256 `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e`) and its decoded-pixel equality proof remains true for `[80,90,610,760]`.

The v6 raw repaint/candidate hashes are `b9f1c5e0e28f0a1e12ebce80b14b935cfe31c32232a784c249bfe15c3073b80a` and `4165007d39d70f45780e3615e5e000ea2d12296141d8d79710fcaedf59e9fac7`. The v7 style-only refinement raw repaint/candidate hashes are `d30891ac10f58dd080b2eeb85081efec9314d6e7e849ab91f8d01f9c05733b6d` and `6b14b6cb8ef48b9c2b256bc331026448450e6dfbd409f4a9d19da6a8c6254501`. The v7 native candidate is 156x210 and uses a full-width no-padding crop followed by Pillow LANCZOS; v6 uses center crop `[27,0,1086,1412]` followed by Pillow LANCZOS.

Independent review at native and exact 4x nearest-neighbour scales against FIN Mannerheim, ICE Bjornsson, ENG Montgomery, GER Manstein, and ITA Badoglio references finds:

- identity/likeness: PASS for v6 and v7;
- source/crop linkage: PASS;
- male presentation: PASS;
- provenance/rights: PASS_WITH_NOTE, preserving the 1912 *Ilustrovana ratna kronika* / Serbian National Library / Commons `PD-collective-work|Serbia` chain and its site-terms caveat;
- role/date: PASS_WITH_NOTE, because Martinovic is a documented Montenegrin general and minister who lived through the 1936 start, while the photograph is from 1912;
- HOI4 style/framing: PASS_WITH_NOTE for v7 and `needs_user_review` for v6. V7 is preferred because its lighter neutral painted background aligns better with the canonical reference family, although both retain a strong brush-texture and colorization note;
- overall: `needs_user_review` with ownership/runtime `BLOCKED_PENDING_PARENT`.

Review artifacts are `review/mnt_mitar_martinovic_v91_v6_v7_portrait_audit_sheet.png` (3240x2824 RGB, SHA-256 `e6d87aaa05904511a82fcbeb195072af9f37764a5882cd123195d30de0bd9365`) and the full markdown audit linked above.

## Admission boundary

Use v7 as the stronger review candidate, but do not convert it to DDS or wire it. The parent must obtain human style approval, preserve source/archive attribution, rerun the exact/variant identity-ownership search, and explicitly accept Mitar Martinovic as a new role-correct MNT roster identity. Do not relabel `MNT_kristo_popovic`, and do not admit IW-030 from this portrait evidence alone. No Event 006 advisor, high-command, dossier, or small portrait was created.
