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
| Recruit an assistant | 45 days | 30 Political Power | Access plus a project target; can acquire one family Theory stage or create exposure/scandal |
| Steal an archive | 60 days | 45 Political Power | Intelligence access and an unstolen project family; can acquire exact family knowledge once |
| Sabotage a project | 75 days | 55 Political Power | Hostile motive and an undamaged project family; damages only the selected family |
| Encourage defection | 60 days | 45 Political Power | Prior contact, diplomatic access, and a transfer-ready Kruger; success revalidates the character transfer |
| Extract Kruger | 75 days | 70 Political Power | Intelligence access and a transfer-ready Kruger outside the actor's faction; partial success captures an assistant or knowledge |
| Offer protection | Immediate host event | 35 Political Power | Diplomatic access without war; creates full, limited, or refused protection memory |
| Attempt assassination | 90 days | 100 Political Power | Meaningful dangerous-project threat, hostile motive, and intelligence access; always produces attribution on a nonfailure |
| Publicly challenge the programme | Immediate host event | 35 Political Power | Authenticated observation, exposed research, detected operations, or a strategic project; host chooses demonstration, denial, publication, observers, sabotage explanation, or threat |
| Build a counter-Kruger programme | 120 days | 60 Political Power + 250 support equipment | Intelligence access, a project evidence receipt, and an active host project; records a family-specific countermeasure and improves later operations against the same host |

Diplomatic approaches use host events `.100` and `.110`. Covert routes use detected host events and paired actor reports across `.120` through `.181`.

## Outcome and detection model

Success and detection are separate bounded calculations. Actor capability includes an intelligence agency, operative count, network strength, major-power reach, prior observation, prior recruitment, joint-laboratory or controlled access, ideology, opinion, alliance, adjacency, and war.

Host vulnerability includes Exposure and the targeted project's stage. Recruitment and defection also read Grievance, Independent Capacity, and Dependence. Extraction and assassination become harder against strong Independent Capacity. Internal security, a compartmentalized military office, hardened laboratories, a multi-site network, completed loyalty reviews, protection agreements, and accumulated security alerts reduce success while increasing detection.

Detected covert operations cost the actor additional Political Power and stability, raise the host's persistent security alert, create bilateral opinion penalties, and allow the host to choose security escalation or diplomatic protest.
These choices feed later containment strength and Grievance rather than disappearing after the report.
Public challenges use their separate public consequence set and do not incur the covert detection surcharge.

After at least one resolved Prototype, the first detected operation that resolves can also schedule `chaosx.nr16.9` on the host. The report retains the exact actor and operation from the foreign-resolution transaction. Controlled exchange is available only while the two countries are not at war and the operation is not extraction or assassination; it grants the actor one capped family-theory result from the host's latest breakthrough and a positive bilateral opinion modifier. A private warning applies a smaller negative opinion modifier and lowers Exposure, while public accusation applies the stronger modifier, raises Mandate and Exposure, and increases the actor's foreign-interest pressure. Host and `KRG_warren_kruger` receipts prevent replay, and the ordinary transfer, terminal, and sovereignty cleanup helpers clear or carry the reaction state without changing the foreign operation's existing success result.

The public challenge is a separate actor-owned operation with its own per-host resolution ledger. It requires the public-challenge interest threshold plus diplomatic or intelligence access and one of four evidence sources: a successful observation, exposed research, detected foreign operations, or a strategic project. The challenge is immediately delivered to the current host as `chaosx.nr16.190`, and the six host answers apply distinct Mandate, Exposure, Dependence, Project Capacity, Grievance, and diplomatic-memory consequences before the actor receives `chaosx.nr16.191`. The host confrontation uses the sovereignty-confrontation card and the actor's after-action report uses the Directorate dossier card. It does not steal a project stage, create a special-project reward, or move Doctor Kruger, and its public detection is recorded in the normal foreign-operation history.

The counter-Kruger programme is a separate one-use actor operation. It requires the counter-program interest threshold, intelligence access, an active host project, a prior observation, recruitment, theft, public-challenge, or strategic-project evidence receipt, and 250 support equipment. The 120-day operation selects the host's most advanced family through the existing project-target helper; a successful result records the host and family in the actor's countermeasure arrays, while a partial result records only a failed family study. The actor's later operation score against that same host receives the bounded `countermeasure_previous` bonus, and the programme never grants a project stage, a second Kruger, or a unit. A detected operation opens `chaosx.nr16.193` before the actor report `.194`; the host response uses the machine-security incident card and the actor report uses the Directorate dossier card, while the dedicated response still avoids the generic controlled-exchange reaction so countermeasure work cannot accidentally become a full project-theory reward.

The host-facing foreign-operation reports (`chaosx.nr16.100`, `.110`, `.120`, `.130`, `.140`, `.150`, `.160`, `.170`, and `.180`) append the same retained host-archetype clause used by the Directorate reports. Universities, industrial hosts, militarized states, threatened governments, colonial administrations, refugee networks, and the default host therefore read invitations, observation, recruitment, theft, sabotage, defection, extraction, and assassination through their own institutional pressures. Actor after-action reports (`.101`, `.111`, `.121`, `.131`, `.141`, `.151`, `.161`, `.171`, and `.181`) use `GetBrilliantScientistForeignHostFlavorClause` to read the carried host target, so the reporting country does not accidentally substitute its own archetype or lose the original context.

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

`brilliant_scientist_foreign_record_resolution` appends one row to each party only when the matching receipt is unrecorded.
`brilliant_scientist_foreign_cancel_operation` clears that receipt's response phase, records cancellation only if no result exists, and calls the guarded finish.
`brilliant_scientist_foreign_finish_operation` runs in actor scope and requires a recorded matching receipt with no pending response before releasing the host slot and live variables.
`brilliant_scientist_foreign_align_history_metadata` is country-scoped, takes no input, pads only missing metadata, and never grants gameplay rewards.

Example of a delayed observation callback:

```text
set_temp_variable = { brilliant_scientist_foreign_expected_operation = constant:brilliant_scientist_foreign_operation.observation }
brilliant_scientist_foreign_resolve_covert_operation = yes
```

### Remaining lifecycle evidence

The documented native event timeout closes intact response/report chains, but a destroyed or annexed event recipient still needs bounded orphan-receipt cleanup evidence.
The receipt guard does not itself schedule such cleanup and must not be presented as proving it.
Country target pointers alone are not proof of popup generation identity after annexation and re-release.
These limits remain in the foreign lifecycle handoff; no periodic world scan is introduced.

## Assets and localisation

Invitation, protection, observation, recruitment, theft, sabotage, defection, extraction, and assassination reports use `GFX_report_event_016_brilliant_scientist_appointment`.
Public challenge uses `GFX_report_event_016_brilliant_scientist_sovereignty_confrontation`, counter-program detection uses `GFX_report_event_016_brilliant_scientist_incident_machine_security`, and their actor reports use `GFX_report_event_016_brilliant_scientist_directorate_dossier`.
This receipt checkpoint changes no art or sprite registration.

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
