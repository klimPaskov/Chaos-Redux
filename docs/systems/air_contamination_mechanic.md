# Air Cleanliness Mechanic

## What This Adds

The Air Cleanliness mechanic tracks global atmospheric contamination and feeds both gameplay pressure and chaos progression.

It introduces:

- an `Air Cleanliness` tab in the Chaos Meter popup,
- a `Condemnation` tab for country-level diplomatic blame tracking,
- persistent global contamination tracking (`global.air_contamination_bp`),
- monthly contamination accumulation/decay logic,
- threshold-driven escalation at 25%, 50%, 75%, and 100%,
- a 75%+ Air Cleanliness Treaty system with invitations and member decisions,
- a contamination-driven request into the dedicated `Fallout` world-end system.

## System Flow

### 1) Monthly contamination update

On monthly host tick (`on_monthly`), `air_contamination_monthly_update` runs and computes contamination delta in basis points (`bp`, where `100 bp = 1%`):

- Chemical contaminated state (`chem_state_contamination`): `+1 bp` each (`+0.01%`).
- Irradiated fallout state (`nuclear_fallout_state`): `+3 bp` per current fallout intensity (`+0.03%` per intensity, up to `+0.21%` at the current intensity cap).
- Large wildfire smoke and volcanic ash: a decaying severity-scaled reservoir, limited to `+4 bp` monthly (`+0.04%`).
- Natural recovery while reversible: `-3 bp` below 25%, `-2 bp` from 25%, `-1 bp` from 50%, and `-0.5 bp` from 75%.

Biological outbreak states do not add air contamination. They remain part of the biological warfare and deaths systems, but they are excluded from Air Cleanliness growth.

Regional or stronger wildfires contribute. Volcanic eruptions, ashfall, and massive eruptions contribute at every resolved severity. Severe or stronger volcanic eruptions, regional or stronger ashfall, and severe or stronger massive eruptions also add one small settled-ash aftermath receipt when their recovery card opens. Each physical Event 013 impact is registered once by state, sequence, impact index, and family, while each aftermath sequence is registered once by its stored disaster id. The reservoir loses `0.25 bp` of monthly pressure after each host tick, which lets widespread ash linger without allowing the natural source to scale without limit. See `docs/systems/air_cleanliness/natural_sources.md`.

The computed delta is applied through `air_contamination_apply_delta_bp`.

#### Natural-source helper ownership

The natural-disaster contamination bridge is private to the Air Contamination and Event 013 integration and lives in `common/scripted_effects/fallout_consolidated_effects.txt`.

- `air_contamination_register_natural_disaster_source` runs in the resolved impact state, validates the Event 013 family and severity context, and adds one deduplicated contribution to the natural-source reservoir.
- `air_contamination_prepare_natural_source_monthly` copies the clamped reservoir into the monthly delta, applies one decay step, and records the monthly tick date so the source cannot decay twice in one host update.

The exact source-family and reservoir proof is documented in `docs/plans/air_cleanliness_fallout_plans/AIR_CONTAMINATION_NATURAL_SOURCE_PROOF.md`.

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

- The lowest-id eligible major democratic country in the bounded Air Winter registry becomes founder. No random founder or world-country scan is used.
- Generation-bound invitations use separate attempt and terminal receipts. Declines do not repeat in one treaty generation, while temporarily failed deliveries can retry on a later ninety-day bounded scan.
- Countries decide whether to join through `chaosx_contamination.9`. Acceptance calls the idempotent member-registration wrapper.
- Treaty members gain mutual respect opinion (`air_cleanliness_treaty_member_respect`) and shared basic Air Winter sampling.
- Member relations refresh only at membership, violation, and cleanup edges.
- If a treaty member uses an unconventional weapon through a chemical, biological, or nuclear hook, it is expelled, marked with permanent betrayal memory, and sanctioned only by current members.
- Native embargo ownership is stored separately for the treaty. Non-members are not embargoed merely for remaining outside the treaty.
- Treaty activation and violations fire news events (`chaosx_contamination.7` and `.8`).
- Members also get treaty decisions:
  - `air_cleanliness_global_cleaning_day`
  - `air_cleanliness_joint_filter_convoy`
