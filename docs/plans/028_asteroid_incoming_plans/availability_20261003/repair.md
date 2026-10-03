# Event 028 automatic availability and viable target pairs

Disposition: implemented in source, with native and probability evidence unresolved.
Acceptance basis: Part 2 and Part 10 require `N/A` and exclusion from automatic selection whenever three viable distinct pairs cannot exist, plus a valid surviving backup for each target country.

## Behavior and integration

`asteroid_incoming_country_has_viable_target_pair` is a country-scope predicate requiring an existing human country other than CXT with at least two usable owned and controlled states.
The current state validity predicate still owns population, meaningful settlement, passability, crater, fragment, and wasteland checks.
`asteroid_incoming_country_is_valid_target` combines that same viability predicate with the saved chooser exclusion, so random selection cannot consume a slot on a one-state or occupied-backup country.
`asteroid_incoming_country_has_backup_state` also rechecks full control of the separate backup when the selected pair is confirmed.
The country needs two broadly usable states and at least one fully controlled backup candidate.
The primary-center predicate requires a distinct fully controlled backup for that exact center, so a partially contested impact center can remain eligible without sacrificing government continuity.
The continent-preferred country query and best-state selector use that same center predicate, avoiding a false preferred match on a country's sole fully controlled state.

`asteroid_incoming_target_pool_can_exist` is a read-only acting-country trigger.
It requires three viable countries other than the acting country without drawing a random target or writing event targets, flags, variables, or arrays.
`asteroid_incoming_automatic_event_is_available` additionally rejects active, resolved, or already-presented transactions.
The shared `evaluate_event_pool_candidate_unavailability` calls it for Event 028.
The shared automatic pool and event-view availability therefore use the same rejection path.

Unavailability reason 45 is `asteroid_target_pool`, and reason 46 is `asteroid_transaction`.
Both have shared event-row and cluster-member reason selectors and final English localisation.
The existing disabled and already-fired precedence remains owned by the shared framework.
No event was enabled, no major weight or option weight was changed, and no new periodic on-action was introduced.

The shared `fire_event_by_temp_id_no_cluster` now invokes the existing Event 028 prefire helper before dispatch and Major accounting.
A failed construction clears partial target references and rejects dispatch, using the existing automatic retry-timer pattern.
The native fire-once root stays `chaosx.nr28.1`.
Cancel returns through internal event `chaosx.nr28.8`, whose five option conditions, effects, and weights match the entry board and whose trigger requires the original chooser, an active transaction, and no locked or resolved trajectory.
The return event has no immediate block, target generation, opening news, history append, or date reset.
It reuses the accepted tracking report sprite with no asset binary change.
An invalidated return board has only its explicit blocked option, which closes the transaction without choosing another coordinate, granting the miss achievement, or creating physical aftermath.

Both boards use a blocked-world description when their three saved pairs are no longer valid.
The internal option labels expand the original labels through localisation aliases.
The source validator compares all five before/return option bodies, exercises chooser and lock guards, verifies that Cancel cannot reroll, and checks that the readiness gate precedes dispatch and Major accounting.

The native iterator count fields use file-local literal mirrors of the shared cardinality constants.
The validator asserts that the mirrors remain equal to `minimum_target_pair_count = 3` and `target_country_minimum_usable_states = 2`.
This is a syntax representation of the fixed accepted cardinalities, and the original three-option design is retained.

## Evidence

Run `python .tools/validation/validate_028_availability.py --fixture docs/plans/028_asteroid_incoming_plans/availability_20261003/source_scenarios.json`.
The model parses the actual before and after trigger sources, evaluates only the declared scope/condition subset, and raises on unknown evaluated tokens.
It does not execute HOI4 or claim native iterator, event-view, or probability behavior.

| Case | After result | Concrete regression caught |
| --- | --- | --- |
| `AST_AVAIL_00`, `01`, `02` | Unavailable with zero, one, or two eligible countries | Automatic selection lacks three distinct pairs |
| `AST_AVAIL_03` | Available with exactly three viable countries | The boundary remains inclusive |
| `AST_AVAIL_DISTRACTORS` | Three eligible countries, available | Before source admitted five candidates including two one-state countries |
| `AST_AVAIL_OCCUPIED_BACKUP` | Two eligible countries, unavailable | Before source admitted the country whose second state was occupied |
| `AST_AVAIL_WASTELAND_BACKUP`, `EMPTY_BACKUP` | Two eligible countries, unavailable | Before source admitted the country on the strength of its sole surviving valid state |
| `AST_AVAIL_NONHUMAN` | Two eligible countries, unavailable | The shared actual-nonhuman exclusion remains in force |
| `AST_AVAIL_PARTIAL_CENTER`, `ONLY_FULL_STATE_IS_BACKUP` | Available with three eligible countries, and only the contested state can be the third center | The fully controlled state must remain the distinct backup |
| `AST_AVAIL_CONTESTED_BACKUPS` | Two eligible countries, unavailable | Neither third-country state is safe for the surviving government |
| `AST_AVAIL_TRANSFERRED_BACKUP`, `ANNEXED_TARGET` | Two eligible countries, unavailable | An old owned-state list or an absent country cannot supply the third pair |
| `AST_AVAIL_FRIENDLY_TARGETS` | Three eligible countries, available | Relations do not filter the human target pool |
| `AST_AVAIL_SYSTEM_CXT` | Two eligible countries, unavailable | The system country cannot consume a target slot |
| `AST_AVAIL_PENDING`, `RESOLVED`, `OPENING` | Unavailable despite three viable countries | Another opening cannot enter the automatic pool during or after the transaction |

