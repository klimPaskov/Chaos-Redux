# Event 015 Utopia Manifesto: Repository Explorer Handoff

## Scope and inspection point

This is a read-only implementation map for replacing the disabled Event 15 placeholder with the accepted Utopia Manifesto package. It does not change gameplay, localisation, UI, art, audio, or the workbook.

The live repository was inspected at HEAD `b89d2e543` (`Update event catalog functional status labels`) while unrelated work was active. The required offline wiki core pages, the additional focus/country/autonomy/cosmetic-tag/achievement/interface/scripted-GUI/sound/division/state pages, relevant installed-game documentation, live Chaos Redux precedents, the complete Event 15 specification package, and the live workbook row were consulted.

The decisive repository fact is that Event 15 has three distinct layers which must not be confused:

1. **Current runtime state:** Event 15 is registered as fire-once but deliberately suppressed and represented by `events/015_placeholder.txt`.
2. **Recoverable historical baseline:** commit `0bce9e9a4` is the last tree before commit `ae2191ed1` removed the previous Utopia implementation.
3. **Accepted current design:** `docs/specs/015_utopia_manifesto_specs/` is substantially broader and uses a different five-route, four-value, stewardship, league, evolution, achievement, asset, and super-event contract. Historical code is therefore reference material, not the source of truth.

## Executive findings

- The live catalog wording is **Event 015 Placeholder**, not the older **World Tension Subsides** text described by the planning package. No live World Tension Subsides gameplay file remains.
- Event 15 already appears once in `global.fire_once_events`, but it is excluded from the active random pool, hard-blocked at dispatch, shown as unavailable in the Event Log, and omitted from the default-enabled reworked-event allowlist.
- The existing `chaosx.nr15.1` file is a hidden, no-op placeholder. It must be replaced by the visible accept/reject entry event while retaining the root ID.
- Super-event presentation slot **15 is not Event 15's slot**. It belongs to Soviet Collapse's **The Black Banner Returns** and must not be overwritten.
- The repository contains a large, tracked, orphaned visual package from the removed implementation: 36 achievement DDS files, 25 decision/category DDS files, 29 idea DDS files, 13 GUI DDS files, 2 event/news DDS files, and 60 flag TGAs. Most identifiers represent the removed design and do not satisfy the accepted asset matrix.
- There is no live reusable protected/replaceable-focus-tree registry. The accepted event cannot be safely enabled until that gate is implemented and populated conservatively.
- No live Event 15 gameplay package, focus tree, decisions, ideas, AI, faction package, scripted GUI, scripted localisation, event/evolution details, route identities, super-event, audio, documentation, or current achievement registry exists.
- The old event-owned files can be inspected or selectively recovered from `0bce9e9a4`. Shared files must never be restored from that commit; they must be edited against HEAD because Event 11, 14, 17, 18, the event log, super-event allocations, achievements, and settings infrastructure have changed since removal.

## Exact live Event 15 and stale-mapping inventory

### Runtime registration and dispatch

| File and current insertion point | Live state | Required Event 15 action |
| --- | --- | --- |
| `common/scripted_effects/chaosx_logic_effects.txt:171-190` | Line 179 registers `global.fire_once_events = 15` with the Utopian Manifesto comment. Classification is already Minor Fire-Once. | Retain exactly one fire-once entry. Prefer a new `constant:utopia_manifesto_event.id` only after constants exist. Do not add Event 15 to repeatable or cluster arrays. |
| `common/scripted_effects/chaosx_logic_effects.txt:508-567`, especially line 540 | `evaluate_random_event_active_pool_candidate` unconditionally excludes ID 15. | Replace the unconditional exclusion with `AND = { event_id = Event15; NOT = { utopia_manifesto_automatic_event_is_available = yes } }`, following Event 11/14/17/18 availability patterns. |
| `common/scripted_triggers/chaosx_settings_triggers.txt:10-26` | `event_log_event_is_reworked_default_enabled` includes 14 and 17 but omits 15. | Add Event 15 once so a newly initialized settings state treats the completed event as enabled. |
| `common/scripted_effects/chaosx_settings_effects.txt:4545-4660` | `fire_event_by_temp_id_no_cluster` initializes dispatch state and runs event-specific preflights. Lines 4657-4660 hard-set `event_single_fire_allowed = 0` for ID 15. | Replace the blocker with Event 15 preflight: clear/initialize ready state, choose and persist the safe actor, validate actor/context, and set `event_single_fire_allowed = 0` without consuming fire-once state if preparation fails. |
| `common/scripted_effects/chaosx_settings_effects.txt:4670-4717` | Specialized target dispatches precede the generic meta-dispatch at lines 4709-4716. | Dispatch `chaosx.nr15.1` in the prepared actor scope, as the removed implementation did. Do not fire the generic event in the settings-owner/root country when the selected recipient differs. |
| `common/scripted_effects/chaosx_settings_effects.txt:4719-4734` | Successful dispatch then calls fire-once bookkeeping. | Preserve this ordering. Failed preflight must exit before this block; human rejection intentionally consumes the event only after the entry event was legitimately dispatched. |
| `common/on_actions/chaosx_on_actions_system.txt:150-166` | The existing timer selects and dispatches a weighted random event. | No Event 15 periodic on-action is needed. Use the shared timer plus Event 15's preflight and target-bound delayed events. Do not add global daily/weekly/monthly iteration. |

### Event file, names, debug, settings, Event Log, and workbook

