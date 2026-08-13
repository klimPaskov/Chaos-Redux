# Event 006 RHI and BAY Level 2 focus implementation handoff

Date: 2026-07-16

Owner: `rhi_bay_focus_impl`

Scope: `IW-008` Rhineland (`RHI`) and `IW-009` Bavaria (`BAY`)

Mode: parent-authorized bounded gameplay patch, no Git staging or commit

## Outcome

The shared full Event 006 focus tree now contains an exact-package Level 2 focus group for each package:

- Rhineland has eight country-specific focuses and completes seven in a single route.
- Bavaria has eight country-specific focuses and completes six in a single route.
- Every focus has final English name, description, effect tooltip, duration, icon, search filters, exact package gate, guarded scripted reward, and state-aware AI weight.
- Every new focus helper is idempotent and every new focus state flag is cleared by the package cleanup adapter.
- No package idea, free unit, equipment loop, claim, core, country identity, package attestation, admission gate, scenario gate, or dispatch gate was added.
- The parent integration assigns a distinct package-specific focus icon to every node. No asset fallback or placeholder is present.

The parent confirmed that the accepted package mapping is `IW-008/RHI` and `IW-009/BAY`. The earlier task label that called them `IW-009/RHI` and `IW-010/BAY` was erroneous. No package ID was migrated.

