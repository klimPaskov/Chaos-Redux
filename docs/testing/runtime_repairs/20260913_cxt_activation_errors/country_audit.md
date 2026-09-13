# CXT activation errors country audit

Status: narrow source and contract audit completed on 2026-09-13.

Scope: CXT country activation, runtime technology enumeration, and deferred condemnation refresh behavior.
Only this handoff and `country_inventory_check.json` are owned by this subagent.
The parent owns all gameplay source and the live-engine validation boundary.

## Verdict

The CXT country and transition contract is source-safe for the reviewed activation path.
The public console effect retains its activation-baseline scheduling, the hidden receiver still supplies `ROOT = CXT`, and initialization reaches the existing setup helpers only after the capital gate.
The condemnation changes preserve normal-country behavior and retain pending CXT refresh work until an owned capital exists.

The indexed technology loop is source-bounded and covers every index in `global.technology` for the currently evidenced 679-entry inventory.
The supplied native `has_tech: Invalid tech` and `set_technology: Invalid tech` pairs still leave the runtime representation or consumer acceptance unresolved, so this audit does not claim that complete technology granting is engine-verified.
No static list, guessed invalid-entry filter, donor-country substitute, disabled history call, or other fallback was introduced.

## Reviewed source surfaces

| Surface | Current source and finding |
| --- | --- |
| Runtime technology grant | `common/scripted_effects/chaosx_test_country_technology_effects.txt`, `chaosx_test_country_complete_all_technologies`; explicit count, indexed reads, native `has_tech`, and native `set_technology`. |
| CXT setup order | `common/scripted_effects/chaosx_test_country_effects.txt:273-318`; deferred condemnation flush is first in initial setup and in the registered-content synchronizer. |
| CXT public command | `common/scripted_effects/chaosx_test_country_effects.txt:320-352`; body is identical to the saved activation baseline, including delayed receiver scheduling before `change_tag_from`. |
| Condemnation deferral | `common/scripted_effects/condemnation_sanctions_effects.txt:349-385` and `1812-...`; only CXT without an owned capital is deferred. |
| Country receiver | `events/chaosx_test_country.txt`; previously accepted hidden triggered-only receiver supplies CXT country scope and capital preflight. |
| Static country inventory | `docs/testing/chaosx_test_country.md`; 83 project receipts, 71 equipment entries, 87 templates, and 261 static divisions remain the documented contract. |

## Technology grant contract

`chaosx_test_country_complete_all_technologies` captures `global.technology^num` into `chaosx_test_country_technology_count`.
It initializes `chaosx_test_country_technology_loop_break = 0` and runs `for_loop_effect` from zero while the loop index is less than the captured count.
Each iteration reads `global.technology^chaosx_test_country_current_technology_index` into `chaosx_test_country_current_technology` before passing that object directly to the unchanged native consumers.
The `has_tech = var:chaosx_test_country_current_technology` idempotence guard and `set_technology = { var:chaosx_test_country_current_technology = 1 popup = no }` consumer remain in place.
There is no entry filter, static technology inventory, inferred sentinel, or intentional early break.

The source-derived inventory count is 679, so the expected valid index range is zero through 678 and the loop remains below the installed `NGame.MAX_EFFECT_ITERATION = 1000` limit.
The saved boundary proof records zero reads for an empty array, one read at index zero for a one-entry array, and 679 reads at indices zero through 678 for the current count.
This is a source-boundary proof only; it does not prove that every array element is accepted by the native technology consumers.

The temporary `CXT_TECH_DIAGNOSTIC` logs remain intentionally present while the runtime issue is unresolved.
The supplied attachment reports two `has_tech`/`set_technology` invalid-tech pairs during history passes and another pair during receiver activation, without identifying the failing index, raw value, or token.
Because the error recurs during both history and receiver calls, removing or deferring history execution would not establish a complete repair.

The installed documentation supports the dynamic database count, indexed arrays, `for_loop_effect`, `has_tech`, and `set_technology` fields.
Vanilla dynamic-end precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/LAR_occupation.txt:247-254`, and indexed database-object precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/operation_strat_effects.txt:218`.
Neither source nor the available native analysis establishes a typed conversion that repairs the rejected runtime object.

## Condemnation deferral contract

`condemnation_recalculate_participants` queues `condemnation_participant_refresh_pending` only when the current country is CXT and has no owned capital state.
Its ordinary body is now `condemnation_recalculate_participants_apply`, whose body matches the activation baseline's original method after removing only the wrapper declaration.
The apply body still initializes the country, stores `THIS` as `condemnation_recalculation_target`, saves the same event target, and performs the same participant traversal and pair updates.

`condemnation_start_targeted_pulse` queues `condemnation_targeted_pulse_pending` under the same CXT-without-owned-capital condition.
Its ordinary body is now `condemnation_start_targeted_pulse_apply`, whose body matches the activation baseline's original method after removing only the wrapper declaration.
The apply body still sets the active flag and schedules `condemnation_sanctions.1` with the original pulse delay.

`condemnation_flush_deferred_refresh` requires an owned capital state, clears each pending flag immediately before calling its existing apply path, and does not clear either flag while CXT remains landless.
Both pending methods are consumed by the first line of `chaosx_test_country_initial_setup` and the first line of `chaosx_test_country_sync_registered_content`.
The initialized CXT receiver therefore flushes queued participant and targeted-pulse work after capital activation, while normal countries continue through the unchanged apply bodies.

