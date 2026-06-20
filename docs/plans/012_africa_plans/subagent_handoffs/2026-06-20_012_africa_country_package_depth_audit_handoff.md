# Event 012 Africa Country Package Depth Audit Handoff

Date: 2026-06-20
Role: Chaos Redux country-package subagent
Scope: bounded audit after the targeted scenario-validation tranche, focused on Event 012 created, transformed, sponsored, and restored actors.

## Instructions Applied

- Read `AGENTS.md`.
- Read and applied `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-event-assets`.
- Consulted the required offline wiki surfaces for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, focus trees, and country creation.
- Consulted vanilla documentation under `/home/klim/projects/Hearts of Iron IV/documentation/` for effects, triggers, script concepts, and modifiers.
- Read the requested Event 012 source-of-truth, foundation disposition ledger, targeted scenario validation matrix, completion gap audit, country-package spec, niche country matrix, and Event 012 foundation doc.

## Changed Files

- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_country_package_depth_audit_handoff.md`

No gameplay, localisation, asset, GFX, GUI, history, country, focus, decision, idea, AI, Event 010, or Event 070 files were edited. No commit was made.

## Changed Identifiers And Surfaces

- Tags documented: `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`, `BON`, `HYR`, `BIR`, `SAO`.
- Focus ids documented as current capstone parity examples: `AFR_BEST_bon_gentle_veto_court`, `AFR_BEST_hyr_night_broadcasts`, `AFR_BEST_bir_verified_wall_warnings`, `AFR_BEST_sao_terracotta_line`.
- Helper names documented as current staff coverage: `africa_generate_created_country_role_staff`, `africa_generate_created_country_command_staff`.
- Country-package documentation wording now distinguishes direct country localisation from institutional leader, party, focus, and staff labels.

## Before And After Behavior

Before:

- The country-package source spec still said Event 012 registered 11 explicit Bestiary actor tags and described `BON`, `HYR`, `BIR`, and `SAO` as outside that implemented actor note.
- The same spec said the generated staff layer gave every created actor one role advisor, which understated the current role-advisor plus command-staff implementation.
- The event foundation doc blurred country public display identities with institutional labels such as Congress, Charter, League, and Council, despite the current country-name rule preferring direct public country names.

After:

- The country-package source spec records the current 15 Bestiary actor package and explicitly lists `BON`, `HYR`, `BIR`, and `SAO`.
- The source spec records that all 15 Bestiary actors now have tag-specific post-World-Witness capstone parity.
- The staff note records two generated role advisors, one generated corps commander, and naval commanders for the nine naval-OOB actors.
- The event doc now states that direct country localisation is used where the region or polity name is the public state identity, while institutional names remain appropriate for leaders, parties, staff, focuses, and mechanics.

## Country Package Coverage Checklist

- Tag registration: static check found all 25 Event 012 created tags in `common/country_tags/chaosx_countries.txt`.
- Country files: all 25 tags have matching `history/countries/TAG - *.txt` files and country-tag paths.
- History and leaders: all 25 histories define institutional or nonhuman/supernatural country leaders through `create_country_leader`; no personal generated opposite-gender name-pool issue was found in the inspected histories.
- OOBs: all 25 tags have `history/units/TAG_1936.txt`.
- Localisation: all 25 tags appear in `localisation/english/chaosx_countries_l_english.yml`; direct country-name documentation now matches the naming policy more closely.
- Focus loading: regional authorities load `africa_regional_authority_focus_tree`; high-chaos actors load `africa_high_chaos_actor_focus_tree`.
- AI: all 25 tags appear in `common/ai_strategy/012_africa.txt`; `BON`, `HYR`, `BIR`, and `SAO` have tag-specific AI strategies.

## File Surface Checklist

Inspected or spot-checked:

- `common/country_tags/chaosx_countries.txt`
- `history/countries/WAC*` through `history/countries/SAO*`
- `history/units/WAC_1936.txt` through `history/units/SAO_1936.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.md`
- `common/national_focus/012_africa_authority_focus.txt`
- `common/national_focus/012_africa_focus.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/ai_strategy/012_africa.txt`
- `localisation/english/012_african_union_l_english.yml`
- `localisation/english/chaosx_countries_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `docs/specs/012_africa_specs/matrices/012_africa_niche_country_matrix.md`