| File / key | Current live value | Required replacement |
| --- | --- | --- |
| `events/015_placeholder.txt:1-9` | Namespace `chaosx.nr15`; hidden, triggered-only, fire-once no-op `chaosx.nr15.1`. | Replace with the Event 15 event family. Root remains `chaosx.nr15.1`; entry must present the human accept/reject choice and force AI acceptance. |
| `localisation/english/chaosx_event_names_l_english.yml:17` | `chaosx.event_name.15: "Event 015 Placeholder"` | Final Event 15 catalog name, aligned with workbook and log. |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:81-82` | Debug event ID 15 maps to `chaosx.event_name.15`. | Mapping can remain; the name key must be final. Add Event 15-specific unavailability reason localisation through event-owned scripted localisation/debug helpers. |
| `common/scripted_localisation/chaosx_scripted_localisation_settings.txt:1686-1688` | Settings ID 15 maps to the shared name key. | Mapping can remain. |
| `common/scripted_localisation/chaosx_scripted_localisation_settings.txt:5687-5689` | Last-fired ID 15 maps to the shared name key. | Mapping can remain. |
| `common/scripted_effects/chaosx_events_log_effects.txt:178-370` | `events_log_set_default_actor_for_current_event` has actor branches for Event 11, 14, 17, 18, etc., but none for Event 15. | Add an Event 15 branch using the persisted selected/latest actor. The actor target must survive entry, evolutions, and tag/cosmetic changes and be cleaned only at terminal cleanup. |
| `common/scripted_effects/chaosx_events_log_effects.txt:3737-3742` | ID 15 always receives live weight `-1`. | Replace the unconditional rule with the same safe-availability trigger used by random selection/manual fire. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:947-955` | Evolution-event ID 15 maps only to the generic event name. | Retain the name branch and add five stage/type/detail branches for active and pre-fire evolution paths. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4442-4445` | Event detail ID 15 maps to `chaosx.events_log.window.event_details.event_015_unavailable`. | Replace with final Event 15 details and state/route-sensitive details where useful. |
| `localisation/english/chaosx_gui_l_english.yml:530` | The detail key says Event 015 is a disabled placeholder. | Remove/replace stale placeholder wording. Add final event/evolution details using in-world wording. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6861-6869` | History ID 15 maps to the generic name. | Retain and supply actor snapshot through shared log effects. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:8497-8505` | Cluster-member ID 15 maps to the generic name. | The generic name branch is harmless, but Event 15 must not be registered to any cluster. Do not add cluster detail content. |
| `localisation/english/chaosx_achievements_l_english.yml:550-551` | Empty reserved comment section for Event 15. | Populate only the 14 accepted stable achievement IDs and final wording. |
| `common/achievements/chaos_redux_achievements.txt` | No Event 15 entries. | Add all 14 accepted definitions after tracking/disqualifier flags are implemented. |
| `interface/chaosx_achievements.gfx` | No Event 15 sprites. | Add 14 completed/grey/not-eligible triplets after final DDS names are frozen. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, Events row 16 | ID 15, name `Event 015 Placeholder`, status `Reserved Disabled`, type `Placeholder`, and details stating no active systems. | Spreadsheet worker updates only after final in-game wording and identifiers stabilize. Details/evolution fields must match localisation. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx.inspect.ndjson` | Contains the same placeholder row. | Regenerate with the workbook through the repository's established inspection workflow after workbook update. |
| `docs/events/015_utopia_manifesto/overview.md` | Missing. | Create the canonical implementation document with mechanic flow, variables/flags, interactions, all icon/sprite paths, super-event/audio provenance, cleanup, validation, and future plans. |

There are no live `World Tension Subsides` strings outside the current planning/spec package. The accepted instruction to replace every stale World Tension Subsides mapping resolves in the current tree to replacing the placeholder surfaces above and avoiding resurrection of `events/015_world_tension_falls.txt` or its old localisation.

## Super-event and audio collision map

Super-event visible ID 15 is occupied and unrelated to Event 15:

- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:108-110` maps image slot 15 to `GFX_super_event_black_banner_returns`.
- The same file maps slot 15 title at `478-480`, quote at `719-721`, button at `960-962`, and description at `1201-1203`.
- `localisation/english/005_soviet_collapse_l_english.yml:1926-1929` owns `chaosx_super_event.15.{t,d,a,q}`.
- `sound/chaosx_sound.asset` owns the settings-scaled sound wrappers and `sound/005_soviet_collapse/super_event_15_black_banner_returns.wav`.
- `music/chaosx_super_event_music.txt:127-131` registers the 1.5-volume song.
- `sound/chaosx_sound.asset:92-97,447,1157-1199` owns the corresponding sound list, WAV, and volume variants.
- `localisation/english/chaosx_music_l_english.yml:92-97` and `music/chaosx_music_track_list.html:267-269` document the track.

At inspection, visible slots in use were `1-22`, `49-53`, `59-77`, and `82-84`. The next contiguous five-slot candidate was `85-89`, suitable if five route variants are implemented as separate visible IDs. Audio IDs in use were `1-15`, `17-18`, `28-50`, and `52-56`; `57` was the next simple free audio ID. These are observations, not reservations. Recheck and reserve atomically before writing constants because other event work is concurrent. One route-sensitive proclamation may also use one visible ID with dynamic selectors, but whichever model is chosen must provide all five accepted route variants and one uniquely licensed real track package.

## Historical recovery baseline and safe restore boundary

### Provenance

- `5483e20d3` initially implemented Event 15.
- Several follow-up commits adjusted availability, load errors, icon wiring, rewards, targeting, and focus layout.
- `0bce9e9a4` is the final repository tree immediately before removal.
- `ae2191ed1` (`Remove Utopia Manifesto implementation`) removed the gameplay package, docs/source assets/audio, shared wiring, and created `events/015_placeholder.txt`.
- `60853561d` later restored a subset of runtime visual files in a broad project snapshot, leaving them orphaned.

### Event-owned files recoverable for reference

The following files exist in `0bce9e9a4` and may be inspected or selectively restored into a scratch comparison. They must be reconciled with the accepted spec before use:

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/decisions/categories/015_utopia_manifesto_categories.txt`
- `common/ideas/015_utopia_manifesto_ideas.txt`
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- `common/opinion_modifiers/015_utopia_manifesto_opinion_modifiers.txt`
- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`
- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `events/015_utopia_manifesto.txt`
- `interface/015_utopia_manifesto.gfx`
- `interface/015_utopia_manifesto_ledger.gui`
- `localisation/english/015_utopia_manifesto_l_english.yml`
- `docs/events/015_utopia_manifesto/overview.md`
- historical Event 15 handoffs under `docs/plans/015_utopia_manifesto_plans/`
- historical source/processed animation packages under `docs/assets/015_utopia_manifesto/`
- historical super-event source/final audio and images under `docs/super_events/source_audio/015_utopia_manifesto/`, `gfx/super_events/015_utopia_manifesto/`, `music/`, and `sound/`.

The old package provides useful implementation fragments for weighted target preparation, actor-scoped dispatch, focus loading, state/country target storage, decision costs, units, GUI wiring, achievement tracking, and cleanup. It is not an acceptable wholesale restoration. Its public state used Need, Consent, Surplus, Overreach, Vocation Balance, Foreign Suspicion, and League Confidence; the accepted system permits only Need, Plenty, Concord, and Choice-versus-Assignment as the central public values. Its routes, final identities, achievements, events, evolutions, league model, stewardship model, assets, and two super-events do not match the current package.

### Shared files which must be integrated against HEAD

Do **not** check out or restore any historical version of these files:

- `common/achievements/chaos_redux_achievements.txt`
- `common/countries/cosmetic.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_triggers/chaosx_settings_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `interface/chaosx_achievements.gfx`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `music/chaosx_super_event_music.asset`
- `music/chaosx_super_event_music.txt`
- `sound/chaosx_sound.asset`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- shared super-event documentation.

