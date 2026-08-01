# IW-018 ARX Sardinia country-package audit v76

Date: 2026-08-01.

Scope: Read-only audit of the ARX country package, IW-018 runtime admission, and the v75 source ledger plus v76 source-locked portrait repaint package. No gameplay, GFX, localisation, flag, map, asset, or workbook files were changed.

## Executive result

ARX has broad country-package coverage, but IW-018 remains fail-closed and must not be promoted. The decisive runtime blocker is the missing `iw_018` arm in `has_independence_wave_runtime_package_content_attestation_for_execution_id` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:67-82`. The adapter and `iw_018`/`ARX` dispatch branch exist, but both runtime and scenario preflight require the omitted content-attestation proof.

The v76 portrait package provides a visually acceptable source-locked candidate for Emilio Lussu and researched replacement candidates for the unresolved crown and commander consumers. It does not approve the existing names, does not create DDS/GFX wiring, and does not clear package admission.

| Consumer and gate | Status | Finding |
| --- | --- | --- |
| Emilio Lussu (`ARX_sardinian_provisional_assembly`) identity, crop, provenance, HOI4 style, and 156x210 readability | PASS for v76 candidate | The Senate source, exact crop, repaint, candidate PNG, hashes, and review sheet are recorded under `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/`. The candidate preserves the source glasses, facial hair, pose, and clothing. |
| Emilio Lussu runtime promotion | HOLD | The current runtime DDS/GFX is an older withdrawn treatment; v76 has no DDS or `.gfx` edit. The CC BY 3.0 IT source needs attribution in the final release manifest, and the candidate still needs the parent-owned DDS/GFX/character post-wire audit. |
| Exact Vittorio Pala (`ARX_sardinian_crown_consultative_council`) | BLOCKED | v75 found no attributable historical portrait for the exact name. Do not relabel Luigi Arborio Mella di Sant'Elia as Vittorio Pala. |
| Luigi Arborio Mella di Sant'Elia as an explicit crown-route replacement | CONDITIONAL HOLD | Mella is born in Sassari, served as Grand Master of Court Ceremonies for Vittorio Emanuele III, was a royal confidant, and was alive in 1936. The Senate source is CC BY 3.0 IT and is late-bounded before 26 June 1955, not an exact 1936 capture. Accept only after an explicit gameplay/localisation identity change to Mella and attribution review. |
| Exact Gavino Piras (`ARX_gavino_piras`) | BLOCKED | v75 found no attributable historical portrait for the exact name and 1936 mountain-command role. Do not relabel another person as Gavino Piras. |
| Vittorio Vernè as an explicit commander replacement | CONDITIONAL HOLD | The source, crop, rights record, repaint, and army-commander visual review pass. Vernè is a Sardinia-linked 1936 commander but was born in Rome, so this is acceptable only if the design changes from a Sardinian-born commander to a Sardinia-linked Italian commander and the consumer is renamed. Under a strict Sardinian-born requirement, this remains BLOCKED. |
| Advisor art | PASS | `ARX_michele_corda` and `ARX_efisio_satta` intentionally have portraitless advisor blocks. No advisor icon, small portrait, dossier, operative, or commander-miniature derivative is required or authorized. |

Exact Pala and Piras names therefore remain blocked. Mella and Vernè are researched replacement proposals, not silent substitutions. No generated or generic fallback is admissible.

## Country package coverage checklist

| Surface | Result | Evidence and identifiers |
| --- | --- | --- |
| Tag and country shell | PASS | `common/country_tags/006_independence_wave_countries.txt:20` maps `ARX` to `countries/006_independence_wave_ARX.txt`; `common/countries/006_independence_wave_ARX.txt` supplies the graphical shell. |
| Country history and recruitment | PASS by runtime design | `history/countries/ARX - Sardinia.txt` sets `civilian_economy`, `export_focus`, and `volunteer_only`, and recruits `ARX_sardinian_provisional_assembly`, `ARX_sardinian_crown_consultative_council`, `ARX_gavino_piras`, `ARX_michele_corda`, and `ARX_efisio_satta`. No static OOB or production file is expected because the runtime force package owns setup. |
| Map anchor and host | PASS statically; runtime evidence pending | Vanilla `history/states/114-Sardinia.txt` is the Sardinian one-state anchor with ITA ownership, ITA/SPM cores, ports at provinces `11773` and `6891`, an airbase, infrastructure, one industrial complex, victory points, and coal. `has_prepared_independence_wave_iw_018_package_setup` and `independence_wave_setup_iw_018_sardinia` require state `114` ownership/control, capital `114`, and a protected former-host state. |
| Release, transfer, and cleanup | PASS by source contract; runtime execution HOLD | `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:779-826` initializes IW-018; `:962-1010` removes ARX decisions, mission, ideas, flags, variables, and lifecycle state. Runtime transaction evidence remains unavailable while attestation is closed. |
| Politics and routes | PASS | The package installs constitutional, popular/labor, traditional/crown, and emergency/mountain-guard routes, excludes patron/radical routes, and writes route leaders and ideas through the ARX package effects. |
| Focus tree | PASS static coverage | `common/national_focus/006_independence_wave_focus.txt:2951-3028` defines six ARX focuses with route gates, prerequisites, rewards, icons, and AI: municipal ledgers, Cagliari shipping, mountain guards, Italian property, island settlement, and FORM-05 delegation. |
| Decisions and mission | PASS static coverage | `common/decisions/006_independence_wave_mediterranean_decisions.txt:158-293` defines the ARX category, timed authority mission, and eight projects with capital-control, cost, active-project, completion, timeout, cancellation, and AI logic. |
| Ideas and localisation | PASS static coverage | `common/ideas/006_independence_wave_mediterranean_ideas.txt:36-59` defines six ARX lifecycle ideas. Country, parties, character names, advisors, ideas, focuses, decisions, tooltips, AI labels, and report text are present in `localisation/english/006_independence_wave_countries_l_english.yml` and `localisation/english/006_independence_wave_mediterranean_l_english.yml`. |
| Flags and icons | PASS static coverage | ARX base and ideology flags exist. ARX focus and decision sprites, shared Mediterranean idea sprites, and the Event 006 report sprite are registered in `interface/006_independence_wave_mediterranean_assets.gfx`; expected DDS files exist. |
| Dynamic forces and technology | PASS by source contract; runtime execution HOLD | `p18` in `common/script_constants/006_independence_wave_force_package_constants.txt` maps to coastal-maritime profile, military tradition `52`, reinforcement mask `647`, navy inheritance mask `1`, and no air inheritance. `common/scripted_effects/006_independence_wave_force_effects.txt` supplies dynamic divisions, stockpiles, host technology/research inheritance, and approved navy/air transfer. |
| AI and playability | PASS static coverage | `common/ai_strategy/006_independence_wave_mediterranean.txt:81-153` contains ARX survival, founding-restraint, host-threat, civic-maritime, and crown/guard profiles with build and emergency weights. |
| Formable, ambition, and league | PASS by source contract; runtime execution HOLD | IW-018 setup selects the Mediterranean Island League family, ARX Mediterranean-island ambition, FORM-05 candidacy, and network-gated delegation. The formable triggers require package state and control proofs. |

## File surface checklist

The inspected ARX surfaces are:

- `common/country_tags/006_independence_wave_countries.txt` and `common/countries/006_independence_wave_ARX.txt`.
- `history/countries/ARX - Sardinia.txt` and vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/114-Sardinia.txt`.
- `common/characters/006_independence_wave_mediterranean_characters.txt`.
- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`, `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt`, and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
- `common/national_focus/006_independence_wave_focus.txt`, `common/decisions/006_independence_wave_mediterranean_decisions.txt`, `common/decisions/categories/006_independence_wave_mediterranean_categories.txt`, and `common/ideas/006_independence_wave_mediterranean_ideas.txt`.
- `common/script_constants/006_independence_wave_force_package_constants.txt`, `common/scripted_effects/006_independence_wave_force_effects.txt`, and `common/scripted_triggers/006_independence_wave_force_triggers.txt`.
- `common/ai_strategy/006_independence_wave_mediterranean.txt`.
- `interface/006_independence_wave_mediterranean_portraits.gfx`, `interface/006_independence_wave_mediterranean_assets.gfx`, the ARX flag files, and the existing full-size ARX leader/commander DDS files.
- `events/006_independence_wave_mediterranean.txt`, including `chaosx.nr6.22` founding incident and `chaosx.nr6.25` route incident.
- `docs/assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/` and `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/`.

## Missing or stale surfaces

1. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:67-82` omits `constant:independence_wave_package_id.iw_018` from the content-attestation OR list. The adapter at `:10-33` and `iw_018`/`ARX` branch at `:133-140` do not bypass the top-level attestation requirement.
2. Existing `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds`, `...vittorio_pala.dds`, and `...gavino_piras.dds` are 156x210 uncompressed DDS files, but the current Pala/Piras identities are not source-cleared and the old Lussu treatment is withdrawn. Their presence is not approval evidence.
3. v76 has processed PNG candidates only. It deliberately makes no final DDS or `.gfx` edits. The parent must own any post-identity-change character/localisation/GFX/DDS wiring and post-wire hash audit.
4. `processing_metadata/portrait_ARX_vittorio_verne_156x210.json` contains the literal subject string `Vittorio Vern?` instead of `Vittorio Vernè`. The v76 audit and manifest use the correct accented spelling. Correct this evidence metadata before any release-manifest or admission decision.
5. The v76 Vernè crop metadata points to a prior v15 source path while retaining the v15 master and crop hashes. This is byte-consistent evidence but should be normalized to the current source-package path during documentation reconciliation.
6. `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:326` says Emilio Lussu is “sourced, processed, and wired” while the current source-of-truth map and v76 audit keep visual admission withdrawn/HOLD. Reconcile this stale statement before admission.

