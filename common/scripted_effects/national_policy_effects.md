# Native national policy helper contract

The parent accepted five native law slots and the exact starting profiles in the national policy and humanitarian panels task on 15 October 2026.
The native idea in each slot owns policy.
Numeric country variables are derived compatibility views and never override a selected idea.
The warfare operation owner separately checks capability, custody, target identity and current retaliation evidence.

## Helper map

All helpers below execute in country scope.

| Helper | Inputs and defaults | Outputs and side effects | Direct callers |
| --- | --- | --- | --- |
| `national_policy_publish_reception` | Required temporary `national_policy_requested_value`, an existing `migration_border_policy` constant | Writes `migration_reception_policy` and civilian compatibility, supplies previous/new values and civilian slot 1, notifies migration after a genuine change | Seven reception law `on_add` blocks |
| `national_policy_publish_departure` | Required temporary `national_policy_requested_value`, free 1, permit 2, prohibited 5 | Writes `migration_departure_policy` and civilian compatibility, supplies previous/new values and civilian slot 2, notifies migration after a genuine change | Three departure law `on_add` blocks |
| `national_policy_publish_chemical` | Required temporary `national_policy_requested_value`, permission 2, 3 or 5 | Writes `cbrn_chemical_use_policy` and combined compatibility, supplies family 1 and previous/new values to warfare callback | Three chemical law `on_add` blocks |
| `national_policy_publish_biological` | Required temporary `national_policy_requested_value`, permission 2, 3 or 5 | Writes `cbrn_biological_use_policy` and combined compatibility, supplies family 2 and previous/new values to warfare callback | Three biological law `on_add` blocks |
| `national_policy_publish_nuclear` | Required temporary `national_policy_requested_value`, permission 0, 2 or 5 | Writes `nuclear_use_policy`, supplies family 3 and previous/new values to warfare callback | Three nuclear law `on_add` blocks |
| `national_policy_publish_civilian_compatibility` | Current published departure and reception variables | Writes their maximum to `migration_border_policy` and its existing active-policy flag | Civilian publishers and reconciliation |
| `national_policy_publish_warfare_compatibility` | Current published chemical and biological variables | Writes their maximum to `cbrn_use_policy` for historical and treaty compatibility | Warfare publishers and reconciliation |
| `national_policy_reconcile_country` | Current native law ideas and country eligibility | Rebuilds all five variables and compatibility views, removes ineligible civilian laws and their variables and holds | Initializer, starting/release/CXT helpers, subsystem read adapters |
| `national_policy_initialize_country` | Existing country, optional installed laws | Fills missing applicable slots with defaults, reconciles, installs cost modifiers and sets `national_policy_initialized` | Startup profile, lifecycle hooks, CXT, subsystem adapters |
| `national_policy_apply_starting_profile` | Existing country and exact tag | Initializes, then applies the accepted profile once under `national_policy_starting_profile_applied` | Existing startup sweep and Japan startup grant |
| `national_policy_initialize_released_country` | Newly released or liberated country | Removes inherited policy ideas, installs its own default/profile and reconciles silently | Free release, puppet release and liberation hooks |
| `national_policy_register_cxt_content` | Existing bounded country scope | Registers the modifier-free `national_policy_cxt_extension` token | GER startup and CXT daily registration |
| `national_policy_cxt_extension_apply` | Initialized CXT only | Idempotently initializes laws and sets `national_policy_cxt_fixture_ready` | Player-triggered CXT extension dispatcher |
| `national_policy_cxt_enable_unrestricted_warfare` | CXT only | Installs the three unrestricted native laws silently, preserving the explicit debug fixture | Existing player-triggered CXT warfare setup |

The caller declares `national_policy_requested_value` before invoking a bare `= yes` publisher.
A missing or unsupported request does not publish any policy value.
The five publishers intentionally consume the newly selected value directly rather than scanning native ideas during `on_add`.
The engine can still expose the old law while adding its replacement.
Subsystem change callbacks must use `national_policy_previous_value`, `national_policy_new_value` and the supplied family or civilian-slot temporary value, and must not reconcile ideas within that callback.
The selected value is published before notification.
The migration callback is `migration_national_policy_changed` and the warfare callback is `national_policy_on_warfare_law_changed`.
Those callbacks own their political, history, treaty and reservation consequences.

Example native law callback:

```txt
on_add = {
	set_temp_variable = { national_policy_requested_value = constant:national_policy_permission.battlefield }
	national_policy_publish_chemical = yes
}
```

The migration owner's `migration_decision_set_policy` remains the authorized external request adapter, including Event 003 refuge choices.
It validates both requested dimensions before mutation, maps reception 1 through 7 and departure 1, 2 or 5 to native `add_ideas`, then reconciles and clears both request temporaries.
Zero means no requested change, and unsupported requests return an invalid result without changing either law.
The adapter charges no scripted CP or PP and cannot assign a numeric policy independently of a native idea.
Ordinary moved migration operations no longer submit national policy requests.

Example country birth reconciliation:

```txt
national_policy_initialize_country = yes
```

## Defaults and profiles

| Slot | Default | Values |
| --- | --- | --- |
| `refugee_reception` | `national_policy_reception_controlled` | Humanitarian 1, controlled 2, transit 3, quarantine 4, closed 5, violent 6, forced return 7 |
| `civilian_departure` | `national_policy_departure_free` | Free 1, permit 2, prohibited 5 |
| `chemical_use_policy` | `national_policy_chemical_retaliation` | Retaliation 2, battlefield 3, unrestricted 5 |
| `biological_use_policy` | `national_policy_biological_retaliation` | Retaliation 2, battlefield 3, unrestricted 5 |
| `nuclear_use_policy` | `national_policy_nuclear_none` | None 0, retaliation 2, unrestricted 5 |

