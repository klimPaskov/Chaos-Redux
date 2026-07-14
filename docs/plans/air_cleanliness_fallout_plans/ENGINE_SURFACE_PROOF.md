# Fallout Engine Surface Proof

Status: implementation gate record for the installed Hearts of Iron IV build and the current Chaos Redux map surface.

This record separates proven engine behavior from design intent. A surface listed as unproven is not silently replaced by a weaker mechanic.

## Reference set

The proof pass used the required offline wiki pages in `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding, Map modding, State modding, Building modding, and Graphical asset modding.

The following official game documentation was used as the higher authority:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/map_modes/documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/_documentation.md`

## Exact thermonuclear province sweep

Verdict: exact native per-province strike semantics are proven through a verified province ledger. Bounded execution cost is not yet proven.

The engine does not expose `every_province`. That absence does not require a state-level substitute. The accepted manual-scenario plan explicitly permits a supported expansion of a verified province list into nuclear effects.

The exact route is:

1. Build a stable ledger from the installed map data.
2. Include only province ids that appear in a valid state `provinces` block and whose `map/definition.csv` type is `land`.
3. Store the ledger in script data and iterate it with the documented array loop effects.
4. Pass each ledger value to the native `launch_nuke` effect with `nuke_type = thermonuclear_bomb`.
5. Advance a persistent batch cursor and begin the seven-day countdown only after the final ledger entry is struck.

Current map audit:

- Chaos Redux has no `map/` override.
- Vanilla has 10,272 unique state-assigned province ids.
- 10,154 of those ids are land provinces in `map/definition.csv`.
- 118 state-assigned ids are non-land and are excluded.
- One land province in `map/definition.csv` is not assigned to a state and is excluded.

This route produces 10,154 actual thermonuclear launch calls. It does not use one strike per state, province modifiers, or variable-only fallout. The engine does not enumerate the provinces itself. The ledger is a version-pinned expansion of installed map data, while every result is still produced by the native `launch_nuke` effect.

Engine evidence:

- `effects_documentation.md`, `launch_nuke`, accepts a province target and an explicit `nuke_type`.
- `effects_documentation.md`, `add_to_array`, `for_each_loop`, and `for_loop_effect`, support scalar province-id storage and deterministic iteration.
- Vanilla `common/raids/nuclear_raids.txt` passes a variable-backed province id to `launch_nuke` and sets `nuke_type = thermonuclear_bomb`.

The ledger must be regenerated and reviewed if Chaos Redux adds a map override or the installed game map changes. The scenario remains blocked from release until a bounded batch implementation proves that every ledger entry is struck exactly once and that the ordinary `on_nuke_drop` pipeline can be safely aggregated for the sweep.

## Exact seven-day delay

Verdict: proven, provided the delayed event is owned by a country guaranteed to exist for the full interval.

`effects_documentation.md`, `country_event`, defines `days` as an exact delay and treats months separately as 30 days. Vanilla `events/AAT_Denmark.txt` repeatedly uses `country_event = { id = ... days = 7 }`.

The manual Fallout scenario will schedule the coordinator event with `days = 7` and no random delay after the final strike batch completes. Persistent completion and countdown flags prevent the sweep from restarting after save recovery. The offline Event modding reference notes that delayed country events stop counting while their target country does not exist, so the coordinator must remain alive through the countdown.

## Host authority and idempotency

Verdict: single-execution simulation authority is proven. Literal multiplayer lobby-host authority is not exposed by the documented script surface.

`common/on_actions/chaosx_on_actions_chaos_meter.txt` owns a single monthly path with the project-defined `is_global_host` country flag. Startup assigns that flag to one human country, and the project uses it as a deterministic simulation coordinator. No official trigger or scripted-GUI surface was found for identifying the actual network lobby host. Fallout extends the existing coordinator route and does not add another global daily, weekly, or monthly country iteration.

All request sources write to one global request ledger. The coordinator accepts the first valid request, records cause and intensity, and rejects duplicate transition starts. Manual, terminal-event, and Air Contamination callers do not own their own rewrite chains.

## Winter mapmode

Verdict: proven.

Official scripted map-mode documentation supports state color layers, country background layers, daily updates, state tooltips, and a forced refresh effect. Chaos Redux already has working state mapmode precedents in `common/map_modes/chaosx_state_map_modes.txt`.

The Air Winter mapmode can therefore expose phase, trend, exposure, recovery, adaptation, food, shelter, reclamation, and category pressure without relying on a country-wide color.

## Normal-map climate route

Verdict: official effect signatures and the approved normal-mapped entity precedent prove the regional state-cue route. Runtime visual observation is outside this proof. Native runtime weather replacement is not claimed.

