# National policies

National policies are country-level laws that govern civilian reception and departure and chemical, biological, and nuclear use. Their native law ideas are authoritative; compatibility variables and operation-specific checks are published from those laws.

## Authority and law families

The five native law slots are defined in `common/ideas/national_policy_laws.txt` and grouped in `common/idea_tags/national_policy_categories.txt`:

| Family | Choices | Base cost |
| --- | --- | ---: |
| Refugee reception | Humanitarian, Controlled, Transit, Quarantine, Closed, Violent, Forced Return | 100 Political Power |
| Civilian departure | Free, Permit, Prohibited | 100 Political Power |
| Chemical use | Retaliation, Battlefield, Unrestricted | 150 Political Power |
| Biological use | Retaliation, Battlefield, Unrestricted | 150 Political Power |
| Nuclear use | None, Retaliation, Unrestricted | 150 Political Power |

Each family has one current law. The law's `on_add` publisher updates its derived value and compatibility view, then calls the owning migration or warfare callback with previous and new values. Initialization suppresses ordinary policy-change consequences while applying the starting profile. Changes to laws are paid through the native law interface; the panel does not charge Political Power itself.

Civilian policies are eligible for countries using the ordinary famine and migration systems. The Holy Realm retains its existing Event 003 refuge-policy actions through a narrow adapter while remaining outside the shared civilian-law panel. Warfare permissions remain family-specific: chemical, biological, and nuclear laws independently authorize their operations. Retaliation evidence can grant a temporary right against the exact confirmed offender across C/B/N families for 365 days; a nuclear `None` law never inherits another family's evidence.

Chaos Warfare grants a live 25% cost reduction to the three warfare laws while the doctrine is active. Doctrine adoption refreshes those costs through the shared dynamic-modifier integration.

## Country profiles and lifecycle

Startup applies controlled reception, free departure, chemical retaliation, biological retaliation, and nuclear none as the baseline. The explicit bookmark profiles set departure permit for GER and SOV, all three unrestricted warfare laws for JAP, and unrestricted chemical use for ITA. JAP's three-family profile is an explicit design choice, not a claim of historical use. MAN and MEN receive ordinary defaults and do not inherit Japan's profile. The full 91-tag inventory across the 1936 and 1939 bookmarks and the audited profile evidence are in the [country initialization matrix](../specs/famine_and_migration_system_specs/national_policy_country_matrix.md).

Startup initializes each country once. Release and liberation remove inherited policy ideas and assign the new country its own default or exact-tag profile. Civil wars preserve the selected laws. Government and state-control lifecycle hooks reconcile only affected countries; no recurring world-country scan is added.

## Management panels and operational actions

The famine and migration management windows are separate, quiet-accessible country panels, each sized 900 by 600, with Overview and States tabs. They provide a stable place to inspect current conditions and perform eligible operational actions. Their panel actions are wrappers around the existing decision/action owners: costs, due dates, receipts, cancellation, rejection and refund rules remain with those owners. Sparse pending-action processing uses bounded per-country registrations and does not add a world loop.

Native law categories are the only purchase surface for policy choices, while the panels provide the operational surface for famine response and civilian management. The migration panel presents current reception and departure policy with its operational controls; it does not create a second policy ledger. The dedicated map modes and existing crisis eligibility rules retain their separate purposes.

## Test-country registration

The national-policy package registers its idempotent setup effect through the modifier-free `national_policy_cxt_extension` carrier. Registration makes the setup available to CXT; it does not grant policies during the daily fallback. Initial setup or a player-triggered debug action applies the package, and unrestricted warfare remains a separate explicit fixture action. See the [CXT package registration contract](../testing/chaosx_test_country.md#national-policy-laws).

## Source and validation limits

Implementation ownership is split among `common/scripted_effects/national_policy_effects.txt` and `national_policy_warfare_effects.txt`, their corresponding triggers, the native idea definitions, cost helpers, the humanitarian action adapters, and the two panel GUI packages. This document summarizes those boundaries; it does not assert live-game completion. The country matrix records source-model limitations, and the current [panel implementation report](../plans/famine_and_migration_system_plans/national_policy_panels_implementation.md) tracks outstanding integration and visual evidence.
