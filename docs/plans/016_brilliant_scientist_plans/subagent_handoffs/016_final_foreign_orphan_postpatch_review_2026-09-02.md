# Event 016 foreign-operation orphan settlement postpatch review

Date: 2026-09-02

Scope: read-only source review against baseline `f3725655256cf5e98374366c5b63c8d44a3fc6a0` for the foreign decisions, effects, triggers, events, Event 016 on-action hooks, terminal caller, and promoted completion contract. No gameplay, localisation, balance, GUI, MCP, game, log, or unrelated documentation changes were made by this subagent. The only file written by this subagent is this handoff.

## Disposition summary

No P0 or demonstrated P1 source defect was found in the documented annex/pre-annex/terminal settlement path for current valid receipts.

P1 coverage boundary for the broader foreign-lifecycle completion claim, not a demonstrated regression: no reachable non-annex country-destruction call site was identified in the repository or Event 016 surfaces. The repository contains `annex_country` call sites, which are covered by `on_annex` and the civil-war pre-annex hook, but no separate country-destruction effect was found. The remaining uncertainty is whether an external/native path can make a stored country scope unenterable without those hooks. The private cancellation core is gated by `brilliant_scientist_foreign_owned_receipt_is_valid`, which itself must enter the stored `var:brilliant_scientist_foreign_operation_host_scope`. If that scope is no longer enterable, the actor cannot clear its live or pending receipt through the current source. A detected dispatch sets `brilliant_scientist_foreign_host_response_pending` before trying to fire the host event (`common\scripted_effects\016_brilliant_scientist_foreign_effects.txt:1723-1766`), and the available documentation does not prove that the native event timeout will settle an unenterable recipient. This is the explicitly documented next-checkpoint coverage requirement, not a demonstrated defect in the supplied annex/pre-annex/terminal paths.

The previously raised clamp concern is rejected and closed by the owner checkpoint. The accepted contract requires reconciliation from the matching retained entries, while the maximum-two rule remains a start-availability gate. `brilliant_scientist_foreign_reconcile_incoming_operations` therefore correctly assigns the true retained cardinality (`common\scripted_effects\016_brilliant_scientist_foreign_effects.txt:347-373`); clamping a three-entry malformed array to two would misreport live slots, and dropping a valid third actor would lose an active receipt. No P2 clamp finding remains.

Pre-pointer active receipts are out of scope by design under the new-save acceptance boundary. The source deliberately fails closed instead of fabricating a host pointer, so this checkpoint makes no old-save migration claim; every current accepted start sets the pointer at its start boundary.

## Source acceptance by lifecycle boundary

The start boundary stores the original host scope and numeric identity before mutating the host registry (`common\scripted_effects\016_brilliant_scientist_foreign_effects.txt:59-86`). All eleven operation types enter through `brilliant_scientist_foreign_start_is_valid`; each route-specific `brilliant_scientist_foreign_can_*_target` helper retains the one-live-actor, current-host, permanent-target, diplomacy/intelligence/project, and host-capacity requirements (`common\scripted_triggers\016_brilliant_scientist_foreign_triggers.txt:214-387,391-439`). The decision files continue to use `fire_only_once = yes` and type-specific permanent resolved-target arrays.

`brilliant_scientist_foreign_owned_receipt_is_valid` pairs the actor live flag/type fields and numeric host id with the stored host scope, checking the host's id from inside `var:` scope (`common\scripted_triggers\016_brilliant_scientist_foreign_triggers.txt:443-450`). This is a valid source-level ownership proof for current receipts, and it intentionally does not add `exists = yes` to annex cleanup.

The actor-only record core writes one actor history row and one aligned host row without regular event-target recreation or reaction dispatch (`common\scripted_effects\016_brilliant_scientist_foreign_effects.txt:269-318`). The ordinary wrapper retains original actor/host event targets and dispatches recognition/reaction only when the response context remains valid (`:324-342`). The actor finish core appends the type-specific resolved target, clears the actor live receipt before reconciliation, rebuilds the original host registry, and clears the host pointer last (`:378-440`).

Cancellation is idempotent. An unresolved matching receipt is assigned the cancellation result and recorded once; an already-recorded success, partial, or failure is preserved. Pending state is cleared before finish, and no private cancellation core fires a reaction or response (`common\scripted_effects\016_brilliant_scientist_foreign_effects.txt:451-474`). A stale event or report cannot cancel a different receipt because the public wrappers retain the regular actor/host targets and fixed expected operation.

The host reconciler snapshots the persistent actor array, deduplicates it in a separate temporary array, retains only actors whose pointer and numeric id identify the current host, rebuilds the persistent array after iteration, and recomputes the assassination marker (`common\scripted_effects\016_brilliant_scientist_foreign_effects.txt:347-373`). This follows the offline array documentation: do not mutate the source array during `for_each_scope_loop`, and use `PREV` to return to the host scope when rebuilding. The cleanup snapshot uses a separate temporary name from the reconciler (`:479-501`), so nested cancellation of one actor cannot clear the outer candidate set.

