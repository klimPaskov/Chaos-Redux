# Event 120: Repository evidence and capability boundaries

## Revision and limits

The read-only inspection used the public [klimPaskov/Chaos-Redux repository](https://github.com/klimPaskov/Chaos-Redux) at commit [41bc4e5045a7b5c131be69dda2f08079d478634c](https://github.com/klimPaskov/Chaos-Redux/commit/41bc4e5045a7b5c131be69dda2f08079d478634c), dated 18 October 2026. Inspection occurred after the supplied-source gate on 23 October 2026. The dated uploaded skill set supplies newer workflow rules where it explicitly revises the repository guidance.

This was bounded repository research, with full reads of selected contracts and precise excerpts of large implementation files. It was not a complete repository read. The canonical catalog workbook was identified through metadata, but its cells were not opened. No gameplay, catalog, asset, settings or repository file was modified. No HOI4 MCP tools or mounted Windows game installation were available. No game launch or live test occurred.

The user's brief controls the current event identities and desired behavior. An older catalog entry does not authorize replacing an unrelated implementation or allocating a shared identifier.

## R01. Current event identity and catalog discrepancy

The bounded search found no Event 120 or 131 root implementing Widespread Mutiny and no completed registration for this requested event. The current exported catalog still assigns 120 to Massive Volcano Eruption and lists Widespread Mutiny under 131 as unavailable. It also uses 114 for Fuel crisis, 124 for Demilitarization, 116 for This is SPARTA!!! and 127 for Warlords, with a mismatched autonomy description on the latter row.

The active Demilitarization design already lives under `docs/specs/114_demilitarization_specs/`. Event 009 White Peace has an implemented root. These observations require identity reconciliation before writing runtime files or editing the workbook. They do not change the user's requested 120, 114, 009 and 116 meanings.

The canonical workbook is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, observed size 98,437 bytes and blob `8898385d0cb4d8993b4818557acd9b64d2caec2a`. This metadata does not establish its current rows, formatting or available reservations. The XLSX remains the writable catalog authority. CSV files are exports. Requested planning status is To Be Reworked, with implementation state and default enablement reported separately. No Playable promotion is authorized by this package.

## R02. Event 019 preserves a narrower generated-unit contract

The inspected [Event 019 derivative transaction source](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt) contains real freeze, stage, destination-proof and source-consumption work for its own generated cohorts.

| Inspected region | What it establishes |
| --- | --- |
| Lines 1171–1232, natural derivative preparation | Freezes Event 019 UID, cohort, template, lot, origin, starting factors and related ledger fields |
| Lines 2469–2537, unit recreation | Builds the destination from recorded starting experience, equipment and manpower factors after private lot/template validation |
| Lines 3975–4053, source deletion and proof | Revalidates Event 019 identity and stored division scope, deletes without disband refund and checks source absence and count change |
| Lines 5410–5510, transaction coordinator | Prepares and stages, creates a dynamic actor, proves destination and commits the source accounting |

The [Event 019 uncertainty document](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/019_infantry_spawn_specs/review/blockers_and_uncertainty.md) records an owner-approved reconstruction exception. It excludes preservation of exact current equipment variants and holdings, manpower fill, organization, gained experience, medals, officer history, assignments and orders. Its earlier HOI4 1.19.2 capability review is historical evidence, not a fresh inspection of an installed game here.

The General Mutiny scenario in [019_infantry_spawn_scenario_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/019_infantry_spawn_scenario_effects.txt), inspected at lines 832–897 and 1339–1381, materializes new random lots. It does not transfer a selected ordinary existing army.

Event 120 can learn from the transaction structure. It cannot inherit that narrower exception or call generated troops the same existing formations. No such substitution was accepted for this task.

## R03. Event 021 records fronts and actors, with explicit formation limits

The complete [Event 021 front-ledger contract](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/021_random_civil_war_front_ledger_effects.md) and the first 180 lines of its [implementation](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/021_random_civil_war_front_ledger_effects.txt) were inspected.

The ledger binds host, crisis, registered actor, front identity and immutable state membership, with consumed or rejected transaction status. It rejects missing rows instead of deriving replacement geography from the current map. Its secondary-transfer validator checks territory, the surviving source remnant and requested division count, then derives a country fraction from the live army size.

The contract expressly states that the validator changes no units and that five-decimal fractional injection does not promise exact integer division transfer. Its front is a crisis-owned actor and region record. The inspected evidence does not establish an engine battle-plan front object, exact opposing formation membership or a sector combat-exclusion operation.

## R04. Native operations still requiring proof

| Required behavior | Inspected evidence | Remaining boundary |
| --- | --- | --- |
| Durable identity of an arbitrary existing division | Supplied current unit guidance documents division scope and selected organization operations. Event 019 stores its generated scopes and UIDs | Persistence through split, merge, reassignment, foreign control and transfer is unproved for ordinary existing formations |
| Nonfatal partial desertion and protected discharge | Current guidance describes unit destruction and refunded disband. Event 114 plans exact fielded-personnel outcomes | Exact nonfatal deployed-personnel removal, actual automatic refunds and protected return accounting still need native proof |
| Selected formation transfer with required live state | Offline effect documentation describes country-fraction transfer. Event 019 reconstructs under its accepted limitations | No inspected operation meets the full Event 120 preservation contract |
| Enforced refusal of a particular duty | Organization changes are documented, and current guidance identifies battle-plan scripting limits | An organization reduction alone does not prove refusal of a selected human order |
| Local ceasefire while national war continues | Offline AI guidance describes `front_control` as AI order preferences. Diplomacy documents country-target peace and truce | No inspected signature enforces the requested sector restriction against human manual orders |
| Country-ending return and limited settlement | Country and diplomacy guidance identifies recipient context and legal ownership concerns | Exact player-control transfer, state settlement, participating wars and survivor outcomes need proof in the chosen implementation |

Relevant pinned offline references are [AI modding](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/paradox_wiki/AI%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md), lines 340–365, and [Effects](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/paradox_wiki/Effects%20-%20Hearts%20of%20Iron%204%20Wiki.md), lines 1490–1530. The current live web wiki was not used as native version evidence.

Event 021 mediation effects at [lines 527–589](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/021_random_civil_war_decision_effects.txt#L527-L589) create a dated mediation receipt, ease pressure, add authority and open settlement talks. They do not themselves impose a sector combat lock. This is a bounded call-site finding, without a claim to have audited every transitive helper in the repository.

These are precise missing proofs for required behavior. They are not a claim that a future engine version can never support it. The package retains the full design and prohibits a silent substitute.

## R05. The three owner connections

### 114 Demilitarization

The complete [Desertion specification](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/114_demilitarization_specs/114_demilitarization_desertion.md) requires actual loss from fielded forces, legitimate ownership, formation continuity, measured returns and equipment accounting. It explicitly distinguishes those outcomes from a manpower-pool deduction or an organization penalty. Its partial-desertion design retains equipment in the surviving formation.

The [world-interactions contract](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/114_demilitarization_specs/114_demilitarization_world_interactions.md), lines 30–36, gives physical ownership to the first committed transaction. The later owner revalidates and skips consumed targets. Pressure and physical outcome receipts remain separate.

No live 114-to-120 adapter was established. Passing already-debited departed personnel to a new recipient must also consume or transfer the delayed-return liability once. The specification alone does not prove that operation.

### 009 White Peace

[events/009_white_peace.txt](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/events/009_white_peace.txt), lines 1–47, prepares a validated context, settles in immediate effects and reports afterward. Acknowledgment is not the settlement executor.

In [009_white_peace_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/009_white_peace_effects.txt), `score_white_peace_pair` at lines 664–706 has no mutiny input. `apply_white_peace_pair` at lines 957–1017 revalidates and settles the exact pair, with no Event 120 stand-down hook. `apply_white_peace_current_context` at lines 1134–1189 suppresses duplicate ordinary on-peace Chaos credit during its own bounded work.

These are the owner boundaries for the planned score adapter and post-settlement notification. A country remaining in another war cannot be treated as unsettled merely because `has_war` remains true. The actual settled relationship is required.

### 116 Warlords

No usable live Event 116 receiving-army owner contract was discovered. Warlord-like actors belonging to Events 014 and 019 do not establish that contract. The required receiving interface must prove the actual recipient, local viability, acceptance, exact destination and completed transfer. This remains future owner work.

## R06. Country carriers and protected content

The parent fully read [country collections](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/collections/chaosx_country_collections.txt) and the [Event 006 country registry API](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/006_independence_wave/systems/country_registry.md) after accepting a persistent council package.

Collections provide active country scopes. Dormant reservations require the static registry, exact package row, tag and anchor. Tag membership does not grant content readiness. Event 120 must record its own origin and apply its own overlay, without calling Event 006 setup merely because a carrier belongs to that collection.

Shared carriers require package and territorial resolution. Existing carrier history and meaningful vanilla, Independence Wave or Soviet-successor focus trees remain protected. The registry's prior collision audit is evidence of that earlier run. It does not certify a new allocation against the current installed vanilla, mod, local-mod and Workshop definitions.

## R07. Costs and current human-crisis policy

The parent read the [universal cost modifier contract](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/systems/universal_cost_modifier.md). Supported costs require the exact authoritative quote, inclusive affordability, one actual debit and receipts for actual payment, settlement and refunds. Temporary helper outputs are initialized by the caller. Owner lifecycle, targets and AI remain owner responsibilities.

Factory commitments are not established as a universally supported cost component. They require a verified native reservation or a complete owner adapter. The shared framework does not promise atomic rollback across arbitrary unrelated effects. Complete preflight, measured outcomes and explicit interruption handling remain necessary.

The inspected [crisis-pressure effect](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/chaosx_crisis_pressure_effects.txt) and exact active trigger still depend on an optional non-AI setting flag. The newer uploaded Mechanics direction requires harder human-country crisis pressure without a disabling toggle. This is an explicit source/runtime discrepancy. Implementation must reconcile the shared owner once and avoid restoring an Event 120 toggle or applying the same adjustment twice.

## R08. Shared identifiers and source authority

The complete [shared identifier registry](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/specs/shared_identifier_registry.md) separates event, presentation, audio, scenario, cluster and country namespaces. Presentation 120 is already reserved for Event 099 The World of Dust. SCN-013 belongs to Event 019. Neither is available to Event 120 by numerical similarity.

[event_cluster_constants.txt](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/script_constants/event_cluster_constants.txt) defines Domestic Unrest as cluster 16. Member rows 16001 through 16004 are occupied. The Low severity floor and cluster unlock tier are 0, independently of the requested event Chaos level 1. The registry's older proposed-state wording is stale against those runtime definitions.

No concrete new tag, cluster-member row, presentation, audio, achievement or scenario identifier was allocated. Before allocation, the implementer must reconcile the canonical workbook, live definitions, registry and active spec reservations. Country creation additionally requires a current installed-source collision scan.

Current source rules resolve several other conflicts. Focus design is path-level, with exact nodes and coordinates left to implementation. Player text remains direction only. Super-event audio follows the current OGG music contract rather than older WAV instructions. Achievement art uses completed, grey and not-eligible states. The supplied modern source corpus and its provenance are indexed in the [coverage record](120_widespread_mutiny_source_coverage.md).

## R09. Current MCP handoff contract

The parent read the tool routes, local-reference workflow, complete handoff-evidence section and event-chain coverage section in [the pinned MCP integration guide](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/systems/hoi4_agent_tools_mcp_integration.md), lines 26–86 and 108–212. The coding prompt's MCP Usage Map follows those documented distinctions between full and focused event analysis, preserved source baselines, complete probability pools, exact artifact retrieval and native evidence. These are documented future workflows. Tool discovery in this planning session exposed no HOI4 MCP route, so no domain call or successful MCP result is claimed.
