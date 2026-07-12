# Air Cleanliness Mechanic

## What This Adds

The Air Cleanliness mechanic tracks global atmospheric contamination and feeds both gameplay pressure and chaos progression.

It introduces:

- an `Air Cleanliness` tab in the Chaos Meter popup,
- a `Condemnation` tab for country-level diplomatic blame tracking,
- persistent global contamination tracking (`global.air_contamination_bp`),
- monthly contamination accumulation/decay logic,
- threshold-driven escalation (25/50/75/100/1000),
- a 75%+ Air Cleanliness Treaty system with invitations and member decisions,
- a new world-end scenario trigger: `Fallout`.

## System Flow

### 1) Monthly contamination update

On monthly host tick (`on_monthly`), `air_contamination_monthly_update` runs and computes contamination delta in basis points (`bp`, where `100 bp = 1%`):

- Chemical contaminated state (`chem_state_contamination`): `+1 bp` each (`+0.01%`).
- Irradiated fallout state (`nuclear_fallout_state`): `+3 bp` per current fallout intensity (`+0.03%` per intensity, up to `+0.21%` at the current intensity cap).
- Natural recovery (when not irreversible): `-35 bp` monthly (`-0.35%`).

Biological outbreak states do not add air contamination. They remain part of the biological warfare and deaths systems, but they are excluded from Air Cleanliness growth.

The computed delta is applied through `air_contamination_apply_delta_bp`.

### 2) Nuke fallout seeding

`chaos_meter_on_nuke_drop` no longer adds a direct global contamination spike.

Instead, a strike applies or strengthens `nuclear_fallout_state` on the target state:

- normal nuke: `+1.0` fallout intensity for `180` days,
- thermonuclear nuke: `+3.5` fallout intensity for `540` days,
- repeated strikes stack intensity up to the current cap of `7.0`.

That fallout intensity then contributes contamination monthly through the state loop, the same way chemical states do.

The same hook also adds direct chaos through the shared nuclear-use ladder documented in `docs/systems/nuclear_chaos_ladder.md`.

### 3) Chaos synchronization

Contamination delta is converted into chaos via `air_contamination_sync_chaos_from_delta`:

- every `+100 bp` (`+1%`) contamination => `+1` chaos,
- every `-100 bp` (`-1%`) contamination => `-1` chaos.

A buffer variable (`global.air_contamination_chaos_buffer_bp`) preserves sub-1% remainder between updates.

### 4) 75% Air Cleanliness Treaty

At `75%` contamination (`constant:air_contamination_threshold_bp.winter_75`), the system activates a global treaty layer:

- A major democratic country that has not used unconventional weapons forms the treaty and sends invitation events to countries globally.
- Countries decide whether to join through `chaosx_contamination.9` (AI weighted toward democracies and minor countries without unconventional stockpiles).
- Treaty members gain mutual respect opinion (`air_cleanliness_treaty_member_respect`).
- Treaty members claim a broad native embargo against all non-members when By Blood Alone is active.
- If a treaty member uses an unconventional weapon through a chemical, biological, or nuclear hook, it is expelled, marked banned, claimed for broad embargo by all other countries, and receives a violation opinion penalty (`air_cleanliness_treaty_violator`).
- Treaty activation and violations fire news events (`chaosx_contamination.7` and `.8`).
- Members also get treaty decisions:
  - `air_cleanliness_global_cleaning_day`
  - `air_cleanliness_joint_decontamination_program`
- A treaty-specific global event (`chaosx_contamination.11`) reports coordinated cleanup waves.

## Threshold Behavior

- `25%` (`2500 bp`): outbreak spread MTTH is accelerated (anthrax/plague/smallpox spread events).
- `50%` (`5000 bp`): mild nuclear winter periods can start.
- `75%` (`7500 bp`): severe nuclear winter periods can start.
- `100%` (`10000 bp`): irreversible mode starts:
	- contamination cannot drop below 100%,
	- fallout modifiers are applied globally,
	- state categories degrade over time toward wasteland.
- Final Silence forces contamination to exactly `100%` and locks future contamination changes at that value for the terminal branch.
- `1000%` (`100000 bp`): triggers world-end scenario event `chaosx_contamination.12` (`Fallout`).

