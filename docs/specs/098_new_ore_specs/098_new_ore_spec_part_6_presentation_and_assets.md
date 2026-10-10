# New Ore, part 6: Presentation, text direction, and assets

## A readable territorial mechanic

Use an ordinary decision category with concise text, two aggregate values, targeted decisions, native state highlighting, and an eligible static category picture. The category remains useful when no action is currently available because it explains the country's current armor access and source commitments.

The category picture depicts the mineral and protective alloy in a period industrial setting. It is decorative art. It contains no painted controls, numbers, meters, country names, or state borders. Current information remains native text and ordinary targeted records.

The selected deposit is the organizing context for practical actions. The player can locate the original source, inspect another known deposit, approach its current controller, or manage a contract. Sorting places the selected state and urgent active commitments first, then controlled sources, contracted sources, and other known deposits. The player can reach every valid source without an arbitrary permanent top-three target restriction.

AI has the full valid target set and does not depend on a human selection variable. Changing the selected state cannot change a pending contract's stored source or the target of a delivered demand.

## Information placement

| Surface | Information to show | Direction and constraints |
| --- | --- | --- |
| Decision category header | Current effective Event 098 armor advantage and directly controlled deposit count | Two consistent values with units, icon identity, and plain causal explanation |
| Selected-state record | State, current controller, original-source status, current grade, available agreement families | Actual current information, with native state location and highlight |
| Active agreement record | Supplier, physical source, recipient, term, current benefit, qualification, buyback or expiry | Exact named commitments, no hidden ranking score |
| Country idea or modifier tooltip | Direct or foreign access, effective armor contribution, relevant source count, gain/loss cause | The active source is clear and does not suggest permanently imbued exported equipment |
| State marker | Ore identity, current controller entitlement, geological persistence | Consumer-specific icon and readable tooltip |
| Offer and confirmation | Exact terms, payment, source, duration, termination rule, counterparties | No unmentioned debit or misleading stale price |
| Demand response | Named deposit, proposed terms, reply deadline, possible preparation after refusal | Describe the actual diplomatic choice and possible consequences |
| Active defense mission | Named state, deadline, continuous-control requirement, actual success and failure outcomes | Native timer matches the stored date, objective completes automatically |
| Event Details | Premise of the material, territorial importance, and current publicly revealed development | Descriptive premise, with numerical effects kept in their proper mechanical surfaces |
| Event Log | Real discovery and evolution history, actual actor where present, actual dates | Historical entries keep their original actor, current state information remains separate |
| Global news | First discovery, significant new suppliers, and material milestones | Country and state names are dynamic, future hidden outcomes are not advertised |

When several transfers occur in one battle or peace resolution, keep mechanical updates immediate and consolidate repetitive presentation. A former controller and a new controller receive their own relevant change report. Other players receive concise strategically meaningful news rather than every internal reconciliation.

## Required display states

The presentation must distinguish a direct controller, a foreign customer, a country with direct access and a redundant paid backup, a country without access, an invalid or changed supplier, an expired offer, an active demand, and a deposit without a valid controller.

A country losing its last source sees the resulting weaker agreement or zero access immediately. A country retaining another source sees the reduced deposit count and any changed Super-Alloy contribution. The source state must remain findable after a different country takes it.

Blocked actions explain the material missing condition. Use equipment and XP icons for costs, a controller identity for changed control, explicit relation information for an invalid security commitment, and a date for expiry. Never rely on color alone. Numbers use the project's formatting and distinguish whole equipment units from fractional percentage calculations.

## Writing direction

| Text family | Viewpoint and visible information | Tone and variation | Dynamic information |
| --- | --- | --- | --- |
| Original controller report | Local discovery and practical protective behavior | Surprise turning into calculation, with restrained pride or acquisitive humor depending on government | State, controller, current access grade |
| Initial world news | A newly important material and identifiable territory | Documentary attention to the material's observed usefulness and sudden strategic value | State, controller, publicly known application |
| Deep Vein report | Further excavation and stronger usable alloy | Confidence about abundant supply, unease about the attention it attracts | Original state, current controller, affected users |
| Rival discovery news | Another country now has its own source | Changed bargaining power, relief among customers, disappointment for a monopolist | New state, new controller, whether independent supply has appeared |
| Transfer report | The source changed hands and national access changed with it | Practical urgency for the loser, cautious opportunity for the winner | State, old and new controllers, resulting actual benefit |
| Commercial options | A supplier or buyer comparing a concrete bargain | Negotiating confidence, acquisitiveness, dry understatement | Exact compensation, term, partner and source |
| Security options | A government trading access for actual protection or a useful concession | Determination, uneasy dependence, or a partner's measured reassurance | Required guarantee or access commitment and parties |
| Faction options | A controller choosing which allied army to strengthen | Solidarity, military pragmatism, or disagreement over priorities | Actual selected ally and physical source |
| Demand options | A capable country pressing a denied interest, and the supplier responding | Firm political language, restrained contempt or resolve where fitting | Deposit, terms, expiry and likely military consequence |
| Defense objective | The country committing attention and forces to a prized territory | Specific military purpose and the cost of losing the material | State, threat, continuous-control period |
| Achievement text | A difficult accomplishment expressed without internal implementation detail | Distinctive title direction and concise truthful condition summary | Required event state and relevant visible outcomes |

