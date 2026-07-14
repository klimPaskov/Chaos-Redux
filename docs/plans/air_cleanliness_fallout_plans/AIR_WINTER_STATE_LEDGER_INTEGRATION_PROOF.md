# Air Winter State Ledger Integration Proof

## Integration result

The reviewed `air_winter_presentation_states` typed arrays are consumed by
`air_winter_refresh_presentation_class_from_ledger` in
`common/scripted_effects/air_cleanliness_winter_effects.txt`.

The exact runtime call site is the first operation in
`air_winter_update_state`. The existing Air Cleanliness host invokes that
effect at `common/scripted_effects/chaos_meter_effects.txt:5204`, inside the
single unfiltered `every_state` block that begins at line 5085. Presentation
classification therefore executes for every state reached by the host pass
before `air_winter_state_is_valid` excludes impassable, ownerless, or explicitly
excluded states from gameplay processing. No second state loop and no on-action
entry point were added.

Before this patch, the reviewed ledger and the numeric set/refresh helpers were
present but `air_winter_update_state` never read the typed arrays, so an
unseeded state remained unclassified. After this patch, the existing per-state
call migrates the state from the authoritative ledger before the gameplay gate.
The change is bounded to presentation variables and flags; it does not alter
which states receive Air Winter gameplay damage.

## Engine syntax proof

The installed vanilla build is Hearts of Iron IV 1.19.2.0.

- `common/script_constants/state_groups.txt` defines typed state collections as
  `schema = { any_key = yes array = state }`. The reviewed ledger uses the same
  schema.
- `documentation/triggers_documentation.md`, under `any_state_of`, says that
  the trigger checks the supplied states and that its `target` supports script
  constants. Its explicit-list example and script-constant example establish
  that the constant replaces the typed state list accepted by `target`.
- Live vanilla consumers use the loaded-constant form
  `constant:<category>.<entry>`, for example
  `target = constant:country_groups.nordics` in
  `common/scripted_triggers/NORDIC_scripted_triggers.txt` and
  `target = constant:country_groups.literally_china` in
  `common/decisions/CHI_decisions.txt`. Vanilla collection consumers use the
  same dotted lookup for state arrays, for example
  `input = constant:state_groups.balkans` in
  `common/collections/collections.txt`.
- `documentation/triggers_documentation.md`, under `state`, documents the state
  identity trigger and lists `PREV` as a supported target. The membership test
  is therefore:

  ```text
  any_state_of = {
      target = constant:air_winter_presentation_states.boreal_continental
      state = PREV
  }
  ```

  `any_state_of` scopes into each state supplied by the typed constant. `PREV`
  is the calling state, so `state = PREV` succeeds only when that calling state
  is a member. `ROOT` is deliberately not used: at the live call site the root
  scope is the host country outside the `every_state` iterator.
- `documentation/effects_documentation.md`, under `every_state`, defines the
  scope as executing on every state that fulfils its optional `limit`. The live
  host block has no `limit`, so it does not implicitly remove impassable states.
  The separate `impassable = no` condition remains inside
  `air_winter_state_is_valid` and is evaluated only after presentation
  classification.

The offline wiki snapshot was consulted in parallel: Data structures (typed
arrays and variables), Triggers (`any_state_of` and state identity), Effects
(`every_state`), and Scopes (`PREV` and iterator scope transitions), together
with the repository-required core pages.

## Idempotence and schema contract

Each state stores `air_winter_presentation_ledger_version`. Membership is
re-evaluated only when that variable is missing, differs from
`constant:air_winter_presentation_ledger.schema_version`, or the stored class is
missing/out of the accepted enum range. A current valid version only runs the
existing validator, keeping the unclassified flag synchronized without
rescanning nine arrays every month.

All nine arrays are checked during migration. The helper counts matches and
accepts a class only when the count is exactly one. Zero matches or more than
one match writes class `unclassified` through
`air_winter_set_presentation_class`; that helper records the current schema
version and `air_winter_refresh_presentation_class` sets
`air_winter_presentation_unclassified`. No geographic, strategic-region,
terrain, ownership, or category fallback exists.

A ledger edit that changes membership must be accompanied by a schema-version
increment in `air_winter_presentation_ledger`; otherwise current states are
intentionally not remigrated.

## Changed identifiers and files

- `common/scripted_effects/air_cleanliness_winter_effects.txt`
  - Added `air_winter_refresh_presentation_class_from_ledger` (STATE scope).
  - Added its call before the gameplay-validity gate in
    `air_winter_update_state`.
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_STATE_LEDGER_INTEGRATION_PROOF.md`
  - Records the engine proof, call site, schema behavior, and validation basis.

The reviewed ledger and classification review were not modified. No scripted
trigger, map mode, asset, decision, localisation, event, on-action, or host-loop
file was changed by this integration.

## Task-specific validation

- The reviewed ledger still parses as nine arrays containing 1,081 unique IDs,
  exactly covering 1 through 1081, including all 21 impassable states.
- The consumer contains one membership query for each reviewed array and maps
  it to the correspondingly named numeric presentation constant.
- The live call remains inside the existing single `every_state` pass, and the
  presentation refresh precedes `air_winter_state_is_valid`.
- Missing and conflicting membership paths both resolve to class 0 and set the
  visible unclassified state flag.

## Remaining risk

The installed engine documentation proves the typed target and scope syntax,
but no runtime game session was launched for this narrow handoff. The parent
agent should retain this exact-cover check if the reviewed ledger or installed
state topology changes.
