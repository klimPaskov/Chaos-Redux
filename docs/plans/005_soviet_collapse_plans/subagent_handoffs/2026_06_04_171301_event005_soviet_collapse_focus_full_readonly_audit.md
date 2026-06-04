# Event 005 Soviet Collapse Focus Trees - Current Worktree Read-Only Audit

Timestamp: 2026-06-04 17:13 UTC  
Agent role: `chaosx_focus_tree_auditor`  
Scope: all current-worktree Soviet Collapse focus trees and supporting idea/effect/trigger/decision/localisation surfaces.  
Edit mode: read-only for gameplay/script/localisation. This report is the only file written.

## Executive Findings

1. Direct focus-level idea spam is not present in the current worktree. The four focus files contain no direct `add_ideas` calls inside focus rewards; focus idea changes are helper-driven or setup/decision-driven.
2. Helper-induced duplicate same-idea spam is mostly fixed. The main suspected repeat helpers now use guards or swap models: PRA clears and replaces authority ideas before adding one (`common/scripted_effects/005_soviet_collapse_effects.txt:7795-7854`), CFR only adds `cfr_construction_mandates` if missing (`:11204-11208`), and MFR setup/decision helpers guard `mfr_arsenal_quotas` / `mfr_factory_guard_state` (`:11964-11983`, `:17411`).
3. The remaining reward problem is helper-only focus spam: many focuses still reward only a flag plus a generic helper, often with tiny stat/building deltas. This hides reward shape from the focus file and leaves political/industry/expansion branches unclear even when helpers have payloads.
4. Several chaos concepts that should be overpowered are still structurally small or weak. The 18-focus trees (`TSC`, `RMC`, `DSC`, `NRF`, `ICD`) and the 16-focus ancient trees are the clearest offenders; PRA is thematically strong but still too short for a rail-state concept.
5. Layout is better than earlier audits on duplicate coordinates: no duplicate `(x,y)` focus coordinates were found. The major remaining pathline risk is dense one-step spacing and same-row/reversed prerequisite lines, especially Ukraine, Central Asia, PRA, MFR, DSC/ICD, and ancient charter joins.
6. Focus filters still do not always match visible reward behavior. The worst reliable examples are ancient charter focuses using `FOCUS_FILTER_ANNEXATION` while providing charters/decisions/logistics rather than direct claims, cores, wargoals, or annexation effects.

## References Consulted

Required project guidance:

- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

Required offline wiki pages:

- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`

Vanilla references:

- `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- Vanilla focus examples in `/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt`
- Vanilla focus examples in `/home/klim/projects/Hearts of Iron IV/common/national_focus/estonia.txt`

## Idea Spam Audit

### Direct focus idea spam

No direct `add_ideas`, `remove_ideas`, `swap_ideas`, or `add_timed_idea` calls were found inside the four audited focus-tree files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

The direct idea changes are in decisions and scripted effects:

- `common/decisions/005_soviet_collapse_decisions.txt:66` adds `soviet_collapse_emergency_union_authority`.
- `common/decisions/005_soviet_collapse_decisions.txt:105` adds `soviet_collapse_loyalist_officer_corps`.
- `common/decisions/005_soviet_collapse_decisions.txt:2405` removes `soviet_collapse_union_crisis` and adds `soviet_collapse_union_restored`.
- `common/scripted_effects/005_soviet_collapse_effects.txt:1426` adds `soviet_collapse_union_crisis`.
- `common/scripted_effects/005_soviet_collapse_effects.txt:3929` adds `soviet_collapse_republican_startup_disorder`.

### Helper-induced idea spam

Current evidence points to guarded or swapping helpers rather than duplicate-add spam:

- `common/scripted_effects/005_soviet_collapse_effects.txt:7795-7854`: `soviet_collapse_update_pra_authority_idea` clears PRA authority ideas and adds only one current authority idea, with `NOT = { has_idea = ... }` guards.
- `common/scripted_effects/005_soviet_collapse_effects.txt:11204-11208`: `soviet_collapse_ensure_cfr_construction_mandates_idea` only adds `cfr_construction_mandates` if missing. It is called repeatedly at `:11216`, `:11283`, `:11318`, and `:11531`, but the guard prevents duplicate same-idea spam.
- `common/scripted_effects/005_soviet_collapse_effects.txt:11964-11969`: `soviet_collapse_apply_mfr_audit_arsenal_orders` only adds `mfr_arsenal_quotas` if missing.
- `common/scripted_effects/005_soviet_collapse_effects.txt:11978-11983`: `soviet_collapse_apply_mfr_convert_depots_to_arms_lines` only adds `mfr_factory_guard_state` if missing.
- `common/scripted_effects/005_soviet_collapse_effects.txt:17014-17022`: DSC dead-army updater removes prior staged ideas before adding `dsc_dead_army_politics`.
- `common/scripted_effects/005_soviet_collapse_effects.txt:17391-17980`: high-chaos setup ideas use guarded `add_ideas` blocks for CFR, MFR, KRS, FTH, BBH, BSC, RMC, DSC, TNC, ALA, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, OGB, BAC, TSC, ICD, ARD, NRF, and NLC.

Remaining risk:

- `common/scripted_effects/005_soviet_collapse_effects.txt:5566-5613` clears a large set of older republic staged ideas.
- `common/scripted_effects/005_soviet_collapse_effects.txt:5720` defines `soviet_collapse_update_consolidated_republic_ideas`, which is called very frequently from helper rewards and decisions, but this current version mostly clears/clamps and does not visibly add replacement staged ideas. That avoids duplicate idea spam but leaves many republic focus rewards as variable-only or tooltip-only identity.
- MFR can keep both `mfr_arsenal_quotas` and `mfr_factory_guard_state` as permanent identity carriers (`:11964-11983`). This is not duplicate same-idea spam, but it is a stacked permanent-idea model rather than a clear staged/swap model.

## Tree-by-Tree Matrix

Legend: `F` focus count. `Pol/Ind/Ann/Mil` are focus-filter counts. `Map` is direct focus-block claim/core/wargoal evidence. `Bld` is direct focus-block building evidence. `Helpers` is helper-call count. `Mutex` is mutual-exclusion entry count. `Risk` is the audit conclusion.

