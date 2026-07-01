# Event 015 final improvement-loop depth audit addendum

## Implementation resolution

Status: accepted and implemented in the Event 015 workset.

- Mission-objective pass: implemented through objective-ready triggers for harvest rotation, household guard, boundary arbitration, marked district survey, League aid corridor, and renunciation vote.
- Needful Land arbitration: implemented as `mission_utopia_boundary_arbitration`; the decision starts a timed mission and only successful mission resolution adds a claim. It does not grant a core.
- Marked Bounds district survey: implemented as `mission_utopia_marked_district_survey`; the decision starts a timed survey and only successful mission resolution adds a risky claim.
- League confidence: implemented as auxiliary ledger value `utopia_league_confidence`, visible in the ledger footer and used by League target gating, AI focus weighting, League identity, aid outcomes, and the League achievement.
- Route unit families: implemented as Household Guard, Storehouse Engineers, Craft Militias, Harbor Watch, Surveyor Columns, and League Cadres with centralized caps and state/network scaling.
- Late cosmetic identity: implemented through `common/countries/cosmetic.txt`, cosmetic localisation, generated flag asset triplets, and late focus/League identity effects.
- Documentation/spec alignment: promoted into `docs/events/015_utopia_manifesto.md` and the source specs under `docs/specs/015_utopia_manifesto_specs/`.

Completion-report verification is tracked through the specialist audit handoffs in this folder rather than through a new design addendum.

## Audit verdict

Event 015 is broadly deep enough in its core surfaces. It is not a shallow event shell: the current implementation has a full replacement tree, a ledger category, dynamic ledger variables, targeted decisions, Needful Land and integration hooks, AI weights, achievements, assets, and two late super-events.

The closure package below has been implemented in the Event 015 workset. This document is retained as a trace of the accepted improvement-loop addendum rather than an open blocker list.

Accepted implementation facts were promoted into:

- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_3_decisions_mechanics.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_4_ai_assets_acceptance.md`
- `docs/events/015_utopia_manifesto.md`

## Prior addenda and handoff status

No prior improvement-loop addendum exists for Event 015.

Existing handoffs in this plans folder are specialist handoffs, not design addenda:

- `subagent_handoffs/2026-07-01_scripted_system_architect.md`
- `subagent_handoffs/2026-07-01_super_event_text_research.md`
- `subagent_handoffs/2026-07-01_super_event_audio_research.md`
- `subagent_handoffs/2026-07-01_decision_mission_audit.md`
- `subagent_handoffs/2026-07-01_decision_mission_followup_audit.md`
- `subagent_handoffs/2026-07-01_focus_tree_audit_patch_handoff.md`
- `subagent_handoffs/2026-07-01_country_package_adjacent_audit.md`
- `subagent_handoffs/2026-07-01_focus_icon_regeneration.md`
- `subagent_handoffs/2026-07-01_decision_idea_icon_regeneration.md`

The decision/mission audit findings were addressed by the follow-up decision mission patch and parent arbitration/ledger patches.

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

## Implemented closure package

### 1. Missions need map-objective consequences

Resolution: timed missions now resolve through timeout handlers and objective-ready triggers that check concrete map, resource, ledger, and target conditions before applying success effects.

Implemented as a small mission-objective pass rather than a large new mission system.

Implemented mission upgrades:

| Mission | Add objective pressure | Success | Failure |
| --- | --- | --- | --- |
| `mission_utopia_harvest_rotation` | ledger open, trains/support reserves still available, core states controlled, Need below crisis, and Vocation Balance holding | Need down, Surplus up, Vocation Balance up | Need up and Consent down |
| `mission_utopia_household_guard` | ledger open, Overreach safe, and a real defensive pressure such as war, armed borders, or nearby conflict | Consent up if defensive and Overreach safe | Foreign Suspicion up if used without threat |
| `mission_utopia_league_aid_corridor` | target still valid, no war with root, Surplus stable, League Confidence not low, and required convoys/trains/support equipment still available | target receives aid, root gains member/confidence progress | Foreign Suspicion up and League Confidence down |
| `mission_utopia_renunciation_vote` | require Consent stable and Overreach not high at timeout | clear Marked Bounds active flag and ready renunciation achievement | Overreach up and Marked Bounds pressure remains |

The implementation uses decision tooltips and ledger changes rather than popup follow-ups.

### 2. Needful Land arbitration should not be instant

Resolution: arbitration starts `mission_utopia_boundary_arbitration`, stores its target country and state in per-country arrays, and resolves only at timeout. A valid state can become a compensated settlement or guarantee-backed charter; refusal or invalid conditions add no claim and can call outside guarantees when Suspicion or hardline pressure is high.

Implemented surface:

- Decision id: keep `decision_utopia_boundary_arbitration`.
- New mission id: `mission_utopia_boundary_arbitration`.
- Active flag: `utopia_manifesto_boundary_arbitration_active`.
- Target state flag: `utopia_manifesto_boundary_arbitration_state`.
- Target country storage: `utopia_manifesto_boundary_arbitration_targets`.
- Target state storage: `utopia_manifesto_boundary_arbitration_states`.
- Duration: `@utopia_arbitration_days` in the decision file, currently 150 days.

Start requirements:

- Needful Land branch open.
- Need above the ordinary Needful Land gate.
- target state passes existing safety checks.
- target country is not a major unless already collapsing, at war, or otherwise explicitly safe.
- root can pay trains, command power, and stability cost.
- no active arbitration mission.

Success checks at timeout:

- Need remains proven.
- the stored state remains target-owned and target-controlled, is not already claimed, and is not a ROOT core.
- the target still exists, uses normal civilian systems, is not capitulated, and is not at war with ROOT.
- Overreach is safe unless `utopia_no_secret_empire` mitigates it.
- Foreign Suspicion is below danger unless commonwealth observers or no-secret-empire mitigations are present.

Success effects:

- add a witnessed claim, not an instant core.
- set visible state flags for arbitrated claims and the specific settlement outcome.
- compensated settlements spend Surplus and improve Consent.
- guarantee-backed charters create a real guarantee from the manifesto country to the target, raise League Confidence, and lower Foreign Suspicion.
- successful arbitration lowers Need and adds League Confidence while still making a small foreign-suspicion mark.

Failure effects:

- no core.
- no claim.
- target countries record a public refusal and receive the refusal opinion modifier.
- high Suspicion, high Overreach, or Marked Bounds pressure can draw an outside major guarantee to the target.
- Need, Foreign Suspicion, and Overreach rise while League Confidence falls.

### 3. League behavior needs a visible confidence layer, not a faction rewrite

Resolution: the League has visible `utopia_league_confidence`, friend and member counts, aid-corridor target storage, aid resolution, achievement gates, AI weights, and ledger GUI readouts.

No full faction or separate international organization was added; that would add bloat and conflict with the event's minor-country premise.

Implemented confidence/cohesion layer:

- Variable: `utopia_manifesto_league_confidence`.
- Display: ledger GUI right or footer line when `utopia_manifesto_league_of_need` is active.
- Rises from successful aid corridors, recognized friends, observers, and low Overreach.
- Falls from failed aid corridors, high Foreign Suspicion, Marked Bounds, offensive claims, and failed arbitration.
- Gate the League achievement on both member count and confidence above a modest threshold.
- Let `utopia_no_secret_empire` reduce suspicion or protect confidence after a claim.

AI behavior:

- AI starts League aid only when Surplus is stable, convoys/trains/support equipment are available, Foreign Suspicion is not high, and League Confidence is not low.
- AI weights pause League and diplomacy pressure when Need, Surplus, or Suspicion makes the route unsafe.
- Marked Bounds AI absorbs more diplomatic cost through its own route flags and harsher claim path.

### 4. Unit families should cover route identity without becoming a unit pack

Resolution: dynamic unit helpers cover Household Guard, Storehouse Engineers, Craft Militias, Harbor Watch, Surveyor Columns, and League Cadres, with centralized caps and state/network scaling.

Implemented focused helper families without turning the event into a broad unit pack.

#### Craft Militias

Purpose: Guild route defense and workshop mobilization.

Unlocks:

- `utopia_workshop_councils` or `utopia_guild_charter`.
- Decision can reuse existing vocation/apprenticeship costs.

Effects:

- spawn one small infantry-based militia batch from focus rewards, capped by controlled states and batch count.
- scale upward when Vocation Balance is stable.

AI:

- focus AI favors these through Guild and workshop route weights rather than a separate repeatable decision.

#### Surveyor Columns

Purpose: Marked Bounds and Needful Land occupation support without free conquest.

Unlocks:

- `utopia_mark_needed_districts`, `utopia_boundary_posts`, or `utopia_needful_land_commission`.

Effects:

- spawn one support/occupation division batch from Needful Land and Marked Bounds focus rewards.
- add capability without granting instant claims or cores.
- Marked Bounds route effects carry Overreach and Foreign Suspicion risk elsewhere in the branch.

AI:

- Marked Bounds focus AI uses these more aggressively.
- peaceful routes encounter them through Needful Land/integration focuses rather than broad repeatable spam.

#### League Volunteer Cadres

Purpose: make the League feel like cooperative manpower without forming a faction.

Unlocks:

- `utopia_league_of_need` and at least one successful aid corridor or recognized friend.

Effects:

- small capped defensive unit batch from League focus rewards, scaled by friend and League member counts.
- League aid missions separately spend convoys, trains, support equipment, Surplus, and confidence pressure.

AI:

- focus and decision AI use the League route only when Surplus, confidence, and diplomatic safety are stable enough.

Do not add Hired Companies in this pass. More's mercenary material is useful historical contrast, but adding mercenary gameplay now would create a second dark-war economy beside Marked Bounds.

### 5. Late identity needs cosmetic closure

Resolution: late outcomes apply cosmetic tags and fictional generated flag packages while keeping the original country tag and leader.

Implemented cosmetic identity package:

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

The addendum is resolved by the implemented option: the parent implemented the scoped mission, arbitration, League confidence, route-unit, ledger-GUI, and cosmetic identity closure package and updated docs/spec alignment.

Closure evidence:

- decision/mission audit findings were addressed by the follow-up audit patch and parent mission patches.
- the ledger GUI has route, geography, pressure, active project, League, and scripted action buttons.
- route unit gaps are covered by the focused helper families listed above.
- late cosmetic identity is implemented with generated flag packages and ideology-specific runtime variants.
- `docs/events/015_utopia_manifesto.md`, asset manifests, and source specs match the accepted implementation.
