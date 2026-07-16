# Event 006 IW-010 Saar country package

## Scope

IW-010 creates the Saar as `AJX` from state `42` in Northern and Western
Europe. It is a one-state industrial-security package built around coal, rail,
municipal administration, factory guards, and cross-border contracts. It uses
reservation group `RG-RHINE-SAAR`, so IW-010 and IW-008 cannot be selected in
the same Event 006 incident. A later repeatable wave may release the other
package, allowing living AJX and RHI countries to coexist.

The country is led by two fictional humans:

- Friedrich Hoffmann, a municipal jurist and neutral-commission chair;
- Karl Becker, an industrial-security commissioner and corps commander.

The Municipal Neutral Commission is civilian. Karl Becker has no country-
leader role, and neither script nor localisation describes the neutral route as
military, traditional, restorationist, or emergency government.

## Runtime sequence

1. The release transaction transfers and controls state `42`, makes it the AJX
   capital, records the dynamic former host, and preserves that host's selected
   remnant state.
2. `can_initialize_independence_wave_iw_010_package` proves the exact package,
   region, standard depth, industrial-breakaway archetype, anchor, capital,
   living former host, and host-owned protected remnant. Same-incident
   exclusion is enforced earlier by the shared `RG-RHINE-SAAR` plan
   reservation, not by testing whether RHI already exists in the world.
3. The dormant history supplies the baseline laws and recruits Friedrich
   Hoffmann and Karl Becker. Runtime setup installs provisional politics,
   localized parties, the full shared focus framework, package routes, the
   power struggle, ambition family, AI profile, and lifecycle values.
4. The shared p10 force table supplies the `industrial_security` profile,
   military tradition `50`, no naval or air inheritance, and exactly five
   reinforcement pathways: integrated militias, secure depots, factory and rail
   guards, foreign arms, and capital/border defense.
5. The prepared proof checks every one of those opening facts, including the
   exact positive and negative pathway set. The final proof also checks live
   active-country and network registries.
6. Package cleanup removes its mission and decisions, ideas, route state,
   lifecycle variables, AI flag, ambition hooks, and AJX-local markers before
   the shared origin reset clears generation state.

No daily, weekly, monthly, or world-country iteration is used.

## Politics and permanent routes

The provisional state starts under Friedrich Hoffmann with elections suspended
until the founding settlement selects one of four accepted routes.

| Route | Permanent government | Ruling family | Identity idea |
| --- | --- | --- | --- |
| Constitutional | Saar Constitutional Charter Coalition | democratic | `ajx_constitutional_municipal_charter` |
| Popular / labor | Saar Congress of Mine, Rail, and Factory Councils | communism | `ajx_saar_labor_compact` |
| Patron-client | Saar Industrial Guarantee Board | neutrality | `ajx_patron_industrial_mandate` |
| Neutral commission | Saar Municipal Neutral Commission | neutrality | `ajx_municipal_neutral_commission` |

Traditional restoration, emergency military government, and Radical
Sovereignty are not exposed. The neutral route has its own enum value, route
flag, selection proof, focus settlement, government installer, idea, AI branch,
localisation, and durable-sovereignty closure flag. It is not an alias for any
of the rejected shared routes.

## Lifecycle and power struggle

Two player-visible values begin at `30` and stabilize at `60`:

- Industrial Continuity measures working mines, wagons, power, and contracts;
- Neutrality Credibility measures whether border, patron, and security policy
  is accepted as independent rather than improvised or externally dictated.

Until both values reach the stable threshold, AJX carries
`ajx_exposed_saar_industrial_compact`. Reaching the threshold swaps it for
`ajx_balanced_saar_industrial_compact` and safely resolves the `480`-day
founding mission. Timeout or loss of the capital applies the package failure
transaction and records failure.

The shared power-struggle lane uses the AJX-specific
`municipal_commission_vs_industrial_security` type. The player-visible balance
starts at `50`; lower values favor the Municipal Commission and higher values
favor the Industrial Security Companies. The generic focus outcomes retain
their normal one-shot closure, while scripted localisation supplies the two
Saar identities.

## Decisions and costs

The Saar Compact category shows both lifecycle values and the internal balance.
All player-started actions use shared Event 006 cost proofs and payment effects;
only the automatic founding mission has no player cost.

- Administration: restore mine and rail dispatch; seat constitutional, labor,
  or neutral-commission government.
