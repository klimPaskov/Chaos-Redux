# Event 006 IW-010 Saar country-package implementation handoff

> **Portrait-specific supersession (2026-07-16):** AJX fictional portrait
> hashes and visual acceptance in this handoff are superseded by the male-HOI4
> package manifest and final independent audit. Flag-ledger and gameplay
> findings remain historical within their stated scope.

Date: 2026-07-15

Implementer: `event6_ajx_package`

Scope: `IW-010` Saar (`AJX`) only, including its bounded shared-framework
wiring and the approved IW-008/IW-010 coexistence correction. No commit was
created; final review and commit ownership remain with the parent agent.

## Status

The bounded AJX gameplay package is implemented. It has exact setup and final
proofs, four accepted permanent routes, a distinct civilian Municipal Neutral
Commission route, lifecycle ideas and mission, visible values, costed
decisions, focus content, shared p10 starting forces, dynamic former-host and
patron behavior, FORM-04 carrier hooks, origin-aware AI, localisation, portrait
wiring, documentation, and cleanup.

This handoff does **not** attest IW-010 for automatic runtime content readiness
or SCN-008. Those gates remain fail-closed. The later FORM-04 operational
re-audit/readiness promotion and AJX asset-completion tranche close the older
external consumer and asset findings without opening package admission.

## Binding and coexistence contract

- Immutable package identity: `IW-010`, `AJX`, anchor/capital state `42`,
  Northern and Western Europe, standard territory depth, industrial-breakaway
  archetype.
- The setup proof requires a living dynamic former host that still owns its
  protected remnant state. No fixed German or French host is assumed.
- IW-008 and IW-010 both load reservation group `rg_rhine_saar`, and both plan
  triggers reject that group once it has been reserved inside the current
  incident. This prevents same-incident double selection.
- Runtime setup and prepared proofs do not test whether the other country is
  already active. The earlier active-AJX absence clauses were removed from the
  RHI initialization and prepared proofs. A later repeatable wave may therefore
  release the second country, supporting living RHI and AJX founders for the
  approved Rhenish League direction.
- Unique tag/anchor availability and current-plan reservation checks remain
  unchanged.

## Implemented package

### Country, politics, and characters

- The dormant AJX history installs `civilian_economy`, `export_focus`, and
  `volunteer_only`, then recruits two static fictional humans.
- Friedrich Hoffmann is the civilian municipal jurist and country leader for
  the constitutional, labor, patron, and neutral settlements.
- Karl Becker is a skill-3 industrial-security corps commander with no
  country-leader role. The neutral route is never described as a military or
  traditional government.
- Starting popularity is 40 democratic, 25 communist, 30 neutral, and 5
  fascist. Each permanent route installs a tuned 100-point distribution,
  route-specific party name, route idea, and appropriate Hoffmann role.

The four exact permanent routes are:

1. constitutional municipal charter;
2. popular/labor congress;
3. patron industrial mandate;
4. civilian Municipal Neutral Commission.

Traditional restoration, emergency military government, and Radical
Sovereignty remain unavailable. The neutral commission has its own route enum,
flag, route lock, focus lane, government installer, idea, AI condition,
localisation, and durable-sovereignty closure flag.

### Lifecycle, decisions, and balance

- Industrial Continuity and Neutrality Credibility begin at 30, are clamped to
  0..100, and mature at 60. The exposed lifecycle idea swaps to the balanced
  compact only when both values pass the exact threshold.
- The 480-day founding mission resolves safely at the threshold and records a
  failed compact on timeout or capital loss.
- The decision category exposes both lifecycle values and the shared
  Municipal Commission versus Industrial Security balance.
- The package contains one mission and thirteen decisions: mine/rail dispatch,
  security-company integration, cross-border trade, dynamic former-host
  settlement, four permanent-government installers, durable independence,
  bounded patron balancing, Rhenish corridor survey, formation congress, and
  network coal transit.
- Timed projects serialize through an AJX-only active-project proof. Costs use
  the shared administration, security, diplomatic, and strategic payment
  contracts; cancellation conditions apply package failure effects where
  relevant.
- A no-focus baseline path of mine/rail dispatch, security integration, and the
  trade desk reaches 75 Industrial Continuity and 70 Neutrality Credibility in
  375 serialized days, leaving 105 days inside the founding mission. Focus
  rewards can stabilize the compact earlier but are not required to rescue an
  impossible timer.
- Former-host changes write through the dynamic bilateral ledger. Patron
  balancing iterates only the country's bounded aligned-patron ledger. No
  daily, weekly, monthly, or world-country iteration was added.

### Focus and force content

- AJX receives the shared full Event 006 framework plus ten package focuses.
- Six country focuses cover survival, coal/rail administration, industrial
  security, cross-border diplomacy, former-host accounts, and the Rhenish
  delegation.
- Four mutually linked focuses create the distinct Municipal Neutral
  Commission settlement.
- Static inspection found no unit creation, division-template creation,
  equipment grant, repeated reward loop, or random-list reward in the ten AJX
  focuses.
- The shared p10 force row resolves to `industrial_security`, military
  tradition 50, no naval or air inheritance, and reinforcement mask 1349.
  That mask is exactly five pathways: integrate militias (1), secure depots
  (4), factory/rail guards (64), foreign arms (256), and capital/border defense
  (1024). The prepared proof requires all five positive flags and explicitly
  rejects the other six pathways.

### Diplomacy, FORM-04, AI, and cleanup

- AJX selects and registers the Rhine federation family, its AJX FORM-04
  candidate flag, and Rhine-corridor ambition.