The removal diff is still a useful insertion-point index. For example, the historical implementation added an Event 15 default-actor branch, replaced the ID 15 active-pool exclusion with an availability trigger, prepared an actor before dispatch, fired `.1` in that actor, added the default-enabled settings branch, and registered two super-event IDs. Reimplement those concepts against HEAD using current names and the accepted one-proclamation/five-variant contract.

## Orphaned current asset inventory

These files are tracked and present at current HEAD but have no live `.gfx`, `.gui`, gameplay, achievement, idea, decision, or cosmetic-tag registration. They require content/provenance review before reuse.

### Achievement DDS: 12 old families, 36 files

Each family has completed, `_grey`, and `_not_eligible` variants:

- `015_utopia_all_useful_arts`
- `015_utopia_friends_without_treaties`
- `015_utopia_inland_island`
- `015_utopia_league_of_need`
- `015_utopia_marked_bounds_survivor`
- `015_utopia_need_not_greed`
- `015_utopia_new_utopia`
- `015_utopia_no_bloody_glory`
- `015_utopia_paper_no_more`
- `015_utopia_renounced_bounds`
- `015_utopia_six_hour_country`
- `015_utopia_storehouses_abroad`

Only `need_not_greed` and `inland_island` directly overlap accepted achievement concepts, and even those need final naming/art/provenance review. The accepted matrix has 14 different stable IDs; do not wire the old 12 as substitutes.

### Decision/category DDS: 25 files

- `decision_category_utopia_league`
- `decision_category_utopia_ledger`
- `decision_utopia_boundary_arbitration`
- `decision_utopia_boundary_wardens`
- `decision_utopia_collect_petitions`
- `decision_utopia_common_administration`
- `decision_utopia_common_storehouse`
- `decision_utopia_fund_apprenticeships`
- `decision_utopia_guard_shore`
- `decision_utopia_household_census`
- `decision_utopia_household_guard`
- `decision_utopia_just_cause_review`
- `decision_utopia_league_aid_corridor`
- `decision_utopia_local_households`
- `decision_utopia_local_store`
- `decision_utopia_mark_needed_district`
- `decision_utopia_open_stores`
- `decision_utopia_recognize_friend`
- `decision_utopia_renunciation_vote`
- `decision_utopia_rural_rotation`
- `decision_utopia_send_magistrates`
- `decision_utopia_settlement_charter`
- `decision_utopia_storehouse_aid`
- `decision_utopia_storehouse_audit`
- `decision_utopia_urgent_service`

Several visual concepts may fit the accepted Survey, Stores, Callings, Need, Stewardship, League, or Defense families, but the accepted decision matrix is much larger. Reuse requires a manifest entry and semantic match; resizing/relabeling does not prove coverage.

### Idea DDS: 29 files

- `idea_utopia_arbitration_tables`
- `idea_utopia_civic_wardens`
- `idea_utopia_common_administration`
- `idea_utopia_common_store_network`
- `idea_utopia_common_stores_unproven`
- `idea_utopia_compulsory_assignments`
- `idea_utopia_empty_stores`
- `idea_utopia_feared_doctrine`
- `idea_utopia_foreign_laughter`
- `idea_utopia_found_manifesto`
- `idea_utopia_guild_congress`
- `idea_utopia_guilds`
- `idea_utopia_household_councils`
- `idea_utopia_household_guard`
- `idea_utopia_island_discipline`
- `idea_utopia_living_humanism`
- `idea_utopia_marked_bounds`
- `idea_utopia_marked_bounds_doctrine`
- `idea_utopia_necessary_commonwealth`
- `idea_utopia_needful_land`
- `idea_utopia_new_utopia`
- `idea_utopia_paper_utopia`
- `idea_utopia_public_storehouses`
- `idea_utopia_store_state`
- `idea_utopia_storekeeper_commission`
- `idea_utopia_unproven_common_stores`
- `idea_utopia_useful_arts`
- `idea_utopia_vocation_accord`
- `idea_utopia_vocation_confusion`

