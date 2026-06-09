# Event 006 Country Package Audit Handoff - 2026-05-30 06:48:52 UTC

Read-only country package audit for Event 006 Independence Wave. No gameplay, localisation, interface, asset, or source-spec files were patched. This is a planning handoff, not a completion claim.

## Instructions and References Applied

- Repository instructions: `AGENTS.md`.
- Skills: `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`.
- Offline wiki pages consulted before repo conclusions: `Data structures`, `Triggers`, `Effect`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`, `Country creation`, `State modding`, `National focus modding`.
- Vanilla documentation consulted: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`, `dynamic_variables_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, `script_collection_input.md`, `script_collection_operator.md`, `common/script_constants/documentation.md`.

## Files Inspected

Event 006 source and current implementation:

- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_29_starter_package_viability_audit.md`
- `docs/events/006_independence_wave.md`
- `events/006_independence_wave.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/decisions/categories/006_independence_wave_categories.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`

Country and contamination surfaces:

- `common/country_tags/chaosx_countries.txt`
- `common/countries/Old Great Bulgaria.txt`
- `common/countries/Pale Railway Authority.txt`
- `history/countries/OGB - Old Great Bulgaria.txt`
- `history/countries/PRA - Pale Railway Authority.txt`
- `localisation/english/chaosx_countries_l_english.yml`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/ai_strategy/005_soviet_collapse.txt`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`
- `interface/005_soviet_collapse_custom_icons.gfx`

Vanilla evidence:

- `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt`
- `~/projects/Hearts of Iron IV/common/countries/Assyria.txt`
- `~/projects/Hearts of Iron IV/common/countries/Danzig.txt`
- `~/projects/Hearts of Iron IV/common/countries/Uganda.txt`
- `~/projects/Hearts of Iron IV/common/countries/Sokoto.txt`
- `~/projects/Hearts of Iron IV/common/countries/Khiva.txt`
- `~/projects/Hearts of Iron IV/history/countries/ASY - Assyria.txt`
- `~/projects/Hearts of Iron IV/history/countries/DNZ - Danzig.txt`
- `~/projects/Hearts of Iron IV/history/countries/UGA - Uganda.txt`
- `~/projects/Hearts of Iron IV/history/countries/SOK - Sokoto.txt`
- `~/projects/Hearts of Iron IV/history/countries/KHI - Khiva.txt`
- `~/projects/Hearts of Iron IV/history/states/85-Danzig.txt`
- `~/projects/Hearts of Iron IV/history/states/249-Kazan.txt`
- `~/projects/Hearts of Iron IV/history/states/256-Cheboksary.txt`
- `~/projects/Hearts of Iron IV/history/states/548-Uganda.txt`
- `~/projects/Hearts of Iron IV/history/states/570-TS 12.txt`
- `~/projects/Hearts of Iron IV/history/states/571-TS 13.txt`
- `~/projects/Hearts of Iron IV/history/states/676-Mosul.txt`
- `~/projects/Hearts of Iron IV/history/states/781-Niger.txt`
- `~/projects/Hearts of Iron IV/history/states/831 - Khiva.txt`
- `~/projects/Hearts of Iron IV/history/states/832 - Dashhowuz.txt`
- `~/projects/Hearts of Iron IV/history/states/901-Borno.txt`
- `~/projects/Hearts of Iron IV/history/states/902-Sokoto.txt`
- `~/projects/Hearts of Iron IV/history/states/949 - Aysen.txt`
- `~/projects/Hearts of Iron IV/history/states/950 - Araucania.txt`
- `~/projects/Hearts of Iron IV/common/characters/ASY.txt`
- `~/projects/Hearts of Iron IV/common/characters/UGA.txt`
- `~/projects/Hearts of Iron IV/common/characters/SOK.txt`
- `~/projects/Hearts of Iron IV/common/characters/KHI.txt`
- `~/projects/Hearts of Iron IV/interface/_leader_portraits.gfx`
- `~/projects/Hearts of Iron IV/localisation/english/countries_l_english.yml`
- `~/projects/Hearts of Iron IV/localisation/english/parties_l_english.yml`
- `~/projects/Hearts of Iron IV/localisation/english/goe_characters_l_english.yml`
- `~/projects/Hearts of Iron IV/localisation/english/WUW_characters_l_english.yml`

