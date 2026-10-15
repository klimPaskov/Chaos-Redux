# Part 9: National policy laws and management panels

Disposition: accepted design; implementation and source/visual review complete; isolated commit verification is in progress.

Acceptance basis: the user explicitly instructed “PLEASE IMPLEMENT THIS PLAN” on 2026-10-15. This accepted addendum records that decision and the associated parent-approved requirements; its location or date is not being used as evidence of acceptance.

## Accepted decisions

- Keep famine and migration as independent mechanics with separate country panels. Each panel is a quiet-accessible, always-eligible 900×600 camps-style window with Overview and States tabs.
- Put the operational famine and migration actions in their panels while retaining native AI missions and existing decision/action owners. Panel wrappers must preserve existing costs, due dates, receipts, rejection handling, refunds and bounded sparse processing.
- Use five native political-law slots with nineteen total choices: reception (7), civilian departure (3), chemical use (3), biological use (3), and nuclear use (3). Base costs are 100 Political Power for each civilian slot and 150 for each warfare slot. Chaos Warfare gives the three warfare slots a live 25% discount.
- Native laws are the authority for derived policy values and operation permission. This adds no food law and no food-production economy. Famine remains a support crisis driven by war, blockade, history, fallout and wasteland conditions.
- Confirmed chemical, biological or nuclear use creates cross-family retaliation only against the exact offender for 365 days. Nuclear `None` blocks nuclear authorization regardless of C/B evidence.
- Apply JAP's all-three-unrestricted profile explicitly in both bookmarks (1936-01-01 and 1939-08-14), ITA unrestricted chemical, and GER/SOV departure permit. Other countries use controlled reception, free departure, C/B retaliation and nuclear none. MAN/MEN remain at those defaults; Japan's nuclear setting is not inherited automatically.
- Preserve the Holy Realm's exact civilian-policy exception by adapting its existing Event 003 policy actions to native laws while keeping it outside the ordinary civilian category.
- Register this package with the modifier-free CXT carrier and player-triggered package application. Panels do not initialize gameplay.

## Country evidence and scope

The linked [national policy country matrix](national_policy_country_matrix.md) records the tag union from the 1936 and 1939 vanilla bookmarks (91 distinct tags), exact starting profiles, CXT and lifecycle evidence. It distinguishes explicit policy decisions from source-derived implementation and historical inference. Its accepted basis for the country-specific exceptions is the same user instruction named above; source code confirms implementation, not design authority.

## Implementation mapping

The canonical overview is [National policies](../../systems/national_policies.md). Famine and migration mechanics remain documented in [famine_system.md](../../systems/famine_system.md) and [migration_system.md](../../systems/migration_system.md); this addendum does not merge their ledgers, categories or crisis rules. The CXT setup contract is documented in [chaosx_test_country.md](../../testing/chaosx_test_country.md#national-policy-laws).

The current implementation report is [national_policy_panels_implementation.md](../../plans/famine_and_migration_system_plans/national_policy_panels_implementation.md). It carries implementation evidence, individual handoff dispositions, validation limits and pending parent checks. GUI source presence and reference images alone do not establish final visual acceptance.

## Historical notes and open evidence

Older famine and migration design parts predate this accepted policy-panel integration and remain historical design for their own subjects. Where they describe famine/migration eligibility, crisis support or native AI missions, retain those decisions unless this addendum explicitly changes them. The accepted panel-first operational surface does not silently replace the AI mission system.

Parent integration owns the final GUI renderer/layout evidence and completion status. Until that evidence is recorded in the current implementation report, the overall panel work remains in progress. Live-game validation remains outside this documentation record.