| Tree | F | Pol | Ind | Ann | Mil | Map | Bld | Helpers | Mutex | Risk |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Ukraine | 83 | 58 | 17 | 4 | 41 | 0 | 10 | 97 | 4 | Large tree, but expansion/industry rewards rely heavily on helpers; same-row pathline risk remains at `ukr_soviet_collapse_bread_state_whispers` (`republics.txt:2065`). |
| Breakaway fallback | 36 | 23 | 9 | 0 | 17 | 0 | 11 | 35 | 0 | Functional fallback, but still a compact generic government tree with no direct expansion surface. |
| Internal republic | 62 | 33 | 24 | 1 | 27 | 1 | 45 | 72 | 6 | Better industry payload density, but generic helper dependence remains high. |
| Baltic shared | 42 | 28 | 9 | 0 | 18 | 0 | 17 | 41 | 0 | Political/military filters dominate; no direct expansion branch evidence. |
| Caucasus shared | 40 | 28 | 13 | 0 | 13 | 0 | 12 | 40 | 0 | Shallow shared regional tree; helper-only reward shape remains unclear. |
| Central Asia shared | 45 | 32 | 9 | 1 | 16 | 7 | 21 | 48 | 4 | Has map payload, but pathline risk from same-row expansion join at `central_asia_soviet_collapse_the_southern_shield` (`republics.txt:7272`). |
| Moldova | 48 | 35 | 12 | 0 | 13 | 0 | 18 | 51 | 6 | Political-heavy, no direct expansion evidence, several compact route locks. |
| Belarus | 53 | 34 | 22 | 0 | 20 | 0 | 12 | 62 | 4 | Industry branch still not visually/payload-deep enough for rail/logistics potential. |
| Kazakhstan | 92 | 54 | 27 | 2 | 31 | 0 | 23 | 101 | 14 | Largest tree, but helper reliance remains extreme; many route locks and filters need player-visible payoff audit. |
| FTH | 47 | 28 | 15 | 0 | 26 | 0 | 15 | 74 | 2 | High helper count and generic helper-only reward chain; needs deeper free-territory mechanics. |
| PRA | 22 | 13 | 10 | 2 | 7 | 1 | 23 | 44 | 4 | Good rail payload and idea lifecycle, but only 22 focuses for a rail-state concept; expansion depth is thin. |
| TSC | 18 | 13 | 6 | 1 | 7 | 1 | 5 | 34 | 4 | Tiny chaos tree; concept does not receive enough political/industry/expansion depth. |
| RMC | 18 | 13 | 3 | 3 | 9 | 3 | 3 | 23 | 4 | Compact death/cult tree; expansion and industry are underbuilt. |
| DSC | 18 | 13 | 3 | 4 | 14 | 2 | 9 | 33 | 4 | Improved dead-army aggression, but still too small for the concept. Key node `DSC_grave_ordnance_claims` at `custom_splinters.txt:3007`. |
| NRF | 18 | 13 | 4 | 3 | 3 | 3 | 10 | 20 | 4 | Naval/dead fleet concept has weak military-filter count and shallow branch depth. |
| ICD | 18 | 13 | 4 | 3 | 9 | 3 | 3 | 19 | 4 | Death-state concept still very shallow; `ICD_claim_the_unburied_front` (`custom_splinters.txt:4228`) and `ICD_grave_columns_march` (`:4249`) are narrow. |
| BSC | 47 | 30 | 12 | 0 | 22 | 0 | 14 | 58 | 2 | Oasis/confederation identity exists, but no direct expansion evidence and high helper reliance. |
| TNC | 47 | 30 | 13 | 0 | 21 | 0 | 17 | 45 | 2 | Generic 47-focus shape; city-council concept needs stronger municipal mechanics. |
| ALA | 47 | 30 | 12 | 0 | 19 | 0 | 11 | 40 | 2 | Restoration concept is political-heavy but not payoff-heavy. |
| BBH | 47 | 26 | 13 | 0 | 28 | 0 | 12 | 51 | 2 | Militia concept should be more threatening; direct building/map evidence is modest. |
| KRS | 47 | 25 | 10 | 0 | 19 | 0 | 21 | 51 | 2 | Better infrastructure count, but route identity still helper-dependent. |
| UDC | 47 | 25 | 11 | 0 | 26 | 0 | 6 | 82 | 2 | High helper count and low direct building/map evidence; priority for reward specificity. |
| SDZ | 47 | 25 | 11 | 0 | 26 | 0 | 7 | 72 | 2 | Archive/security concept has weak visible industry/expansion payloads. |
| GAC | 47 | 26 | 15 | 0 | 24 | 0 | 11 | 45 | 2 | Village congress concept needs mechanical differentiation beyond helper deltas. |
| DHC | 47 | 27 | 13 | 0 | 23 | 0 | 20 | 45 | 2 | Better construction count, but still no direct expansion evidence. |
| KHC | 47 | 27 | 13 | 0 | 24 | 0 | 18 | 41 | 2 | Similar to DHC; needs sharper crossing-council mechanics. |
| FEV | 47 | 25 | 19 | 1 | 24 | 0 | 28 | 54 | 2 | Stronger industry/logistics count; expansion payoff still helper-hidden. |
| SZA | 47 | 25 | 18 | 0 | 24 | 0 | 24 | 51 | 2 | Better building payload density; political route identity still shallow. |
| UWD | 47 | 25 | 17 | 0 | 24 | 0 | 29 | 48 | 2 | Factory-guard concept is stronger than most generic chaos trees; expansion still absent. |
| MRC | 47 | 25 | 13 | 0 | 26 | 0 | 22 | 49 | 2 | Mountain council has some building support, but no direct map branch evidence. |
| IUL | 47 | 26 | 16 | 0 | 26 | 0 | 15 | 47 | 2 | League concept needs diplomacy/expansion mechanics beyond helpers. |
| BAC | 47 | 26 | 16 | 0 | 25 | 0 | 18 | 47 | 2 | Settlement-defense concept moderately supported, not overpowered. |
| ARD | 47 | 26 | 16 | 0 | 25 | 0 | 30 | 49 | 2 | Stronger construction count; port-directorate identity can still be more distinctive. |
| NLC | 47 | 29 | 14 | 1 | 22 | 0 | 33 | 70 | 4 | Stronger building count, but late mutual exclusion/pathline risk around polar/extreme endpoints. |
| CFR | 47 | 34 | 30 | 3 | 8 | 0 | 4 | 53 | 24 | Construction concept has good idea guard but too little direct construction in focus file and many route locks/mutexes. |
| OGB | 23 | 17 | 7 | 6 | 10 | 1 | 6 | 17 | 4 | Better annex filters than most short trees, but only 23 focuses for restored-name successor. |
| MFR | 58 | 42 | 38 | 2 | 28 | 2 | 16 | 58 | 0 | Stronger overall, but the four-way route split is hidden via `available` instead of visible mutual exclusions (`factory_successors.txt:1739-1842`). |
| KZR | 16 | 9 | 4 | 5 | 5 | 10 | 8 | 22 | 2 | Very compact; symbolic/expansion fork joins into an annexation-filter charter without direct annex effect at `ancient_restorations.txt:288-294`. |
| SOG | 16 | 9 | 3 | 5 | 5 | 10 | 3 | 21 | 2 | Very compact; weakest ancient industry footprint. Charter pattern at `ancient_restorations.txt:697-703`. |
| KHW | 16 | 10 | 3 | 5 | 5 | 10 | 9 | 21 | 2 | Very compact; water/oasis identity needs deeper infrastructure decisions. Charter pattern at `ancient_restorations.txt:1096-1102`. |
| ALN | 16 | 9 | 2 | 5 | 5 | 13 | 11 | 21 | 2 | Very compact; mountain/pass identity has payload but no real route depth. Charter pattern at `ancient_restorations.txt:1508-1514`. |