## Package Viability Table

| Package | Current status | Tag and state evidence | Asset/localisation/history evidence | Event 005 contamination risk | Verdict |
| --- | --- | --- | --- | --- | --- |
| `OGB` Volga / Old Great Bulgaria | Implemented as an Event 006 starter mini-package. `independence_wave_seed_verified_package_candidates` adds OGB cores to `249` and `256`; setup assigns `independence_wave_package_volga_bulgaria`; focus/decision/log proof exists. | Repo tag: `common/country_tags/chaosx_countries.txt`. State proof: vanilla `249` Kazan is `SOV`/`TAT` core, town, VP 10; vanilla `256` Chuvashia is `SOV`/`CHU` core, town. Event 006 adds OGB cores before release. | Repo country/history/localisation/flags exist. `history/countries/OGB - Old Great Bulgaria.txt` creates institutional leader `The Volga Restoration Council`; flags exist in all three sizes. Current Event 006 idea/focus/decision loc exists. | High. OGB is an Event 005 high-chaos successor too. Event 006 guards content with `chaosx_release_origin_independence_wave`, but base history comment and leader portrait sprite are Event 005-branded (`interface/005_soviet_collapse_factory_ancient_icons.gfx`, `gfx/leaders/005_soviet_collapse/OGB_leader.dds`). Event 005 effects also add OGB cores/transfer states. | Usable as current separation-test package, but still has asset/leader-source contamination risk if strict Event 006 asset separation is required. Do not expand with Event 005 OGB focus, decisions, event logs, formables, or helper state. |
| `ASY` Assyria | Implemented as an Event 006 starter mini-package through generic release pool plus package scoring. Setup assigns `independence_wave_package_assyria`, spirit, focus hook, decisions, and log entries. | Vanilla tag: `ASY = "countries/Assyria.txt"`. State `676` Mosul has owner `IRQ`, cores `IRQ`, `KUR`, `ASY`, oil, VPs Mosul/Kirkuk/Erbil. | Vanilla country/history/characters/localisation/party names/flags exist. `ASY_shimun_eshai` and `ASY_benjamin_arsanis` are recruited; portraits are defined in vanilla `_leader_portraits.gfx`. | Low. No direct Event 005 `ASY` surfaces found. Shared generic Event 006 tree only. | Usable current starter package. Remaining work is depth: bespoke route, AI profile, state-group proof beyond Mosul if desired, and asset/source review for final Event 006-specific icons. |
| `DNZ` Danzig Free City | Implemented as an Event 006 starter mini-package through city/port pool plus package scoring. Setup assigns `independence_wave_package_danzig_free_city`, free-city spirit, focus hook, decisions, and log entries. | Vanilla tag: `DNZ = "countries/Danzig.txt"`. State `85` Danzig has owner `POL`, cores `POL`, `DNZ`, `KSH`, city category, naval base, dockyards, VP 10, demilitarized zone. | Vanilla country/history/localisation/party names/flags exist. `DNZ` history uses named leaders including Albert Forster and Arthur Brill; Danzig flags exist in all sizes. | Low. No Event 005 Danzig-specific surfaces found. | Usable current starter package. Remaining work is deeper free-city/free-port branch, guarantees, patron/city diplomacy, and port-specific AI behavior. |
| `UGA` Buganda / Uganda carrier | Not implemented in Event 006. No current package id, trigger, focus, decision, idea, or log hook. | Vanilla tag: `UGA = "countries/Uganda.txt"`. State `548` Uganda has owner `ENG`, core `UGA`, rural category, rubber, VP 1. Vanilla localisation explicitly supports `UGA_neutrality = "Kingdom of Buganda"` and `UGA_neutrality_ADJ = "Bugandan"`. | Vanilla country/history/characters/localisation/flags exist. `UGA` history recruits many generic/advisor characters and has democratic default politics. | Low. No Event 005 `UGA` surfaces found. | Viable next package if parent accepts `UGA` as the Buganda carrier. This is not a fallback if the package explicitly defines the Buganda route as the neutrality/local-polity/protectorate outcome on the vanilla Uganda tag. |
| Mapuche / Araucania | Not implemented. No independent Event 006 package surface. | No standalone `MAP`/Mapuche tag found in repo or vanilla. Vanilla states `950` Araucania and `949` Aysen are Chilean cores/owned by `CHL`; no Mapuche core/tag exists. | Repo has cosmetic country entries `CHL_mapuche_state` and `kingdom_of_araucania_and_patagonia`; vanilla has Chilean/cosmetic support, not an independent release tag. | Low Event 005 risk, but no real independent package carrier. | Blocked under no-fallback rule. Do not use `CHL` plus cosmetic tag as an Event 006 independent package. Needs explicit real tag creation/approval and source-aware assets. |
| `PRA` Pale Railway Authority | Not implemented in Event 006. Current Event 006 has a generic railway package type and railway pool gate, but no PRA seed, package id, idea, focus hook, decision, or log hook. | Repo tag: `PRA = "countries/Pale Railway Authority.txt"`. Event 005 uses states `570` Novosibirsk and `571` Omsk by adding cores/transfers in `005_soviet_collapse_effects.txt`; no persistent state-history cores for PRA were found. | Repo country/history/localisation/flags/portrait exist, all Event 005-branded. PRA history uses `GFX_portrait_PRA_timetable_authority_board` but assigns random single-person names and sets Soviet-collapse random-name flags. | Very high. PRA is an Event 005 high-chaos successor with Event 005 focus/decision/category/AI/localisation/portrait surfaces. | Queued, not next. Needs an Event 006-specific railway carrier plan or explicit PRA origin separation, institutional leader override, Event 006 core seed, and no Event 005 focus/decision/helper/log use. |
| `SOK` Sokoto | Additional viable high-chaos package identified. Not implemented in Event 006. | Vanilla tag: `SOK = "countries/Sokoto.txt"`. State proof: `902` Sokoto owner `ENG`, cores `NGA`/`SOK`, VP 1; `901` Borno owner `ENG`, cores `NGA`/`SOK`; `781` Niger owner `FRA`, cores `NGR`/`SOK`. One-state start on `902` is viable; later claims can target `901`/`781` through proof. | Vanilla country/history/characters/localisation/party names/flags exist. `history/countries/SOK - Sokoto.txt` recruits `SOK_siddiq_abubakar`; portrait is defined in vanilla `_leader_portraits.gfx`; country loc supports `SOK_neutrality = "Sokoto Caliphate"` plus democratic/fascist/communist variants. | Low. No Event 005 `SOK` surfaces found. | Viable next high-chaos package. Best implemented as `iw_pkg_sokoto`, Evo IV historical-return/emirate federation, initial state `902`, optional cross-colonial proof for `901` and `781`. |
| `KHI` Khiva | Additional evidence checked but not recommended for this tranche. Not implemented in Event 006. | Vanilla tag: `KHI = "countries/Khiva.txt"`. States `831` Khiva and `832` Dashhowuz both owned by `SOV`, core `KHI`, with `831` as capital. | Vanilla country/history/characters/localisation/party names/flags exist. | Medium/high. Event 005 progressive release logic references `KHI` as a Soviet-collapse candidate in `005_soviet_collapse_triggers.txt` and `005_soviet_collapse_effects.txt`. | Viable in principle, but queue behind a separate Event 005 separation audit. Do not include in the immediate no-fallback tranche while UGA and SOK are cleaner. |

