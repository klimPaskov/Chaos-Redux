# Event 014 Cannibalism country package audit handoff

Audit date: 2026-08-24.

Exact stage: source audit of the CBA-CBH reusable warlord slots, CBL unified host, existing ZZZ Wendigo discovery and preservation path, and their country, history, state, leader, portrait, flag, party, idea, advisor, unit, technology, AI, territory, claims, cores, recruitment, and player-control surfaces.

Disposition: one P1 country-package defect is proven, two P2 design risks remain, and several required HOI4 MCP evidence routes are blocked or unavailable. No gameplay or asset file was changed because concurrent work is present. This handoff is the only file changed by this audit tranche.

## Executive findings

- CBA-CBH are the only reusable warlord slots in the Event 014 tag file, and CBL is the only ordinary unified host tag.
- The active origin set is exactly Island Host, Siege Commune, and March Host. No live Event 014 `Prison Host` trigger, tag, effect, or localisation identifier remains.
- Eight-slot allocation and cleanup are explicitly implemented for CBA-CBH, including reusable release helpers.
- The source package wires nine custom irregular subunits and the existing vanilla `elephantry` unit through setup, templates, activation technology, inherited recruitment, unified recruitment, Wendigo inheritance, localisation, icons, and CXT registration.
- Unified host and Wendigo source logic preserves donor identity and player control through human-first host selection and guarded transfer paths, but required map and runtime evidence could not be completed.
- Hannibal secrecy is not satisfied in the current source. Both CBL and Wendigo histories use `recruit_character` before their public reveal role is created. This is an engine-semantic P1 blocker, not only a comment or naming concern.
- No Event 014 advisor, high-command, theorist, or political-advisor character surface was found. The package currently uses country-leader roles and command ideas, which is a P2 design warning unless that substitution is explicit in the specification.
- The regional name mapping covers seven supported identities with four names each. The Oceania pool is internally consistent but entirely Anglo-settler in presentation, so its regional identity needs design confirmation.

## Required references consulted

The repository `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-comfyui`, and `chaos-redux-improvement-loop` skills were read before this audit.

The offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, country creation, national focuses, divisions, equipment, technology, and map modding were consulted.

The vanilla documentation files `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`, `script_concept_documentation.md`, and `dynamic_variables_documentation.md` were consulted where the relevant syntax and engine semantics were needed.

The country-creation wiki page defines `recruit_character = TAG_character_name` as recruiting the specified character and states that recruiting attaches the character to a country. Vanilla `effects_documentation.md:5696-5705` independently defines `recruit_character` in country scope as attaching a character to a country.

