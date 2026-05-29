# Soviet Collapse Focus Subagent Duplicate Reward, CFR, and DSC Patch

Date: 2026-05-29  
Subagent: Chaos Redux focus-tree subagent  
Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

## References Used

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla/reference precedent: focus `ai_will_do`, `create_wargoal`, scoped `add_ai_strategy`, focus search filters, and state construction rewards.

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Removed five-focus updater duplication pattern from four republic focuses by moving variable changes before existing updater helpers or inlining only the high-chaos variable/pressure payload. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Removed duplicated KRS staged-idea updater; made `DSC_armies_that_do_not_demobilize` an earlier aggressive-neighbor war-plan focus. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | Strengthened `CFR_factories_first` with extra offsite civilian industry. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_subagent_duplicate_reward_cfr_dsc_patch.md` | This handoff. |

## Changed Focus IDs

| Focus id | Before | After |
| --- | --- | --- |
| `ukr_soviet_collapse_the_ukrainian_commune_debate` | Called both `soviet_collapse_apply_focus_socialist_sovereignty` and `soviet_collapse_apply_focus_high_chaos_identity`, causing two staged-idea refreshes. | Keeps high-chaos recognition, local-authority, and Soviet old-movement pressure inline, then lets the socialist helper perform the single refresh. |
| `central_asia_soviet_collapse_khwarazm_restoration_debate` | Called high-chaos and legal helpers, then forced another direct staged-idea refresh after claims. | Moves local-authority pressure before helpers and removes the direct updater; state claims remain. |
| `moldova_soviet_collapse_smugglers_and_border_committees` | Called high-chaos/depot helpers, added route pressure, then forced another direct updater. | Applies route pressure before helper refreshes and removes the direct updater. |
| `kaz_soviet_collapse_red_nomad_committees` | Called socialist helper, then added variables, then forced another direct updater. | Adds variables before the socialist helper and removes the direct updater. |
| `KRS_inner_faction` | Called custom-splinter inner-faction helper, then added variables, then forced another direct updater. | Adds variables before the helper and removes the direct updater. |
| `CFR_factories_first` | Civilian-build helper plus one state civilian factory. | Adds offsite industrial complexes using the existing factory-successor mandate constant. |
| `DSC_armies_that_do_not_demobilize` | Claimed/cored two road/front states and pressured Soviet obedience, but did not yet create neighbor war goals. | Adds annexation filter, hidden non-allied neighbor war goals, hidden conquer/antagonize AI against those neighbors, and assault columns. |

## Route Coverage Table

| Required route/content area | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Republic political branches | Ukraine, Belarus, Kazakhstan, Baltic, Caucasus, Central Asia, Moldova, internal republic, generic breakaway branches. | Partial | Real branches exist, but many still pay off through shared staged-idea helpers. This patch only removed exact updater duplication. |
| Republic industry branches | Multiple republic construction/depot/rail branches. | Partial | Still needs more decision-backed industry programs and fewer one-off factory/AA/truck rewards. |
| Republic expansion branches | Ukraine, Kazakhstan, Central Asia, Baltic, Caucasus, Moldova and internal republic expansion hooks. | Partial | Claims exist in places, but postwar integration and AI target behavior remain thin. |
| High-chaos custom splinters | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`. | Partial | Full shells exist, but many middle branches remain templated and helper-heavy. |
| Shallow crisis splinters | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`. | Partial/Fail | Prior endpoint aggression exists. This pass strengthens DSC mid-end aggression, but all six still need full fixed-purpose branch depth. |
| Factory successors | `CFR`, `MFR`, `OGB`. | Partial | CFR civilian industry is stronger after this patch; MFR is the strongest factory tree; OGB remains too shallow. |

## Duplicate Idea / Updater Spam Audit

Direct `add_ideas` and `swap_ideas` in the three scoped focus files: none found.

Exact duplicate staged-idea updater cases patched:

- `ukr_soviet_collapse_the_ukrainian_commune_debate`
- `central_asia_soviet_collapse_khwarazm_restoration_debate`
- `moldova_soviet_collapse_smugglers_and_border_committees`
- `kaz_soviet_collapse_red_nomad_committees`
- `KRS_inner_faction`

Remaining design-level spam risk:

- Full custom splinter trees still use repeated route identity helpers across adjacent focuses.
- Many republic focuses still use direct staged updater helpers as their main reward, even when not duplicated in the same focus.
- Broad helper consolidation belongs to a parent scripted-system pass, not a bounded focus patch.

## Shallow Reward Clusters

| Cluster | Exact examples | Recommendation |
| --- | --- | --- |
| Small trucks/trains/convoys/support rewards | `moldova_soviet_collapse_smugglers_and_border_committees`, `ARD_*convoy*`, `IUL_rail_and_river_patrols`, `NLC_ice_port_tolls`, `NRF_ghost_convoy_escorts`. | Replace with decision unlocks, route missions, depot/rail authority changes, target claims, or state projects. |
| One-off factory/AA/infrastructure rewards | Many full custom splinter middle branches, plus compact republic industry lanes. | Keep as supporting rewards only; pair them with route variables, decisions, or state-specific strategic goals. |
| Repeated identity-helper cadence | Most 47-focus custom splinters. | Consolidate refreshes at route milestones and add tag-specific mechanics. |
| Short crisis trees | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`. | Needs full branch redesign; small patches cannot make these complete. |

