# Event 016 International Scientific Contest

## Purpose

The international contest begins with Evolution II. It gives only relevant foreign countries a targeted decision category against the current Kruger host. It does not run from a daily, weekly, or monthly world loop: one bounded country scan initializes eligible actors when Evolution II opens and again after a successful host transfer.

Foreign behavior reacts to Security Exposure, host security, facility access, intelligence capability, ideology, diplomatic relations, war, alliance structure, project history, Grievance, Dependence, and Independent Capacity. The current host can answer visible diplomatic approaches and detected covert operations.

## Actor and target lifecycle

`brilliant_scientist_foreign_initialize_contest` clears stale target arrays, finds countries satisfying `brilliant_scientist_is_valid_foreign_actor`, and gives each actor a one-country target array containing the current host. The category remains visible only while Event 016 is in its international phase, Kruger is alive, the host is valid, and no terminal world state has locked the chain.

Each actor may conduct one live operation at a time. A host accepts at most two simultaneous incoming operations. Every timed action stores its actor, host, operation type, target project family, start date, outcome band, detection state, and later diplomatic attribution. Cancellation removes both actor and host locks.

## Foreign actions

| Action | Time | Base cost | Primary gates and results |
|---|---:|---:|---|
| Observe the program | 30 days | 15 Political Power | Diplomatic or intelligence access; builds a dossier and later operation access |
| Send a formal invitation | Immediate host event | 25 Political Power | Relations, ideology, faction, or academic access; host can refuse, permit a visit, or let Kruger decide |
| Recruit an assistant | 45 days | 30 Political Power | Access plus a project target; can acquire one family Theory stage or create exposure/scandal |
| Steal an archive | 60 days | 45 Political Power | Intelligence access and an unstolen project family; can acquire exact family knowledge once |
| Sabotage a project | 75 days | 55 Political Power | Hostile motive and an undamaged project family; damages only the selected family |
| Encourage defection | 60 days | 45 Political Power | Prior contact, diplomatic access, and a transfer-ready Kruger; success revalidates the character transfer |
| Extract Kruger | 75 days | 70 Political Power | Intelligence access, hostility, and a transfer-ready Kruger; partial success captures an assistant or knowledge |
| Offer protection | Immediate host event | 35 Political Power | Alliance, faction, guarantee, or patron access; creates full, limited, or refused protection memory |
| Attempt assassination | 90 days | 100 Political Power | Meaningful dangerous-project threat, hostile motive, and intelligence access; always produces attribution on a nonfailure |
| Publicly challenge the programme | Immediate host event | 35 Political Power | Authenticated observation, exposed research, detected operations, or a strategic project; host chooses demonstration, denial, publication, observers, sabotage explanation, or threat |

Diplomatic approaches use host events `.100` and `.110`. Covert routes use detected host events and paired actor reports across `.120` through `.181`.

## Outcome and detection model

Success and detection are separate bounded calculations. Actor capability includes an intelligence agency, operative count, network strength, major-power reach, prior observation, prior recruitment, joint-laboratory or controlled access, ideology, opinion, alliance, adjacency, and war.

Host vulnerability includes Exposure and the targeted project's stage. Recruitment and defection also read Grievance, Independent Capacity, and Dependence. Extraction and assassination become harder against strong Independent Capacity. Internal security, a compartmentalized military office, hardened laboratories, a multi-site network, completed loyalty reviews, protection agreements, and accumulated security alerts reduce success while increasing detection.

Detected operations cost the actor additional Political Power and stability, raise the host's persistent security alert, create bilateral opinion penalties, and allow the host to choose security escalation or diplomatic protest. These choices feed later containment strength and Grievance rather than disappearing after the report.

After at least one resolved Prototype, the first detected operation that resolves can also schedule `chaosx.nr16.9` on the host. The report retains the exact actor and operation from the foreign-resolution transaction. Controlled exchange is available only while the two countries are not at war and the operation is not extraction or assassination; it grants the actor one capped family-theory result from the host's latest breakthrough and a positive bilateral opinion modifier. A private warning applies a smaller negative opinion modifier and lowers Exposure, while public accusation applies the stronger modifier, raises Mandate and Exposure, and increases the actor's foreign-interest pressure. Host and `KRG_warren_kruger` receipts prevent replay, and the ordinary transfer, terminal, and sovereignty cleanup helpers clear or carry the reaction state without changing the foreign operation's existing success result.

The public challenge is a separate actor-owned operation with its own per-host resolution ledger. It requires the public-challenge interest threshold plus diplomatic or intelligence access and one of four evidence sources: a successful observation, exposed research, detected foreign operations, or a strategic project. The challenge is immediately delivered to the current host as `chaosx.nr16.190`, and the six host answers apply distinct Mandate, Exposure, Dependence, Project Capacity, Grievance, and diplomatic-memory consequences before the actor receives `chaosx.nr16.191`. It does not steal a project stage, create a special-project reward, or move Doctor Kruger, and its public detection is recorded in the normal foreign-operation history.

The host-facing foreign-operation reports (`chaosx.nr16.100`, `.110`, `.120`, `.130`, `.140`, `.150`, `.160`, `.170`, and `.180`) append the same retained host-archetype clause used by the Directorate reports. Universities, industrial hosts, militarized states, threatened governments, colonial administrations, refugee networks, and the default host therefore read invitations, observation, recruitment, theft, sabotage, defection, extraction, and assassination through their own institutional pressures. Actor after-action reports (`.101`, `.111`, `.121`, `.131`, `.141`, `.151`, `.161`, `.171`, and `.181`) use `GetBrilliantScientistForeignHostFlavorClause` to read the carried host target, so the reporting country does not accidentally substitute its own archetype or lose the original context.

## Transfer and assassination safety

Defection and extraction call the existing Event 016 guarded transfer transaction at the final rendezvous. The recipient and host are revalidated, Kruger cannot move while actively assigned to a special project, the old host is reconciled before nationality and roles move, and the original appointment reward is not replayed. A race lost to another transfer becomes a partial operation instead of creating another character.

Assassination can confirm death only for ordinary human continuity. Clone, machine, temporal, or proven extraterrestrial continuity converts a successful strike into injury, greater Grievance, greater Independent Capacity, higher Exposure, and the matching continuity record. A failed or partial attempt likewise changes the later sovereignty balance.

## Persistent history

Actor arrays retain observation, invitation, recruitment, theft, sabotage, defection, extraction, protection, and assassination history per host. The selected project family and stage remain recorded for exact follow-up descriptions and KRG route weighting. Opinion modifiers preserve invitation refusals, scientific contact, protection compacts, exposed operations, and diplomatic protests.

## Assets and localisation

The current reports use the registered Event 016 Kruger appointment image so every diplomatic and covert event has a valid asset while the shared Event 016 asset package is completed. No unregistered sprite is referenced.

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
