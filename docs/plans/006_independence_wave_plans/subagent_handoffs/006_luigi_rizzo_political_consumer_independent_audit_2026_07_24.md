# Event 006 Sicily Luigi Rizzo political-consumer independent audit

Audit date: 2026-07-24.

Auditor: independent sourced-visual reviewer, separate from the producer package and the prior Luigi Rizzo army/corps-command audit.

Scope: the current male `ASX_luigi_rizzo` `civilian.large` country-leader consumer for the Sicilian Straits Security Directorate.

This audit does not authorize the previously reviewed army/corps-command consumer, a navy-leader consumer, an advisor/dossier card, `_small` texture, female variant, alternate identity, fallback, or raw/resized source image.

## Verdict

The current political-consumer gate is **PASS with disclosure** for `ASX_luigi_rizzo` as a male civilian-large country leader of the fictional Sicilian Straits Security Directorate.

The full IW-019 runtime-admission verdict remains **HOLD** because package-status records conflict and the IW-019 automatic-pool content attestation remains closed in the package re-audit.

| Gate | Verdict | Evidence and limits |
| --- | --- | --- |
| Provenance and rights | **PASS with disclosure** | The unchanged attributed master is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/sicily_trial_01/source_masters/asx_luigi_rizzo_rear_admiral_1935.jpg`, SHA-256 `aa113393b9b51ed481bfa485aaf729e867c20c6a364b41d3f8999b0dc2c8663e`, with the Commons 1935 Rear Admiral Luigi Rizzo record, *Medaglie d'oro della Grande Guerra* provenance, Italian Navy corroboration, and Commons PD-Italy/PD-1996/US notes recorded in `manifest.md` and the prior independent audit. The exact crop is `(70,0,333,354)` in `source_masters/ASX_luigi_rizzo_source_crop_preview.png`; the retained raw ImageGen repaint, processed candidate, prompt, package DDS, and comparison sheet are separately retained and hash-ledgered. The photographer is unnamed and the parent must retain the cited attribution and re-check derivative-use terms before release. |
| Exact-person likeness and identity | **PASS** | Native inspection of the source master, exact crop, raw repaint, processed `156x210` candidate, and the retained comparison sheet preserves Rizzo's broad square face, swept dark hair, heavy brows, thick moustache, direct gaze, stern expression, age, pose, Regia Marina uniform, shoulder cords, sash, medals, and crosses. No genericization, beautification, symmetrization, face substitution, unsupported facial detail, or identity-changing uniform replacement was observed. Identity remains the non-compensable gate. |
| HOI4 painted leader style | **PASS** | `processed_png/ASX_luigi_rizzo.png` is an opaque full `156x210` painted portrait with modeled facial planes, deliberate brushwork, controlled slate blue-gray background, readable head-and-shoulders/upper-chest framing, and no photographic-only or merely resized finish. I compared it against the canonical country-leader family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and the curated leader sheet at `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/contact_sheet.png`; the darker, more naval-command texture remains within the HOI4 leader family. The earlier commander-style reference does not by itself authorize a commander consumer. |
| Civilian-large political/security-director role fit | **PASS with disclosure** | `common/characters/006_independence_wave_mediterranean_characters.txt:174-179` defines `ASX_luigi_rizzo` as male with `portraits = { civilian = { large = GFX_portrait_ASX_independence_wave_luigi_rizzo } }` and only a despotism `country_leader` role. `history/countries/ASX - Sicily.txt:19` recruits it, `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:499` promotes it only for the military-government route, and `localisation/english/006_independence_wave_mediterranean_l_english.yml:19,122-123,192-193` names Luigi Rizzo and the Straits Security Directorate. The offline Character modding rules define `civilian.large` as the large country-leader portrait slot, not a requirement for civilian clothing, and the canonical leader family includes a uniformed Mannerheim precedent. The portrait therefore fits a security-directorate political office, but this is an alternate Sicilian officeholder use of a real admiral and must not be presented as a historical claim that Rizzo led this fictional state. |
| Ownership and safe wiring | **PASS for this consumer only** | Current active ownership is the single `ASX_luigi_rizzo` character and `GFX_portrait_ASX_independence_wave_luigi_rizzo` sprite. `interface/006_independence_wave_mediterranean_portraits.gfx:41-42` points to `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_rizzo.dds`; the runtime DDS is `156x210`, 131,168 bytes, a valid legacy one-level BGRA texture, and SHA-256 `659c819547559f50025fb3007cd5c60947a150ca4673238cc179dc2f0867d714`, matching the package DDS and pixel-identically decoding to the approved processed PNG. `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt:51,55` confirms the character exists and is not a corps commander. Vanilla searches found only incidental Italy ship-production strings named Luigi Rizzo, not a character, portrait, or GFX owner; the prior audit also recorded no active Chaos Redux duplicate. No `_small`, advisor, dossier, navy, or corps-command consumer is authorized by this handoff. |

## Package and reference evidence

The audited package is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/sicily_trial_01/`.

The prior independent visual/provenance audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_sicily_trial01_portrait_visual_provenance_audit_2026_07_22.md`; it passed Rizzo provenance, identity, and painted style but explicitly authorized only the then-existing army/corps-command large consumer.

The current package re-audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw019_sicily_country_package_reaudit_2026_07_24.md`; it records the current civilian-large role split as internally correct but blocks political-portrait admission pending this separate consumer audit.

The source/crop/raw/processed/painted comparison is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/sicily_trial_01/contact_sheets/source_crop_result_style_comparison.png`.

The current package hashes independently rechecked for Rizzo are source `aa113393b9b51ed481bfa485aaf729e867c20c6a364b41d3f8999b0dc2c8663e`, crop `02394a103358298a06d929df76323a4a0310c5d28ed2db68654475dbd5b94403`, raw repaint `589bcfa1b1f53ad2619515aa867cae222d5f4c2d19065a8fdc9b3b843b1a0fdc`, processed PNG `a950f3737ba12dca1dd21372347e0999e0a80166be5076024a1f41ee9a6ebafd`, prompt `ee10d8b6fbcb7dae1d9cbec4f92031aff808ba0646aaf5ac75fd7678d43003ea`, package DDS `659c819547559f50025fb3007cd5c60947a150ca4673238cc179dc2f0867d714`, and comparison sheet `5823f7008a5589a52e16522f41064c4653f2a2b5e562161ae296a2ecd17c8fcf`.

Portrait semantics were checked against `paradox_wiki/Character modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/_documentation.md`, and the relevant `effects_documentation.md` entries for `recruit_character`, `set_portraits`, and country-leader portrait handling.

The canonical style rules and role families were checked in `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`, `CATALOG.md`, `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/README.md`, and `REFERENCE_MANIFEST.md`.

## Blockers and parent follow-up

1. `sicily_trial_01/metadata.json` still says `status: needs_user_review`, while `manifest.md` and `gfx_handoff.md` say `independently_approved_and_wired`; reconcile this contradiction before treating the package as durably admitted.
2. IW-019 remains outside the automatic runtime content-attestation set, as recorded by the 2026-07-24 country-package re-audit; this handoff does not change that gate.
3. Preserve the Commons/Italian Navy attribution and the unnamed-photographer/PD-Italy rights disclosure; do not silently upgrade the rights claim.
4. Do not infer authorization for the prior army/corps-command consumer, a navy-leader role, or any new portrait family from this political-consumer PASS.

No gameplay, character, history, GFX, localisation, workbook, source, processed PNG, DDS, manifest, or skill file was edited by this audit; only this handoff is new.
