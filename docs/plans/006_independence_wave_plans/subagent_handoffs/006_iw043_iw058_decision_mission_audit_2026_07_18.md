# IW-043 / IW-058 decision and mission audit — 18 July 2026

## Scope and outcome

Audited the two Event 006 decision categories, all 32 decisions, their six
formation-bound timed operations, the 20 owned incidents, the owned package
helpers, and their dedicated English localisation. This review did not alter
focuses, country definitions, global AI, GFX, portraits, advisors, or assets.

Two local decision/UI corrections were applied. One high-severity provenance
gap remains: the six force-bound operations cannot prove that the selected
division came from the current generation's supplied force package.

## Changed files

- `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`
  - `independence_wave_iw058_open_diaspora_expert_mission`: added the same
    civilian-factory availability predicate to `custom_cost_trigger` that its
    `available` block and active mission modifier already use.
  - `independence_wave_iw058_fortify_mountain_river_corridor`: did the same
    for its two-factory requirement.
  - Before: a decision could be unavailable for lack of civilian factories
    while its custom cost remained displayed as affordable. After: the cost
    is blocked consistently with the actual availability rule.
- `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
  - Added `_blocked` and `_tooltip` variants for all 26
    `independence_wave_iw043_cost_*` and `independence_wave_iw058_cost_*`
    custom-cost keys.
  - Before: the engine's implicit failed-cost and hover keys were absent.
    After: unavailable costs render red and hovering explains the concrete
    command-power, manpower, equipment, train, convoy, and/or factory need.

## Issues, highest severity first

### High — unresolved: force provenance is country-scoped, not division-scoped

Affected operations:

- `independence_wave_iw043_secure_kazan_cheboksary_navigation`
- `independence_wave_iw043_discipline_the_river_guard`
- `independence_wave_iw058_secure_mosul_council_quarter`
- `independence_wave_iw058_discipline_levies_under_civilian_law`
- `independence_wave_iw058_patrol_nineveh_approaches`
- `independence_wave_iw058_fortify_mountain_river_corridor`

`independence_wave_apply_dynamic_starting_force` in
`common/scripted_effects/006_independence_wave_force_effects.txt` creates the
opening divisions, then writes only the country variable
`independence_wave_force_package_generation_id`. The IW-043/IW-058 receipt
effects add only country flags. Their bind effects subsequently choose a
random owned division that matches a generic composition and save it as a
global target. Neither `random_country_division` limit nor the matching
validation trigger requires a division variable/flag proving supplied-package
origin or generation.

Consequently, an unrelated player-built division with the matching template
composition can satisfy the six operations. The bound target itself is stable
through a timer, but it is not an exact current-generation supplied division.

Do not patch this by treating the existing country receipt as a unit identity.
That would preserve the false proof. Parent/force-system follow-up must:

1. Add a safe allocator-level mechanism that writes a package and generation
   receipt to each relevant supplied division at creation time.
2. Require that division-scoped receipt in both `has_independence_wave_iw043_*`
   and `has_independence_wave_iw058_*` supplied-candidate and live-binding
   predicates.
3. Keep the global event target only as the operation's stable pointer; retain
   its current validation, release, and generation checks.
4. Test that a matching player-trained division cannot start a formation
   operation, while a current-generation supplied one can.

This crosses the shared force allocator and is intentionally not patched in
the narrow decision surface.

### Fixed — custom-cost feedback did not describe factory unavailability

The two corrected decisions each reserve civilian factories through a decision
modifier and already checked factory availability in `available`, but omitted
that predicate from `custom_cost_trigger`. The custom cost now turns blocked
when factory capacity is missing.

### Fixed — all 26 custom costs lacked engine-generated localisation variants

The base custom-cost keys were present, but every implicit `_blocked` and
`_tooltip` variant was absent. This was a player-facing localisation gap for
all 32 decisions. The new variants mirror the concrete cost values and use
the standard red/yellow decision-cost presentation.

### Intentional route lock — FORM-12, FORM-13, and FORM-18 remain fail-closed

`can_independence_wave_form12_iw043_commit`,
`can_independence_wave_form13_iw043_commit`, and
`can_independence_wave_form18_iw058_commit` depend on their readiness
contracts, each of which requires its `*_adapter_attested` flag. No writer
for these three attestation flags is present in the audited Event 006 source.
The three decisions and incident options recheck the same gate. This is safe
and matches the required fail-closed behavior; no formable was promoted.

## Category lifecycle

Both categories are visible only to their exact package identity:

- `independence_wave_iw043_middle_volga_congress_category` is gated by
  `is_independence_wave_iw043_country` (original tag `CHU`, exact package ID
  IW-043).
- `independence_wave_iw058_council_of_communities_category` is gated by
  `is_independence_wave_iw058_country` (original tag `ASY`, exact package ID
  IW-058).

Decision visibility adds focus/route/receipt gates. Twenty-four timed actions
have a complete/remove/cancel lifecycle; eight clause/guarantee choices pay,
open their incident immediately, and resolve through its options. Package
cleanup removes every owned decision, releases bound force targets, clears
paid-transaction state, and clears package-owned receipts before identity
teardown. No passive political-power store was found.

## Formation-operation quality notes

| Operation | Owner/category/region | Requirement and duration | Success / failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| `secure_kazan_cheboksary_navigation` | CHU, Middle Volga Congress, states 249 and 256/transit | River-guard receipt, force binding, control; 120 days | River control and authority / navigation crisis, Event 4306 | Receipt plus release prevent repetition; provenance gap remains. |
| `discipline_the_river_guard` | CHU, Middle Volga Congress, River Guard and Kazan | Force binding and security resources; 150 days | Civilian River Guard conversion / security crisis, Event 4307 | Permanent receipt and binding release; provenance gap remains. |
| `secure_mosul_council_quarter` | ASY, Council of Communities, Mosul state 676 | Civic-guard receipt, force binding, owned and controlled anchor; 120 days | Anchor defense / anchor and severe-security crisis, Event 5806 | Permanent receipt and binding release; provenance gap remains. |
| `discipline_levies_under_civilian_law` | ASY, Council of Communities, Levies/Mosul | Levies receipt, force binding, state 676 control; 150 days | Civilian Levies board / severe crisis, Event 5809 | Permanent receipt and binding release; provenance gap remains. |
| `patrol_nineveh_approaches` | ASY, Council of Communities, Mosul/Nineveh anchor | Civic-guard receipt, force binding, state 676 control; 120 days | Security and cohesion / patrol escalation, Event 5806 | Permanent receipt and binding release; provenance gap remains. |
| `fortify_mountain_river_corridor` | ASY, Council of Communities, Mosul state 676 | Civic guard, force binding, owned and controlled anchor, resources, two civilian factories; 180 days | One bounded bunker and infrastructure step in 676 / construction burden, Event 5806 | Permanent receipt and binding release; provenance gap remains. |

All six pay first through the package transaction helpers, validate the saved
division on completion, release the global target on completion or cancel,
and do not create units or refund paid equipment/manpower. The exact-division
origin finding above is the remaining quality blocker.

## Cost, target, AI, event, and exploit review

- All 32 decisions have AI weights. All 24 timed decisions have complete,
  remove, cancel trigger, cancel effect, and a concrete custom cost. The eight
  immediate clause/community-guarantee choices begin a paid transaction and
  their incident options commit or roll it back without refunding it.
- The two factory corrections bring custom-cost state in line with active
  mission factory requirements. No decision is a flat political-power trade.
- The three target lists each contain 150 unique, defined tags. The CHU
  carrier is excluded from the IW-043 trade action; ASY is excluded from both
  IW-058 target actions. Their target triggers reject self, war targets, and
  subjects, then require a valid major/treaty/league/patron/diaspora reach.
- The 20 events (`4301`–`4310`, `5801`–`5810`) are all
  `is_triggered_only = yes`; their 59 options all have AI chances. Event 5805
  consumes the saved diaspora partner only while it exists and is at peace;
  Event 5807 applies a guarantee only to the saved valid target. No owned
  event uses `make_subject`, `puppet`, or annexation effects.
- No `create_unit` or `load_oob` appears in the owned decision or event file.
  The formation operations only change an already-bound division. Their
  transaction rollback clears ledgers rather than restoring resources, so the
  audited surface does not create an equipment, manpower, or unit-refund loop.
- All direct decision/event localisation references resolve in the three
  dedicated English files. No decision-owned scripted GUI surface is present,
  so GUI inspection/rendering was not applicable.

## Validation evidence

- Core decision audit: 32 decisions total; 24 timed, 8 immediate; all timed
  decisions had complete/remove/cancel blocks; all 32 had AI weights; six
  formation operations had bind, validation, and release calls.
- Target audit: each pool had 150 unique defined tags, and its own carrier was
  excluded.
- Event audit: 20 triggered-only incidents and 59 options, all with AI chance.
- Localisation audit: 26 custom-cost keys now each have base, `_blocked`, and
  `_tooltip` keys; 276 explicit decision/event localisation references resolve;
  the touched English file remains UTF-8 with BOM.
- HOI4 MCP event inspection was attempted with the owned event file. It
  returned `EVENT_HELPER_PROJECTION_LIMIT` at a 200,000-node cap and produced
  no artifact. Direct source inspection was therefore used for the event and
  helper evidence above.

## Skipped validation

No in-engine runtime session was run. The unresolved provenance issue depends
on allocator-level division identity, so static source evidence cannot prove
the desired live distinction. No GUI MCP check was run because no owned
decision GUI exists.

## Remaining work

Implement and test the allocator-level division receipt contract described in
the high-severity finding. FORM-12/13/18 must remain fail-closed until their
exact registry/adapter contract is authored and proven.
