# IW-019 Sicily final admission re-audit

Date: 2026-07-24.

Audit baseline: Rizzo political-consumer audit commit `cc703e4de4844a81928f43b1170794c66b1a5007` (`Audit Luigi Rizzo political portrait consumer`) and parent metadata reconciliation commit `8e455cd5b60c6f13e3d954289e4de844e768028f` (`Reconcile Sicily portrait consumer approval`).

The prior package audit is `docs\plans\006_independence_wave_plans\subagent_handoffs\006_iw019_sicily_country_package_reaudit_2026_07_24.md` and the separate Di Benedetto audit is `docs\plans\006_independence_wave_plans\subagent_handoffs\006_sicily_di_benedetto_trial01_independent_audit_2026_07_24.md`.

This re-audit re-read the current Sicily trial metadata, manifest, GFX handoff, both independent visual audits, the prior IW-019 package audit, current ASX character/history/GFX/trigger/effect files, and the runtime DDS/processed-PNG files.

No gameplay, asset, localisation, readiness, map, or workbook file was edited.

## Final verdict

The prior static IW-019 country-package PASS remains valid.

The current Luigi Rizzo civilian-large political consumer is independently authorized **PASS with disclosure** for the fictional Sicilian Straits Security Directorate, and the disclosure is now present in the current metadata, manifest, and GFX handoff.

Vincenzo Di Benedetto remains the sole ASX army-large corps commander, with the exact emergency-role wording preserved.

The current Sicily portrait metadata/status contradiction is closed: `metadata.json`, `manifest.md`, and `gfx_handoff.md` all describe the package as independently approved and wired, cite the Rizzo political-consumer audit, and carry the same role limitation and fictional-office disclosure.

The **only remaining runtime admission hold** found in this re-audit is that `iw_019` is absent from the shared content-attestation trigger `has_independence_wave_runtime_package_content_attestation_for_execution_id`.

Parent promotion recommendation: **YES, conditionally on adding the exact `iw_019` attestation entry.** No additional country-package, portrait-role, metadata, asset, roster, map, focus, decision, force, AI, or host-survival blocker was found.

## Re-audit checklist

| Surface | Result | Evidence |
|---|---|---|
| Identity and package binding | PASS | `ASX`, package `iw_019`, anchor state `115`, Sicily identity, and reservation group `RG-115` remain consistent across the prior package audit, active country/tag files, package triggers, and installed-map binding row. |
| Territory, capital, origin, and host survival | PASS | The prior state/history inspection remains unchanged: state `115` is Sicily, the package uses it as capital/anchor, and the execution/preflight paths preserve the former host and Italy's capital state `2`. |
| History and roster | PASS | `history\countries\ASX - Sicily.txt` recruits Sturzo, Lanza di Scalea, Rizzo, Di Benedetto, Lo Giudice, and Messina; no stale active `ASX_salvatore_licata` reference remains. |
| Politics and route consumer | PASS | Rizzo is promoted only by `independence_wave_install_asx_military_government` as despotism and is the current civilian-large country leader for the fictional security directorate. |
| Rizzo visual consumer | PASS with disclosure | `cc703e4de` independently passes provenance, identity, HOI4 painted style, and civilian-large political/security-director role fit, while explicitly disclaiming a historical claim that Rizzo led this fictional state and disallowing corps, navy, advisor, dossier, and `_small` consumers. |
| Di Benedetto role | PASS | `ASX_vincenzo_di_benedetto` has only an army-large portrait and a corps-commander block; package triggers assert `is_corps_commander = yes`; its localisation remains “retired Sicilian general recalled for the synchronized independence emergency.” |
| Other ASX characters | PASS | Sturzo and Lanza remain civilian-large country leaders; Giuseppe Lo Giudice and Leone Messina remain portraitless political advisors; all six active ASX characters have male metadata. |
| Portrait metadata and status | PASS | Current `sicily_trial_01\metadata.json` is `independently_approved_and_wired`, references both the package audit and Rizzo consumer audit, and records Rizzo's civilian role and disclosure. Current `manifest.md` and `gfx_handoff.md` match that status and role. |
| Runtime portrait GFX | PASS | `interface\006_independence_wave_mediterranean_portraits.gfx` contains exactly four full ASX portrait sprites, all four runtime DDS paths exist, and no forbidden advisor/dossier/`_small`/female token is registered. |
| Runtime DDS and PNG identity | PASS | All four runtime DDS files remain 156x210 and pixel-identical to their approved processed PNGs; hashes are recorded below and match the prior audit evidence. |
| Flags, ideas, focus, decisions, incidents, localisation | PASS | No related gameplay or asset source changed after the prior package PASS; its focus, decision, event, idea, GFX, localisation, and flag checks remain applicable. |
| Forces, technology, industry, supply, and AI | PASS | The prior `regular_defectors`/p19 force mapping, military-tradition 65, dynamic starting-force transaction, AI route/survival blocks, and host inheritance checks remain unchanged. No custom technology tree is claimed. |
| Form05, host, diplomacy, and cleanup | PASS | The prior ASX Form05/Mediterranean island league, host-route, Italian-property, patron, and cleanup checks remain unchanged. |
| Runtime admission | HOLD only on shared attestation | Adapter and exact IW-019/ASX preflight branches are present, but the shared content-attestation OR list still omits `iw_019`. |

## Metadata and disclosure reconciliation

`docs\assets\006_independence_wave\sourced_portrait_refinishes_2026_07_22\sicily_trial_01\metadata.json` now reports `status: independently_approved_and_wired`, includes both independent audit paths, assigns Rizzo the role `country leader / Sicilian Straits Security Directorate`, and records the disclosure that this is an alternate political use of a real Sicilian admiral for a fictional office with no historical claim that he led the state.

