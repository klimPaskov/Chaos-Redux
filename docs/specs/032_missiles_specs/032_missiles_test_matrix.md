# Event 32 test matrix

## Testing boundary

This file defines the required test cases.

It does not claim that the cases have been run.

Autonomous live testing requires explicit invocation of the Chaos Redux debug-playtest skill. Normal implementation agents must not claim in-game verification from static inspection.

## Static source and MCP tests

| ID | Surface | Test | Expected |
| --- | --- | --- | --- |
| `STATIC-01` | Event chain | Inspect `chaosx.nr32` chain | Stable IDs, no missing calls, no duplicate entry |
| `STATIC-02` | Event graph | Render baseline and evolution chain | Entry, reports, incidents, warnings, and cleanup are connected |
| `STATIC-03` | Event compare | Compare legacy and rework | Legacy blanket grant removed, Event 16 bridge preserved |
| `STATIC-04` | Technology | Inspect normalized graph | Every stage maps to valid installed technology |
| `STATIC-05` | Technology | Render affected folder | Prerequisites and exclusivity remain valid |
| `STATIC-06` | Technology | Compare final source | One-step grant and mature package match design |
| `STATIC-07` | Probability | Run full scenario matrix | Expected ordering and blockers pass |
| `STATIC-08` | Decisions | Audit costs and visibility | Four-cost limit, phase budget, cleanup |
| `STATIC-09` | Localisation | Audit keys and dynamic text | No missing or raw keys |
| `STATIC-10` | Assets | Audit sprites and DDS paths | No missing or placeholder art |
| `STATIC-11` | Scenario | Inspect registry | SCN-015 collision-free and fully wired |
| `STATIC-12` | Docs | Compare specs, event doc, workbook | Player-facing fields agree |

## Baseline global firing

### `BASE-01`: First firing in an ordinary world

Setup:

- fresh campaign
- several majors, minors, subjects, and one-state countries
- no Event 32 program
- Calm World
- evolutions disabled for isolation

Verify:

- one global history row
- every valid recipient receives one stage
- every valid recipient receives reserve
- every valid recipient receives one site
- humans receive reports
- AI does not receive blocking popups
- first global news appears once
- Event 16 bridge fires only for the current valid host
- no special payload or evolution content appears

### `BASE-02`: Repeat firing

Setup:

- Event 32 fired once
- mixed technology stages
- some damaged sites
- some mature programs
- evolutions disabled

Verify:

- one next stage per country
- mature programs get mature package
- damaged site receives priority
- existing site upgrades before new site
- reserve increases within cap
- readiness recovery is bounded
- no global news repeat
- one new history row
- repeatable cap and recovery update once

### `BASE-03`: Mixed recipient validity

Include:

- ordinary major
- subject
- one-state minor
- landless government in exile
- temporary revolt
- system carrier
- organized special actor
- nonindustrial special actor

Verify exact accepted, deferred, and skipped results.

### `BASE-04`: No valid recipient

Setup a controlled test where no recipient passes.

Verify:

- Event list shows `N/A`
- automatic selection does not queue the event
- force trigger returns a clear setup failure
- no history row or partial mutation

## Site selection

### `SITE-LIVE-01`: Interior site beats capital

Create:

- protected interior core
- exposed capital
- occupied industry state

Verify selected site and score explanation.

### `SITE-LIVE-02`: One-state minor

Verify the sole valid state receives the site.

### `SITE-LIVE-03`: Secondary redundancy

Verify:

- another strategic region is preferred
- site cap is enforced
- existing site still upgrades first when capacity need is absent

### `SITE-LIVE-04`: Damaged and captured sites

Verify:

- damaged owned site can be repaired
- captured compromised site cannot launch
- former owner loses capacity
- new controller receives resolution actions

## Technology

### `TECH-01`: No technology

Receives first supported step.

### `TECH-02`: Mid-line

Receives exact next valid step.

### `TECH-03`: Later technology already researched

Normalized stage rises before grant.

### `TECH-04`: Full line

Receives mature package, no invalid technology.

### `TECH-05`: DLC variant

Verify exact installed DLC graph.

### `TECH-06`: No-DLC variant

Verify usable operation adapter and complete program.

## Reserve and accounting

### `RES-01`: Replenishment

Verify costs, batch size, cooldown, cap, and AI floor.

### `RES-02`: Operation reservation

Prepare one strike, then attempt another.

Verify reserved missiles cannot be reused.

### `RES-03`: Cancel before commitment

Verify correct refund and readiness cost.

### `RES-04`: Abort after commitment

Verify partial or full consumption according to rules.

