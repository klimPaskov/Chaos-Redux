# CBRN Warfare System

## Scope and authority

The system links protective production, Chaos Warfare specialization, native chemical and biological raids, outbreaks, state response, evidence, deaths, contamination, Condemnation and recovery.
The [accepted CBRN amendment](../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md) governs design; the [requirement ledger](../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md) and [completion report](../../plans/chaos_warfare_system_plans/2026-09-25_cbrn_overhaul_completion_report.md) distinguish current source implementation from remaining gaps.
This overview describes the current source loop and does not certify the complete package or native execution.

## Playable loop

1. Research ordinary protection, medical and delivery technologies and produce their real equipment and payloads.
2. Choose Retaliation Only, Battlefield Authorization or Unrestricted Authorization through the three direct policy decisions, each costing 5 Command Power with a 90-day reassessment interval.
3. Let stock-backed maintenance derive readiness, service military filters and issue military masks before threatened civilian filter service/issue and remaining civilian work.
4. Equip the available support and Army HQ roles, with Chaos Warfare adoption and mastery providing specialization without separate establishment, claim, training-purchase or commission cards.
5. Use the native Chemical Raids or Biological Raids interface, meeting the selected route's exact target, origin, assigned forces, intelligence, preparation, policy, protection and real payload requirements.
6. Resolve source-recorded consequences and respond through applicable treatment, protection, containment, decontamination, evidence and diplomatic actions.

Native land routes use assigned divisions and supply-node origins, while air routes retain their own aircraft requirements.
Doctrine never raises use policy automatically, and ordinary protected battlefield routes retain vanilla-doctrine access after their normal research, project and equipment gates.
Chemical Readiness is derived from issued equipment, cleanup kits, training and specialization rather than purchased as a separate currency.
Civil Defence responds to live alerts, contamination, active chemical responses or credible current-enemy capability/use, with separate biological-outbreak and active occupied-program visibility.
Own durable victim history or retaliation permission alone does not sustain current civilian issue, and biological-only visibility does not grant a new chemical respirator benefit.
Routine new civilian issue retains its 50% effective-coverage target, serves threatened rural cores before clean strategic fallback, and leaves paid occupied-population and foreign-aid reservations under their existing contracts.
The dedicated British historical receipt, real model stocks, filter costs and bounded country scheduler remain separate from optional emergency response purchases.
See [command and protection](cbrn_simplification.md), [current need and priority](../../specs/chaos_warfare_system_specs/corrections/2026-10-09_civil_defence_current_need_and_priority.md) and [native raid integration](cbrn_native_raid_migration.md) for exact boundaries.

## Formations and mastery

Three HQ sections provide Operations and Intelligence, Protection and Decontamination, and Medical and Biosecurity.
The field package has one Protection Company, one Field Medical Company, reconnaissance, projectors, ammunition logistics, biosecurity assault, the Chaos Battalion and three light/medium/heavy armored-delivery roles.
The eighteen obsolete agent-specific tank companies are deleted; retained inactive legacy definitions elsewhere do not expand the playable roster.
Nerve suppression remains an operation upgrade rather than a standing company.
The four authored mastery lists cover thirteen unique retained roles, with membership shared across tracks as shown below.

| Track | Authored contributors | Count |
| --- | --- | ---: |
| Hazard Assault Formations | Protection, reconnaissance, Field Medical, biosecurity assault, Chaos Battalion | 5 |
| Contaminant Fire Support | Projector, ammunition train, Field Medical | 3 |
| Toxic Armored Warfare | Light, medium and heavy armored delivery | 3 |
| Integrated CBRN Command | Operations HQ, Protection HQ, Medical HQ, Protection, reconnaissance, Field Medical | 6 |

The [unit package](cbrn_unit_consolidation.md) and [doctrine guide](chaos_warfare_doctrine.md) own exact identifiers, unlocks, equipment bills, abilities and category memberships.
The lists describe source eligibility, not measured mastery speed or native division statistics.

## Projects and historical starts