## Country Package Coverage Checklist

| Surface | OGB | ASY | DNZ | UGA/Buganda | Mapuche | PRA | SOK |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Real tag | Yes, repo | Yes, vanilla | Yes, vanilla | Yes, vanilla | No | Yes, repo | Yes, vanilla |
| Valid start state | Yes, Event 006 adds `249`/`256` cores | Yes, `676` | Yes, `85` | Yes, `548` | States only, no tag | Needs Event 006 core seed | Yes, `902` |
| Host survival evidence | `SOV` must control >2 states; capital excluded | Iraq keeps Baghdad and other states | Poland keeps capital and other states | England keeps capital and global empire states | N/A until tag exists | Needs new proof | England keeps other states; multi-host claims delayed |
| Country/history file | Yes, Event 005-branded | Yes | Yes | Yes | No | Yes, Event 005-branded | Yes |
| Base localisation | Yes | Yes | Yes | Yes, includes Buganda neutrality | Cosmetic only | Yes, Event 005-branded | Yes |
| Party localisation | Mostly Event 005 custom | Yes | Yes | Vanilla/generic support | No independent party loc | Event 005 custom | Yes |
| Flags | Yes, repo | Yes, vanilla | Yes, vanilla | Yes, vanilla | Cosmetic only | Yes, repo | Yes, vanilla |
| Leader/portrait safe | Institutional council, but sprite path is Event 005-branded | Vanilla leaders/portraits | Vanilla leaders/portraits | Needs Buganda source review; vanilla roster exists | Blocked | Unsafe for Event 006 until institutionalized | Vanilla leader/portrait |
| Event 006 package id | Yes | Yes | Yes | Missing | Missing | Missing | Missing |
| Event 006 focus overlay | Mini-overlay | Mini-overlay | Mini-overlay | Missing | Missing | Missing | Missing |
| Event 006 decisions | Formation Ledger package decisions | Formation Ledger package decisions | Formation Ledger package decisions | Missing | Missing | Missing | Missing |
| Event 006 startup idea | Yes | Yes | Yes | Missing | Missing | Missing | Missing |
| Event 006 log milestones | Yes | Yes | Yes | Missing | Missing | Missing | Missing |
| Event 005 risk | High | Low | Low | Low | Low | Very high | Low |

