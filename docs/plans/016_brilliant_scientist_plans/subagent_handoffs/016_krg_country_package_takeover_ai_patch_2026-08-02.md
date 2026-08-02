# Event 016 KRG country-package takeover AI patch

Date: 2026-08-02

Status: bounded patch complete; parent review and live formation/takeover validation remain outstanding.

## Scope

This pass audits the Kruger State country package without creating or wiring 3D models.

The one gameplay patch removes the static country gate from the two takeover AI plans whose `enable` blocks already carry the full dynamic takeover conditions.

No country tag, state, focus, decision, event, character, portrait, flag, technology, equipment, or model was created.

## Changed file and identifiers

- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`
  - `KRG_takeover_consolidation_plan` no longer has `allowed = { original_tag = KRG }`.
  - `KRG_takeover_post_audit_plan` no longer has `allowed = { original_tag = KRG }`.
  - Their existing `enable` and `abort` conditions are unchanged.
  - The same file contains an unrelated parent edit that reorders two entries in `KRG_project_synthesis_plan`; that line is not part of this patch.

## Before and after behavior

Before this patch, both takeover plans required `original_tag = KRG` in `allowed`.

The offline AI modding reference states that `allowed` is checked only at game start, while `enable` is checked daily.

`brilliant_scientist_transform_host_into_kruger_state` in `common/scripted_effects/016_brilliant_scientist_country_effects.txt` intentionally retains the host's original tag, sets `brilliant_scientist_host_transformed_into_kruger_state`, and sets `brilliant_scientist_formation_takeover`.

Therefore a host such as GER could satisfy the takeover conditions after the game started but could never satisfy the old `allowed` gate.

After this patch, the two plan definitions are parsed for every country, but their daily `enable` blocks still require `brilliant_scientist_is_kruger_sovereign_country = yes` and `brilliant_scientist_formed_by_takeover = yes`, with the consolidation plan additionally requiring an incomplete founding audit and the post-audit plan requiring a completed audit and open identity.

The scripted trigger recognizes either `original_tag = KRG` or `has_country_flag = brilliant_scientist_host_transformed_into_kruger_state`, so the dynamic gate is bounded to an active KRG or transformed host.

The other seventeen plans retain their original-tag `allowed` gate and therefore remain KRG-origin-only until a broader takeover AI decision is approved.

## Country-package coverage checklist

| Surface | Status | Evidence |
| --- | --- | --- |
| Tag registration and country definition | Covered | `common/country_tags/016_brilliant_scientist_country.txt:8` registers `KRG`; `common/countries/Kruger State KRG.txt` supplies graphics and color. |
| Dormant history and OOB | Intentional dormant setup | `history/countries/KRG - Kruger State.txt:9-15` uses bootstrap capital 1, empty OOB `016_brilliant_scientist_dormant`, zero research slots, and neutral politics until runtime formation. |
| Map, state ownership, capital, cores, and claims | Static contract present; live proof pending | `common/scripted_effects/016_brilliant_scientist_territory_effects.txt` and `common/scripted_effects/016_brilliant_scientist_country_effects.txt` validate facilities, capital, supply, ports, ownership, cores, and claims before transfer. The parent owns live map/formation validation. |
| Politics and country identity | Covered for released KRG; takeover identity warning remains | `brilliant_scientist_initialize_current_kruger_state` and `brilliant_scientist_transform_host_into_kruger_state` apply government, ideas, diplomacy, focus tree, and Kruger roles. The takeover path currently drops the host cosmetic tag without assigning a base KRG cosmetic identity; see the remaining-risk section. |
| Leaders, advisors, commanders, and portraits | Covered statically | `common/characters/016_brilliant_scientist_characters.txt` contains `KRG_warren_kruger`, `KRG_continuity_network`, and the four fixed institutional offices `KRG_general_staff_office`, `KRG_machine_command_node`, `KRG_clone_officer_corps`, and `KRG_project_command_council`. Their route activation is documented in the existing route-command handoff. |
| Parties, names, and localisation | Covered statically | `localisation/english/016_brilliant_scientist_country_l_english.yml` contains base KRG, party, leader, advisor, trait, and six route-cosmetic keys. The file retains a UTF-8 BOM. |
| Focus tree | Covered statically | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` contains 100 KRG focuses and loads through `brilliant_scientist_is_active_kruger_state`. Read-only focus inspection reported zero diagnostics for the KRG tree. |
| Decisions and missions | Present | Foundation, staff, project, safeguard, foreign-integration, evolution, and terminal decision files are present under `common/decisions/`; the parent owns live route availability checks. |
| Ideas and lifecycle | Logic covered; icon surface incomplete | `common/ideas/016_brilliant_scientist_country_ideas.txt` contains the KRG lifecycle ideas and `brilliant_scientist_apply_starting_country_ideas` applies them. Twenty-one visible ideas have no `picture` assignment and no matching bespoke DDS in `gfx/interface/ideas/016_brilliant_scientist`; this is an asset handoff, not a fallback patch. |
| Starting military, technology, industry, supply, and production | Dynamic package present; live balance pending | Country effects derive the conventional guard from host/formation history and materialise project forces only from matching project receipts and facilities. Limited former-host technology inheritance is in `common/scripted_effects/016_brilliant_scientist_technology_effects.txt`. |
| AI | Patched for takeover entry and post-audit handoff | `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` contains 19 plans; the two takeover plans now use daily dynamic eligibility, while 17 other plans remain original-tag gated. |
| Cleanup and formation lifecycle | Static helpers present; live proof pending | Formation transaction and takeover cleanup are in `common/scripted_effects/016_brilliant_scientist_country_effects.txt`; route staff reset and takeover flags are present. Live state transfer, host residual flags, and succession remain parent-owned checks. |

