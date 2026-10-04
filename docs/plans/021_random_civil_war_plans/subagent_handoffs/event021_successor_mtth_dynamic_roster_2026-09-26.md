# Event 021 successor and evolution dynamic-roster handoff

Disposition: implemented within the assigned successor and MTTH consumer files. The same-scenario probability comparison and live actor behavior remain unresolved. No commit, game launch, workbook edit, parent-file edit, or war declaration was made.

## Acceptance and owned change

The 2026-09-26 parent request authorizes the successor and evolution-timing consumer migration. The follow-up authorizes MTTH edits only after the exact baseline handoff and preserves all coefficients and unrelated eligibility gates. The user-approved external-war contract is relation-only continuity, with a case-specific human prompt for each missing relation and AI fail-closed behavior. These changes leave that parent-owned queue and its declaration decisions untouched.

Changed files:

- `common/scripted_effects/021_random_civil_war_successor_effects.txt`
- `common/scripted_triggers/021_random_civil_war_successor_triggers.txt`
- `common/mtth/021_random_civil_war_mtth.txt`
- `common/scripted_effects/021_random_civil_war_successor_effects.md`
- `common/mtth/021_random_civil_war_mtth.md`
- this handoff

## Helper and call-site map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `event021_prepare_successor_roster_adoption` | Promoted ordinary successor; explicit chain-local predecessor target and matching crisis receipts. | Saves chain-local adoption targets, copies host counters and historical evolution-I multifront receipt, sets pending transaction receipts, then rebuilds local roster. No war operation. | Existing parent before-annex path. |
| `event021_adopt_successor_roster` | Surviving ROOT with current lifecycle successor witness and matching pending crisis. | Adopts host role, clears losing opposition role and self-opponent pointer, rebuilds roster, clears pending receipts. No Event 006 identity/history rewrite. | Existing parent after-annex path. |
| `event021_rebuild_successor_roster` | Same successor and chain-local expected host/crisis targets; aligned global front ID, actor, crisis, and status rows. | Clears and rebuilds `random_civil_war_opposition_actors`, writes exact live `random_civil_war_successor_roster_count`, points the single legacy primary pointer to the first valid actor, clears the old secondary pointer, and derives live multifront state from count greater than one. It updates surviving actors' host pointers after annex. No global row is removed or mutated. | Both public adoption effects. |
| `event021_evolution_has_extra_active_actor` | Evolution sample country with `random_civil_war_crisis_id`; global front actor roster and live actor/front/war receipts. | Boolean true for two distinct active registered same-crisis opposition actors still fighting their own immediate opponents. No state writes or default roster inference. | Evolution I extra/no-extra and Evolution II multifront MTTH modifiers. |
| `event021_evolution_has_active_event6_actor` | Same sample scope; live Event 006 `random_civil_war_event6_front_active` role. | Boolean true for a live same-crisis registered primary or secondary Event 006 front still fighting its immediate opponent. No Event 006 mutation. | Evolution II independence-front and no-exposure modifiers. |

The old secondary-front flags and `random_civil_war_secondary_actor_scope` no longer select or count adopted actors. The latter is cleared only to prevent a stale compatibility pointer. The roster is filled once from current active ledger rows and keeps every eligible sibling, including an Event 006-origin actor. The global arrays are read by a reverse index loop and are never mutated during traversal. `random_civil_war_opposition_actor_scope` remains a first-actor compatibility pointer, not a roster count or an exclusion filter.

## Tuning, targets, and migration

The `base` and `factor` token sequence in the MTTH file is byte-for-byte identical after extracting those lines from the saved baseline and current source. The existing categories remain Evolution I base, authority, large-country, extra/no-extra, near-defeat, settlement; Evolution II base, border, sponsor, independence, multifront, settlement, strong-neighbor, no-exposure; and Evolution III base/severe-war. No constant or coefficient changed. A dormant Event 006 route no longer stands in for a live participant.

The adoption targets remain regular chain-local event targets with their existing completion and pending-receipt lifecycle. No new global target, country variable, array, or cleanup hook was introduced. The parent still owns front registration, post-annex row rebinding, front closure, external-war snapshots and prompts, and final sibling status reconciliation. No target/decision/mission/queue eligibility predicate was changed.

## Exact source identities and MCP evidence

The baseline auditor's saved MTTH source is `docs/plans/021_random_civil_war_plans/probability_snapshots/event021_evolution_mtth_pre_migration_2026-09-26/021_random_civil_war_mtth.txt`, raw SHA-256 `6A8C516E1A2625F3534995F6744ED373E5803AC981FD139EA95787F07B9EA71F`. The current MTTH source raw SHA-256 is `7982F0768B8ED04AE7154BCFF8CBDAC33589F8F7B031CFE12353F625891881C1`.

The successor-effects source at HEAD before this patch was raw SHA-256 `11EF44213A306A54BE3AA4E45A7D3B7C6AD661DFB92A229688AC304490A20F0D`; its current raw SHA-256 is `73A1556BC9DB6123C34FF3744A6EE2B9CCF46DE9A8CC3AB718B83C6A28323EC1`. The successor-triggers source at HEAD before this patch was raw SHA-256 `8F9787614BD6B3B3C0D477AFFD432D4AA53EDFF42819563C6D57EA16CA08AF14`; its first migration draft was `B51E4DC75E4E574A1A5A4A9AA227F2A07F0777559D85806DD6EE459B204F7F97`, and its corrected current raw SHA-256 is `B64D4D409ADBB9B2486983A72CA9246860EECBE39CEF18EC6DB1A6B943CEC6CF`.