- Global Cleaning Day is an equipment-funded atomic project with a global lock, sponsor receipt, transaction number, and six-month cooldown.
- Joint Filter Convoy is a real country-targeted decision. It spends support equipment and convoys, records the donor in a dedicated active-project registry, reserves the recipient's exact Phase 3 or worse priority state, changes existing Air Winter ledgers, and opens an `air_winter_relief_route` for up to six months while its conditions hold.
- A pre-winter treaty pulse removes invalid routes before monthly state pressure is calculated.
- Fallout preserves treaty membership and betrayal memory while silently cancelling active projects, invitations, and relief routes.
- A treaty-specific global event (`chaosx_contamination.11`) reports coordinated cleanup waves.

The full lifecycle, tuning, cleanup behavior, and remaining treaty omissions are documented in `docs/systems/air_cleanliness_treaty.md`.

## Threshold Behavior

- `25%` (`2500 bp`): outbreak spread MTTH is accelerated (anthrax/plague/smallpox spread events).
- `50%` (`5000 bp`): mild nuclear winter periods can start.
- `75%` (`7500 bp`): severe nuclear winter periods can start.
- `100%` (`10000 bp`): irreversible mode starts:
	- contamination cannot drop below 100%,
	- fallout modifiers are applied globally,
	- state categories degrade over time toward wasteland,
	- `fallout_evaluate_air_contamination_request` can submit the gradual-air-collapse request when Fallout is enabled and no other world end is active.
- Final Silence forces contamination to exactly `100%` and locks future contamination changes at that value for the terminal branch.

One-time global threshold news events are fired from `events/chemical_warfare_events.txt` (`chaosx_contamination.1` to `.6`) for:

- 25%, 50%, 75%, 100% milestones,
- mild/severe winter period starts.

Treaty event IDs in the same file:

- `chaosx_contamination.7` Treaty activation news
- `chaosx_contamination.8` Treaty violation news
- `chaosx_contamination.9` Country invitation/join event
- `chaosx_contamination.10` Founder confirmation
- `chaosx_contamination.11` Global Cleaning Day news

Treaty project and succession reports live in `events/air_cleanliness_treaty_events.txt` under `chaosx_air_treaty`:

- `.1` Filter Convoy dispatch
- `.2` Filter Convoy arrival
- `.3` Secretariat succession
- `.4` Filter Convoy route failure
- `.5` Cleaning charter cancellation

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
- wildfire-smoke and volcanic-ash contribution,
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

Fallout is owned by the dedicated `fallout_world_end` system. Air Contamination is one request source for that system and does not own the terminal transition. Air Winter and post-consequence survivor events live in `events/fallout_world_end_events.txt` under the `chaosx.fallout` namespace. The Fallout consequence itself has no public Event Details row, evolution entry, or ordinary event-log registration.

After each contamination change, `air_contamination_apply_delta_bp` calls `fallout_evaluate_air_contamination_request`. At or above `100%`, the evaluator submits a gradual-air-collapse request through `fallout_request_aftermath` when no other world end is active and Fallout is enabled. Re-enabling Fallout at or above the threshold runs the same evaluator immediately.

The Fallout request coordinator validates the request, records its source and intensity, and owns the transition that sets `world_end` and `world_end_fallout`. It can enter the `chaosx.fallout.*` transition chain and full-screen blackout GUI. Strict postconditions prevent map return while successor allocation, player continuation, country packages, focus packages, or old-world diplomacy cleanup remain incomplete. Fallout has no Event 2 ownership, evolution entry, public event-log row, or ordinary super-event slot. Its blackout may still play the dedicated Fallout sound path for presentation.

When a Fallout request enters the coordinator, `fallout_air_cleanliness_disabled` is a reversible transaction pause that closes the host-reconciliation gap. Rejected validation removes that pause and restores the ordinary modifier surface. A committed consequence replaces it with `fallout_air_contamination_permanent_99`, sets the total and Fallout-owned source to 9,900 basis points, zeros every later source and decay delta, and refreshes the ordinary modifier surface. Air Winter pauses only while `fallout_transition_active` protects the frozen rewrite snapshot, then resumes against the fixed atmosphere. Treaty operations remain closed because Fallout owns their diplomatic boundary. Save reconciliation reapplies the same idempotent lock.

The Fallout checkbox lives in the Miscellaneous settings panel. The stable Fallout id remains in the internal settings and request ledger with owner event `none` and linked super-event `none`. It is not inserted into the public Event Details registry or projected into Event 2 rows.