## Country package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Tag registration | Pass | `common/country_tags/014_cannibalism_countries.txt:8-16` registers exactly CBA, CBB, CBC, CBD, CBE, CBF, CBG, CBH, and CBL. |
| Country definitions | Source pass | `common/countries/Cannibal Warlord Slot CBA.txt` through `CBH.txt` and `common/countries/Cannibal Unified Host CBL.txt` provide the matching definitions and colours. |
| Country histories | P1 defect | Dormant CBA-CBH histories are coherent, but `history/countries/CBL - Cannibal Unified Host.txt:15` and `history/countries/ZZZ - Zombie Outbreak.txt:18` attach Hannibal before reveal. |
| Origins | Pass | `common/scripted_triggers/014_cannibalism_triggers.txt:3050-3107` contains only Island Host, Siege Commune, and March Host formation triggers. |
| Prison Host exclusion | Source pass | No live `prison_host`, `Prison Host`, or equivalent Event 014 identifier was found under `common`, `history`, `events`, `interface`, or `localisation`; old references are documentation history only. |
| Reusable slots | Pass | `common/scripted_triggers/014_cannibalism_triggers.txt:3599-3609` checks all eight availability flags, and `common/scripted_effects/014_cannibalism_effects.txt:5396-5479` defines all eight allocation helpers. |
| Regional identity | Pass with P2 warning | `common/scripted_localisation/014_cannibalism_scripted_localisation.txt:313-372` and `:4645-4706` map seven regions and three origins to names and parties. The Oceania names at `localisation/english/014_cannibalism_l_english.yml:477-504` are all Anglo-settler names. |
| States, capitals, cores, and claims | Source pass; MCP unresolved | Dynamic creation transfers the origin plus up to two valid neighbours, cores transferred states, and sets the origin capital in `common/scripted_effects/014_cannibalism_effects.txt:5334-5375`. Rollback removes cores and clears references around `:5280-5300`. |
| Unified host | Source pass with P1 Hannibal defect | CBL setup and role creation are in `common/scripted_effects/014_cannibalism_effects.txt:12400-12458`; the public event is `events/014_cannibalism.txt:436-452` with ID `chaosx.nr14.70`. |
| Wendigo discovery, preservation, and unification | Source pass with P1 Hannibal defect | `common/scripted_effects/014_cannibalism_effects.txt:18659-18705` preserves the ZZZ host and creates the Wendigo role, while the merge path begins around `:18800`. The public event is `events/014_cannibalism.txt:555-574` with ID `chaosx.nr14.72`. |
| Player control safety | Source pass; MCP unresolved | Human-first host selection and no-human-displacement guards are in `common/scripted_effects/014_cannibalism_effects.txt:11993-12034` and `:12409-12470`; Wendigo donor and host guards are around `:18800-18870`. |
| Politics and parties | Source pass | Dormant histories use neutrality with elections disabled. Runtime setup creates the ritual-predation identity and origin party names through `common/scripted_effects/014_cannibalism_effects.txt` and `common/scripted_localisation/014_cannibalism_scripted_localisation.txt:346-372`. |
| Leaders and portraits | P1 secrecy defect | Dynamic warlord leaders have male-presenting regional names and no female metadata. CBL and Wendigo static character records exist in `common/characters/014_cannibalism_characters.txt`, but their histories recruit them before reveal. |
| Advisors and high command | P2 design warning | No Event 014 advisor, high-command, theorist, or political-advisor character definitions were found in `common/characters/014_cannibalism_characters.txt` or the Event 014 leader surface. Current command ideas and leader traits are not equivalent advisor slots unless the specification says so. |
| Flags | Source pass | CBA-CBH each have base and four ideology variants in all three sizes. CBL has base and four ideology variants plus the CBL_CENTRAL_COMMAND, CBL_HOST_CONFEDERATION, and CBL_RITUAL_STATE cosmetic families in all three sizes. |
| Focus trees | Source pass; MCP unresolved | `common/national_focus/014_cannibalism_focus.txt` contains 108 unified, 68 warlord, and 28 Wendigo focus blocks. Runtime loading occurs around `common/scripted_effects/014_cannibalism_effects.txt:5229`, `:12442`, and `:19164`. |
| Decisions, missions, and ideas | Source/localisation pass | `common/decisions/014_cannibalism_decisions.txt`, `common/decisions/categories/014_cannibalism_categories.txt`, and `common/ideas/014_cannibalism_ideas.txt` are wired to the Event 014 route and localisation. |
| Units and equipment | Source pass; technology viewer unavailable | Nine custom subunits are defined, activated by matching hidden bridge technologies, and granted by package, origin, inherited, unified, and Wendigo effects. Vanilla `elephantry` is included in templates and setup. |
| AI | Source pass; probability evidence blocked | `common/ai_strategy/014_cannibalism_warlords.txt` contains common and Island, Siege, and March profiles with self-removing guards. Required probability-auditor evidence was unavailable. |
| Recruitment and cleanup | Source pass except Hannibal secrecy | Warlord allocation, release, state transfer, actor generation, and template cleanup are explicit in `common/scripted_effects/014_cannibalism_effects.txt:5687-5724` and related helpers. |

## Critical findings and proposed fixes

### P1 CR-014-HANNIBAL-PRE-REVEAL-ATTACHMENT

`history/countries/CBL - Cannibal Unified Host.txt:15` contains `recruit_character = CBL_hannibal` in the country history. `history/countries/ZZZ - Zombie Outbreak.txt:18` contains `recruit_character = ZZZ_hannibal_wendigo` in the starting history.

The corresponding characters have portraits in `common/characters/014_cannibalism_characters.txt`, so this is a real country-character attachment rather than an inert localisation token. The comments in both histories call the characters roleless and invisible, but the required wiki and vanilla documentation define `recruit_character` as attaching the character to the country and do not establish a hidden internal-only exception.

CBL public role creation occurs later at `common/scripted_effects/014_cannibalism_effects.txt:12451-12458` for `CBL_hannibal`. Wendigo role creation occurs at `:18697-18705` for `ZZZ_hannibal_wendigo`. The reveal events require `has_character` at `events/014_cannibalism.txt:443` and `:562`, so simply deleting the history recruitment without changing reveal ordering would create a second failure.