- Security: register and subordinate the factory security companies.
- Diplomacy: open the cross-border trade desk, settle former-host ledgers,
  accept the patron mandate, balance registered patron contracts, survey the
  Rhenish corridor, and charter network coal transit.
- Strategic: codify durable independence and convene the Rhenish congress.

Timed actions serialize through
`has_independence_wave_ajx_active_package_project`. Cancellation on package
loss, capital loss, war with the former host, or network exit is explicit where
relevant and uses the package failure transaction.

Former-host settlement writes only through the dynamic bilateral ledger. It
does not assume that Germany, France, or any other fixed tag is the host.
Patron balancing iterates only the country's bounded aligned patron ledger.

## Focus integration

AJX receives the complete shared Event 006 tree plus ten package focuses.

The permanent neutral settlement contains:

- Appoint the Neutral Commission;
- Codify Municipal Neutrality;
- Bind Security to the Commission;
- Entrench the Neutral Commission.

The country branch contains:

- Keep the Mines Breathing — survival;
- Charter the Coal and Rail Authority — economy and infrastructure;
- Screen the Industrial Security Companies — security;
- Open the Cross-Border Trade Desk — diplomacy;
- Settle the Saar Accounts — former-host policy;
- Send the Rhenish League Delegation — network and FORM-04 ambition.

The branch adds no repeated dust grants, equipment loops, or unit-creation
loops. Its rewards use the lifecycle values, existing public-value effects, one
infrastructure improvement, and bounded flags. The neutral settlement's final
flag is part of the shared durable-sovereignty closure proof.

## FORM-04 hooks

AJX selects and registers `independence_wave_formable_family.rhine_federation`,
sets `independence_wave_ajx_form04_candidate` and the shared Rhine-corridor
ambition, exposes a corridor survey, readies a Rhenish League delegation, and
can run the shared FORM-04 preparation transaction through its custom congress.
The congress builds the frozen invitation/member ledgers and resolves the vote;
only a shared `transaction_ready` result grants the AJX congress reward. The
separate shared proclamation action then revalidates the vote, charges the
selected-method costs, and atomically applies the audited `RLX` identity and
integration adapters. It also has a network coal-transit project.

The shared reservation blocks AJX and RHI only inside one incident, so later
repeatable waves can establish both founders for the approved Rhenish League
direction. FORM-04 passed its post-transaction operational re-audit and exact
readiness promotion. That family result does not admit IW-010 to automatic waves
or SCN-008; country-package admission remains a separate fail-closed gate.

## AI behavior

Every strategy is locked to `original_tag = AJX` and the exact setup/package
flags. AJX prioritizes an infantry force with support equipment and artillery,
arms production, civilian industry, and infrastructure. It avoids starting wars
through the founding period and under constitutional, labor, patron, and neutral
settlements. Severe threat reads the dynamic former-host ledger and adds army
and bunker priority without assuming a fixed host tag.

## Visual assets and sprite wiring

### Required and wired

| Surface | Runtime asset | Registration / consumer |
| --- | --- | --- |
| National flag | `gfx/flags/AJX.tga` | HOI4 flag path discovery |
| Medium flag | `gfx/flags/medium/AJX.tga` | HOI4 flag path discovery |
| Small flag | `gfx/flags/small/AJX.tga` | HOI4 flag path discovery |
| Friedrich Hoffmann | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` | `GFX_portrait_AJX_friedrich_hoffmann` in `interface/006_independence_wave_region_01_portraits.gfx` |
| Karl Becker large | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` | `GFX_portrait_AJX_karl_becker` in the same `.gfx` file |
| Karl Becker small | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner_small.dds` | `GFX_portrait_AJX_karl_becker_small`; army portrait only |
| Mine and Rail Dispatch Superintendent | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds` | `GFX_portrait_advisor_AJX_independence_wave_mine_rail_dispatch_superintendent` in `interface/006_independence_wave_region_01_portraits.gfx` |
| Cross-Border Accounts Comptroller | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds` | `GFX_portrait_advisor_AJX_independence_wave_cross_border_accounts_comptroller` in the same `.gfx` file |
| Factory Security Inspector | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds` | `GFX_portrait_advisor_AJX_independence_wave_factory_security_inspector` in the same `.gfx` file |
| Municipal Neutral Commission focus | `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds` | base and shine in `interface/006_independence_wave.gfx`; base consumed by `independence_wave_ajx_appoint_neutral_commission_focus` |

