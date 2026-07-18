# Event 006 Pacific Country-Package Admission Audit — 2026-07-18

## Scope and disposition

This audit covers the Pacific tranche of Event 006 Independence Wave:

- IW-173 HAW (vanilla `HAW`, exact dormant-package gate)
- IW-179 FSM (vanilla `FSM`, exact dormant-package gate)
- IW-184 HBX (registered Event 006 California carrier tag)
- PFX (FORM48 cosmetic identity only)
- FORM48 Pacific integration of HBX, HAW, and FSM

**Status: PASS for country-package admission review; no P0/P1 patch was required.**

**Promotion recommendation: HOLD / FAIL-CLOSED.** Keep IW-173, IW-179, and IW-184 out of the runtime content attestation and keep FORM48 readiness/attestation flags unset. This is an explicit boundary from the tranche design, not a package defect. The country surfaces are internally ready for a parent-owned admission decision, but this audit does not promote runtime eligibility.

No gameplay files were changed by this audit. No commit was created.

## Country-package coverage checklist

| Surface | HAW / IW-173 | FSM / IW-179 | HBX / IW-184 | Result |
|---|---|---|---|---|
| Tag identity and registration | Vanilla tag retained; no custom registration | Vanilla tag retained; no custom registration | `HBX` registered once in `common/country_tags/006_independence_wave_countries.txt` | PASS |
| Runtime package identity | Exact `original_tag = HAW`, `independence_wave_package_id = IW173` | Exact `original_tag = FSM`, `independence_wave_package_id = IW179` | Exact `original_tag = HBX`, `independence_wave_package_id = IW184` | PASS |
| Anchor state and capital | State 629, owned/controlled at runtime | State 684, owned/controlled at runtime | State 378, owned/controlled at runtime | PASS |
| Dormant/start setup | Vanilla dormant country history preserved | Vanilla dormant country history preserved | Dormant shell only; runtime setup owns state/politics | PASS |
| Politics and leaders | Vanilla leader roster preserved; no HAW leader mutation | Event 006 inter-island congress chair is package-gated | Event 006 civic convention chair is package-gated | PASS |
| Focus loading | Full Event 006 tree only under exact IW-173 gate; guarded generic-tree cleanup | FSM keeps its own tree and uses additive overlay | Full Event 006 tree under exact IW-184 gate | PASS |
| Decisions and missions | HAW project surface present and gated | Four audited government decisions plus project surface | HBX project surface and carrier actions present | PASS |
| Ideas and assets | Shared existing idea sprites; vanilla HAW flag | Shared existing idea sprites; vanilla FSM flag | Two package ideas; complete HBX flag ladder and portrait | PASS |
| Military, technology, industry, supply | Runtime force package mapping `coastal_maritime` / tradition 62; vanilla history baseline | Runtime force package mapping `coastal_maritime` / tradition 46; vanilla history baseline | Runtime force package mapping `regular_defectors` / tradition 76; dynamic carrier setup | PASS |
| AI and playability | Exact IW-173 strategy; airbase/air-sea priorities | Exact IW-179 strategy; no stale country references | Exact IW-184 strategy; host-threat and carrier priorities | PASS |
| FORM48 membership | Sovereign autonomous member only after current-generation consent/ledger proof | Sovereign autonomous member only after current-generation consent/ledger proof | Carrier and postformation owner under exact PFX/ledger proof | PASS |

## File-surface checklist and findings

### Identity, country files, and setup

- `common/country_tags/006_independence_wave_countries.txt`: `HBX = "countries/006_independence_wave_HBX.txt"` is the sole Event 006 Pacific country registration. No duplicate HAW/FSM registration and no PFX country tag registration were found.
- `common/countries/006_independence_wave_HBX.txt`: dormant HBX shell uses the intended graphical culture and map colour; no unrelated starting setup is injected.
- `history/countries/HBX - Event 006 Country Shell.txt`: recruits only `HBX_independence_wave_civic_convention_chair`; state, politics, OOB, and production remain runtime-owned.
- Vanilla `history/countries/HAW - Hawaii.txt` and `history/countries/FSM - Micronesia.txt` remain the source of truth for dormant vanilla tags. HAW keeps its three vanilla leaders; FSM remains dormant with its vanilla baseline.
- `common/countries/006_independence_wave_formable_cosmetics.txt`: PFX is cosmetic-only and has no country tag registration.

### Runtime triggers, effects, dispatch, and force mapping

- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`: exact package wrappers, HAW leader-preservation checks, FSM government-route checks, and full/additive preparation gates are internally consistent.
- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`: IW-173, IW-179, and IW-184 setup/cleanup are exact-tag and exact-generation guarded. HAW cleanup restores `generic_focus` only when the current tree is the Event 006 tree; FSM cleanup does not overwrite its tree; HBX cleanup retires only the Event 006 chair.
- `common/scripted_effects/006_independence_wave_execution_effects.txt`: runtime release transfers the planned anchor state and adds the target core; no static map ownership override is required.
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt` and `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt`: reservations are exact (HAW 629, FSM 684, HBX 378) and remain attestation-gated.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` and `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`: Pacific adapters exist, but compile-time content attestation intentionally excludes IW-173/IW-179/IW-184; Soviet Collapse origins remain separate.
- `common/scripted_effects/006_independence_wave_force_package_constants.txt`, `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt`, and `common/scripted_effects/006_independence_wave_force_effects.txt`: profile/tradition mappings and repeat guards are valid for all three packages.

### Politics, leaders, portraits, flags, and advisors

