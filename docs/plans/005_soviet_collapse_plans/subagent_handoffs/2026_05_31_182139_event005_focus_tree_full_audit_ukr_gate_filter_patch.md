# Event005 Soviet Collapse focus tree audit handoff

Timestamp: 2026-05-31 18:21:39 UTC

Role: Chaos Redux focus-tree auditor

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Hard exclusions honored:
- No `gfx/flags` or flag sprite changes.
- No Event006 edits.
- No broad generated rewrite.

## Patch Summary

Files changed by this audit:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_182139_event005_focus_tree_full_audit_ukr_gate_filter_patch.md`

Changed focus ids:
- `ukr_soviet_collapse_peasant_socialist_congress`
- `SOG_scholar_envoy_rooms`

Localisation keys changed:
- None.

Icon ids changed:
- None.

Route behavior before and after:
- `ukr_soviet_collapse_peasant_socialist_congress`
	- Before: the socialist peasant congress focus had a route prerequisite on `ukr_soviet_collapse_socialist_republic_without_moscow` but an additional `available` gate requiring `ukr_soviet_collapse_german_liaison_question`, forcing a socialist internal branch to cross through an unrelated German liaison focus.
	- After: the unrelated `available` gate is removed. The focus now follows its socialist route prerequisite cleanly.
- `SOG_scholar_envoy_rooms`
	- Before: the focus had `FOCUS_FILTER_POLITICAL` but granted an industry `add_tech_bonus`.
	- After: the focus keeps `FOCUS_FILTER_POLITICAL` and adds `FOCUS_FILTER_RESEARCH`.

## Validation Run

Commands/checks run:
- Read required offline wiki pages before inspection:
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
	- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
	- `paradox_wiki/AI focuses - Hearts of Iron 4 Wiki.md`
- Read vanilla documentation and precedents:
	- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
	- vanilla focus files including `common/national_focus/baltic_shared.txt`, `common/national_focus/soviet.txt`, and `common/national_focus/uk.txt`
- Parsed 1698 focus blocks across the four scoped files.
- Checked duplicate direct `add_ideas` rewards inside one focus: none found.
- Checked parsed focuses for missing icon, `completion_reward`, and `ai_will_do`: none found.
- Checked focus id localisation names/descriptions across `localisation/english`: 0 missing keys found.
- Checked unsupported operators `<=` and `>=` in scoped focus files: none found.
- Checked brace balance in scoped focus files with `python3`: all ended at depth 0 with no negative depth. Counts were republics 501, custom splinters 1005, factory successors 128, ancient restorations 64.
- Checked exact duplicate coordinates after patch: none found.
- Checked scoped `gfx/flags` diff: no files changed.

Skipped validation:
- A first attempt to run the brace helper with `python` failed because `python` is not installed on PATH; the same check passed with `python3`.
- No in-game load test was run from this subagent pass.
- No broad route simulation was run; this handoff is a static script and route-structure audit.
- No full localisation encoding rewrite was attempted because the task scope was focus-tree audit and the parsed localisation keys were present.

## Route Coverage Table

| Tree or group | Implemented route coverage | Audit result | Priority |
| --- | --- | --- | --- |
| Ukraine, `soviet_collapse_ukraine_focus_tree` | 83 focuses. Political, rural/socialist, German liaison, state-building, army, industry, expansion, and endgame content exist. | Broad coverage exists but the layout remains cramped and route readability is poor. Several same-row near-adjacent focuses make pathlines look tangled. One unrelated socialist/German route gate was patched. Ukraine still needs a layout pass and stronger branch identity. | High |
| Belarus, `soviet_collapse_belarus_focus_tree` | 53 focuses. Minsk legitimacy, security, industry, foreign aid, military, and expansion content exist. | Better coverage than the shallow stubs, but at least one same-row close pair remains and the branch payoffs read generic in places. Needs clearer split between national council, border defense, and opportunist expansion. | Medium |
| Kazakhstan, `soviet_collapse_kazakhstan_focus_tree` | 92 focuses. Deepest republic successor tree with political, industry, rail, steppe, army, and expansion arcs. | Quantity is strong, but many rewards are helper-heavy and need a manual pass for branch payoff clarity and decision/mechanic visibility. | Medium |
| Moldova, `soviet_collapse_moldova_focus_tree` | 48 focuses. Corridor, river, security, industry, and expansion arcs exist. | Coverage is acceptable but several icon and reward patterns repeat. Needs route payoff contrast and stronger mechanic hooks for corridor and border wars. | Medium |
| Baltic/Caucasus/Central Asia shared trees | 40 to 45 focuses. Regional political, defense, economy, and expansion arcs exist. | Functional medium-depth scaffolds. Still rely on generic defensive construction, stability, and army rewards. Need stronger regional mechanics and fewer interchangeable payoff focuses. | Medium |
| Internal republic and breakaway shared trees | 62 and 36 focuses. Survival, autonomy, radio/security, industry, and armed neutrality arcs exist. | Internal republic coverage is acceptable; breakaway is shallow. Breakaway route needs a purpose beyond survival bonuses and a clearer path into aggression, federation, or hard neutrality. | High |
| Custom splinters, 47-focus group | Most custom splinters have 47 focuses with political, industry, military, foreign, and expansion labels. | The trees are present but often feel scaffolded. Many identity routes use similar reward cadence and icon families. Need hand-authored payoff replacements and decision links by country identity. | High |
| Crisis splinters, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` | 18 focuses each. | Too shallow for the user's requested chaos-country identity. `DSC` especially needs recruitable population, congress/dead-state identity, cores/claims/war goals, and stronger OP payoff. | Critical |
| `PRA_soviet_collapse_focus_tree` | 22 focuses. | Shallow and unlikely to satisfy chaos-country strength requirements. Needs a real identity branch and major payoff chain. | High |
| `CFR_soviet_collapse_focus_tree` | 47 focuses. | Closest to the requested factory-directorate fantasy. Construction/factory/rail/supply identity is visible. Still needs review for OP scaling, route-exclusive payoffs, and decision hooks. | Medium |
| `MFR_soviet_collapse_focus_tree` | 58 focuses. | Stronger arsenal and worker-factory identity than most splinters. Needs clearer final route payoffs and mechanic links so the arsenal branch is not just factories plus army bonuses. | Medium |
| `OGB_soviet_collapse_focus_tree` | 23 focuses. | Too shallow for an identity-driven chaos successor. Needs a proper political/industry/expansion/military split and final payoff. | High |
| Ancient restorations, `KZR`, `SOG`, `KHW`, `ALN` | 16 focuses each. | All four are compact stubs. They have symbolic-state, old-route, guard, charter, expansion, and survival concepts, but not enough depth or bespoke mechanics. One filter mismatch was patched for `SOG_scholar_envoy_rooms`. | Critical |