## Portrait and role recommendation

The parent may accept Lussu as the current civilian-route identity after the final source attribution, DDS conversion, stable GFX wiring, and post-wire audit. The parent may accept Mella only by explicitly changing the crown character name, localisation, and consumer identifiers to Luigi Arborio Mella di Sant'Elia; the portrait must not remain under `ARX_vittorio_pala`. The parent may accept Vernè only by explicitly changing the commander identity and design wording to a Sardinia-linked Italian commander; if Sardinian birth is mandatory, retain the commander gate as BLOCKED and continue research. The exact Pala and Piras consumers have no current source evidence and must remain closed.

## Package admission gates

| Gate | Status | Evidence |
| --- | --- | --- |
| Tag uniqueness and identity | PASS | The installed tag audit records IW-018 `ARX` as distinct from SPM/Sardinia-Piedmont with `no_identity_block`; see `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_08_01.md:70-72,126`. |
| Setup, anchor, former host, politics, focus, decisions, ideas, forces, AI, and cleanup | PASS static contract | The ARX package effects/triggers and surfaces listed above are present and internally cross-referenced. |
| Source identity and portrait roles | HOLD/BLOCKED | Lussu is v76 visual/provenance PASS but not runtime-promoted; exact Pala/Piras are BLOCKED; Mella/Vernè require explicit identity and role changes. |
| Asset promotion and post-wire evidence | HOLD | No v76 DDS, `.gfx` edit, character rename, localisation rename, or final release attribution exists. |
| Runtime content attestation | BLOCKED | IW-018 is absent from the compile-time attestation list, so `is_independence_wave_runtime_package_preflight_ready` and scenario preflight cannot pass. |
| Final IW-018 admission | BLOCKED | Do not add attestation or promote portraits until the source roster, identity/name changes, visual evidence, DDS/GFX wiring, and full package audit are accepted. |