The actor scope remains the existing country scope for each method.
The participant apply path still records `THIS` as the recalculation actor and uses its existing `ROOT` relationships inside the unchanged traversal.
No normal-country call site, score, AI weight, timed pulse body, native embargo body, or participant ledger was removed.

## CXT transition and preservation checks

The `chaosx_test` body is byte-equivalent to the activation baseline's public command body after line-ending normalization.
It still resolves CXT after the capital transfer, sets the one-hour setup delay, queues `chaosx_test_country.1` before `change_tag_from`, and performs the player transfer last.
The saved regular event targets therefore retain the origin and capital pointers for the delayed receiver under the documented event-target chain contract.

The hidden receiver and owned-controlled-capital preflight remain parent-owned and were not changed by this audit.
The receiver continues to support multi-state origins, one-state origins with an empty-annex guard, and initialized-CXT refresh without duplicating the static roster or registered processed markers.

The camp fixture's `genocide_responsible_country = PREV` assignment remains inside the CXT capital state scope before existing registration calls, so `PREV` is the CXT country and inherited capital responsibility is rebound without altering ordinary historical registration.

The following existing inventories remain preserved by the reviewed source contract: 83 special-project receipts, zombie fixture coverage, six facility types, 71 stockpile entries, 87 static templates, and 261 static divisions.
The registered extension bus and tag-scoped daily and weekly hooks remain in place.

## Country package coverage checklist

- [x] `CXT` tag registration, country definition, landless history, flag variants, and localisation remain wired through the existing country package.
- [x] Public `chaosx_test` and hidden `chaosx_test_country.1` identifiers remain stable.
- [x] Capital ownership, controller, receiver ROOT, one-state guard, initialized repeat path, and setup ordering are retained.
- [x] Condemnation participant and targeted-pulse requests are deferred only for landless CXT and are flushed after the capital gate.
- [x] The technology helper reads the complete current runtime index range without replacing the database-driven contract.
- [x] Existing project, equipment, unit, facility, doctrine, CBRN, camp, roster, and extension surfaces remain called by the original setup paths.
- [ ] Complete native acceptance of every runtime technology object remains unverified because the supplied invalid-tech pairs do not identify or explain the rejected object.

## File surface checklist

| Surface | Path and result |
| --- | --- |
| Country tag | `common/country_tags/chaosx_test_country.txt`; `CXT` registration remains present. |
| Country shell and history | `common/countries/Chaos Redux Test Country.txt` and `history/countries/CXT - Chaos Redux Test Country.txt`; dormant landless start remains intentional. |
| Public harness and setup | `common/scripted_effects/chaosx_test_country_effects.txt`; transition, actor ROOT, flush ordering, camp pointer, and roster calls remain present. |
| Technology helper | `common/scripted_effects/chaosx_test_country_technology_effects.txt`; indexed dynamic grant contract is present, with runtime consumer acceptance unresolved. |
| Unit helper | `common/scripted_effects/chaosx_test_country_unit_effects.txt`; 87-template/261-division source contract is preserved. |
| Condemnation system | `common/scripted_effects/condemnation_sanctions_effects.txt`; two CXT-only wrappers and one capital-gated flush are present. |
| Receiver event | `events/chaosx_test_country.txt`; hidden receiver remains the parent-owned ROOT rebasing surface. |
| Hooks | `common/on_actions/chaosx_test_country_on_actions.txt`; tag-scoped daily and weekly repair remains bounded. |
| Documentation | `docs/testing/chaosx_test_country.md`; transition, camp, inventory, and extension contracts remain documented. |

## Other country-package surfaces

No focus tree, decision, mission, leader, advisor, portrait, party, AI-weight, map rewrite, or new asset surface is introduced by this repair.
The existing neutral no-election identity shell, country localisation, and flags have no new missing dependency within this bounded review.

The state setup risk is limited to the documented landless CXT interval and to future technology inventories that exceed the installed 1000-iteration effect limit.
No generic capital or technology fallback was added.

## Evidence and limits

Relevant offline references were `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, and the installed `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, and `documentation/script_concept_documentation.md` under the vanilla HOI4 directory.
The stored activation baseline is under `docs/testing/runtime_repairs/20260913_cxt_activation_errors/baseline/`.
The adjacent `technology_handoff.md`, `technology_index_boundaries.json`, `technology_mcp_evidence.json`, and `condemnation_before_hashes.json` record the prior source and analysis evidence.

The technology MCP evidence reports 679 technologies and a known analysis boundary around variable and meta-generated identifiers.
The available native analysis does not execute the CXT helper or prove the rejected database object's representation, so source evidence is not treated as engine-equivalent evidence.
The exact `EVENT_REVISION_NOT_CACHED` and partial-helper limitations remain recorded in the parent MCP packet and are not reinterpreted here.

No game launch, console control, log search, restart, staging, commit, fallback, or unrelated source write was performed by this subagent.

## Disposition

Disposition: country transition and condemnation source contracts are accepted for parent review.
The technology implementation is complete as an indexed runtime contract but remains unresolved as a live native-consumer repair.
The parent must retain that limitation in the final repair report and remove the temporary diagnostic logging only after the runtime rejection is identified and resolved.