The character sprites are consumed by
`common/characters/006_independence_wave_saar_characters.txt`. The installed
portrait hashes are checked against
`docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/portrait_package_hashes.sha256`;
the flag hashes remain checked against `generated_nwe_hashes.sha256`.

### Reused Event 006 icons

The decisions and focuses use already registered Event 006 sprites:

- `GFX_decision_independence_wave_government_actions`;
- `GFX_decision_independence_wave_integration_missions`;
- `GFX_decision_independence_wave_army_integration_actions`;
- `GFX_decision_independence_wave_former_host_negotiations`;
- `GFX_decision_independence_wave_formable_proclamation`;
- `GFX_decision_independence_wave_league_votes`;
- `GFX_goal_independence_wave_founding_administration`;
- `GFX_goal_independence_wave_infrastructure_authority`;
- `GFX_goal_independence_wave_army_integration`;
- `GFX_goal_independence_wave_recognition_diplomacy`;
- `GFX_goal_independence_wave_former_host_settlement`;
- `GFX_goal_independence_wave_regional_formable`.

No placeholder icon is counted as completed art. A distinct Municipal Neutral
Commission focus icon and three independently composed advisor dossiers are
installed as runtime DDS files and documented in
`docs/assets/006_independence_wave/ajx_asset_completion_2026_07_15/manifest.md`.
The verified handles are:

- `GFX_goal_independence_wave_ajx_neutral_commission` at
  `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds`;
- `GFX_portrait_advisor_AJX_independence_wave_mine_rail_dispatch_superintendent`;
- `GFX_portrait_advisor_AJX_independence_wave_cross_border_accounts_comptroller`;
- `GFX_portrait_advisor_AJX_independence_wave_factory_security_inspector`.

The three character records consume the matching advisor handles, carry the
approved gender metadata, have role-title localisation, and are recruited by
the Event 006 setup event. The focus base and shine handles are registered; the
base handle identifies the neutral-commission entry focus while its three
  follow-up nodes retain their specific shared icons. The commander's separately
  composed `65x67` army dossier remains army-only and is not used by any advisor
  card. Its runtime SHA-256 is
  `470C29FD6CC73F5B6A269969160F1F4D721F31D4197F3D070C8388765F269312`.

## Implementation files

- `common/script_constants/006_independence_wave_saar_constants.txt`
- `common/characters/006_independence_wave_saar_characters.txt`
- `common/ideas/006_independence_wave_saar_ideas.txt`
- `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_saar_package_effects.txt`
- `common/decisions/categories/006_independence_wave_saar_categories.txt`
- `common/decisions/006_independence_wave_saar_decisions.txt`
- `common/ai_strategy/006_independence_wave_saar.txt`
- `localisation/english/006_independence_wave_saar_l_english.yml`
- `history/countries/AJX - Event 006 Country Shell.txt`
- shared route, focus, dispatch, scripted-localisation, and portrait registries

## References used

The implementation was checked against the offline wiki pages for data
structures, scopes, triggers, effects, modifiers, localisation, events,
decisions, ideas, AI, country creation, divisions, portraits, and national
focuses. Official vanilla documentation was used for script constants,
effects, triggers, characters, decisions, AI, and localisation formatters.
Vanilla precedents include Assyria's history character recruitment,
Afghanistan's timed mission structure, Brazil's mutually exclusive focus
branches, and Argentina's origin-gated AI strategy.

## Readiness blockers and future plans

- Runtime content attestation and SCN-008 preflight remain fail-closed by
  contract. The adapter and exact tag identity are present, but AJX is not
  listed in either readiness registry.
- FORM-04 identity, consent, integration, rollback construction, and
  military-settlement adapters have passed their separate operational audit and
  readiness promotion. Their status does not substitute for an IW-010 package
  admission audit.
- The three advisor dossiers and distinct neutral-commission focus art are
  produced, installed, hash-validated, registered, and consumed by the live
  parent-owned records. No AJX asset-integration blocker remains, and no
  generic, placeholder, leader-crop, or army-thumbnail substitute is used.

After those contracts are resolved, useful extensions would be patron-specific
coal contracts, former-host-dependent border prose, a negotiated Saar/Rhine
customs board, and event reactions to the commission-versus-security power
settlement. They are future depth, not substitutes for the implemented package.