## Missing Or Simplified Content

High-priority gaps:
- `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`: each needs expansion from 18-focus survival stubs into distinct political, industry, military, expansion, and identity branches. Do not bulk-generate; write country-specific route families.
- `DSC_soviet_collapse_focus_tree`: the dead congress concept should receive recruitable population, legitimacy-through-dead-records flavor, manpower mobilization, and aggressive neighbor claims/war goals. Current depth is not enough for the user requirement.
- `OGB_soviet_collapse_focus_tree`: add a real identity-driven route family. Current 23-focus depth is not enough for an OP chaos-country branch.
- Ancient `KZR`, `SOG`, `KHW`, `ALN`: expand from 16 focuses to proper branch sets. Recommended branches: restoration legitimacy, modern administrative survival, caravan/water/pass economy, relic-guard or warrior military, neighbor claim/core aggression, and a final survival/empire payoff.
- Ukraine layout: same-row close pairs and remaining route crossings need a hand layout pass. Priority focus ids:
	- `ukr_soviet_collapse_peasant_socialist_congress` at x15 y7 and `ukr_soviet_collapse_coalition_of_three_ministries` at x16 y7.
	- `ukr_soviet_collapse_rural_deputy_bloc` at x16 y8 and `ukr_soviet_collapse_workers_congress_in_kharkiv` at x17 y8.
	- `ukr_soviet_collapse_re_register_the_party` at x19 y10 and `ukr_soviet_collapse_black_soil_oath` at x20 y10.
- Belarus layout: `blr_soviet_collapse_foreign_aid_through_brest` at x6 y5 and `blr_soviet_collapse_national_council_of_minsk` at x7 y5 are too close on the same row.
- Custom splinters: several 47-focus trees are structurally present but still read as variants of the same generic template. Route recommendations should replace generic rewards with country-specific hooks, not add more ideas.