## Files changed

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_rhineland_bavaria_constants.txt`
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt`
- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`
- `docs/events/006_independence_wave/northern_western_europe_packages.md`
- this handoff

The parent-owned `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt` was not edited by this subagent. It was already dirty from the parent transaction-repair tranche.

The shared focus constants and shared Event 006 idea files were not edited. The only new tuning fields are the package-specific negative Stability and War Support tradeoffs under `independence_wave_rhine_bavaria_focus`.

## Rhineland branch

### Graph

1. `independence_wave_rhi_establish_corridor_authority_focus`
2. Parallel children:
   - `independence_wave_rhi_unify_rail_dispatch_focus`
   - `independence_wave_rhi_arm_customs_guard_focus`
3. AND convergence:
   - `independence_wave_rhi_secure_industrial_belt_focus`
4. Mutually exclusive diplomacy:
   - `independence_wave_rhi_ratify_host_transit_compact_focus`
   - `independence_wave_rhi_proclaim_neutral_corridor_focus`
5. OR convergence after either diplomatic choice:
   - `independence_wave_rhi_charter_network_transit_office_focus`
6. `FORM-04` capstone marker:
   - `independence_wave_rhi_authorize_form04_delegation_focus`

The branch occupies authored columns 89 through 91 and rows 1 through 6. Its root is gated by `allow_branch = { is_independence_wave_rhi_package = yes }`, and every focus also requires the exact package trigger in `available`.

The package-owned Rhine Congress is deliberately separate from the shared
`FORM-04` preparation transaction. It can settle RHI's internal corridor
mandate, schedule the third country incident, and unlock the delegation focus
without a living AJX. The shared formation congress remains responsible for
the later two-founder invitation, consent, adjacency, territory, and carrier
delegation proofs; no package action bypasses those mutation gates.

### Rewards and tradeoffs

- The authority root, rail dispatch, customs guard, and industrial belt each grant 10 Corridor Authority. From the package opening value of 25, completing those four focuses reaches the stable threshold of 65 exactly.
- Rail dispatch adds one Infrastructure and one 50 percent Industry research bonus.
- The customs guard grants 15 Army Experience and 15 Command Power.
- The industrial belt adds one Civilian Factory and one matching state slot to the package anchor.
- The host transit compact grants 10 Corridor Authority, settles the former-host bilateral ledgers, improves legitimacy, recognition, and capacity, and trades away 5 security and 5 percent War Support.
- Neutral-corridor diplomacy grants 10 Corridor Authority, 5 percent Stability, and 10 security while trading away 5 recognition.
- The network office requires active network membership and grants 5 Corridor Authority plus network, league, recognition, and capacity progress.
- The Rhine Federation delegation requires the exact Rhine Federation family, the RHI `FORM-04` carrier marker, and a completed package Rhine Congress. It grants 5 Corridor Authority, sets `independence_wave_rhi_form04_delegation_ready`, opens formable discovery, and advances network and ambition ledgers.

At base focus speed, the four-focus authority sequence uses 26 authored cost points, or 182 days. It solves the 420-day Corridor Authority crisis through focus opportunity cost rather than Political Power storage or a passive checklist.

## Bavaria branch

### Graph

1. `independence_wave_bay_broker_civic_settlement_focus`
2. Parallel children:
   - `independence_wave_bay_reconcile_landesbank_accounts_focus`
   - `independence_wave_bay_bind_rail_and_pass_authorities_focus`
3. Mutually exclusive institutional settlement after an AND convergence:
   - `independence_wave_bay_seat_landtag_and_court_focus`
   - `independence_wave_bay_entrust_mountain_guardians_focus`
4. OR convergence after either institutional settlement:
   - `independence_wave_bay_open_alpine_network_office_focus`
5. Mutually exclusive diplomatic capstones:
   - `independence_wave_bay_convene_south_german_settlement_focus`
   - `independence_wave_bay_ratify_german_host_compact_focus`

The branch occupies authored columns 95 through 97 and rows 1 through 5. Its root is gated by `allow_branch = { is_independence_wave_bay_package = yes }`, and every focus also requires the exact package trigger in `available`.

### Rewards and tradeoffs

- The civic root grants 10 Civic Settlement and 5 Mountain Security.
- Landesbank reconciliation grants 15 Civic Settlement, one Civilian Factory and matching state slot, and one 50 percent Industry research bonus.
- The rail and pass authority grants 15 Mountain Security, one Infrastructure, 15 Army Experience, and 15 Command Power.
- The Landtag and court compact grants 15 Civic Settlement and 5 percent Stability at a cost of 10 Mountain Security and 5 percent War Support.
- The guardians mandate grants 15 Mountain Security and 5 percent War Support at a cost of 10 Civic Settlement and 5 percent Stability.
- The Alpine Network Office requires active network membership and grants 5 to both package values plus network and diplomatic progress.
- The South German capstone requires the completed South German estates settlement and grants 10 to both package values plus network and ambition progress. It grants no German claims and creates no competing identity.
- The host-compact capstone requires a living former host, the package's no-competing-claim state, and no selected South German policy. It grants 10 Civic Settlement, 5 Mountain Security, settles the bilateral host ledgers, and advances public and diplomatic settlement.

The focus branch deliberately does not solve both Bavarian crisis values by itself. Starting from 25 Civic Settlement and 30 Mountain Security:

- after the common root and parallel projects the package stands at 50 and 50;
- the Landtag path reaches 80 and 55 after the South German capstone, or 80 and 50 after the host compact;
- the guardians path reaches 55 and 80 after the South German capstone, or 55 and 75 after the host compact.

Each institutional route therefore needs at least one appropriate package crisis project to cross both stable thresholds of 60. This keeps the existing decision family relevant and makes the civic-versus-security tradeoff concrete.

## No-competing-German-claim correction

Parent review identified a pre-existing setup assertion, `independence_wave_bay_german_reunification_preserved`, that exposed a pan-German decision and dead-ended both accepted capstones.

Within the parent-authorized package-effect and prepared-proof surfaces:

- setup now sets `independence_wave_bay_no_competing_german_claim`;
- setup clears stale `independence_wave_bay_german_reunification_choice` and `independence_wave_bay_german_reunification_preserved`;
- the prepared package proof requires the new no-competing-claim flag and proves both old claim flags absent;
- the German host compact requires the new closed state; and
- cleanup clears the replacement flag and the stale legacy flags.

At handoff time the parent still owned retirement of `independence_wave_bay_keep_german_reunification_claim`; the parent integration review below records its completed removal.

## AI behavior

- Both roots receive urgent preference while their package crisis remains unsettled.
- RHI prioritizes customs security under severe former-host threat, prefers the host compact when threat is not severe, and strongly prefers guarded neutrality when the former host is threatening or absent.
- BAY prioritizes Landesbank work below its Civic Settlement threshold and rail/pass work below its Mountain Security threshold.
- BAY prefers the Landtag and court compact under constitutional or traditional government and prefers the guardians under emergency government or severe former-host threat.
- Network and capstone focuses remain gated by the same player-facing campaign state used by their rewards. Invalid routes cannot be selected.

## Icons and assets

The parent integration replaces the initial shared-icon wiring with sixteen distinct `94x86` focus icons under `gfx/interface/goals/006_independence_wave/rhineland_bavaria/`. Their normal and shine sprites are registered in `interface/006_independence_wave_rhineland_bavaria_assets.gfx`, and each focus consumes the sprite whose stem matches its focus ID. The same package supplies eight distinct route-idea icons and two country-incident report scenes. Source masters, exact prompts, processed PNGs, contact sheets, validation, hashes, manifest, and sprite handoff are kept under `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/`.

## Validation evidence

### Static focus graph

- 16 new focus IDs were found, with no duplicate tree ID.
- All 21 prerequisite edges resolve to existing focus IDs and every prerequisite parent has a lower authored row than its child.
- The three intended AND convergence nodes are RHI industrial security and the two BAY institutional choices.
- The two intended OR convergence nodes are the RHI transit office and BAY Alpine Network Office.
- All three mutual-exclusion pairs are reciprocal.
- Both branch roots and only those roots contain the exact package `allow_branch` gate.
- All 16 focuses contain an exact package `available` gate, an authored duration, AI behavior, a registered icon, one custom tooltip, and one package reward helper.
- None of the 16 authored positions collides with another focus in the current shared tree.

### Reward and cleanup contracts

- All 16 reward helpers have the exact package guard, a completion-flag repeat guard, and one completion flag setter.
- Every one of the 16 completion flags has exactly one package cleanup clearer.
- The new reward helpers contain no free-unit, OOB, stockpile, identity, claim, core, admission, or package-readiness mutation.
- New reward values use script constants. The focus-helper section contains no raw numeric gameplay assignment.
- The prepared BAY proof now requires the neutral no-competing-claim state and proves both rejected claim flags absent.

### Localisation and icon resolution

- Each of the 16 focuses has exactly one English title, description, and custom-effect tooltip.
- The package localisation remains UTF-8 with BOM and contains no legacy `:0` keys.
- The new player-facing text contains no em dash or semicolon.
- Every referenced focus icon is registered and its DDS file exists.

### Vanilla precedent

- Vanilla `baltic_shared.txt` was used for the conditional `allow_branch` pattern.
- Vanilla `belgium.txt` was used for one-block OR prerequisites, reciprocal mutual exclusion, and state slot plus building rewards.
- Official `effects_documentation.md` was checked for the country/state scopes of Stability, War Support, Command Power, Army Experience, technology bonuses, building construction, state slots, variables, and country flags.

### HOI4 MCP result

Both required read-only calls were attempted against `independence_wave_focus_tree`:

- `hoi4.focus_inspect`
- `hoi4.focus_render` at review scale 0.25

Both stopped before scanning the file with the exact result:

- code: `ARTIFACT_STORAGE_LIMIT`
- message: `Artifact storage retention limit has been reached`
- workspace: `mod_chaos_redux_ea3b2d67c2c0`

No MCP artifact is claimed. The bounded static graph, reference, layout, localisation, icon, helper, cleanup, and balance checks above compensate for the unavailable artifact pass.

## Integration boundary and remaining risk

`independence_wave_rhi_form04_delegation_ready` is now produced and cleaned by the RHI branch, but the current shared `has_independence_wave_form04_strict_mutation_preconditions` does not yet consume carrier-specific delegation readiness. The parent must require the RHI marker for an RHI carrier and the existing AJX marker for an AJX carrier before this capstone becomes a binding `FORM-04` gate. Until that parent-owned trigger patch lands, the focus records readiness and opens discovery but does not itself authorize formation.

The parent must also finish retiring the rejected BAY pan-German decision in the decision-owned transaction patch. The package setup and prepared proof are already fail-closed against that rejected state.

No admission-readiness or overall Event 006 completion claim is made here. The branch implementation does not alter automatic allocation, SCN-008 preflight, content attestation, or `FORM-04` readiness certification.

## Parent integration review

The parent completed the two bounded integrations identified by this handoff:

- `has_independence_wave_form04_strict_mutation_preconditions` now requires `independence_wave_rhi_form04_delegation_ready` for an RHI carrier or `independence_wave_ajx_form04_delegation_ready` for an AJX carrier;
- the rejected Bavarian pan-German decision and its player-facing localisation were retired, Event 006 Bavaria closes the vanilla German reunification decision after prepared setup, and cleanup restores it.
- all sixteen package focuses, eight route ideas, and seven country incidents now consume the package-specific visual set registered by `interface/006_independence_wave_rhineland_bavaria_assets.gfx`.

These changes do not grant package attestation. A fresh independent exact-package audit remains required.

## Simplifications, omissions, and blockers

- No focus, route, reward, AI path, localisation entry, or required visual asset was simplified or omitted inside the bounded Level 2 branch scope.
- MCP visual artifacts are blocked by the artifact-retention limit described above.
- Fresh exact-package focus, decision, setup, cleanup, AI, identity, and FORM-04 audit remains required before admission.

## Skills and references used

- `chaos-redux-events`
- `chaos-redux-focus-trees`
- `chaos-redux-decisions-missions`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- required offline Paradox wiki core pages and National Focus Modding
- official vanilla script-concept, script-constant, trigger, effect, modifier, decision, and focus documentation
- installed vanilla Baltic shared-tree and Belgian focus precedents

No skill was created or updated. The new identifiers and balance details are Event 006-specific and do not belong in a reusable repository skill.