## File Surface Checklist

- Tag registration: OGB/PRA in repo `common/country_tags/chaosx_countries.txt`; ASY/DNZ/UGA/SOK/KHI in vanilla `00_countries.txt`.
- Country definitions: OGB/PRA in repo `common/countries`; ASY/DNZ/UGA/SOK/KHI in vanilla `common/countries`.
- Country history: OGB/PRA repo files are Event 005-branded; ASY/DNZ/UGA/SOK/KHI vanilla files are usable as base releasables.
- State setup: audited `85`, `249`, `256`, `548`, `570`, `571`, `676`, `781`, `831`, `832`, `901`, `902`, `949`, `950`.
- Event 006 release and package logic: OGB/ASY/DNZ only.
- Focus loading: all Event 006 releases load `independence_wave_liberation_provisional_tree` only after `chaosx_release_origin_independence_wave`; no Event 005 focus-tree load found in Event 006 files.
- Decisions and missions: OGB/ASY/DNZ package decisions exist inside `independence_wave_formation_ledger_category`; UGA/Mapuche/PRA/SOK are absent.
- Ideas: OGB/ASY/DNZ package spirits exist in `common/ideas/006_independence_wave_ideas.txt`; UGA/Mapuche/PRA/SOK are absent.
- Localisation: OGB/ASY/DNZ Event 006 package text exists in `006_independence_wave_l_english.yml`; UGA/Mapuche/PRA/SOK Event 006 package text absent.
- Event log: OGB/ASY/DNZ package/formation log types exist in constants, effects, scripted localisation, and `chaosx_gui_l_english.yml`; UGA/Mapuche/PRA/SOK absent.
- AI: current package-specific AI is limited to focus/decision weights. No `common/ai_strategy/006_independence_wave*.txt` package strategies found.
- Assets: current Event 006 package icons use generic sprites; docs list future stable Event 006 sprite names for OGB/ASY/DNZ. OGB/PRA bespoke visual assets remain in Event 005 asset folders.

## Missing or Stale Country Package Surfaces

