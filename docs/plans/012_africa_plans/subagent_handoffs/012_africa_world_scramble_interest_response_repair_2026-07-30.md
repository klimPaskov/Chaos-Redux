# Event 012 Scramble Interest and Response Repair Handoff

Date: 2026-07-30

Owner: `/root/africa_world_w2_w4_integrator`

Parent handoff: `/root`

Scope: the existing Event 12 world-order participant census, response effects, coalition decisions, response events/localisation, constants, and cleanup only. AI64 files, super-event readiness, country tags, models, fallback wars, and recurring on-actions were not touched.

## Implementation state

The one-time participant census remains owned by `africa_initialize_scramble_and_world_packages`. It is capped by `constant:africa_scramble_response.participant_census_cap`, sets `africa_scramble_interest_census_complete`, and admits no new periodic scan.

Each frozen participant is classified once into explicit host arrays and participant flags for former colonial relationship, ideological rival, resource-nationalisation exposure, fear of a complete external continental unifier, and South Africa or Allied relationship. The host arrays are `africa_scramble_former_colonial_interests`, `africa_scramble_ideological_rivals`, `africa_scramble_resource_exposure_interests`, `africa_scramble_continent_unifier_fears`, and `africa_scramble_south_africa_allied_contacts`.

The response tracks now have concrete material effects. Recognition grants political power, infantry equipment, convoys, and host stability while leaving the coalition. Conditional recognition spends political power and supplies a negotiated convoy concession to both sides. Sanctions grant domestic political power and war support while imposing host stability loss. Ultimatums spend political power, grant war support and military stockpiles, and increase host war pressure. Expedition members each receive infantry equipment, support equipment, convoys, and war support before the existing `topple_government` intervention war is declared. The host pays a guarded war-support loss and records defence material demand. Ratified or deferred aftermath closure grants reconstruction equipment, support equipment, convoys, stability, war support, and political power once.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `africa_scramble_classify_participant_interests` | Frozen participant; Event 12 host target and existing flags/tags | Writes the five participant class flags, host class arrays, and host class counters | `africa_scramble_register_participant` during the one-time census |
| `africa_scramble_enlist_coalition_member` | Frozen participant; host coalition counter and six-member cap | Sets participant membership, appends `africa_scramble_coalition_members`, increments host count, or sets the capped flag | Sanctions and ultimatum response effects |
| `africa_scramble_remove_coalition_member` | Frozen participant with membership flag | Clears membership, removes the participant from the host array, and decrements the guarded host counter | Recognition, full/partial action 81/84 results, roster cleanup |
| `africa_scramble_apply_class_response_consequences` | Frozen participant class flags | Adds class pressure and integration burden, records host class response flags, and clamps host pressure | All four response effects |
| `africa_scramble_apply_aftermath_materials` | Event 12 host; guarded by aftermath material flag | One-time reconstruction and political settlement package | Ratified aftermath and Africa-only docket close |
| `africa_scramble_cleanup_response_roster` | Event 12 host and frozen participant array | Clears transient participant, class, response, planner, and coalition state; clears all arrays; resets class/coalition counters; leaves host outcome summary flags | Settlement, deferred close, and defeat paths |

The expedition path now iterates `africa_scramble_coalition_members` with `for_each_scope_loop`, checks every planner against the host and the actor cap, grants expedition matériel, and marks every eligible declarer as an intervention actor. The first launch queues `africa_world_order.8` and the existing news event; no random world planner scan remains in this response helper.

## Constants and tuning

`africa_scramble_response` in `common/script_constants/012_africa_world_order_constants.txt` owns the census cap (32), coalition cap (6), response equipment/convoy amounts, political-power/stability/war-support changes, expedition host loss, aftermath reconstruction package, and the class pressure/integration-burden increments. The existing `africa_world_order` phase/cost constants remain the source for action costs and deadlines.

## Decisions, events, and localisation

`africa_select_scramble_coalition_member_target` targets the explicit coalition array and uses the same bounded Event 12 activation and target usability checks as the participant selector. `africa_world_order.1` retains the `africa_ai_classify_scramble_response` hook and now reads the frozen class flags in AI chance modifiers. `africa_world_order.8` reports the bounded multi-member expedition response. Localisation updates cover the five interest classes, the coalition selector, and the new war report; the existing Scramble picture contracts are reused and no new icon or image asset is required.

## Cleanup and persistence

The host class flags and response counters remain available for the settlement summary while the docket is open. After the settlement, deferred close, or defeat log is queued, cleanup clears participant flags (including the five frozen classes and active response markers), planner/leader/war-actor flags, target arrays, coalition membership, class arrays, and class/coalition counters. Host outcome counters and final host summary flags are preserved. The cleanup helper is idempotent through `africa_scramble_response_roster_cleaned`.

## Validation performed

- Read the required repository, event, decisions, and subagent skills plus the offline Paradox wiki and vanilla effects documentation for arrays, `for_each_scope_loop`, event targets, and equipment effects before editing.
- Confirmed balanced braces for all seven touched script/event files and no unsupported `<=` or `>=` operators in the touched Event 12 surfaces.
- Confirmed no new `on_daily`, `on_weekly`, or `on_monthly` scan and no `random_country` remains in `africa_scramble_launch_expedition_if_unresolved`; other `random_country` uses in the same file belong to pre-existing package/world-order helpers.
- Confirmed every new helper, class array, coalition array, selector, event ID, and localisation key has cross-file references.
- Confirmed `git diff --name-only` contains zero `012_africa_ai` files.
- Read-only `hoi4.event_inspect` scans were run for `africa_world_order.1` and `.8`; authoritative artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a533d055dd72bf28bfc7eba556799c49e61baac05f65597fa3166166bbd5b4d4/e8b0f80c5fa4e7865acd722b9db893af3d987578f1de2fdd137a25a6cbdad5d8/event-scan-a49ed592e16f.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f474d41b05d899beb8c6df874851eb9c40476bcd14c2fec5014e0b10c1f9f02b/ba2d13142f4ee5175277c7a43213be3afd5e397283615b34560bb378be1becea/event-scan-a49ed592e16f.json`.
- Static validation only; the HOI4 executable was not launched and no live save or consumer validation was performed.

The MCP scans returned `EVENT_INSPECTED_PARTIAL` with `MCP_INLINE_FILES_TRUNCATED`; workspace-wide helper projection and lifecycle analysis were deferred, so the linked artifacts are structural evidence rather than a complete engine lint.

## Limitations and follow-up

The expedition still uses Event 12's existing `topple_government` war type, which is the current treaty-enforcement war contract rather than a new fallback war. The classifier's former-colonial class uses the frozen original-tag/current-interest witness and does not invent historical tags. Existing AI64 profile classification remains the AI hook; this repair adds class-aware option weighting without changing AI64 implementation. No new assets, super-event readiness, world readiness, or external package implementation gates were added.

No commit was created per the parent request; the working tree also contains unrelated changes from other agents.