The normal-map prototype evaluates two independent script surfaces:

- A low-opacity player-context GUI grade attached to the main interface. Its visual elements use `alwaystransparent = yes`, which the offline Interface modding reference defines as click-through behavior. Full-screen sizing and click-through are separately documented, but no local precedent proves a parentless full-screen grade that stays behind every hardcoded window. The proof must therefore check interface tint, border readability, mapmode interaction, and open-window behavior before this surface is accepted.
- State-positioned, normal-mapped 3D entities created with the documented `create_entity` effect. The effect accepts state or province placement, scale, minimum zoom, a stable id, and a scripted visibility trigger. `destroy_entity` and stable replacement ids provide a lifecycle surface for thaw and cleanup.

The approved Kaiserreich reference implements runtime landmarks through `common/scripted_effects/00_ambient_object_effects.txt`, registers the matching entities under `gfx/entities/landmarks.asset` and `gfx/entities/landmarks.gfx`, and calls those helpers from live country events. Its compiled meshes bind diffuse, normal, and specular textures. This proves the runtime normal-mapped entity chain on the ordinary map.

The route can place coarse regional snow, frost, cold rain, ash, dead vegetation, frozen-water, and thaw cues on the ordinary map. Presentation class and phase decide which entity family is used. Desert and tropical states do not inherit universal snow. A state target chooses the entity center. It does not conform the mesh to state borders and does not rewrite the static terrain normal map. The implementation must therefore call this a normal-mapped entity route, not a terrain-normal or state-decal rewrite.

The official effect catalogue exposes `randomize_weather`, but it does not expose a state or strategic-region effect for forcing a selected weather type or replacing the native snow-cover simulation. The implementation therefore does not claim to rewrite native weather or water shaders. Military weather pressure is driven by the same state phase through documented modifiers while the supported entity layer supplies the matching normal-map cue.

Save recovery must derive from the saved state phase and presentation class because `on_startup` does not run when loading a save and no useful `on_load` route is documented. Runtime-created entity serialization is not documented. The lifecycle effect must therefore reconstruct the desired entity on every existing Air Winter coordinator pulse. Reusing a stable id is documented to replace an existing entity, making that reconstruction idempotent. Recovery is guaranteed on the first resumed coordinator pulse, not at the load screen. Entity ids have no documented reserved range, so Fallout and Air Winter require their own reviewed id ledger before rollout.

Multiplayer clients read the synchronized phase ledger and receive the same scripted effects. The bounded prototype supplies one coarse entity, one proof state, one reserved stable id, a create-or-replace helper, and a destroy helper. Zoom behavior, terrain intersection, visual replacement, and save recovery remain unobserved runtime properties and are not claimed.

## Blackout GUI and input control

Verdict: full-screen cover, sequential text, mouse-modal blocking, save recovery, and host sequencing are proven. Complete keyboard interception is not proven.

A player-context scripted GUI can attach a full-screen container to the base interface. A non-transparent full-screen element prevents pointer interaction with elements behind it. Visibility and text selection can read synchronized global variables, so save-load restores the active beat without relying on a nonexistent `on_load` recovery hook. Only the project simulation coordinator advances the beat and performs rewrite effects.

Neither the official scripted-GUI documentation nor the offline Interface modding reference exposes a modal, exclusive-input, keyboard-capture, or pause-game script property. Individual buttons can define shortcuts, but the references do not prove that a scripted GUI can suppress every hardcoded keyboard action.

This is an engine-sensitive blocker for the literal interpretation of all-input blocking. The implementation must not claim complete keyboard lock without a proven engine surface. Mouse-modal blackout and gameplay-system locks can still be built, but using them as a substitute for total keyboard interception requires an explicit user decision.

## Dynamic successor allocation

Verdict: the creation effect is proven. Conflict-free allocation still requires the live ledger.

`create_dynamic_country` is documented in `effects_documentation.md`. It can create a country from a selected original or copy tag and run initialization effects. Fallout may use it only after the live conflict ledger records occupied tags, active event countries, reserved player identity, and selected successor packages. The 99-successor matrix remains a candidate pool.

## Open proof obligations

- Preserve the recorded normal-map runtime observation checklist without claiming that its visual checks were performed.
- Measure entity density and strike-batch execution cost on the current map.
- Record whether a verified hardcoded modal surface exists for complete keyboard blocking. None was found in the documented script interfaces.
- Record that no documented literal lobby-host trigger exists. `is_global_host` is a project simulation coordinator.
- Re-run the province-ledger audit after any map-version change.
