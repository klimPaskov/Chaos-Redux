# IW-043 / IW-058 scripted architecture handoff — 2026-07-18

Owner: `chaosx_scripted_system_architect` subagent

## Documentation reconciliation note (2026-07-18)

The helper-map and cleanup evidence below is retained, but its FORM adapter
section records the earlier pre-promotion state. The current exact CHU/ASY
signature tranche has operational FORM-12/13/18 transactions and setup
attestations, including paid 180-day congress ledgers, consent/anchor
recounts, staged sovereignty-preserving integration, and sole signature-proof
writers. Do not use the historical “unwritten” wording below to infer a
current hold; wider Event 006 families remain separately fail-closed.

## Scope completed

This handoff covers the bounded reusable scripted layer for the Middle Volga (IW-043) and Assyria (IW-058) packages. It does not change the protected BAY/RHI portrait surfaces, add advisor assets, rewrite the country pools, or commit a branch.

### Files changed

- `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`
- `docs/events/006_independence_wave/systems/iw043_iw058_signature_packages.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw043_iw058_scripted_architecture_handoff_2026_07_18.md`

The existing package constants file was inspected and remains the single tuning source; no new numeric threshold was needed for relationship reach.

## Helper map

### Target-scope reach triggers

All are evaluated in candidate-country scope with the active package country as `ROOT`; every tier rechecks the matching package identity on `ROOT`, and none iterates over the world.

| Helper | Input scope | Output | Contract |
|---|---|---|---|
| `is_independence_wave_iw043_reachable_partner` | target country | boolean | exact IW-043 root, non-self, non-war, non-subject, any IW-043 tier |
| `is_independence_wave_iw058_reachable_partner` | target country | boolean | exact IW-058 root, non-self, non-war, non-subject, any IW-058 tier |
| `is_independence_wave_iw0xx_major_reach` | target country | boolean | target is a major and not at war with ROOT |
| `is_independence_wave_iw0xx_treaty_reach` | target country | boolean | non-aggression pact or guarantee in either direction; no subject relation |
| `is_independence_wave_iw0xx_league_reach` | target country | boolean | active Event 006 country with league or network membership |
| `is_independence_wave_iw0xx_patron_reach` | target country | boolean | delegates the existing validated patron-target contract |
| `is_independence_wave_iw0xx_diaspora_reach` | target country | boolean | active same-region Event 006 network member |

`iw0xx` means the explicit `iw043` and `iw058` variants. These helpers are intended for `target_trigger` and AI-weight call sites owned by the decision lane.

### Force binding and designation triggers

| Helper | Input scope | Output / side effects |
|---|---|---|
| `has_independence_wave_iw043_supplied_division_candidate` / IW-058 equivalent | country | proves current generation receipt plus one owned, non-reserve division above package strength and organization floors |
| `can_bind_independence_wave_iw043_force_package` / IW-058 equivalent | country | admission gate; rejects overlapping flags or a stale global pointer |
| `independence_wave_bind_iw043_force_package` / IW-058 equivalent | country then selected division | saves the exact selected division as a global target and records country generation |
| `has_valid_independence_wave_iw043_force_binding` / IW-058 equivalent | country + global target | validates the live target's pre-conversion composition and current generation |
| `independence_wave_commit_iw043_force_discipline` / IW-058 equivalent | country + global target | mutates the selected division in place, sets organization, and writes division/country designation receipts |
| `has_independence_wave_iw043_designated_formation` / IW-058 equivalent | country | durable post-conversion proof: designation flag, current-generation variable, and final named template |
| `has_valid_independence_wave_iw043_designated_formation_binding` / IW-058 equivalent | country + global target | designated proof plus division-scoped generation receipt while the pointer is live |
| `independence_wave_release_iw043_force_package` / IW-058 equivalent | country | clears division receipt first, then global pointer, bound generation, and active-binding flag |

Final player-facing template names are `Middle Volga River Guard` and `Assyrian Levies Detachment`. No unit is created by the discipline effects.

