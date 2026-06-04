# Event005 Focus Auditor Remaining Issues

Scope: current worktree audit of Event005 Soviet Collapse focus trees, excluding all CFR focus work plus `PRA_count_the_locomotives`, `PRA_repair_the_branch_lines`, `DSC_field_hospital_memorials`, and `DSC_register_field_hospital_columns` / `dsc_register_field_hospital_columns`. No gameplay files were edited.

References consulted before gameplay inspection: `AGENTS.md`, `.agents/skills/hoi4-focus-trees/SKILL.md`, `.agents/skills/hoi4-decisions-missions/SKILL.md`, offline Paradox wiki pages for Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding, plus vanilla `effects_documentation.md` focus effects.

Flags were not touched. `gfx/flags` and `interface/flags` were not opened or edited.

## 10 Highest-Priority Remaining Issues

1. `common/national_focus/005_soviet_collapse_republics.txt:11583` - `kaz_soviet_collapse_industrial_settlement_compacts`
   Visible reward dump: the completion reward directly shows depot helper, stability, two random-state blocks, four building additions, a shared slot, and resource gain. It also pathlines from `kaz_soviet_collapse_emergency_oil_boards` at `:11514` with `dx=12`, `dy=2`, making the already noisy reward sit on a layout-stressed join.

2. `common/national_focus/005_soviet_collapse_republics.txt:1204` - `ukr_soviet_collapse_black_sea_port_ledgers`
   Visible reward spam and filter mismatch: `FOCUS_FILTER_POLITICAL` is present, but the visible payload is naval/industrial (`navy_experience`, convoy stockpile, naval base, dockyard, coastal bunker). The actual political part is only the foreign-supply helper, so the player-facing reward reads like a raw port bundle.

3. `common/national_focus/005_soviet_collapse_republics.txt:7370` - `central_asia_soviet_collapse_khwarazm_restoration_debate`
   Claim spam and filter contradiction: the focus directly exposes up to seven `add_state_claim` lines across tag branches while carrying `FOCUS_FILTER_STABILITY` without a stability reward. This should be a summarized Khwarazm claim/legitimacy tooltip with hidden claims.

4. `common/national_focus/005_soviet_collapse_custom_splinters.txt:2043` - `TSC_perimeter_regiments`
   Visible reward dump: `add_manpower`, support equipment, air XP, every-owned-state bunkers, and random AA are all visible with only `FOCUS_FILTER_ARMY_XP`. This is still a generic defense bundle rather than a Tunguska observatory perimeter payoff.

5. `common/national_focus/005_soviet_collapse_custom_splinters.txt:23608` - `ARD_murmansk_port_records`; `:23736` - `ARD_naval_infantry_yards`
   Arctic Directorate rewards still read as raw mixed payloads. `ARD_murmansk_port_records` has political/stability filters but visibly gives navy XP, convoys, dockyard/infrastructure, liaison, recognition, and legal recognition. `ARD_naval_infantry_yards` gives dockyard/coastal bunker construction without an industry filter.

6. `common/national_focus/005_soviet_collapse_custom_splinters.txt:16716` - `FEV_war_plan`; `:17186` - `FEV_endgame`
   Shallow route payoff plus layout blocker. `FEV_war_plan` directly shows two random-state fortification blocks and army XP, then uses a generic custom-splinter expansion tooltip. `FEV_endgame` fans in from nine prerequisite focuses; several parents are 6-10 columns away, including `FEV_amur_buffer_posts`, `FEV_no_foreign_command_on_the_line`, and `FEV_razdolnoye_rear_area`.

7. `common/national_focus/005_soviet_collapse_custom_splinters.txt:24883` - `NLC_ice_road_customs`; `:24986` - `NLC_heated_workshop_contracts`
   Northern Lights Commune still has visible train/equipment/building chunks in mid-branch rewards. The ice-road focus also pathlines from `NLC_economy` with `dx=6`, `dy=1`, and the heated-workshop follow-up continues the same direct reward style.

8. `common/national_focus/005_soviet_collapse_factory_successors.txt:1780` - `MFR_officers_chair_the_board`; `:1835` - `MFR_merchants_of_ammunition`
   MFR route fan-out remains a layout blocker. Both route choices sit one row below `MFR_who_owns_the_rifle` at `:1760`, but `MFR_officers_chair_the_board` is `dx=13` and `MFR_merchants_of_ammunition` is `dx=9`; this is exactly the long near-horizontal prerequisite shape the wiki warns causes bad path sprites.

9. `common/national_focus/005_soviet_collapse_republics.txt:4669` - `baltic_soviet_collapse_the_legal_state_or_the_front_state`; `:4684`, `:4718`; `:6534` - `central_asia_soviet_collapse_local_republic_council`; `:6939` - `central_asia_soviet_collapse_foreign_border_patronage`
   Regional route-choice layout still has long mutual-exclusion and prerequisite lines. Baltic legal continuity to military border government is `dx=12`, and both Baltic route choices sit only one row below the fork. Central Asia local republic to foreign border patronage is also `dx=12`, with other same-row exclusions at `dx=8`. These rows should be compacted before completion claims.

10. `common/national_focus/005_soviet_collapse_republics.txt:2048` - `ukr_soviet_collapse_bread_state_whispers`
    Hard pathline issue: this child is at `x=19`, `y=9`, while its prerequisite `ukr_soviet_collapse_breadbasket_empire` is also on `y=9`. The wiki states prerequisite focuses should be above their children; same-row prerequisite layout risks broken or misleading path sprites.

## Bounded Parent Patch Suggestions

1. Hide raw reward bundles behind existing or new custom tooltips for the three worst visible dumps: `kaz_soviet_collapse_industrial_settlement_compacts`, `ukr_soviet_collapse_black_sea_port_ledgers`, and `TSC_perimeter_regiments`. Keep the gameplay effects, but move raw stockpile/building/state loops into `hidden_effect`.

2. Convert `central_asia_soviet_collapse_khwarazm_restoration_debate` to a single visible Khwarazm restoration tooltip, hide tag-conditional `add_state_claim` branches, and either remove `FOCUS_FILTER_STABILITY` or add a real stability/legitimacy payoff.

3. Compact the MFR route choice row around `MFR_who_owns_the_rifle`: move the officer, worker, merchant, and quota paths closer to the parent, or insert visible intermediate anchors so no route-choice prerequisite line spans 9-13 columns.

4. Compact the Baltic and Central Asia political route-choice rows in the same style: keep mutual exclusions meaningful, but reduce route-choice distances to avoid 8-12 column exclusion bars and one-row fan-outs.

5. Give the remaining compact chaos-country route payoffs a tag-specific visible mechanic or decision hook before more flat buildings/equipment: start with TSC observatory perimeter, FEV Far Eastern war/endgame, ARD naval directorate, and NLC ice-road logistics.

## Notes

- Direct idea spam in audited focus blocks was not found: `add_ideas`, `add_timed_idea`, `swap_ideas`, and `remove_ideas` did not appear directly inside the audited focus blocks.
- No CFR focus blocks were included in the issue list.
- No gameplay validation was run because this was a read-only audit plus handoff creation.
