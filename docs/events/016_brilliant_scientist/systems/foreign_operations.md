# Event 016 International Scientific Contest

## Purpose

The international contest begins with Evolution II. It gives only relevant foreign countries a targeted decision category against the current Kruger host. It does not run from a daily, weekly, or monthly world loop: one bounded country scan initializes eligible actors when Evolution II opens and again after a successful host transfer.

Foreign behavior reacts to Security Exposure, host security, facility access, intelligence capability, ideology, diplomatic relations, war, alliance structure, project history, Grievance, Dependence, and Independent Capacity. The current host can answer visible diplomatic approaches and detected covert operations.

## Actor and target lifecycle

`brilliant_scientist_foreign_initialize_contest` clears stale target arrays, finds countries satisfying `brilliant_scientist_is_valid_foreign_actor`, and gives each actor a one-country target array containing the current host. The category remains visible only while Event 016 is in its international phase, Kruger is alive, the host is valid, and no terminal world state has locked the chain.

Each actor may conduct one live operation at a time.
A host accepts at most two simultaneous incoming operations.
The shared start helper checks the same route, access, and permanent per-host exclusion as the public decision before it acquires either lock, selects a project, or opens a diplomatic response.
The counter-program's support equipment is debited inside that successful start boundary at selection, alongside the decision's native Political Power cost.
Every timed action stores its actor, host, operation type, target project family, start date, outcome band, detection state, and later diplomatic attribution.
Cancellation removes both actor and host locks for the matching operation, consumes that route's per-host one-shot, and does not refund preparation.

Every delayed decision callback and event option supplies its own fixed operation type.
The callback must match the live actor receipt and original host id before it can record, cancel, or finish anything.
Host responses additionally consume an actor-owned pending-response flag before applying effects.
Immediate diplomatic responses precede the operation result; detected covert responses follow an already recorded result.
Actor reports require the matching recorded result and no pending host response.
A repeated host response, an early report, or a stale popup from another operation cannot mutate a later receipt.
The original host remains the settlement target after a successful transfer; immediate diplomacy still requires the current living host.
Invalid response context closes only its matching receipt and preserves any result already recorded.

## Foreign actions

