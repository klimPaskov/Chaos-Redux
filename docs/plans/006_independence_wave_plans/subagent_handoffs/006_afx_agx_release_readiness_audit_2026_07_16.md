# Event 006 AFX/AGX release-readiness audit

> **Portrait-specific supersession (2026-07-16):** The old portrait hashes,
> comparisons, and visual-fallback conclusion are superseded by the male-HOI4
> package manifest and final independent audit. Gameplay and admission findings
> remain historical on their own terms.

Date: 2026-07-16
Mode: read-only source audit; this handoff is the only file created
Packages: IW-006 / AFX / Wallonia and IW-007 / AGX / Frisia
Dependency under re-audit: FORM-03 Low Countries progression restoration

## Executive verdict

**PASS for one coordinated promotion of IW-006 and IW-007.** The package,
FORM-03, tag, allocator, host-survival, Event 005 collision, scenario,
localisation, AI, and visual surfaces reviewed below contain no remaining
static content blocker.

The checked-in source is nevertheless still **intentionally fail-closed**.
Neither package can currently enter the automatic pool, and neither package
can currently enter SCN-008, because the three compile-time admission gates
listed in [Exact authorized gate changes](#exact-authorized-gate-changes) have
not yet been promoted. This audit authorizes those three changes only, as one
atomic change set. It does not claim that the checked-in packages are already
selectable.

| Required result | Static promotion verdict | Current checked-in behavior | Behavior after the exact coordinated gate changes |
| --- | --- | --- | --- |
| Automatic IW-006 / AFX | **PASS** | **FAIL-CLOSED**: the IW-006 readiness wrapper returns `always = no`, and runtime content attestation omits package ID 6 | Eligible for the ordinary weighted automatic allocator only when its live tag, anchor, host, uniqueness, capacity, and Event 005/006 safety proofs pass |
| Automatic IW-007 / AGX | **PASS** | **FAIL-CLOSED**: the IW-007 readiness wrapper returns `always = no`, and runtime content attestation omits package ID 7 | Eligible for the ordinary weighted automatic allocator only when its live tag, anchor, host, uniqueness, capacity, and Event 005/006 safety proofs pass |
| SCN-008 IW-006 / AFX | **PASS** | **FAIL-CLOSED**: scenario package preflight has no exact IW-006 branch | Attempted from its single ranked-registry row and accepted only when the exact AFX availability proof and shared reservation API pass, for every valid scenario type and intensity |
| SCN-008 IW-007 / AGX | **PASS** | **FAIL-CLOSED**: scenario package preflight has no exact IW-007 branch | Attempted from its single ranked-registry row and accepted only when the exact AGX availability proof and shared reservation API pass, for every valid scenario type and intensity |
| Host survival | **PASS** | The shared N-1 capacity, protected-state, frozen-host snapshot, capital-relocation, and post-transfer ownership proofs are already active | Unchanged; BEL, HOL, or any later live anchor owner must retain at least one protected owned state |
| Event 005 collision safety | **PASS** | Shared country/state reservations, active-origin exclusions, capacity witnesses, one lock, and one transaction already protect the joint route | Unchanged; Event 005 reserves first and Event 006 rejects or rerolls around its frozen footprint before either event mutates ownership |

The word **PASS** above is a release-authorization verdict based on current
static source. It is not evidence of an in-game execution. No runtime session
or save was executed by this audit.

## Exact authorized gate changes

All three functional changes below must land together. A partial promotion is
not authorized: it would either leave one route closed or make automatic and
scenario admission disagree about the same audited package.

### 1. Replace the two fail-closed static readiness wrappers

File: `common/scripted_triggers/006_independence_wave_package_triggers.txt`

The resulting wrapper bodies should be exactly:

```txt
is_independence_wave_ready_package_iw_006_tag_available = {
	is_independence_wave_exact_package_iw_006_tag_available = yes
}

is_independence_wave_ready_package_iw_007_tag_available = {
	is_independence_wave_exact_package_iw_007_tag_available = yes
}
```

This retains the immutable original-tag, absent-country, reservation, and
origin-system proof in the wrapper. Do not replace either wrapper with
`always = yes`, and do not add a dormant country-history readiness flag. The
stale comment at current lines 85-88, which says FORM-03 is uncertified, must
be reconciled in the same edit; that is comment maintenance, not a fourth
functional gate.

### 2. Add IW-006 and IW-007 to runtime content attestation

File:
`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`

The resulting attestation OR should be:

```txt
has_independence_wave_runtime_package_content_attestation_for_execution_id = {
	OR = {
		check_variable = { independence_wave_execution_package_id = constant:independence_wave_package_id.iw_006 }
		check_variable = { independence_wave_execution_package_id = constant:independence_wave_package_id.iw_007 }
		check_variable = { independence_wave_execution_package_id = constant:independence_wave_package_id.iw_009 }
	}
}
```

The existing runtime preflight already combines this attestation with
`exists = no`, the package adapter, Event 005/006 origin exclusions, and exact
ID-to-original-tag identity at current lines 37-73.

### 3. Add the two exact SCN-008 preflight branches

File:
`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`

The resulting scenario-preflight OR should be:

```txt
is_independence_wave_scenario_package_preflight_ready = {
	OR = {
		AND = {
			check_variable = { independence_wave_scenario_dispatch_package_id = constant:independence_wave_package_id.iw_006 }
			is_independence_wave_exact_package_iw_006_tag_available = yes
		}
		AND = {
			check_variable = { independence_wave_scenario_dispatch_package_id = constant:independence_wave_package_id.iw_007 }
			is_independence_wave_exact_package_iw_007_tag_available = yes
		}
		AND = {
			check_variable = { independence_wave_scenario_dispatch_package_id = constant:independence_wave_package_id.iw_009 }
			is_independence_wave_exact_package_iw_009_tag_available = yes
		}
	}
}
```

The scenario OR is itself the compile-time content attestation, matching the
existing IW-009 precedent. Its exact trigger supplies the live absence,
reservation, active-origin, and original-tag checks. The shared scenario
reservation API supplies anchor, host, uniqueness, and host-remnant checks.

No other gameplay, readiness, history, scenario, or fallback change is
authorized by this report.

## Audit basis

The audit used the repository requirements and the following skills as its
workflow authority:

- `chaos-redux-events`
- `chaos-redux-subagents`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`

The required offline wiki references were consulted before source inspection:
Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On
actions, Event modding, Decision modding, Idea modding, and AI modding. The
relevant country, national-focus, division/unit, and portrait/interface pages
were also consulted. No Paradox wiki web page was used.

Vanilla documentation consulted included
`documentation/script_concept_documentation.md`,
`documentation/effects_documentation.md`,
`documentation/triggers_documentation.md`, and
`common/script_constants/documentation.md`. Vanilla state history, country
release/fixed-tag behavior, focus loading, the Netherlands/Benelux formable
lane, and comparable focus/decision structures were used as precedents. The
approved reference-mod tag registries were checked where relevant.

The HOI4 MCP domain tools were not exposed in this subagent session, so this
report does not claim an MCP render, rewrite, or runtime result. Direct source,
official documentation, vanilla precedent, manifests, and existing audit
evidence were sufficient for this bounded static readiness decision.

## Package identity and map anchors

- `common/country_tags/006_independence_wave_countries.txt:16-17` registers
  exactly `AFX` and `AGX` to their Chaos Redux country-definition files.
- The current Chaos Redux tree, vanilla tag registry, and the three approved
  reference mods contain no competing AFX or AGX country-tag definition. The
  earlier full installed-mod registry audit recorded zero incompatible
  collisions across its 122 discovered mod roots; this audit independently
  reconfirmed the current repository, vanilla, and approved-reference scope.
- `history/countries/AFX - Wallonia.txt` and
  `history/countries/AGX - Frisia.txt` are dormant package histories with
  baseline laws and character recruitment only. They do not grant a gameplay
  readiness flag that could bypass the static registry.
- Vanilla state 34 resolves to BEL ownership/core history, and vanilla state
  36 resolves to HOL ownership/core history. No Chaos Redux state-history
  override for state 34 or 36 was found.
- `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:69-92`
  loads IW-006 as AFX / state 34 / reservation group RG-34 / regional
  industrial breakaway, and IW-007 as AGX / state 36 / reservation group
  RG-36 / standard port-or-island package.
- The corresponding publishers at lines 273-287 reserve only the mandatory
  anchor state. Neither package publishes compact or extended optional states.

The exact availability triggers at
`common/scripted_triggers/006_independence_wave_package_triggers.txt:23-37`
and `:60-68` require an absent target tag, no current country reservation, no
same-plan rejection, no Event 005 origin, no Event 006 active origin, and the
correct immutable original tag. A living AFX or AGX therefore fails closed;
the allocator never overwrites or repurposes it.

## Automatic Event 006 path

The automatic route is structurally ready after gates 1 and 2:

1. `common/scripted_triggers/006_independence_wave_triggers.txt:349-367`
   supplies distinct IW-006 and IW-007 runtime readiness functions. Each sets
   the exact package ID, enters the exact target country, checks exact identity,
   checks the static readiness wrapper, checks runtime package preflight, and
   checks its exact anchor's availability.
2. `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:194-200`
   gives each row a calculated weight only when its readiness function passes.
   Lines 333-344 include both rows in the ordinary regional weighted draw.
3. The publishers at lines 273-287 use the shared begin/reserve/finish API.
   Failed country, anchor, reservation-group, or host checks record rejection;
   the automatic allocator recomputes viable weights and rerolls rather than
   substituting territory or bypassing the failure.
4. `common/scripted_triggers/006_independence_wave_triggers.txt:521-575`
   contains exact Liberations capacity witnesses for both packages, including
   package count, earliest band, exact runtime readiness, country uniqueness,
   anchor uniqueness, reservation-group uniqueness, Event 005 exclusions, and
   host eligibility.
5. The final cluster capacity proof at lines 633-665 requires the exact target
   count, aligned package/country/anchor/group arrays, and another owned state
   for every prospective anchor owner.

There is no alternate AFX/AGX fallback row. If either tag is living, its anchor
is unavailable, its host cannot survive the planned loss, or an Event 005
reservation conflicts, that package receives zero effective availability and
the allocator continues with another independently ready package.

## SCN-008 path: every valid type and intensity

SCN-008 is structurally ready after gate 3:

- `common/scripted_effects/006_independence_wave_scenario_effects.txt:191`
  registers IW-006 once, and line 206 registers IW-007 once, in the deterministic
  ranked package registry.
- Lines 303-374 dynamically dispatch the exact package loader and reservation
  publisher from the numeric package ID. The two underlying publishers remain
  the same anchor-only publishers used by the automatic path.
- Lines 376-413 attempt every ranked row. A missing or failing preflight is
  recorded as `package_unready`; a reservation failure is recorded by the
  shared reservation API. Neither condition admits a partial country.
- Lines 415-462 set the scenario target and expected country count to the
  number actually selected only after every bound row has been attempted, then
  require aligned metadata and successful optional expansion. Thus a blocked
  AFX or AGX row is omitted cleanly without corrupting other scenario rows.
- `common/scripted_triggers/006_independence_wave_scenario_triggers.txt:9-17`
  accepts the six scenario types: Sovereign Scatter, Common Congress, Wars of
  Separation, Universal Belligerence, Patron Worlds, and Great Partition.
  Lines 28-34 accept Low, Medium, High, and Maximum intensity.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt:96-157`
  maps all four intensities into the common wave tuning. Great Partition may
  advance the requested territory tier, but IW-006 and IW-007 expose no
  optional states, so their frozen footprint remains exactly state 34 or 36.
- Lines 505-582 apply the selected type to each committed release; lines
  976-995 apply the shared post-commit type operation. All six types and all
  four intensities therefore use the same preflight, reservation, host, lock,
  execution, and package-finalization safety chain. No type or intensity has a
  bypass specific to AFX or AGX.

This establishes static coverage for all 24 valid type/intensity combinations
per package. It does not claim that those 48 combinations were executed in
game.

## Host-survival proof

**Verdict: PASS.** The proof is dynamic and does not depend on BEL or HOL
remaining in their vanilla borders.

- The scenario and automatic publishers identify the live owner of state 34
  or 36 as the candidate host.
- `common/scripted_effects/chaosx_liberation_release_effects.txt:205-227`
  computes the host's loss ceiling as `num_owned_states - 1`; the next state
  cannot be reserved when planned loss reaches that ceiling.
- Lines 233-354 choose a protected host state outside the anchor/reserved
  footprint, prioritizing the live capital, then controlled core/state and
  other viable owned territory. Host snapshots preserve the protected state
  and original capital before lock.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt:248-300`
  repeats the N-1 measurement before the mandatory anchor is admitted. Optional
  territory is trimmed before an otherwise viable country would be dropped.
- `common/scripted_effects/chaosx_liberation_release_effects.txt:1160-1220`
  recomputes the live and frozen host-loss proof before execution. The global
  plan is not lockable unless its country, state, set, and host proofs agree.
- `common/scripted_triggers/chaosx_liberation_release_triggers.txt:248-263`
  requires every frozen state to be owned and controlled by its target after
  transfer, while every former host still exists and owns its protected state.
- Capital relocation/restoration runs around the transfer, preventing an
  anchor capital from being stranded in the released footprint.

Vanilla BEL and HOL each provide a simple multi-state baseline witness, but
that baseline is not treated as the safety proof. If war, annexation, another
package, or a future map change leaves the live anchor owner without a safe
remnant, the shared N-1 checks reject the package before lock.

## Event 005 / Event 006 collision proof

**Verdict: PASS.** IW-006 and IW-007 are safe in the shared Liberations path,
including the case where the two events are scheduled together.

- Event 005's opening country registry is the fixed Soviet-republic set in
  `common/scripted_triggers/006_independence_wave_triggers.txt:395-412` and
  `common/scripted_effects/005_006_liberations_collision_effects.txt:69-133`.
  AFX and AGX are not Event 005 tags, and package IDs 6 and 7 do not collide
  with Event 005's joint package-ID namespace.
- Current state 34 and state 36 are not cores of any Event 005 opening
  republic. BEL and HOL do not own or control such a core in the inspected
  baseline. More importantly, the capacity witness at
  `common/scripted_triggers/006_independence_wave_triggers.txt:387-433`
  rejects any future target tag, anchor, or anchor owner that could collide
  with Event 005's live opening footprint.
- Event 005 candidate construction uses the same state/country reservation
  API and explicitly excludes Event 006 active origins. Event 006 exact
  availability reciprocally excludes Event 005 active origins.
- In the joint transaction,
  `common/scripted_effects/005_006_liberations_collision_effects.txt:1237-1270`
  begins one shared plan, freezes Event 005 first, then runs the Event 006
  automatic allocator against that frozen footprint. Lines 1272-1298 expand
  optional territory only after both mandatory selections and take one shared
  lock only when both contributions and exact counts pass.
- Lines 1300-1359 validate both metadata sets, protect host capitals,
  instantiate both country sets, transfer both frozen state sets, and require
  exact transfer counts plus frozen ownership before finalization.
- Lines 1361-1413 require Event 005 initialization and Event 006 package setup
  to validate before committing the shared plan. Lines 1416-1444 cancel before
  ownership mutation or run the defined compensating failure path after
  execution begins. Finalization failure is deliberately terminal after the
  package finalizer barrier; the prepared/complete proofs reviewed below are
  what make promoting AFX/AGX into that barrier safe.

The joint route therefore has no race in which AFX/AGX can seize an Event 005
reservation, erase a living tag, or leave BEL/HOL without a remnant. A
conflicting package is rejected or rerolled before mutation; it is not replaced
by a fallback footprint.

## Exact release footprint and transaction safety

`common/scripted_effects/006_independence_wave_execution_effects.txt:153-244`
masks every unplanned historical core from the fixed target tag, adds cores
only to the frozen package states, releases the absent tag from the frozen
former host, restores masked historical cores, and counts successful
instantiation. State transfer then iterates the frozen aligned arrays rather
than every historical core. This prevents a dormant registered tag from
claiming territory outside its accepted package.

The standalone Event 006 executor locks and validates before execution, then
runs four package passes: prepare target origins, run package setup, activate
the origin, and validate complete setup before the final initialized count can
match. The joint executor uses the same Event 006 package passes inside the
shared Event 005/006 transaction. The package dispatcher already registers
IW-006 and IW-007 for setup, final validation, and cleanup.

## Wallonia and Frisia package-content proof

### Setup, validation, and cleanup

- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:20-64`
  validates exact package ID, region, depth, archetype, owned/controlled
  anchor, former host, capital, laws, and exact character roster for each
  package.
- Prepared proofs at lines 155-269 require the full shared framework, exact
  route allow/deny set, former-host routes, power struggle, the FORM-03 family
  and selected-carrier mapping, FORM-03 readiness, ambition, exact force
  mapping and application, AI enablement, lifecycle idea, and exact capital.
- Complete proofs after line 274 additionally require setup flags, activation
  arrays, active-origin registration, and network membership.
- `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:356-449`
  performs the exact IW-006 and IW-007 setup. Lines 455-493 dispatch and
  validate the package. Lines 499-589 remove package missions, decisions,
  ideas, variables, FORM-03 state, and package flags during cleanup.

### Focus, decisions, ideas, force package, and AI

- Full-framework packages load the shared `independence_wave_focus_tree`
  through `common/scripted_effects/006_independence_wave_focus_effects.txt:29-56`.
  AFX and AGX are absent dormant tags before release, so this does not overwrite
  a living country's focus tree. Their route gates, rewards, AI factors, and
  FORM-03 post-charter progression are present in the shared focus source.
- The Wallonia/Frisia decision and idea files contain distinct industrial and
  maritime project lanes, route governments, crises, former-host relations,
  regional-conference behavior, costs, cancellation behavior, and AI weights.
  Their categories and scripted triggers are wired to the exact package state.
- `common/script_constants/006_independence_wave_force_package_constants.txt`
  maps IW-006 to the industrial-security profile and IW-007 to the
  coastal-maritime profile, with distinct tradition and reinforcement masks.
  Both use the non-inheritance lane. The prepared proofs require the exact
  mapping and a successful force application, so a missing or mismatched force
  package cannot pass finalization.
- `common/ai_strategy/006_independence_wave_wallonia_frisia.txt` enables each
  strategy only for the exact active package flag, aborts when that condition
  stops being true, scopes former-host behavior dynamically, and supplies
  survival, restraint, civic, industrial, or maritime priorities appropriate
  to the package.

### Localisation and visual assets

- Country names, adjectives, and ideology variants exist for AFX and AGX.
  Package names, characters, parties, ideas, categories, decisions, tooltips,
  routes, and FORM-03 progression are localised. A read-only exact-key
  cross-check built from the two package gameplay surfaces expected 95
  player-facing keys and found all 95.
- AFX and AGX each have normal, medium, and small flag textures. Their current
  files match the package manifest's authoritative ladders.
- Both country leaders and both commanders have wired large portraits; both
  commanders have separate army-small portraits. Sprite declarations at
  `interface/006_independence_wave_region_01_portraits.gfx:10-32` match the
  character consumers.
- Current portrait files match
  `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/portrait_package_hashes.sha256`;
  the commander-small files match the authoritative correction inventory under
  `army_small_dossier_correction_2026_07_15/`. The historical
  `generated_nwe_hashes.sha256` ledger is explicitly superseded for these
  portraits by `docs/assets/006_independence_wave/manifest.md:255-302` and is
  not a readiness blocker.

No placeholder, missing sprite handoff, missing portrait consumer, or visual
fallback was found for AFX or AGX.

## FORM-03 dependency re-audit

The former package blocker has been removed in current source:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form03_promotion_reaudit_2026_07_16.md`
  records a PASS for the restored FORM-03 bundle. This audit independently
  traced the current FORM-03 effects, triggers, decisions, ideas, focus
  progression, cleanup, localisation, and visual registration used by AFX and
  AGX.
- The Wallonia/Frisia setup calls the FORM-03 readiness adapter, and its
  prepared proof requires FORM-03 readiness before package setup can validate.
  Cleanup calls the FORM-03 cleanup adapter.
- The restored FORM-03 path supplies the complete generic formable identity and
  integration attestation set plus its readiness/progression proof. Its
  decision, idea, state-modifier, focus, report-scene, and icon assets are wired.
- LCX is a cosmetic carrier identity for the accepted AFX/AGX formable lane;
  BEL, HOL, and LUX remain sovereign identities. FORM-03 does not transfer or
  core the neighboring states 6, 7, 8, 35, 977, or 980. The package may act
  only through its selected AFX or AGX carrier and the already-frozen anchor.

The earlier FORM-03 audit and package handoff remain useful historical evidence
for why readiness was withdrawn, but their old blocker statement is superseded
by the 2026-07-16 promotion re-audit and the restored current sources.

## Blockers, simplifications, and runtime boundary

### Current checked-in blocker

The only current release blocker found is the intentional three-part
compile-time gate closure:

1. IW-006 and IW-007 readiness wrappers still return `always = no`.
2. Runtime package-content attestation still admits only IW-009.
3. Scenario package preflight still admits only IW-009.

Those are coordinated admission controls, not missing package content. The
exact replacement bodies are authorized above.

### After the authorized gate change

No remaining static gameplay, tag, state, host-survival, Event 005 collision,
FORM-03, focus, decision, idea, force-package, AI, localisation, or asset
blocker was found for IW-006 or IW-007.

### Runtime boundary

This is static source proof, not runtime execution. It does not demonstrate a
particular random draw, every dynamic world-state permutation, all 48 SCN-008
type/intensity package combinations in a live game, or an actual joint
Event 005/Event 006 commit. The scripts retain fail-closed runtime checks for
exactly those dynamic facts. A later live failure would be a defect to
investigate, not evidence that a fallback is permitted.

### Simplifications and fallbacks

No simplification, omitted requested surface, placeholder, or fallback was
used in this audit. No gameplay, readiness, documentation, asset, or source
file was edited other than this evidence report. No skill was created or
updated, and no commit was made.
