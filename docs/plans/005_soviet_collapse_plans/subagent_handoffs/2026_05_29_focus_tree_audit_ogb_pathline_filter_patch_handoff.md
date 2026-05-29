# Soviet Collapse Focus Tree Audit and OGB Pathline/Filter Patch Handoff

Date: 2026-05-29
Subagent: Chaos Redux focus-tree audit/patch
Scope: `common/national_focus/005_soviet_collapse_republics.txt`, `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt`, and matching localisation. No scripted effects were edited because the parent is actively patching Soviet Collapse release/scenario/systems files.

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_tree_audit_ogb_pathline_filter_patch_handoff.md`

## Changed Focus IDs

| Focus id | Change |
| --- | --- |
| `CFR_ration_cards_for_workers` | Added `FOCUS_FILTER_MANPOWER` because the reward grants manpower. |
| `OGB_reopen_volga_trade_tolls` | Reanchored visible prerequisite line to the shared council parent while preserving the route gate requiring either charter-guardian focus. |
| `OGB_friday_schools_and_court_records` | Reanchored visible prerequisite line to the shared council parent while preserving the route gate requiring either charter-guardian focus. |
| `OGB_raise_the_heritage_guard` | Reanchored visible prerequisite line to the shared council parent while preserving the route gate requiring either charter-guardian focus. |
| `OGB_treat_with_idel_ural` | Reanchored visible prerequisite line to the shared council parent while preserving the route gate requiring either charter-guardian focus. |
| `OGB_the_volga_cannot_have_two_seals` | Reanchored visible prerequisite line to the shared council parent while preserving the route gate requiring either charter-guardian focus. |
| `OGB_claim_the_old_trade_cities` | Added `FOCUS_FILTER_ANNEXATION` and direct state claims for Ulyanovsk, Samara, and Ufa to match the focus name and description. |
| `MFR_repair_the_tank_lines` | Added `FOCUS_FILTER_RESEARCH` because the reward grants an armor research bonus. |
| `MFR_aircraft_parts_in_secret_workshops` | Added `FOCUS_FILTER_AIR_XP` because the reward grants air XP. |

No localisation keys or icon ids were changed.

## Route Behavior Before and After

| Area | Before | After |
| --- | --- | --- |
| OGB shared follow-up linework | Several shared follow-up focuses drew visible pathlines from mutually exclusive sibling focuses, making the branch read as if both exclusive children fed the same line directly. | Shared follow-up focuses now draw from `OGB_the_council_takes_the_seal`; `available` still requires either `OGB_scholars_guard_the_charter` or `OGB_clerics_guard_the_charter`, so route gating is unchanged while pathlines are cleaner. |
| OGB trade-city expansion | `OGB_claim_the_old_trade_cities` described old trade-city claims but only adjusted variables and pressure. | Focus now grants local claims on Ulyanovsk, Samara, and Ufa and has an annexation filter. |
| CFR/MFR reward filters | Some filters omitted the actual reward class. | Manpower, research, and air XP filters now match the affected focus rewards. |

## Route Coverage Table

| Tree or route family | Current coverage | Status | Remaining work |
| --- | --- | --- | --- |
| Ukraine republic tree | 83 focuses covering emergency rule, democratic/socialist/military politics, grain, Dnieper industry, Black Sea, foreign policy, League/Black Banner, and high-chaos Bread State content. | Partial but substantial | Needs final reward-variety pass, icon uniqueness pass, and proof that late route payoffs are distinct instead of helper-updater idea stacking. |
| Kazakhstan republic tree | 92 focuses with steppe politics, Alash/socialist/military routes, resources, southern cascade, Central Asian League, Basmachi pressure, and foreign/industry branches. | Strongest major republic coverage | Needs route-aware AI behavior review, repeated icon cleanup, and direct reward variety audit across large route endings. |
| Belarus and Moldova republic trees | Belarus has 53 focuses and Moldova has 48 focuses with political, industry, border, and diplomacy/expansion elements. | Partial | Need deeper late-game political payoffs and clearer special mechanics beyond consolidation helpers. |
| Baltic, Caucasus, Central Asia shared republic trees | 40 to 45 focuses each with regional politics, industry, security, and diplomacy/expansion surfaces. | Partial | Need per-country lore distinction and less shared generic route feel. |
| Internal republic and breakaway templates | 62 and 36 focuses respectively. | Partial | Need route-specific special mechanics and stronger expansion/diplomacy outcomes. |
| Full custom splinters | Most full custom splinters sit near 47 focuses each. | Partial | Better than the compact trees but still depend heavily on helper identity ideas and repeated route scaffolds. |
| Compact crisis splinters | PRA has 22 focuses; TSC, RMC, DSC, NRF, and ICD have 18 each. | Shallow | Need real political, industry, military, expansion, and special-mechanic branches. These still read as compact placeholders. |
| Factory successors | CFR has 47, MFR has 58, OGB has 23. | Mixed | CFR/MFR have workable structure; OGB remains shallow and needs a real full route family after this local cleanup. |
| Ancient restorations | KZR, SOG, KHW, and ALN each have 16 focuses. | Shallow | Need full lore-matching political, industrial, military, expansion, diplomacy, and endgame branches. |

## Missing or Simplified Content

| Priority | Issue | Evidence | Recommended owner action |
| --- | --- | --- | --- |
| High | Helper-call idea spam remains outside direct focus rewards. | Focus files have no direct duplicate `add_ideas`, but 27 called helpers in `common/scripted_effects/005_soviet_collapse_effects.txt` add ideas. `soviet_collapse_update_consolidated_republic_ideas` is called 111 times from focus files. | Parent should audit helper rewards and convert repeated tier-updater idea calls into route-specific decisions, modifiers, claims, cores, units, laws, or one-time endgame ideas. |
| High | Compact crisis splinters are still shallow. | PRA has 22 focuses; TSC/RMC/DSC/NRF/ICD each have 18. | Add full route families or queue a separate focus rework plan. |
| High | Ancient restoration trees are shallow and lore-light. | KZR/SOG/KHW/ALN each have 16 focuses and share repeated ancient-restoration icon families. | Add distinct restoration mechanics, claims, diplomacy, army, industry, and endgame paths. |
| High | OGB is still too shallow. | OGB has 23 focuses. This patch only cleaned linework, filters, and one obvious claim reward mismatch. | Give OGB real political/clerical/scholarly, Volga trade, heritage army, diplomacy, and conquest branches. |
| Medium | Route-special mechanics are often helper driven. | Many focuses call consolidation/custom-splinter helper effects rather than exposing unique route unlocks in the focus file. | Parent should inspect helpers after current scripted-effect work settles. |
| Medium | Focus filters have improved locally but still need a full semantic review. | This patch corrected five obvious filter mismatches; a heuristic scan cannot prove all filters match every helper-side reward. | Re-run after helper reward changes. |

## Icon Coverage Table

| Check | Result | Notes |
| --- | --- | --- |
| Focuses with explicit icon assignments | 1698/1698 | No focus was missing an icon assignment in the four audited files. |
| Repeated icon ids | 140 repeated icon ids | Repeats remain across ancient restoration families, shared regional routes, and repeated factory/custom-splinter scaffolds. This violates the spec goal that every focus should have a unique or at least route-distinct visual identity. |
| Icons changed by this patch | 0 | No icon ids were changed. |
| Missing icon references validated against physical DDS files | Not fully validated | This audit checked focus-side assignment coverage, not every referenced sprite definition and DDS. |

## Localisation and Reward Mismatches

| Check | Result | Notes |
| --- | --- | --- |
| Missing focus names/descriptions | 0 missing names, 0 missing descriptions | Localisation keys are present for all 1698 audited focus ids. |
| Direct reward mismatch patched | 1 | `OGB_claim_the_old_trade_cities` now grants direct claims matching its title/description. |
| Remaining mismatch risk | High | Helper-side rewards can make descriptions appear correct while the focus file itself remains generic. Parent should review helper effects after concurrent system edits settle. |
| Localisation keys changed | 0 | No localisation edits were required for the bounded patch. |

## AI Behavior Gaps

| Area | Gap |
| --- | --- |
| AI weights exist | Every audited focus has an `ai_will_do` block. |
| Route strategy | Many weights are local base/modifier choices rather than a broader route-aware strategy that commits countries into coherent political, industrial, military, diplomacy, expansion, or special-mechanic lines. |
| Compact and ancient trees | AI behavior cannot compensate for shallow route structure; these trees need content depth first. |
| Helper reward awareness | AI weights cannot be fully audited until helper-side idea/reward spam is resolved. |

## Validation Run

| Validation | Result |
| --- | --- |
| Brace depth for four audited focus files | Passed: final depth 0 and minimum depth 0 for each file. |
| Duplicate focus id scan | Passed: 1698 total focus ids, 1698 unique focus ids. |
| Missing prerequisite refs | Passed: none found. |
| Missing mutual exclusion refs | Passed: none found. |
| Missing `relative_position_id` refs | Passed: none found. |
| Direct duplicate `add_ideas` inside focus rewards | Passed: none found. |
| Unsupported `<=` or `>=` in audited focus files | Passed: none found. |
| Missing localisation name/description keys | Passed: none found. |
| Missing icon assignments | Passed: none found. |
| `git diff --check` for touched files | Passed. |

## Skipped Validation

- In-game HOI4 validation was not run from this subagent environment.
- Full helper-side behavior validation was skipped because `common/scripted_effects/005_soviet_collapse_effects.txt` is parent-owned during the current concurrent patch.
- Full sprite DDS existence validation was not run; this audit focused on focus-side icon assignment coverage.

## Remaining Route Risks

| Risk | Impact |
| --- | --- |
| Helper-call idea spam remains unresolved. | The trees can still feel idea-spammy even though direct duplicate `add_ideas` in focus rewards were clean. |
| Shallow compact, OGB, and ancient trees remain. | Several chaos/factory/ancient countries still do not meet the requested overpowered distinct political/industrial/expansion branch standard. |
| Repeated icons remain. | Visual route identity remains weaker than the focus-tree spec requires. |
| AI route identity remains local and thin. | Countries may take focuses legally but not behave like coherent political or expansion routes. |
| Parent scripted-effect changes may alter reward semantics. | Focus reward/filter/localisation audits should be rerun after parent work in scripted effects and decisions is complete. |

## Plan Handoff Path

No separate improvement-plan file was created by this subagent. This handoff is the actionable follow-up record:

`docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_tree_audit_ogb_pathline_filter_patch_handoff.md`
