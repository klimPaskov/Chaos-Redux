# Event 005 Soviet Collapse Focus Tree Audit and NRF/OGB Patch Handoff

Date: 2026-05-30
Scope: focused audit of Soviet Collapse focus files and a bounded patch in the custom splinter / factory successor focus scope.

## Changed Files

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_event005_focus_tree_audit_nrf_ogb_patch_handoff.md`

No localisation keys were changed.

## Changed Focus IDs

- `NRF_salvage_the_dark_berths`
- `NRF_dead_convoy_supply_board`
- `NRF_ghost_convoy_escorts`
- `NRF_fleet_that_does_not_dock`
- `NRF_northern_revenant_fleet`
- `OGB_claim_the_old_trade_cities`

## Route Coverage Table

| Required route family | Implemented coverage | Status | Notes |
|---|---|---|---|
| Political/state identity | Present in all four files, strongest in republics and 47-focus custom splinters | Partial | Several crisis trees are identity-forward but short. OGB remains a 23-focus tree. |
| Industry/economy | Present broadly | Partial | Many trees use repeated one-state building rewards instead of a developed production loop. Worst clusters remain in `internal_soviet_collapse_*`, `KRS`, `DHC`, `KHC`, `UWD`, `ARD`, `NLC`. |
| Military/security | Present broadly | Partial | DSC is now strongly aggressive; NRF has stronger naval/port payoffs after this patch. Several security/directorate trees still lean on repeated equipment/building payoffs. |
| Expansion/map ambition | Present in many endgames | Partial | Many branches defer real map aggression to late helpers. Some middle branches still have only one claim or no postwar handling. |
| Decisions/mechanics | Uneven | Partial | PRA/DSC/NRF/OGB/CFR have decision hooks; many 47-focus splinters still have zero or one direct decision/map hook in the focus parser. |
| AI route behavior | Present but uneven | Partial | Every parsed focus had `ai_will_do`, but many weights are base-only or simple pressure checks rather than full route-aware plans. |

## Current-State Audit Findings

| File/tree | Evidence | Risk |
|---|---|---|
| `005_soviet_collapse_custom_splinters.txt`, `NRF_soviet_collapse_focus_tree` | 18 focuses; parser found 11 equipment-focused rewards and 9 flat reward cluster examples, including `NRF_salvage_the_dark_berths`, `NRF_dead_convoy_supply_board`, `NRF_ghost_convoy_escorts`, `NRF_fleet_that_does_not_dock`, `NRF_northern_revenant_fleet`. | Naval identity existed, but too many rewards were small convoy/equipment payouts. |
| `005_soviet_collapse_custom_splinters.txt`, `DSC_soviet_collapse_focus_tree` | 18 focuses; parser found 7 equipment rewards, 4 building rewards, 7 map/decision hooks. `DSC_grave_ordnance_claims`, `DSC_dead_regiment_columns`, `DSC_armies_that_do_not_demobilize`, and `DSC_congress_of_the_dead_army` are the danger core. | Much better than the complaint baseline, but still compact for a high-chaos military threat. |
| `005_soviet_collapse_factory_successors.txt`, `OGB_soviet_collapse_focus_tree` | 23 focuses versus 47 for CFR and 58 for MFR. `OGB_claim_the_old_trade_cities` only added claims before this patch. | Shallow compared with other successors; expansion payoff needed stronger controlled-state handling. |
| `005_soviet_collapse_factory_successors.txt`, `CFR_soviet_collapse_focus_tree` | 47 focuses, 9 building rewards, 6 map/decision hooks. Existing dirty diff shows broader CFR construction payoff edits already present before this handoff. | High-impact construction identity is underway, but broad review is needed to separate parent edits from final intended design. |
| `005_soviet_collapse_custom_splinters.txt`, 47-focus trees | Parser found flat reward clusters in `KRS` 18, `DHC` 15, `KHC` 16, `UWD` 23, `ARD` 20, `NLC` 16. | These remain the worst repeated building/equipment reward offenders after this narrow patch. |
| `005_soviet_collapse_republics.txt` | Flat reward clusters remain high in `internal_soviet_collapse_focus_tree` 29, `kazakhstan` 19, `central_asia` 17, `moldova` 14. | Needs a separate republic-route reward pass. |
| `005_soviet_collapse_ancient_restorations.txt` | Four trees, 16 focuses each. No direct idea spam, but branch depth is shallow by the Event 005 focus spec. | Needs expansion plan or explicit crisis-tree classification. |

Direct duplicate scan result: no repeated `add_ideas` entries inside the same `completion_reward` were found in the four Soviet Collapse focus files. Current "idea spam" now mostly appears as repeated helper/update calls and endgame helper ideas rather than direct duplicate focus rewards.

## Layout and Pathline Risks

| Tree/file | Evidence | Risk |
|---|---|---|
| `soviet_collapse_ukraine_focus_tree` | Coordinate audit found path risks around `ukr_soviet_collapse_black_banner_compact` and route selectors under `ukr_soviet_collapse_question_of_statehood`. | Possible lines through route blocks; needs visual review. |
| `PRA_soviet_collapse_focus_tree` | Path risks around `PRA_armored_train_directorate` and the late moving-state branch; compact continuous panel position remains at x=1536. | Mobile rail branch can still read crowded. |
| `KRS`, `UDC`, `SDZ`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `BAC`, `ARD`, `NLC` | Coordinate audit found multiple possible parent-child line crossings. | Broad layout pass still required; not safe to solve in this narrow patch. |

No same-coordinate focus collisions were found in the mechanical coordinate audit.

## Focus Icon Coverage Table

| File | Focus blocks | Missing focus icon assignment | Notes |
|---|---:|---:|---|
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | Definition-file validation was not in scope. |
| `005_soviet_collapse_republics.txt` | 501 | 0 | Definition-file validation was not in scope. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | No focus art assignment changed. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | No focus art assignment changed. |

## Localisation and Reward Mismatch List

- No localisation keys were edited.
- No changed focus title/description needed a new key because all patch changes reused existing focus IDs and existing tooltip keys.
- Remaining mismatch risk: NRF focus text may still understate the stronger mobilization/port-control rewards added here; a localisation tone pass should verify this in `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`.

## AI Behavior Gaps

- All parsed focuses have `ai_will_do`.
- Several large trees still use simple base weights plus one or two conditions. The worst remaining issue is not missing AI blocks, but missing route strategy depth across the 47-focus splinters and republic trees.
- NRF improved indirectly because its stronger focus rewards call existing mobilization and expansion helpers that already add hostile AI strategy where appropriate.

## Patch Behavior Before and After

| Focus | Before | After |
|---|---|---|
| `NRF_salvage_the_dark_berths` | Small convoy reward plus infrastructure. | Unlocks the marine decision tooltip, adds naval experience, expands a coastal industrial port with a dockyard and infrastructure. |
| `NRF_dead_convoy_supply_board` | Small convoy reward plus naval experience and supply helper. | Adds depot control and builds coastal supply/infrastructure instead of another convoy payout. |
| `NRF_ghost_convoy_escorts` | Manpower, convoy, naval experience, coastal defenses. | Replaces the convoy with the existing signature-force mobilization helper and keeps coastal defenses. |
| `NRF_fleet_that_does_not_dock` | Claim, naval experience, dockyard, identity helpers. | Removes another convoy payout and adds existing expansion-claim/wargoal helper in hidden effects. |
| `NRF_northern_revenant_fleet` | Duplicated convoy/support/building rewards on top of the endgame helper. | Leaves the endgame helper to provide the final payoff and removes the direct duplicate equipment/building stack. |
| `OGB_claim_the_old_trade_cities` | Added claims to 250, 251, 651. | Adds cores on those states if OGB already controls them, keeping the claim setup for future conquest. |

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt` - passed.
- Brace balance check for touched focus files - passed, final depth 0 for both.
- `rg -n "<=|>="` on touched focus files - passed, no matches.
- Duplicate direct reward scan for repeated `add_ideas` inside each `completion_reward` in touched files - passed, no duplicates.

## Skipped Validation

- No game load was run.
- Localisation encoding validation was skipped because no localisation file was changed.
- Focus visual definition validation was skipped because this pass did not inspect visual definition files.

## Remaining Route Risks

- Full focus rework remains incomplete. This patch only improved NRF and one OGB expansion payoff.
- `PRA`, `TSC`, `ICD`, and several 47-focus custom splinters still need reward identity cleanup.
- `OGB` still needs broader depth if it is meant to stand beside CFR and MFR.
- Republic and ancient-restoration trees still require separate reward/layout passes.
- Existing unrelated dirty edits are present in the touched focus files; review this handoff against the changed focus IDs above rather than the entire current dirty diff.
