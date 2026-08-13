# Event 006 IW-004 Brittany Country-Package Implementation Handoff

> **Portrait-specific supersession (2026-07-16):** The old BRI portrait
> manifest, hashes, and commander-small evidence are superseded by the
> male-HOI4 package manifest and final independent audit. Gameplay
> implementation findings remain preserved; the Debeauvais rights blocker is
> still current.

Date: 2026-07-15
Country/package: `BRI` / `IW-004` / state `14`
Implementation owner: `/root/event6_bri_package`
Parent integration owner: `/root`

## Outcome

The bounded Brittany package is implemented across setup, identity, politics, forces, characters, ideas, focuses, decisions, mission pressure, AI, former-host relations, Celtic regional ambition, final package validation, cleanup, localisation, portraits, and package documentation.

The package remains deliberately fail-closed at the Event 006 framework level. `IW-004` is registered in the narrow package adapter and has its immutable `IW-004`/`BRI` availability and runtime-preflight identity proofs. It is absent from content attestation and SCN008 scenario preflight. This tranche does not set any runtime-content-attestation or scenario-readiness flag.

The implementation is exact to the installed-map binding: original tag `BRI`, package key `IW-004`, capital/anchor/territorial state `14`, retained former host, and Celtic Congress `FORM01` only. No allocator, cluster, Event 014, Event 015, or Event 019 file was changed.

## Implemented package

### Identity, setup, and force profile

- The setup gate refuses a living/meaningful existing Brittany and refuses to overwrite a meaningful non-Event-006 focus tree.
- Brittany starts under Maurice Duhamel's democratic family and retains the former-host relationship for the French asset settlement.
- The package uses the accepted coastal-maritime force row without reinterpretation:
  - force profile: `5`
  - military tradition: `58`
  - reinforcement mask: `1543`
  - inheritance mask: `1` (naval inheritance permitted; air inheritance excluded)
  - research-sensitive flag: `0`
- The package is confined to state `14`; no other state is granted, claimed, cored, transferred, or required by BRI package script.
- Setup installs the full Event 006 framework only because vanilla BRI has no bespoke meaningful tree beyond the generic tree.

### Founding compact and pressure

- Visible package values:
  - `independence_wave_bri_language_compact`: starts at `30`, stable at `60`
  - `independence_wave_bri_coastal_command`: starts at `25`, stable at `60`
- Both values are clamped to `0..100` by shared package logic.
- The 480-day mission `independence_wave_bri_hold_breton_settlement_together` resolves only when both values reach the stable threshold; expiry applies the documented package failure state.
- Lifecycle ideas are mutually refreshed between:
  - `bri_divided_ports_and_language_state`
  - `bri_bilingual_maritime_compact`

### Political routes and human roster

Five allowed framework routes receive distinct governments, party identities, route ideas, AI posture, and player-facing decisions:

| Framework route | Government decision | Route idea |
| --- | --- | --- |
| Constitutional | `independence_wave_bri_ratify_federalist_compact` | `bri_federalist_civic_charter` |
| Popular council | `independence_wave_bri_charter_dock_rail_fisheries_councils` | `bri_dock_rail_fisheries_councils` |
| Traditional | `independence_wave_bri_entrust_regionalist_union` | `bri_regionalist_cultural_compact` |
| Emergency military | `independence_wave_bri_establish_joint_coastal_command` | `bri_joint_coastal_command` |
| Patron client | `independence_wave_bri_accept_protected_ports_mandate` | `bri_protected_ports_mandate` |

The radical-sovereignty route is explicitly excluded. Olier Mordrel is never installed as the package government.

The roster reuses the authentic vanilla BRI human character/advisor set and official portraits where available, including Yann-Morvan Gefflot, Morvan Marchal, Olier Mordrel, Maurice Duhamel, and the existing BRI advisor roster. Package readiness specifically requires the vanilla advisor IDs `BRI_coi`, `BRI_stc`, `BRI_acd2`, `BRI_nccr`, and `BRI_mt`.

Two fictional but human, single-person HOI4-style package figures were added for roles not covered by the historical roster:

- `BRI_independence_wave_civic_delegate` — Tangi Kerbrat, civic delegate/oligarchism route role
- `BRI_independence_wave_coastal_commandant` — Jodoc Tanet, coastal commandant/despotism route role and corps commander

The civic delegate is intentionally one distinctive individual following the corrected design brief. It is not a council composite, institutional emblem, substitute flag, or fallback portrait.

### Decisions, projects, focuses, diplomacy, and ambition

The category is `independence_wave_bri_brittany_category`. Its 15 entries comprise the founding mission, four founding/settlement projects, the mutually exclusive maritime-force choice, five route-government projects, durable independence, the Celtic port corridor, and the Celtic delegation congress:

- `independence_wave_bri_hold_breton_settlement_together`
- `independence_wave_bri_charter_breton_gallo_services`
- `independence_wave_bri_reopen_ports_fisheries_board`
- `independence_wave_bri_integrate_sailors_territorial_guards`
- `independence_wave_bri_settle_french_asset_ledgers`
- `independence_wave_bri_prioritize_inherited_flotilla`
- `independence_wave_bri_hold_inland_mobile_reserve`
- `independence_wave_bri_ratify_federalist_compact`
- `independence_wave_bri_charter_dock_rail_fisheries_councils`
- `independence_wave_bri_entrust_regionalist_union`
- `independence_wave_bri_establish_joint_coastal_command`
- `independence_wave_bri_accept_protected_ports_mandate`
- `independence_wave_bri_codify_durable_independence`
- `independence_wave_bri_open_celtic_port_corridor`
- `independence_wave_bri_convene_celtic_delegation`

The five package focuses are:

- `independence_wave_bri_charter_ports_fisheries_focus`
- `independence_wave_bri_establish_breton_gallo_services_focus`
- `independence_wave_bri_integrate_sailors_guards_focus`
- `independence_wave_bri_settle_french_accounts_focus`
- `independence_wave_bri_convene_celtic_delegation_focus`

Focus and decision paths both make the founding compact reachable without free political power, units, or equipment. The French-ledger project uses the retained former-host scope. The Celtic delegation selects only shared `FORM01` and runs its shared preparation transaction: frozen ledgers and the vote are resolved there, a package reward is granted only on `transaction_ready`, and final `KCX` commitment remains with the separate shared proclamation. No `FORM02`, `FORM03`, `FORM04`, or North Atlantic path is exposed by the BRI package.

### Package entry points

The package defines and wires these principal entry points:

- `can_initialize_independence_wave_iw_004_package`
- `has_prepared_independence_wave_iw_004_package_setup`
- `has_complete_independence_wave_iw_004_package_setup`
- `independence_wave_setup_iw_004_brittany`
- `independence_wave_validate_iw_004_brittany`
- `independence_wave_cleanup_iw_004_brittany`
- `independence_wave_dispatch_brittany_package_setup`
- `independence_wave_dispatch_brittany_package_final_validation`
- `independence_wave_dispatch_brittany_package_cleanup`

Cleanup removes the mission/decision entries, package ideas, route ideas, package variables, all package flags, and the BRI radical-route exclusion flag. The two generated package characters remain registered but are harmless outside the exact package gates; retaining them also preserves guarded repeat initialization. Cleanup does not remove shared Event 006 state owned by another package or framework layer.

## Files added

### Gameplay and wiring

- `common/script_constants/006_independence_wave_brittany_constants.txt`
- `common/scripted_triggers/006_independence_wave_brittany_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_brittany_package_effects.txt`
- `common/decisions/categories/006_independence_wave_brittany_categories.txt`
- `common/decisions/006_independence_wave_brittany_decisions.txt`
- `common/ideas/006_independence_wave_brittany_ideas.txt`
- `common/ai_strategy/006_independence_wave_brittany.txt`
- `interface/006_independence_wave_brittany_portraits.gfx`
- `localisation/english/006_independence_wave_brittany_l_english.yml`

### Documentation

- `docs/events/006_independence_wave/northern_western_europe_packages.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_bri_country_package_implementation_2026_07_15.md`

### Final portrait assets

- `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`
- `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds`
- `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant_small.dds`

### Asset-production package

The complete source/provenance/review handoff lives under `docs/assets/006_independence_wave/bri_package_2026_07_15/` and contains:

- `manifest.md`
- `gfx_handoff.md`
- `prompt.md`
- `source_png/portrait_BRI_independence_wave_civic_leader_source.png`
- three processed PNGs
- two metadata JSON records
- two role-specific review sheets
- three decoded-DDS verification PNGs
- `contact_sheets/006_bri_runtime_portraits_contact_sheet.png`

## Files modified narrowly

- `common/national_focus/006_independence_wave_focus.txt` — adds only the five BRI focus nodes.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` — adds only BRI setup, final-validation, and cleanup dispatch calls.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` — registers `IW-004` in the package adapter and exact runtime identity preflight; content readiness remains closed.
- `common/scripted_triggers/006_independence_wave_package_triggers.txt` — adds the immutable `IW-004`/`BRI` availability proof without adding a readiness wrapper.
- `docs/assets/006_independence_wave/manifest.md` — appends the BRI portrait source-of-truth entry.

No allocator, cluster, on-action, Event 014, Event 015, or Event 019 file was edited.

## Portrait wiring and provenance

Sprite names:

- `GFX_portrait_BRI_independence_wave_civic_commission`
- `GFX_portrait_BRI_independence_wave_coastal_commandant`
- `GFX_portrait_BRI_independence_wave_coastal_commandant_small`

Runtime DDS verification:

- civic large: `156x210`, BGRA
- commandant large: `156x210`, BGRA
- commandant small: `65x67`, BGRA

SHA-256 evidence:

| Artifact | SHA-256 |
| --- | --- |
| Civic source PNG | `A0A11A95778E3CA3BD32D731B739BC05AE9272BADC5126D8EC11F72D3D252522` |
| Coastal-commandant source PNG | `36649988955A9DAAE3192EA27FA4252105F7C6B10272E651D9968F67A0972D2E` |
| Civic DDS | `64AE374585C2A8B3A26BBD9A1E8880E182FDAFA93540BFB84E6C6D87647AB6B4` |
| Commandant large DDS | `F1603D707170002E7729C535E6DDD990CDFCC7E03F221684E1E6C821F12366C1` |
| Commandant small DDS | `12C1A20D2CC1234895E7AF557BDA9BAF7CDDCA58593527194B5EDAD3AF058684` |
| Corrected small review sheet | `89FE6926F62A567FB959E163D01C4243787EF4A44DAEF0D8051BB6B0A4390F69` |

The parent visually reviewed and approved both the corrected single-human civic leader and the coastal commandant contact sheet. The older four-person institutional BRI image is not wired anywhere in this package.

Vanilla BRI Gwenn-ha-du flags are reused. No new cosmetic tag is created by this package, so the Event-006 `X` suffix rule is not implicated.

## Validation and balance evidence

- All new/touched Clausewitz blocks are balanced and the BRI package calls resolve.
- All 79 `constant:` references used by the package resolve to declared script constants.
- BRI package script definitions and all five focus IDs are unique; every BRI focus prerequisite resolves.
- Localisation coverage includes the category, mission, decisions, focuses, effects/tooltips, ideas, parties, and both generated characters. The file is UTF-8 with BOM and follows repository key style.
- All three BRI portrait textures exist and every BRI GFX token resolves to the registered sprite.
- The decoded DDS files match the intended runtime dimensions and BGRA pixel format.
- The corrected Jodoc Tanet army-small dossier is separately composed at `65x67`, with runtime SHA-256 `12C1A20D2CC1234895E7AF557BDA9BAF7CDDCA58593527194B5EDAD3AF058684`.
- State-isolation review found only state `14` in BRI package conditions/effects.
- Formable-isolation review found `FORM01` only in BRI gameplay. `FORM02`, `FORM03`, `FORM04`, and North Atlantic are absent.
- The accepted force constants were rechecked against the source row: profile `5`, tradition `58`, reinforcement mask `1543`, inheritance mask `1`, research-sensitive `0`.
- Every route's ideology-popularity assignment totals `100`.
- Focus-only progress reaches language `60` and command `65`; decision-only progress reaches language `60` and command `70`. Both paths can therefore satisfy the `60/60` mission requirement before the 480-day deadline without a route-specific dead end.
- Cleanup symmetry covers all 15 category entries, every package variable, every package idea, every BRI package flag, and the package-set radical exclusion flag.
- No BRI package file directly grants equipment, divisions, units, or political power. The flotilla/reserve choice is a modifier/priority tradeoff, not a repeatable resource loop.

### Readiness proof

The expected fail-closed state was verified directly:

| Gate | `IW-004` present |
| --- | --- |
| Package adapter registry | Yes |
| Content attestation | No |
| Runtime identity preflight | Yes, immutable proof only |
| SCN008 scenario preflight | No |

No runtime-content-attestation or SCN008 readiness claim is made by this handoff.

## Simplifications, omissions, and blockers

### Package implementation

No gameplay simplification or fallback was used inside the bounded BRI package. The five accepted routes, state binding, former-host settlement, force profile, AI posture, focuses, decisions, mission, lifecycle, Celtic `FORM01` ambition, cleanup, localisation, and portrait wiring are present. The fictional civic delegate and coastal commandant are deliberate individual human roles required by the package design, not stand-ins for omitted historical leaders.

### Debeauvais portrait-rights blocker

A distinct Célestin Lainé/Debeauvais-era individual portrait was not produced or wired. The rights-cleared 1928 group image was too weak to support an identifiable individual portrait, while sharper 1932/1933 candidates lacked a defensible United States public-domain basis. No generated likeness, substituted person, misleading crop, DDS, or sprite was created. This is an explicit unresolved rights/provenance blocker, not a silent fallback. Existing vanilla BRI character art remains the only historical-character art used by the package.

### Shared FORM01 dependency

The BRI package selects the existing shared `FORM01` Celtic Congress architecture and does not redefine it. The post-repair operational re-audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form01_04_operational_reaudit_2026_07_16.md` passes FORM-01's invitation binding, connection proof, deterministic mutation construction, symmetric cleanup, identity, flags, and Event 5 isolation. `006_form01_04_readiness_promotion_2026_07_16.md` records the exact promoted family bundle. IW-004 automatic and SCN-008 admission remain separate and closed.

### Independent audit handoff

The independent BRI audit is recorded in `006_bri_country_package_audit_2026_07_15.md`; its superseded congress and army-small findings are closed by the later parent repair and `006_bri_ajx_commit_readiness_reaudit_2026_07_16.md`. This document does not claim whole-Event-006 certification or open IW-004 admission.

## Skills and references used

Repo skills used:

- `chaos-redux-events`
- `chaos-redux-focus-trees`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`

Required offline Paradox wiki pages, vanilla script documentation, vanilla BRI country/history/character/party/flag references, and vanilla generic-focus precedent were consulted before implementation. No web Paradox-wiki source was used.

## Git and ownership

No commit was created. The parent owns final diff review, independent audit follow-up, shared FORM01 dependency reconciliation, readiness/attestation decisions, and any later commit.