- `UGA`/Buganda: missing Event 006 package id, package flag, seed/scoring override, startup idea, focus overlay, package decisions, package log rows, Event 006 localisation, AI route preference, and source-reviewed leader/flag plan.
- `SOK`/Sokoto: missing the same Event 006 package surfaces as UGA. Vanilla support is strong enough to implement next without fallback.
- Mapuche: missing a real independent tag, country definition, history, country localisation, flags, leader/portrait plan, and Event 006 package surfaces.
- `PRA`: missing Event 006 core seed and all origin-separated package surfaces. Existing assets/history/focus/decision/AI are Event 005-branded and should not be reused directly.
- `OGB`: current Event 006 gameplay is present, but base leader portrait sprite and DDS path are Event 005-branded. If the parent treats visual asset paths as part of Event 005 separation, add an Event 006 portrait/sprite alias or institutional leader override before expanding.
- `ASY`/`DNZ`: current starter implementations are functional mini-packages, not complete deep packages. They still need package-specific route depth, AI strategies, final package icons, and richer diplomatic/formation aftermath.

## Map and State Setup Issues

- Host survival is guarded generically by `can_independence_wave_host_release_current_candidate_safely` and OGB-specific `num_of_controlled_states > host_survival_volga_state_floor`. This is skip-only validation, not reduced-territory shrink logic.
- OGB starts from Event 006-added cores on `249` Kazan and `256` Chuvashia. This is valid only when one host controls both and has enough other controlled states. It should not be expanded into extra Volga/Kama states without separate state proof.
- ASY on `676` Mosul is a clean one-state start. Iraq keeps other core/capital territory in normal starts.
- DNZ on `85` Danzig is a clean one-state city/free-port start. Poland keeps other territory in normal starts.
- UGA on `548` Uganda is a clean one-state start. England host survival is safe in normal starts.
- SOK should start only on `902` Sokoto for the first tranche. `901` Borno and `781` Niger cross owner/colonial borders and should be claims or later proof decisions, not free initial release states.
- PRA has no persistent state-history cores; Event 005 adds cores/transfers dynamically. Event 006 cannot release PRA without its own core seed and should not borrow Event 005 setup.
- Mapuche has plausible state geography (`950`, `949`) but no independent tag/core path, so no safe release can be made.

## Politics, Leader, Portrait, Flag, Advisor, and Party Issues

- OGB uses institutional leader `The Volga Restoration Council`, which is conceptually safe for a council portrait. Risk: the portrait sprite is registered in an Event 005 `.gfx` file and points to an Event 005 folder.
- PRA is unsafe for Event 006 as-is: it uses institutional-board portrait art with random single-person male names and Soviet-collapse random-name flags. For a railway authority, Event 006 should use an institutional leader name such as a board/court/authority, not personal random pools.
- UGA/Buganda must not invent a kabaka or royal portrait. Use vanilla `UGA` character support if acceptable, or an institutional Lukiko/council leader plan with sourced/generated asset routing later.
- SOK has vanilla leader `SOK_siddiq_abubakar` and vanilla portrait definition. If Event 006 wants an institutional council route instead of the real leader, that needs a separate source/asset decision; vanilla support is already usable.
- ASY and DNZ have vanilla leaders/portraits and party names. Event 006 can use them for initial viability, but later high-chaos route changes should source or institutionalize any new leaders.
- Mapuche requires a full tag/leader/flag/source package before implementation.

## Focus, Decision, Idea, and Asset Issues

- OGB/ASY/DNZ have mini-overlays, not full route families:
  - OGB: `independence_wave_volga_archive_opened`, `independence_wave_council_of_the_old_name`, Volga archive/assembly/ministry decisions.
  - ASY: `independence_wave_assyrian_recognition_congress`, recognition congress decisions.
  - DNZ: `independence_wave_danzig_free_city_board`, free-city board/charter decisions.
