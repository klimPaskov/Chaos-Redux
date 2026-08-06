# IW-030 Montenegro source-placeholder runtime gate

Date: 2026-08-06.

Scope: bounded review of the existing grounded male portrait evidence for Event 006 IW-030 (MNT), using the accepted unchanged-source to exact-crop to deterministic `156x210` source-placeholder policy. This tranche made no runtime, character, gameplay, allocation, readiness, attestation, flag, localisation, or advisor-icon change.

## Verdict

`SAFE_RUNTIME_PROMOTION = NO`.

The safest retained candidate is Jovan Simonov Plamenac, but he remains `needs_user_review` and cannot be installed against the current IW-030 roster. The source crop and deterministic placeholder are valid evidence; they are not a runtime admission. No DDS was created, no `.gfx` sprite was registered, and no character consumer was changed.

## Candidate and source provenance

| Field | Evidence |
| --- | --- |
| Candidate | Jovan Simonov Plamenac (1873–1944), male Montenegrin/Yugoslav politician, former Minister of Education (1907–1909), Minister of Interior and Foreign Affairs, and Prime Minister of the Kingdom of Montenegro in Exile (17 February 1919–28 June 1921). The retained role source records him alive at the 1936 baseline, but this role/date evidence still needs an independent admission review. |
| Source page | [Wikimedia Commons: Jovan S. Plamenac](https://commons.wikimedia.org/wiki/File:Jovan_S._Plamenac.jpg). The archived raw record is `docs/assets/006_independence_wave/iw030_mnt_leader_source_research_current_2026_08_03/research/commons_jovan_plamenac.raw.txt`. |
| Source attribution and rights | Commons records source `http://www.gov.me/info_vodici/vodici/570/Vodic-kroz-Vladu-Crne-Gore.html`, date range 1914–1916, author `unknown`, and a `PD-old` assertion. The cited gov.me endpoint is currently unavailable, and the author, first-publication chain, and archive accession are unresolved. `PD-old` is therefore not treated as unconditional runtime clearance. |
| Role evidence | `research/jovan_plamenac_role.raw.txt` records the 1873 birth year, 1944 death year, Montenegro offices, and exile premiership. `research/worldstatesmen_montenegro.html` is retained as the related office-list source. These establish a plausible adult male period role but do not close the independent source/role gate. |
| Source master | `docs/assets/006_independence_wave/iw030_mnt_leader_source_research_current_2026_08_03/source_masters/mnt_jovan_plamenac_commons_c1914_1916.jpg`; RGB `217x332`; SHA-256 `8b9d86b03c265ac88660625c2bf3bd24af548659587a05ca2f66f7e46697441d`. |
| Exact crop | `source_crops/mnt_jovan_plamenac_c1914_1916_head_shoulders.png`; RGB `217x332`; decoded crop `[0,0,217,332]`; SHA-256 `e525190ecaa23992584da9bd397918131ecab5307759183ca1c960bd6781da59`. `crop_metadata/mnt_jovan_plamenac_crop.json` reports `decoded_pixels_equal=true`, Pillow `11.1.0`, crop utility v1.0, and matching RGBA equality hashes. |
| Deterministic source placeholder | `source_placeholders/portrait_MNT_jovan_plamenac_source_placeholder_156x210.png`; RGB `156x210`; SHA-256 `4f25cfd11a29dc3afe13e93d907e3f448d4541fd0832de149e6dc4169a7055ab`. `source_placeholders/portrait_MNT_jovan_plamenac_source_placeholder_156x210.json` records centered `ImageOps.fit`, LANCZOS, no recolour, retouch, repaint, or padding, and `runtime = not authorized; evidence only`. |
| Replacement state | `source_placeholder` evidence only. No provider-backed styled-final request was made or supplied, so `replacement_pending` is not used. The source remains in the active event evidence workspace; no new durable archive/runtime basename was promoted while the identity and rights gates are open. |

The source is an unchanged, softly detailed civilian head-and-shoulders photograph. It is visually compatible with the full `156x210` leader convention, but visual compatibility does not cure the unresolved source rights or identity-consumer gates.

The existing placeholder processing JSON had one trailing literal `\n` after its closing brace. That evidence-only metadata defect was removed without changing the PNG or any source pixels. The corrected metadata file is `source_placeholders/portrait_MNT_jovan_plamenac_source_placeholder_156x210.json` with SHA-256 `c2242dfd4853d2ae940d945ddbf40deb330c9f0849c5718fd6786a97e8f574e0`.

## Existing runtime consumer and ownership gate

The installed vanilla MNT carrier has only these recruited character ids in `history/countries/MNT - Montenegro.txt`: `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, and `MNT_blazo_dukanovic` from `common/characters/MNT.txt`.

Their existing large portrait contracts are `GFX_portrait_europe_generic_land_19`, `GFX_portrait_Blazo_Jovanovic`, and `GFX_portrait_MNT_blazo_dukanovic` in vanilla `interface/_leader_portraits.gfx`. The mod has no MNT leader texture or MNT `.gfx` definition, and a runtime-root search found no `Plamenac`, `Jovan Plamenac`, `MNT_plamenac`, or `Simonov` character, history, interface, GFX, or localisation consumer.

Plamenac is not one of the existing MNT identities. Assigning his face to `MNT_kristo_popovic`, `MNT_blazo_jovanovic`, or `MNT_blazo_dukanovic` would relabel a real person and violate the ownership gate. Creating a new `MNT_*` character and history consumer would be a parent-owned roster/design amendment outside this portrait-only tranche. No such amendment is accepted.

Installed-vanilla ownership search covered `Plamenac`, `Jovan Plamenac`, `Jovan_S_Plamenac`, `MNT_plamenac`, and `Simonov` across `common/characters`, `history/countries`, `interface`, and `localisation`; no owner match was found. Current-project runtime roots were searched with the same variants; no match was found.

## Related MNT evidence reviewed

- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v110_2026_08_03/manifest.md` keeps `SAFE_PACKAGE_PROMOTION = NO`. The full native roster remains unresolved: Popović lacks capture-date/photographer/archive evidence, Jovanović retains a creator-versus-unknown-photographer discrepancy, and Đukanović remains an unknown-photographer book reproduction. The distinct Martinović row is not a relabel or runtime admission.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v110_2026_08_03/gfx_handoff.md` explicitly proposes no DDS, `.gfx`, or character edit and keeps all `156x210` candidates evidence-only.
- `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v107_2026_08_02/manifest.md` records Danilo Petrović-Njegoš as a stronger rights/role lead, but only as a distinct proposed identity at `needs_user_review`; it has no runtime consumer and cannot substitute for a native MNT id.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw030_mnt_package_audit_current_2026_08_05.md` remains HOLD / fail-closed. IW-030 is intentionally omitted from central content attestation, and the audit accepts no generic portrait, relabel, fallback, DDS, `.gfx`, history, or advisor-art substitute.

## Reference and processing review

The canonical full leader family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and its `contact_sheet.png` were inspected; all eight references are native `156x210`. The canonical commander family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/` and its contact sheet were also inspected; all nine references are native `156x210`. The Plamenac master, exact crop, and source placeholder were compared at native size and enlarged inspection scale against those role families. Identity and framing are readable, with no generated or repainted detail, but provenance remains independently unapproved.

The existing package review sheet is `docs/assets/006_independence_wave/iw030_mnt_leader_source_research_current_2026_08_03/review/mnt_leader_source_placeholder_contact_sheet.png`. No source image was altered, filtered, or replaced in this tranche.

## Runtime and validation record

| Check | Result |
| --- | --- |
| Source master and crop hashes | Confirmed against the current manifest and crop JSON. |
| Dimensions and modes | Master/crop `217x332` RGB; placeholder `156x210` RGB; no alpha channel, as expected for the opaque leader family. |
| Crop equality | PASS in retained JSON: `decoded_pixels_equal=true`, exact rectangle `[0,0,217,332]`. |
| Placeholder metadata | PASS after removing the trailing literal `\n`; JSON parses and its recorded source/output hashes match the current files. |
| Vanilla reference family | PASS for inspection: leader and commander contact sheets and native `156x210` references inspected. |
| Ownership search | PASS for no Plamenac owner in installed vanilla or current project runtime roots. |
| Runtime texture/GFX search | PASS for no MNT-specific mod DDS or `.gfx` definition; vanilla contracts remain untouched. |
| DDS conversion | Not run because rights, role/identity admission, and runtime consumer gates remain open. |
| Character/history wiring | Not run because Plamenac has no accepted existing consumer and relabelling native MNT ids is forbidden. |
| Package admission/attestation/readiness | Not touched by design. |
| Advisor/high-command/dossier assets | Not created; no such family is authorized for IW-030. |
| Live game/MCP validation | Skipped; no runtime change was made and the package remains fail-closed. |

## Remaining admission blockers

1. **Source rights:** the source page's `unknown` photographer, missing first-publication/archive chain, and unavailable gov.me endpoint must be resolved or explicitly accepted before runtime promotion.
2. **Role/date confirmation:** the retained role text and World Statesmen source show a plausible adult male Montenegrin officeholder, but independent parent admission is still required.
3. **Identity consumer:** Plamenac is a distinct real person absent from the current native MNT roster. A new character identity and consumer would require parent design/character/history ownership; no relabel is permitted.
4. **Full MNT roster:** v110 still leaves the three native consumers at `needs_user_review`, so the package remains outside central attestation even if Plamenac's own source gate later closes.

## Files changed

The following portrait-specific evidence files were changed:

- `docs/assets/006_independence_wave/iw030_mnt_leader_source_research_current_2026_08_03/source_placeholders/portrait_MNT_jovan_plamenac_source_placeholder_156x210.json` (removed a trailing literal `\n`; PNG unchanged).
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw030_mnt_source_placeholder_runtime_gate_2026_08_06.md`

No runtime DDS, `.gfx`, character, history, localisation, flag, gameplay, allocation/readiness, attestation, or advisor-icon file was changed. No fallback or simplification was introduced; runtime promotion is intentionally blocked pending the gates above.
