# Event 015 Ledger State Architecture Reaudit — 2026-07-16

## Verdict

**PASS after two bounded local correctness fixes.**

The ten Necessary Ground case cards are mutually exclusive and cover every lifecycle-consistent state; all seven district presentation roles have distinct durable mappings across ordinary, island, and incident paths; the six district state overlays are mutually exclusive; the seven-day planned presentation window has one tuning constant, one producer, natural expiry, and full-runtime cleanup; every variable-derived state scope in the scripted GUI is guarded; the actor-scoped recurring pulse does not perform a world scan; and the value/Calling consumers have matching sprite names, assets, and non-conflicting geometry.

No fallback or mechanics simplification was used. No commit was created, as required by the bounded audit assignment.

## Audit scope

Audited source files:

- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_decision_effects.txt`
- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/script_constants/015_utopia_manifesto_decision_constants.txt`
- `events/015_utopia_manifesto.txt`
- `interface/015_utopia_manifesto.gfx`
- `interface/015_utopia_manifesto_ledger.gui`

This audit did not redesign mechanics, edit assets, edit top-level Event 015 specifications, or create a commit.

## Required sources consulted

Repository guidance:

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_2_commonwealth_ledger.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/asset_manifest_plan.md`

Offline Paradox wiki snapshot:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- Scripted GUI modding
- Interface modding

The most relevant engine rules were variable default behavior, array `^num` reads, variable scopes, invalid-scope safety, default-AND short-circuiting, timed country flags, decision-category scripted-GUI scope, and element visibility mappings.

Vanilla documentation and precedents:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/AST_cabinet_trust_scripted_gui.txt`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/AST_cabinet_trust_scripted_gui.gui`

Vanilla current-script precedent also confirms a duration variable can be passed to `days =` in a timed `set_country_flag` block after loading a script constant into that variable.

## Local corrections made

### 1. Retire a historical expiration marker when a newer case opens

Changed `common/scripted_effects/015_utopia_manifesto_effects.txt` in the successful branch of `utopia_manifesto_open_need_case_against_from`:

```hoi4
clr_country_flag = utopia_manifesto_case_expired
```

The marker had one producer, `utopia_manifesto_expire_active_need_case`, and previously only the all-runtime teardown cleared it. A case could therefore expire, a later case could open and resolve, and the old expiration card could resurface after the newer state was gone. Clearing it only after the new-case validity limit succeeds preserves the historical card while there is no newer live case and retires it at the authoritative supersession point.

Lifecycle proof:

1. Expiry sets `utopia_manifesto_case_expired`.
2. Active-case teardown clears response, target, state, mission, and case variables but deliberately leaves the historical marker.
3. Candidate, selected-target, associate, stewardship, and live-case predicates all suppress the historical expiration card while a newer visible state exists.
4. A successfully opened newer case now clears the marker before setting `utopia_manifesto_need_case_active`.
5. Full Event 015 runtime teardown still clears the marker.

### 2. Keep a valid inactive target selection visible when the ultimatum predicate is already true

Changed `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` so `utopia_ledger_case_target_selected_visible` excludes ultimatum availability only when a case is active:

```hoi4
NOT = {
	AND = {
		has_country_flag = utopia_manifesto_need_case_active
		utopia_manifesto_case_can_issue_ultimatum = yes
	}
}
```

`utopia_manifesto_case_can_issue_ultimatum` can be true before a case is active through its lawful-ladder exception, for example a Closed Island actor with existential Need. The ultimatum card itself correctly requires an active case. The old unconditional exclusion could therefore suppress the selected-target card without allowing the ultimatum card, leaving a legitimate selection with no case card. The narrowed exclusion preserves active-case priority while making pre-case selection independent of an active-only display state.

## Criterion results

| Criterion | Result | Evidence |
| --- | --- | --- |
| Ten mutually exclusive case cards | PASS | 10 scripted visibility handlers, 10 GUI consumers, and 10 GFX sprites have exact stem parity. Exhaustive Boolean enumeration found zero overlap states. Lifecycle-consistent enumeration found exactly one card in every state. |
| Seven durable district roles | PASS | Seven unique constants map to one numeric `utopia_manifesto_district_visual_role`; all seven have scripted visibility, GUI, GFX, and DDS coverage. |
| Six exclusive district overlays | PASS | Six handlers have explicit dispute/block/terminal/recency/phase exclusions. Exhaustive enumeration across phase and condition inputs found zero overlaps. |
| Central seven-day planned window | PASS | `district_plan_card_days = 7`; one producer uses the constant through a temp variable; timed expiry is automatic; full district teardown explicitly clears the flag. |
| Missing-variable scope safety | PASS | All seven `var:utopia_manifesto_district_project_state` scopes are guarded by `has_variable`; missing numeric/array values are read only through safe numeric checks. |
| No recurring world scan | PASS | No daily, weekly, or monthly on-action exists in scope. The recurring actor event only reconciles tracked district states and refreshes actor state; it does not call country discovery. |
| Value/Calling consumer semantics and positions | PASS | 4/4 value and 6/6 Calling GFX-to-GUI stems match; decoded asset dimensions match the layout; static bounding boxes do not collide. |

## Case-card exclusivity and lifecycle proof

The active-state precedence is:

1. stewardship
2. refusal
3. counteroffer
4. pending offer
5. ultimatum available
6. selected target / active baseline

The inactive-state precedence is:

1. selected target
2. eligible candidate
3. established associate
4. historical expiration
5. no target

The predicates are made exclusive through explicit negative conditions rather than relying on GUI element declaration order.

Formal enumeration modeled stewardship, active case, selected target, any refusal, counteroffer, response, ultimatum predicate, historical expiration, first-associate memory, associate count, and candidate count:

- all `2^11 = 2,048` Boolean combinations: maximum simultaneous cards = 1; overlap states = 0
- `1,152` lifecycle-consistent combinations, where response/counter/refusal state requires an active case: exactly one visible card in all 1,152 combinations

Static trace:

| State trace | Visible card |
| --- | --- |
| inactive selected target + true lawful ultimatum predicate | target selected |
| active case, no response and no available ultimatum | target selected |
| active case + available ultimatum | ultimatum available |
| active response | offer pending |
| active response + counteroffer | counteroffer |
| active refusal, including stale lower-priority response/counter flags | refusal |
| stewardship active, regardless of lower-priority case state | stewardship active |
| inactive, no selection, candidate count above zero | target eligible |
| inactive, no selection/candidates, associate memory or count | associate established |
| inactive, no selection/candidates/associate, expired marker | expired |
| inactive, no selection/candidates/associate, no expired marker | no target |

`utopia_manifesto_clear_case_response_state` clears the response, counteroffer, settlement refusal, ultimatum refusal, and target refusal flags. `utopia_manifesto_clear_active_need_case` calls it before clearing the active case. Stewardship has its own authoritative teardown. New-case opening clears the old historical expiration marker after the validity gate succeeds.

## District role mapping

`utopia_manifesto_decision_district_role` defines seven distinct fixed-point integer identities:

| Role | Constant | Producer paths |
| --- | ---: | --- |
| market garden | 1 | ordinary district selection; district incident option |
| industrial housing | 2 | ordinary district selection; district incident option |
| rail junction | 3 | ordinary district selection; district incident option |
| refugee municipality | 4 | ordinary district selection; district incident option |
| port town | 5 | coastal-island commitment |
| research town | 6 | learning-and-care district incident option |
| inland island ring | 7 | inland-island commitment |

The four ordinary selection helpers set both project type and presentation role before calling the centralized project-state registrar. Island commitment supplies the two geography-specific roles. `chaosx.nr15.40` supplies ordinary incident recovery plus the research-town presentation role. Because one numeric variable stores the role, the seven role cards are intrinsically exclusive. The variable is cleared by full district runtime teardown, not by ordinary phase changes, so the last accepted presentation role is durable as required.

## District overlay exclusivity

The explicit priority is:

1. disputed
2. blocked
3. complete
4. planned
5. building
6. surveyed

Key exclusions:

- disputed reads the unresolved country dispute or guarded live-state breach/refusal/loss.
- blocked excludes disputed, then reads no-role, debt, delayed phase, or guarded state delay.
- complete excludes dispute and every blocking condition, then requires built or chartered phase.
- planned requires the recent-plan flag and a live project state, and excludes dispute, blocking conditions, built, and chartered.
- building requires a live state, an expired recent-plan window, a build/charter phase, and no dispute/block condition.
- surveyed requires a live state, surveyed phase, an expired recent-plan window, and no dispute/block condition.

Formal enumeration used seven phase values (`unset`, `surveyed`, `building`, `chartering`, `delayed`, `built`, `chartered`) and seven Boolean condition dimensions (live state, recent plan, country dispute, debt, no role, severe state conduct, state delay):

- combinations checked: 896
- maximum simultaneous overlays: 1
- overlap states: 0

Representative traces each returned exactly one overlay: surveyed, planned during the seven-day window, building after expiry, debt-blocked, built-complete, and state-breach disputed.

## Seven-day planned presentation lifecycle

- Tuning source: `utopia_manifesto_durations.district_plan_card_days = 7`.
- Sole producer: `utopia_manifesto_register_district_project_state`.
- Engine-safe dynamic duration path: script constant -> temp variable -> timed country flag `days =` value.
- Ordinary project selectors all call the centralized registrar.
- The planned overlay also requires a live state and excludes blocked, complete, and disputed outcomes.
- The building and surveyed overlays require the recent-plan flag to be absent.
- Timed expiry hands a continuing building/chartering project to the building overlay without an on-action.
- Full district teardown explicitly clears the flag, covering disable/teardown before natural expiry.

## Missing-variable and scope safety

The scripted GUI contains seven variable-derived state-scope reads:

- four are inside local `AND` blocks with `has_variable = utopia_manifesto_district_project_state` immediately before the scope
- planned, building, and surveyed have the same `has_variable` guard earlier in their outer default-AND trigger before the nested `var:` scope

This ordering is safe under documented default-AND short-circuit behavior. Role and phase checks use safe numeric `check_variable` behavior when variables are absent. Candidate and associate counts use safe array `^num` numeric reads, where an absent array count behaves as zero. No event target is used as a scripted-GUI scope.

## Recurring scan audit

`chaosx.nr15.150` is the actor-scoped recurring pulse. Its relevant path is:

`reconcile_tracked_district_state_control -> refresh_ledger -> evolution evaluation/validation -> reschedule actor event`

`utopia_manifesto_refresh_ledger` rebuilds actor-local/live contributions, clamps and bands values, refreshes Calling state, and dirties focus layout. It does not call `every_country`, case-candidate discovery, or league-candidate discovery.

No `on_daily`, `on_weekly`, `on_monthly`, or tag variant was introduced in the audited files.

One explicit non-recurring performance note remains: the player-clicked Ledger Refresh button also calls `utopia_manifesto_refresh_league_state`, which ends by rebuilding league candidates through two `every_country` loops. That path is manual and one-shot, not reachable from the recurring actor pulse, so it does not violate the accepted no-recurring-world-scan contract. It should remain a deliberate choice if the refresh button is changed later.

## GFX, GUI, and asset validation

Identifier parity:

- case cards: scripted 10, GFX 10, GUI 10, exact stem parity
- district roles: scripted 7, GFX 7, GUI 7, exact stem parity
- district states: scripted 6, GFX 6, GUI 6, exact stem parity
- value icons: GFX 4, GUI 4, exact stem parity
- Calling icons: GFX 6, GUI 6, exact stem parity

All 33 Ledger-folder texture references in `interface/015_utopia_manifesto.gfx` resolve to files.

Decoded DDS dimensions:

- 4 value icons: 32x32 BGRA
- 6 Calling icons: 48x48 BGRA
- 10 case cards: 300x96 BGRA
- 7 district role cards: 300x96 BGRA
- 6 district state overlays: 48x48 BGRA

Static layout proof:

- value columns use icon/text intervals `30-62 / 64-182`, `194-226 / 228-346`, `358-390 / 392-510`, and `522-554 / 556-674`, all within the 700-pixel container
- Calling art is scaled from 48x48 to 36x36
- left Calling text ends at x=276 and its icons occupy x=280-316
- right Calling text ends at x=602 and its icons occupy x=606-642
- both Calling columns remain inside the 652-pixel panel, with row origins at y=4, 74, and 144
- semantic order matches the GUI text columns: Need/Plenty/Concord/balance, then Provisioning/Workshops/Civic Works and Learning and Care/Maritime and Settlement/Defense and Watches

## Validation summary

- Exhaustive case-card overlap and lifecycle-coverage enumeration: PASS
- Static requested case lifecycle trace: PASS
- Exhaustive district-overlay overlap enumeration: PASS
- 10/7/6 scripted-GUI/GFX/GUI stem parity: PASS
- 4 value and 6 Calling GFX/GUI stem parity: PASS
- 33/33 Ledger texture paths present: PASS
- DDS dimension and pixel-format decode: PASS

## Remaining risks and handoff notes

- This was a static source and decoded-asset audit. No live engine render or click-region capture was performed in this bounded subagent turn. The value and Calling position verdict is based on exact decoded dimensions and GUI geometry.
- The disputed overlay is intentionally tied to a live unresolved dispute or guarded live project state. Once state-loss cleanup removes the current project pointer, the durable role can remain without a state overlay. That matches the current “active state plus durable role” contract; historical lost-state art would be a separate design request.
- The manual Refresh button's two league discovery scans are not recurring, but they are the only presentation-surface path that can scan all countries and should not be moved into the actor pulse.
- The district asset sibling supplied the seven role and six state DDS files during this audit under the already-wired stems. This architect subagent did not create or edit those assets.

## Files changed by this subagent

- `common/scripted_effects/015_utopia_manifesto_effects.txt`
  - clear stale `utopia_manifesto_case_expired` on successful newer-case opening
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`
  - scope ultimatum priority to active cases so an inactive selected target remains visible
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/ledger_state_architecture_reaudit_2026_07_16.md`
  - this audit record

No other source file was edited by this subagent. No commit was created.