`Found Manifesto` and `Common Store Network` are the clearest conceptual matches. The accepted lifecycle requires Unmeasured Country, Inherited Order, five route ideas, Garden District Network, Auxiliary Dependency, Stewardship Burden, and their staged failure/final forms, most of which have no current matching asset.

### GUI DDS: 13 files

- `utopia_ledger_background_panel`
- `utopia_ledger_header_plate`
- `utopia_ledger_seal_sheet`
- `utopia_ledger_seal_static`
- `utopia_ledger_warning_panel`
- `utopia_marked_bounds_seal_sheet`
- `utopia_marked_bounds_seal_static`
- `utopia_new_utopia_seal_sheet`
- `utopia_new_utopia_seal_static`
- `utopia_overreach_warning_sheet`
- `utopia_overreach_warning_static`
- `utopia_storehouse_fill_sheet`
- `utopia_storehouse_fill_static`

The accepted animation set is Ledger seal, Need warning, two Choice/Assignment balance shifts, and formation-ready seal. The current runtime sheets have no current source-frame package or manifest in the working tree, and several represent removed Overreach/Marked Bounds/New Utopia states. Historical source frames exist in `0bce9e9a4`, but every animation must be reviewed under `chaos-redux-frame-animation`; a runtime sheet alone is not completion proof.

### Event/news art: 2 files

- `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_found.dds`
- `gfx/event_pictures/015_utopia_manifesto/news_event_utopia_boundary_crisis.dds`

The accepted package needs the opening report, common-store reports, settlement reports, multiple Need/League/revolt news scenes, and five route super-event variants. These two files cover at most two scenes after provenance/semantic review.

### Flags: 4 old identities, 60 files

Each old identity has base plus four ideology variants at root, medium, and small sizes:

- `utopia_new_utopia`
- `utopia_necessary_commonwealth`
- `utopia_marked_bounds_state`
- `utopia_league_of_need`

Their definitions were removed from `common/countries/cosmetic.txt`, so they are orphaned. The accepted identities are voluntary commonwealth, council union, planned Utopia, island state, and practical commonwealth. None of the four old families can be wired as a silent substitute; an asset audit may preserve a suitable composition under a stable accepted name if the visual meaning and full manifest support it.

No current Event 15 focus-icon folder, super-event image folder, league-emblem package, calling icons, case/district cards, portrait package, or `docs/assets/015_utopia_manifesto/` source/manifest package exists.

## Complete accepted-matrix implementation crosswalk

### Completion coverage matrix: all 31 rows

| Accepted surface | Primary implementation proof / owner |
| --- | --- |
| Event classification | Parent: retain ID 15 once in `chaosx_logic_effects.txt` fire-once registry; no cluster/repeatable entry. |
| Target selection | Parent/architect: Event 15 triggers/effects/constants plus HEAD active-pool and dispatcher hooks; safe predicate, score, pool order, manual reason. |
| Player choice | Parent: `chaosx.nr15.1`, AI fixed accept, human accept/reject, replacement warning, rejection cleanup. |
| Focus replacement | Parent with `hoi4-focus-trees`: complete tree, safe loader, route audit. |
| Ledger | Parent: four-value kernel, scripted GUI, breakdown localisation, AI-readable helpers. |
| Callings | Parent: focus/decision/effect/idea/AI families; real training/support/time costs. |
| Common stores | Parent: reserve bands, projects, emergency release, rotation, long mission, aid and failure states. |
| Districts | Parent: state-targeted survey/build/charter state machines and map-grounded roles. |
| Island variants | Parent: existing-island, coastal/lease, and Inland Island selection with verified geography. |
| Necessary Ground | Parent: one active case, deficit/integrity, negotiation ladder, expiry, renunciation, war only after refusal. |
| Stewardship | Parent: local provision, route repair, charter, review/status, cleanup/exit/integration. |
| Political routes | Parent/focus owner: Consent, Common Table, Guardians, Closed Island, hidden Joke Understood with distinct AI/tradeoffs. |
| Ideas | Parent: staged 12-family lifecycle, not one spirit per focus. |
| Country identity | Parent + asset owner: five cosmetic identities, party/office/leader/flag/emblem distinctions, original tag/base flag preserved until formation. |
| Military | Parent: paid citizen watch/engineers/auxiliaries/professional paths, bounded units and contracts. |
| League | Parent: faction template/rules/goals, membership autonomy, cohesion, aid/reserve/defense actions, refusal/exit/sponsor/failure. |
| Formation | Parent: sustained values, island/capital ring, conduct, external ties, route capstone; no free annexation/cores. |
| Evolutions | Parent: five paced stages, active and pre-fire paths, disable safety, actor logs. |
| Event families | Parent: founding, route, contradiction-without-meter, reaction, crisis, associate, formation, evolution events. |
| AI | Parent: route plans, dynamic decisions/missions, target safety, resource/concord/need/chaos responses. |
| Multiplayer | Parent: human target priority, asynchronous invitations/negotiation, no silent war goal or host bias. |
| Assets | Asset subagents produce; parent registers and wires every file. |
| Animation | Frame-animation subagent produces real source-frame packages; parent wires static/animated toggle states. |
| Super-event | Text/audio/art subagents research/produce; parent allocates and wires route-sensitive regional proclamation. |
| Achievements | Parent: 14 definitions/tracking/disqualifiers; icon agent: 42 DDS outputs; docs/localisation aligned. |
| Localisation | Parent/localisation auditor: final in-world text, UTF-8 BOM, no raw trigger/mechanical-history wording. |
| Event log | Parent: actor, event detail, five evolution details; remove placeholder wording. |
| Documentation | Parent/curator: canonical event doc, source-of-truth map, resolved handoffs/manifests. |
| Catalog | Spreadsheet worker after final localisation; workbook and inspection artifact aligned. |
| Improvement loop | Improvement planner after meaningful implementation tranches; addendum must be implemented/folded/queued/rejected before another pass. |
| Completion audit | Focus, decisions, country, localisation, and event-completion audits with evidence and no undisclosed fallback. |

