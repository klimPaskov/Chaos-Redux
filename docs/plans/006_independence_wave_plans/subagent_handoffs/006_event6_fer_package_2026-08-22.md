# IW057 Far Eastern Republic country-package handoff

Date: 2026-08-22

Status: HOLD / FAIL-CLOSED / INCOMPLETE.

Scope: Event 006 country-package audit for the Far Eastern Republic (FER, IW-057) only.

Authority: `docs/specs/006_independence_wave_specs/`, `docs/plans/006_independence_wave_plans/006_iw057_fer_identity_roster_symbol_receipt_addendum_2026_08_15.md`, the package-local source files, the offline Paradox wiki, and the installed vanilla documentation.

## Disposition

The package-local FER tranche is present and remains fail-closed. No source gameplay, identity, flag, portrait, cosmetic-tag, central-attestation, allocator, or shared-system change was made in this audit.

The package has a registered vanilla `FER` tag and an Event 006 package-local adapter, but it is not admitted to the central Event 006 runtime. The package still lacks an independently cleared identity/roster receipt, a runtime portrait and character consumer, an approved flag/symbol and cosmetic-tag receipt, typed probability evidence, and current live MCP sign-off. These are admission blockers, not reasons to weaken gates.

The vanilla `FEV` Far Eastern Republic Revival package is Event 005 content and remains a separate origin. Its fictional leaders, committee portrait, and history must not be reused as Event 006 FER identity evidence.

## Country-package coverage checklist

| Surface | Finding | Status |
| --- | --- | --- |
| Tag and loader | `FEV = "countries/Far Eastern Republic Revival.txt"` is registered in `common/country_tags/chaosx_countries.txt`; Event 006 uses the registered `FER` package identity in the IW-057 planner and package triggers. | Present, origin-separated |
| Event 006 adapter and central admission | Package-local triggers/effects, shared focus callbacks, decisions, ideas, AI, and localization exist. No central adapter, attestation, preflight, SCN-008, or Join admission was added for IW-057. | Local only; not admitted |
| State and map setup | Ordered runtime anchors are states 408 and 409; the package requires ownership/control and a capital anchor. State 563 is not an Event 006 runtime anchor. No map write was attempted. | Source guards present; live MCP blocked |
| Host and collision safety | Former-host and Soviet-origin exclusions, exact package identity, anchor ownership, current-generation, and lifecycle guards are present in the package triggers. | Present; not central proof |
| Leader and roster | No Event 006 FER character, institutional roster, or leader source has cleared the parent identity/rights gate. The addendum proposes `FER_independence_wave_pyotr_nikiforov` as a historical male candidate, but it remains source-placeholder and rights-pending. | Blocking hold |
| Portraits | The archived Nikiforov source and research artifacts are not a runtime portrait. There is no approved 156x210 runtime DDS, portrait GFX entry, or character wiring for Event 006 FER. | Blocking hold |
| Flag and symbol | No Event 006 FER cosmetic tag or runtime flag family exists. `FER-H0-1920-FLAG` remains rights-unresolved; `FER-H1-1921-CONST-FLAG` is only a comparison fallback requiring explicit parent authorization. | Blocking hold |
| Politics and parties | Package setup applies the existing FER package party/ideology ladder and baseline laws only after the roster gate; cleanup restores the package baseline. | Present, gated |
| Ideas and decisions | Seven package ideas, one 420-day mission, and ten serialized project decisions are localized and guarded by the package setup/current-generation/anchor checks. | Present, gated |
| Focus | The shared `independence_wave_focus_tree` has FER callback routes and localization. There is no dedicated FER tree or missing-tree patch to add. | Present, shared |
| Forces and starting setup | `regular_defectors` force package level 67 maps to railway/coastal/regular-defector forces. Runtime setup remains downstream of the identity/command-roster gate; no unsupported Event 006 OOB was invented. | Present, gated |
| Technology, industry, and supply | No Event 006-specific technology-tree surface or major industry rewrite was added. Railway, port, infrastructure, supply, and force setup are handled by existing package effects and decisions. | Package-local only |
| AI and probabilities | Four FER AI strategy blocks are present. The settled-compact block lacks the same setup/current-generation guard used by the other blocks, but it was not changed because the required baseline and `probability_compare` pass through `chaosx_ai_probability_auditor` is unavailable. | Audit risk; no patch |
| Cleanup | FER cleanup removes package ideas, decisions, ledgers, package flags, and the package/shared roster receipt. It does not clear the parent-owned identity-rights receipt. There is no absent character/cosmetic cleanup to wire. | Present, fail-closed |
| Localization and assets | Package party, idea, decision, mission, tooltip, and focus localization exists. Character, portrait, cosmetic-tag, flag, and symbol localization/runtime asset wiring does not. | Partial; blockers remain |

