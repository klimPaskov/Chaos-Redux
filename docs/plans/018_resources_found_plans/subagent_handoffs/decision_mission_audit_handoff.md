# Event 018 Decision and Mission Audit Handoff

## Result

The Event 018 decision and mission surface passed the final decision/mission audit after bounded corrective patches. All 100 priced decisions now show an exact rounded payment and the correct duration or immediate commitment before selection. Activation uses the same calculator, requires an exact cache match, rechecks every displayed resource, and pays those exact rounded values. Ten missions remain player-facing. The eight MTTH evolution clocks and their one-day reschedule mission retain their existing field locks, MTTH durations, cancellation, and timeout callbacks under a permanently hidden category.

No fallback, placeholder, omitted route, or simplified substitute was used.

## Required references used

- Offline wiki: `Decision modding - Hearts of Iron 4 Wiki.md`, especially the mission note that mission-level `visible` has no effect and the category `visible` contract; plus Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Idea modding, and AI modding.
- Official game documentation: `documentation/decisions/_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, `documentation/triggers_documentation.md`, and `documentation/effects_documentation.md`.
- Vanilla activated-mission precedent: `common/decisions/CHI_warlord_decisions.txt` uses `allowed = { always = no }` missions explicitly activated from effects; the Event 018 clocks retain that engine-native activation pattern. Vanilla decision-category files provide the category-level `visible`/`visible_when_empty` rendering contract. Event 018 adds the stricter always-hidden category because the wiki explicitly documents that mission `visible` is ignored.

## Exact preview and payment ledger

- Added 13 cost rows: nine selected-field profiles, remote diplomacy, cave, anti-cave, and remote security.
- Added 16 duration rows: ten selected-field base-duration classes and six remote classes.
- The shared calculator now rounds and zero-clamps political power, command power, army experience, manpower, civilian and military factory requirements, infantry/support/anti-tank equipment, trucks, trains, convoys, fuel, and duration before either display or payment.
- Fuel is copied only after rounding. Convoys participate in clear, scale, round, cache, affordability, parity, and payment.
- Every activation maps its real family/profile/base duration to a cost and duration row, then requires exact equality between fresh calculator output and the cached rows before payment.
- Five category-local refresh decisions remain visible only when the ledger is stale and the project queue is idle. Their AI weight is `resources_found_decision_ai.critical`.
- Direct initialization/refresh occurs after Event `.1`, Event `.2`, DHO setup, ordinary-country cave-war registration, foreign-interest actor selection, and previous/next field selection.
- The cache context matches country scale tier, war state, selected state, exact excavation/breach/disturbance/safety values, infrastructure band, and valid-contract state. Priced actions are hidden when that context changes, while the refresh action remains visible.
- The 100-decision mapping audit returned `PRICED=100`, `MISMATCH=0`; all 100 custom affordability triggers matched their actual profile/family (`TRIGGERS=100`, `MISMATCH=0`).
- Forty live exact-cost localisation keys are referenced. Base, `_blocked`, and `_tooltip` variants all exist (`MISSING=0`). The obsolete generic “Scaled” cost text has no remaining definition or reference.
- Immediate field actions are labelled immediate. The frontier objective copies its displayed computed duration into the mission. The border-war action separately previews its exact 240-day conflict limit. Contract, commission, and recapture follow-on windows display their exact stored constants.

## Mission ownership and callbacks

| Mission family | Immutable owner/target evidence |
| --- | --- |
| Field/trade/containment projects | `resources_found_active_project_field`, kind, family, profile, exact days |
| Contract term | locked field plus locked partner; state partner must still equal the launch partner |
| Frontier corridor | stored owner and claimant states; outcome no longer follows GUI selection |
| Commission observation | `resources_found_commission_observation_field`; success/failure both rebind that state |
| Border war | stored owner state, claimant state, and claimant country; callbacks `.25`–`.28` rebind the owner state before saving the event target |
| Cave/anti-cave target projects | `resources_found_active_response_state` or locked partner |
| Anchor recapture | `resources_found_anchor_recapture_state`; both outcome paths clear state and duration |

- Partner-targeted trade projects cancel if the launch partner disappears or becomes invalid.
- Contract missions cancel if the current state partner is not exactly the locked partner.
- Frontier and border callbacks no longer depend on the mutable selected-field pointer.
- Burrow completion uses `resources_found_transport_target_state`; no generic `resources_found_marked_target_state` reference remains in decision-owned files.
- Ten rendered missions have both name and description localisation (`VISIBLE_LOC_MISSING=0`).
- All nine evolution/reschedule missions resolve only to `resources_found_hidden_clock_category`; no visible category owns one. The hidden category has `visible = { always = no }` and `visible_when_empty = no`, and needs no rendered localisation or art.

## Cave denial, cleanup, and reconstruction

- Resource denial remains prepared through interrupted activation attempts.
- Each attempt receives the tuned +30-day delay. The -3 capacity penalty is applied on the successful activation path, clamped to zero, and the prepared state/penalty are then cleared. Beginning an attempt no longer consumes it.
- Removed the stale `resources_found_cave_resource_denied` total-exclusion check, so accepted denial reduces capacity rather than making the state permanently ineligible.
- Terminal defeat clears persistent global target `resources_found_cave_spawn_state` alongside the other cave targets.
- `resources_found_deep_survey_complete` is now the single deeper-survey completion marker; the mismatched setter no longer exists.
- Successful `seal_access_network` completion clears `resources_found_unsealed_nest`.
- Reconstruction Event `.99` remains one-shot: readiness requires global-defeat eligibility, contributor evidence, at least three cleanup contributions, no remaining cleanup state, and no live threat; `.99` immediately sets `resources_found_reconstruction_choice_presented`, and reconstruction completion does not call the offer helper.

## Ordinary-country AI acceptance

- Preview initialization cannot deadlock cave-war AI: `resources_found_register_ordinary_country_cave_war` refreshes the ledger, while the category recovery decision has critical AI weight if context later changes.
- Emergency anti-armor contracts: visible at war with DHO while not prepared; exact anti-cave affordability gate; AI base `critical`, plus `critical` for a major and `urgent` while at war with DHO.
- Threatened-state denial: exact anti-cave affordability gate, owned-and-controlled resource state, adjacent DHO control, and no prior prepared denial; AI base `high`, plus `critical` for the threatened adjacency.
- Field hard-attack aid request: public breach, unaccepted weapons, non-major, exact diplomacy affordability; AI base `high`, plus `urgent` for a non-major. Completion grants anti-tank equipment and countermeasure preparation before Event `.65` presents the aid package.
- Anti-cave aid to another belligerent: exact anti-cave affordability and a live target at war with DHO; AI base `medium`, plus `urgent` for a major. Completion grants anti-tank/support equipment and `resources_found_anti_armor_prepared` to the locked recipient.
- Ordinary cave-war registration queues Event `.83` once after the named 14-day analysis delay; the queued/presented flags prevent duplicates and the event remains deliverable if the war ends first. Event `.83` records the DHO analysis in immediate, then records piercing only from the anti-tank or armor response and hostile-air exposure only from the airpower response. Delaying defense records neither observation.

## Files changed in this audit

- `common/decisions/018_resources_found_decisions.txt`
- `common/decisions/categories/018_resources_found_categories.txt`
- `common/script_constants/018_resources_found_decision_constants.txt`
- `common/scripted_effects/018_resources_found_decision_effects.txt`
- `common/scripted_effects/018_resources_found_cave_effects.txt`
- `common/scripted_effects/018_resources_found_ui_effects.txt`
- `common/scripted_triggers/018_resources_found_decision_triggers.txt`
- `common/scripted_triggers/018_resources_found_triggers.txt`
- `events/018_random_resource.txt`
- `localisation/english/018_resources_found_decisions_l_english.yml`
- `docs/events/018_resources_found/overview.md`
- this handoff

## Meaningful validation evidence

- 100 priced decisions: exact cost/duration mapping `100/100`; trigger/profile mapping `100/100`.
- 40 referenced cost keys: all base, blocked, and tooltip variants present.
- 19 total missions: ten rendered/localised and nine confined to the hidden category.
- Denial search shows only prepared-state/penalty logic; the consumed flag and stale total-exclusion flag have no live use.
- No decision-owned generic cave target reference and no old deeper-test completion marker remain.
- The decision localisation file remains UTF-8 with BOM and contains no duplicate keys.
- All touched Event 018 script files have balanced blocks. These checks found no remaining blocking issue.

## Remaining risks

No known implementation blocker remains. Final integration, audit aggregation, staging, and commit remain parent-owned because the Event 018 files are shared with concurrent parent and asset/error-log work.