## Pathline / Layout Audit

Current mechanical parser results across the scoped files:

- Duplicate same-tree focus coordinates: none found.
- Straight same-row/same-column prerequisite blockers: none found.
- Focuses sitting directly between mutually exclusive endpoints: none found.
- Continuous focus panels are to the right in current files; no parser-detectable overlap found.

Manual layout risks still needing screenshot review:

- Ukraine is very wide and deep; it likely needs an in-game pathline readability pass even though exact blockers were not found.
- Belarus has compact route families around corridor/forest/foreign branches and needs in-game pathline review after any future movement.
- Curved engine pathlines and focus-box hover overlap cannot be proven by text parsing alone.

## Chaos-Country Concepts And Missing OP Mechanics

| Tree | Concept | Still lacks for overpowered identity |
| --- | --- | --- |
| `CFR` | Civilian Factory / Construction Directorate | More recurring civilian construction decisions, map-wide reconstruction contracts, client-city integration, and construction AI. Patched `CFR_factories_first` adds heavier civ industry. |
| `MFR` | Military Factory / Arsenal Directorate | Stronger than others; still needs postwar arms-client integration and target-specific attack AI beyond endpoints. |
| `OGB` | Old Great Bulgaria / Volga restoration | Too short; needs politics, restoration economy, Idel-Ural settlement, war/postwar integration. |
| `FTH` | Free Territory / black-banner communes | Needs commune logistics, raider governance, and borderless expansion mechanics beyond generic helper cadence. |
| `PRA` | Railway authority / armored-train corridor | Needs full railway military, toll economy, junction conquest, and integration decisions. |
| `TSC` | Tunguska/starfall observatory state | Needs anomaly/science mechanic, impact-zone claims, air/radar escalation, and hostile perimeter behavior. |
| `RMC` | Resurrection/martyr communes | Needs cult governance, shrine economy, dead-volunteer recruitment loop, and aggressive burial-road postwar handling. |
| `DSC` | Dead Soldiers' Congress | Needs a full dead-army command/economy branch; this patch adds earlier neighbor war goals and assault columns. |
| `NRF` | Northern revenant fleet | Needs convoy raiding, port-control decisions, naval invasions, and White Sea/North Sea expansion mechanics. |
| `ICD` | Iron/immortal commissariat | Needs commissar terror administration, memorial recruitment, front claims, and cleanup/aftermath. |
| `BSC` | Siberian/Baikal successor | Needs bespoke Siberian resource and frontier-expansion mechanics. |
| `TNC` | Trans-Caspian / transit authority | Needs stronger transit tolls, Caspian claims, and sponsor conflict hooks. |
| `ALA` | Alash / steppe national restoration | Needs Alash-specific courts, steppe integration, Kazakh claims/cores, and cavalry expansion AI. |
| `BBH` | Black Banner Host / anarchist raiders | Needs non-domination pact decisions, raider supply loops, and hostile anti-state expansion. |
| `KRS` | Kronstadt/Red sailor council | Needs naval-port mechanics and Baltic/Gulf aggression beyond generic identity helpers. |
| `UDC` | Union Defense Command | Needs command-network annexation, emergency laws, and target-specific Soviet successor war plans. |
| `SDZ` | Security Directorate zone | Needs archive/security mechanics, purge/occupation decisions, and hostile intelligence branch. |
| `GAC` | Green Army communes | Needs peasant land-control mechanics, forest partisan decisions, and anti-urban expansion. |
| `DHC` | Don Host/Cossack authority | Needs host-law mechanics, cavalry raid decisions, and Don/Kuban settlement branches. |
| `KHC` | Kuban Host/Cossack authority | Needs Kuban-specific host economy, Black Sea road claims, and Cossack integration. |
| `FEV` | Far Eastern Vladivostok authority | Needs Pacific sponsor conflict, port/naval economy, and Siberian/Far East expansion targets. |
| `SZA` | Siberian Zemstvo authority | Needs zemstvo elections, Siberian city federation mechanics, and trans-Siberian expansion. |
| `UWD` | Ural Workers Directorate | Needs worker/factory seizure decisions, railbelt conquest, and industrial mobilization AI. |
| `MRC` | Mountain Republic / Caucasus pass state | Needs pass-control missions, mountain war goals, and postwar integration. |
| `IUL` | Idel-Ural federation | Needs Volga federal settlement, oil/river economy, and OGB/neighbor conflict decisions. |
| `BAC` | Birobidzhan/Amur commune | Needs refuge/archive politics, Amur border control, and Far Eastern diplomacy/expansion. |
| `ARD` | Arctic Directorate / northern ports | Needs Arctic convoy/port economy, Murmansk/Kola expansion, and naval AI. |
| `NLC` | Northern Lights / polar station commune | Needs polar logistics, weather/science mechanics, and northern route control. |