## File surface checklist

- `common/country_tags/chaosx_countries.txt`: vanilla `FEV` registration is separate Event 005 content; no Event 006 `FER` source file was invented.
- `history/countries/FEV - Far Eastern Republic Revival.txt`: capital 408 and fictional Event 005 buffer-committee leaders; not an Event 006 identity source.
- `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt`: exact IW-057 package, ordered anchors, capital, host, generation, lifecycle, roster, and setup gates.
- `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt`: roster checkpoint, setup, package initialization, and cleanup effects.
- `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt`: IW-057 loader and reservation path.
- `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt`: exact planner availability and 408/409 owner checks.
- `common/national_focus/006_independence_wave_focus.txt`: shared `independence_wave_focus_tree` and FER callbacks.
- `common/decisions/categories/006_independence_wave_far_eastern_categories.txt`: FER package decision category.
- `common/decisions/006_independence_wave_far_eastern_decisions.txt`: 420-day mission and ten serialized projects.
- `common/ideas/006_independence_wave_far_eastern_ideas.txt`: seven FER package ideas.
- `common/ai_strategy/006_independence_wave_far_eastern.txt`: railway-port survival, host restraint, settled compact, and coastal emergency strategy blocks.
- `localisation/english/006_independence_wave_far_eastern_l_english.yml`: existing package-facing localization; no Event 006 character or cosmetic keys.
- `docs/events/006_independence_wave/far_eastern_republic_package.md`: package-local contract and explicit no-central-admission statement.
- `docs/assets/portraits/006_independence_wave/iw057_fer_pyotr_nikiforov_source_original.jpg`: archived research source only; not a runtime asset.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw057_fer_portrait_identity_source_research_2026_08_15.md`: source-placeholder and rights-pending portrait handoff.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw057_fer_symbol_flag_research_handoff_2026_08_15.md`: unresolved H0/H1 flag/symbol research handoff.
- `docs/plans/006_independence_wave_plans/006_iw057_fer_identity_roster_symbol_receipt_addendum_2026_08_15.md`: accepted package-local identity/roster/symbol receipt design; it is not central admission authority.

## Concrete findings

### Identity, roster, and portrait

`common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt:113-118` currently makes `has_independence_wave_fer_command_roster` depend on the parent-owned `independence_wave_iw_057_identity_rights_cleared` and `independence_wave_iw_057_command_roster_ready` receipts. That is the correct fail-closed outcome while no actual Event 006 FER character, institutional roster, or portrait consumer has cleared review.

`common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt:353-363` only publishes the package checkpoint and shared command-roster receipt after both parent receipts are already present; it does not mint evidence. `:367-435` keeps setup downstream of that checkpoint, and `:449-495` clears package-derived state without clearing the parent identity receipt.

The proposed historical candidate is `FER_independence_wave_pyotr_nikiforov` with portrait sprite `GFX_portrait_FER_independence_wave_pyotr_nikiforov` and basename `portrait_FER_independence_wave_pyotr_nikiforov`, but those identifiers are not wired. The archived source is a research artifact, not permission to create a final or fallback portrait. No opposite-gender pairing is present because no Event 006 character was created.

### Flag, symbol, and cosmetic tag

The proposed cosmetic identifier is `FER_INDEPENDENCE_WAVE_PROVISIONALX`, but no cosmetic-tag file, flag TGA family, GFX entry, or runtime manifest exists. H0 is a historical continuity candidate with unresolved rights; H1 is a comparison-only constitutional reconstruction. Adding either to runtime would invent an unapproved asset path and weaken the package gate.

### Map and state setup

`common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt:26-45,76-110` requires the exact package, current generation, anchor ownership/control, former-host protection, and capital anchor. `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt` contains the narrow 408/409 planner owner checks. No map rewrite was needed or attempted.

The current bounded HOI4 map inspection for states 408, 409, and 563 timed out after 180 seconds, including a state-only retry. Existing dated package artifacts remain context only and are not a fresh current MCP sign-off.