The prompt-mentioned `common/characters/012_africa_characters.txt` does not exist; Event 012 country leaders and staff are currently handled through history `create_country_leader` entries and scripted `generate_character` helpers.

## Missing Or Stale Country Package Surfaces

1. Medium severity: created packages still rely on shared regional-authority and high-chaos companion trees, even with tag-gated branches and capstones. This is a deliberate bounded implementation, not full bespoke country-package depth.
2. Medium severity: the selected-host origin layer is meaningful but still not a long-form bespoke route family. The spec continues to mark deeper route-specific events and host branches as future country-package depth.
3. Low severity, patched: the source country-package spec was stale about 11 Bestiary actors and one role advisor. It now matches the current 15-actor and staff/command implementation.
4. Low severity: the older `2026-06-19_012_africa_country_package_depth_sidecar_handoff.md` still contains historical stale notes saying `BON`, `HYR`, `BIR`, and `SAO` lack capstones. I did not rewrite that older handoff; the current source-of-truth and this handoff supersede that claim.

## Map And State Setup Issues

- No new map/state defect was found in this pass.
- Current documentation and setup list distinct one-state seats for all 25 created tags.
- Static checks confirmed the current surfaces still include all 25 target tags; I did not run a full supply, railway, port, airbase, victory-point, or resource balance pass.

## Politics, Leaders, Portraits, Flags, Advisors, And Parties

- Created countries use institutional or nonhuman/supernatural leader names, not random personal name pools.
- High-chaos actors are present in shared `is_special_chaos_country` and `is_actual_nonhuman_country` coverage.
- Regional authorities are special chaos/event-managed countries but not actual nonhuman countries.
- The docs now clarify that public country names and institutional labels are separate surfaces.
- Asset files and portrait sources were not visually revalidated in this pass.

## Focus, Decision, Idea, And Asset Issues

- `BON`, `HYR`, `BIR`, and `SAO` have high-chaos focus branches and tag-specific post-World-Witness capstones in `common/national_focus/012_africa_authority_focus.txt`.
- Regional authority mandate completion correctly checks the ten regional authority capstone flags, not high-chaos actors.
- Existing decision and mission surfaces for regional authority mandates are present and localised.
- No missing Event 012 country-package localisation key was patched in this pass.

## Starting Military, Technology, Industry, Supply, And Production

- Static tag audit confirmed all 25 created tags have static land OOB files.
- The setup helper applies one-time created-country logistics, production setup, generated staff, generated command staff, and dynamic guard/reinforcement routes.
- This pass did not rebalance static OOB size, production lines, naval starts, air starts, supply hubs, or state buildings.

## AI And Playability Issues

- All 25 created tags have AI surface references in `common/ai_strategy/012_africa.txt`.
- AI depth is still role/tag posture and focus/decision weighting, not a live scenario proof.
- Highest-value remaining bounded parent tranche: pick 3-4 selected-host archetypes and 3-5 created actors, then add route-specific events, decision consequences, advisor unlocks, reinforcement hooks, and failure/abuse responses that are not just shared-tree value movement. The best candidates are `WAC`/`SAH`/`IOC` for regional authorities, `BON`/`HYR`/`BIR`/`SAO` for recent high-chaos parity, and one selected-host origin such as `LIB`, `ETH`, or a fragile `WAC` fallback.

## Meaningful Validation Run

- Verified the stale "11 explicit Bestiary" and "one generated role advisor" wording no longer appears in the current source spec or event doc.
- Verified all 25 created tags appear across tag/history/OOB/focus/AI/localisation surfaces using a static `rg` loop.
- Verified `BON`, `HYR`, `BIR`, and `SAO` have current focus and AI references.
- Reviewed the diff for the two documentation edits.

## Skipped Meaningful Validation

- Live in-game validation remains unrun.
- No HOI4 launch, scenario launch, screenshot pass, or GUI interaction pass was run.
- No full localisation parser, asset visual QA, balance pass, or exploit-loop validation was run.

## Remaining Setup Or Identity Risks

- Event 012 is still not complete-ready; the targeted scenario matrix remains static/script coverage only.
- Shared companion trees and shared setup packages still carry most created actors, even though tag-specific capstones and AI reduce the generic feel.
- Historical dossier packages remain primarily dossier/office records rather than full country tags unless map state justifies them.
- Country-package depth should not be closed until live scenario proof confirms fragile unifier, ally-under-attack, high-chaos covenant, full unification, cross-continent union, and World Is One gate behavior.
