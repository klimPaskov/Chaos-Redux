# Soviet Collapse Focus Tree Depth Route Integration Handoff

Date: 2026-05-29
Agent: Chaos Redux focus tree subagent

## Scope

Continued the Soviet Collapse focus cleanup after `2026_05_29_focus_tree_reward_route_patch_handoff.md`.

Owned files touched:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No localisation, icons, helpers, decisions, or scripted effects were edited.

## High-Priority Fixes Applied

| Area | Before | After |
| --- | --- | --- |
| Ukraine League route | League focuses set many flags but did not consistently expose the actual Ukrainian League decisions. | Added decision unlock tooltips to League founding, equality, arms, border arbitration, Black Sea, and security-zone focuses. |
| Belarus rail/League route | Rail and depot focuses were mostly variable/building rewards. | Added logistics/front/League unit decision surfacing and unit deployment unlock on the Minsk depot route. |
| Kazakhstan/Central Asia/Caucasus league routes | Regional league payoffs were mostly generic preparation/recognition rewards. | Added regional-faction decision surfacing, defensive-war hooks, and League unit deployment unlocks on route-capstone focuses. |
| PRA/DSC/NRF/ARD chaos splinters | Existing decisions existed but some route focuses did not clearly point players toward them. | Added direct unlock tooltips for rail repair/supply/junction pushes, dead army, revenant fleet, and Arctic Directorate signature-force/extreme decisions. |
| CFR/MFR factory successors | Industrial routes still had weak decision linkage in some mid/late route focuses. | Added reconstruction/arsenal decision surfacing and rail authority payoff on MFR armored train workshops. |
| Ancient restorations | Returned-name decisions were mostly exposed by setup/endgame flags, not early focus route choices. | Old border files now activate returned-name decision surface and point to museum/archivist decisions; charters point to banner and tag-specific claim decisions. |
| Focus filters | A few touched focuses did not advertise the reward type they actually grant. | Updated `kaz_soviet_collapse_caspian_security_detachments`, `ARD_naval_infantry_yards`, and `MFR_the_arsenal_state` filters. |

## Changed Focus IDs

Republics:

- `ukr_soviet_collapse_league_founding_charter`
- `ukr_soviet_collapse_league_of_equals`
- `ukr_soviet_collapse_kyiv_leads_the_front`
- `ukr_soviet_collapse_black_sea_hegemony`
- `ukr_soviet_collapse_border_states_accept_kyiv`
- `ukr_soviet_collapse_external_border_arbitration`
- `ukr_soviet_collapse_league_security_zone_mandates`
- `blr_soviet_collapse_prepare_league_freight_tables`
- `blr_soviet_collapse_every_track_through_minsk`
- `blr_soviet_collapse_the_league_depot_at_minsk`
- `kaz_soviet_collapse_steppe_federation_charter`
- `kaz_soviet_collapse_resource_sovereignty`
- `kaz_soviet_collapse_caspian_security_detachments`
- `kaz_soviet_collapse_call_the_steppe_congress`
- `caucasus_soviet_collapse_oilfield_security_compacts`
- `caucasus_soviet_collapse_caucasus_defense_compact`
- `central_asia_soviet_collapse_southern_republics_coordinate`
- `central_asia_soviet_collapse_the_southern_shield`
- `central_asia_soviet_collapse_federation_state`

Custom splinters:

- `PRA_repair_crews_without_ministries`
- `PRA_mobile_workshops`
- `PRA_seize_the_junction_cities`
- `PRA_rails_over_capitals`
- `DSC_dead_regiment_columns`
- `DSC_congress_of_the_dead_army`
- `NRF_icebound_marine_guard`
- `NRF_northern_revenant_fleet`
- `ARD_naval_infantry_yards`
- `ARD_arctic_port_endurance`
- `ARD_extreme_path`

Factory successors:

- `CFR_a_civilian_factory_in_every_capital`
- `MFR_production_war_room`
- `MFR_factory_guard_columns`
- `MFR_armored_train_workshops`
- `MFR_the_arsenal_state`

Ancient restorations:

- `KZR_old_border_files`
- `KZR_khazar_charter`
- `SOG_old_city_border_files`
- `SOG_sogdian_city_charter`
- `KHW_old_oasis_border_files`
- `KHW_khwarazmian_water_charter`
- `ALN_old_pass_border_files`
- `ALN_alan_pass_charter`

## Route Coverage Table

| Tree / Branch | Coverage After Patch | Remaining Risk |
| --- | --- | --- |
| Ukraine League / Black Sea / border arbitration | Better connected to Ukrainian League decisions, League unit templates, League arms, Black Sea, and security-zone mechanics. | Broad Ukraine layout still has pathline risks from the earlier tree shape; no full route redesign was attempted. |
| Belarus rail corridor / League logistics | Minsk rail and depot focuses now connect to regional logistics, depot/front decisions, and League deployments. | Forest/high-chaos Belarus route still has limited unique mechanics beyond existing high-chaos identity helpers. |
| Kazakhstan resources / steppe federation | Federation and steppe congress focuses now point to regional federation decisions; Caspian/resource branches point to defense/oilfield decision surfaces. | Resource branch still relies on existing variable and construction helpers; no new resource decision chain was added. |
| Caucasus compact / oilfield security | Defense compact now surfaces founding, defense goal, defensive war, and League deployments. | Caucasus remains compact, with only narrow decision linkage added. |
| Central Asia federation / southern shield | Federation and shield focuses now point to regional federation, coordination, defense, and defensive-war decisions. | Basmachi and oasis subroutes still need deeper bespoke decisions in a future pass. |
| PRA Pale Railway | Rail repair, mobile supply, junction push, and moving-state decisions are surfaced by the rail route focuses. | No new PRA rail decision effects were added; existing decision logic remains authoritative. |
| DSC Dead Soldiers | Dead regiment and dead-army endgame focuses now point to dead-army decisions. | The living/memorial alternative route was not expanded. |
| NRF Revenant Fleet | Marine and revenant fleet focuses now point to existing naval decisions. | The living port route remains mostly conventional. |
| ARD Arctic Directorate | Naval infantry, endurance, and extreme path now point to ARD signature/extreme decisions; naval filter fixed on infantry yards. | ARD route remains dense and still has broader layout/style issues inherited from the generated splinter set. |
| CFR Construction state | Civilian factory route now points to reconstruction contracts. | CFR still needs a full pass on city/protectorate route identity. |
| MFR Arsenal state | War room, guards, armored trains, and arsenal state now point to arsenal decisions and stronger rail/army payoff. | Arms-market and eternal-arsenal route identity remains broader than this bounded patch. |
| Ancient restored states | Old border files activate returned-name decision surface; charters point to banner and claim decisions. | No new formable or claim chains were created; ancient trees remain 16-focus compact trees. |

