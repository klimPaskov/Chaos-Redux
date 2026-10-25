# Achievement implementation prompt

Implement the three exact Event 123 achievements in Part 6 through `common/achievements/chaos_redux_achievements.txt` and the existing shared achievement framework.
Read the current event, equipment, unit, asset, and achievement owner guidance relevant to these callbacks.
Use the canonical IDs below after the identity check against the shared identifier registry.
The labels remain working directions, and the localisation owner writes final natural wording.

| ID | Visibility | Design difficulty | Core accomplishment |
| --- | --- | --- | --- |
| `123_equipment_choice_rearmed_under_fire` | Visible | Hard | Natural wartime shortage shipment, measurable fielded growth from its actual delivery baseline, and a relevant victorious army within 90 days |
| `123_equipment_choice_two_services_one_delivery` | Visible | Hard | Two land-combat groups from one natural combined immediate offer, both fielded thresholds, own handling expiry, and a qualifying mixed-army victory within 120 days |
| `123_equipment_choice_borrowed_impossibilities` | Visible | Very Hard | Two different natural unusual shipments, two complete template-equivalent material requirements in the victorious army within 365 days, and no corresponding owner production permission |

Part 6 is the source of truth for all thresholds, timing, route eligibility, and disqualifiers.
Preserve the original shortage at offer creation for the first route, and capture fielded growth baselines immediately before the first successful physical primary-row delivery.
A zero-delivery attempt cannot establish a baseline.
Freeze the actual primary equipment need of an existing compatible battalion as the minimum meaningful growth unit.
Open a challenge only after its required complete delivery succeeds.

Use one active record per achievement and country.
Later shipments cannot overwrite an ongoing attempt.
Preserve exact firing, recipient generation, origin, selected primary family, physical amounts, fielded baseline, original deficit where relevant, expiry, and owner-production state.
Separate ordinary policy or cosmetic tag changes from a new country identity.
Natural automatic selection may qualify, while manual, forced, test-country, or origin-laundered deliveries cannot.
A player leaving the tracked country or passing it to AI invalidates an active attempt.

All three routes require a verified victorious-army or commander-army callback with the exact compatible equipment evidence described by the route.
Confirm that the actual supported native query can establish the required quantities and scope.
A missing query is a concrete implementation blocker.
Do not substitute a country-wide stockpile decline, any battle victory, template existence, a production flag, or a report acknowledgement.
Equipment is fungible, so the achievement wording must avoid a false claim of serial-level attribution to gifted items.

For the two-family unusual route, verify separate compatible formations or aggregate the requirement vector and sum duplicate ordinary equipment rows.
Robots and paleogenetic creatures together require 120 support equipment in addition to both unusual rows.
Two tests that each reuse the same 60 support units are invalid.
Keep both owner production permissions absent at the qualifying victory and preserve their exact existing owner gates.

Update only through actual delivery, relevant battle, handling-expiry, country-lifecycle, player-control, and bounded country-owned expiry hooks.
Avoid a new recurring world scan.
Keep completion idempotent and record useful disqualification reasons for developer inspection.

Produce the three original achievement subjects and complete aligned 64 by 64 completed, grey, and not-eligible triplets through the asset prompt and mandatory achievement processor.
Use full registry IDs as root achievement filenames.
The localisation auditor checks that every description states the real condition and that no broader or easier claim appears in the catalog or tooltip.

Acceptance evidence must cover correct and wrong-army victories, before-threshold victories, transfer and stock-decline false positives, zero and partial grants, pre-delivery production growth, duplicated callbacks, two shipments from the same firing, shared complementary rows, owner production unlocked before victory, country identity change, player-control loss, and expiry.
Use actual source and supported callbacks.
Report native execution or save evidence only when it was actually obtained, and separate remaining live validation from completed implementation work.