### Focus route matrix: all 17 rows

All rows belong in `common/national_focus/015_utopia_manifesto_focus_tree.txt` with route-specific effects in Event 15 effects/decisions and AI weights in the Event 15 AI file:

1. Recovery and survey: Ledger, first store, first calling shortage, interim charter, interpretive congress.
2. Consent of Households: Choice/Concord, charters/cooperatives/plebiscites/voluntary league, slower emergency correction.
3. Common Table: reserve pooling, councils/shared production, transition shock/deadlock.
4. Guardians of Measure: Plenty/forecasting/planned cities with higher Assignment and bad-data/paternalism risk.
5. Closed Island: Assignment/autarky/service/penal works/auxiliaries/assigned colonies with resistance/isolation.
6. The Joke Understood: hidden revisable mixed order, sunset clauses/public audit, lower peak planning output.
7. Callings and education.
8. Common stores.
9. Garden settlements.
10. Island project with island/coastal/landlocked variants.
11. Defense with route-specific militia/engineers/auxiliary/professional forms.
12. Foreign Commonwealth and reserve diplomacy.
13. Necessary Ground case system.
14. Stewardship and integration.
15. Crisis branch with route correction and preserved consequences.
16. Formation lane with conduct/value/project/external thresholds.
17. Post-formation succession, associates, claim law, defense, and mature regional role.

### Decision/mission matrix: every accepted action

Primary files are Event 15 decisions/categories, effects/triggers/constants, scripted localisation, GUI, and AI. Exact rows by family:

- **Survey:** Count Houses and Hands; Publish the Accounts.
- **Stores:** Establish Capital Store; Fill Seasonal Reserve; Rotate Old Stores; Release Emergency Stores; Two Years Against Hunger; Send Surplus Abroad.
- **Callings:** Issue Open Call; Guarantee Placement; Assignment Quota; Fill Unpopular Calling; Learn Second Trade.
- **Workday:** Suspend Short Day.
- **Property:** Register Public Land; Convert Estate to Trust; Transfer Factory to Council; Assign Productive Tenure.
- **Districts:** Survey District Site; Build District Role; Complete District Charter.
- **Island:** Select National Variant; Secure Island Site; Complete Provision Ring.
- **Need:** Survey Domestic Alternatives; Draft Need Case; Offer Purchase; Request Lease; Joint Administration; Issue Ultimatum; Renounce Case.
- **Stewardship:** Emergency Provision; Restore the Route; Convene Charter; Hold Charter Period; Status Vote.
- **League:** Technical Mission; Reserve Compact; Invite to League; Prove It Is Not a Mask.
- **Defense:** Raise Citizen Watch; Form Engineer Companies; Hire Auxiliaries; End the Contract.
- **Formation:** Prove the Commonwealth.

Every row requires dynamic costs/durations where specified, activation and target validity, player-visible trigger/effect tooltips, success/partial/failure resolution, AI use, invalid-target cancellation, and cleanup. A collection of old 25 icons does not reduce this scope.

### Idea lifecycle matrix: all 12 rows

1. Found Manifesto.
2. Unmeasured Country.
3. Inherited Order.
4. Charter of Households.
5. Common Table.
6. Perfect Measure.
7. Closed Island.
8. Practical Commonwealth.
9. Common Store Network.
10. Garden District Network.
11. Auxiliary Dependency.
12. Stewardship Burden.

Each needs start/unlock, mitigation, route upgrade, failure form, removal/terminal behavior, and final form. Centralize numeric stages and use swap/remove patterns so mutually exclusive stages cannot stack.

### Target eligibility matrix: all 17 checks

The Event 15 safe-recipient trigger/score must explicitly implement:

1. Major status exclusion.
2. Industry weak/modest bands and strong-economy exclusion.
3. Generic/approved replaceable focus-tree gate.
4. Political/identity focus-depth protection.
5. Ordinary-country origin and event-created-package exclusion.
6. Peace/limited defensive breathing-room preference and civil-war/near-capitulation/offensive-war exclusions.
7. Valid, recoverable capital.
8. Special/nonhuman/terminal/world-end Chaos actor exclusion.
9. Dominant faction-leader exclusion.
10. Extensive subject-empire exclusion.
11. Extensive occupation burden exclusion.
12. Safe human priority.
13. Island/coast positive context but never a requirement.
14. Landlocked Inland Island viability.
15. Migration/housing pressure positive context.
16. Infrastructure weakness positive context but fatal collapse exclusion.
17. Active/recent country-transformation exclusion.

Pool order is safe humans, safe generic/approved AI minors, then explicitly approved lightly developed AI minors. Manual force may bypass scarcity/weight only; special actors, protected packages, and invalid countries still require an explicit stronger override. No live reusable protected-tree registry exists, so this is an implementation prerequisite, not an optional refinement.

### Country package matrix: every surface

The six columns are shared opening plus Consent, Common Table, Guardians, Closed Island, and hidden humanist. Every route needs a distinct implementation for all 14 surfaces:

- original tag preservation;
- route cosmetic identity;
- leader/institutional office;
- ruling organization/party;
- flag;
- starting/route ideas;
- advisors;
- military identity;
- economy/property model;
- diplomacy;
- territorial method;
- integration model;
- formation proof;
- post-formation risk.

The original leader, parties, forces, templates, technologies, tag, and base flag remain through the opening. Cosmetic identity is a formation outcome, not an acceptance-time overwrite.

### AI strategy matrix: all 20 rows

