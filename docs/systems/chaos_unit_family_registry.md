# Chaos Unit Family Registry

The Chaos unit family registry is the opt-in contract used by Event 19 and future systems that need to discover unusual battalion families without maintaining their own family lists. The live Event 19 provider contract is version 4.

## Ownership model

Each family owns one registration entry and one startup registration call. Event 19 reads the aligned `global.chaos_unit_family_*` rows and dispatches through the stored provider ID. Adding a future family therefore does not require adding it to an Event 19 family list.

Event 19 keeps its consolidated ordinary table and the initial zombie, ghost, and golem provider integrations in the single `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt` file. Registry tuning lives in the existing Event 19 constants, registry triggers live in the existing Event 19 trigger file, and startup registration calls live in the relevant existing parent on-action files. A future family defines its one complete registration effect and Event 19 callbacks in that family's existing integration surface, then calls the registration once from its existing parent startup path. It does not edit the Event 19 registry file, add a family-specific Event 19 registry file, add a second Event 19 registry file, or add an Event 19 family-list row.

The shared registry never infers eligibility from a unit token and never substitutes a different family. A missing provider, duplicate family ID with conflicting ownership, unsupported contract version, or misaligned table sets `chaos_unit_family_registry_invariant_failure` and prevents the affected Event 19 operation.

## Current Event 19 implementation status

The current registry and category lifecycle increment has been re-audited after
the 2026-07-29 changes. The sole dedicated Event 19 registry code file remains
exactly `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`;
there is no second Event 19 registry and no fixed-tag derivative route. Ordinary
automatic generation consumes rows whose policy is `ordinary_mix`, `family_only`,
or `both` only when the provider eligibility callback sets the native receipt;
family-only rows remain available through direct requests, first-family
reception, scenario, natural-release, and derivative consumers. Every consumer
walks aligned global registry rows and dispatches the stored provider ID, so a
future family contributes one complete registration row and provider callback
surface from its existing parent startup path without an Event 19 list or
registry-file edit. The parent-side derivative revolt marker and Board close are
success-gated at the final exact-transfer or one-state takeover proof, and the
country pulse clears a stale Board-open flag after passive closeout. Historical
whole-event asset, country, focus, scenario, catalog, and audit evidence remains
valid for those broader surfaces; this increment's focused handoff is the
current completion authority for registry selection and ordinary-category
lifecycle.

### Event 016 generic provider bridge

Event 016 registers the following generic Event 019 families from its idempotent runtime-package rebuild in `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`.

| Family | Family/provider ID | Event 016 implementation consumer | Provider-owned material profile |
| --- | ---: | --- | --- |
| Clone Infantry | 504 | `kruger_clone_infantry`, `infantry_equipment` | Standard infantry equipment plus exact manpower and training/sustainment costs. |
| Autonomous Robot | 505 | `kruger_robot_frame`, `kruger_robot_equipment_1` | Robot equipment, manpower, political power, and command power callbacks. |
| Paleogenetic Creature | 506 | `kruger_paleogenetic_beast`, `kruger_paleogenetic_equipment_1` | Paleogenetic equipment, manpower, political power, and command power callbacks. |
| Xenobiological Organism | 507 | `kruger_xenobiological_assault`, `kruger_xenobiological_equipment_1` | Xenobiological equipment, manpower, political power, and command power callbacks. |
| Alien Interface Infantry | 508 | `kruger_exotic_guard`, `kruger_exotic_arms_equipment_1` | Alien-arms equipment, manpower, political power, and command power callbacks. |

These rows use neutral visual profile 999 and remain unavailable until their corresponding Event 016 history-derived runtime flag is active, so Event 016 native force materialisation remains unchanged and no provider row becomes a synonym for the Event 016 parent identity.

The provider callbacks record only manpower in the shared Event 019 obligation ledger; project equipment is deliberately reconciled and paid by the provider callbacks so the shared equipment-profile enum is not broadened for Event 016-only equipment lines.

Generic derivatives use the common Event 019 country shell plus a provider-owned hidden family idea, neutral host commander, route variable, release report, and removable package marker, and cleanup verifies the stored family/provider pair and requested lifecycle phase before proving teardown.

## Registration fields

Every row records:

- family, provider, and source-event IDs;
- trainable, spawn-only, or combined availability;
- Event 19 family-lot and ordinary-mix policy;
- derivative, sustainment, containment, AI, visual, cleanup, and parent-isolation profiles;
- spawn weight and contract version.