Reward-pattern gaps:
- Generic train/truck/AA/factory/construction rewards are still common and often lack route meaning. Replace selected repeated generic payoffs with existing mechanic hooks where present: decision unlock tooltips, targeted claims, cores, war goals, construction directorate scripted effects, arsenal procurement effects, border-war hooks, recruitable population, and route-specific national spirits.
- Do not add more flat national spirits as the default fix. The user's complaint is idea spam. Prefer route mechanics, state-scoped effects, decisions, claims/cores, building projects, and one final route-defining idea when needed.
- For factory and construction directorates, emphasize large factory, rail, infrastructure, supply hub, and production-line payoffs. `CFR` is closest; copy its design direction, not its exact focus ids, into weaker chaos factory states.

## Icon Coverage Table

| Icon issue | Affected ids or group | Recommendation |
| --- | --- | --- |
| Reused Ukraine democratic icon | `GFX_ukr_soviet_collapse_democratic` on `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_coalition_of_three_ministries`, `ukr_soviet_collapse_republic_of_laws`, `ukr_soviet_collapse_civilian_command_over_the_army` | Assign distinct existing icons or register unique stable icon ids. Do not touch flag sprites. |
| Reused radio/security icon | `GFX_focus_soviet_collapse_guard_the_radio_stations` on `ukr_soviet_collapse_guard_the_telegraph_house`, `soviet_collapse_guard_the_radio_stations`, `soviet_collapse_neutrality_under_pressure`, `internal_soviet_collapse_secure_autonomous_capital` | Split route-specific security, neutrality, and radio icons. |
| Ancient generic icons reused across all four ancient trees | `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_restoration_survives`, `GFX_focus_soviet_collapse_ancient_returned_names_endgame`, `GFX_focus_soviet_collapse_ancient_symbolic_state`, `GFX_focus_soviet_collapse_ancient_workshop_compact` | Acceptable as temporary scaffold, but not final. Each ancient restoration should receive identity-specific route icons. |
| Reused Moldova corridor icon | `GFX_moldova_soviet_collapse_ukrainian_corridor` appears on four focuses | Split corridor diplomacy, corridor military, and corridor economy icons. |
| Reused Central Asia rail/irrigation icon | `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` appears on four focuses | Split rail, irrigation, logistics, and administrative economy icons. |
| Custom splinter repeated generic families | Multiple custom splinter focuses in 47-focus trees, including repeated diplomatic, supply, war, civil, and foreign-plan icon families | During route deepening, assign one icon family per route purpose and avoid using the same sprite for every phase of a branch. |

## Localisation And Reward Mismatch List

No missing focus name or description localisation keys were found in `localisation/english` for parsed focus ids.

Mismatch and review candidates:
- `SOG_scholar_envoy_rooms`: search filter mismatch was patched by adding `FOCUS_FILTER_RESEARCH`.
- Building-only or building-heavy military focuses often omit `FOCUS_FILTER_INDUSTRY`. Some are legitimate military/fortification focuses, so bulk patching would be unsafe. Manual review candidates include:
	- `ukr_soviet_collapse_first_republican_line`
	- `soviet_collapse_military_defense_council`
	- multiple internal republic, Baltic, Caucasus, Central Asia, custom splinter, and ancient defense or route-building focuses.
- Focus names that imply route-defining political decisions but only grant small generic rewards should be reviewed first in shallow trees:
	- `DSC`, `TSC`, `RMC`, `NRF`, `ICD` 18-focus groups.
	- ancient `*_symbolic_state`, `*_ancient_league_bargain`, `*_restoration_survives`, and `*_returned_names_endgame` family.
	- `OGB_soviet_collapse_focus_tree` payoff focuses.

Direct duplicate idea rewards:
- None found from direct `add_ideas` parsing inside individual focuses.
- No direct focus-level repeated `add_ideas` ids were found by the parser.
- Remaining idea-spam risk is likely inside scripted helper calls, route-generated ideas, or repeated route-spirit upgrades. Audit helper effects before adding more spirits.

## AI Behavior Gaps

Observed:
- Every parsed focus has an `ai_will_do` block.
- Several trees use route-aware AI gates, but many shallow and scaffolded trees still have generic weights that do not express strong country identity.