## Icon Coverage Table

| Surface | Status | Notes |
| --- | --- | --- |
| All scoped focus blocks | Pass | Every parsed focus has an `icon = ...`. |
| Interface sprite resolution | Pass | No missing focus icon references found in current scoped files. |
| Icons changed by this patch | None | No `.gfx` or icon ids changed. |
| Repeated icon risks | Partial | Repeated icons remain in `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, central Asia, Moldova, internal republic, and Ukraine. These need asset work or icon reassignment. |

## Localisation And Reward Mismatches

- No focus ids were renamed.
- No localisation keys were changed.
- Existing localisation remains present for all changed focus ids.
- `CFR_factories_first` reward now better matches its civilian-factory-first text.
- `DSC_armies_that_do_not_demobilize` reward now better matches its dead-army escalation text.
- Remaining mismatch: many focus descriptions still promise institutional transformation while the reward is a helper refresh plus small stat or equipment reward.

## AI Behavior Gaps

Fixed:

- `DSC_armies_that_do_not_demobilize` now grants hidden conquer/antagonize AI against valid non-allied neighbors.

Remaining:

- Custom splinters need tag-specific AI strategy plans, not only focus-local `ai_will_do`.
- Ukraine/Belarus/Kazakhstan still have many flat `ai_will_do` blocks.
- High-chaos branches mostly delay attack behavior to late focuses.
- Postwar behavior after war goals remains underdesigned.

## Validation Run

- Brace balance on all three scoped focus files: final depth 0, no early closes.
- Unsupported operator check on all three scoped focus files: no `<=` or `>=`.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`: passed.
- Duplicate updater scan for focus blocks containing direct updater plus updater helper, or high-chaos plus socialist helper: no remaining hits.
- Icon reference scan across scoped files and `interface/*.gfx`: no missing icon refs.

## Skipped Validation

- No HOI4 launch or in-game screenshot pass was run.
- No full mod-wide validator was run because the parent worktree is already dirty with many Soviet Collapse changes.
- No localisation BOM check was needed for this patch because no localisation files were edited.
- No Git commit was created because this is a subagent handoff in an actively dirty parent worktree.

## Remaining Full-Rework Requirements

1. Redesign shallow crisis trees (`PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`) into real fixed-purpose trees with politics, economy, military, expansion, and endgame depth.
2. Expand `OGB` into a full restoration tree.
3. Replace repeated helper cadence in 47-focus custom splinter trees with tag-specific mechanics and fewer staged-idea refreshes.
4. Add decision and mission integration for republic and chaos-country industry, expansion, postwar integration, and recognition routes.
5. Add tag-specific AI strategy plans for custom splinter aggression and expansion timing.
6. Run an in-game layout screenshot pass for Ukraine and Belarus before final completion claims.
