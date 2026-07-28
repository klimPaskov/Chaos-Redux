# Migration and Compatibility Plan

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Scope

This system changes persistent global variables, state variables, terminal event ownership, scenario ids, focus trees, country identities, and world-state relationships. Migration must be explicit. A save should never enter a black screen because an old variable happened to match a new phase value.

## Version markers

Add version variables for each independently migratable surface:

- `air_winter_system_version`
- `fallout_world_end_system_version`
- `triggerable_scenario_registry_version`
- `fallout_country_package_version`
- `fallout_focus_package_version`

Initialization helpers compare missing or older versions and perform only the migrations needed for that surface.

## Air Contamination migration

Existing values to preserve:

- global contamination basis points
- monthly delta
- contamination Chaos buffer
- chemical and irradiated state counts
- nuclear fallout state intensity
- current irreversibility
- achievement state

Existing global winter flags should be converted into state seed pressure:

- mild winter flag seeds Phase 1 or 2 target pressure based on local contamination and climate
- severe winter flag seeds Phase 3 or 4 target pressure
- old temporary atomic or thermonuclear state modifiers remain until expiry but do not become the new phase source of truth

After conversion:

- clear old winter-only random pulse flags
- initialize state phase, exposure, and recovery values
- set the new Air Winter version

Do not lower existing contamination or remove live nuclear fallout during migration.

## Treaty migration

The live monthly update owns a bounded treaty lifecycle. Schema reconstruction restores valid members, existing violators, and their permanent diplomatic edges. It cancels active project receipts and clears route ledgers without a country-world scan.

Migration steps:

1. clear stale founder targets that point to invalid countries
2. preserve valid treaty members only when the treaty had genuinely formed in the save
3. restore opinion and embargo ownership through idempotent membership and violator edges
4. rebuild the treaty member and violator caches
5. cancel stale active projects and clear relief-state caches through their exact receipts
6. initialize the treaty generation and Cleaning Day transaction values
7. set a treaty system version

A save with no real treaty formation should not suddenly gain a random founder merely because stale member flags exist.

## Fallout event migration

Create `events/fallout_world_end_events.txt` and register `add_namespace = chaosx.fallout`.

Migration work:

- locate every existing Fallout event definition
- delete each Fallout event block outside the dedicated file
- locate every caller of those old event identifiers
- replace callers with `fallout_request_aftermath` or a dedicated `chaosx.fallout.*` entry event
- remove Fallout super-event image, text, quote, reaction, and audio wiring
- remove Fallout texture and sprite paths inside another feature package
- update docs and catalogs to name the dedicated event file and namespace

Compatibility policy:

- do not keep an event shim in another namespace
- do not fire an old event id from save migration
- use a versioned `fallout_world_end_migrate_save` scripted effect for any required flag or variable conversion
- the migration effect may recognize generic Fallout state such as `world_end_fallout`
- the migration effect must not depend on another feature's flags, tags, assets, or event chain

Possible recovery cases:

- `world_end_fallout` exists and the new transition has not started
- the old Fallout presentation flag remains active
- the old Fallout audio variable remains set
- the world is terminal but no player continuation state exists

For each case, the dedicated migration effect either clears stale presentation state and starts a Fallout-owned recovery event, or records a blocking error for parent review. It never calls an event outside `chaosx.fallout`.

## Scenario registry extension

Fallout reserves a new internal manual-trigger id from the live maximum without appending a public registry row. Do not renumber existing scenarios.

Allocation procedure:

1. Read every assignment in `triggerable_scenario_id`.
2. Confirm that each assigned integer is unique.
3. Find the highest assigned integer in the live checkout.
4. Set the Fallout scenario id to that value plus one.
5. Add the same allocated id to registry arrays, sorting branches, scripted localisation, GUI dispatch, launch events, documentation, and catalog records.
6. Record the allocated value in the implementation handoff.

Compatibility behavior:

- Existing stored scenario selections keep their current meaning.
- No existing raw id is remapped.
- No save migration is needed solely to reserve the Fallout-owned manual-trigger value because Fallout is not added to the public registry.
- A registry version may still be bumped when the existing framework uses one, but the version update must not rewrite old ids.

The inspected repository snapshot ended at id 8. That observation cannot be used as the final assigned value because later work may add more scenarios before implementation.

## Mapmode migration

Mapmode ids are script names, not stored numeric scenario ids. Preserve existing names:

- `deaths_state_map_mode`
- `contaminated_states_map_mode`

Add:

- `air_winter_state_map_mode`

The texture strip migration must keep old frame ordering. Append the verified winter icon and leave existing frames in place.

## Focus migration

A country entering Fallout receives a new focus tree through runtime assignment.

Before loading the Fallout tree, capture selected old-world focus memory that post-Fallout content needs:

- government route
- military doctrine direction
- industrial preparation
- civil defense and nuclear preparation
- relevant event routes
- prior successor identity

Do not attempt to preserve every old completed focus as a completed Fallout focus. Convert relevant history into country-memory flags and starting values.

For a country that already uses a Chaos Redux event tree:

- record its event origin
- record completed route milestones
- map those milestones into the country memory overlay
- load the Fallout tree

Use `keep_completed = yes` only when shared focus ids are intentionally common between the old and new tree. Unrelated completed ids must not leak.

## Country and tag compatibility

Before state transfer:

- identify every active dynamic country
- identify event-managed countries
- identify nonhuman and special Chaos countries
- identify collaboration governments and civil-war tags

Rules:

- surviving event-created countries can receive Fallout packages when the matrix supports them
- incompatible event actors are retired through their own cleanup helpers before state reassignment
- base tags are not reused while active
- dynamic tags are not assumed available
- cosmetic tags change appearance but do not erase event-origin memory

## Diplomacy compatibility

The transition must account for DLC-specific and engine-specific relationships.

Validate local effects for:

- faction removal
- war termination
- subject release
- government in exile cleanup
- collaboration government cleanup
- expeditionary and volunteer return
- lend lease cancellation
- guarantee and access removal
- intelligence network behavior

The cleanup order must not leave a country in a war after losing every valid state.

## DLC compatibility

The system should operate without assuming every expansion is enabled.

Potential DLC-sensitive surfaces:

- collaboration governments
- government in exile
- special projects and thermonuclear technology
- intelligence agencies
- balance of power
- market contracts
- specific focus or character systems

Use DLC checks only where an effect or content surface truly requires them. The core winter, blackout, rewrite, and successor campaign cannot depend on optional DLC.

## Multiplayer compatibility

Persist host-owned transition state globally.

Each human player needs:

- captured pre-transition tag
- reserved candidate state group
- selected or automatic successor
- valid tag switch or continuation

Resolve candidate overlap deterministically by:

1. existing ownership and capital relation
2. protected population share
3. player reservation priority
4. stable player index or another verified deterministic tie-breaker

Do not use random selection for contested human candidates.

## Save-load test points

Required save points:

- before contamination reaches 100 percent
- after eligibility but before request
- during a severe winter phase
- after manual strike but before day seven
- on day seven before request event execution
- each blackout beat
- during state processing
- during country processing
- during player successor selection
- immediately after reveal
- one month after reveal

Every load must resume without duplicate population loss, duplicate country creation, duplicate focus loading, or a permanent black screen.

## Documentation compatibility

Update or supersede:

- old event id claims
- normal Fallout super-event claims
- chaos-above-1000-only claims
- old fixed recovery values
- old random winter behavior
- old scenario id assignments

Keep one migration note under the plans folder. Player-facing docs should describe current behavior, not migration history.