Event 15 AI must cover: eligible AI recipient; democratic founder; communist founder; neutral founder; fascist founder; voluntary route; council route; planner route; Closed Island route; hidden humanist route; league founder; league candidate; major sponsor; Need target; associate; auxiliary source; low Plenty; low Concord; high Need; high chaos. Each row needs preferred behavior, avoid conditions, escalation, and invalid-state/terminal cleanup rather than only focus `ai_will_do` values.

### Asset manifest matrix: every family

Required families are opening report; common-store reports; settlement reports; Need news; five-route final super-event; focus icons; idea icons; decision icons; decision-category icons; 14 achievement triplets; five route flags; five league emblems; implemented institutional portraits; implemented fictional personal portraits; Ledger panel; Need/Plenty/Concord/Choice-Assignment value icons; six calling icons; case cards; district cards; real-frame Ledger seal; real-frame Need warning; real-frame balance shift in both directions; real-frame formation-ready seal. Asset agents own production/manifests; the parent owns stable names, `.gfx`/`.gui` registration, gameplay references, and proof that runtime files match manifests.

### Achievement matrix: all 14 stable IDs

- `utopia_manifesto_no_place_but_home`
- `utopia_manifesto_need_not_greed`
- `utopia_manifesto_every_calling_chosen`
- `utopia_manifesto_two_year_table`
- `utopia_manifesto_archipelago_of_small_places`
- `utopia_manifesto_inland_island`
- `utopia_manifesto_gold_for_common_use`
- `utopia_manifesto_the_joke_understood`
- `utopia_manifesto_consent_of_the_governed`
- `utopia_manifesto_the_perfect_measure`
- `utopia_manifesto_closed_circle`
- `utopia_manifesto_no_foreign_hands`
- `utopia_manifesto_the_stores_remain`
- `utopia_manifesto_no_one_in_chains`

Snapshot immutable eligibility facts at acceptance where required (human control, landlocked status, starting coastline, starting relative strength, route eligibility). Maintain permanent conduct disqualifiers for offensive war/coercive ultimatum, Assigned Colony, forced relocation/labor, repeated votes, auxiliary use, member annexation, censorship, data scandal/revolt, and crisis repeal as specified. Do not infer historical conduct only from current state at unlock time.

## Recommended event-owned file surface

The exact split may be adjusted by the parent/architect, but the following ownership keeps the package reviewable:

| System | Recommended files |
| --- | --- |
| Entry and event families | `events/015_utopia_manifesto.txt` |
| Shared tuning | `common/script_constants/015_utopia_manifesto_constants.txt` |
| Eligibility, route/value/case/stewardship/league/achievement gates | `common/scripted_triggers/015_utopia_manifesto_triggers.txt`, split by subsystem if needed |
| Prefire, acceptance, Ledger, cases, districts, stewardship, league, evolution, formation, cleanup | `common/scripted_effects/015_utopia_manifesto_effects.txt`, split by subsystem if needed |
| Focus tree | `common/national_focus/015_utopia_manifesto_focus_tree.txt` |
| Decisions/missions | `common/decisions/categories/015_utopia_manifesto_categories.txt`; `common/decisions/015_utopia_manifesto_decisions.txt` |
| Ideas/dynamic state | `common/ideas/015_utopia_manifesto_ideas.txt`; optional Event 15 dynamic-modifier file for state/country modifiers |
| AI | `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` plus focus/decision weights |
| Faction/league | Event 15 files under `common/factions/templates/`, `rules/`, `goals/`, and manifests if used |
| Leaders/advisors | `common/characters/015_utopia_manifesto_characters.txt` for stable implemented characters/institutions; dynamic office creation only where engine-valid and documented |
| Narrow hooks | `common/on_actions/015_utopia_manifesto_on_actions.txt` only for event-driven war/state/capitulation hooks actually needed; no broad periodic hook |
| GUI | `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`; `interface/015_utopia_manifesto.gui`; `interface/015_utopia_manifesto.gfx` |
| Dynamic text | `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` |
| Localisation | `localisation/english/015_utopia_manifesto_l_english.yml` with UTF-8 BOM |
| Opinions | `common/opinion_modifiers/015_utopia_manifesto_opinion_modifiers.txt` if reactions need durable named modifiers |
| Documentation/assets | `docs/events/015_utopia_manifesto/overview.md`; `docs/assets/015_utopia_manifesto/manifest.md` and subagent handoffs; `docs/super_events/` research/provenance updates |

Potential additions to `chaosx_dynamic_effects.txt` or shared triggers must first prove they are reusable beyond Event 15 and must update `chaosx_dynamic_effects.md` in the same change. Event-specific helpers belong in Event 15 files.

## Live Chaos Redux precedents