The shared registry contains only the generic contract and aligned runtime rows. The initial Event 19-specific tuning, triggers, and static-token adapters follow the single-file ownership rule above; later providers remain externally owned and join through the generic provider-ID dispatch contract.

The eligibility callback returns two separate receipts. `chaos_unit_family_candidate_eligible` exposes a row to direct, first-reception, scenario, natural-release, and derivative consumers, while `chaos_unit_family_candidate_native` admits that row to the weighted automatic-generation family draw. A family-only row may therefore participate in automatic generation only for a provider-defined native host, while an ordinary-mix or both row can opt into the same draw for its own eligible countries.

## Provider contract

An Event 19-capable provider implements:

- `chaos_unit_family_provider_N_event19_evaluate_eligibility`;
- `chaos_unit_family_provider_N_event19_build_template`;
- `chaos_unit_family_provider_N_event19_spawn_unit`;
- `chaos_unit_family_provider_N_event19_evaluate_management`;
- `chaos_unit_family_provider_N_event19_pay_management_action`;
- `chaos_unit_family_provider_N_event19_refund_management_action`;
- `chaos_unit_family_provider_N_event19_reconcile_sustainment`;
- `chaos_unit_family_provider_N_event19_setup_derivative`;
- `chaos_unit_family_provider_N_event19_remove_public_additions`;
- `chaos_unit_family_provider_N_event19_cleanup_derivative`.

Static-token operations are selected with `meta_effect` using the recorded provider ID. Registration is idempotent only when every field in the existing row matches the offered entry; any conflicting provider, source event, availability mode, lot policy, profile, weight, or contract version marks the registry invariant failed. Startup initialization therefore cannot duplicate or silently redefine a row. A future family contributes one aligned runtime registration row and its provider contract from its own existing integration surface; Event 19 needs no hardcoded family enumeration, localisation map, picture map, list edit, or registry-file edit.

Contract version 4 makes parent isolation, public-package ownership, visual ownership, and provider cleanup executable. Parent event actors carry `chaos_unit_family_parent_actor`. The shared `infantry_spawn_parent_event_identity_is_absent` boundary rejects that marker together with provider-specific parent tags, original tags, country flags, stages, and progression markers before derivative creation. Event 19 clears `infantry_spawn_derivative_provider_parent_isolation_proved` and `infantry_spawn_derivative_provider_public_package_proved` before setup dispatch. The provider sets the first proof only after its shared and parent-specific isolation checks pass. It then initializes the Event 19 private package, installs its own public identity, leadership or council, family ideas, route package or adapted equivalent, and release report, and sets the public-package proof only after that complete public surface succeeds. Both proofs remain clear on failure. Event 19 refuses to classify, materialize, roster, or unlock an unproved nonhuman derivative.

All provider-installed one-person leaders and technical council characters use
`female = no`. A council's player-facing name and identity remain institutional;
the engine character is only the supported carrier for that authority. The six
fixed derivative identity slots depict massed hosts without an individual focal
person, even though their stable sprite identifiers use engine `portrait`
terminology.

Visual profiles 1, 2, and 3 are owned bindings, not generic presentation values. Profile 1 is valid only for family 501 with provider 501, profile 2 only for family 502 with provider 502, and profile 3 only for family 503 with provider 503. An external future provider must explicitly register `constant:chaos_unit_family_visual_profile.provider_neutral_army`, whose value is 999, unless a later contract adds another supported provider-owned profile. Profile 999 selects the identity-neutral Event 19 army or massed-host presentation. It never selects a human authority portrait or another family's scene, and it cannot be paired with any family or provider ID reserved by the three initial bindings. An unknown positive profile fails registration, and the row-time visual guard makes every Event 19 consumer reject an unsupported or mismatched saved row.

`event19_evaluate_management` reports provider-owned train and spawn eligibility, costs, and weights through the shared temporary-variable contract. `event19_pay_management_action` must set `infantry_spawn_family_provider_payment_succeeded` only after every provider-owned cost has been paid. If template creation or unit spawning then fails, Event 19 calls `event19_refund_management_action`; that hook must restore exactly the resources consumed by the selected action. Shared political-power, command-power, cooldown, Muster Control, and per-generation escalation costs remain Event 19-owned and are accounted separately.

