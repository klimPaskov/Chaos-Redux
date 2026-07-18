# Event 19 Country-Package Live Final Reaudit

**Date:** 2026-07-16  
**Role:** Independent country-package auditor  
**Scope:** Live Event 19 claimant, derivative-country, route, unit-family, combat-trial, AI, identity, asset-routing, progression-isolation, and cleanup implementation

## Verdict

The live Event 19 country package is complete and internally consistent within this audit surface.

| Severity | Findings |
|---|---:|
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |

No fixed-tag fallback, generic identity fallback, unapproved release fallback, country-package simplification, or gameplay blocker was found.

## Ownership boundary: regional flag regeneration

The country-package flag contract is clean in the live source: all 13 derivative identities route across all 7 regions, yielding 91 regional identity routes; the complete current runtime set contains 104 flags at each of the normal, medium, and small sizes (13 generic plus 91 regional), with exact filename parity, expected dimensions, and no missing or extra files.

A separately owned parallel asset-production task is still replacing the 91 regional visual sources and their 273 derived TGA files with independently generated ImageGen results. New-source provenance, visual-style acceptance, and final derived-output acceptance belong to that task's post-generation asset audit. This open production task is deliberately not presented here as completed. It does not alter the clean gameplay, identity-routing, filename, count, or dimensional verdict recorded by this country-package audit.

## Audit matrix

| Surface | Result | Live evidence |
|---|---|---|
| Claimant takeover, failed coup, and territorial revolt | Clean | `common/scripted_effects/019_infantry_spawn_claimant_effects.txt` routes a natural takeover only for an eligible low-control microstate, converts the Event 67 Generalissimo rivalry to a failed coup, and otherwise uses failed-coup or non-microstate territorial-revolt handling. `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt` promotes/retires the exact claimant on takeover and removes the exact failed claimant while restoring lot control on failure. |
| Microstate safety | Clean | Claimant creation requires the exact recorded recreate/prove/delete transfer facility unless its one-time rollback recreation has already been consumed. Microstates do not receive an unsafe territorial split, and takeover is gated by the intended eligibility and control state. |
| Mainland-preferred, island-viable release geography | Clean | `common/scripted_triggers/019_infantry_spawn_triggers.txt` selects controlled, passable, non-capital states; mainland candidates take precedence, while an island becomes viable only when no qualifying controlled mainland state exists. Connected expansion grows from the loyal formation's origin/HQ region. |
| Three release modes | Clean | The live triggers and package effects distinguish ordinary claimant release, anomalous claimant release at the required evolution/registry state, and independent family release. The single-state same-tag family route is separately proved; multi-state claimant/family releases use exact dynamic-country creation. |
| Exact transaction, rollback, and accounting | Clean | `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt` freezes the selected rows and UIDs, recreates and proves the exact destination formations, proves destination territory/core/control, deletes and proves the exact source rows, snapshots commit readiness, commits, and then re-proves global accounting. Pre-commit failure rolls back territory and exact recorded formations. Post-commit failure closes fail-safe. Recovery is explicitly one-use where the engine cannot reconstruct an unrecorded live composition. |
| Dynamic actors; no fixed-tag fallback | Clean | Dynamic country creation uses the current actor as `original_tag` and exact event targets. No fixed country tag is substituted for release. No civil-war fallback is used. The one-state family route stays on the exact current tag only under its separately proved conditions. |
| Identities, cosmetics, leaders, and councils | Clean | All 13 identities have generic cosmetics and exact 7-region variants. Invalid identity/region resolution fails closed. Claimant profiles are region-compatible and fail closed rather than falling back to a mismatched claimant. Player-facing human commanders are created with `female = no`; derivative councils and institutional leaders are also created with `female = no`. Crown promotion requires the exact living male claimant or a successfully proved male claimant transaction. |
| Zombie, ghost, and golem packages | Clean | The registry defines the base zombie as family-only `trainable_and_spawnable`; the ghost and golem entries are `spawn_only`. Only the exact family templates are unlocked. Spawn, reinforcement, and sustain paths are paid, proved, and refunded/rolled back when materialisation fails. No ghost or golem training path was found. |
| Slow ghost decline | Clean | Ghost decay is interval-driven at 180 days, selects one controlled state, uses the configured low rate ladder (0.25% base, 0.20% anchored, 0.15% managed, capped at 0.50%), and records its owner-scoped marker/death meter. It is not an uncontrolled daily mass drain. |
| Focus tree depth, routes, and locks | Clean | The derivative tree contains 45 unique focus nodes: 30 shared nodes plus three 5-node family overlays. Each family exposes 35 nodes. The claimant crown, collective council, and species commander routes are mutually exclusive; claimant breakaways cannot take the collective/species routes. Crown entry and promotion are proof-gated. Leader replacement preserves the appropriate route state. Every focus has AI weighting. |
| Decisions, missions, AI, and expansion | Clean | The package exposes 68 decisions and 14 timed missions, all uniquely identified and AI-weighted where applicable. Twenty-two dynamic AI strategy profiles cover opening, route, family, and route-subchoice behavior. Expansion uses a dynamic neighboring target, excludes unsafe/special/nonhuman/derivative/diplomatically blocked targets, checks state capacity, warns the target, and constructs the exact dynamic war goal without a fixed target fallback. |
| Controlled one-formation combat trials | Clean | Four trial decisions and one trial mission select exactly one formation by recorded UID/ledger proof, use a fixed state pair and one locked defender detachment, and resolve through the dedicated border-war callbacks. Win, loss, cancellation, and timeout each have exact cleanup. No ordinary-battle inference or broad army-leader combat hook substitutes for the controlled trial. |
| Classifiers and progression isolation | Clean | Exact derivative, human-claimant, zombie, ghost, golem, nonhuman, and parent-isolation classifiers are present. Derivatives are special Chaos actors, but only ghost/zombie/golem derivatives classify as nonhuman. Derivative initialization unregisters ordinary evolution membership and clears ordinary participation. No Event 4/5/10 progression call, world-end setter, or super-event mutation was found in the package. |
| Lifecycle and cleanup | Clean | Provider callbacks run before shared teardown; active missions and ideas close; selected formations and owner-scoped markers are cleaned exactly; private ledgers are cleared; cosmetics, classifiers, route/family state, and package variables are proof-gated before final completion. Failed cleanup queues an exact retry rather than silently discarding state. Natural transaction rollback annexing is protected from ordinary annex lifecycle processing. |
| Recurring execution safety | Clean | No daily, weekly, or monthly world-iteration on action was added. Event 19's broad country scans are bounded one-time manifestation/dispatch/setup operations. Recurring derivative work is actor-local, and evolution reconciliation uses the established lifecycle receipt design. |
| Fixed 27 scene slots | Clean | The fixed contract resolves to 20 regional claimant army/muster scenes, 6 massed derivative host/council-as-formation scenes, and 1 neutral massed muster. Visual inspection found no focal person in any slot. The 3 council slots each depict formations rather than a portrait subject. Source, processed, runtime, and sprite wiring all have exact 27-slot parity. |

