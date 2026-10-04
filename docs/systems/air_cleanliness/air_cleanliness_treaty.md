# Air Cleanliness Treaty

## Current implementation boundary

The Air Cleanliness Treaty is a persistent severe-contamination diplomacy and Air Winter mitigation system. It forms at 75 percent Air Contamination when at least one eligible founder has been observed by the existing Air Winter state pass.

The implemented tranche contains:

- deterministic founder selection
- generation-bound invitations
- idempotent membership registration and removal
- treaty-owned opinion and embargo cleanup
- permanent violation memory
- non-periodic annex cleanup
- an atomic Global Cleaning Day project
- a country-targeted Joint Filter Convoy project
- a state relief route lasting up to six months that feeds the existing Air Winter pressure formula
- a secretariat-owned Verification Mission with three inspected-member responses
- an exact seven-day delayed verification result with durable country memory
- a Fallout pause receipt that ends operational projects while preserving treaty memory
- four treaty operations from baseline spec 02: the Shared Sampling Grid, Seed Archive Exchange, Evacuation Corridor, and naming a burner
- treaty memory carried into Fallout survivors: member recognition and cohesion, violator distrust, seed archive food, and a push toward military rule for named burners
- AI weights for joining, every project and operation, and every verification response

Pooled decontamination, member relief votes, and broader manually reviewed treaty event families remain unimplemented.

## Runtime owner

`air_contamination_monthly_update` remains the only global monthly Air Cleanliness coordinator. It calls `air_cleanliness_treaty_pre_winter_pulse` before the existing state pass and `air_cleanliness_treaty_host_pulse` afterward. The pre-pass removes invalid routes before winter pressure is calculated. The post-pass records `global.date`, reconciles current membership, and uses only bounded arrays.

The treaty does not add an `on_monthly`, `on_daily`, or other periodic on action. The treaty section of `common/on_actions/fallout_consolidated_on_actions.txt` contains only `on_annex`, where ROOT is the annexer and FROM is the annexed country. Annex cleanup is disabled during Fallout transition and Fallout so the world rewrite cannot fire treaty reports or elect transient founders.

## Persistent ledgers

The principal scope arrays are:

- `global.air_cleanliness_treaty_members`
- `global.air_cleanliness_treaty_violators`
- `global.air_cleanliness_treaty_relief_states`
- `global.air_cleanliness_treaty_filter_convoy_donors`
- `global.air_cleanliness_treaty_active_inspectors`

Mutation queues are separate from the arrays they repair:

- `global.air_cleanliness_treaty_member_removals`
- `global.air_cleanliness_treaty_violation_queue`
- `global.air_cleanliness_treaty_route_removals`
- `global.air_cleanliness_treaty_filter_convoy_cancellations`
- `global.air_cleanliness_treaty_verification_cancellations`

The code never removes a country or state while iterating the same registry. It first records the scope in the appropriate work queue and mutates the source registry during a second loop.

## Formation and invitations

At or above `constant:air_contamination_threshold_bp.winter_75`, the host examines `global.air_winter_registered_countries`. It chooses the eligible founder with the lowest live country id. No random country selector or world-country scan is used.

Formation increments `global.air_cleanliness_treaty_generation`, registers the founder, stores `air_cleanliness_treaty_founder`, fires `chaosx_contamination.7` and `.10`, and issues the first invitation set.

Each observed country stores `air_cleanliness_treaty_invitation_attempt_generation` before the delayed event command is emitted. The invitation has a thirty-day pending window and a two-day delivery delay. The terminal generation receipt is written only when the event opens. A decline or completed invitation prevents another offer during the same treaty generation. A delivery that fails because the founder or recipient is temporarily invalid can be tried again on a later ninety-day bounded scan.

Event `chaosx_contamination.9` validates the current generation and persistent founder before opening. Acceptance calls `air_cleanliness_treaty_register_member`. It does not set a membership flag directly.

## Membership and sanctions

Registration sets the current and historical membership flags, adds one country-scope array entry, applies mutual cooperation only against current members, and clears treaty-owned embargo residue between members. Opinion edges remove the treaty-owned modifier before adding its one current instance. Schema reconstruction routes through the same edge helpers, so restored member and violator arrays restore their permanent opinions and native embargo ownership without stacking duplicate treaty modifiers.