Government and cultural variations should change voice without hardcoding which country deserves the deposit. An armored monarchy, revolutionary government, liberal trading power, or military regime can interpret the same discovery differently. Use sourced period idioms if a cultural allusion is desired. No unresearched quotation, slogan, lyric, or sample button is supplied in this planning package.

Avoid a generic changed-map scene, a staff table, paperwork mystery, broadcasts, or officials denying a rumor as the emotional center. Material tests, excavation, protective surfaces, guarded entrances, transported alloy, and soldiers reassessing their equipment provide more specific imagery. Humor belongs in minor negotiations or confident reactions. Actual war and loss receive appropriate seriousness.

## The Super-Alloy reveal

The presentation reserves slot `119` in `super_event_visible` under the [central identifier ledger](../shared_identifier_registry.md) and its [machine-readable counterpart](../shared_identifier_registry.json).
The user-authorized parent allocation approves the presentation identity only, leaving final text, art, audio and runtime integration separate.
Recheck presentation occupancy, including constant-based selectors, before wiring and allocate any audio ID independently.

One global super-event marks the first materially present direct Super-Alloy armor capability. It shares the concrete-outcome receipt used by the +10 Chaos milestone. The evolution flag alone is insufficient. A direct controller must actually receive at least the +200% tier while possessing an applicable armor consumer in service or stock. A foreign-only +80% customer cannot trigger this reveal when all direct controllers lack applicable armor.

This is a public demonstration that the new alloy has fundamentally altered protection. It applies equally when the first operational user is a small country, a major power, or an unusual supported country. Country size does not retroactively bias the original discovery.

The super-event's role is a military-material breakthrough. The intended feeling is recognition of an extraordinary protective capability and the strategic danger of allowing its sources to concentrate. Its image centers on a visibly tested finished protective surface and the distinctive ore identity in a believable period setting.

Title, description, button remark, and main quote remain research and writing directions. The text researcher should investigate period science, military technology, fortification, confidence in protective systems, and the political price of strategic materials. It must verify any exact wording and attribution before producing final copy.

The audio researcher should seek one distinct, structured musical recording with measured industrial or martial tension and a credible historical tone. Prefer 60–120 seconds. Composition and recording rights must both permit use. Generated tones, texture beds, generic stingers, and unidentified reused audio cannot satisfy the final package. Exact track, quote, title and independent audio ID are selected through the later super-event workflow, using reserved presentation slot 119.

## Asset identity

The mineral is fictional. Use a consistent dark metallic stone with a restrained steel-blue crystalline seam. Finished alloy carries the same subdued signature in a dense protective surface. The art should suggest a useful material rather than a jewel, radioactive hazard, magical currency, futuristic computer component, or another game's named ore.

Generated event imagery follows 1936–1945 documentary composition. News is black and white. Report images use the repository's report treatment. There are no real named historical people in the required compositions. Figures, where useful, remain anonymous participants in fictional scenes.

Icons use original family-specific ImageGen subject art and the correct native alpha contract. A 32-pixel decision icon, 64-pixel idea icon, state modifier, and category icon each receive their own composition. Resizing one focus-style source across all families is not the production route.

## Asset coverage matrix

Paths below are proposed event-owned asset identities. Exact native consumers and final canvases must be checked against the matching reference family before production. This table describes requirements, not files already produced.