`docs\assets\006_independence_wave\sourced_portrait_refinishes_2026_07_22\sicily_trial_01\manifest.md` now reports `independently_approved_and_wired`, cites the separate current-consumer audit, and says Rizzo has no corps-command consumer.

`docs\assets\006_independence_wave\sourced_portrait_refinishes_2026_07_22\sicily_trial_01\gfx_handoff.md` now identifies Rizzo as a male country leader for the Sicilian straits-security government, cites the current consumer audit, and repeats the no-corps-command limitation.

The previous `needs_user_review` versus `independently_approved_and_wired` contradiction is therefore closed in the current trial package. The older source-of-truth/resume prose elsewhere still contains archival pre-reconciliation wording, but it is not active metadata or a runtime gate and is not an admission blocker in this narrow audit.

## Role and asset evidence

The current character file has the following role split:

- `ASX_luigi_rizzo`: `gender = male`, `civilian = { large = GFX_portrait_ASX_independence_wave_luigi_rizzo }`, one despotism `country_leader`, and no army, navy, or corps-commander block.
- `ASX_vincenzo_di_benedetto`: `gender = male`, `army = { large = GFX_portrait_ASX_independence_wave_vincenzo_di_benedetto }`, one corps-commander block, and no civilian country-leader block.
- `ASX_giuseppe_lo_giudice` and `ASX_leone_messina`: male political advisors with no portrait block.

Targeted role assertions passed for Rizzo civilian-only, Di Benedetto army/corps-only, portraitless advisors, male metadata, and absence of ASX female metadata.

The active GFX file contains exactly four full ASX portrait entries and no `_small`, advisor, dossier, or female variant entry. Active gameplay/history/localisation references contain no stale `ASX_salvatore_licata`, `ASX_vincenzo_lanza`, or `ASX_sebastiano_restivo` name.

## Runtime DDS hash and pixel-equality evidence

| Subject | Runtime DDS SHA-256 | Approved processed PNG SHA-256 | Dimensions | Pixel-equal after RGBA decode |
|---|---|---|---|---|
| Luigi Sturzo | `4768e69316d2a03754be052143c68a157902c6953d99ce9389472ed1ada52e57` | `cef2e7ac3c7548a012bea3f6f009aff6c892774cc70126262b1d190e2cb41ff4` | 156x210 | YES |
| Pietro Lanza di Scalea | `7d1201f05a7189001b88a9d7aa9b5e2ed565379cbd30f2fe170ef6aaa245475a` | `0e1b84ac901ac5c14ee029a7d4222e0f5eebe396c801a5604c684bb00d5ff650` | 156x210 | YES |
| Luigi Rizzo | `659c819547559f50025fb3007cd5c60947a150ca4673238cc179dc2f0867d714` | `a950f3737ba12dca1dd21372347e0999e0a80166be5076024a1f41ee9a6ebafd` | 156x210 | YES |
| Vincenzo Di Benedetto | `bc709fe8d00916a60da4b7445e872a746a41901f3c619502824b078dbf7ec173` | `37d7256285abef55cb9b81ee6a3ac04aae8e337297120a85de6c99c489e77108` | 156x210 | YES |

The three Sicily trial-01 DDS hashes match the current `sicily_trial_01\hashes.sha256` and GFX handoff, and the Di Benedetto DDS hash matches its independent audit/runtime handoff. No byte or pixel drift was found.

## Runtime hold evidence

`common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt:20-22` keeps the IW-019 adapter registered, and `:104-106` retains the exact IW-019/ASX preflight branch.

`common\scripted_triggers\006_independence_wave_triggers.txt:497-504` still calls the exact IW-019 tag/preflight wrapper for ASX and state `115`.

`common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt:43-50` currently attests `iw_001`, `iw_004`, `iw_007`, and `iw_017`; it does not attest `iw_019`.

The shared preflight invokes that attestation, so the automatic IW-019 wrapper remains false until the exact `iw_019` clause is added. No other runtime admission omission was found in the active adapter, exact-tag, anchor, or scenario branches.

The installed binding row still records IW-019's intended `automatic_pool_ready`/`ready_automatic` disposition and state/host facts; this declarative row does not override the runtime attestation gate.

## Validation performed

- `python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, and 138 ranked selectable packages, with the expected Event-005-before-Event-006 order.
- JSON/Markdown metadata checks confirmed the approved status, Rizzo audit reference, civilian role, disclosure, and matching manifest/GFX status text.
- Targeted role parsing confirmed Rizzo civilian-large only, Di Benedetto army-large corps-only, two portraitless advisors, male metadata, and no ASX female role metadata.
- Active GFX parsing found four full ASX portrait sprites, all four runtime DDS files present, and zero forbidden `_small`, advisor, dossier, or female tokens.
- Pillow DDS decoding and SHA-256 checks confirmed all four runtime files remain 156x210 and pixel-identical to the approved processed PNGs.
- The prior package audit's focus, decision, event, localisation, flag, force, AI, host, and Form05 checks remain valid because neither metadata reconciliation commit changed those gameplay surfaces.

Live HOI4 startup/campaign execution, map rendering, MCP map writes, and Technology Tree Viewer validation were skipped. The installed tooling exposes no Technology Tree Viewer, and this task explicitly forbids changing readiness/gameplay files.

## Admission handoff

Parent may promote `iw_019` by adding the exact package id to the shared content-attestation OR block after reviewing this handoff. The package-level audit, Rizzo consumer audit, Di Benedetto command role, metadata/status reconciliation, runtime DDS chain, and forbidden-asset checks provide no remaining blocker.

The only remaining hold is the deliberate omission of `iw_019` from `has_independence_wave_runtime_package_content_attestation_for_execution_id`.