A new member also joins the active sanctions ledger against existing treaty violators. The native embargo helper records the Air Cleanliness Treaty as a separate relation owner. Removing treaty ownership breaks an engine embargo only when no condemnation, Great Embargo, external, or other tracked owner remains.

An unconventional-weapon hook calls the compatibility effect `air_cleanliness_treaty_on_unconventional_use`. Inspection refusal calls the same idempotent consequence transaction with a distinct short-lived cause flag. A current member is removed once, added to the violator registry once, marked with `air_cleanliness_treaty_betrayal_memory`, stripped of active relief routes, and sanctioned only by current members. The unconventional-weapon news report can fire only for the weapon cause and only once for that country. Refusal retains its separate inspection memory and uses the verification result report.

Opinion modifiers are permanent while their lifecycle edge exists. Member departure removes mutual cooperation and the departing country's treaty sanctions. Annexation removes the absent country from live registries while preserving its betrayal flag for a later return.

## Global Cleaning Day

`air_cleanliness_global_cleaning_day` is a forty-five-day atomic project. Air Contamination must be above the project floor and below the irreversible boundary when work begins. The sponsor and at least one other signatory must remain live members through completion, and the sponsor must possess the required support equipment, convoys, and available civilian factories at the start. Crossing the irreversible boundary or falling below the full one-hundred-basis-point result cancels the project before it can enter a clamped reduction path.

Equipment is removed at project start. A global transaction number, a sponsor receipt, a generation receipt, a global lock, and a persistent sponsor target prevent concurrent starts and duplicate completion. Successful completion reduces Air Contamination by one hundred basis points, starts a one-hundred-eighty-day cooldown, and fires `chaosx_contamination.11`.

Cancellation releases every lock and receipt. Equipment already issued from depots is not refunded.

## Joint Filter Convoy

`air_cleanliness_joint_filter_convoy` is a targeted country decision backed by `target_array = global.air_cleanliness_treaty_members`. The decision contract is ROOT as donor and FROM as recipient.

The recipient must retain a designated priority state that is:

- a valid Air Winter state
- at Phase 3 or worse
- owned and controlled by the recipient
- still marked as the recipient's priority state
- free of another active or reserved treaty route

The donor and recipient must be distinct live members and cannot be at war. The donor pays support equipment and convoys at dispatch and reserves civilian factories for twenty-one days. The donor enters a dedicated active-project registry. The selected state stores the donor, recipient, treaty generation, and reservation flag. Ownership, control, membership, generation, and war status are checked again before arrival.

Arrival applies existing Air Winter response values for filters and clinic sheltering. It reduces exposure and disease pressure, improves adaptation, shelter, and recovery, normalizes the state ledger, and recalculates `air_winter_survival_value`. It also sets `air_winter_relief_route` for one hundred eighty days. The existing Air Winter pressure calculator subtracts `constant:air_winter_pressure.relief_route` while that flag remains active.

Active route states are held in a bounded registry. A route is removed before monthly winter pressure if its timed flag expires, the owner or controller changes, either country leaves the treaty, either country violates the treaty, the treaty generation changes, or the two countries enter a war. Membership removal, dissolution, annexation, and Fallout also cancel active donor projects and release exact state reservations through the dedicated donor registry.

The Air Winter mapmode displays whether the selected state currently has a treaty filter route.

## Verification Mission

`air_cleanliness_treaty_verification_mission` is a targeted country decision backed by the bounded member array. ROOT is the current treaty founder and secretariat. FROM is the inspected member. Restricting dispatch authority to the current secretariat permits only one active verification file at a time and prevents every member pair from becoming a daily decision target.

The mission requires two distinct live members at peace with each other. The subject cannot already be reserved by another inspection and cannot have completed a response during the previous one hundred eighty days. The secretariat commits sixty support equipment and five convoys, reserves one civilian factory for fourteen days, and enters a ninety-day dispatch cooldown when the mission begins. Equipment is not refunded after a broken route.

The travelling phase stores the treaty generation, a monotonic transaction number, the inspector, and the subject on both countries. The secretariat is held in `global.air_cleanliness_treaty_active_inspectors`. When travel completes, event `chaosx_air_treaty.6` gives the inspected government three responses:

- full facility access costs thirty support equipment and five trains
- certified records without facility access cost twelve support equipment and two trains
- refusal costs no equipment and creates an inspection dispute