The independent baseline `hoi4.probability_inspect` returned `no_weighted_surfaces`, zero candidates, and no evaluable `scenarioSet`. The post-edit inspection of `common/mtth/021_random_civil_war_mtth.txt` with adapter `event_mean_time_to_happen` and `refresh: true` again returned `no_weighted_surfaces`, zero candidates, MCP source revision `12aed2f96986abc6968c1b1416792d54fcfced2a7494035f1921dc247853242b`, MCP source hash `090cf4c0e32cde8b8b04c1f4e7b92e74179b4e17ded2ad7f10450cc05fd6e102`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94137270bff638c00b11baa68701325c76e1b72f2dd493540a731d776d18289b/83059387fd717571a43fe6dd2b10666d4cca9db00bdb539569b5c975ec2c8409/probability-inspect-090cf4c0e32c.json`. MCP hashes are not asserted to be raw-byte hashes.

The focused post-edit `hoi4.event_inspect` trace for `chaosx.nr21.11` returned `EVENT_INSPECTED_PARTIAL`, revision `02aadd003a66d42965ee451ee17108816105638af9ec6f0a31e9ffaa4138eafb`, graph hash `65d862ddd1a7893bfede856be54280246099dc7c95c67203da75673e889a9695`, zero expanded helpers and zero blocking diagnostics. Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f5db9b7b5a5cc0311f9986c12f6f63c309158e1b01204ecbd1243bb791f43ff/062588c64fe003e5c8da8cf3f614f31c8a29d3fd648cc5a3786e8bfc5febe052/event-trace-02aadd003a66.json`. This does not validate the new scripted triggers or compute a delay.

## Meaningful validation and open comparison gate

The fixed-slot search over the three owned gameplay files found no old secondary-front flag or Event 006 route-ready read and only the deliberate `clear_variable = random_civil_war_secondary_actor_scope`. The corrected Event 006 search finds `random_civil_war_event6_front_active` at successor-trigger lines 20 and 62 as ordinary-successor exclusions and line 174 as the evolution live-front role gate; it finds no `random_civil_war_event6_secondary_origin` gate in the owned consumers. Parent-source role writers set `random_civil_war_event6_front_active` for the secondary actor at line 4450 and primary opening actor at line 4580, while `random_civil_war_event6_secondary_origin` is only set in the secondary path at line 4452. The successor roster requires same-index actor, crisis, and active-status receipts plus actor/front ID, role, and host proof. No array being traversed is removed or resized. The MTTH base/factor sequence matches the saved pre-edit snapshot exactly. Vanilla documents `any_of_scopes` and the `mtth:` variable pattern; the offline wiki and Event 021/Event 006 spec contracts were consulted.

The same-scenario `hoi4.probability_compare` gate is **unresolved and compare-required**. The connected adapter produced no baseline or post-edit candidate and no valid saved `scenarioSet`; a fabricated comparison or current-to-current comparison would not be evidence. `EVO1-01`, `EVO1-02`, `EVO2-01`, `EVO2-02`, `EVO3-01`, and `EVO3-02` still require an adapter-supported same-scenario comparison or a documented alternate exact engine route. Effective delay, selected-actor context in live campaigns, and save/load behavior were not validated here. The parent should request the separate read-only probability auditor to repeat the same-scenario gate when the route becomes evaluable and should retain this unresolved status meanwhile.

No fallback, fixed slot, per-crisis cap, relation redeclaration, or AI war-goal choice was introduced. The only intentional timing behavior change is that live registered participants, rather than stale route or secondary-slot flags, determine the actor-related factors.

## Parent-review correction

The first draft of `event021_evolution_has_active_event6_actor` used `random_civil_war_event6_secondary_origin`, which excluded the primary Event 006 opening actor despite the prior Evolution II condition using `random_civil_war_event6_front_active`. Parent review identified that mismatch. The corrected helper uses the live front-active role while retaining the same-crisis, registration, opposition, immediate-opponent, and current-war checks. The MTTH file and all coefficients are unchanged by this correction. The corrected trigger and matching MTTH contract documentation are the only files edited in this follow-up.

The post-correction `hoi4.probability_inspect` still returned `no_weighted_surfaces`, zero candidates, revision `da8b9074ac9ef42bffa059864254abaa1f73188399293c4619f75491cc0270a7`, and unchanged MCP source hash `090cf4c0e32cde8b8b04c1f4e7b92e74179b4e17ded2ad7f10450cc05fd6e102`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3127f441b2a65aa2bb6d429f7535f4493eb1fda4183c376a418461c7f9dee78/d1b35218721ba003ba4f4d1e8403a1bb15b2c7180459c61785c4378083e46cb2/probability-inspect-090cf4c0e32c.json`. The same-scenario compare gate remains unresolved because no evaluable scenario set was produced.