## Quantitative evidence

| Item | Expected | Observed | Result |
|---|---:|---:|---|
| Unique focus nodes | 45 | 45 | Exact |
| Shared focus nodes | 30 | 30 | Exact |
| Family-overlay focus nodes | 3 x 5 | 15 | Exact |
| Visible nodes per family | 35 | 35 | Exact |
| Decisions | 68 | 68 | Exact |
| Timed missions | 14 | 14 | Exact; all 14 have mission timeouts |
| Ideas | 42 | 42 | Exact |
| Dynamic AI strategy profiles | 22 | 22 | Exact |
| Derivative identities | 13 | 13 | Exact |
| Regions per identity | 7 | 7 | Exact |
| Regional cosmetic routes | 91 | 91 | Exact |
| Generic cosmetic routes | 13 | 13 | Exact |
| Runtime flags per size | 104 | 104 normal / 104 medium / 104 small | Exact current routing set |
| Regional cosmetic localisation keys | 1,365 | 1,365 | Exact |
| Generic cosmetic localisation keys | 195 | 195 | Exact |
| Event 19 localisation keys | — | 2,881 unique of 2,881 | No duplicate keys |
| Custom focus/decision/category icon references | 96 | 96 definitions and 96 extant textures | Exact |
| Event IDs | — | 48 unique across 2 files | Root `chaosx.nr19.1` present |
| Top-level Event 19 scripted effects | — | 1,002 unique | No duplicate definitions |
| Top-level Event 19 scripted triggers | — | 343 unique | No duplicate definitions |
| Fixed visual scene slots | 27 | 27 source / 27 processed / 27 DDS / 27 sprite routes | Exact |
| Processed scene dimensions | 156 x 210 | 27/27 | Exact |
| Processed scene uniqueness | 27 | 27 unique hashes | Exact |
| Runtime scene dimensions/format | 156 x 210 legacy 32-bit BGRA DDS | 27/27 | Exact |
| PNG-to-DDS pixel parity | 27 | 27 exact; 0 mismatches | Exact |

The localisation matrix has complete name/description pairs for all 45 focuses, 82 decisions/missions, and 42 ideas. The Event 19 localisation file is UTF-8 with BOM. Current TGA flag headers are type-2, 32-bit, bottom-left origin with the expected 82x52, 41x26, and 10x7 dimensions.

## Principal implementation surfaces reviewed

- `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_derivative_package_triggers.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_effects.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt`
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`
- `common/script_constants/019_infantry_spawn_derivative_package_constants.txt`
- `common/national_focus/019_infantry_spawn_derivative_focus.txt`
- Event 19 decision, mission, idea, event, on-action, scripted-localisation, cosmetic-tag, interface, and English-localisation files
- Event 19 asset manifests, crosswalks, source/processed contact sheets, processed images, DDS outputs, and runtime flag directories
- The complete Event 19 specification set, route/count matrices, near-completion addendum, improvement-closure addendum, and current implementation/audit handoffs

## Required references consulted

The audit used the repository instructions and the `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-event-assets` skills. The required offline wiki pages were reviewed, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Cosmetic tag, National focus, Division, and Unit. Relevant vanilla effect, trigger, script-concept, script-constant, and character documentation was also checked, together with dynamic-country and state-local border-war precedents in vanilla Romania, Czechoslovakia, and Chinese warlord content.

Optional HOI4 event/focus inspection calls were attempted, but the MCP returned `ARTIFACT_STORAGE_LIMIT` with no files or diagnostics. This was a tooling-storage limitation, not a source diagnostic; direct source, data, binary, and visual inspection supplied the evidence above.

## Files changed by this audit

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_country_package_live_final_reaudit_2026_07_16.md`

No gameplay, localisation, interface, binary asset, workbook, or export file was changed.

## Simplifications, omissions, and blockers

None within the country-package audit. No fallback or reduced substitute was accepted. The independently coordinated regional flag regeneration remains openly separated under its own asset-production ownership as described above; it is not a hidden omission and does not block the live country-package gameplay/routing verdict.