### Focus, decisions, ideas, and localization

The shared tree and package callback routes are already present in `common/national_focus/006_independence_wave_focus.txt`; the ten serialized projects and 420-day mission are already present in `common/decisions/006_independence_wave_far_eastern_decisions.txt`; and the seven package ideas are already present in `common/ideas/006_independence_wave_far_eastern_ideas.txt`. No narrow source repair was identifiable without changing the accepted design.

The current focus inspection/render route and event inspection/render route did not return before termination. No dedicated FER focus tree, Event 006 FER event root, or technology-tree viewer surface was added. The installed package exposes no Technology Tree Viewer, so that remains an unresolved validation limitation.

### AI and probability

`common/ai_strategy/006_independence_wave_far_eastern.txt:21-69` contains four AI strategy blocks. The `settled_compact` block should be revisited only through the required scenario-specific probability workflow because it does not repeat the setup/current-generation guard. The direct probability MCP route did not return, and `chaosx_ai_probability_auditor` is absent from the callable tool inventory. Therefore no AI weight was changed and no quantitative probability claim is made.

### Allocator, central runtime, and cleanup

The allocator and cleanup audit found no safe local change that could promote IW-057. Existing allocator/attestation/central-runtime gates remain authoritative. Package cleanup is local and does not clear the parent identity-rights receipt. No central allocator, attestation, shared registry, or cleanup code was edited.

## Exact blockers for parent review

1. Parent identity decision and rights clearance are missing for Nikiforov or an approved institutional roster. The source-placeholder handoff remains HOLD.
2. A portrait worker-owned runtime package is missing: approved identity evidence, portrait-specific wiring, 156x210 HOI4-style runtime output, DDS, GFX, manifest, and character source are all absent.
3. Flag/symbol rights and design approval are missing. H0 remains rights-unresolved, H1 requires explicit parent acceptance, and no neutral Event 006 cosmetic runtime family exists.
4. The raw runtime consumer trigger and receipt sequence cannot be safely added before the actual character and cosmetic assets exist. Introducing unknown character or asset tokens would be speculative and could break loading.
5. Typed probability fixtures and the mandatory `chaosx_ai_probability_auditor` baseline/compare pass are unavailable. The direct probability route also did not return.
6. A central Event 006 adapter/attestation/preflight/SCN-008/Join proof for IW-057 is absent. Package-local gates must remain fail-closed.
7. Current live MCP map, focus, event, and probability routes timed out or returned no result. Retained older artifacts cannot substitute for a fresh route result.
8. The installed package has no Technology Tree Viewer, so technology-tree inspection cannot be completed through the mandated viewer route.

## Validation and recovery evidence

- `python -B .tools/audit_event6_country_api.py` passed with broad 242 unique tags, 191 resolved carriers, 0 missing, and 0 duplicates.
- `python -B .tools/audit_event6_flags.py` passed with 102 registered Event 006 tags, 102 complete flag families, and 0 incomplete families.
- `python -B .tools/audit_event6_allocator.py` passed its publisher, selectable-package, runtime-adapter, attestation, reservation-group, standalone-witness, protected-state, ordering, and Event 005-to-Event 006 checks. The output still identifies IW-057 as package-local/not centrally admitted.
- No map write, `hoi4.map_rewrite`, apply, rollback, or recovery operation was attempted.
- No Hearts of Iron IV launch or live playtest was performed.
- No probability compare was run because no weighted patch was made and the required auditor route is unavailable.
- No source gameplay patch was made; only this handoff document was added. The concurrently modified older handoff `006_iw057_fer_country_package_audit_2026-08-20.md` was not edited.

## Changed files and identifiers

Changed file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_fer_package_2026-08-22.md`.

No tags, state IDs, leaders, parties, focus IDs, localization keys, formables, assets, allocator gates, central runtime files, or AI weights were changed.

## Next safe action

Keep IW-057 HOLD / FAIL-CLOSED. Route the historical identity and portrait package to `chaosx_portrait_creator` only after parent identity and rights direction is supplied, obtain a separately reviewed flag/symbol decision, then add the raw consumer receipts and runtime wiring in a later bounded tranche. Run the required country/focus/event/map/probability MCP inspections and typed probability compare before any central promotion.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui`. No asset or portrait production was initiated because the accepted evidence and rights gates remain unresolved.