## Constants and tuning table

The package categories in `common/script_constants/006_independence_wave_iw043_iw058_constants.txt` remain authoritative for:

- strength and organization admission floors;
- discipline organization and commander-XP values;
- package route thresholds, mission durations, and transaction costs;
- FORM adapter state values (`unattested`, `staged`, `attested`) and transaction serials.

Reach tiers are structural bilateral contracts (major status, NAG/guarantee, Event 006 league/network membership, validated patron target, or same-region network membership), so no untracked opinion or distance magic number was introduced.

## Event-target and cleanup lifecycle

The two force targets are global because the same formation must survive across timed mission phases. They are named `independence_wave_iw043_bound_force_division` and `independence_wave_iw058_bound_force_division`. Bind preflight, release, and package cleanup clear them explicitly. Before each pointer is cleared, the target division's designation-generation variable is removed. Cleanup then clears bound-generation variables, durable designation-generation variables, designation flags, template-ready flags, force receipts, and package state. The named templates themselves are retained so an already-converted fielded division is not deleted during package cleanup.

IW-058 guardianship restoration uses `independence_wave_restore_iw058_preserved_civilian_cosmetic_identity`; it prefers the church or civic applied/route receipt and otherwise restores the opening national-council identity. Guardianship's cosmetic receipt is removed without changing route ownership.

## FORM-12/13/18 adapter evidence

The three adapters are fail-closed, not operational:

- `has_independence_wave_form12_readiness` requires `independence_wave_form12_adapter_attested`.
- `has_independence_wave_form13_readiness` requires `independence_wave_form13_adapter_attested`.
- `has_independence_wave_form18_readiness` requires `independence_wave_form18_adapter_attested`.

The keyed identity/integration effects only set their receipt flags inside those readiness gates. The achievement-writer hooks do not set attestation. No owned call site writes any of the three attestation flags, so the adapters cannot commit. The IW-058 integration result now references the declared `independence_wave_iw_formable_adapter.attested` constant; this fixes a category typo without opening the readiness gate.

## References and validation

Consulted before editing:

- Offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, divisions, and units under `paradox_wiki/`.
- Vanilla documentation for effects/triggers, script constants, and script concepts under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.
- Vanilla `change_division_template` call sites in Sweden, Switzerland, and Norway. The current vanilla source uses the block payload `change_division_template = { division_template = "..." }`, which is retained here even though the generated effect documentation also shows a shorthand string.

Task-specific checks performed:

- Confirmed the old working template labels are absent from the owned scripted files and the final names are used by definition, conversion, and trigger checks.
- Confirmed every new global target has a release clear and a cleanup clear; release clears the division-scoped receipt before the target.
- Confirmed the designated triggers no longer depend on pre-conversion composition and are generation-gated.
- Confirmed all new reach predicates are target-local and contain no `any_country`/world iteration.
- Confirmed at handoff time that the FORM-12/13/18 adapter flags were
  unwritten in the owned effects and therefore failed closed; the later exact
  CHU/ASY setup pass supplies the admitted-carrier attestations recorded in the
  reconciliation note above.

The read-only `hoi4.event_inspect` request was attempted against `events/006_independence_wave_iw043_iw058.txt` with a bounded scan, but the MCP call did not return an artifact within the available wait window. No artifact reference is therefore claimed; direct source inspection of the linked event and decision call sites is the authoritative evidence for this handoff.

## Known limitations and follow-up

- Decision/AI owners must migrate bounded target pools to the public reach wrappers; this handoff does not edit their files.
- The durable designation receipt proves that the package conversion effect succeeded and that the named country template exists. The stronger `has_valid_*_designated_formation_binding` proof is available only while the short-lived division target remains live.
- FORM-12/13/18 compatibility remains intentionally blocked pending an exact keyed vanilla/Event 006 promotion contract.
- No advisor, portrait, icon, sprite, or other visual asset was created or rewired in this architecture pass.
- The canonical 150-tag decision-pool shape is outside this owned scripted layer and remains with the decision owner.