Gaps:
- Chaos countries need route-aware preference for their identity branch. Examples:
	- Factory directorates should strongly prefer construction, factory, rail, and supply payoffs before optional foreign politics.
	- `DSC` should prefer manpower/congress-mobilization and aggressive recovery routes.
	- Ancient restorations should prefer their restoration legitimacy and old-border aggression routes when high-chaos conditions exist.
- Expansion, core, claim, and war-goal branches need AI constraints so countries do not fire suicidal aggression early but still become threatening once stabilized.
- Ukraine AI should avoid crossing or unrelated route gates. The patched `ukr_soviet_collapse_peasant_socialist_congress` gate removes one obvious issue, but a full AI route pass is still needed after layout cleanup.

## Mutual Exclusion And Pathline Risks

Narrow issue patched:
- `ukr_soviet_collapse_peasant_socialist_congress` no longer requires `ukr_soviet_collapse_german_liaison_question`.

Remaining review risks:
- Many single `prerequisite = { focus = a focus = b }` blocks act as OR prerequisites. Some are intentional convergence points, but they can make routes visually cross or feel overlapping if not paired with clear route locks.
- High-risk manual review examples:
	- Ukraine: `ukr_soviet_collapse_free_soil_compromise`, `ukr_soviet_collapse_last_harvest_plan`.
	- Breakaway: `soviet_collapse_stabilize_food_and_currency`, `soviet_collapse_rail_hub_or_mountain_pass`, `soviet_collapse_armed_neutrality`.
	- Factory successors: several `CFR_*`, `MFR_*`, and `OGB_*` OR-convergence points.
	- Ancient restorations: `KZR_khazar_charter`, `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, `ALN_alan_pass_charter`.

Recommendation:
- Do not convert every OR prerequisite into AND. Vanilla focus trees use OR groups heavily. Instead, map each route visually, then add or adjust route-lock `available` blocks, mutual exclusions, or x/y placement only where the route meaning is ambiguous.

## Focus-To-Decision And Mechanic Links

Current concern:
- Several trees look like they grant isolated one-time rewards rather than unlocking or escalating mechanics.

Implementation recommendations:
- Before adding new decisions, inspect existing Event005 decision categories and scripted helpers for reusable hooks.
- Prefer narrow focus rewards that unlock existing decisions or call existing scripted effects over adding another flat idea.
- Add route payoffs where the focus name promises a system:
	- Factory/directorate states: construction mandates, regional build projects, supply/rail repair missions, procurement decisions.
	- Dead congress and other crisis states: recruitable population, emergency legitimacy, war-goal/claim packets, and mobilization decisions.
	- Ukraine: democratic, socialist, rural, German-liaison, army, and black-soil routes should each have a distinct decision or mechanic hook.
	- Ancient restorations: old-border claim/core decisions, caravan/water/pass projects, restoration legitimacy, and controlled neighbor aggression.

## Existing Plan Handoff Path

Related existing broad redesign plan:
- `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`

This audit should be treated as an update and prioritization layer on top of that plan. The broad route redesign work should be merged into the source spec or queued explicitly by the parent before implementation.

## Priority List For Parent

1. Expand or redesign the 18-focus crisis splinter trees, especially `DSC`, into real identity-driven chaos countries.
2. Expand ancient restorations from 16-focus stubs into route families with restoration legitimacy, economy, military, aggression, and endgame payoff.
3. Fix Ukraine layout and remaining route-path readability; the unrelated socialist/German gate is patched, but spacing and OR-convergence still need a hand pass.
4. Replace generic repeated rewards with route mechanics and decision hooks, not more flat ideas.
5. Review icon reuse after branch redesign, registering stable non-flag icons where needed.
6. Add route-aware AI behavior for OP chaos countries so identity branches are actually chosen.

## Remaining Route Risks

- The scoped tree files were already dirty before this audit. This handoff lists only the narrow edits made by this auditor; other diffs in the same files may be pre-existing parent work.
- No broad rewrite was attempted because the user explicitly requested audit plus narrow safe patches.
- The audit found no direct duplicate `add_ideas` in focus rewards, so the reported idea spam likely sits in scripted helpers or repeated upgrade patterns outside direct focus reward parsing.
- Static validation passed, but live-game route behavior still needs parent validation after the broader route redesign.
