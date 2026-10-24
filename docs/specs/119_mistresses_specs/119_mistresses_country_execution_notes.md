# Country and unit execution notes

This companion preserves the detailed native integration and source evidence for [Part 6](119_mistresses_spec_part_6_countries_forces.md). These are future implementation obligations and inspected source facts. They do not claim runtime completion.

## Event 19 integration and country classification

The pinned implementation exposes Chaos unit-family registry contract version 4. Future family and provider numeric IDs begin at 500 and remain unreserved symbolic identifiers in this plan. The package must register complete aligned metadata and its owner-side callbacks. Registration is idempotent by family ID, and a repeated registration with different metadata is an invariant failure. [R1][R2][R3]

Register three distinct family rows, one each for Cadre, Line and Siege, under one Event 119 owner-side provider with family-aware callbacks. Each row has its own reserved family ID and explicit concrete-unit disposition. This registry grouping differs from the single CXT package family token used for co-located showcases. Choose `family_only` lot participation for ordinary native brood hosts. Keep derivative release and other direct consumers explicitly gated. An unrelated human country must not receive a self-sustaining alien breeding army through a generic random infantry reward. A special scenario or deliberate derivative consumer can be supported only with its own custody, recruitment and cleanup rules. Such a derivative receives a complete, separately bounded adult-alien and equipment entitlement rather than human conscription or a new initial-revelation grant.

The proposed row metadata is deliberately explicit while numeric reservations remain open:

| Row | Availability mode | Event 19 lot policy | Base spawn weight | Additional live gate |
| --- | --- | --- | ---: | --- |
| Cadre family | `3`, trainable and spawnable | `1`, family only | 35 | Active brood or explicit supported derivative/test permission, paid adults and equipment. |
| Line family | `3`, trainable and spawnable | `1`, family only | 60 | Same identity and payment gates, valid Line operational access. |
| Siege family | `3`, trainable and spawnable | `1`, family only | 5 | Same gates plus actual heavy capability, stores and legal supplied site. |

Every row records source event 119, registry contract version 4, visual profile 999 and the common reserved provider ID. Sustainment, containment, AI, derivative, cleanup and parent-isolation profiles remain symbolic owner-defined reservations until their current namespaces are audited. They must exist before registration. These base weights are selection inputs among eligible rows, not unconditional percentages of all Event 19 outcomes. Parent isolation means provider delivery cannot fire Unveiling, seed a household network or qualify the Mother.

The registry uses availability modes and lot policies as separate fields. Set the actual supported combination for training and spawning, rather than treating registration as permission to recruit everywhere. The provider supplies sustainment, containment, AI, cleanup, parent-event isolation and visual profiles. Future providers must use visual profile `999`, `provider_neutral_army`, as required by the shared extension contract. The reserved original display profiles are not an invitation to attach new hardcoded Event 19 art mappings.

Provider callbacks dispatch through `chaos_unit_family_provider_[PROVIDER]_event19_<hook>`. The owner must implement the complete relevant callback surface and actual paid obligations. The default payment callback checks availability and marks success but charges nothing. The default refund callback clears a receipt and refunds nothing. Neither is a valid organic recruitment payment implementation. The Event 119 provider validates and debits real manpower and equipment atomically, records delivery, and refunds only the measured paid amount on a supported failed delivery. An Event 19 lot never reuses the Unveiling initial-equipment receipt.

The package adds its own registration surface and startup call. It does not require edits to a central Event 19 family list, display map, picture map or shared registry implementation. Documentation updates belong to the owner change, including `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` and `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`.

The broad `all_chaosx_country_tags` registry includes dormant carriers and countries with other event provenance. Add finalized brood tags to that lookup when reserved, but use a separate Event 119 active-generation registry and live lifecycle gates for alien behavior. Broad special-country membership is not evidence of active Event 119 identity, readiness or origin. Existing Event 006 provenance remains its own ledger. [R4]

## CXT registration and test-country fixture

Use one package-owned modifier-free hidden-idea carrier and a matching idempotent `_apply` helper. Register from a bounded existing-country startup hook. An additive `on_daily_CXT` fallback may register unseen content and mark synchronization pending. It must never apply resources, technologies, units or gameplay systems daily. The carrier is not a visible national spirit and needs no localisation or icon. [X]