- UGA/SOK next tranche should add:
  - package constants `buganda` and `sokoto`
  - flags `independence_wave_package_buganda` and `independence_wave_package_sokoto`
  - package identity triggers `is_independence_wave_buganda_package` and `is_independence_wave_sokoto_package`
  - state-control triggers for `548` and `902`
  - package startup spirits
  - 1-2 package focus mini-overlays each
  - 2-3 package Formation Ledger decisions each
  - event-log types, scripted localisation mappings, and GUI localisation keys
  - Event 006 localisation for all new ideas/focuses/decisions/tooltips
  - generic placeholder icon use only if wired as Event 006 sprites or explicitly documented as temporary; no fallback tags
- PRA should not use Event 005 PRA focus icons, decision icons, ideas, focus tree, or AI. Its first safe step is an Event 006 railway package design with a neutral/institutional leader override.
- Asset routing remains incomplete for all packages. Current package docs list desired Event 006 sprite names for OGB/ASY/DNZ, but no final Event 006-specific art package was inspected.

## Starting Military, Technology, Industry, Supply, and Production Issues

- Current Event 006 release setup grants generic manpower and equipment to every release. It does not add package-specific OOBs or production lines.
- Vanilla ASY/DNZ/UGA/SOK/KHI history files define baseline technologies, but Event 006 releases also receive shared Event 006 startup equipment through `independence_wave_setup_released_country`.
- DNZ has meaningful starting industry/port/dockyard state setup in `85`.
- ASY has oil in `676` but little industry.
- UGA and SOK are rural/pastoral, low-industry packages. Their mini-overlays should include grounded defensive/administrative support rather than large armies.
- PRA railway package would need supply/railway-specific state proof and should not receive large armies without design support.

## AI and Playability Issues

- Event 006 package AI is currently only local `ai_will_do` on focuses and decisions. There are no package-level AI strategies for OGB/ASY/DNZ, and none for UGA/SOK/PRA/Mapuche.
- ASY and DNZ are playable starter packages but shallow. Their core proof decisions give identity/legitimacy, not broad expansion or route depth.
- UGA and SOK can be implemented without fallback but need AI preferences for local-polity/historical-return behavior, conservative expansion, and patron resistance.
- Mapuche is not playable as an independent package until a real tag is created.
- PRA is not safely playable through Event 006 until Event 005 separation is handled.

## Recommended Next Package Tranche

Implement exactly two packages next:

1. `iw_pkg_buganda` using vanilla `UGA` as the carrier.
   - Tag: `UGA`.
   - Initial state: `548` Uganda.
   - Package family: local-polity/protectorate-memory historical return.
   - Evidence: vanilla tag/country/history/flags/characters, `UGA_neutrality = "Kingdom of Buganda"`, state `548` core.
   - Event 005 risk: low; no Event 005 `UGA` surfaces found.
   - Required Event 006 surfaces: constants, scoring override, `independence_wave_package_buganda`, `is_independence_wave_buganda_package`, state-control trigger for `548`, startup spirit, Lukiko/protectorate-record focus mini-overlay, 2-3 Formation Ledger decisions, package log types, localisation, AI weights, docs update.
   - Design caution: parent must explicitly accept `UGA` as the Buganda package carrier. Do not create a fake `BUG` fallback.

2. `iw_pkg_sokoto` using vanilla `SOK`.
   - Tag: `SOK`.
   - Initial state: `902` Sokoto.
   - Later proof/claims only: `901` Borno, `781` Niger.
   - Package family: Evo IV historical-return / emirate federation.
   - Evidence: vanilla tag/country/history/flags/characters, `SOK_neutrality = "Sokoto Caliphate"`, party localisation, state `902` core and VP.
   - Event 005 risk: low; no Event 005 `SOK` surfaces found.
   - Required Event 006 surfaces: constants, scoring override, `independence_wave_package_sokoto`, `is_independence_wave_sokoto_package`, state-control trigger for `902`, startup spirit, scholar council/emirate federation focus mini-overlay, Formation Ledger decisions for Sokoto council and northern emirates proof, event-log types, localisation, conservative border/claim hooks, AI weights, docs update.

Do not add a third package in the same tranche unless the parent specifically wants broader scope. `KHI`/Khiva is vanilla-supported but already appears in Event 005 Soviet-collapse release logic, so it needs a shared-tag separation check similar to OGB before it is safe. `PRA` and Mapuche are not safe immediate packages.