| Asset working key | Consumer and required variants | Target | Composition direction | Reference family |
| --- | --- | --- | --- | --- |
| `new_ore_state_deposit` | State marker, same durable geological identity through capture | Exact state-modifier consumer size, unresolved until inspected | Exposed mineral seam and compact protective plate, readable at native size | `icons/state_modifiers/` |
| `new_ore_direct_baseline` | Direct country advantage | 64×64 | Raw ore beside a strong plate, restrained metal colors | `icons/ideas/` |
| `new_ore_direct_deep` | Deep Vein direct advantage | 64×64 | Richer seam and visibly denser layered plate | `icons/ideas/` |
| `new_ore_direct_super` | Super-Alloy direct advantage, including count scaling | 64×64 | Finished distinctive alloy plate with extreme material confidence | `icons/ideas/` |
| `new_ore_foreign_baseline` | Foreign country advantage | 64×64 | A limited shipment with protective material | `icons/ideas/` |
| `new_ore_foreign_deep` | Deep Vein foreign advantage | 64×64 | Improved limited shipment, family-consistent composition | `icons/ideas/` |
| `new_ore_foreign_super` | Super-Alloy foreign advantage | 64×64 | Finished alloy shipment, visibly separate from direct possession | `icons/ideas/` |
| `new_ore_category` | Ordinary decision category icon | Exact category consumer size | Ore and protective plate as the system's compact identity | `icons/decision_categories/` |
| `new_ore_category_picture` | One eligible static category picture | 114×101 reference-family nominal, confirm active consumer | Period workbench, raw material and tested protective plate, no painted UI | `icons/decision_categories/pictures/` |
| `new_ore_inspect` | Source inspection decision | 32×32 | Magnifying glass and mineral fragment | `icons/decisions/` |
| `new_ore_request` | Request allocation decision | 32×32 | Inward material crate and simple seal | `icons/decisions/` |
| `new_ore_offer` | Offer allocation decision | 32×32 | Outward material crate and simple seal | `icons/decisions/` |
| `new_ore_terms` | Respond and confirm terms | 32×32 | Two compatible industrial pieces joined by a clasp | `icons/decisions/` |
| `new_ore_renew` | Renewal decision | 32×32 | Replenished shipment and a durable link | `icons/decisions/` |
| `new_ore_buyback` | Supplier buyback | 32×32 | Returned equipment and closed allocation seal | `icons/decisions/` |
| `new_ore_abandon` | Recipient abandonment | 32×32 | Open clasp and an unused shipment place | `icons/decisions/` |
| `new_ore_reassign` | Consensual source reassignment | 32×32 | Two mineral pieces with one active connection | `icons/decisions/` |
| `new_ore_demand` | Ore access demand | 32×32 | Firm gauntlet over a material seal | `icons/decisions/` |
| `new_ore_prepare` | Preparation after refusal | 32×32 | Military objective pennant and an ore motif | `icons/decisions/` |
| `new_ore_withdraw` | Abandon ore dispute | 32×32 | Folded objective pennant and released seal | `icons/decisions/` |
| `new_ore_defend` | Start source-defense objective | 32×32 | Protective works around a mineral fragment | `icons/decisions/` |
| `new_ore_hold_source` | Active source-defense mission | 32×32 with inspected mission treatment | Guarded entrance and protective barrier | `icons/missions/` |
| `new_ore_news_discovery` | Initial global discovery news | 397×153 black and white | Field extraction and a concrete protective material test | `event_art/news/` |
| `new_ore_news_new_supplier` | Subsequent material discovery news family | 397×153 black and white | Fresh excavation in a geographically neutral setting | `event_art/news/` |
| `new_ore_report_discovery` | First controller report | 210×176 | Close material inspection with period testing equipment | `event_art/report/` |
| `new_ore_report_deep` | Deep Vein report | 210×176 | Rich exposed vein within an excavation | `event_art/report/` |
| `new_ore_report_control` | Loss, capture, and recovered-source reports | 210×176 | A guarded mine entrance and armored presence, no painted national identity | `event_art/report/` |
| `new_ore_report_agreement` | Commercial, security, and faction agreement report family | 210×176 | Material and practical equipment prepared for transfer | `event_art/report/` |
| `new_ore_super_alloy_reveal` | One global Super-Alloy super-event | 457×328 | Finished protective alloy with visible test damage that establishes exceptional resilience | `event_art/super_event/` and live super-event consumer |
| Eight achievement IDs in part 7 | Each needs completed, grey, and not-eligible states | 64×64 each | Original motif specified per achievement | `icons/achievements/` and `icons/achievements/template/overlay.png` |

## Production and review requirements

The asset handoff names the canonical reference root `.claude/skills/chaos-redux-event-assets/assets/gfx_references/` and the consumer-specific families above. The original planning repository connection did not expose the requested reference shelf. The later asset worker must inspect the installed shelf and exact consuming definitions before choosing unresolved sizes or producing final art.

For the category picture, require a labeled reference contact sheet.
If missing, retain review-only contact-sheet evidence from the actual reference images in the assigned Event 098 workspace, with filenames, native dimensions and provenance.
Updating the shared shelf's contact sheet, README or CATALOG requires an exact parent-owned maintenance assignment naming the files, or routing to `chaosx_skill_maintainer`.
This ownership clarification introduces no additional user approval gate or art fallback.
The shelf and contact sheet remain review material, and final runtime paths remain event-owned.

The completed achievement subject is generated first. Its grey and not-eligible variants use the approved deterministic template workflow, retaining the exact required overlay. Other transparent icon families request native transparent backgrounds in the initial generation and preserve alpha through conversion.

Final acceptance checks logical requirement, registered sprite alias, actual consumed runtime path, source provenance, native-size appearance, and every required state. A generated image alone is not a wired asset. Counts do not compensate for missing state-marker or achievement coverage.

The image, text, quote, audio, settings-aware playback, sprite selector, and reserved presentation slot 119 of the Super-Alloy reveal must all agree. The coding parent owns the final shared-framework integration and verifies the actual image getter as well as the text and audio.