The Event 016 `on_annex` hook calls cleanup in documented `FROM` annexed-country scope before the existing defeat-victor path, and `on_civil_war_end_before_annexation` calls the same idempotent cleanup while `FROM` is documented to still exist (`common\on_actions\016_brilliant_scientist_project_on_actions.txt:81-95`). The terminal caller runs foreign cleanup before clearing foreign context (`common\scripted_effects\016_brilliant_scientist_effects.txt:3884-3890`). Ordinary relationship cleanup remains free of foreign orphan cancellation (`common\scripted_effects\016_brilliant_scientist_foreign_effects.txt:1425-1452`), preserving the transfer/extraction/assassination operation that is still resolving.

## Operation and response coverage

The finish core contains one branch for every constant in `brilliant_scientist_foreign_operation` (`common\script_constants\016_brilliant_scientist_foreign_constants.txt:10-28`), and every branch writes the original host scope to its matching permanent resolved-target array before clearing the receipt.

| Operation type | Permanent final-target array | Response/report path | Source disposition |
|---|---|---|---|
| `observation` | `foreign_observation_resolved_targets` | Host `chaosx.nr16.120` when detected; actor report `chaosx.nr16.121` | Guarded and mapped. |
| `formal_invitation` | `foreign_invitation_resolved_targets` | Immediate host event `chaosx.nr16.100`; actor report `chaosx.nr16.101` | Guarded and mapped. |
| `assistant_recruitment` | `foreign_recruitment_resolved_targets` | Host `chaosx.nr16.130`; actor report `chaosx.nr16.131` | Guarded and mapped. |
| `archive_theft` | `foreign_theft_resolved_targets` | Host `chaosx.nr16.140`; actor report `chaosx.nr16.141` | Guarded and mapped. |
| `project_sabotage` | `foreign_sabotage_resolved_targets` | Host `chaosx.nr16.150`; actor report `chaosx.nr16.151` | Guarded and mapped. |
| `encourage_defection` | `foreign_defection_resolved_targets` | Host `chaosx.nr16.160`; actor report `chaosx.nr16.161` | Guarded and mapped. |
| `extraction` | `foreign_extraction_resolved_targets` | Host `chaosx.nr16.170`; actor report `chaosx.nr16.171` | Guarded and mapped. |
| `protection_offer` | `foreign_protection_resolved_targets` | Immediate host event `chaosx.nr16.110`; actor report `chaosx.nr16.111` | Guarded and mapped. |
| `assassination_attempt` | `foreign_assassination_resolved_targets` | Host `chaosx.nr16.180`; actor report `chaosx.nr16.181` | Guarded and mapped. |
| `public_challenge` | `foreign_public_challenge_resolved_targets` | Immediate host event `chaosx.nr16.190`; actor report `chaosx.nr16.191` | Guarded and mapped. |
| `counter_program` | `foreign_counter_program_resolved_targets` | Host `chaosx.nr16.193`; actor report `chaosx.nr16.194` | Guarded and mapped. |

The eight delayed decision callbacks set a fixed expected operation before `foreign_resolve_covert_operation`; the three immediate diplomacy operations set their own fixed type in every event option. The actor report events set the same fixed type before `foreign_finish_operation`. The relevant callback predicates are `brilliant_scientist_foreign_callback_matches_active_operation`, `brilliant_scientist_foreign_event_receipt_matches_active_operation`, `brilliant_scientist_foreign_host_response_is_pending`, and `brilliant_scientist_foreign_actor_report_is_ready` (`common\scripted_triggers\016_brilliant_scientist_foreign_triggers.txt:453-529`).

The fixed tuple of original actor, original host, and operation type is sufficient under the current contract because `fire_only_once` and the permanent per-type resolved-target arrays prevent a valid same-pair/type reuse. An old timer or response with a different type, actor, or host fails its guard. If another caller clears a resolved-target array or fabricates a new receipt without honoring the permanent exclusion, there is no generation token and a same-pair/type collision is possible; that is an external contract violation, not a normal source path.

## Focused adversarial traces

An old callback for actor A after actor A starts a different operation B fails the fixed expected type or host-id check and cannot clear B. A late report requires the original actor and host event targets, a recorded flag, and no pending response; it cannot settle a newer receipt.

For two assassins A and B at one host, finishing A clears A's live flag before nested reconciliation, so the host snapshot retains B and recomputes the assassination marker. Finishing B then clears the marker and leaves an empty registry. Duplicate A entries are deduplicated before rebuild; a stale entry whose actor now points to another host is pruned from the current host array without touching that actor's different-host receipt.

For an already-recorded result, private cancellation clears pending state and finishes without assigning `cancelled` or writing another history row. For a delayed target-loss cancellation, the unresolved receipt receives exactly one cancellation row and its permanent resolved-target exclusion is retained.