### Current transition boundary

The live transition schema is version 11. Completed schema-10 and older saves promote non-destructively and are marked as lacking current-schema receipts. Active schema-7 through schema-10 saves can rebuild only in the snapshot phase before snapshot application or destruction and without an unrelated error. A schema-10 phase 2 transition can promote before grading mutation. Schema-10 phases 3 through 6 require current grading and exact live-to-frozen supply-network equality before allocation. Later or ambiguous transitions fail closed under blackout. The former schema-3 map-return-error promotion is removed. No generic pre-destructive restart or altered-grade replay is active.

Player reservations are planned before the successor conflict ledger and before any successor allocation is permitted. The live commit path requires an already existing target with current-transition country and focus packages, survivable territory, and the exact reserved capital under its ownership and control. A two-pass global preflight validates every existing commit and proposed target before any switch. The durable assignment ledger is written before an optional `change_tag_from`, and retry recovery can rebuild reservations and revalidate assignment uniqueness.

An uncommitted player can therefore be committed only when the selected target is already materialized and carries both package generations for the current transition. Actual successor materialization, country and focus package producers, candidate-choice UI, and general successor allocation are absent. Static inspection also cannot prove that the destination observes `is_ai = no` immediately after `change_tag_from`. No Hearts of Iron IV run was authorized. The map-return gate must remain closed until the missing systems, tag-switch timing proof, and full diplomacy reset are resolved.

### Dormant manual Fallout scenario

The manual scenario is a separate caller into the same transition. Its dormant installed-build substrate expands 10,154 valid assigned land targets across 1,081 states into 41 batches. Batches 0 through 39 contain 250 targets and batch 40 contains 154. Event 20 now owns the public `SCN-012` row and dispatch in the shared triggerable-scenario UI. Its launch establishes the two-tag Black Plague bootstrap and remains separate from the Fallout-owned manual trigger. The live registry continues to preserve the existing Fallout reservations and other scenario ids.

Static control flow requires complete callback and state-count verification, applies aggregate Air and nuclear consequences once, and stores an exact seven-day countdown before requesting Fallout. Runtime behavior is not proven. In particular, `launch_nuke` with `use_nuke = no` callback occurrence and synchrony are unknown. If all calls emit `on_nuke_drop`, vanilla may schedule about 121,848 one-day nuclear news event attempts through its twelve repeated news-event branches. This is a release blocker.

## Icons and GFX Wiring

### Fallout-owned transition sprites

- Sprite definitions: `interface/fallout_world_end.gfx`
- Blackout sprite: `GFX_fallout_blackout_tile`
- Blackout texture: `gfx/interface/fallout_world_end/fallout_blackout_tile.dds`
- State-grade idea sprite: `GFX_idea_fallout_state_grade`
- State-grade idea texture: `gfx/interface/ideas/fallout_world_end/idea_fallout_state_grade.dds`
- Asset manifest: `docs/assets/fallout_world_end/manifest.md`

### Existing sprite reused

- `GFX_modifiers_radiation` (already defined in `interface/countrystateview.gfx`) is used for the global contamination state modifier icon.
- Condemnation list and detail view use `GFX_flag_small2` and `GFX_diplo_countrylist_flag_frame` for country flags, plus `GFX_mini_tooltip` for the detail-view diplomacy button.
- Treaty reports use existing `GFX_report_event_generic_sign_treaty1`, `GFX_report_event_generic_sign_treaty2`, `GFX_report_event_generic_factory`, and `GFX_news_event_chaosx_cbw_doom` images.
- Treaty decisions use `GFX_decision_category_contamination_defense` from `interface/chaosx_decisions.gfx` and vanilla `GFX_decision_generic_operation`.
- No new treaty sprite or texture is required by the implemented tranche.
- Natural smoke and ash uses the existing monthly model line and requires no icon or sprite registration.

## Future Plans

1. Add more contamination sources (reactor accidents, industrial disasters, strategic bombardment side effects).
2. Add regional climate bands so winter effects scale by latitude/biome instead of global random spread only.
3. Complete pooled decontamination, seed archive, evacuation corridor, inspection, vote, and major-burner treaty projects.
4. Expand the Fallout-owned blackout and winter transition art with additional air-tab iconography and threshold warning overlays.
