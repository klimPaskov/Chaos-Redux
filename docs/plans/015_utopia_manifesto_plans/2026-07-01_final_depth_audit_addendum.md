# Event 015 final improvement-loop depth audit addendum

## Audit verdict

Event 015 is broadly deep enough in its core surfaces. It is not a shallow event shell: the current implementation has a full replacement tree, a ledger category, dynamic ledger variables, targeted decisions, Needful Land and integration hooks, AI weights, achievements, assets, and two late super-events.

The remaining depth risk is narrower: several late or event-adjacent systems are present but thinner than the source specs promised. These should be treated as a queued final polish/blocker package before the event is called complete, unless the parent explicitly rejects them as out of scope.

This addendum should stay in `docs/plans/015_utopia_manifesto_plans/` until accepted. If accepted, promote the chosen changes into:

- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_3_decisions_mechanics.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_4_ai_assets_acceptance.md`
- `docs/events/015_utopia_manifesto.md` after implementation matches the final behavior

## Prior addenda and handoff status

No prior improvement-loop addendum exists for Event 015.

Existing handoffs in this plans folder are specialist handoffs, not design addenda:

- `subagent_handoffs/2026-07-01_scripted_system_architect.md`
- `subagent_handoffs/2026-07-01_super_event_text_research.md`
- `subagent_handoffs/2026-07-01_super_event_audio_research.md`
- `subagent_handoffs/2026-07-01_decision_mission_audit.md`

The decision/mission audit remains unresolved and is the main reason this final audit is not a closure handoff.

## Evidence of sufficient depth

The current implementation already satisfies the main event promise:

- Event entry exists as `chaosx.nr15.1`, has AI accept and human reject paths, and uses `GFX_report_event_utopia_manifesto_found`.
- The focus tree has 105 focuses and AI weights on all focus entries.
- The decision file has 26 decisions or missions and 22 decision-side AI blocks.
- Ledger values exist as Need, Consent, Surplus, Overreach, Vocation Balance, and Foreign Suspicion, with constants, triggers, display variables, and refresh helpers.
- Needful Land claims and integration projects use state flags, costs, compliance gates, active project caps, and delayed completion instead of instant coring.
- Achievements are present as 12 Event 015 achievements with final icon triplets.
- Runtime assets exist for the event picture, boundary-crisis news image, two super-event images, focus icons, decision icons, idea icons, achievement icons, ledger panels, and animated ledger seal.
- New Utopia and Marked Bounds super-events have sourced quote/audio handoffs and runtime music/sound wiring.
- `docs/events/015_utopia_manifesto.md` documents the implemented event, ledger, focus routes, decisions, integration, units, assets, and super-events.

## Remaining depth gaps

### 1. Missions need map-objective consequences

Current risk: the mission layer is mostly timed ledger resolution. The source spec asks the player to hold ports, maintain supply, protect storehouses, complete harvest rotation, send aid, arbitrate claims, and administer local districts.

Implement a small mission-objective pass rather than a large new mission system.

Required mission upgrades:

| Mission | Add objective pressure | Success | Failure |
| --- | --- | --- | --- |
| `mission_utopia_harvest_rotation` | require peace or no occupation of core states, enough trains/support equipment, and no severe low-supply state if feasible | Need down, Surplus or Vocation Balance up | Need up, Consent down, delay rural rotation repeat |
| `mission_utopia_household_guard` | require active defensive posture: at war, threatened, or enough divisions in controlled core states | Consent up if defensive and Overreach safe | Foreign Suspicion up if used without threat |
| `mission_utopia_league_aid_corridor` | require target still exists, no war with root, route or sea access where possible, and required convoys/trains/support equipment still available | target receives aid, root gains member/confidence progress | root loses Surplus/Consent or gains Suspicion, target flag clears |
| `mission_utopia_renunciation_vote` | require Consent stable and Overreach not high at timeout | clear Marked Bounds active flag and ready renunciation achievement | Overreach up and Marked Bounds pressure remains |

Do not add many popup follow-ups. Use decision tooltips and ledger changes unless the event text already has a specific moment to show.

### 2. Needful Land arbitration should not be instant

Current risk: arbitration immediately creates a Needful Land claim. That weakens the event's core ethical tension because proof, consent, and administration are supposed to matter before ownership.

Add one explicit arbitration mission.

Proposed surface:

- Decision id: keep `decision_utopia_boundary_arbitration`.
- New mission id: `mission_utopia_boundary_arbitration`.
- Active flag: `utopia_manifesto_boundary_arbitration_active`.
- Target state flag: `utopia_manifesto_boundary_arbitration_state`.
- Optional target country flag: `utopia_manifesto_boundary_arbitration_target`.
- Duration: 120 to 180 days through `constant:utopia_manifesto_duration.boundary_arbitration_days` if the effect field accepts it, otherwise a file constant with the existing duration style.

Start requirements:

- Needful Land branch open.
- Need above the ordinary Needful Land gate.
- target state passes existing safety checks.
- target country is not a major unless already collapsing, at war, or otherwise explicitly safe.
- root can pay trains, command power, and stability cost.
- no active arbitration mission.

Success checks at timeout:

- root still controls or can legally administer the state, or the target accepted arbitration through relationship status.
- Overreach is not high unless Marked Bounds is active.
- Foreign Suspicion is below danger or observers/no-secret-empire mitigations are present.
- local household or storehouse work exists if the state is already occupied.

Success effects:

- add claim or unlock integration project, not instant core.
- set a visible state flag marking the claim as arbitrated.
- reduce Need slightly and increase Foreign Suspicion slightly.
- for peaceful success, add toward `achievement_utopia_need_not_greed_ready` progress if no offensive-war disqualifier is set.

Failure effects:

- no core.
- if peaceful route: refund part of the claim pressure through Consent or Need relief, but do not create land.
- if Marked Bounds: allow a harsher follow-up decision, with Overreach and Foreign Suspicion costs.
- set a cooldown so the same target is not spammed.

### 3. League behavior needs a visible confidence layer, not a faction rewrite

Current risk: the League exists as a focus, idea, target flags, member count, and aid mission. That is playable, but it can read like a counter rather than a league.

Do not implement a full faction or separate international organization. That would add bloat and conflict with the event's minor-country premise.

Add a small confidence/cohesion layer:

- Variable: `utopia_manifesto_league_confidence`.
- Display: ledger GUI right or footer line when `utopia_manifesto_league_of_need` is active.
- Rises from successful aid corridors, recognized friends, observers, and low Overreach.
- Falls from failed aid corridors, high Foreign Suspicion, Marked Bounds, offensive claims, and failed arbitration.
- Gate the League achievement on both member count and confidence above a modest threshold.
- Let `utopia_no_secret_empire` reduce suspicion or protect confidence after a claim.

AI behavior:

- AI should start League aid only when Surplus is stable, convoys/trains/support equipment are available, and Foreign Suspicion is not high.
- AI should pause League aid when Need is high and Surplus is low.
- AI should not pursue League confidence if Marked Bounds is active unless the hardline route explicitly absorbs the diplomatic cost.

### 4. Unit families should cover route identity without becoming a unit pack

Current implementation has two concrete dynamic unit families: Household Guard and Storehouse Engineers. That is enough for a base military identity but not enough for the Guild, League, and Marked Bounds branches promised in the spec.

Add only three additional small helpers. Do not implement every brainstormed unit family.

#### Craft Militias

Purpose: Guild route defense and workshop mobilization.

Unlocks:

- `utopia_workshop_councils` or `utopia_guild_charter`.
- Decision can reuse existing vocation/apprenticeship costs.

Costs:

- infantry equipment
- support equipment
- Vocation Balance or Consent pressure if spammed

Effects:

- spawn one small light infantry or militia-style division batch, capped by controlled states and batch count.
- improve defense or production recovery through an idea if the parent prefers no new template.

AI:

- use when threatened, low division count, or Guild route selected.
- avoid if equipment is scarce or Consent is low.

#### Surveyor Columns

Purpose: Marked Bounds and Needful Land occupation support without free conquest.

Unlocks:

- `utopia_mark_needed_districts`, `utopia_boundary_posts`, or `utopia_needful_land_commission`.

Costs:

- army XP
- trucks or cavalry/infantry equipment
- Overreach and Foreign Suspicion risk

Effects:

- spawn one support/occupation division or apply a temporary state administration modifier.
- improve integration speed only for states already marked by Needful Land.
- never grant instant claims or cores.

AI:

- only Marked Bounds AI uses aggressively.
- peaceful AI uses only when an active integration state has resistance or low compliance.

#### League Volunteer Cadres

Purpose: make the League feel like cooperative manpower without forming a faction.

Unlocks:

- `utopia_league_of_need` and at least one successful aid corridor or recognized friend.

Costs:

- support equipment
- convoys or trains
- Surplus
- League confidence

Effects:

- small capped defensive unit or equipment/manpower aid from member network.
- if the root is not at war, prefer equipment and planning bonuses over units.

AI:

- use only in defensive war, low division count, or when a League member is threatened and root has stable Surplus.

Do not add Hired Companies in this pass. More's mercenary material is useful historical contrast, but adding mercenary gameplay now would create a second dark-war economy beside Marked Bounds.

### 5. Late identity needs cosmetic closure

Current risk: late outcomes have focuses, spirits, and super-events, but the implementation appears not to apply cosmetic tags, fictional flags, or map-name changes. The spec reserved this surface for New Utopia, League leadership, and Marked Bounds.

Add the smallest viable cosmetic identity package:

| Identity | Trigger | Effect |
| --- | --- | --- |
| New Utopia | `utopia_new_utopia` completed, high Consent/Surplus, Overreach safe | set cosmetic tag/name and apply New Utopia flag |
| Utopian League | `utopia_league_of_need` complete, member count and confidence met | optional cosmetic name if the parent wants a public League identity |
| Marked Bounds State | `utopia_marked_bounds_state` completed | set hardline cosmetic tag/name and Marked Bounds flag |

Implementation surfaces:

- `common/countries/cosmetic.txt` or the repo's existing cosmetic-tag file.
- localisation for cosmetic names.
- fictional flag DDS triplets if cosmetic flags are accepted.
- focus completion rewards for the late proclamation focuses.
- docs asset manifest update.

Do not add new tags, cores, formable decisions, country leaders, or portrait systems in this pass. Keep the original country tag and leader unless a later country-package plan explicitly asks for more.

## Historical and thematic basis

The design should keep using Thomas More's `Utopia` as contrast, not as a generic socialist or fascist tree.

Useful anchors already present in the specs:

- common stores and public distribution justify Surplus, storehouses, and aid corridors.
- household census, councils, and public reading justify Consent and visible ledger accountability.
- agriculture and useful trades justify Vocation Balance and Craft Militia/workshop service.
- the "idle land" clause justifies Needful Land and Marked Bounds as a moral danger, not a normal conquest tree.
- More's war and mercenary passages can inform the tension around League defense and dark-route coercion, but should not become a new mercenary economy in this pass.

Regional adaptation should stay generic because the target country is dynamic. Use geography, size, subject status, coastal/landlocked checks, and state control rather than country-specific history.

## What should not be added

Do not add:

- a full League faction or custom international-organization system.
- new focus branches.
- new country tags.
- leader or portrait replacement.
- large scripted GUI tabs beyond status, route, project, and League confidence display.
- a mercenary/hired-company subsystem.
- instant coring or broad claim generation.
- more super-events.

These would increase bloat more than depth.

## Acceptance criteria for this addendum

The addendum is resolved when one of the following is true:

1. The parent implements the scoped mission, arbitration, League confidence, route-unit, and cosmetic identity closure package and updates docs/specs.
2. The parent explicitly rejects one or more sections with a reason, then updates docs so the remaining implementation is not claiming those rejected surfaces.
3. The parent queues part of the package with a reason, leaving this plan open as a known blocker for final completion.

Implementation should be considered complete only after:

- the decision/mission audit findings are addressed or rejected.
- the ledger GUI either gains route/project/League state readout or the display-only limitation is explicitly accepted and documented.
- route unit gaps are implemented or rejected as bloat.
- late cosmetic identity is implemented or rejected as bloat.
- docs/events and source specs match the accepted implementation.