## Chaos-Country Priority List

1. `ICD`, `DSC`, `NRF`, `RMC`, `TSC`: these 18-focus chaos trees still read like compact side trees rather than overpowered collapse nightmares. `DSC` has useful aggression now, but the concept still deserves a larger political-dead-army/war-economy/expansion route structure.
2. `PRA`: the rail identity is coherent and the authority idea updater is clean, but 22 focuses is too small for a moving railway authority. It needs deeper rail seizure, corridor taxation, armored train, supply-node, and branch-line decisions.
3. `CFR` and `MFR`: construction/factory successor concepts should be visibly overpowered. CFR relies on helpers while showing only 4 direct building payloads in the focus file; MFR has stronger payloads but uses hidden route exclusion instead of visible mutually-exclusive branches.
4. `KZR`, `SOG`, `KHW`, `ALN`: ancient restorations are only 16 focuses each, with one symbolic-vs-expansion fork and a shared charter. They need distinctive starting ideas, deeper old-name legitimacy mechanics, and route-specific end states.
5. `UDC`, `SDZ`, `BBH`, `GAC`, `BSC`: these 47-focus chaos trees have high helper counts, low direct map/building evidence, and concepts that should create pressure on neighbors, not just internal variable growth.
6. `FTH`, `NLC`, `ARD`, `UWD`, `FEV`, `SZA`: comparatively better payload density, but still need stronger route-specific political/industry/expansion divergence.

## Reward and Branch Depth Findings

### Generic helper-only reward spam

Representative pattern:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt:31-230` (`FTH_birth`, `FTH_first_guard`, `FTH_stores`, `FTH_legitimacy`, `FTH_rival`, `FTH_doctrine`, `FTH_economy`, `FTH_league`, `FTH_foreign`) shows a repeated chain of flags plus `soviet_collapse_apply_*` helpers.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:7771-7905` begins the same generic 47-focus shape for BBH.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2408-2422` (`MFR_unsafe_production_surge`) is flag plus helper only despite industry/stability filters.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2527-2542` (`MFR_gates_sirens_rifles`) includes helper plus two identical bunker construction calls; if level 2 is intended, parent should replace this with one explicit level/value or a named defensive scripted effect.

Impact:

- Parent reviewers cannot see whether the political/industry/expansion branch is actually distinct without jumping into scripted effects.
- The player likely sees many tooltips that feel like small abstract deltas unless custom tooltips are very precise.
- Focus filters become hard to verify because the reward behavior is hidden behind helper names.

### Political / industry / expansion branch depth

Lowest depth offenders:

- Ancient trees (`KZR`, `SOG`, `KHW`, `ALN`): 16 focuses each; one compact opening, one symbolic-vs-expansion fork, one shared charter, two endings.
- Compact custom splinters (`TSC`, `RMC`, `DSC`, `NRF`, `ICD`): 18 focuses each; not enough room for real political, industrial, and expansion branches.
- `PRA`: 22 focuses; rail theme is present but needs route depth.
- `OGB`: 23 focuses; has more annexation flavor, still too small for a chaos successor.

Medium-depth but still generic:

- Most 47-focus custom splinters (`FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`) have better size but use similar branch silhouettes and many helper-only rewards.

## Layout and Pathline Findings

No duplicate focus coordinates were found across the audited focus files.

Remaining risks:

- 457 prerequisite edges are same-row, reversed, or one-row tight edges. Not every one is wrong, but the volume is high enough that pathline readability is still risky.
- `common/national_focus/005_soviet_collapse_republics.txt:2065`: `ukr_soviet_collapse_bread_state_whispers` is on the same row as its prerequisite `ukr_soviet_collapse_breadbasket_empire` (`parent (24,9)`, `child (19,9)`), creating a long horizontal/reversed line.
- `common/national_focus/005_soviet_collapse_republics.txt:7272`: `central_asia_soviet_collapse_the_southern_shield` is on the same row as `central_asia_soviet_collapse_khwarazm_restoration_debate` (`parent (9,8)`, `child (15,8)`).
- `common/national_focus/005_soviet_collapse_factory_successors.txt:1739-1842`: MFR four-way ownership route is hidden by `available` blocks checking `has_completed_focus` rather than visible `mutually_exclusive` links. The player cannot easily read that `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, and `MFR_eternal_arsenal` are exclusive.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:294`, `:703`, `:1102`, `:1514`: ancient charter focuses list both mutually exclusive symbolic and expansion focuses in a single `prerequisite` block. HOI4 treats multiple focuses in one prerequisite block as OR, so this is syntactically valid, but visually it draws both branch lines into one shared join after a fork.
- DSC/ICD shared post-fork gates use OR-style prerequisite joins after mutually exclusive branches; these are semantically valid but can create pathlines through a fork. Parent should inspect around `DSC_grave_ordnance_claims` (`custom_splinters.txt:3007`) and ICD endpoint joins (`custom_splinters.txt:4228-4249`).

## Focus Filter Findings

Hard mismatches:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:288-294`: `KZR_khazar_charter` uses `FOCUS_FILTER_ANNEXATION`, but the visible payload is charter flags, decisions, variables, train equipment, rail, and supply node rather than direct annexation/claims/cores.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:697-703`: `SOG_sogdian_city_charter` uses the same annexation-filter charter pattern.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1096-1102`: `KHW_khwarazmian_water_charter` uses the same annexation-filter charter pattern.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1508-1514`: `ALN_alan_pass_charter` uses the same annexation-filter charter pattern.

Review-needed helper filters:

- `common/national_focus/005_soviet_collapse_factory_successors.txt:2408-2422`: `MFR_unsafe_production_surge` uses industry/stability filters but delegates all real behavior to `soviet_collapse_apply_mfr_focus_warning_lamp_protocol`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2527-2542`: `MFR_gates_sirens_rifles` uses army/stability filters, gives helper plus bunkers; if the helper does not materially change army/stability, filters should be adjusted.
- Many republic/custom-splinter focuses use annexation/political/industry filters while map/building payloads are helper-hidden. Parent should validate filter behavior against scripted-effect bodies before calling this complete.

## Safe Immediate Patches for Parent

These are patch recommendations, not applied here.

1. Convert MFR hidden route locks into explicit `mutually_exclusive` links for the four ownership focuses at `common/national_focus/005_soviet_collapse_factory_successors.txt:1739-1842`. Keep the `available` safety checks if desired, but add visible route lines so the branch reads correctly.
2. Replace duplicate bunker calls in `MFR_gates_sirens_rifles` (`factory_successors.txt:2527-2542`) with either one `level = 2` bunker call if supported by the target behavior, or a named helper that clearly communicates “two defensive levels”.
3. For ancient charter focuses (`ancient_restorations.txt:288`, `:697`, `:1096`, `:1508`), either remove `FOCUS_FILTER_ANNEXATION` or add direct, route-appropriate claim/core/wargoal/annexation payloads. Do not leave annexation filters on logistics/charter rewards.
4. Split ancient charter joins into route-specific continuation focuses or add clearer visible route gating. The current single prerequisite block after a mutually exclusive fork is legal, but it is pathline-hostile.
5. Add starting or staged idea carriers for KZR/SOG/KHW/ALN setup in `common/scripted_effects/005_soviet_collapse_effects.txt` near the ancient setup block. Use guarded add/swap behavior like PRA/CFR, not raw repeated `add_ideas`.
6. Expand the 18-focus chaos trees before tuning numbers. `ICD`, `DSC`, `NRF`, `RMC`, and `TSC` need more branch nodes, not just stronger helper constants.
7. For the 47-focus generic chaos countries, replace repeated “flag plus helper” focus rewards with a visible mix of decisions, claims/cores, building targets, unit templates, railway/supply construction, timed missions, and staged idea swaps.
8. For all helper-only rewards, ensure each custom tooltip names the actual player-facing change. Avoid tooltip text that only describes abstract “authority”, “mandate”, or “pressure” when the effect is factories, rails, claims, or units.
9. Run a focus-filter audit after helper edits: every `FOCUS_FILTER_INDUSTRY` focus should visibly or tooltip-explicitly affect construction, factories, resources, research, production, or infrastructure; every `FOCUS_FILTER_ANNEXATION` focus should affect claims, cores, wargoals, annexation decisions, subjects, or territorial integration.
10. Re-run pathline coordinate audit after route expansion, especially same-row/reversed edges and OR-joins after mutually exclusive forks.

## Validation Commands Used / Recommended

Read-only inspection:

```bash
sed -n '1,520p' .agents/skills/hoi4-focus-trees/SKILL.md
sed -n '1,260p' .agents/skills/chaos-redux-subagents/SKILL.md
sed -n '1,160p' "paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Effect - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/On actions - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md"
rg -n "add_ideas|swap_ideas|remove_ideas|add_timed_idea" common/scripted_effects/005_soviet_collapse_effects.txt common/decisions/005_soviet_collapse_decisions.txt common/national_focus/005_soviet_collapse_*.txt
rg -n "id = MFR_(officers_chair_the_board|armorers_elect_delegates|merchants_of_ammunition|eternal_arsenal)|has_completed_focus = MFR_" common/national_focus/005_soviet_collapse_factory_successors.txt
rg -n "id = (KZR_khazar_charter|SOG_sogdian_city_charter|KHW_khwarazmian_water_charter|ALN_alan_pass_charter)|FOCUS_FILTER_ANNEXATION" common/national_focus/005_soviet_collapse_ancient_restorations.txt
wc -l common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt common/ideas/005_soviet_collapse_ideas.txt common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/decisions/005_soviet_collapse_decisions.txt localisation/english/005_soviet_collapse*.yml
git status --short
```

Parser checks performed with inline Python:

- Focus-tree count per `focus_tree = { ... }`.
- Focus coordinate duplicate detection.
- Prerequisite edge spacing detection for same-row/reversed/one-step edges.
- Per-tree counts for `search_filters`, direct map effects, direct building effects, helper calls, and mutual-exclusion entries.

Recommended parent follow-up parser checks:

```bash
python3 - <<'PY'
from pathlib import Path
for p in [
    Path("common/national_focus/005_soviet_collapse_republics.txt"),
    Path("common/national_focus/005_soviet_collapse_custom_splinters.txt"),
    Path("common/national_focus/005_soviet_collapse_factory_successors.txt"),
    Path("common/national_focus/005_soviet_collapse_ancient_restorations.txt"),
]:
    text = p.read_text()
    print(p, text.count("focus = {"), text.count("mutually_exclusive = {"), text.count("add_ideas ="))
PY
```

## Completion / Simplification Note

This was a read-only audit. No gameplay, script, localisation, interface, or asset files were edited. No simplification was used in the audit scope; the main limitation is that helper reward behavior was sampled and mechanically searched, not fully hand-expanded for every one of the hundreds of helper calls. The safest parent next step is a focused patch tranche for MFR route visibility, ancient charter filters/pathlines, and the 18-focus chaos-country depth gap.