- The corridor survey, delegation focus, custom preparation congress, and
  coal-transit project support the approved later-wave two-founder direction.
  The congress resolves the shared vote, rewards AJX only on
  `transaction_ready`, and leaves the audited FORM-04 commitment to the shared
  proclamation action.
- Five AI plans are locked to `original_tag = AJX` and the exact active
  package/setup facts. They prioritize infantry, support, artillery, arms
  production, infrastructure, and civilian industry; restrain founding and
  settled wars; and read the dynamic former-host threat for emergency army and
  bunker priority.
- Cleanup removes the mission, every AJX decision and idea, lifecycle values,
  route-government flags, AI flag, project flags, FORM-04 carrier flags, and
  package completion state before the shared generation reset clears common
  provenance.

## Files added

- `common/script_constants/006_independence_wave_saar_constants.txt`
- `common/characters/006_independence_wave_saar_characters.txt`
- `common/ideas/006_independence_wave_saar_ideas.txt`
- `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_saar_package_effects.txt`
- `common/decisions/categories/006_independence_wave_saar_categories.txt`
- `common/decisions/006_independence_wave_saar_decisions.txt`
- `common/ai_strategy/006_independence_wave_saar.txt`
- `localisation/english/006_independence_wave_saar_l_english.yml`
- `docs/events/006_independence_wave/northern_western_europe_packages.md`
- this handoff

## Existing files updated

- `history/countries/AJX - Event 006 Country Shell.txt`
- `interface/006_independence_wave_region_01_portraits.gfx`
- shared Event 006 route constants, route selection/reset, power-struggle
  registration/proofs/scripted localisation, focus tree, package dispatch,
  exact package identity, and durable-government proof files
- the RHI package proof file, solely to remove permanent active-AJX exclusion
- `docs/events/006_independence_wave.md`
- the Event 006 asset manifest, regeneration manifest/review, generated-art
  manifest/handoff, and regional portrait handoff

Unrelated working-tree changes were not edited or staged.

## Portrait and flag evidence

The following runtime files exist, have registered sprite consumers, and match
the authoritative ledgers:

| Runtime file | SHA-256 |
| --- | --- |
| `portrait_AJX_saar_municipal_neutral_commission.dds` | `53c80062db72b4b8d4696a3921351a0cc4771ec9918975bceb147a81ee00f976` |
| `portrait_AJX_saar_industrial_security_commissioner.dds` | `555ebb4619bf6a672b7edb96dab847cd3ff69b00fc4d6a53d6cff376556faf51` |
| `portrait_AJX_saar_industrial_security_commissioner_small.dds` | `470c29fd6cc73f5b6a269969160f1f4d721f31d4197f3d070c8388765f269312` |
| `gfx/flags/AJX.tga` | `be622a9d8cf12435cf055ae7d59278081975eecfc05a2787a056e1d096810a4c` |
| `gfx/flags/medium/AJX.tga` | `ffb75c4a42b8d6255a2d8f365963ad3da675da91dc7baa15b3e40d967a967772` |
| `gfx/flags/small/AJX.tga` | `9ece1cfa8e6c3f5e61ba6e6e59920c2a843a10751055309b5b8bc9b12d868b6f` |

The portrait hashes match
`portrait_regeneration_2026_07_15/portrait_package_hashes.sha256`. The flag
triplet matches `generated_nwe_hashes.sha256`; that older ledger is explicitly
historical and is not used to attest the regenerated portrait binaries.

## Targeted validation evidence

- Balanced-brace and unsupported-operator inspection passed across 22 touched
  gameplay/shared-wiring files.
- All 104 expected AJX player-visible character, idea, category, decision,
  focus, tooltip, party, and power-center keys resolve; the AJX localisation
  contains no duplicate keys and remains UTF-8 with BOM.
- Definition scans covered 71 AJX effect, trigger, AI, decision, and focus
  identifiers and found no duplicate definitions.
- All 55 scripted effect/trigger calls resolve, and all 76 referenced script
  constants resolve to declared category keys.
- All 18 portrait/shared decision/focus/idea sprite names resolve in the
  interface registry, and all six AJX portrait/flag runtime assets exist.
- The ten AJX focus IDs and their coordinate pairs are unique inside the tree.
- Runtime dispatcher setup/final-validation/cleanup calls and the exact
  IW-010/AJX identity branch are present.
- IW-010 is absent from the runtime content-attestation body and the SCN-008
  scenario-preflight body. Both AJX and RHI package proofs contain zero active
  other-tag absence clauses.
- Targeted tracked-file diff checking found no whitespace errors. The HOI4 MCP
  inspection family was not exposed in this agent session, so no MCP render or
  runtime attestation is claimed.

## Simplifications, omissions, and blockers

1. Runtime content attestation remains closed for IW-010.
2. SCN-008 package preflight remains closed for IW-010.
3. FORM-04 has passed its separate operational re-audit and readiness
   promotion; that family certification does not certify IW-010 admission.
4. The three advisor dossiers, advisor records, distinct Municipal Neutral
   Commission focus icon, and corrected `65x67` commander dossier are installed,
   registered, consumed, and covered by their completed asset ledgers.

No gameplay route, lifecycle transaction, cost contract, AI branch, opening
force proof, localisation surface, or cleanup item inside the accepted bounded
AJX package was simplified. Overall Event 006 completion and IW-010 readiness
are not claimed.

Skills used: `chaos-redux-events`, `hoi4-focus-trees`,
`hoi4-decisions-missions`, `chaos-redux-event-assets`,
`chaos-redux-subagents`, and `chaos-redux-improvement-loop`. No skill was
created or updated.