The pre-fire first-family reception freezes its exact registry index, family ID, provider ID, visual profile, contract version context, and a positive nonce before the visible incident is scheduled. Delayed execution validates those saved values against the same aligned row but deliberately does not rerun current availability or eligibility, so a provider cannot be substituted after the promise is issued. No eligible row leaves the country-local pending state intact for a later Event 19 pulse. Partial, mismatched, out-of-range, or otherwise malformed frozen evidence resolves through the visible failed-reception path instead of dispatching a provider callback.

`cleanup_profile` records the reviewed cleanup contract, and contract version 4 also dispatches `chaos_unit_family_provider_[provider]_event19_cleanup_derivative`. Event 19 resolves cleanup by the actor's exact stored family/provider pair and the immutable lifecycle fields; present-day availability, family-lot, and spawning policy cannot strand an existing derivative. Event 19 clears `infantry_spawn_derivative_provider_cleanup_proved` before each defeat or final-cleanup dispatch. The provider callback must remove all provider-owned public additions, including provider-owned ideas, route state, leadership or institutional state, and other public identity surfaces, before it sets the proof for the requested `defeat` or `final` phase. Provider authority is retired only while `infantry_spawn_derivative_provider_leadership_installed` proves that the current authority still belongs to the provider; promotion of a claimant clears that receipt and protects the replacement leader. Provider 501 additionally revokes zombie training authorization, removes family 501 from the trainable-family ledger, and locks every recorded family-501 template even when no live unit remains. Missing proof fails closed and prevents the corresponding shared teardown from committing. Event 19 owns tracked-formation absence proofs, private ledgers, common derivative ideas and missions, common state markers, common flags and variables, and the remaining shared Event 19 cleanup surfaces. A provider must not clear those shared surfaces itself.

A future family joins through one external registration row plus its complete provider callbacks, including setup and cleanup. Those additions stay in the provider's existing integration surface and startup path. They require no Event 19 family-list, localisation-map, picture-map, or registry-file edit and never create another Event 19 registry file.

## Natural derivative selection

Event 19 evaluates natural anomalous pressure by iterating the aligned registry rows, loading each row through the generic provider contract, and selecting the strongest eligible family by pressure with live recorded formation count as the tie-breaker. It then builds a connected, noncapital candidate region from that family's recorded formation origins and any linked loyal claimant headquarters. This path has no zombie, ghost, golem, or future-family enumeration: a future family becomes eligible through its single registration entry and provider callbacks.

The natural-release transaction freezes the exact family or linked claimant-loyal unit, lot, generation, cohort, template, division, obligation, territory, and accounting identifiers before any country mutation. Because the engine has no division-scoped ownership-transfer effect, the owner approved an exact recreate-prove-delete substitute: the destination actor recreates only the frozen Event 19 formations, proves the complete replacement set, and only then deletes the corresponding source cohorts and commits accounting once. Failure restores the source snapshot or enters quarantine; it never broadens into a random formation or whole-army transfer. The substitute preserves recorded Event 19 identity, composition, liability, and accounting, but the engine cannot preserve exact live equipment variants and inventory, manpower fill, organization, veterancy, decorations, officer history, army assignment, plans, or orders. A conservative strength gate prevents the transaction from refreshing a damaged formation. Scenario-created derivatives retain their separate fresh-unit transaction and do not weaken this natural-release identity contract.

## Event 19 isolation

The initial providers expose only base `zombies`, `death_weak_ghost_host`, and `coal_golem`. Base zombies may be trainable. Ghosts and golems are spawn-only. Provider code may reuse the unit token but must not call the parent event's country setup, evolution, super-event, or world-end helpers.

Derivative identity uses dynamic-country creation or the proved same-tag takeover path. The registry contract has no fixed-tag fallback.

Shared country classifiers likewise remain list-free. A human claimant
breakaway qualifies only with the Event 19 derivative marker, claimant marker,
positive stable claimant UID, ordinary-family sentinel, and absence of the
nonhuman marker. A nonhuman derivative qualifies only with the nonhuman marker,
positive registered family ID, parent-isolation proof, and public-package proof.
`is_actual_nonhuman_country` delegates to that nonhuman derivative proof, so a
claimant-only breakaway remains human while still qualifying as a special Chaos
country. Neither classifier promotes a derivative into its parent event's actor
counts, stages, evolutions, super-events, or world-end progression. A future
provider participates through its registry row and proof callbacks without a
classifier list edit.