Proposed fix: remove both static history recruitments and add a guarded `recruit_character` in the same reveal transaction immediately before the corresponding `add_country_leader_role`, or replace the event trigger with a reveal-state guard that does not require a pre-reveal character attachment. The fix must prove that the character is absent from the country before reveal and present only in the reveal transaction. Do not rely on the current roleless comment as secrecy proof.

### P2 CR-014-ADVISOR-SURFACE

No Event 014 advisor, high-command, theorist, or political-advisor character definitions were found in `common/characters/014_cannibalism_characters.txt` or `common/country_leader/014_cannibalism_traits.txt`. The current package provides country leaders, leader traits, institutional command ideas, and unit commanders, but no advisor-slot consumer.

Proposed fix: either add a bounded, identity-specific institutional advisor/high-command package with its own localisation and portrait wiring, or update the Event 014 specification to state that command-body ideas and country-leader roles intentionally replace advisor slots. The latter is a design decision for the parent and should not be inferred from the current source.

### P2 CR-014-OCEANIA-NAMING

The region resolver maps Australia to `cannibalism_region.oceania`, and the four Oceania names are Colin Mercer, Edwin Rourke, Thomas Keane, and Walter Haines in `localisation/english/014_cannibalism_l_english.yml:477-504`. This is internally deterministic and passes syntax, but it does not communicate a Pacific or Indigenous regional identity if that identity is intended by the feature.

Proposed fix: confirm the intended Oceania scope with the design owner. If Pacific regional identity is required, replace the four-name pool through approved research and portrait sourcing, then update the matching leader metadata and assets together. No asset or identity change was made in this audit.

## Unit and technology integration audit

The nine required custom unit IDs are all present in `common/units/014_cannibalism_irregular_infantry.txt`, each has a matching activation technology in `common/technologies/014_cannibalism_irregular_activation_technologies.txt`, and each is wired to localisation and icons.

| Custom unit ID | Definition | Activation technology and integration |
| --- | --- | --- |
| `cannibal_scavenger_warband` | `common/units/014_cannibalism_irregular_infantry.txt:309` | Activation tech `:16`, templates around `common/scripted_effects/014_cannibalism_effects.txt:4765`, CXT token `common/scripted_effects/014_cannibalism_cxt_test_effects.txt:23`. |
| `cannibal_feast_guard` | `common/units/014_cannibalism_irregular_infantry.txt:359` | Activation tech `:24`, templates around `:4777`, CXT token `:25`. |
| `cannibal_feast_cohort` | `common/units/014_cannibalism_irregular_infantry.txt:408` | Activation tech `:32`, templates around `:4792`, CXT token `:27`. |
| `cannibal_bone_guard` | `common/units/014_cannibalism_irregular_infantry.txt:458` | Activation tech `:40`, templates around `:4813`, CXT token `:29`. |
| `cannibal_bone_riders` | `common/units/014_cannibalism_irregular_infantry.txt:507` | Activation tech `:48`, templates around `:4833`, CXT token `:31`. |
| `cannibal_island_reavers` | `common/units/014_cannibalism_irregular_infantry.txt:562` | Activation tech `:56`, templates around `:4858`, CXT token `:33`. |
| `cannibal_siege_eaters` | `common/units/014_cannibalism_irregular_infantry.txt:618` | Activation tech `:64`, templates around `:4873`, CXT token `:35`. |
| `cannibal_march_predation_column` | `common/units/014_cannibalism_irregular_infantry.txt:668` | Activation tech `:72`, templates around `:4890`, CXT token `:37`. |
| `cannibal_network_cadre` | `common/units/014_cannibalism_irregular_infantry.txt:728` | Activation tech `:80`, templates around `:4905`, CXT token `:39`. |

The matching hidden technologies intentionally use `allow = { always = no }` and `ai_will_do = { factor = 0 }`; package effects grant them with `popup = no` in `common/scripted_effects/014_cannibalism_activation_effects.txt`. This is the current activation bridge and is not classified as a source defect. The latest unit handoff records partial technology MCP evidence with nine one-to-one tech-to-subunit rows and no reported source diagnostics.

Vanilla `elephantry` is included in the shared template at `common/scripted_effects/014_cannibalism_effects.txt:4848`, granted during warlord setup at `:5190`, CBL unification at `:12432`, and Wendigo inherited recruitment around `:18613`.

## Territory, state, starting setup, and player safety

