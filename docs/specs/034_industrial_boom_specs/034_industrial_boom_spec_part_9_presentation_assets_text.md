# Industrial Boom specification, part 9: Presentation, assets, and text

## Presentation choice

The category is a simple decision category: concise header text with basic formatted values, the ordinary decision list, and one static category picture.
This follows the presentation hierarchy in the decision skill ([category presentation hierarchy](../../../.claude/skills/chaos-redux-decisions-missions/references/formables-and-category-presentation.md#decision-category-presentation-hierarchy)), which allows a picture only when the category has no meter or custom controls.
One public value, a trend word, a one-word reserve state and up to three region rows fit that surface, so no meter, inlay or scripted GUI is planned.

Earlier drafts asked for both a meter and phase pictures, which the hierarchy forbids together; this audit resolves the conflict in favor of the simple category (README, open questions).
A dedicated window would need a recorded finding that this surface cannot communicate the state, followed by acceptance and the event UI workflow.

## Category header

Three short lines, built with scripted localisation:

```text
Overheating: 47 (Strained), rising. At 70 the boom loses most of its extra output.
Main pressure: the rail network is overloaded. Reserve: held.
Landing outlook: uncertain. Finishing the Westfalen project would improve it.
```

Rules:

- The band name and trend are words with a texticon, never color alone.
- The leading cause is the largest driver from part 2, written as a concrete phrase.
- The landing line appears only in the Running and Landing states and names the single most useful next step.
- Region status (stage, protection, Miracle or Fragile) appears in each region row's tooltip, not in the header.

## Tooltips

| Surface | Shows | Never shows |
| --- | --- | --- |
| Overheating | What the value means, band, trend, next threshold, the leading cause and the action that addresses it | Driver weights, arithmetic, variable names |
| Region row | Profile, stage, protected or not, Miracle or Fragile, what slows progress, what converts at landing | Progress formula |
| Action | Cost, immediate direction, duration or cooldown, output or project tradeoff, any target state | Incident chances, AI weights, hidden evolution conditions |
| Landing forecast | Expected outcome, main reason, required objective, and that shocks can still change it | A false exact percentage |

Each tooltip stays within four short lines.

## Text direction

**Opening.** The government and industrial authorities, confident and practical: backlogs clearing, rail yards full, new shifts, the first named regions, and a hint of crowded systems without promising collapse.
Sample: "Order books that were full until 1940 are being cleared by spring. The yards around Essen run three shifts, and the ministries are already arguing over who gets the next trainload of steel."

**Band reports.** One per upward band entry.
Strained shows delays, missing inputs, overtime and crowded housing through workers and managers.
Dangerous is serious and specific: interrupted lines, unsafe conditions, failed works; no comedy around injury.
Critical is short and direct about the choice that remains.

**Landing reports.** Controlled names the regions and projects that stayed and the end of the extraordinary output, measured rather than triumphal.
Rough and forced are sober about cancelled orders, idle shifts and unfinished works.

**Crash report.** The same country as orders, credit and production fail at speed, naming the affected regions, with no formulas or stage numbers.
The depression text itself belongs to Event 35, which already selects source-aware prose for an inherited hard landing.

**Decisions.** Run the Economy Hot sounds deliberate, and more coercive in the Strained band; Stabilize Supply Chains is logistical; Build an Industrial Reserve is restrained; Cool the Expansion is serious, and resisted under Speculative Mania; region actions name the state.

Evolution tone is in part 5.
Avoid modern market slang, generic bubble lines, and claims that do not fit the target country.

The implemented opening text (`chaosx.nr34.2`, `chaosx.news.39`) and the visible title "Industrial BOOM!" are interim and are rewritten from this direction.

## Asset inventory

Register every sprite before requesting art so names do not change later.
The opening currently uses the vanilla `GFX_report_event_airplane_factory`.

| Family | Assets |
| --- | --- |
| Report image | Opening report: a 1936 to 1945 factory hall or rail-linked complex at extraordinary pace, workers and machinery in front, crates, wagons, cranes and scaffolding showing volume and strain |
| Category | One static category picture (factory-to-rail industrial flow, busy and useful) and one category icon (factory with an overworked flywheel or gauge) |
| Decisions and missions | Run the Economy Hot, Stabilize Supply Chains, Build an Industrial Reserve, Cool the Expansion (also used by Impose Credit Restraint), Designate an Industrial Project, Protect an Industrial Region, Abandon a Project, Prepare a Controlled Landing, Prevent the Crash, Emergency Production Halt, Approve a Speculative Expansion, Declare a Miracle Region, Contain the Spread |
| Country effects | Industrial Boom, Speculative Mania, The Industrial Miracle, Runaway Industrialization, Export Orders (supplier contract), Reconversion, Industrial Exhaustion |
| State modifiers | Industrial Region, Protected Industrial Region, Secured Project, Fragile Miracle Region, Spreading Industry, Unfinished Works |
| Achievements | Triplets for the four unimplemented achievements in part 10; The Long Fall triplet already exists under `gfx/achievements/` |

Timed effects of Run the Economy Hot and Cool the Expansion reuse their decision icons.
Profile and Miracle form are named in the state modifier text and need no separate icons.

Art rules (owner skill `chaos-redux-event-assets`): period-accurate 1936 to 1945 subjects; no modern robotics, digital displays, high-visibility clothing, readable generated text, war rooms, maps or financial charts as subjects; the category picture contains no fake buttons or numbers; transparent icons keep native alpha; each family uses its own reference consumer and is never a resized copy of another family.
Generated scenes route to `chaosx_generated_event_art` and icons to `chaosx_icon_artist`; the [asset prompt](034_industrial_boom_asset_prompt.md) carries the production handoff.

## Accessibility

Bands and trends use words and texticons as well as color, protected and fragile markers use distinct symbols, and cost strings use matching texticons.
