# Camp live QA source commit boundary review

Read-only dependency review on 2026-10-04.
Reviewed HEAD was `c7fde02a7f6e26b87b5883bc2a46f6d7db1d06dd` at both start and end; this is evidence of the review base only, not permission to reuse that base after concurrent publication.
No source, real index or Git ref was changed by this review.

## Recommended isolated source boundary

The full origin module can be published as an inactive, complete API with its exact owner-consumer closure; the older broad caller integration is not required for name or constant resolution.
This recommendation preserves the existing approved observer design and does not propose substitutes or stub helpers.

| Path | Include only |
|---|---|
| `common/scripted_effects/camp_administration_origin_effects.txt` | Complete current observer module, including supported zero resets for its request contract tokens |
| `common/scripted_triggers/camp_administration_origin_triggers.txt` | Complete current companion scanner/readiness module |
| `common/script_constants/camp_administration_origin_constants.txt` | `camp_origin_value.maximum_row_scan = 1000`; `camp_origin_family.occupation = 1`, `.custody = 2` |
| `common/scripted_effects/camp_administration_effects.txt` | New complete `camp_admin_consume_rows` and `camp_admin_consume_outside_rows` definitions; file-scoped `@CAMP_ADMIN_ROW_RELEASE = 2` and `@CAMP_ADMIN_ROW_OUTSIDE = 3`; exact existing `camp_admin_refresh_country_economy` removal guard hunk |
| `common/scripted_effects/camp_administration_occupation_effects.txt` | New complete `camp_occ_distribute_known_origin_removal` definition |
| `common/script_constants/camp_administration_occupation_constants.txt` | Only `camp_occ_value.row_first_id = 1` and `camp_occ_row_status` with integer schema, `active = 1`, `released = 2` |
| `common/scripted_effects/camp_administration_origin_effects.md` | API and registry contracts with accurate isolated-publication status; document the three owner-consumer contracts; scope integration statements to working-tree evidence |
| Paired existing owner Markdown files | Narrow documentation of the newly published consumer definitions and their inactive integration status, if contracts are kept in these paired files |

`@CAMP_ADMIN_ROW_VOID` is not consumed by this closure and need not be included.
`common/script_constants/camp_administration_constants.txt` needs no change for this closure: HEAD already defines `zero`, `one`, `negative_one`, `people_per_k`, `minimum_population_k`, and `maximum_receipt_k`.
HEAD occupation constants already define the required `camp_occ_value.minimum_population_k`.
No dispatch, country, UI, history, arrival, regional-ceiling, transfer-validity, throughput or demographic-anchor constants are needed.

## Dependency and row evidence

`camp_origin_reconcile_host_membership` calls the two family consumers.
The custody consumer calls `camp_admin_consume_rows` and the origin acknowledgment API.
The occupation consumer calls only the origin acknowledgment API.
All remaining scripted calls in the selected module and triggers resolve inside this closure; dynamic variable scope tokens are scope pointers rather than missing scripted helpers.

Both family consumers require a pending single-row reconciliation of the matching family, no ambiguity, and a successful fresh `camp_origin_host_rows_valid` scan before mutation.
That scan rejects missing initialized registries, missing or invalid authority objects, malformed aligned arrays, inconsistent counts/next IDs, illegal statuses, negative membership, nonzero inactive membership, invalid origins, mismatched host totals and arrays exceeding 1,000 rows.
The custody low-level consumer is an internal primitive, not a general validated public entry point; in the selected closure its only outside caller is the validated custody wrapper.
An absent custody row count leaves its reverse loop inert.
Do not add a new direct caller to that primitive as part of the QA commit.
Both wrapper consumers commit only the selected exact row, preserve death/release history and invoke receipt acknowledgment.

## Older work excluded

Keep broad initialization, capacity, admission, mortality, movement, release, reform, country, lifecycle, GUI and native caller hunks out of the isolated index.
The supported reset in the working close-site terminal contract and UI projection belongs to older bodies absent from HEAD; publishing those entire bodies would pull in the old integration graph.
Those reset repairs can remain in the working tree for their owning integration tranche.
This isolated commit must not claim that it publishes those two older body repairs or all live caller integration.
The new API definitions have no existing HEAD entry caller and therefore do not activate a new gameplay route.

The current origin Markdown states that custody/occupation owner integration is implemented and lists active callers; copying it unqualified into the isolated tree would overstate that tree's implementation.
Retain that working-tree evidence with an explicit publication boundary and distinguish queued caller wiring from the API definitions actually included.

## Validation limits and next action

This review examined extracted production helper bodies and their complete constant tokens against HEAD definitions.
It is a source dependency boundary review, not MCP or engine validation, and does not claim integrated runtime acceptance.
No gameplay/event/GUI/weighted surfaces were redesigned and no MCP fanout was performed under the parent instruction.
The parent must review the isolated staged tree's actual helper definitions and exact constant resolution, then use the shared Git commit skill's current-HEAD compare-and-swap publication and index reconciliation.
The real index had no staged paths when inspected during this review, but its state and HEAD must be captured again immediately before publication.
There were no fallback helpers or source simplifications introduced.