### `RES-05`: Capture transfer

Verify exact debit and credit.

### `RES-06`: Civil-war split

Verify total reserve is conserved and no duplicate appears.

## Conventional operations

### `OP-01`: Precision logistics strike

Verify:

- exact state
- supply target
- low reserve cost
- lower collateral
- readiness loss
- cooldown
- one incident record

### `OP-02`: Strategic industrial barrage

Verify:

- several real building levels damaged
- damage clamps
- deaths use shared API
- target receives report
- actor and attribution correct

### `OP-03`: Counterforce strike

Verify launch-site damage and hardening.

### `OP-04`: Target invalidation

End war or transfer state during preparation.

Verify clean abort and resource rule.

### `OP-05`: Reach failure

Select an out-of-range state.

Verify preparation is blocked with exact reason.

### `OP-06`: No valid target object

Verify no empty-target operation.

## Saturation Arsenals

### `SAT-01`: Unlock and log

Verify tier, MTTH path, evolution row, decisions, and AI.

### `SAT-02`: Large barrage

Verify capacity, reserve, defense saturation, readiness loss, cooldown, and aggregate failure model.

### `SAT-03`: Site cap

Verify no unlimited site creation.

### `SAT-04`: AI reserve floor

Verify AI does not spend every missile on low-value targets.

### `SAT-05`: Disabled evolution

Verify no saturation flag, row, decision, or AI modifier.

## Unreliable Guidance

### `GUIDE-LIVE-01`: High-quality precision

Verify high on-target rate over a bounded seeded test set.

### `GUIDE-LIVE-02`: Damaged long-range barrage

Verify degraded and failure outcomes rise.

### `GUIDE-LIVE-03`: Wrong-state pool

Verify every alternative state belongs to the frozen bounded pool.

### `GUIDE-LIVE-04`: Neutral accident

Verify actual neutral damage, diplomacy, deaths, and response.

### `GUIDE-LIVE-05`: Self-strike

Verify actor state, site damage, and no victim misattribution.

### `GUIDE-LIVE-06`: Special payload dud

Verify no confirmed use when release did not occur.

### `GUIDE-LIVE-07`: Maintenance investment

Verify measurable probability improvement.

### `GUIDE-LIVE-08`: Disabled evolution

Verify baseline failure table remains.

## Special Warheads

### `PAYLOAD-01`: Chemical

Verify exact agent, stockpile debit, missile debit, target state, contamination, evidence, condemnation, deaths, and Air Cleanliness once.

### `PAYLOAD-02`: Biological

Verify exact agent, outbreak pipeline, stockpile debit, and no duplicate spread logic.

### `PAYLOAD-03`: Nuclear from Event 23 stockpile

Verify Soviet payload stockpile remains Event 23 owned and Event 32 consumes delivery resources.

### `PAYLOAD-04`: Thermonuclear

Verify shared stronger effects and no Event 32 terminal flag.

### `PAYLOAD-05`: Missing payload

Verify option unavailable.

### `PAYLOAD-06`: Captured payload

Verify physical custody.

### `PAYLOAD-07`: Disabled evolution

Verify no integration or launch.

## Rogue Launch Commands

### `ROGUE-LIVE-01`: Stable secure program

Advance time through bounded test period.

Verify no incident spam.

### `ROGUE-LIVE-02`: Civil-war crisis

Verify sites, reserve, control, and immediate actions.

### `ROGUE-LIVE-03`: Unauthorized launch countdown

Verify code rotation, isolation, negotiation, assault, and commitment behavior in separate checkpoints.

### `ROGUE-LIVE-04`: Mutiny and recapture

Verify site and reserve accounting.

### `ROGUE-LIVE-05`: Foreign bribery

Verify real actor, access, evidence, and discovery.

### `ROGUE-LIVE-06`: No foreign actor

Verify foreign incident cannot occur.

### `ROGUE-LIVE-07`: Special-payload custody

Verify no payload invention.

### `ROGUE-LIVE-08`: Incident cap

Verify one ordinary crisis per country and global cap.

### `ROGUE-LIVE-09`: Disabled evolution

Verify no rogue logic remains available.

## Automatic Retaliation

### `AUTO-01`: Supervised verified warning

Verify player event, response window, exact attacker, and deliberate launch or stand-down.

### `AUTO-02`: Supervised uncertain warning

Verify verification is available and no immediate launch.

### `AUTO-03`: Delegated warning

Verify prepared response, shorter window, and stop actions.

### `AUTO-04`: Automatic warning

Verify countdown, minimum control gate, and commitment.

### `AUTO-05`: False warning exposed