| Action | Time | Base cost | Primary gates and results |
|---|---:|---:|---|
| Observe the program | 30 days | 15 Political Power | Foreign-interest threshold and a current host; builds a dossier and later operation access |
| Send a formal invitation | Immediate host event | 25 Political Power | Relations, ideology, faction, or academic access; host can refuse, permit a visit, or let Kruger decide |
| Recruit an assistant | 45 days | 30 Political Power | Access plus a project target; success gives the actor the selected family's Theory modifier permanently (see [Foreign Theory knowledge](#foreign-theory-knowledge)) or creates exposure/scandal |
| Steal an archive | 60 days | 45 Political Power | Intelligence access and an unstolen project family; success gives the actor that family's Theory modifier permanently and marks the host archive stolen |
| Sabotage a project | 75 days | 55 Political Power | Hostile motive and an undamaged project family; damages only the selected family |
| Encourage defection | 60 days | 45 Political Power | Prior contact, diplomatic access, and a transfer-ready Kruger; success revalidates the character transfer |
| Extract Kruger | 75 days | 70 Political Power | Intelligence access and a transfer-ready Kruger outside the actor's faction; partial success captures an assistant or knowledge |
| Offer protection | Immediate host event | 35 Political Power | Diplomatic access without war; creates full, limited, or refused protection memory |
| Attempt assassination | 90 days | 100 Political Power | Meaningful dangerous-project threat, hostile motive, and intelligence access; always produces attribution on a nonfailure |
| Publicly challenge the programme | Immediate host event | 35 Political Power | Authenticated observation, exposed research, detected operations, or a strategic project; host chooses demonstration, denial, publication, observers, sabotage explanation, or threat |
| Build a counter-Kruger programme | 120 days | 60 Political Power + 250 support equipment | Intelligence access, a project evidence receipt, and an active host project; installs a standing family countermeasure (see [Counter-Kruger countermeasures](#counter-kruger-countermeasures)) and improves later operations against the same host or the Kruger State formed from it |

Diplomatic approaches use host events `.100` and `.110`. Covert routes use detected host events and paired actor reports across `.120` through `.181`.

## Outcome and detection model

Success and detection are separate bounded calculations. Actor capability includes an intelligence agency, operative count, network strength, major-power reach, prior observation, prior recruitment, joint-laboratory or controlled access, ideology, opinion, alliance, adjacency, and war.

Host vulnerability includes Exposure and the targeted project's stage. Recruitment and defection also read Grievance, Independent Capacity, and Dependence. Extraction and assassination become harder against strong Independent Capacity. Internal security, a compartmentalized military office, hardened laboratories, a multi-site network, completed loyalty reviews, protection agreements, and accumulated security alerts reduce success while increasing detection.

Detected covert operations cost the actor additional Political Power and stability, raise the host's persistent security alert, create bilateral opinion penalties, and allow the host to choose security escalation or diplomatic protest.
These choices feed later containment strength and Grievance rather than disappearing after the report.
Public challenges use their separate public consequence set and do not incur the covert detection surcharge.

After at least one resolved Prototype, the first detected operation that resolves can also schedule `chaosx.nr16.9` on the host. The report retains the exact actor and operation from the foreign-resolution transaction. Controlled exchange is available only while the two countries are not at war and the operation is not extraction or assassination; it grants the actor one capped family-theory result from the host's latest breakthrough and a positive bilateral opinion modifier. A private warning applies a smaller negative opinion modifier and lowers Exposure, while public accusation applies the stronger modifier, raises Mandate and Exposure, and increases the actor's foreign-interest pressure. Host and `KRG_warren_kruger` receipts prevent replay, and the ordinary transfer, terminal, and sovereignty cleanup helpers clear or carry the reaction state without changing the foreign operation's existing success result.

The public challenge is a separate actor-owned operation with its own per-host resolution ledger. It requires the public-challenge interest threshold plus diplomatic or intelligence access and one of four evidence sources: a successful observation, exposed research, detected foreign operations, or a strategic project. The challenge is immediately delivered to the current host as `chaosx.nr16.190`, and the six host answers apply distinct Mandate, Exposure, Dependence, Project Capacity, Grievance, and diplomatic-memory consequences before the actor receives `chaosx.nr16.191`. The host confrontation uses the sovereignty-confrontation card and the actor's after-action report uses the Directorate dossier card. It does not steal a project stage, create a special-project reward, or move Doctor Kruger, and its public detection is recorded in the normal foreign-operation history.

The counter-Kruger programme is a separate one-use actor operation. It requires the counter-program interest threshold, intelligence access, an active host project, a prior observation, recruitment, theft, public-challenge, or strategic-project evidence receipt, and 250 support equipment. The 120-day operation selects the host's most advanced family through the existing project-target helper; a successful result records the host and family in the actor's countermeasure arrays, while a partial result records only a failed family study. The actor's later operation score against that same host, or against the Kruger State formed from it (`brilliant_scientist_foreign_has_countermeasure_against_operation_host`), receives the bounded `countermeasure_previous` bonus. A success also installs the studied family's standing countermeasure, described below. The programme never grants a project stage, a second Kruger, or a unit. A detected operation opens `chaosx.nr16.193` before the actor report `.194`; the host response uses the machine-security incident card and the actor report uses the Directorate dossier card, while the dedicated response still avoids the generic controlled-exchange reaction so countermeasure work cannot accidentally become a full project-theory reward.

The host-facing foreign-operation reports (`chaosx.nr16.100`, `.110`, `.120`, `.130`, `.140`, `.150`, `.160`, `.170`, and `.180`) append the same retained host-archetype clause used by the Directorate reports. Universities, industrial hosts, militarized states, threatened governments, colonial administrations, refugee networks, and the default host therefore read invitations, observation, recruitment, theft, sabotage, defection, extraction, and assassination through their own institutional pressures. Actor after-action reports (`.101`, `.111`, `.121`, `.131`, `.141`, `.151`, `.161`, `.171`, and `.181`) use `GetBrilliantScientistForeignHostFlavorClause` to read the carried host target, so the reporting country does not accidentally substitute its own archetype or lose the original context.

## Foreign Theory knowledge

Five outcomes hand a foreign actor one family's Theory: assistant recruitment success, archive theft success, a partial defection (an assistant leaves while Kruger stays), a partial extraction, and the host's controlled exchange in `chaosx.nr16.9`.
Each calls `brilliant_scientist_foreign_grant_selected_family_theory` on the actor with the persistent selected family as input.
The helper writes Theory into the actor's 15-entry `brilliant_scientist_foreign_project_knowledge_entries` array (indexes 0 to 14 match family IDs 1 to 15), increments `brilliant_scientist_foreign_known_project_family_count`, and sets `brilliant_scientist_foreign_gained_new_family_knowledge`; a family already held sets `brilliant_scientist_foreign_family_knowledge_already_held` instead and changes nothing.

The payoff is the family's own Theory dynamic modifier (`brilliant_scientist_<family>_theory`), the same research-speed and family bonuses a host receives at Theory.
Each of the fifteen Theory modifiers lists `brilliant_scientist_foreign_knows_<family>_theory` as an `enable` branch and a `remove_trigger` exclusion, and that trigger reads the knowledge array, so the modifier stays after the actor loses contact with the host, after Kruger moves or dies, and after the actor itself hosts Kruger and loses him.
`brilliant_scientist_foreign_reconcile_knowledge_runtime` adds the modifier for every held family after a grant and at the end of `brilliant_scientist_disable_project_stage_modifiers`, so a host suspension or transfer cleanup cannot strip stolen Theory.

The grant never exceeds Theory and never copies the host package, Kruger, facilities, Directorate meters, the host project ledger, Project Capacity, or project forces.
No family has a native project line outside Kruger's host or the Mengele provider: every Prototype special project and Directorate stage order writes the host ledger, so stolen Theory does not open a Prototype for the actor.

The after-action reports `.131`, `.141`, `.161`, and `.171` call `brilliant_scientist_foreign_show_theory_grant_tooltip` in their option.
It names the family through `brilliant_scientist_foreign_theory_gained_tt`, shows the Theory modifier, and reports how many Kruger families the actor now holds (the only reader of `brilliant_scientist_foreign_known_project_family_count`), or prints `brilliant_scientist_foreign_theory_already_held_tt` when the family was already known.

## Counter-Kruger countermeasures

A successful counter-Kruger programme calls `brilliant_scientist_countermeasure_record_family` on the actor. It sets one standing flag, `brilliant_scientist_countermeasure_<family>`, for the studied family and installs that family's effect once; a second study of the same family changes nothing.
The countermeasure answers Kruger's methods wherever they are used, because those methods travel with him, so a countermeasure built against one host also applies to the Kruger State formed from it and to any later host.
Every consumer runs inside an existing action scope. There is no world scan, meter, GUI, or focus.
Values live in `brilliant_scientist_countermeasure` (`common/script_constants/016_brilliant_scientist_foreign_constants.txt`); raid weights and idea values are mirrored as file-scoped values where the field rejects constants.

| Family | Consumer | Effect |
|---|---|---|
| Teleportation | Portal raid success formula (`brilliant_scientist_portal_countermeasure`, state scope) and `brilliant_scientist_seal_recaptured_portal_breach` | Portal raids against the holder's states have -15% success chance; sealing a recaptured breach costs 10 Command Power instead of 25 (`brilliant_scientist_can_pay_portal_sealing`, `GetBrilliantScientistPortalSealingCost`) |
| Biological Weapons | All eighteen Event 016 biological raid success formulas (`brilliant_scientist_biological_countermeasure`, state scope) | Biological raids against the holder's states have -15% success chance |
| Temporal | `brilliant_scientist_commit_bounded_temporal_action` | While the user is at war with a holder (`brilliant_scientist_temporal_user_faces_countermeasure`, enemies only), each bounded temporal intervention adds 10 more temporal debt, with a tooltip line |
| Singularity | `brilliant_scientist_singularity_surrender_offer_target_is_valid` | The holder can offer an armed Kruger State a survivable surrender from 50% surrender progress instead of 75% |
| Robotics | Spirit `brilliant_scientist_countermeasure_anti_machine_warfare` | +10% attack against `KRG` |
| Cloning | Spirit `brilliant_scientist_countermeasure_clone_identity_screening` | +10% defense against `KRG` |
| Paleogenetics | Spirit `brilliant_scientist_countermeasure_creature_containment` | +8% defense and +4% attack against `KRG` |
| Xenobiological Synthesis | Spirit `brilliant_scientist_countermeasure_organism_control_jamming` | +6% defense and +6% breakthrough against `KRG` |
| Alien Arms | Spirit `brilliant_scientist_countermeasure_alien_arms_shielding` | +5% attack and +8% breakthrough against `KRG` |
| Computation | Dynamic modifier `brilliant_scientist_counter_kruger_studies` | +10% decryption |
| Electronics | Same modifier | +10% air detection |
| Materials | Same modifier | -15% factory damage from air attack |
| Rocketry | Same modifier | +15% static anti-air damage |
| High Energy | Same modifier | +15% factory repair speed |
| Biomedical | Same modifier | -5% army attrition |

The five combat spirits use `targeted_modifier` with `tag = KRG` because vanilla notes in `common/dynamic_modifiers/aat_dynamic_modifiers.txt` that targeted modifiers do not work inside dynamic modifiers. They therefore act against the fixed-tag Kruger State only; a host transformed into the Kruger State in place keeps its own tag and is not covered by them.
The six conventional values share one modifier whose values are country variables written by the record helper, so a country that studied several conventional families shows one line in its national modifiers.
The programme's report `chaosx.nr16.194` names the studied family and its effect through `brilliant_scientist_countermeasure_result_tt` and `GetBrilliantScientistCountermeasureEffect`.

## Transfer and assassination safety

Defection and extraction call the existing Event 016 guarded transfer transaction at the final rendezvous. The recipient and host are revalidated, Kruger cannot move while actively assigned to a special project, the old host is reconciled before nationality and roles move, and the original appointment reward is not replayed. A race lost to another transfer becomes a partial operation instead of creating another character.

Assassination can confirm death only for ordinary human continuity. Clone, machine, temporal, or proven extraterrestrial continuity converts a successful strike into injury, greater Grievance, greater Independent Capacity, higher Exposure, and the matching continuity record. A failed or partial attempt likewise changes the later sovereignty balance.

## Persistent history

Actor arrays retain observation, invitation, recruitment, theft, sabotage, defection, extraction, protection, assassination, public-challenge, and counter-program history per host.
Each chronological resolution row has aligned type, result, detection, family, start date, selected project stage, peer, and actor/host role values.
The shared prefix is `brilliant_scientist_foreign_operation_history_`, with suffixes `types`, `results`, `detected`, `families`, `started_dates`, `stages`, `peers`, and `roles`.
Roles use `brilliant_scientist_foreign_history_role.actor` and `.host`.
The older `hosts` and `actors` peer lists remain role-specific; consumers needing a chronological join use `peers` and `roles`.
Non-project operations explicitly record the none family and stage.
Missing metadata for an earlier row is padded with the invalid sentinel (-1), not a fabricated date, stage, role, or country.
Metadata reconciliation only grows short arrays to the existing type-row count; it does not truncate history.
The selected family and stage also feed exact follow-up descriptions and family-specific countermeasure receipts.
Opinion modifiers preserve invitation refusals, scientific contact, protection compacts, exposed operations, and diplomatic protests.

## Internal callback contract

`brilliant_scientist_foreign_start_operation` runs in the targeted decision's actor scope with `FROM` as the proposed host and temporary `brilliant_scientist_foreign_operation_type` set to a fixed operation constant.
It returns no reward or receipt on a failed route check.
It owns initial project selection, immediate host dispatch, and the counter-program support debit.
Callers must not repeat those actions after invoking it.

`brilliant_scientist_foreign_callback_matches_active_operation` queries a delayed targeted callback using the fixed temporary `brilliant_scientist_foreign_expected_operation`, the actor's live type, and `FROM.id`.
`brilliant_scientist_foreign_event_receipt_matches_active_operation` queries the same receipt through the regular original actor and host event targets.
These temporary inputs are fixed at each source call site; they are not persistent per-popup snapshots or reads of whichever operation happens to be active.

The actor also retains `brilliant_scientist_foreign_operation_host_scope`, a country-scope pointer paired with the numeric original-host id and cleared only at final settlement.
The pointer is independent of the response chain's regular event targets.
`brilliant_scientist_foreign_record_resolution` appends one row to each party only when the matching receipt is unrecorded.
Only its intact-chain wrapper can refresh recognition or present a foreign reaction, and only while the original parties remain valid recipients outside terminal lock.
`brilliant_scientist_foreign_cancel_operation` clears that receipt's response phase, records cancellation only if no result exists, and calls private settlement without presenting another reaction.
`brilliant_scientist_foreign_finish_operation` runs in actor scope and requires a recorded matching receipt with no pending response before releasing the host slot and live variables.
`brilliant_scientist_foreign_align_history_metadata` is country-scoped, takes no input, pads only missing metadata, and never grants gameplay rewards.

Example of a delayed observation callback:

```text
set_temp_variable = { brilliant_scientist_foreign_expected_operation = constant:brilliant_scientist_foreign_operation.observation }
brilliant_scientist_foreign_resolve_covert_operation = yes
```

### Annex and terminal settlement

`brilliant_scientist_foreign_owned_receipt_is_valid` queries a country-scoped live receipt and verifies that its stored host pointer resolves to its original numeric host id.
It takes no temporary argument and does not change state.
The private actor helpers `brilliant_scientist_foreign_record_owned_resolution`, `brilliant_scientist_foreign_finish_owned_operation`, and `brilliant_scientist_foreign_cancel_owned_operation` share the same history and per-operation resolved-target handling as ordinary callbacks.
They never create regular event targets, change the caller's expected-operation temporary, spend or refund resources, or dispatch a response or recognition event.
An unresolved cancellation writes one cancellation row to both parties; an already recorded success, partial result, or failure keeps its original result and rows.
Final settlement clears the live flag before rebuilding the original host's registry, then clears the stored host pointer last.

`brilliant_scientist_foreign_reconcile_incoming_operations` is a non-destructive host query/rebuild: it snapshots unique actor entries that still own a live operation against this host, rebuilds the persistent array after iteration, and derives the exact count and assassination-live marker from the retained entries.
It never cancels another actor's receipt, including an actor whose stale array entry points at a different host.
Duplicate entries and count drift do not release a second slot, and one completed assassination does not clear another live assassin's marker.
The normal two-incoming-operation start limit remains unchanged; reconciliation records the actual unique count rather than hiding entries behind a count cap.

`brilliant_scientist_foreign_cleanup_country_operations` is the destructive country-owned annex/terminal entry point.
It settles only that country's outgoing receipt and matching actors in its own incoming registry, using a separate snapshot that nested host reconciliation cannot overwrite.
The `on_annex` and `on_civil_war_end_before_annexation` hooks call it on documented `FROM`, and the terminal helper calls it before clearing foreign context.
It is deliberately absent from ordinary relationship cleanup during transfer, defection, extraction, or assassination, when an operation can still be producing its valid result.
No world scan or new periodic scheduler is introduced.

Example for an irreversible terminal transition in the affected country's scope:

```text
brilliant_scientist_foreign_cleanup_country_operations = yes
```

### Evidence boundary

The native event timeout still closes intact response/report chains; participant-owned hooks provide the additional annex and terminal cleanup path.
Cleanup does not require `exists = yes`, which would reject the annexed country's supplied scope solely because it no longer owns territory.
The civil-war pre-annex hook has documented access before annexation; ordinary post-annex scope lifetime remains an engine-ordering acceptance question, not something proved by the source guard.
MCP's focused event evidence defers helper/lifecycle expansion, and the current cached-revision comparison failed with `EVENT_REVISION_NOT_CACHED`.
The artifact-backed retry rejected the trace report with `EVENT_GRAPH_ARTIFACT_INVALID` because its schema is not a supported comparison graph.
Passing source review is not presented as a substitute for that missing comparison.
Country pointers alone do not prove popup generation identity after annexation and re-release.

## Assets and localisation

Invitation, protection, observation, recruitment, theft, sabotage, defection, extraction, and assassination reports use `GFX_report_event_016_brilliant_scientist_appointment`.
Public challenge uses `GFX_report_event_016_brilliant_scientist_sovereignty_confrontation`, counter-program detection uses `GFX_report_event_016_brilliant_scientist_incident_machine_security`, and their actor reports use `GFX_report_event_016_brilliant_scientist_directorate_dossier`.
The countermeasure spirits and the Counter-Kruger Studies modifier reuse registered vanilla sprites: `GFX_idea_generic_radio_concern`, `GFX_idea_generic_secret_police`, `GFX_idea_generic_wall_line`, `GFX_idea_generic_radar`, `GFX_idea_generic_armor`, and `GFX_idea_generic_spy_intel`. No new art or sprite registration is needed.
- Countermeasure spirits: `common/ideas/016_brilliant_scientist_countermeasure_ideas.txt`
- Counter-Kruger Studies modifier: `common/dynamic_modifiers/016_brilliant_scientist_countermeasure_modifiers.txt`

- Category icon: `GFX_decision_category_SOV_soviet_academy_of_sciences`
- Decision icons: registered vanilla research, political-discourse, operation, and infiltration sprites
- Event file: `events/016_brilliant_scientist_foreign_events.txt`
- Scripted localisation: `common/scripted_localisation/016_brilliant_scientist_foreign_scripted_localisation.txt`
- English localisation: `localisation/english/016_brilliant_scientist_foreign_l_english.yml`

## Future extensions

- Public exposure decisions can convert detected evidence into a multilateral condemnation route.
- A successful protection compact can create a named joint-security state mission around the primary laboratory.
- Repeated country-to-country scientific bargaining can trade exact family stages rather than generic research bonuses.
- KRG diplomacy can reuse the actor ledger to distinguish former patrons, exposed assassins, thieves, and genuine scientific partners.