The response is stored before hidden dispatcher `chaosx_air_treaty.9` is issued to the secretariat with an exact seven-day delay. On that day it opens result report `chaosx_air_treaty.7` only for the matching live transaction. Invalid delayed receipts are cleared immediately. If stores change while the response event is open, report `chaosx_air_treaty.8` preserves the request, recounts the depots, and reopens only the choices that can still be paid. Full access gives current members a decaying twenty-point diplomatic opinion benefit for up to twelve months. Records without access give a decaying fifteen-point penalty for up to nine months. Refusal gives a decaying forty-point penalty for up to eighteen months and then uses the existing treaty violation path to expel the member, revoke relief access, apply the standing violator opinion penalty, and register treaty-owned embargoes. The refusal memory is distinct from unconventional-weapon use and does not fire the weapon-use news report.

The chain does not change Air Contamination, any Air Winter tuning formula, survival grading, exposure, deaths, adaptation, Fallout eligibility, or Fallout grading. Refusal can remove an existing treaty relief route through the accepted violation consequence, so the state loses that route's ordinary pressure reduction. The permanent flags and last-partner, last-date, and last-outcome variables are scheduler memory for later manually reviewed treaty events.

Monthly reconciliation inspects only the active-inspector array. Membership loss, founder succession, war between the pair, transaction drift, annexation, dissolution, schema migration, and Fallout release the exact paired receipts through a separate cancellation queue. Timed cooldown and recency flags and completed historical memory survive operational cleanup.

## Treaty operations

The four operations from the baseline spec 02 treaty table are timed decisions in `air_cleanliness_treaty_category`. Every number lives in `air_cleanliness_treaty_operation`, `air_cleanliness_treaty_operation_ai`, and `fallout_treaty_memory` in `common/script_constants/fallout_consolidated_constants.txt`, and the localisation reads those constants directly.

They share one lifecycle:

1. The start effect re-checks the full affordability and target gate, pays every equipment cost once, and records the sponsor's receipt (an active flag, the target, and the treaty generation).
2. The decision's `cancel_trigger` re-validates the receipt every day. Treaty dissolution, membership loss, war between the pair, a generation change, and the Fallout transition all cancel through the operation's cancel effect, which sends report `chaosx_air_treaty.14` with an operation-specific description (no report is sent once the Fallout transition has begun). Equipment already sent is not refunded.
3. The `remove_effect` re-validates once more and applies the result, or cancels.
4. Locks shared with other countries (the global grid lock, the evacuation source and receiving states, and the burner's pending flag) are timed flags that outlive the operation by `reservation_slack_days`, so an annexed sponsor can never leave a permanent lock. `air_cleanliness_treaty_handle_annexed_country` also releases an annexed sponsor's operation receipts and locks at once, without a withdrawal report, so a restored tag starts with no stale operation.

Costs use `custom_cost_trigger` and `custom_cost_text` with texticons; the same affordability trigger gates `available`.

### Shared Sampling Grid

`air_cleanliness_treaty_shared_sampling_grid` needs at least `sampling_grid_minimum_members` live members and no grid being built, running, or cooling down. The sponsor pays support equipment and reserves civilian factories for the build. On completion every live member receives `chaosx_air_treaty.10`, and for `sampling_grid_active_days` the Air Winter mapmode treats every member as having an atmospheric office (likely phase next season, trend, and local fallout for every state). Members with their own atmospheric office also get terminal modelling, the possible Fallout classification. The changed triggers are `air_winter_mapmode_player_has_atmospheric_office` and `air_winter_mapmode_player_has_terminal_modelling`. A new grid can start `sampling_grid_cooldown_days` after the old one goes dark.

### Seed Archive Exchange

`air_cleanliness_treaty_seed_archive_exchange` targets another live member. The donor must own and control a breadbasket (a pastoral or rural Air Winter state whose food reserve is at least `seed_archive_breadbasket_food_reserve`) or a seed vault (a state with `air_winter_greenhouse_refuge`). On completion every Air Winter state the recipient owns and controls gains `seed_archive_food_reserve_gain` food reserve, its ledger is normalized, and its survival value is recalculated. Report `chaosx_air_treaty.11` goes to the recipient. Both countries keep `air_cleanliness_treaty_seed_archive_memory`. The donor waits `seed_archive_cooldown_days` before the next shipment and the recipient cannot receive another for the same period.

### Evacuation Corridor

`air_cleanliness_treaty_evacuation_corridor` targets another live member whose emergency priority state is at Phase 4 or worse, holds at least `evacuation_minimum_source_population_k` thousand people, and borders a state the sponsor owns and controls that is below Phase 4 and under the Air Winter refugee pressure ceiling. The receiving state is chosen when the corridor opens: the sponsor's designated reception state when it borders the source, otherwise the bordering state with the most shelter capacity. Both states are reserved for the corridor's duration.

On completion the request is `evacuation_population_share` of the source population, capped at `evacuation_capacity_share` of the receiver's population. The source loses that many people through `apply_exact_state_civilian_population_loss` above an `evacuation_protected_source_k` floor, with no Deaths record because nobody dies on the corridor. The measured debit is added to the receiving state and the arrival is read back from its population. Refugee pressure rises by `evacuation_receiver_pressure_gain` in the receiver and falls by `evacuation_source_pressure_relief` in the source, and both ledgers recalculate their survival value. Reports `chaosx_air_treaty.12` (sponsor) and `.13` (recipient) name the states and the number of people. A corridor that moves nobody is reported as withdrawn.

The corridor follows the Air Winter island-refugee transfer contract instead of the migration cohort transfer, because the migration transfer requires a live migration cohort row, a reception front, and a food-safety projection that a one-off treaty relocation does not have.

### Naming a burner

`air_cleanliness_treaty_sanction_burners` targets countries in the Condemnation registry `global.condemnation_targets`. A target qualifies when it carries the 180-day `condemnation_recent_use` flag, its chemical, biological, and nuclear Condemnation together reach `sanction_severe_condemnation`, it is not a treaty member, and it is not already a treaty violator. The sponsor pays political power through the native cost row and spends `sanction_duration_days` assembling the case.

On completion the target gains Condemnation through `condemnation_add_source` (public, major, observer-report context), is banned from membership, and enters the treaty violator ledger through `air_cleanliness_treaty_register_observed_violator`. Every live member, and every later member, applies the violator opinion penalty and a treaty-owned embargo. The target receives `chaosx_air_treaty.15` and keeps `air_cleanliness_treaty_sanctioned_burner`, which makes it eligible for the Warlord Command government during the Fallout classification even without an active war. The sponsor waits `sanction_cooldown_days` before naming another burner.

### Fallout memory

`fallout_treaty_apply_survivor_memory` runs once per Fallout generation inside each registry country's Ash-week orientation step:

- a country with `air_cleanliness_treaty_banned` loses `violator_recognition` Recognition
- otherwise a country with `air_cleanliness_treaty_ever_member` gains `member_recognition` Recognition and `member_cohesion` Cohesion
- a country with the seed archive memory gains `seed_archive_food` Food

The values change the survivor's current resource entries and are clamped to the survival range. The orientation closure report `chaosx.fallout.82` lists each memory that applied.

## AI behavior

Invitation AI weighs government, major status, unconventional stockpiles, prior weapon use, and war with the founder.

Cleaning Day AI weighs government, war strain, and very high Air Contamination. Filter Convoy AI has a zero-validity gate through the decision availability trigger. It then weighs donor capacity, war strain, target phase, and critical target survival value.

Treaty operation AI follows the spec 02 AI table. Democratic members and the secretariat favor the sampling grid, and war strain lowers it. Seed archive AI rises when the donor holds a seed vault and when the recipient's priority state is short of food. Evacuation AI rises for democratic sponsors and for Phase 5 or worse sources, and falls when every bordering state the sponsor could use has little shelter, which keeps island and small members from taking refugees they cannot house. Naming a burner is favored by democracies, disfavored by fascist members and against neighbors, and never chosen against a faction partner, overlord, or subject.

Verification dispatch AI weighs secretariat government, war strain, the subject's inspection history, prior refusal, and fascist administration. The inspected government has separate AI weights for full access, records-only access, and refusal. Government, war strain, available equipment, and prior refusal shape the response. Every AI value is stored in the treaty section of `common/script_constants/fallout_consolidated_constants.txt` (consolidated from `air_cleanliness_treaty_constants.txt`).

## Files

- `common/script_constants/fallout_consolidated_constants.txt`, treaty section consolidated from `air_cleanliness_treaty_constants.txt`
- `common/scripted_triggers/fallout_consolidated_triggers.txt`, treaty section consolidated from `air_cleanliness_treaty_triggers.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`, treaty section consolidated from `air_cleanliness_treaty_effects.txt`, with the winter and Fallout world-end sections consolidated from `air_cleanliness_winter_effects.txt` and `fallout_world_end_effects.txt`
- `common/scripted_effects/chaos_meter_effects.txt`
- `common/scripted_effects/chaosx_welcome_effects.txt`
- `common/decisions/fallout_consolidated_decisions.txt`, treaty section consolidated from `air_cleanliness_treaty_decisions.txt`
- `common/decisions/categories/fallout_consolidated_categories.txt`, treaty section consolidated from `air_cleanliness_treaty_categories.txt`
- `common/on_actions/fallout_consolidated_on_actions.txt`, treaty section consolidated from `air_cleanliness_treaty_on_actions.txt`
- `events/fallout_world_end_events.txt`, treaty section consolidated from `air_cleanliness_treaty_events.txt`
- `events/chemical_warfare_events.txt`
- `common/opinion_modifiers/air_contamination_opinion_modifiers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- `localisation/english/_chaosx_events_l_english.yml`
- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/chaosx_map_modes_l_english.yml`
- `localisation/english/chaosx_modifiers_l_english.yml`
- `localisation/english/fallout_consolidated_l_english.yml`, treaty operations, their reports, and the Fallout memory tooltips

## Icons and event images

No new visual asset is required by this tranche.

- Treaty category: `GFX_decision_category_contamination_defense`, defined in `interface/chaosx_decisions.gfx`, with texture `gfx/interface/decisions/decision_category_contamination_defense.dds`
- Treaty projects: `GFX_decision_generic_operation`, defined by vanilla `interface/decisions.gfx`, with texture `gfx/interface/decisions/decision_generic_operation.dds`
- Formation, invitation, and succession reports: vanilla `GFX_report_event_generic_sign_treaty2`
- Cleaning Day report: vanilla `GFX_report_event_generic_sign_treaty1`
- Violation report: Fallout-independent Chaos Redux sprite `GFX_news_event_chaosx_cbw_doom`
- Convoy reports: vanilla `GFX_report_event_generic_factory`
- Verification request: vanilla `GFX_report_event_generic_sign_treaty2`
- Verification result: vanilla `GFX_report_event_generic_sign_treaty1`
- Verification depot recount: vanilla `GFX_report_event_generic_factory`
- Shared Sampling Grid decision: `GFX_decision_air_winter_samplers`; grid report: vanilla `GFX_report_event_generic_sign_treaty2`
- Seed Archive Exchange decision: `GFX_decision_air_winter_crop_trials`; delivery report: `GFX_report_event_air_winter_phase_2`
- Evacuation Corridor decision: `GFX_decision_air_winter_controlled_evacuation`; arrival and departure reports: `GFX_report_event_fallout_refugee_train`
- Naming a burner decision: vanilla `GFX_decision_generic_break_treaty`; listed-country report: vanilla `GFX_report_event_generic_sign_treaty1`
- Withdrawn operation report: vanilla `GFX_report_event_generic_sign_treaty1`

The Air Winter and Fallout sprites above are already registered in the Fallout interface files. A future dedicated treaty icon package should use a treaty-owned directory and stable sprite ids before art is commissioned. That package is not required for the implemented decisions to render.

## Proof and runtime boundary

Static engine proof is recorded in `docs/plans/air_cleanliness_fallout_plans/AIR_CLEANLINESS_TREATY_LIFECYCLE_PROOF.md` and `docs/plans/air_cleanliness_fallout_plans/AIR_CLEANLINESS_TREATY_INSPECTION_PROOF.md`.

Hearts of Iron IV was not launched. Targeted decision persistence, delayed invitation and verification delivery, regular event-target retention, mapmode text rendering, native embargo behavior, Fallout pause timing, and save reconstruction remain runtime observation gates. No runtime pass is claimed.

## Future plans

1. Add pooled state decontamination through the existing Air Winter decontamination project and formula.
2. Add member relief vote transactions so the secretariat can direct convoys and corridors toward the worst-hit member.
3. Let a named burner answer the listing through a response event (defiance, quiet compliance, or a pledge) that interacts with the Condemnation compliance paths.
4. Carry inspection outcomes into Fallout successors as a separate memory beside membership and violation.
5. Give the seed archive a post-Fallout greenhouse decision for survivors that hold the archive memory.