## File-surface checklist

The audited KRG surface is present in `common/country_tags/016_brilliant_scientist_country.txt`, `common/countries/Kruger State KRG.txt`, `common/countries/016_brilliant_scientist_cosmetics.txt`, `history/countries/KRG - Kruger State.txt`, `history/units/016_brilliant_scientist_dormant.txt`, `common/characters/016_brilliant_scientist_characters.txt`, `common/country_leader/016_brilliant_scientist_traits.txt`, `common/scripted_effects/016_brilliant_scientist_country_effects.txt`, `common/scripted_effects/016_brilliant_scientist_territory_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt`, `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`, `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`, KRG decision files under `common/decisions/`, project-force files under `common/units/`, `common/units/equipment/`, and `common/technologies/`, and localisation/flag/interface assets under `localisation/english/`, `gfx/flags/`, and `interface/`.

No new file surface was needed for this bounded AI fix.

## Missing or stale country-package surfaces

1. The takeover path retains the host tag and calls `drop_cosmetic_tag = yes` at `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1040`, but it does not call `set_cosmetic_tag = KRG` or define a base `KRG` cosmetic block in `common/countries/016_brilliant_scientist_cosmetics.txt`. This creates a design/engine risk that a transformed host continues to display the former host's map name, adjective, or flag until a route cosmetic tag is selected. I did not patch this because the source comment explicitly says the takeover retains the host tag and map, and changing that contract requires a parent decision about host identity, flags, localisation, and original-tag behavior.
2. The seventeen route/project/terminal plans other than the two takeover plans still use `allowed = { original_tag = KRG }`. A transformed host can therefore use the patched takeover consolidation and post-audit plans but may fall back to focus-level `ai_will_do` after identity lock rather than receiving the route-specific project and terminal queues. Broadening all plan gates is a separate AI design decision.
3. Twenty-one visible KRG ideas in `common/ideas/016_brilliant_scientist_country_ideas.txt` have no `picture` assignment. The current bespoke icon folder contains 28 DDS files, but not one for each visible lifecycle idea. Adding an unrelated icon would be a prohibited fallback; route this to the Event 016 idea-icon asset handoff.
4. The installed package exposes no Technology Tree Viewer. Technology-tree validation therefore remains unresolved beyond source-level ID checks and the parent-owned partial technology inspection.
5. Event 016 has no approved 3D `.mesh`, `.anim`, entity `.asset`, or entity `.gfx` package. No 3D work was attempted in this country pass.

## Politics, leader, portrait, flag, advisor, and party findings

The fixed Kruger and institutional office characters use fixed institutional names where the portrait is an office or network, and the existing route-command patch keeps male metadata aligned with the reused male-presenting scientist portraits.

Base KRG and six route cosmetic flags exist in normal, medium, and small sizes, and their route-localisation keys are present.

The only unresolved identity finding is the takeover cosmetic-tag tension recorded above.

