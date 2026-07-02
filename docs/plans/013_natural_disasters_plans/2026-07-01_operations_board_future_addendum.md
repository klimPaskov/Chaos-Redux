# Event 013 post-completion addendum: Disaster Operations Board

Date: 2026-07-01
Status: Accepted and implemented in the current tranche as a compact four-slot decision-category operations board. Optional relief-liaison and lane-header expansion remains future-only.

## Implementation note

The implemented board lives in `common/scripted_guis/013_natural_disasters_scripted_gui.txt`, `interface/013_natural_disasters.gui`, `common/scripted_effects/013_natural_disasters_effects.txt`, and `common/scripted_triggers/013_natural_disasters_triggers.txt`. It opens from the Event 013 response category, refreshes four priority slots from controlled aftermath and warning states, stores the selected state through cleared global event targets, shows family/phase/risk/action text through scripted localisation, and routes rescue, route clearance, supply restoration, and evacuation buttons through the same concrete-cost scripted effects used by the recovery decisions. It does not add per-disaster Event Log entries or AI dependency on the GUI.

## Scan result

Event 013 is deep enough that another disaster-family, evolution, super-event, or recovery-mechanic pass would add bloat. The useful depth gap was presentation and command clarity: the scripted GUI needed to show active hazards, predicted paths, affected states, danger level, and response actions rather than only abnormal warning animations and the latest family picture.

This is not a missing recovery mechanic. Recovery decisions, missions, AI priorities, warning flags, moving corridor state, building damage, deaths-system losses, SCN-007, clusters, news, and super-event surfaces already exist. The issue is that the player reads those systems through regular decisions and a compact warning panel rather than a full operations board.

## Prior addendum status

- `docs/plans/013_natural_disasters_plans/2026-07-01_completion_audit_resolution.md` records the previous broad audit resolution and appears folded into the current implementation/documentation.
- Event 013 category-picture and animation handoffs indicate their asset scopes were completed or superseded by later parent validation.
- No unresolved broad design addendum for an operations board was found in `docs/plans/013_natural_disasters_plans/`.
- The scripted API audit risk around `natural_disaster_news_state` was resolved by carrying the affected state as a regular event target into immediate human-country news delivery instead of storing one shared delayed global news target.

## Research anchors

Use these as flavor and structure anchors, not as claims that every country used the same institutions:

- Civil defense model: wartime Air Raid Precautions personnel handled shelters, masks, blackout, incendiary fighting, and rescue work after attacks; shelter marshals handled order and first aid in shelter systems. This supports a board organized around rescue posts, shelter/medical support, route clearance, fire control, and evacuation.
- Relief liaison model: the Joint Relief Commission of the International Red Cross operated from 1939 to 1946 with National Red Cross Societies and sent food, clothing, medical, and pharmaceutical supplies to affected civilians. This supports optional relief-convoy flavor if the system ever needs a diplomatic or convoy-cost action.
- Forecast desk model: international meteorological cooperation predates the period through the International Meteorological Organization, and wartime meteorological coordination included civilian/military forecast-analysis structures. This supports forecast cards, uncertainty bands, and path-warning text without making the system feel modern.

Sources consulted:

- `https://www.rafmuseum.org.uk/research/online-exhibitions/history-of-the-battle-of-britain/air-raid-shelter-protection/`
- `https://blogs.icrc.org/cross-files/the-icrc-during-world-war-ii/`
- `https://wmo.int/about-wmo/history-of-imo-and-wmo`
- `https://www.weather.gov/timeline`

## Proposed enhancement

Add an optional human-facing `Disaster Operations Board` after Event 013 completion. It should reuse existing variables, flags, decisions, AI priorities, warning sprites, and category pictures. It should not add new disaster families, new Event Log rows, or new super-events.

### Entry and scope

- Keep the current compact category strip as the always-available warning surface.
- Add a no-cost decision such as `natural_disaster_open_operations_board`, visible only when the existing response category is visible and the country has active recovery or warning state.
- The decision opens a separate scripted GUI window by setting a country flag such as `natural_disaster_operations_board_open`; a close button clears it.
- Prefer a `player_context` independent scripted GUI container for the larger board. If the implementation stays inside `decision_category` context, avoid relying on temporary arrays or temp scopes for state lists because the wiki warns that decision-category scripted GUI has context limitations.