For transfer and extraction, `brilliant_scientist_foreign_attempt_selected_transfer` keeps the operation receipt and original operation targets separate from the transfer recipient target, while `brilliant_scientist_clear_foreign_relationships` does not invoke foreign orphan cancellation. For assassination, the confirmed-death path may clear ordinary foreign relationship context before the resolver records the operation, but it does not clear the operation actor/host event targets or the new actor-owned host pointer; the record wrapper can therefore still write the final history when that pointer is enterable. If the scope has already disappeared, the P1 limitation above applies.

## Scope and engine evidence limits

The source review used the required offline `paradox_wiki\Data structures`, `Triggers`, `Effects`, `Scopes`, `On actions`, `Event modding`, and `Decision modding` pages, plus the installed vanilla documentation `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `script_collection_input.md`, and `script_collection_operator.md`. The relevant references support regular scope variables and `var:` entry, `PREV` parent restoration, arrays of scopes, `is_in_array`, post-loop reconstruction, and `on_annex`/`on_civil_war_end_before_annexation` ROOT/FROM ordering. Vanilla `common\on_actions\09_aat_on_actions.txt` and `05_lar_on_actions.txt` provide matching pre-annex/on-annex ordering precedent, while repository decisions and effects use regular variables that store country scopes and later enter them with `var:`.

No independent MCP call, game launch, save test, or log inspection was made in this postreview. The owner checkpoint records the current narrow before/after `.100` inspections as `EVENT_INSPECTED_PARTIAL` with `validation = false` and the option renders as `EVENT_RENDERED_PARTIAL`. Its exact cached-revision comparison between source revisions `3237301e947374484a4e3989e24f59d677c110075673b4a555a02fb02a907dfc` and `27c77545e9241b4398d074f7bae0aaedf8ebba6790c26141f6e3508bf4238175` returned `EVENT_REVISION_NOT_CACHED`. The artifact-backed comparison of those returned trace resources returned `EVENT_GRAPH_ARTIFACT_INVALID`, with the explanation that the report uses an unsupported graph schema version. Neither compare produced an acceptance artifact; these statuses are copied from `016_final_foreign_orphan_owner_checkpoint_2026-09-02.md`, not from an earlier checkpoint. No visual or live-lifecycle completion claim is made here.

The remaining engine questions are whether every ordinary post-annex path still permits entering the supplied `FROM` scope, whether a stored country-scope variable remains enterable after non-annex destruction, and whether native timed-event timeout/cancellation runs after a recipient becomes unenterable. The source cannot answer those questions without the unavailable runtime evidence.

## Narrow non-foreign surfaces

No foreign decision cost, duration, AI weight, outcome formula, localisation, category, GUI, or mission definition changed in the reviewed patch. The parent probability owner remains responsible for weighted-operation evidence. The category and visual-density review is therefore not claimed here; this handoff is limited to receipt identity, history, response routing, registry reconciliation, and terminal/annex cleanup.

## Current SHA-256 evidence

The following hashes were captured after the source review and identify the reviewed working-tree files:

| File | SHA-256 |
|---|---|
| `common\decisions\016_brilliant_scientist_foreign_decisions.txt` | `EB163AE804104D01D68B2E2DFC4E76896FD6069812039E33E1A072F829052D62` |
| `common\scripted_effects\016_brilliant_scientist_foreign_effects.txt` | `EC1D4D5038733C8D14DE3D505CF4DF76039C1BFF2B4A2A436A651D967E22AE3C` |
| `common\scripted_triggers\016_brilliant_scientist_foreign_triggers.txt` | `386F1C5916597942D847CB5964C5F363CC4925B7588D6BF9A5982A2D2C415F59` |
| `events\016_brilliant_scientist_foreign_events.txt` | `2B6629FC445F8D495867FBA26B85B44D5EB4715665D14690AF412E874D763264` |
| `common\script_constants\016_brilliant_scientist_foreign_constants.txt` | `9FA0E9CA054C4B9C2911A9E9F9910298C652347EE34F6E742809D197E71B8B72` |
| `common\on_actions\016_brilliant_scientist_project_on_actions.txt` | `D56934AC7016E8229A135B63B6240A2ECC70A37BCCE3DC3AEB836B60D08125D8` |
| `common\scripted_effects\016_brilliant_scientist_effects.txt` | `7C4C07AF4AB81180186191A320FDD1EBB5874CCB7620CC9CDA5B17F6918E0A48` |
| `docs\specs\016_brilliant_scientist_specs\specs\016_final_completion_contract.md` | `74A2E1016DEDCA54BA0C359716B6917A7BBBD60A44CA1E04A40317DE31695839` |

No gameplay patch or commit was made by this subagent. Parent integration should preserve the unenterable-country coverage boundary above, keep the true-count reconciliation and maximum-two start gate unchanged, and should not claim complete foreign orphan coverage until the unresolved engine/coverage question has an accepted bounded resolution.