No diplomatic condition appears in the viability predicate.
Neutral, allied, enemy, subject, or guaranteed countries retain the same geographic eligibility for the human chooser.
The existing option AI continues to own protected relationships.

## Immutable before sources

| File under `before/` | SHA256 |
| --- | --- |
| `028_asteroid_incoming_triggers.txt` | `EFA22ACB10085504B65E1C7DF95E47931E2B980D9A3780312CE0B65F885EC08F` |
| `028_asteroid_incoming_runtime_effects.txt` | `3662A248017DE946C19BDA1D395D892CB99A8A435B82F06FCDBCF7C0A90CB980` |
| `chaosx_logic_effects.txt` | `15E24FECD2A2F2D8C36050AADA773576AC77325C5CC216070DC71DDC208A8F10` |
| `028_asteroid_incoming_constants.txt` | `1403A2F46D41CB7668393C931C10AFC98091697763ADC8C88B786CC773A8EF7E` |
| `event_system_constants.txt` | `146306A31022D2FD2CF4C4E5BE6AED50E16E1A6837E02504366BF225B1BD8512` |
| `028_asteroid_impact.txt` | `4E7D1171DD2307B86875938036B33385B4240410879069A11C6587C43A57A51F` |
| `chaosx_settings_effects.txt` | `ABCCF7D64A359004D9AE106C2D40627D793E7F1C287A1CD2050CEDB97548B272` |

## References and limitations

During the initial repair the connected `ALL_TOOLS` inventory exposed zero `mcp__hoi4_agent_tools__` coding routes, and `source_lookup` and `script_validate` were undefined on the callable tool object.
The server's artifact resource template still responded, which establishes resource availability only.
That client exposure did not permit a narrower retry.
After the parent's continuation the coding routes became exposed, with an older `source_lookup` schema lacking `view` and `keyPath`, and no `script_validate` route.
Narrow reference context, corrected event trace, and one-state map requests were submitted again, with their evidence tracked separately from the completed source scenarios.
The read-only probability specialist was assigned the immutable before sources, after sources, and named cases for the required comparison.
No current numeric probability comparison is claimed.

The relevant offline `Scopes - Hearts of Iron 4 Wiki.md` section at lines 31 through 55 documents the `any_<object>` count threshold and scope iteration.
Installed `documentation/triggers_documentation.md` sections `any_country` at lines 1336 through 1343, `any_owned_state` at 1612 through 1619, `exists` at 2708 through 2715, and `is_owned_and_controlled_by` at 6079 through 6086 were read directly.
Its `any_collection_element` example at lines 1291 through 1315 supplies the installed count-three precedent.
The Event 028 target builder and shared Event 027/042 availability branches supplied the current project integration precedents.
This source evidence remains separate from native acceptance.

The offline Event modding section at lines 145 through 149 confirms that the native fire-once entry cannot be re-fired except through the console, which establishes the old Cancel defect.
Its lines 60 through 74 document ordered conditional descriptions.
Installed `events/Generic.txt` at lines 11 through 25 supplied the corresponding native conditional-description precedent.
The current shared Event 013 and Event 021 prefire blocks supplied the dispatcher readiness pattern.

Reference revisions read directly: offline Scopes SHA256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`, offline Event modding `96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D`, installed triggers documentation `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`, and installed `Generic.txt` `96D510E119EC0548C3957689395674C7361C6689D2C7D0D65D1C0E024956EC26`.
The installed full-control trigger section at lines 5585 through 5592 was also read while reconciling backup viability.
The final local suite contains nineteen availability cases plus returning-board and dispatcher-order checks.

The read-only probability auditor's separate client exposed the required tools, unlike the parent's client.
Valid calls and narrower queries still timed out after 600 seconds and returned no usable artifact, revision, scenario hash, or numeric comparison.
Its returned source review confirmed the original thirteen-case patch and matching `.1`/`.8` option formulas, while explicitly distinguishing target preflight from the disabled automatic event and zero initial Major weights.
Default disablement remains required until the full package's gates close, and Major pacing remains unchanged.