## Blocked or Queued Packages

- Mapuche / Araucania: blocked. No independent tag or country package exists. Existing support is cosmetic Chile-only. Needs explicit tag creation/approval and source-aware flag/leader plan.
- `PRA` railway: queued. Real repo tag exists, but Event 005 contamination is too high, state cores are not persistent outside Event 005 setup, and leader/portrait/name handling is unsafe for Event 006.
- `KHI` Khiva: queued, not blocked. Vanilla support is strong, but Event 005 progressive release logic already references the tag. Needs Event 005 separation audit before Event 006 implementation.
- Broader OGB expansion: queued. Current OGB starter package works as a separation test, but extra Volga/Kama states or Event 006-specific assets need separate proof and asset routing.
- Full Mapuche/Buganda/Sokoto final assets: queued. Real/historical leaders, symbols, and final flags/icons require source or asset-subagent work before final polish.

## Validation Commands and Evidence

Representative commands run:

```bash
rg -n "\b(OGB|ASY|DNZ|UGA|PRA|Mapuche|Buganda|Volga|Assyria|Danzig|Sokoto|SOK)\b" events common history localisation docs
rg -n "can_independence_wave_seed_volga_bulgaria_package|independence_wave_volga_old_state_memory|independence_wave_assyrian_recognition_congress_spirit|independence_wave_free_city_board_spirit" events common localisation docs
rg -n "\b(ASY|DNZ|UGA|SOK|KHI)\b" ~/projects/'Hearts of Iron IV'/common/country_tags ~/projects/'Hearts of Iron IV'/history/countries ~/projects/'Hearts of Iron IV'/history/states ~/projects/'Hearts of Iron IV'/localisation/english
find gfx/flags -maxdepth 3 -type f \( -name 'OGB*' -o -name 'PRA*' \)
find ~/projects/'Hearts of Iron IV'/gfx/flags -maxdepth 3 -type f \( -name 'ASY*' -o -name 'DNZ*' -o -name 'UGA*' -o -name 'SOK*' -o -name 'KHI*' \)
rg -n "add_core_of\s*=\s*PRA|add_core_of\s*=\s*OGB|add_core_of\s*=\s*SOK|add_core_of\s*=\s*UGA" history common ~/projects/'Hearts of Iron IV'/history/states
rg -n "\b(KHI|SOK|UGA)\b" common/decisions/005_soviet_collapse_decisions.txt common/national_focus/005_soviet_collapse_republics.txt common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt
git status --short
```

Evidence highlights:

- The older starter audit blockers for OGB missing trigger/idea are stale: `can_independence_wave_seed_volga_bulgaria_package` now exists, and `independence_wave_volga_old_state_memory` is defined in ideas and localisation.
- OGB/ASY/DNZ package identifiers are present in Event 006 effects/triggers/focuses/decisions/ideas/log localisation.
- UGA/SOK/PRA/Mapuche package identifiers are absent from current Event 006 implementation files.
- PRA and OGB have Event 005 surfaces; ASY/DNZ/UGA/SOK do not show Event 005 contamination in the searched Event 005 files.
- No live HOI4 load, parser validation, or in-game validation was run. This was a read-only planning audit.

## Remaining Risks and Uncertainty

- Current Event 006 implementation files are untracked or dirty in the worktree. This audit treats the worktree as the current implementation because the parent explicitly named those files.
- The generic resolver still uses skip-only host survival validation. It does not implement reduced-territory release shrinkage.
- OGB asset separation is unresolved if Event 005 visual asset paths are considered prohibited, not just Event 005 gameplay flags/helpers.
- Vanilla country histories may bring in vanilla leaders and politics that are acceptable for viability but not yet tailored to Event 006 identity.
- UGA as Buganda requires parent acceptance of the vanilla `UGA` carrier. Without that acceptance, Buganda remains queued, not blocked by state/tag availability.
- SOK multi-state ambitions cross colonial owners; first implementation should start on `902` only and put `901`/`781` behind claims/proof.
- No fallback packages were recommended.