Both accepted bookmarks, `1936.1.1.12` and `1939.8.14.12`, use the same policy profiles.
Japan receives unrestricted chemical, biological and prospective nuclear authorization by explicit user direction.
Italy receives unrestricted chemical authorization, with the 1939 continuation recorded by the parent as a gameplay inference.
Germany and the Soviet Union receive departure permits.
MAN and MEN retain ordinary defaults and do not inherit Japan's profile merely because they are subjects.
All other existing countries use the default profile.
This is an authorization profile and grants no technology, weapon, readiness or live crisis.

Civilian law applicability requires `uses_normal_civilian_systems` and either exclusion of `is_special_chaos_country` or the explicit `is_holy_realm_country` humanitarian exception.
The Holy Realm retains the ordinary famine and migration boundary already established by `humanitarian_country_is_valid`.
The ordinary humanitarian panel category can keep its separate special-country presentation exclusion.
Warfare applicability follows `cbrn_action_actor_is_valid`, with no capability or active-crisis prerequisite for selecting a law.
Civil-war ideas use `allowed_civil_war = { always = yes }` and the existing government-change callback initializes missing slots and reconciles inherited laws.
Release and liberation callbacks deliberately use the separate reset helper.
Retaliation evidence is never copied or reconstructed by these helpers.
The warfare owner authenticates its own receipts independently of inherited native laws.

## Constants and AI

`common/script_constants/national_policy_constants.txt` owns permission values, family identifiers, civilian-slot identifiers, the doctrine discount and native law AI tuning.
The existing migration border enum remains the only civilian policy value table.
The native static `cost` fields use the two file-local macros at the top of `national_policy_laws.txt`, 100 civilian and 150 warfare.
No documented idea cost field guarantees `constant:` parsing, so those static fields follow the installed native law precedent and the repository's file-local constant exception.
Cost modifiers, the Chaos Warfare reduction and Black Friday accounting belong to the cost-integration owner.

AI uses base score 1, current-law preference 20, operational response 64, and a bounded current Japanese or Italian unrestricted-profile factor 8.
A genuine law change creates a family-specific 180-day AI hold, passed through the matching file-local literal duration macro to the native timed flag.
Holds affect AI scoring only, and a civilian choice cannot delay a separate warfare family.
An alternative scores zero during that family's hold or without the configured PP reserve.
Native purchase affordability remains enforced by the engine with its actual modified cost.

Quiet countries retain their selected policy.
Reception alternatives require a valid pending offer and measured spare capacity, an active disease threat, or a valid exhausted-capacity signal.
Violent rejection and forced return are retained if explicitly selected but have no autonomous AI adoption signal.
Departure permits can follow the German or Soviet profile while there is no flight, trapped population or overloaded-host signal.
Departure relaxes under those relief signals, and AI never autonomously chooses prohibited departure.
Chemical and biological first-use escalation requires actual family capability and an explicit route.
The Japanese chemical campaign signal is excluded from biological first-use intent.
Nuclear retaliation requires real nuclear capability and the warfare owner's exact offender/family evidence trigger.
Unrestricted nuclear selection requires real capability, war and an explicit unrestricted route, while the accepted Japanese starting law remains stable without inventing capability.
Doctrine adoption alone supplies no AI escalation signal.
These are selection scores, not probabilities or claims about native AI evaluation frequency.

## Lifecycle and cleanup

No new event target, world iterator, periodic law reconciliation or crisis registry is added.
Startup reuses the existing human-system startup country sweep.
Birth, government and state-control hooks use the affected country only.
The CXT daily fallback registers unseen content and marks the existing pending flag, and never applies the package.
The explicit player-triggered CXT setup owns its unrestricted fixture.

The temporary `national_policy_initializing` flag suppresses law-change notifications and AI holds during setup, default repair, release and debug setup.
Every initializer exit clears it.
Ineligible civilian countries lose both civilian native laws, derived variables, compatibility marker and civilian AI holds.
The native family-specific hold flags expire without a periodic script.
Profile and fixture readiness flags are lifecycle receipts and require no recurring cleanup.
The warfare owner remains responsible for stale retaliation evidence and pending operation cleanup.

## Art and localisation

The parent owns GUI and GFX integration.
The five idea pictures are `national_policy_reception`, `national_policy_departure`, `national_policy_chemical`, `national_policy_biological` and `national_policy_nuclear`, resolved as `GFX_idea_<picture>`.
Empty-slot sprites use the exact five slot IDs through the native `GFX_idea_slot_<slot>` family.
English names, descriptions, category names, eligibility tooltips and cost-source labels live in `localisation/english/national_policy_laws_l_english.yml`.
The CXT carrier is never applied and needs no icon or player-facing name.

## Validation limits and future work

The maintained production-source fixture `.tools/tests/test_national_policy_laws.py` executes initialization, exact publishers, reconciliation and CXT helpers while recording external callbacks.
It covers the 18 named bookmark/tag cases and all 132 ordered replacement/callback cases, plus exclusion, release, inherited-law and representative AI scenarios.
Native engine callback timing, actual AI selection frequency and retaliation receipt authentication remain outside this fixture.
MCP file-mode results are partial because helper roots have unknown scope and native argument blocks are not fully checked.
The source check returned no confirmed native-command defect, and the initially unresolved migration callback is supplied by its assigned owner.

Independent probability review belongs to the parent's bounded AI auditor.
Future policy expansion should extend the existing owner enums and direct publishers rather than add a second numeric authority or a periodic repair loop.
Additional historical profiles require explicit accepted design and country-specific evidence.

Run the law regression with `python .tools/tests/test_national_policy_laws.py`.
It reads committed production source and writes its result only to `.tmp/national_policy_panels/laws_test_results.json`.