| Need | Preferred live precedent |
| --- | --- |
| Weighted safe recipient and actor-scoped prefire | `common/scripted_effects/011_secret_alliance_effects.txt:20-281` and `common/scripted_triggers/011_secret_alliance_triggers.txt:77+`; simpler ticket-array precedent at `common/scripted_effects/007_fury_effects.txt:85-198` with `fury_can_be_selected` at `common/scripted_triggers/007_fury_triggers.txt:22-38`. |
| Fire-once preflight without consumption on failure | Event 11/14/17/18 branches in `chaosx_settings_effects.txt:4597-4647`. |
| Runtime focus loading | `common/scripted_effects/003_holy_realm_effects.txt:1867-1871`, `007_fury_effects.txt:212-219`, `014_cannibalism_country_effects.txt:718-743`, and `014_cannibalism_unification_effects.txt:514-523`. These are identity-owned transformations, not proof that arbitrary existing unique trees are safe. |
| Selected country/state decision surfaces | `common/decisions/017_random_faction_decisions.txt`, `common/decisions/014_cannibalism_unified_decisions.txt`, and their matching target triggers/scorers. |
| Complex Ledger GUI | `common/scripted_guis/camp_repression_ledger_scripted_gui.txt:12-193` with `interface/camp_repression_ledger.gui`; compact category GUI at `common/scripted_guis/003_holy_realm_scripted_guis.txt:5-63`; selected target/animation fallback at `common/scripted_guis/014_cannibalism_scripted_gui.txt:67-168`. |
| Five-stage idea/modifier lifecycle | Event 14 idea/dynamic-modifier files and update effects; use staged swap/remove behavior rather than permanent stacks. |
| Modern faction template/rules/goals/cohesion | `common/factions/templates/holy_realm_mandala_of_nations.txt`, `common/factions/rules/holy_realm_mandala_rules.txt`, `common/factions/goals/holy_realm_mandala_goals.txt`, and `common/scripted_effects/003_holy_realm_effects.txt:1160-1413`. |
| Event actor and evolution logs | Default actors in `chaosx_events_log_effects.txt:178-370`; Fury records at `007_fury_effects.txt:1223-1279`; compact four-stage wrapper at `018_resources_found_log_effects.txt:91-141`; complex actor snapshots at `014_cannibalism_core_effects.txt:1633-1670`. |
| Cosmetic identities | `common/countries/cosmetic.txt` plus `set_cosmetic_tag` in `003_holy_realm_effects.txt:1867` and Event 14 unified route effects. |
| AI strategy lifecycle | `common/ai_strategy/003_holy_realm.txt` and Event 11/14/18 AI files, especially allowed/enable/abort and emergency-state behavior. |
| Timed decision-to-mission flow | `common/decisions/007_fury_decisions.txt` and current Event 14/17 mission families. |
| Achievements | `common/achievements/chaos_redux_achievements.txt`; triplet sprites in `interface/014_cannibalism_achievements.gfx` and `interface/chaosx_achievements.gfx`; localisation in `chaosx_achievements_l_english.yml`. |
| Super-event/audio | Settings-aware launch in `007_fury_effects.txt`; selectors in `chaosx_scripted_localisation_super_events.txt`; audio helpers in `chaosx_settings_effects.txt:4741+`; sound registration files listed above. |

## Vanilla and official-documentation precedents

| Major system | Exact installed-game precedent |
| --- | --- |
| Focus replacement | `documentation/effects_documentation.md:4771-4786` documents `load_focus_tree` and `keep_completed`; `events/NSB_Poland.txt:1381-1384` loads `polish_focus`; `common/on_actions/07_nsb_on_actions.txt:558-563` gates a generic-tree country before loading Poland's tree. |
| Focus plus cosmetic identity | `common/national_focus/china_warlord.txt:518-524` loads a new tree and applies `CHI_warlord_leader`; `documentation/effects_documentation.md:6720-6728` documents `set_cosmetic_tag`. |
| Event targets | `documentation/effects_documentation.md:6496-6512` documents regular/global event-target saves; `documentation/triggers_documentation.md:3844-3851` documents `has_event_target`. |
| Targeted state decisions | `common/decisions/BRA.txt:14-22` uses `state_target`/`target_trigger`; `common/decisions/AST.txt:114-127` combines target arrays and root/target triggers. |
| Timed missions | `common/decisions/AST.txt:25-76` shows cancel trigger, `days_mission_timeout`, and timeout effects. |
| Dynamic state modifiers | `common/decisions/BRA.txt:84-97` removes one state modifier and adds its upgraded replacement; additional settlement modifier at `BRA.txt:660-664`; official effect headings at `effects_documentation.md:1153`, `5978`, and `8239`. |
| Modern faction creation | `documentation/effects_documentation.md:3115-3138` documents `create_faction_from_template`; `common/decisions/BALTIC.txt:36-41` uses it and adds faction initiative. |
| Autonomy/associate states | `documentation/effects_documentation.md:6588-6600` documents `set_autonomy`; `common/decisions/BEL.txt:1106-1110` applies a custom autonomy state to a target. |
| Scripted GUI | `common/scripted_guis/_documentation.md`; `common/scripted_guis/RAJ_tax_fraud_scripted_gui.txt` provides a decision-category window with variable-driven visible states. |
| AI strategy lifecycle | `common/ai_strategy/ENG.txt:392-411` includes allowed/enable/abort and production strategies; later ENG sections cover alliance, protect, front-control, and allied-border defense. |
| Achievements | `common/achievements.txt` uses `possible` and `happened`; `gfx/achievements/` provides completed/grey/not-eligible triplets; `interface/achievements.gfx` registers them. |
| Character/country transformation | Vanilla France/Spain event chains show ordered leader/cosmetic/focus changes; `events/France.txt:1169-1172` applies Free France identity and tree without changing the original country tag. |

## Dependency-safe implementation order

1. Freeze Event 15 identifiers and create constants. Reserve visible/audio IDs only after a fresh collision check. Decide whether route variants use one or five visible slots.
2. Implement the protected/replaceable-tree registry and exact recipient trigger/score, including debug/manual rejection reason. Until this passes, keep Event 15 unavailable.
3. Implement prefire selection, actor persistence, actor-scoped `.1` dispatch, human accept/reject, AI accept, focus-replacement warning, idempotent cleanup, and HEAD shared registration/log availability. This is the first meaningful commit.
4. Implement the four-value Ledger kernel, bands/breakdowns, public scripted GUI, AI-readable triggers, and cleanup. Do not introduce an Overreach/contradiction substitute meter.
5. Implement opening focuses and the five route locks, then the staged idea kernel. Verify the hidden route cannot be selected generically by AI and has explicit reveal conditions.
6. Implement Survey, Stores, Callings, Workday, Property, District, and Island decisions/missions with target validity, costs, partial/failure outcomes, and AI.
7. Implement one-at-a-time Necessary Ground cases and geography variants, then stewardship/status state machines. Validate every country/state target and expiry path before adding military escalation.
8. Implement league template/rules/goals, cohesion, invitations/refusal/exit/sponsor behavior, reserve/aid/defense actions, and multiplayer consent.
9. Implement identity/party/office/leader/advisor/cosmetic flag packages, paid military growth, auxiliaries, succession, formation, and post-formation play.
10. Implement all five evolution paths and event families, including pre-fire stage application, dynamic pacing, disable safety, actor log entries, and event/evolution details.
11. Implement formation proof and the route-sensitive regional proclamation; wire verified text, art, licensed audio, and settings-aware playback.
12. Implement immutable achievement tracking and all 14 registry/localisation/icon triplets.
13. Reconcile or replace orphaned assets through asset/frame-animation workflows; wire only manifest-backed final runtime files.
14. Update the canonical event doc, super-event provenance docs, source-of-truth map, and final localisation; then run focus, decision/mission, country-package, localisation, and event-completion audits.
15. Run the improvement loop after substantial mechanics are playable, resolve/fold/queue/reject its addendum, then update workbook row 16 and inspection artifact from final in-game wording.