Warlord formation selects an eligible live state, derives one of the three origins, transfers the selected state and up to two valid controlled neighbours, adds cores, and sets the selected origin state as capital. The source paths are `common/scripted_triggers/014_cannibalism_triggers.txt:3050-3107`, `:3612-3641`, and `common/scripted_effects/014_cannibalism_effects.txt:5334-5375`.

Rollback returns transferred states, removes Event 014 cores, clears actor and state references, and releases the slot only after reference checks in `common/scripted_effects/014_cannibalism_effects.txt:5280-5300` and `:5687-5724`.

The eight histories are dormant with empty `history/units/014_cannibalism_dormant.txt`, neutral politics, no public leader, and no starting army. Runtime setup creates templates, manpower, equipment, fuel, trains, convoys, and origin-specific forces. CBL inherits donor technology and recruitment through the unification effects. ZZZ's existing generic `ZZZ_leader`, infantry technology, and convoy setup remain separate from the Hannibal secrecy defect.

Host selection prioritizes a viable human host and refuses the dual-human displacement case. The CBL path records a human host before `change_tag_from`, and the Wendigo path preserves the original ZZZ host and donor ledger. These are source-level passes, not live-runtime proofs.

## Focus, event, GUI, map, and probability evidence blockers

The required read-only HOI4 MCP routes were attempted for each supported surface. No rewrite or map write was attempted.

- `hoi4_focus_inspect` first returned `MCP error -32602` because the installed schema rejected the supplied `refresh` key. The schema-correct retry and `hoi4_focus_render` both timed out after 180 seconds. Focus claims above are source evidence only.
- `hoi4_map_inspect` for representative state IDs 1-10 and 219-226 timed out after 180 seconds. No map render was treated as evidence. State transfer, rail, port, supply, adjacency, and building positions therefore remain MCP-unresolved.
- Combined read-only `hoi4_event_inspect`, `hoi4_event_render`, `hoi4_tech_inspect`, and GUI inspection calls produced no result before the parent-directed stop of long-running checks. Event and GUI claims above are source evidence only.
- The installed package exposes no Technology Tree Viewer. The latest unit activation handoff has only partial `hoi4.tech_inspect` and `hoi4.tech_render` artifacts, and the hidden unplaced nodes cannot receive a full tree-viewer confirmation.
- No callable `chaosx_ai_probability_auditor` appears in the installed tool inventory. A generic `hoi4.probability_inspect` attempt with an explicit workspace returned `WORKSPACE_NOT_REGISTERED`; the no-workspace retry was stopped after it continued running. No quantitative AI or probability claim is made here.

## Asset and portrait evidence

Portrait production and source-recovery ownership is recorded in `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_portrait_source_recovery_v6.md`. The runtime aliases in `interface/014_cannibalism.gfx` point to the retained Event 014 portrait package, and no runtime reference into the durable source archive was found during this audit.

Protected Hannibal DDS hashes checked during this audit are:

- `gfx/leaders/014_cannibalism/hannibal.dds` SHA-256 `5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88`.
- `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` SHA-256 `26D7566F7B93D17C4D7FDE5B262AB8B6E4B04FBA0B862315404D6A33ABE34717`.
- `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds` SHA-256 `F67A1B33A1D4F9B9B1B5EC0D6FB716AD1F2342083E9992550B5DD7356F590587`.
- `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds` SHA-256 `F0DFA61EA29293F8393711F97EB67524D336CB6C2A2D55734C0C38484219D18B`.

No protected DDS file, flag, portrait, icon, or other asset was changed.

## Handoff priorities and simplifications

1. Fix the two static Hannibal recruitments before any release claim. Preserve the reveal event ordering by recruiting immediately before role promotion or by changing the reveal trigger contract.
2. Decide whether Event 014 requires advisor and high-command slots. If yes, create a bounded identity-specific package. If no, record the command-idea substitution in the design source of truth.
3. Confirm the intended cultural scope of the Oceania name pool before the next identity or portrait pass.
4. Re-run the required focus, event, GUI, map, technology, and probability MCP routes when their workspace registration and tool availability are restored. Do not treat source-only evidence as replacing those routes.

No gameplay, map, localisation, portrait, flag, unit, technology, AI, or other asset simplification was implemented in this audit. The only unresolved omissions are the documented MCP evidence blockers and the source defects and design warnings listed above.

## Changed files

- Added `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_country_package_audit_2026-08-24_exact_stage.md`.
- No other file was intentionally changed by this audit.