## Focus, decision, idea, and asset findings

The KRG focus tree has 100 authored focus blocks, all focus icons are registered in `interface/016_brilliant_scientist_kruger_state_focus.gfx`, and the read-only focus inspector returned `status = ok` with zero KRG diagnostics.

The foundation decision layer includes `brilliant_scientist_krg_count_and_recruit_surviving_staff` and `brilliant_scientist_krg_coordinate_project_commanders`; route lifecycle decisions and focus consumers are present.

The idea logic is present, but the 21 no-picture visible ideas need a dedicated icon production and wiring pass.

## Starting military, technology, industry, supply, and production findings

The dormant history intentionally grants no army, equipment, production, or research slots.

Runtime helpers derive a capped conventional guard from actual host/formation values and only instantiate project-derived forces after matching project history, facilities, and receipt guards.

Takeover retains the host army and receives no free conventional grant; this remains a live scenario check.

## AI and playability findings

The dynamic takeover patch is safe at the source-contract level because the two ungated plans have no effects in `allowed`, and their daily `enable` and `abort` blocks remain fully guarded by KRG sovereign, takeover-origin, audit, identity, and focus-tree conditions.

No non-KRG country receives a KRG AI strategy plan solely from this patch because `enable` remains false unless the Event 016 sovereign trigger or transformed-host flag is true.

After the identity lock, transformed hosts still do not satisfy the seventeen original-tag gates for route/project/terminal plans. This is a documented residual AI coverage risk, not an unreported fallback.

## Validation performed

- Read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`, and `hoi4-decisions-missions` skills before editing.
- Read the required offline Paradox wiki pages, including `AI modding - Hearts of Iron 4 Wiki.md`, where `allowed` is documented as game-start-only and `enable` as daily.
- Read the relevant vanilla effects and AI documentation, including `effects_documentation.md` and the vanilla country/cosmetic examples for `set_cosmetic_tag`.
- Confirmed with repository scans that the source contains 19 KRG AI plan blocks, 17 remaining `allowed` blocks, and exactly two takeover plans without an `allowed` block.
- Confirmed `brilliant_scientist_is_kruger_sovereign_country` accepts either `original_tag = KRG` or `brilliant_scientist_host_transformed_into_kruger_state`, and `brilliant_scientist_formed_by_takeover` checks `brilliant_scientist_formation_takeover`.
- `git diff --check -- common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` returned no whitespace errors.
- Read-only `hoi4_focus_inspect` for `brilliant_scientist_kruger_state_focus_tree` returned `status = ok`, 100 focuses, and zero diagnostics for the KRG tree. The artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ba30159db7ddc31b1430b61dcf28e3ecb17ea749e124da8f83d5d94a5a7723e/8287d2c89c2e5ccff8fdaa8697eab03e52e70b3b8999283460cbd56ad6606645/focus-inspect.cc58941aa91bd941.json`.
- No Hearts of Iron IV process was launched, and no live formation, takeover, AI activation, map transfer, technology-tree, advisor, or balance claim is made here.

## Skipped meaningful validation and why

- Live takeover and route-AI activation were skipped because agents must not launch Hearts of Iron IV; the parent/user owns live scenario validation.
- Map write or map apply was skipped because this patch changes no state or province data.
- Technology-tree viewer validation was skipped because no Technology Tree Viewer is installed in the current package.
- Weighted AI simulation was not run because the bounded change affects plan eligibility rather than a numeric weight, and the read-only probability adapters do not expose a direct AI-strategy-plan lifecycle adapter.

## Remaining risks and parent checks

1. Exercise one transformed-host takeover and one KRG-tag formation in a user-owned live session. Confirm that the takeover plan appears after the transformation, the consolidation plan aborts after the audit, and the post-audit plan aborts after identity lock.
2. Decide whether takeover should receive a base `KRG` cosmetic identity or intentionally retain the host's map identity, then align `set_cosmetic_tag`, `common/countries/016_brilliant_scientist_cosmetics.txt`, flags, and localisation accordingly.
3. Decide whether all 17 remaining route/project/terminal plans should be made dynamic for transformed hosts or whether focus-level AI fallback is the accepted takeover behavior.
4. Route the 21 no-picture idea IDs to dedicated asset production and GFX registration; do not reuse an unrelated icon as a fallback.

No commit was created.
