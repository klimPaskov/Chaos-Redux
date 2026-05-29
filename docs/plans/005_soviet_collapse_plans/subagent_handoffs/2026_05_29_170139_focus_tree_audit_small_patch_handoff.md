# Soviet Collapse Focus Tree Audit and Small Patch Handoff

Timestamp: 2026-05-29 17:01:39 UTC

Scope:

- Audited:
	- `common/national_focus/005_soviet_collapse_republics.txt`
	- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
	- `common/national_focus/005_soviet_collapse_factory_successors.txt`
	- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Patched only:
	- `common/national_focus/005_soviet_collapse_factory_successors.txt`
	- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- No localisation, scripted effects, scripted triggers, decisions, binary flags, scenario effects, or release systems were edited.
- Skills used: `hoi4-focus-trees`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`.
- Required references read before edits: offline Paradox wiki Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding; vanilla documentation for triggers, effects, modifiers, localisation formatter, script concepts; vanilla focus precedent from `generic.txt`/`soviet.txt`.

## High-Priority Fixes First

| Focus id | File | Before | After |
| --- | --- | --- | --- |
| `OGB_reopen_volga_trade_tolls` | `005_soviet_collapse_factory_successors.txt` | Reopened Volga tolls with train and infantry stockpile rewards plus one infrastructure build. | Removed the generic stockpiles and added rail and supply-node construction to the existing Volga logistics state reward. |
| `MFR_workers_own_the_arsenal` | `005_soviet_collapse_factory_successors.txt` | Worker arsenal route added three separate stockpile rewards. | Replaced the stockpile list with a core-state arms factory and shared slot while keeping manpower, XP, quotas, depot control, and worker route variables. |
| `KZR_caspian_patrol_letters` | `005_soviet_collapse_ancient_restorations.txt` | Caspian patrol focus included a small convoy stockpile and only political filter. | Removed the convoy stockpile and added `FOCUS_FILTER_NAVY_XP` to match the navy XP reward. |
| `KZR_khazar_charter` | `005_soviet_collapse_ancient_restorations.txt` | Charter payoff added train and convoy stockpiles. | Replaced the convoy reward with rail and supply-node construction while keeping train support for the transit state. |
| `ALN_symbolic_pass_principality` | `005_soviet_collapse_ancient_restorations.txt` | Symbolic pass route gave a small motorized stockpile. | Replaced it with capital pass infrastructure and fort construction. |

## Route-Depth Table

Counts are static focus-block scans. Branch columns are filter/effect coverage counts, not quality guarantees.

| Tag/tree | Focuses | Political | Industry/logistics | Military | Expansion | Decision/mechanic hooks | Chaos aggression | Idea/stockpile risk | Layout/pathline risk | Remaining work |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `UKR` / `soviet_collapse_ukraine_focus_tree` | 83 | 63 | 18 | 41 | 0 | 83 | 0 | No direct ideas; 1 stockpile focus | 20 rough line-hit risks; multi-route mutual-exclusion row has focuses between distant route locks | Needs manual layout rewrite and expansion/war consequence pass. |
| shared breakaway / `soviet_collapse_breakaway_focus_tree` | 36 | 23 | 9 | 17 | 0 | 36 | 0 | No direct ideas; 2 stockpile focuses | 1 line-hit risk | Medium depth; needs sharper route end states. |
| internal republics / `soviet_collapse_internal_republic_focus_tree` | 62 | 40 | 24 | 27 | 0 | 62 | 0 | No direct ideas; 2 stockpile focuses | 1 line-hit risk | Stronger expansion and regional decision payoffs still needed. |
| Baltic / `soviet_collapse_baltic_focus_tree` | 42 | 33 | 9 | 18 | 0 | 42 | 0 | No direct ideas; 2 stockpile focuses | 2 line-hit risks | Needs more direct claims/settlement or defensive league consequences. |
| Caucasus / `soviet_collapse_caucasus_focus_tree` | 40 | 31 | 13 | 13 | 0 | 40 | 0 | No direct ideas; 4 stockpile focuses | 2 line-hit risks | Oil/mountain branches need more route-specific decisions. |
| Central Asia / `soviet_collapse_central_asia_focus_tree` | 45 | 36 | 9 | 16 | 1 | 45 | 1 | No direct ideas; 4 stockpile focuses | One route selector sits between mutually exclusive selector endpoints | Needs layout cleanup for route selector row. |
| Moldova / `soviet_collapse_moldova_focus_tree` | 48 | 38 | 12 | 13 | 0 | 47 | 0 | No direct ideas; 6 stockpile focuses | 11 line-hit risks | Needs corridor/union branch spacing and non-stockpile reward pass. |
| Belarus / `soviet_collapse_belarus_focus_tree` | 53 | 40 | 22 | 20 | 0 | 53 | 0 | No direct ideas; no direct stockpile spam | 6 line-hit risks | Rail/corridor identity is present but route mechanics remain shallow. |
| Kazakhstan / `soviet_collapse_kazakhstan_focus_tree` | 92 | 72 | 26 | 32 | 0 | 92 | 0 | No direct ideas; 5 stockpile focuses | 24 line-hit risks | Large but still layout-heavy; expansion payoffs need clearer claims/war/settlement. |
| `FTH` | 47 | 28 | 15 | 26 | 0 | 47 | 0 | 5 stockpile focuses | Low static layout risk | Needs route-specific endgame, not more helper-only rewards. |
| `PRA` | 22 | 14 | 7 | 7 | 1 | 22 | 1 | 4 stockpile focuses | Low static layout risk | Shallow railway crisis tree; needs deeper rail/supply decision loop. |
| `TSC` | 18 | 13 | 5 | 7 | 1 | 18 | 1 | 3 stockpile focuses | Low static layout risk | Shallow science crisis tree. |
| `RMC` | 18 | 13 | 3 | 9 | 3 | 18 | 1 | 4 stockpile focuses | Low static layout risk | Shallow reliquary/military route. |
| `DSC` | 18 | 13 | 3 | 12 | 3 | 18 | 3 | 4 stockpile focuses | Low static layout risk | Aggression exists, but Dead Soldiers Congress remains too shallow for the requested war-goal/core/unit identity. |
| `NRF` | 18 | 13 | 4 | 13 | 3 | 18 | 2 | 11 stockpile focuses | Low static layout risk | Highest remaining reward-spam risk among crisis splinters. |
| `ICD` | 18 | 13 | 4 | 9 | 3 | 18 | 1 | 5 stockpile focuses | Low static layout risk | Shallow memorial/death route. |
| `BSC` | 47 | 32 | 12 | 22 | 0 | 47 | 0 | 9 stockpile focuses | Low static layout risk | Mountain route rewards still equipment-heavy. |
| `TNC` | 47 | 33 | 13 | 21 | 0 | 47 | 0 | 2 stockpile focuses | Low static layout risk | Route depth acceptable, identity payoff needs review. |
| `ALA` | 47 | 31 | 12 | 20 | 0 | 47 | 0 | 4 stockpile focuses | Low static layout risk | Needs expansion/mechanic payoff. |
| `BBH` | 47 | 27 | 13 | 28 | 0 | 47 | 0 | 8 stockpile focuses | Low static layout risk | Military column identity still stockpile-heavy. |
| `KRS` | 47 | 25 | 10 | 32 | 0 | 47 | 0 | 7 stockpile focuses | Low static layout risk | Naval/port branch needs stronger decision hooks. |
| `UDC` | 47 | 30 | 11 | 26 | 0 | 47 | 0 | 4 stockpile focuses | Low static layout risk | Route payoffs still generic. |
| `SDZ` | 47 | 30 | 11 | 26 | 0 | 47 | 0 | 6 stockpile focuses | Low static layout risk | Security/archive mechanics need depth. |
| `GAC` | 47 | 29 | 15 | 24 | 0 | 47 | 0 | 7 stockpile focuses | Low static layout risk | Green/forest branch needs more map pressure. |
| `DHC` | 47 | 27 | 13 | 23 | 0 | 47 | 0 | 10 stockpile focuses | Low static layout risk | Host/river identity still convoy-stockpile heavy. |
| `KHC` | 47 | 27 | 13 | 24 | 0 | 47 | 0 | 13 stockpile focuses | Low static layout risk | Highest full-tree stockpile risk. |
| `FEV` | 47 | 26 | 18 | 25 | 0 | 47 | 0 | 8 stockpile focuses | Low static layout risk | Far East route needs more port/rail decision depth. |
| `SZA` | 47 | 26 | 18 | 24 | 0 | 47 | 0 | 4 stockpile focuses | 1 line-hit risk | Needs endgame route payoff. |
| `UWD` | 47 | 26 | 16 | 25 | 0 | 47 | 0 | 11 stockpile focuses | 5 line-hit risks | Ural factory tree remains stockpile-heavy despite layout improvements. |
| `MRC` | 47 | 26 | 13 | 26 | 0 | 47 | 0 | 4 stockpile focuses | Low static layout risk | Expansion/payoff hooks need review. |
| `IUL` | 47 | 27 | 16 | 26 | 0 | 47 | 0 | 7 stockpile focuses | Low static layout risk | Volga federation route should interact more with OGB. |
| `BAC` | 47 | 27 | 16 | 25 | 0 | 47 | 0 | 7 stockpile focuses | Low static layout risk | Autonomy route needs mechanics. |
| `ARD` | 47 | 27 | 16 | 26 | 0 | 47 | 0 | 13 stockpile focuses | 1 line-hit risk | Arctic/naval route remains convoy-stockpile heavy. |
| `NLC` | 47 | 30 | 14 | 22 | 0 | 47 | 0 | 5 stockpile focuses | 4 line-hit risks | Polar logistics needs more mission/decision depth. |
| `CFR` | 47 | 41 | 30 | 7 | 3 | 47 | 2 | No direct ideas; no direct stockpile rewards | Multi-choice mutual-exclusion rows have intermediate route choices | Stronger but still needs governance/strategy route layout rewrite. |
| `OGB` | 23 | 19 | 6 | 8 | 2 | 23 | 2 | No direct ideas; 1 stockpile focus after patch | Low static layout risk | Still shallow and needs fuller Old Great Bulgaria route family. |
| `MFR` | 58 | 48 | 38 | 27 | 1 | 58 | 3 | No direct ideas; 1 stockpile focus after patch | Multi-choice mutual-exclusion rows have intermediate route choices | Strong identity, but route selector pathline cleanup remains. |
| `KZR` | 16 | 9 | 3 | 6 | 5 | 16 | 3 | No direct ideas; 3 stockpile focuses after patch | Low static layout risk | Shallow ancient restoration; needs broader route depth. |
| `SOG` | 16 | 9 | 3 | 5 | 5 | 16 | 3 | No direct ideas; 1 stockpile focus | Low static layout risk | Shallow ancient restoration. |
| `KHW` | 16 | 10 | 3 | 5 | 5 | 16 | 3 | No direct ideas; 4 stockpile focuses | Low static layout risk | Shallow ancient restoration. |
| `ALN` | 16 | 9 | 2 | 5 | 5 | 16 | 3 | No direct ideas; no stockpile focuses after patch | Low static layout risk | Shallow ancient restoration. |

## Duplicate or Repeated Idea Rewards

- Direct `add_ideas =` scan across all four scoped focus files returned no matches.
- Duplicate repeated idea additions inside a focus are therefore not present in the audited focus files.
- No idea localisation or idea definitions were changed.
- Remaining idea-spam risk is indirect: many focuses still call helper effects that update consolidated republic ideas. This is not duplicate direct idea spam, but the parent should audit helper-side idea lifecycles before claiming final completion.

## Remaining Stockpile Reward Issues

Patched stockpile-heavy focus ids are listed in the high-priority fixes section. Remaining direct stockpile focuses include:

- Republic/shared: `ukr_soviet_collapse_count_the_depot_keys`, `soviet_collapse_military_defense_council`, `soviet_collapse_foreign_liaison_government`, `internal_soviet_collapse_far_eastern_port_authority`, `internal_soviet_collapse_republic_volunteer_standards`, Baltic/Caucasus/Central Asia/Moldova/Kazakhstan stockpile support focuses.
- Crisis/high-chaos stockpile-heavy trees: `NRF` 11 focuses, `KHC` 13, `ARD` 13, `UWD` 11, `DHC` 10, `BSC` 9, `BBH` 8, `FEV` 8.
- Ancient restorations after patch: `KZR_old_border_files`, `KZR_expansionist_steppe_levy`, `KZR_khazar_charter`, `SOG_expansionist_merchant_claims`, `KHW_canal_recognition_letters`, `KHW_expansionist_water_claims`, `KHW_khwarazmian_water_charter`, `KHW_delta_without_a_center`.

I left these for parent or a broader pass because replacing them cleanly requires route-by-route design, state targeting, or decision system expansion rather than a safe local cleanup.

## Static Layout Audit

- Duplicate focus ids: none.
- Missing prerequisite or mutual-exclusion references: none.
- Duplicate coordinates within a single tree: none detected.
- Near same-row coordinate collisions: none detected at distance 0 or 1.
- Mutual-exclusion focus between/under pathlines detected:
	- `soviet_collapse_ukraine_focus_tree`: the multi-route row around `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_black_banner_compact`, and `ukr_soviet_collapse_protectorate_debate` has intermediate route choices between distant mutual-exclusion endpoints.
	- `soviet_collapse_central_asia_focus_tree`: `central_asia_soviet_collapse_turkestan_federation_road` sits between `central_asia_soviet_collapse_local_republic_council` and `central_asia_soviet_collapse_military_border_authority`.
	- `CFR_soviet_collapse_focus_tree`: governance and strategy multi-choice rows have intermediate choices between distant mutual-exclusion endpoints.
	- `MFR_soviet_collapse_focus_tree`: ownership multi-choice row has intermediate choices between distant mutual-exclusion endpoints.
- Rough straight prerequisite-line hits:
	- Ukraine: 20, highest-risk examples include `ukr_soviet_collapse_question_of_statehood -> ukr_soviet_collapse_black_banner_compact` passing near `ukr_soviet_collapse_the_commander_or_the_cabinet` and `ukr_soviet_collapse_direct_national_claims`.
	- Kazakhstan: 24 line-hit risks.
	- Moldova: 11 line-hit risks.
	- Belarus: 6 line-hit risks.
	- UWD: 5 line-hit risks.
	- NLC: 4 line-hit risks.
	- Baltic/Caucasus: 2 each.
	- Shared breakaway/internal/SZA/ARD: 1 each.
- I did not patch these layout findings because fixing them cleanly requires moving route families or reducing visible mutual-exclusion lines across large route selectors, which is broader than this safe patch pass.

## Icon Coverage Table

| Surface | Status |
| --- | --- |
| Focus icon field presence | 1,698/1,698 focus blocks have an `icon =` assignment. |
| Changed icon ids | None. |
| Changed search filters | `KZR_caspian_patrol_letters` now includes `FOCUS_FILTER_NAVY_XP` to match its navy XP reward. |
| Missing icon sprite definitions | Not revalidated against interface sprite files in this bounded pass. Earlier file-level icon assignment scan passed. |

## Localisation and Reward Mismatch List

- No localisation keys were added, renamed, or edited.
- `OGB_reopen_volga_trade_tolls`: reward now matches Volga trade/toll logistics better by building infrastructure, rail, and supply.
- `MFR_workers_own_the_arsenal`: reward now matches arsenal identity better by adding an arms factory instead of a generic equipment bundle.
- `KZR_caspian_patrol_letters`: no longer pays a small convoy stockpile for patrol letters; filter now matches navy XP.
- `KZR_khazar_charter`: transit charter now adds actual rail/supply infrastructure instead of a convoy reward.
- `ALN_symbolic_pass_principality`: pass principality now reinforces the pass rather than handing out motorized equipment.

## AI Behavior Gaps

- Direct aggression exists for several chaos tags, but many 47-focus custom splinter trees still have `aggr = 0` in the static scan. They may rely on helper effects, but visible focus-level conquer/war-goal behavior is sparse.
- `DSC` has some aggression, but the requested Dead Soldiers Congress behavior still needs more war goals, cores/claims, units, and aggressive route AI.
- `CFR` and `MFR` are improved by prior/current patches, but governance/strategy AI choices still need route cleanup around multi-choice selectors.
- `OGB` is still shallow at 23 focuses and needs a stronger restoration/Volga-expansion AI package.
- Ancient restorations are all 16-focus shallow trees. Their expansion branches have claims and SOV hostility, but they do not yet meet full route-depth expectations.

## Missing or Simplified Content

- Broad route redesign was not attempted. This pass did not add new branch families, new formable chains, new decision systems, new country identity changes, or new release hooks.
- Construction Directorate/CFR is stronger and no longer stockpile-heavy in the audited focus rewards, but its political and strategy forks still need a layout and distinct operating-model pass.
- Dead Soldiers Congress/DSC remains shallow and needs a dedicated war-goal/core/unit route expansion.
- Railway/PRA has rail identity, but remains a 22-focus shallow crisis tree and needs a deeper rail/supply decision loop.
- Factory/naval/special successors mostly have identity hooks, but many still use stockpile-heavy rewards or helper-only route payoffs.

## Validation Run

- Brace depth on four focus files:
	- `005_soviet_collapse_republics.txt`: opens 4249, closes 4249, final depth 0.
	- `005_soviet_collapse_custom_splinters.txt`: opens 10899, closes 10899, final depth 0.
	- `005_soviet_collapse_factory_successors.txt`: opens 1363, closes 1363, final depth 0.
	- `005_soviet_collapse_ancient_restorations.txt`: opens 621, closes 621, final depth 0.
- Duplicate focus ids: none across 1,698 focus blocks.
- Missing prerequisite/mutual-exclusion refs: 0.
- Unsupported operator scan: `rg -n "<=|>=" ...` returned no matches.
- Direct `add_ideas =` scan: no matches.
- `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_170139_focus_tree_audit_small_patch_handoff.md`: passed.

## Skipped Validation

- No in-game HOI4 load test or visual focus-tree screenshot pass was run.
- No localisation encoding check was needed because localisation was not edited.
- No sprite-definition validation was run because icon ids were not changed.

## Remaining Route Risks

- Worktree was dirty before this pass; many diffs in the same files predate this audit. I did not revert or normalize unrelated edits.
- Static line-hit detection is approximate and should be confirmed visually before a final focus-tree completion claim.
- The remaining stockpile lists are too broad for this patch scope and should be handled with route-specific design rather than mechanical deletion.
- No commit was made, per user instruction.