## Validation performed

- Read the required repository guidance, offline Paradox wiki pages, and relevant vanilla documentation before inspecting the package.
- Traced `ARX`, `iw_018`, state `114`, ARX characters, portrait consumers, focus ids, decision ids, idea ids, AI strategies, force profile `p18`, Form-05 hooks, events, and cleanup through the exact source files listed above.
- Verified the v76 candidate PNG dimensions, modes, hashes, source-master hashes, crop hashes, and review-sheet chain with Python/Pillow metadata inspection.
- Visually reviewed the v76 Lussu, Mella, and Vernè candidate/review-sheet images; no text, UI, modern prop, or obvious identity-destroying facial reconstruction defect was observed at native candidate size.
- Confirmed no advisor, small, dossier, operative, or commander-miniature asset is required by the ARX contract.
- Attempted `python .tools/audit_hoi4_country_tags.py`; the broad installed-workshop scan timed out after 120 seconds with no output. This is recorded as inconclusive, not a pass. The narrower installed-tag report and exact ARX file tracing above supplied the identity evidence.
- No game launch, save/load, live runtime, or Technology Tree Viewer evidence was performed. The installed package exposes no Technology Tree Viewer, so technology-tree visual evidence remains unavailable.

## Changes made

- Added only this handoff report: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw018_arx_package_audit_v76_2026_08_01.md`.
- No gameplay, character, GFX, DDS, localisation, flag, map, force, AI, workbook, or source-asset files were changed.

## Remaining bounded actions for the parent

1. Decide whether the crown route may become explicitly Luigi Arborio Mella di Sant'Elia and whether the commander route may become explicitly Vittorio Vernè under a Sardinia-linked, not Sardinian-born, role.
2. If accepted, update character ids/names, localisation, GFX sprite names, DDS files, and release attribution as one identity-consistent change; do not relabel Pala/Piras.
3. Correct the Vernè metadata subject string and stale source path, and reconcile the resume packet’s Lussu “wired” statement.
4. Run the independent post-wire portrait and complete country-package audit, then consider adding IW-018 to the compile-time content-attestation registry only after every gate passes.
5. Keep exact Pala/Piras and strict Sardinian-born commander requirements BLOCKED if no source evidence is found; no fallback is authorized.

## Simplifications, omissions, and blockers

IW-018 is incomplete for runtime admission. The package has no accepted exact Pala or Piras portrait sources, no final v76 DDS/GFX wiring, no post-wire asset hashes, and no runtime content attestation. These are deliberate fail-closed holds, not substitutions. No gameplay patch was appropriate within this portrait/package audit scope.