Before registering related units, publish the real family token. Register concrete equipment and each frontline subunit through the existing CXT extension helpers. The harness creates an individual four-battalion homogeneous showcase for every combat type. Also register the actual practical package formations under distinct modifier-free formation markers. Each marker is a token for a template, not another extension-effect carrier.

All individual and mixed Event 119 formations reuse the retained family site chosen by the common allocator. The site must be owned, controlled, passable and compatible with the supply-route checks. Invalid sites release their reservation and remain eligible for later allocation. A one-province island cannot host an unlimited number of distinct family sites, and the fixture must not annex unrelated territory merely to make the screenshots convenient.

Template registration and initial deployment have separate receipts. A template that exists but has not had a valid creation dispatch remains eligible for application. Native `create_unit` has no documented success return. The harness's successful-dispatch flag is evidence of guarded dispatch, not proof that the engine actually placed and equipped the division. Actual model, counter, manpower, equipment and supply observations remain a live verification step.

Initial or player-triggered application exposes the country fixture and unit roster without firing Event 119, selecting ordinary hosts, creating a Mother, or fabricating population and payment history. CXT remains the normal test-harness classifier and is not inserted into the active alien generation registry. A narrow explicit fixture permission exposes alien unit access without impersonating a live brood or invoking nonhuman civilian-system cleanup. Destructive scenarios such as simultaneous Unveiling, absorption and player transfer are separate explicitly selected fixtures. CXT's broad research completion cannot certify an authentic technology clock, provider payment or ordinary-country progression. No base-game acceptance case relies on a CXT-only all-technology shortcut.

## Source anchors and evidence limits

This chapter applies the fully read supplied project protocol, current `AGENTS.md`, improvement-loop planner, country-package auditor, focus-tree auditor and equipment-units worker contracts. It also applies the event-planning skill and all seven references. The following anchors identify the technical source basis for the nearby claims.

- [U] Current `.claude/skills/chaos-redux-units-divisions/SKILL.md` and all three references, including runtime effects, names/stats/visuals and naval/air OOBs.
- [E] Current `.claude/skills/chaos-redux-equipment/SKILL.md` and both production/stockpile and modular-equipment references.
- [T] Current `.claude/skills/chaos-redux-technology-doctrines/SKILL.md` and both technology-tree and doctrine references.
- [C] Current `.claude/skills/chaos-redux-characters-leaders/SKILL.md` and both character and trait references.
- [D] Current `.claude/skills/chaos-redux-diplomacy-war/SKILL.md` and syntax reference.
- [A] Current `.claude/skills/chaos-redux-ai-strategies/SKILL.md` and both AI references.
- [R1] Pinned repository `common/script_constants/chaos_unit_family_registry_constants.txt`, SHA256 `db65279e9d83a9d488437eb55bb672d310c9703369b348b2d303b61128c1ef96`.
- [R2] Pinned repository `common/scripted_effects/chaos_unit_family_registry_effects.txt`, SHA256 `08ed1c4fb92d7b1ecdd6be7bea3a114e1ce65ea3eb151caf5cacf4e31ac49bd5`.
- [R3] Pinned repository `common/scripted_triggers/chaos_unit_family_registry_triggers.txt`, SHA256 `f8d845f42371bf0ce53448648e57f7eb870e36327ba208e455aeafbc6e238514`.
- [R4] Pinned repository `common/script_constants/chaosx_country_registry_constants.txt`, SHA256 `19d394e977fc14703f0513326ca6c9f081d2b044fd969e52709bc466b2007dcd`.
- [X] Pinned repository `docs/testing/chaosx_test_country.md`, all 519 lines, SHA256 `ea3408ba78a40ee7e8eaa6febfc96b6cb92d8e320fa377ed113588a9bea59ecc`.

The five repository sources above were read fully at commit `41bc4e5045a7b5c131be69dda2f08079d478634c`. This is source-grounded design evidence. It is not a claim of installed-game inspection, tag collision clearance, live native spawning, complete multiplayer transfer support or measured combat balance. Part 10 owns the future implementation gates and promotion sequence.