One-time global threshold news events are fired from `events/chemical_warfare_events.txt` (`chaosx_contamination.1` to `.6`) for:

- 25%, 50%, 75%, 100% milestones,
- mild/severe winter period starts.

Treaty event IDs in the same file:

- `chaosx_contamination.7` Treaty activation news
- `chaosx_contamination.8` Treaty violation news
- `chaosx_contamination.9` Country invitation/join event
- `chaosx_contamination.10` Founder confirmation
- `chaosx_contamination.11` Global Cleaning Day news

Treaty embargo ownership is tracked separately from condemnation sanctions and the Great Embargo event. Removing one source releases the native relation only when no other owner remains and the relation was created by these systems. Without By Blood Alone, treaty state and opinion consequences still apply but no native embargo relation can be created.

## UI Integration

The Chaos Meter popup has five tabs:

1. `Status`
2. `History`
3. `Air Cleanliness`
4. `Condemnation`
5. `Deaths`

The contamination tab displays:

- contamination %, cleanliness %, monthly net delta,
- natural recovery amount,
- chemical/irradiated state counts and contribution,
- one consolidated contamination stage status line,
- winter state,
- one plain-language summary sentence explaining that each 1% contamination adds environmental attrition pressure across all states, regardless of owner type,
- progress to the fallout world-end threshold,
- right-side quick overview text with tooltip help.

The right-side monthly-model and threshold reference values are refreshed whenever the Chaos Meter popup is opened and whenever the `Air Cleanliness` tab is selected, so the UI does not depend on stale cached globals after loading a save.

The condemnation tab displays:

- the player's public condemnation,
- global total condemnation and active country count,
- sortable country rows with total, tier, recent gain, main source, sanction count, highest active sanction tier, and compliance state,
- a selected-country detail view with public-source breakdown, current and peak tier, participant counts, estimated trade dependency, practical penalties, decay, and compliance state.

Hidden evidence is excluded from the list and detail snapshot until it is disclosed. Exact bilateral trade is unavailable to script, so the displayed trade value is an aggregate complementarity estimate. See `docs/systems/condemnation_sanctions.md` for the complete UI read model and embargo ownership rules.

## World-End Integration

A triggered terminal event owns the live Fallout transition:

- `events/chemical_warfare_events.txt` -> `country_event = { id = chaosx_contamination.12 }`

It sets:

- `world_end`,
- `world_end_fallout`,
- `super_event_visible = 4` (30 days).

The public event catalog continues to associate Fallout with Event 2's world-end namespace. Event Details therefore shows Fallout as its own Event 2 row beside Zombie Apocalypse. Its checkbox gates the Fallout terminal event independently from Event 2 and the zombie ending.

The central `air_contamination_apply_delta_bp` effect calls `air_contamination_try_fire_fallout_world_end` after each contamination change. The dispatcher preserves the existing contamination threshold, master world-end guards, Fallout scenario toggle, and super-event path. Re-enabling Fallout while contamination already meets the threshold runs the same dispatcher immediately.

## Icons and GFX Wiring

### New sprite registration

- Add sprite definition in: `interface/chaosx_super_events.gfx`
- Sprite name used in code: `GFX_super_event_fallout`
- Expected texture path: `gfx/super_events/002_zombie_outbreak/super_event_fallout.dds`

### Existing sprite reused

- `GFX_modifiers_radiation` (already defined in `interface/countrystateview.gfx`) is used for the global contamination state modifier icon.
- Condemnation list and detail view use `GFX_flag_small2` and `GFX_diplo_countrylist_flag_frame` for country flags, plus `GFX_mini_tooltip` for the detail-view diplomacy button.
- Treaty news event uses existing report image:
  - `GFX_report_event_generic_sign_treaty2` (no new sprite required).

## Future Plans

1. Add more contamination sources (reactor accidents, industrial disasters, strategic bombardment side effects).
2. Add regional climate bands so winter effects scale by latitude/biome instead of global random spread only.
3. Add mitigation systems (global treaties, decontamination projects, adaptation tech) before irreversible collapse.
4. Add dedicated fallout art package (`super_event_fallout`, air-tab iconography, threshold warning overlays).