- `common/characters/006_independence_wave_pacific_characters.txt`: HBX and FSM use male canonical large portraits and institutional chair names. No Event 006 advisor or high-command role is defined. HAW's vanilla roster is untouched.
- `interface/006_independence_wave_pacific_portraits.gfx`: only the two approved large portrait sprites are registered.
- Runtime portrait DDS files are present at canonical 156x210 dimensions (DDS headers are 210x156 storage orientation) and match the approved hashes:
  - HBX `7CD86794C10C9621F90340490E2D57B72EDD01B6C785240DB943FE9253AF145E`
  - FSM `64DB23C13F8F3F488079EA24CA4D8EF9326BBB3FD9ABBC94EE9B9251B004AE29`
- HAW and FSM have no mod flag files by design and therefore use vanilla flags. HBX and PFX each have complete normal/medium/small five-file flag ladders. PFX is the audited flat federal cosmetic identity.
- No custom Event 006 advisor icons, advisor portraits, small leader sprites, or corps-commander replacements were found. Protected BAY/RHI DDS files were not touched.

### Focus, decisions, ideas, localisation, and assets

- `common/national_focus/006_independence_wave_focus.txt`: full tree id is `independence_wave_focus_tree`; full/additive loading gates match package contracts.
- `common/national_focus/006_independence_wave_pacific_focus.txt`: seven HBX and seven HAW focuses are present; FSM remains additive. Focus prerequisites, route exclusions, rewards, and host-collapse locks are consistent with the re-audit.
- `common/decisions/006_independence_wave_pacific_decisions.txt`, `common/decisions/categories/006_independence_wave_pacific_categories.txt`, and `common/decisions/006_independence_wave_form48_decisions.txt`: Pacific projects, the four FSM government decisions, human invitation choices, paid recurring programs, timed responses, and dissolution action are present and gated.
- `common/ideas/006_independence_wave_pacific_ideas.txt` and `interface/006_independence_wave.gfx`: all package ideas resolve to existing shared sprites; no missing country-specific advisor art is implied.
- `interface/006_independence_wave_pacific_focus_icons.gfx`: all 14 base/shine focus icon pairs resolve to the generated DDS package.
- `localisation/english/006_independence_wave_pacific_l_english.yml` and `localisation/english/006_independence_wave_countries_l_english.yml`: scoped reference audit found 141 referenced localisation keys and zero missing keys. HAW/FSM vanilla country strings remain vanilla-owned.

### FORM48 transaction and stale-generation safety

- `common/scripted_triggers/006_independence_wave_form48_triggers.txt` and `common/scripted_effects/006_independence_wave_form48_effects.txt` require exact carrier/member tags, anchors, PFX family, generation pointers, sovereign status, consent, and founding ledger rows before mutation.
- HAW/FSM become sovereign autonomous members; no annexation or transfer is used. Reciprocal military access and guarantees are directional and guarded against duplicates.
- Paid/timed recurring programs have material costs, member fulfil/withhold responses, strain/failure outcomes, and dissolution cleanup. The current-generation binding trigger and frozen-row cleanup prevent stale cross-generation relations.
- `common/decisions/categories/006_independence_wave_form48_categories.txt` keeps invitations and compact actions hidden unless their exact carrier/member triggers pass.

## Map and state setup

Vanilla state inspection confirms the intended anchors:

- `378-California.txt`: USA-owned vanilla state; HBX receives the runtime state/core transaction.
- `629-Hawaii.txt`: USA-owned vanilla state with HAW core, airbase, and naval base; IW-173 runtime release is exact-state gated.
- `684-Caroline Islands.txt`: JAP-owned vanilla state with FSM core, airbase, naval base, and coastal bunker; IW-179 runtime release is exact-state gated.

No mod state override, capital mismatch, stale owner/controller reference, or invalid reserved-state claim was found. Candidate reservation lists are planner inputs; the final package anchors remain exact 378/629/684.

## Validation evidence

- `python .tools/audit_event6_allocator.py`: PASS; 149 publishers, 126 automatic/high-chaos selectable, SCN008 ranked 138, automatic counts 3/4/5/7/10, and all anchors reach compact → extended → lock.
- `python .tools/audit_hoi4_country_tags.py --workshop-root C:/does_not_exist_chaosx --local-mod-root C:/does_not_exist_local`: exit 0, zero collisions, 50 identity matches. This targeted run intentionally skipped installed workshop/local roots; the result is supplemental, not a replacement for the prior full installed-root tag audit.
- Scoped localisation-reference audit over the Pacific country package: 141 references, zero missing keys; both touched localisation files retain UTF-8 BOM.
- Portrait DDS inspection: both canonical large portraits are present at 156x210 and match the approved handoff hashes; no advisor/small sprite references exist.
- Prior tranche handoffs independently report PASS for focus, FORM48 architecture, FORM48 decisions/missions, localisation, postformation/human invitation, and Pacific visual assets.
- Read-only `hoi4_map_inspect` could not produce an artifact because the installed map model exceeded its fixed 500,000-record budget (`MAP_MODEL_BUDGET_BLOCKED`, observed 501,137 records). This is a tooling limitation only; state-file and runtime-anchor review above remains complete.

## Missing or stale surfaces

None found within the requested Pacific country-package scope. No P0/P1 patch is recommended.

## Simplifications, omissions, and blockers

- No gameplay simplification or fallback was introduced.
- HAW/FSM custom flags and Event 006 advisor/portrait assets were intentionally not created because the tranche explicitly requires vanilla flags and zero custom advisor art.
- IW-173/IW-179/IW-184 runtime attestation and FORM48 readiness remain unset by design; this audit does not promote them.
- The map MCP artifact is unavailable due to the fixed model-budget ceiling described above.

## Parent action

Treat this country-package review as **admission-ready but fail-closed**. Keep runtime content attestation and FORM48 readiness disabled until the parent completes the separate final admission decision and its required cross-system review. No gameplay rollback is needed.