## Unresolved gaps and validation risks

### Hard implementation prerequisites

1. **Protected-tree registry:** none exists live. Start with `generic_focus` and an explicit, reviewed allowlist only. A vague “lightly developed” score is not a safe substitute. Protect any approved tree after meaningful political/identity progress.
2. **Balance thresholds:** exact factory, state-count, focus-depth, capitulation, occupation, subject-network, and recent-transformation bands remain unset and must be centralized after live distribution review.
3. **Geography:** island/coastal/landlocked helpers exist at primitive trigger level, but the accepted island-site, corridor, lease, district, and Inland Island routes need verified state selection and invalidation rules. Do not fake coast access or hardcode unreviewed state lists.
4. **Character portability:** the recipient is arbitrary. Stable institutional/personal character definitions and dynamic country-leader creation must be tested for arbitrary country scope; do not assume a fixed-tag character package.
5. **Faction depth:** a named faction alone fails the spec. Template, rules, goals, cohesion, initiative, autonomy, membership lifecycle, and cleanup need one coherent owner.
6. **Pre-fire evolutions:** five disabled/enabled stages can exist before Event 15 fires. Initialization must apply the strongest valid baseline package without mislabeling the founding stage, instant popup spam, or trapping disabled stages.
7. **Global event target cleanup:** the selected/latest actor must persist for dispatch and logs, then be cleared on reject/terminal invalidation. Regular event targets are preferable inside a single chain; use global targets only for cross-chain persistence.
8. **State machines and concurrency:** one active Need case, one negotiation phase, stewardship area state, status vote, district projects, reserve mission, auxiliary contracts, and league obligations require idempotent cancellation when target/controller/owner/faction state changes.
9. **Assets:** runtime remnants do not prove source, semantic fit, animation legitimacy, dimensions, or wiring. Missing focus icons, route flags/emblems, most events/news, five route super-event images, cards/callings, and accepted achievement art remain blockers.
10. **Super-event research:** text and uniquely licensed audio are not live. Slot 15 is forbidden; old historical slots/audio must not be silently resurrected.

### Task-specific validation scenarios

- Automatic selection with no safe recipient returns Event 15 to the pool/timer without consuming it; manual UI shows the exact reason.
- Safe human is preferred over AI; protected human is never selected. Safe AI always accepts.
- Human rejection leaves the original tree, tag, flag, leader, forces, ideas, and country state untouched, clears all Event 15 temporary/global state, and consumes the legitimate fire-once event.
- Human acceptance warns before replacement and loads only the Event 15 tree with the chosen `keep_completed` policy.
- Tag/cosmetic/leader changes do not lose the Event Log actor or evolution actor.
- Every Ledger action visibly changes an explainable breakdown and the AI uses the same underlying values without GUI dependence.
- Island, coastal, and landlocked recipients each have a valid non-placeholder formation path.
- Need case purchase, lease, joint administration, refusal, ultimatum, renunciation, expiry, and invalid-target paths all close exactly once; unrelated annexation cannot be laundered through the case.
- Stewardship can end in association, integration, independence, revolt/exit, or cleanup without indefinite hidden occupation.
- League invitations to humans require a choice; refusal/exit works; member annexation/coercion records permanent conduct and affects formation/achievements.
- Auxiliary contracts cost real equipment/payment, can end cleanly, and permanently disqualify `no_foreign_hands` where required.
- Formation cannot trigger on domestic values alone; island/capital-ring, conduct, and at least three meaningful external ties plus regional objective are all enforced.
- Each of five evolutions works when earned during play and when enabled before Event 15 fires, with correct actor/stage/detail and disabled-stage safety.
- Super-event route art/text changes correctly, plays only the Event 15 licensed audio through the settings-aware helper, and never displays Black Banner slot 15.
- All 14 achievements have immutable eligibility/disqualifier evidence and exact completed/grey/not-eligible sprites.
- Event 15 remains absent from every cluster registry.
- Workbook row 16 and evolution/detail wording match final localisation exactly.

## Working-tree preservation

At the final inspection before writing this handoff, the branch was `master`, ahead of `origin/master`, with unrelated active air-cleanliness and chemical-air-variant work. Modified files included Event 15-unrelated air-cleanliness effects/triggers/docs/assets/interface files, and untracked chemical-air asset working folders/files. None was edited, staged, reverted, or included by this explorer. Shared-file implementation must begin with a fresh status check because the branch advanced during exploration and other agents may be active.

## Completion statement for this exploration

The live repository map, historical recovery boundary, stale ID 15 inventory, current shared insertion points, accepted matrix crosswalk, local/vanilla precedents, dependency order, orphaned asset inventory, and validation risks are covered above. No gameplay or asset simplification is approved by this handoff. Event 15 itself remains unimplemented; this report is implementation evidence and routing guidance only.