### Data model

Reuse existing state and country state where possible:

- Active recovery states: states with Event 013 aftermath, emergency, stabilization, or reconstruction state.
- Warning states: states flagged for moving corridor, tsunami countdown, ashfall, skyfall, or related abnormal warnings.
- Priority: reuse or mirror the existing `natural_disaster_ai_recovery_priority` scoring so the board shows the same states the AI already treats as urgent.
- Selected state: either a single country event target/global target cleared on close, or fixed priority slots refreshed by a scripted effect. Do not introduce daily or weekly world iteration for board refresh.

If true dynamic state lists are fragile, implement four fixed priority slots instead:

- Slot 1: highest active emergency or active abnormal warning.
- Slot 2: next highest recovery priority.
- Slot 3: next active recovery state.
- Slot 4: newest/latest family state.

Each slot should clean up when the state no longer has Event 013 aftermath or warning state.

### Board layout

The board should be functional, restrained, and data-led:

- Header: latest disaster family, open recovery-state count, worst phase, top risk band, and active abnormal warning badge if any.
- Active state cards: up to four cards or a dynamic list with state name, family icon, current phase, priority band, warning badge, and select/focus button.
- Selected-state panel: current family, damage/recovery phase, likely next hazard if predicted, death-risk band, supply/port/rail/food/fire/ash/dust concerns, and short "why this state matters" tooltip.
- Operations lanes: Rescue, Routes and Ports, Shelter and Medical, Forecast Desk, Relief Liaison. These are grouping labels for existing decision types, not new route families.
- Action routing: first implementation should route the player to existing decisions or focus the selected state. Do not duplicate resource-spending decisions as GUI buttons unless those buttons call the same scripted triggers/effects and have AI equivalents.

### Optional Phase 2 only

If the board feels too passive after Phase 1, add exactly one relief-liaison action family:

- `Request International Relief`: costs convoys or political power, requires active high-severity aftermath, has a cooldown, and reduces famine/refugee/recovery pressure modestly.
- `Send Relief Convoy`: available to stable countries with convoys/support equipment and nearby diplomacy; improves relations or grants a small stability/war-support effect while consuming real resources.

This should remain optional. It can easily bloat Event 013 into a diplomacy system, so add it only if the parent wants a specific post-completion diplomatic hook.

### AI behavior

- AI must not depend on the GUI.
- AI continues using the existing recovery decisions and missions.
- If Phase 2 relief actions are added, AI use must check convoy/equipment availability, war pressure, ideology/diplomacy constraints, and cooldowns.

### Assets

Reuse existing Event 013 assets:

- `GFX_decision_cat_picture_nd_*` family pictures for selected-state/family art.
- Existing animated warning sprites for corridor, tsunami, ashfall, skyfall, and general pulse.
- Existing decision icons for rescue, clear routes, restore supply, ports/airfields, food/water, firebreaks, ash/dust, and evacuation.

Only request new icons if the board needs distinct lane headers:

- `GFX_nd_board_rescue_post`
- `GFX_nd_board_relief_convoy`
- `GFX_nd_board_forecast_desk`
- `GFX_nd_board_shelter_medical`

No new super-event art or audio is justified for this addendum.

## Acceptance criteria

- The board exposes existing Event 013 state rather than inventing new disaster mechanics.
- It shows at least the top four active or warning states, with state names, family, phase, risk/priority band, and a route to the relevant existing decisions.
- It closes and cleans its selected-state/slot state when no Event 013 recovery or warning state remains.
- It does not create per-disaster Event Log entries.
- It does not add world-iteration on actions.
- It keeps AI behavior on the existing decision/missions path.
- It leaves current compact category GUI usable for players who do not open the board.

## What should not be added

- No new disaster families.
- No broad foreign-aid economy.
- No scientific or military exploitation hook unless another event explicitly asks for it.
- No per-disaster Event Log entries.
- No new super-events.
- No focus tree, country package, formable, or achievement expansion.

## Promotion guidance

Keep this file in `docs/plans/013_natural_disasters_plans/` as the implementation note for the current compact board and as the future queue for optional relief-liaison or lane-header expansion. The implemented board is summarized in `docs/events/013_natural_disasters.md`.
