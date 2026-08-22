# Event 019 registry and scenario contract v4 independent re-audit

Date: 2026-07-16  
Mode: live-source read-only specialist audit; the auditor wrote only this handoff  
Gameplay ownership: parent agent  
Contract audited: Chaos unit-family provider contract version 4

## Verdict

The final live snapshot satisfies the requested registry, provider-isolation,
consumer, cleanup, and SCN-013 anomalous-family contract. No open P0, P1, or P2
finding remains in this audit scope.

| Severity | Open count | Result |
| --- | ---: | --- |
| P0 | 0 | No corrupting registry, ownership, derivative, or scenario defect remains. |
| P1 | 0 | All functional contract gaps found during the audit were repaired and re-read in live source. |
| P2 | 0 | The one inert scenario-provider token left after remediation was removed; no stale contract residue remains. |

This is a registry/scenario scope verdict, not a claim that every unrelated
Event 019 feature or approval-gated engine limitation is complete.

The final hashes used to freeze this verdict are:

- sole Event 019 registry effect file: `A576E45CD52B134CED539F7563ECE722799F1EDA1C43F9726B724EE9D2B0863B`;
- Event 19 scenario effects: `C0C89BC9E76047A64849786A28B728B4F20566E525A73B0DE33FF76DA9113C3E`;
- Event 19 registry/derivative trigger file: `942061B9D10F80526AC5D3DFCC37978E9AD8B1A2F8B06850988B51F1625951B5`.

## Contract matrix

| Contract point | Final live evidence | Result |
| --- | --- | --- |
| One dedicated Event 19 registry file | The only dedicated Event 19 registry implementation is `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`. The only other registry-named gameplay files are the shared constants, shared triggers, and shared effects. No split provider registry exists. | Pass |
| Future provider requires no Event 19 edit | `docs/systems/cbrn_warfare/chaos_unit_family_registry.md:7-49` defines one external registration entry, complete callbacks in the provider integration surface, and one existing parent startup call. Runtime consumers iterate aligned rows and meta-dispatch the recorded provider ID. | Pass |
| Contract v4 registrar | `common/scripted_effects/chaos_unit_family_registry_effects.txt:47-181` rejects a non-v4 or visually unsupported registration and treats an existing family ID as idempotent only when every row field matches. | Pass |
| Exact visual ownership | `common/scripted_triggers/chaos_unit_family_registry_triggers.txt:100-165` binds profile 1 to 501/501, 2 to 502/502, and 3 to 503/503. Profile 999 rejects every reserved family or provider ID. Unknown profiles fail. | Pass |
| Generic parent actor blocks creation | `common/scripted_triggers/019_infantry_spawn_triggers.txt:1085-1098` rejects `chaos_unit_family_parent_actor` before all provider-specific parent markers, tags, and original tags. Parent setup paths stamp the generic marker. | Pass |
| Separate positive derivative proofs | `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4262-4295`, `4489-4522`, and `4722-4755` clear both proofs, prove parent isolation, build the public package, and only then prove public-package ownership. `common/scripted_triggers/019_infantry_spawn_triggers.txt:1027-1045` requires both proofs for a nonhuman derivative. | Pass |
| Defeat and final provider cleanup | `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:7083-7130` dispatches and proves defeat cleanup; `7510-7535` does the same after exact formation absence for final teardown. Missing proof fails closed. | Pass |
| Current family composition and training | Constants at `common/script_constants/019_infantry_spawn_constants.txt:2466-2561` and providers at registry lines 4112-4769 expose only base zombies, weak ghosts, and coal golems. Only family 501 is trainable. | Pass |
| No fixed-tag fallback | Natural release uses `create_dynamic_country` with `original_tag = THIS`; SCN uses the same dynamic model or its designed same-tag microstate takeover. No fixed derivative/release tag is present. | Pass |
| No parent/world-end leakage | Audited provider, derivative, and scenario code reads parent/world-end gates but contains no parent setup/evolution/super-event/world-end mutation call. | Pass |
| SCN anomalous contract and microstate safety | SCN selection and takeover lookup use the generic derivative row predicate. Multi-state hosts split dynamically; one-state/all-island hosts use same-tag takeover and never split their only state. The repaired dynamic actor persists and revalidates exact family/provider ownership. | Pass |

## Registry ownership and extension proof

The dedicated-file inventory is exact:

- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt` owns the consolidated ordinary unit registry and the three initial provider integrations;
- `common/scripted_effects/chaos_unit_family_registry_effects.txt` owns the generic registrar;
- `common/scripted_triggers/chaos_unit_family_registry_triggers.txt` owns generic row alignment and visual-ownership predicates;
- `common/script_constants/chaos_unit_family_registry_constants.txt` owns the shared v4 enums and profile 999.

The parent startup calls remain exactly one apiece:

- provider 501 at `common/on_actions/002_zombie_outbreak_on_actions.txt:10`;
- provider 502 at `common/on_actions/010_death_on_actions.txt:10`;
- provider 503 at `common/on_actions/005_soviet_collapse_on_actions.txt:10`.

The three initial providers each define the same nine externally dispatched
callbacks: eligibility, template build, spawn, management evaluation, payment,
refund, sustainment reconciliation, derivative setup, and derivative cleanup.
All nine suffixes have generic meta-dispatch callers. The three additional
`event19_remove_public_additions` effects are provider-private helpers, not a
missing generic callback.

The future-provider rule is executable rather than documentary. Automatic
generation, first reception, Muster, natural release, active derivative
management, cleanup, and scenario paths discover rows through aligned arrays;
static tokens and provider behavior are selected with the recorded provider ID.
The neutral family name and army/host scene require no new Event 19 localisation
or picture-map branch.

## Visual ownership and every Event 19 consumer

Registration-time and row-time guards are both present. The neutral 999 branch
expressly excludes family IDs 501-503 and provider IDs 501-503, so a reserved
provider cannot be rebound to the neutral scene and an external provider cannot
claim a reserved family.

The audited consumers fail closed as follows:

- Automatic generation guards both weighted passes before eligibility dispatch
  in `common/scripted_effects/019_infantry_spawn_core_effects.txt:191-264`.
- Muster view construction guards rows before provider dispatch at
  `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:324-380`.
  Selection reload also checks view-index bounds, registry-index bounds, visual
  ownership, availability, lot policy, and spawning before dispatch at lines
  787-825.
- Natural release selects through the full derivative predicate at
  `common/scripted_effects/019_infantry_spawn_pressure_effects.txt:164-247`.
  Template reconstruction uses the exact frozen registry index, family, provider,
  and full derivative contract at
  `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:2038-2102`.
- Active derivative lookup requires exact stored family/provider and the full
  formation contract at derivative-package lines 5564-5595. Lifecycle cleanup
  has a separate exact lookup at 5600-5630 which deliberately ignores later
  enabled/spawn/lot-policy changes while retaining v4, visual, derivative,
  parent-isolation, and cleanup ownership.
- SCN weighted selection and the second selection pass call the same derivative
  predicate at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:433-532`.
  Same-tag takeover re-resolves the selected family through that predicate at
  lines 1078-1131.

### Delayed first-family reception

The first reception freezes registry index, family, provider, visual profile,
and a monotonic nonce at
`common/scripted_effects/019_infantry_spawn_evolution_effects.txt:1093-1132`.
The pure delayed-row trigger at
`common/scripted_triggers/019_infantry_spawn_triggers.txt:290-385` verifies:

- aligned registry and in-bounds frozen index;
- exact current row family, provider, and visual values;
- minimum family/provider IDs;
- a nonce at or above the configured initial nonce;
- positive cleanup and parent-isolation profiles;
- contract version 4;
- exact 1/501, 2/502, 3/503 binding or non-reserved profile 999.

Dispatch at evolution-effect lines 1134-1179 leaves a no-eligible-row incident
pending for a later country-local retry. Any partial, malformed, or previously
dispatched frozen evidence resolves through the explicit failure outcome. Event
`chaosx.nr19.105` requires the frozen trigger, reloads it immediately, and all
three options revalidate before applying refusal or materializing a provider
package. Scripted picture localisation at
`common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt:345-360`
uses the exact owned bindings; the neutral scene is reachable only through a
valid profile-999 row.

## Parent isolation and public-package proof

The generic parent marker is stamped in all inspected creation/setup surfaces,
including Event 002, Death, cave/KMB, Soviet-collapse KMB, zombie special
projects, and their triggerable-scenario counterparts. The reusable absence
trigger rejects that marker first, then retains provider-specific defensive
checks for `ZZZ`, `DTH`, `KMB`, their original tags, and their progression flags.

Each provider clears both derivative proofs before setup. Parent isolation is
proved before the shared initializer. Public-package proof is set only after the
private package, Event 19 derivative classification, cosmetic identity,
provider commander/council or claimant leadership, starting ideas, focus tree,
and release report exist without identity or ledger failure. Failure clears both
proofs. A nonhuman country cannot satisfy `is_infantry_spawn_derivative_country`
without both receipts.

## Provider cleanup proof and public ownership

Cleanup row resolution is lifecycle-specific, so disabling a family or changing
it to train-only cannot strand an existing derivative. Dispatch clears the proof,
requires the exact family/provider/v4/visual lifecycle row, calls the recorded
provider, and marks a ledger invariant failure if the callback does not prove the
requested phase.

Provider-owned removal coverage is complete:

- 501 removes the zombie command/route ideas and public flags, owned state
  markers, cosmetic identity, and provider leadership. It removes family 501
  from `infantry_spawn_trainable_family_ids` and uses exact template-to-lot
  ledger ownership to set every generated family-501 template back to
  `force_allow_recruiting = no` and locked before proof.
- 502 removes the ghost command/route ideas, public flags and cooldowns, owned
  anchor/population state markers, cosmetic identity, and provider leadership.
- 503 removes the golem command/route ideas, public flags, owned bound-district
  marker, cosmetic identity, and provider leadership.

The shared authority helper at registry lines 4033-4045 uses a one-time removal
receipt. The provider-leadership flag is set only for a provider commander or
council and is cleared when a claimant replaces that authority, so the defeat
callback cannot retire an unrelated claimant and the final callback cannot
retire a later replacement leader.