The eight first-tier projects are Mechanized Smoke Screens, Collective Protection Systems, Self-Renewing Filters, Phantom Mist, Mass Vaccine Production, Field Antibiotics, Regenerative Serum and Broad-Spectrum Antiserum.
Self-Renewing Filters, Phantom Mist, Regenerative Serum and Broad-Spectrum Antiserum are fictional project entries.
The [user-approved shared Event 016 exception](../../specs/chaos_warfare_system_specs/corrections/2026-10-09_shared_event016_project_budget_exception.md), integrated in `e4372477`, preserves full Biomedical Acceleration, cloning, paleogenetics and xenobiology rewards through existing shared APIs while ordinary CBRN bonuses retain their caps.
Budget reporting keeps ordinary subtotal, exceptional family/stage contributions and combined totals visible, with native aggregation and the reconnaissance countermodel unresolved.
Weaponization remains separately authorized rather than an automatic ordinary project stage.
France's [1939 protective-industry setup](../../specs/chaos_warfare_system_specs/corrections/2026-10-09_france_1939_protective_industry.md), integrated in `7133a8990`, requests basic-respirator production from an existing military factory without granting a factory, starting stock or inferred civilian issue.
Other historical entitlements remain governed by the accepted country-specific profiles and evidence.

## Consequences and biological response

Chemical delivery uses exact source records and equipment-backed protection before the shared consequence dispatcher updates disruption, deaths, contamination, medical saturation, evidence, attribution and Condemnation.
Doctrine's bounded Condemnation mitigation does not erase payload expenditure, deaths, attribution, confirmed-use history or public-harm records.
Idle chemical-capable aircraft do not create exposure through an unverified ordinary-air activity estimator.
Ordinary anthrax, plague, tularemia and smallpox retain separate incubation, spread, containment and treatment profiles, while weaponized zombies have their own lifecycle.
The [biological system](biological_warfare/biowarfare_system.md) and [continuing civilian protection](continuing_civilian_protection.md) describe their current consumers and timing contracts.

Biomedical response entitlement reads the durable `conventional_technology_biomedical_operational` flag, with the separate weaponized flag additionally requiring operational entitlement.
The current biological lifecycle adds fifty points per eligible tier to surveillance, containment, medical response and biosecurity, retaining the existing response clamp.
The ordinary shared API grants operational entitlement; story stage/owner lifecycle is a separate contract, so project damage, suspension or owner inactivity does not itself establish automatic loss of a durable neutral capability.
This source trace does not prove native callback execution or every response outcome.

## Current consumers and remaining status

The original restored grand emblem remains `GFX_doctrine_chaos_warfare_medium`, using `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds`.
Current asset references follow their actual consumers rather than obsolete six-HQ, six-MIO or staged window/animation inventories.

| Consumer family | Current source or owner reference |
| --- | --- |
| Protection technology, equipment, decisions and state modifiers | [cbrn_protection.gfx](../../../interface/cbrn_protection.gfx) |
| Doctrine, officer corps and commander traits | [cbrn_doctrine.gfx](../../../interface/cbrn_doctrine.gfx), [chaosx_traits.gfx](../../../interface/chaosx_traits.gfx) |
| Unit counters and texticons | [unit/texticon coverage](cbrn_unit_texticon_assets.md), [subunit icons](../../../interface/chaosx_subuniticons.gfx), [texticons](../../../interface/chaosx_texticons.gfx) |
| Project equipment and special-project cards | [project equipment](../../../interface/cbrn_project_equipment.gfx), [special projects](../../../interface/cbrn_special_projects.gfx) |
| Chemical delivery and biological response | [chemical delivery](../../../interface/cbrn_chemical_delivery.gfx), [biological warfare](../../../interface/biological_warfare.gfx) |
| Designers and industry | [designers](../../../interface/cbrn_designers.gfx), [MIO industry](../../../interface/cbrn_mio_industry.gfx) |
| Achievements | [achievement contract and status](cbrn_achievements.md) |

Registration and source references do not prove every asset's final wiring, visible appearance or complete coverage.
No Wind Is Friendly and Unbroken Supply Corridor remain accepted implementation gaps because exact affected-army/forecast recovery and assigned-army supply/objective evidence are absent.
Personal native-raid-to-commander association, exact lifecycle/refunds, effective aggregation and visual consumers remain unverified.
Within-tier allocation order and native state/resource transactions retain their documented limits.
The current [requirement ledger](../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md) and [completion report](../../plans/chaos_warfare_system_plans/2026-09-25_cbrn_overhaul_completion_report.md) control remaining work; historical stage plans do not create duplicate current requirements.
