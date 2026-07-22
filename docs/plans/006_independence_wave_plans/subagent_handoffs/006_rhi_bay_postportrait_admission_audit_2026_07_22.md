# IW-008 RHI / IW-009 BAY post-portrait country-package admission audit

Date: `2026-07-22`

Status: `static_package_audit_passed_runtime_admission_blocked`

Scope: post-replacement audit of the Rhineland (`RHI`, IW-008) and Bavaria (`BAY`, IW-009) packages after the sourced male leader portraits were wired. The protected `portrait_RHI_josef_friedrich_matthes.dds` and `portrait_BAY_rupprecht_of_bavaria.dds` assets were treated as immutable. No portrait, manifest, resume-packet, tag-audit, or skill file was changed.

## Disposition

The country packages are internally complete for static content, setup, mechanics, and asset wiring. Both remain fail-closed and must **not** be re-admitted to automatic runtime execution or SCN-008 at this time. The authoritative content attestation is deliberately empty:

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:42-44`

```text
has_independence_wave_runtime_package_content_attestation_for_execution_id = {
	always = no
}
```

The runtime and scenario preflights require that attestation (`:52`, `:140`), so the adapter registry and capacity branches are present but cannot execute either package. This is an admission-control blocker, not a country-package defect. No local patch is warranted.

| Package | Country | Static package audit | Runtime / SCN-008 admission | Recommendation |
| --- | --- | --- | --- | --- |
| IW-008 | RHI, Rhineland | Pass | Blocked by empty attestation | Do not admit |
| IW-009 | BAY, Bavaria | Pass | Blocked by empty attestation | Do not admit |

## Country package coverage checklist

| Surface | IW-008 RHI | IW-009 BAY | Evidence |
| --- | --- | --- | --- |
| Registered/reused tag identity | Pass | Pass | Vanilla `00_countries.txt` maps `RHI` to `countries/Rhineland.txt` and `BAY` to `countries/Bavaria.txt`; package effects/triggers use exact tags. |
| Package identity/precondition | Pass | Pass | `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:8-43`; exact origin, region, depth, archetype, anchor, and host checks. |
| Command roster | Pass | Pass | Package effects roster setup and package triggers `:46-55`; both commandants are `is_corps_commander = yes`. |
| Advisor roster | Pass | Pass | Package triggers `:58-67`; three exact advisors per country are created and guarded. |
| Existing vanilla leader reuse | Pass | Pass | Matthes availability `:70-73`; Rupprecht availability `:75-79` additionally requires GER not to retain the character. |
| Politics/government routes | Pass | Pass | Package effects setup block around `:913-1022`; route flags and mutually exclusive route guards match prepared-proof triggers. |
| Starting ideas/lifecycle | Pass | Pass | Twelve package ideas in `common/ideas/006_independence_wave_rhineland_bavaria_ideas.txt`; lifecycle and route ideas are package-allowed and localized. |
| Decisions/missions | Pass | Pass | `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt`; fourteen project decisions plus one hidden mission per country, package/host-war/capital guarded. |
| Focus assignment | Pass | Pass | Shared tree `independence_wave_focus_tree`; assignment effect only loads the full framework for a valid package scope. |
| AI/playability | Pass | Pass | `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt`; survival, restraint, host-threat, route, and high-chaos profiles exist for both tags. |
| Cleanup/rollback | Pass | Pass | Package effects cleanup around `:1064-1211`; package decisions/ideas/flags/variables and protected portrait aliases are restored. |

## File surface checklist

The following runtime surfaces were read and cross-checked. No gameplay source file was changed.

- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt` — guarded character creation, leaders, government installs, starting laws, force application, focus framework, route/founding flags, GER reunification cleanup, and package cleanup.
- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt` — identity, setup anchors, roster proofs, route proofs, formable/ambition proofs, force/lifecycle/AI proofs, and final prepared/complete proofs.
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt` and `common/characters/006_independence_wave_nwe_advisors.txt` — leader/character and advisor tokens.
- `common/national_focus/006_independence_wave_focus.txt` and `common/scripted_effects/006_independence_wave_focus_effects.txt` — shared tree assignment and RHI/BAY Level-2 branches.
- `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt` — package decision categories, hidden missions, project actions, host-war cancellation, and route locks.
- `common/ideas/006_independence_wave_rhineland_bavaria_ideas.txt` — lifecycle and route ideas.
- `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt` — country-specific AI profiles.
- `common/scripted_effects/006_independence_wave_force_effects.txt` and `common/script_constants/006_independence_wave_force_package_constants.txt` — dynamic opening force, inherited technology/slots, supply, stockpiles, templates, and p8/p9 mappings.
- `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt` and `common/scripted_effects/006_independence_wave_package_planner_effects.txt` — package adapter, reservation groups, host-survival ceiling, and optional-state trimming.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, and `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` — registry, automatic-ready/preflight, capacity collision, setup/final/cleanup dispatch, and fail-closed attestation.
- `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt` and `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt` — FORM-04 Rhine Federation eligibility, connected-capital proof, and mutation/readiness contract.
- `interface/006_independence_wave_region_01_portraits.gfx`, `interface/006_independence_wave.gfx`, and `interface/006_independence_wave_rhineland_bavaria_assets.gfx` — stable portrait, focus, idea, and report sprite registrations.
- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml` and related Event 006 localisation files — country/party/leader/advisor/idea/focus/decision/event key coverage.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, `docs/plans/006_independence_wave_plans/map/006_current_map_state_collisions.csv`, and `docs/plans/006_independence_wave_plans/map/006_current_map_reservation_groups.csv` — registry, installed map ownership, and Event 5 collision contracts.
- Vanilla references: `history/countries/RHI - Rhineland.txt`, `history/countries/BAY - Bavaria.txt`, states `42-Rhineland.txt`, `51-Moselland.txt`, `52-Wuttemberg.txt`, `53-Oberbayern.txt`, and `54-Bayreuth.txt`, plus vanilla tag and flag registrations.

## Missing or stale country-package surfaces

- No missing RHI/BAY gameplay surface was found.
- No Event 006 advisor, theorist, high-command, officer-corps, dossier, or `_small` portrait asset is required by the current design. `interface/006_independence_wave_nwe_advisors.gfx` is intentionally absent, and no Event 006 advisor/dossier `_small` consumer remains.
- The four sourced-portrait processor metadata JSON records correctly retain `candidate_requires_visual_approval`. The asset skill requires processor output to keep that status permanently; separate parent approval is recorded in the sourced manifest and `visual_review.md`, which carry the `processed_wired` disposition. No metadata-status rewrite is permitted or required.
- Vanilla country names, adjectives, ideology flags, and histories are intentionally reused; no mod override is required for these two tags.

## Map and state setup

- IW-008 uses anchor state `51` (Moselland) and optional extension `42` (Rhineland/Moselland collision surface); IW-009 uses anchor `52` and optional compact states `53|54`.
- Installed ownership is coherent: states `42|51|52|53|54` are GER-owned/controlled in the binding table and GER retains state `64`; vanilla state histories provide capitals, cores, VPs, factories, resources, infrastructure, and supply-relevant data.
- RHI's installed cores `51|42` and BAY's vanilla cores `52|53|54` match the package/formable contracts. RHI capital is state `51`; BAY capital is state `52`.
- Reservation groups and Event 5 collision helpers are coherent. `RG-RHINE-SAAR` enforces one automatic package and trims the IW-008 extension before collision with IW-010; `RG-52-53-54` is exclusive to IW-009. Host-survival logic rejects a sole-state host loss and trims optional states when needed.
- No map rewrite is proposed. A live map/MCP renderer was not available in this subagent, so this is a source/binding audit rather than a claim of in-game map rendering.

## Politics, leaders, portraits, flags, advisors, and parties

- RHI creates sourced Konrad Adenauer as `RHI_independence_wave_provisional_directorate` and sourced Josef Harpe as `RHI_independence_wave_river_commandant`; both are explicitly `gender = male`. Harpe is both country-leader-capable and a corps commander.
- BAY creates sourced Heinrich Held as `BAY_independence_wave_state_council` and sourced Franz Ritter von Epp as `BAY_independence_wave_mountain_commandant`; both are explicitly `gender = male`. Epp is both country-leader-capable and a corps commander.
- Protected vanilla Matthes and Rupprecht portraits remain wired and are only made available through guarded character/host checks; cleanup restores vanilla aliases.
- Runtime portrait files are `156x210` DDS and hash-verified. New stable sprites are exactly the four in `interface/006_independence_wave_region_01_portraits.gfx`; no small portrait consumers exist. Runtime SHA-256 evidence: RHI Adenauer `06C40E7D557CF7E5BFD719C2A576E15D86A435B8EA9757F1F91620BF0E61AC64`, RHI Harpe `33DCC5595610AC7069E01D6C7C2515657C1FD93D921E55FE8B3707B7914F0D1A`, BAY Held `C371F76669AFBC23E80D862AE8A97F20E6E15B89B4546667ECDB62134CDEE035`, and BAY Epp `E1B37C14E058CCEB7C96280BCE14ACC809C9C6D9F572627171C28F4A48DE7EC6`. Protected hashes remain unchanged: RHI Matthes `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`; BAY Rupprecht `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`.
- All characters are male, with no opposite-gender name-pool or portrait metadata pairing. These are real sourced historical identities; no fictional random-name pool is used.
- RHI route politics cover democratic constitutional, labor/Matthes, emergency/Harpe, and patron/Adenauer outcomes. BAY covers constitutional, labor, traditional/Rupprecht when safe, and emergency/Epp outcomes. Party names and country/leader/advisor localisation are present.
- RHI and BAY reuse vanilla ideology flags; required vanilla variants exist and no custom Event 006 flag is needed.

## Focus, decision, idea, and asset surfaces

- RHI has eight package-specific Level-2 focuses (`establish_corridor_authority`, `unify_rail_dispatch`, `arm_customs_guard`, `secure_industrial_belt`, host/neutral mutual branch, `charter_network_transit_office`, `authorize_form04_delegation`) with prerequisites, route locks, AI weights, icons, effects, and localisation.
- BAY has eight package-specific Level-2 focuses (`broker_civic_settlement`, `reconcile_landesbank_accounts`, `bind_rail_and_pass_authorities`, court/guardians mutual branch, `open_alpine_network_office`, South German/host mutual branch) with the same coverage.
- All sixteen focus IDs have title/description/tooltip localisation and matching icon sprites. No meaningful existing focus tree is overwritten: full-tree loading is guarded by the full-framework assignment scope; additive/post-formation modes do not reload the tree.
- Thirty Event 006 RHI/BAY decision/category/mission IDs have title/description localisation. Twelve ideas have icons, allowed/visible/available scopes, lifecycle/route modifiers, and localisation. Six asset-neutral institutional office advisors have traits, costs, AI, lifecycle hooks, and localisation; they are offices rather than named fictional people, and no custom advisor art is specified.
- Event report picture references for RHI/BAY resolve to the two registered report sprites.

## Starting military, technology, industry, supply, and production

- The package deliberately has no bespoke country-history unit or production override. The dynamic force layer (`006_independence_wave_force_effects.txt`) calculates opening strength from population, factories, infrastructure, rail, ports, supply, host divisions, and host-war state; it applies p8 (RHI) or p9 (BAY) `regular_defectors` mappings only after roster/prepared proof.
- Opening templates, inherited host technology/research slots, infantry/artillery/support/truck/train/convoy/fuel stockpiles, and state refresh are all wired through the dynamic effects and constants. Vanilla histories supply the expected factories/resources/VPs/infra.
- This is an intentional dynamic-start design, not a missing setup. No hardcoded major army, production line, or research shortcut was introduced by the portrait replacement.

## AI, diplomacy, formables, host survival, Event 5, and SCN-008

- RHI/BAY each have six AI profiles covering survival, founding restraint, former-host threat, route policy, emergency/guardians, and high-chaos behavior. Profiles are package- and setup-flag-gated and abort when disabled.
- Host-war and capital-loss cancellation, former-host reunification decision closure, subject release handling, and cleanup are present in package effects/decisions.
- FORM-04 is correctly linked only to the RHI carrier path: anchor `51`, connected corridor state `42`, delegated readiness, and strict mutation proof. No BAY formable family is claimed.
- Event 5 exclusion helpers correctly clear IW-008/IW-009 country/anchor/host collisions; capacity bands are p8 and p9 respectively. The installed map binding preserves the stated host-survival margin.
- SCN-008 automatic-ready and scenario preflight branches recognize IW-008/IW-009 exact IDs/tags, but both fail before execution because the content attestation is `always = no`. Therefore re-admission is not safe or authorized yet.

## Meaningful validation evidence

- Mechanical source inspection found four and only four new Event 006 portrait sprite consumers, no Event 006 `_small` portrait consumers, all sixteen focus icon references, all eight idea icon references, all report picture references, and complete title/description localisation sets for package focuses/decisions/ideas/advisors.
- DDS header/hash inspection confirmed all six RHI/BAY full portraits are `156x210`; the two protected DDS hashes above are unchanged. Focus/idea/report DDS dimensions and referenced texture paths also resolve.
- Character/effect/trigger cross-check confirmed exact token, sprite, gender, leader/commander role, availability, cleanup, route, and prepared-proof contracts.
- State-history and installed-binding inspection confirmed anchor/extension ownership, capitals, cores, VPs, factories/resources/infrastructure, and reservation-group collision contracts.
- Offline Paradox wiki core pages and related country/focus/decision/idea/AI pages were consulted, together with relevant vanilla HOI4 documentation and vanilla RHI/BAY precedents.
- No HOI4 runtime load, live save, or installed Technology Tree Viewer validation was available in this subagent; do not present this handoff as a live-game admission proof.

## Changed files and identifiers

Changed files: **none** in gameplay, localisation, interface, GFX, manifests, specs, resume packets, or tag-audit reports. This handoff is the only file added.

Identifiers checked: tags `RHI`, `BAY`; package IDs `IW-008`, `IW-009`; anchors `51`, `52`; optional states `42`, `53`, `54`; groups `RG-RHINE-SAAR`, `RG-52-53-54`; force profiles p8/p9 `regular_defectors`; leaders `RHI_independence_wave_provisional_directorate`, `RHI_independence_wave_river_commandant`, `BAY_independence_wave_state_council`, `BAY_independence_wave_mountain_commandant`; protected characters `RHI_josef_friedrich_matthes`, `BAY_rupprecht_of_bavaria`; FORM-04 Rhine Federation carrier path.

## Blockers, uncertainty, and follow-up

1. **Admission blocker:** the authoritative runtime content attestation is intentionally fail-closed (`always = no`), and both runtime and SCN-008 preflight require it. The parent must update that source-of-truth attestation only after the independent package and visual-review gates are satisfied, then rerun this admission audit.
2. **Provenance contract:** the four processor metadata JSON files must remain `candidate_requires_visual_approval`; the separate sourced manifest and `visual_review.md` are the approval authority. This is the required two-record workflow, not an unresolved metadata issue.
3. **Validation boundary:** no live HOI4/MCP renderer or Technology Tree Viewer was available here. Source-level proof is strong, but runtime admission should still be followed by the parent’s normal live-load/SCN-008 checks after attestation changes.

Simplifications/omissions: none found in the country package. The absence of custom advisor/dossier art, bespoke country-history units, custom flags, and BAY formable content is intentional and documented by the current design. No fallback asset or gameplay substitute was used. No package was re-admitted.