Common classification, exact formation/lot/template ledgers, common route state,
shared missions/ideas, defeat reports, remnant ideas, and final state variables
remain Event 19-owned and are not prematurely erased by provider callbacks.
Defeat commits only after provider proof. Final cleanup commits only after both
tracked-formation absence and provider proof; otherwise the actor is retained for
retry.

## Exact current family behavior

| Family | Registration | Template | Management |
| --- | --- | --- | --- |
| Zombie 501 / provider 501 / source 2 | `trainable_and_spawnable`, family-only, visual 1 | four base `zombies` battalions | uses training; base zombie template only |
| Ghost 502 / provider 502 / source 10 | `spawn_only`, family-only, visual 2 | four `death_weak_ghost_host` battalions | spawning only |
| Golem 503 / provider 503 / source 5 | `spawn_only`, family-only, visual 3 | two `coal_golem` battalions | spawning only |

No mutated, weaponized, advanced zombie, stronger ghost, or alternate golem
token is registered or train-enabled. All provider templates begin locked and
non-recruitable. Only the exact family-501 generated template can receive the
proved training authorization, and defeat reverses that authorization.

## SCN-013 anomalous scenario and microstate safety

Host eligibility at
`common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt:125-139`
requires a live normal-civilian country, the generic parent-identity absence
boundary, an idle scenario transaction, no derivative/scenario identity, and at
least one controlled passable owned state. `world_end` is only a negative launch
gate.

The split trigger at scenario-trigger lines 238-246 requires more than the
microstate maximum and a controlled noncapital mainland state. Valid larger
hosts create dynamic actors with `original_tag = THIS`; a one-state or all-island
host takes the designed same-tag path. Failure during a split stops that front
and records setup failure; it does not fall through to a weaker tag or takeover
substitute. Successful actors declare only valid regional wars through the
budgeted candidate array.

The final SCN lifecycle repair is present in live source:

- dynamic anomalous creation persists both
  `infantry_spawn_derivative_family_id` and
  `infantry_spawn_derivative_provider_id` at
  `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2736-2747`;
- actor setup calls the active registry lookup, requires the exact loaded
  family/provider pair, and dispatches setup through the persistent derivative
  provider at scenario-effect lines 2459-2491;
- the obsolete scenario-only provider variable has no remaining occurrence.

The actor therefore uses the same provider identity for public setup, active
management, defeat cleanup, and final cleanup. No fixed tag, parent-event setup,
super-event call, or terminal world-end setter exists in the audited SCN path.

## Remediation observed and closed during this audit

This audit was run against live source while the parent applied narrow repairs.
Each item below was re-read after the corresponding patch:

1. profile 999 was restricted from all reserved family and provider IDs at both
   registration and row time;
2. cleanup lookup was separated from current availability/spawn/lot policy;
3. provider cleanup became live, proof-gated, and complete, including zombie
   trainability reversal and owned public identity removal;
4. claimant promotion now clears provider-leadership ownership before later
   cleanup;
5. first reception gained exact frozen identity, v4/visual/nonce validation,
   all-option revalidation, malformed-evidence failure, and no-provider retry;
6. Muster gained selected-view and registry bounds plus pre-dispatch visual
   validation;
7. natural template rebuilding gained exact frozen row/family/provider/v4
   validation;
8. active derivative lookup gained exact provider/full-contract validation;
9. SCN dynamic anomalous actors now persist, re-resolve, and reuse the exact
   derivative provider through cleanup;
10. the final inert scenario-only provider cleanup token was removed.

No item remains open in the final source snapshot.

## References and tool evidence

Repository skills read and followed:

- `chaos-redux-events`;
- `chaos-redux-subagents`.

Required offline wiki pages consulted before source inspection: Data structures,
Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding,
Decision modding, Idea modding, AI modding, Division modding, and Unit modding.

Vanilla authority consulted included:

- `documentation/script_concept_documentation.md`;
- `common/script_constants/documentation.md`;
- the exact relevant entries in `effects_documentation.md` and
  `triggers_documentation.md`;
- a vanilla dynamic-country precedent in
  `common/national_focus/czechoslovakia_mu.txt:4553-4556`.

The required narrow `hoi4.event_inspect` attempt for `chaosx.nr19.105` could not
produce an artifact because the MCP server returned `ARTIFACT_STORAGE_LIMIT`.
This is recorded as a tooling limitation, not a gameplay finding. The live event,
trigger, effect, localisation, provider, and scenario sources were inspected
directly and completely for the contract in scope.

## Files changed, simplifications, and remaining risk

- The auditor changed only this handoff file.
- The auditor made no gameplay, localisation, specification, registry, constant,
  trigger, on-action, asset, workbook, or exported-CSV edit.
- No fallback tag, substitute family, unknown-profile presentation, parent setup
  helper, world-end mutation, or weakened cleanup proof was accepted.
- No requested registry/scenario audit criterion was omitted.
- No simplifications or omissions remain in this audit scope.
- No files were staged and no commit was created by the auditor.