Verify stand-down and no launch.

### `AUTO-06`: Forged signal

Verify valid foreign actor and attribution change.

### `AUTO-07`: Compromised site

Verify isolate action.

### `AUTO-08`: Chain reaction

Verify linked incident IDs, generations, participant cap, and closure.

### `AUTO-09`: Duplicate root

Verify one response per country.

### `AUTO-10`: Cap reached

Verify chain stops.

### `AUTO-11`: No site or reserve

Verify no virtual launch.

### `AUTO-12`: Fallout connection

Create enough real thermonuclear consequences to satisfy shared conditions.

Verify Fallout owns the transition and Event 32 sets no terminal flag.

### `AUTO-13`: Disabled evolution

Verify no posture or warning actions.

## Cross-event tests

### `BRIDGE-05`: Soviet Collapse

Verify site and reserve allocation to successors.

### `BRIDGE-06`: Independence Wave

Verify inherited site setup and no universal free program.

### `BRIDGE-13`: Natural disaster

Verify site damage adapter.

### `BRIDGE-16`: Brilliant Scientist

Verify one Event 16 reaction receipt.

### `BRIDGE-21`: Civil war

Verify split helper.

### `BRIDGE-23`: Soviet nuclear missiles

Verify dual stockpile payment and ownership boundaries.

### `BRIDGE-76`: Weapons test

Verify bridge only after Event 76 implementation supports it.

## SCN-015 tests

### `SCN-01`: Registry and selection

Verify sort, name, detail, type, intensity, confirmation, cancel, and launch enablement.

### `SCN-02`: Global Proliferation at four intensities

Verify scaling and no unintended evolution.

### `SCN-03`: Saturation War at four intensities

Verify safe war preflight and belligerent-only saturation setup.

### `SCN-04`: Command Breakdown at four intensities

Verify affected share, control, readiness, and incident cap.

### `SCN-05`: Special Payload Crisis

Verify availability only with payload owner and no payload grant.

### `SCN-06`: Retaliation Network

Verify Low has no immediate destructive incident and Maximum remains bounded.

### `SCN-07`: Atomic preflight

Force a setup failure and verify zero partial mutation.

### `SCN-08`: Repeat launch

Verify idempotence or clear block.

### `SCN-09`: Save and reload

Verify program and scenario state persists.

### `SCN-10`: Terminal conflict

Verify launch block where required.

### `SCN-11`: Registry collision and source contract

Verify the live shared registry contains Fallout at raw ID `14`, Missile Age at raw ID `15`, and the existing Global Jihad row at raw ID `16`, with one matching entry in each of the four sort views. Verify Event 031's current triggerable selector is aligned to Global Jihad at raw ID `16`; its separate world-end registry reservation remains raw ID `15` and is not the shared triggerable-scenario namespace.

Verify the shared selector, name, `#015` entry label, five profile labels and descriptions, four intensity impacts, eligibility bridge, dispatcher, setup receipt, duplicate guard, and bypass cleanup all reference the same SCN-015 identity.

This static case does not substitute for the parent-owned Event 032 core launch, save/reload, or live setup evidence.

## UI and text tests

- open and close category repeatedly
- verify phase changes
- verify header values
- verify texticons
- verify selected target cleanup
- verify exact state names
- verify no raw localisation keys
- verify no clipped category text
- verify Event Details premise
- verify five evolution rows
- verify scenario wording
- verify integer formatting
- verify achievement text

## Asset tests

At native size, inspect:

- report image
- news image
- category picture
- program idea
- state modifiers
- decision icons
- mission icons
- raid icons
- texticons
- achievement triplets

Check:

- correct path
- correct sprite
- dimensions
- transparency
- readability
- no white halo
- no opaque square
- no modern generated text
- no placeholder
- no unrelated reused icon

## Save and reload tests

Save and reload after:

- first program setup
- repeat firing
- prepared operation
- site capture
- site repair
- rogue crisis
- active warning
- retaliation chain
- scenario setup
- achievement progress

Verify:

- values persist
- selected targets clean or persist correctly
- no duplicate delayed event
- no lost reserve receipt
- no repeated history row
- no repeated evolution row
- no stale site pointer

## Long progression test

Run a bounded campaign with AI active.

Observe:

- repeatable Event 32 weight
- repeat firing
- technology progression
- replenishment
- launch frequency
- reserve floors
- site growth
- evolution pacing
- incident frequency
- warning chains
- decision spam
- popup spam
- performance
- invalid cleanup
- shared-system duplication

The final report should state the test duration, countries observed, evolutions active, launches, incidents, and unresolved limits.