## Missing Or Simplified Content

- No new focus families, formable chains, decision categories, scripted helpers, or localisation were added.
- No large redesign of Ukraine, Belarus, Kazakhstan, Caucasus, Central Asia, custom splinters, factory successors, or ancient restorations was attempted.
- Several improvements are decision-surface integration via existing `unlock_decision_tooltip` and existing flags/helpers, not new mechanics.
- Regional decision tooltips assume existing regional leader/founder conditions; this patch did not change the underlying `can_found_*` or regional faction triggers.
- Ancient restored states still use existing returned-name mechanics; this patch only makes the decision surface reachable/visible earlier through old-border focuses.

## Icon Coverage Table

| File | Result |
| --- | --- |
| Republics | No icon IDs changed. Changed focuses already had icons. |
| Custom splinters | No icon IDs changed. Changed focuses already had icons. |
| Factory successors | No icon IDs changed. Changed focuses already had icons. |
| Ancient restorations | No icon IDs changed. Changed focuses already had icons. |

## Localisation And Reward Mismatch List

- No localisation keys were added or renamed.
- Changed focus IDs all have English localisation somewhere under `localisation/`.
- No new custom tooltip localisation was introduced.
- No missing `unlock_decision_tooltip` target IDs were found.
- Reward text risk remains where localisation does not mention newly surfaced decisions; because these are standard HOI4 unlock tooltips and no focus names/descriptions were changed, no localisation edit was made in this bounded pass.

## AI Behavior Gaps

- Existing `ai_will_do` blocks were not broadly redesigned.
- Some changed focuses now expose stronger decisions to the player but AI behavior still mainly follows prior route flags, chaos tier, war state, and SOV pressure checks.
- Regional league AI remains dependent on the existing decision AI weights and regional faction triggers.
- Broad route-aware AI for Belarus forest routes, Kazakhstan resource diplomacy, Central Asia Basmachi/oasis routes, CFR city/protectorate routes, and ancient symbolic-vs-expansion routes remains future work.

## Validation Run

Commands/checks run:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Passed with no output.
- Unsupported operator scan:
  - `rg -n "<=|>=" ...target focus files`
  - Passed; no `<=` or `>=` found.
- Brace balance script:
  - Republics: `opens=4245 closes=4245 final_depth=0`
  - Custom splinters: `opens=10866 closes=10866 final_depth=0`
  - Factory successors: `opens=1340 closes=1340 final_depth=0`
  - Ancient restorations: `opens=618 closes=618 final_depth=0`
- Duplicate focus ID scan:
  - `1739` focus/tree IDs scanned across the four focus files.
  - `0` duplicates found.
- Decision target scan:
  - `unlock_decision_tooltips_missing 0`
- Repeated same-idea reward scan:
  - `add_ideas_total 0` in all four target focus files.
- Changed focus localisation scan:
  - `changed_focus_ids 43`
  - `missing_loc_any_english_yml 0`
- Invalid old focus filter scan:
  - `rg -n "FOCUS_FILTER_ARMY(\\s|\\})" ...target focus files`
  - Passed with no output.
- Basic coordinate/pathline scan:
  - Republics: `501` focuses, `9` trees, `0` same-tree duplicate coordinates, `76` basic same-row/same-column pathline risks.
  - Custom splinters: `1005` focuses, `25` trees, `0` same-tree duplicate coordinates, `20` basic pathline risks.
  - Factory successors: `128` focuses, `3` trees, `0` same-tree duplicate coordinates, `48` basic pathline risks.
  - Ancient restorations: `64` focuses, `4` trees, `0` same-tree duplicate coordinates, `0` basic pathline risks.

## Skipped Validation

- No full HOI4 launch or in-game validation was run.
- No scripted-effect or decision syntax validation was performed beyond decision target existence, because the task scope was focused on four focus files.
- No commit was created because the worktree already contains many unrelated dirty edits in and outside the touched files; staging whole files would risk including parent/other-agent work.

## Remaining Route Risks

- Broad pathline/layout risks remain in republic, custom splinter, and factory successor trees. This pass added no coordinates and did not attempt the full layout rewrite.
- Some regional/league links are still decision-surface exposure rather than new route-specific mechanics.
- Belarus, Kazakhstan, Central Asia, CFR, MFR, and ancient restored states still need route-specific AI weighting and deeper branch identity in a later full pass.
- Focus descriptions may not explicitly mention every surfaced decision; no localisation was changed to avoid unnecessary text churn.

## Plan Handoff

No new broader improvement plan was written. The existing follow-up plan remains the correct broad-work handoff:

- `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
