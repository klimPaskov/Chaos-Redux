# Next reviewed Fallout tranche addendum: The County Fair Returns

Date: 2026-07-25

Status: accepted implementation addendum, promoted to source spec 55, and not release-floor credit while scheduler activation remains closed.

All event titles, option labels, asset identifiers, and catalogue wording in this addendum are working directions rather than final localisation.

## Disposition update: 2026-07-26

The parent-selected European `The River Ration League` tranche is complete.

This County Fair design is now the next implementation owner and is promoted to `docs/specs/air_cleanliness_fallout_specs/specs/55_reviewed_regional_county_fair_returns.md`.

The provisional events `565` through `571`, transaction `710053`, route `7153`, Event Log history `9158`, and catalogue identity `FALLOUT-565` remain owned by River Ration League.

County Fair is remapped to events `572` through `578`, transaction `710054`, route `7154`, Event Log history `9159`, and catalogue identity `FALLOUT-572`.

This disposition resolves the improvement-loop queue and preserves the accepted design as source spec 55.

## Recommendation

Implement the existing North American regional-matrix row `The County Fair Returns` as the next manually reviewed ordinary Fallout chain after Ashline Firebreak.

This is a bounded seven-block recovery chain about rural communities turning stable food, local security, repair work, and public memory into a seasonal institution.

It is useful expansion because the current reviewed library has many scarcity, hazard, command, death, and salvage incidents but no North American civic agricultural fair that brings several recovered rural states into one peaceful public institution.

It should not become a new decision category, recurring scheduler, bilateral trade system, focus route, successor package, character package, scripted GUI, achievement, super-event, or formable in this tranche.

## Improvement-loop cadence and non-duplication

The prior Ashline Firebreak tranche is implemented and reconciled in `specs/52_reviewed_regional_ashline_firebreak.md`, `ASHLINE_FIREBREAK_CHAIN_PROOF.md`, the scheduler proof, and the event-id ledger.

There is therefore no unresolved Ashline expansion layer blocking this pass.

`The County Fair Returns` remains a dormant candidate row in `matrices/fallout_regional_event_matrix.md` and is now implemented outside release-floor credit.

Repository searches found no gameplay, localisation, or reviewed-spec implementation under the county-fair working label.

The chain must remain distinct from the following implemented content:

| Existing chain | Existing ownership | County-fair boundary |
| --- | --- | --- |
| Year Zero, candidate `401` | National calendar identity and first-anniversary legitimacy | The fair does not choose the national calendar or redefine the post-collapse year. It may read durable calendar memory only to colour the seasonal callback. |
| The Orchard Flowers Once, candidate `408` | Recovery of one orchard and its first harvest | The fair requires prior agricultural stability and spends or exhibits surplus. It does not simulate crop recovery or rewrite orchard outcomes. |
| The Market Under the Viaduct, candidate `380` | Regulation of a permanent transport market | The trade-fair branch is a temporary regional exchange attached to a civic gathering. It does not create a bilateral market, merchant constitution, or permanent viaduct-market duplicate. |
| A New Funeral, candidate `541` | Ritual governance, burial policy, public health, and mourning law | The memorial-gathering branch creates a remembrance pavilion inside a fair. It does not settle funeral law or reopen the ritual-governance crisis. |
| The Ammunition Winter, candidate `534` | Emergency ammunition scarcity and coercive arms policy | The militia muster displays readiness and recruits volunteers. It does not manufacture ammunition or repeat private-arms seizure. |
| Ashline Firebreak, candidate `554` | Immediate wildfire and ash-hazard containment | The fair requires stable rural recovery and cannot target an active or unresolved Ashline aftermath state. |

## Research and North American identity

Agricultural fairs in the United States and Canada historically combined livestock and crop competition, machinery and craft display, agricultural education, entertainment, and community gathering.

The Library of Congress identifies livestock and agricultural competitions sponsored by agricultural societies and 4-H clubs as fixtures of state and county fairs.

The United States Cooperative Extension System was nationally organized through the 1914 Smith-Lever Act, while its roots lay in earlier agricultural clubs and societies.

Extension networks later connected county agents, land-grant institutions, farm families, youth clubs, production campaigns, record keeping, and local demonstrations.

The Smithsonian’s agricultural-fair collection emphasizes tradition, education, innovation, youth participation, and the fair’s ability to adapt with its community.

Those connections justify a fictional Fallout institution in which surviving county ledgers, extension notebooks, livestock clubs, repair exhibits, seed exchanges, and volunteer muster traditions are recombined by successor communities.

The post-Fallout continuity of any specific institution is fictional.

No final localisation should claim that a real 4-H, Extension, Farm Bureau, FFA, tribal, provincial, or county organization survived unless a later research pass establishes the location and attribution.

Research references:

- [Library of Congress, state and county fair history](https://www.loc.gov/item/today-in-history/august-22/)
- [Library of Congress, 4-H and community associations](https://www.loc.gov/exhibitions/join-in-voluntary-associations-in-america/about-this-exhibition/a-nation-of-joiners/building-communities/4-h/)
- [USDA NIFA, Cooperative Extension history](https://www.nifa.usda.gov/about-nifa/what-we-do/extension/cooperative-extension-history)
- [Smithsonian Libraries, Agricultural Fairs in America](https://www.si.edu/object/agricultural-fairs-america-tradition-education-celebration-julie-avery-editor%3Asiris_sil_616214)

## Reserved ownership

The following values are the next available sequence after the reconciled Ashline Firebreak ledger and are reserved by this plan only.

The implementer must rescan the event file, candidate arrays, script constants, localisation keys, Event Log tables, and `FALLOUT_EVENT_ID_LEDGER.md` immediately before implementation.

If any value has been claimed in the shared worktree, remap the entire row together and update every affected document rather than reusing or splitting ownership.

| Surface | Proposed ownership |
| --- | --- |
| Working chain title | The County Fair Returns |
| Namespace | `chaosx.fallout` |
| Candidate id and opening token | `572` |
| Scheduler transaction key | `710054` |
| Route identity | `7154` |
| Event Log history identity | `9159` |
| Primary family | `constant:fallout_event_primary_family.regional_and_biome` |
| Cooldown family | `constant:fallout_event_cooldown_family.recovery` |
| Event class | ordinary routine incident, followed by delayed result and callback |
| Required region | `constant:fallout_region.north_america` |
| Earliest phase | `constant:fallout_event_phase.rival_orders`, equivalent to Years 3 onward |
| Subject | one deterministic current-generation native rural state |
| Catalogue row direction | `FALLOUT-572` |

Proposed event allocation:

| Event | Role |
| --- | --- |
| `chaosx.fallout.572` | Human opening with four visible choices |
| `chaosx.fallout.573` | Hidden-AI opening using the same costs, branch reservation, and effects |
| `chaosx.fallout.574` | Human delayed result with branch-specific success, partial, and failure descriptions |
| `chaosx.fallout.575` | Hidden-AI delayed result using the same grading and effects |
| `chaosx.fallout.576` | Human one-season-later fair review |
| `chaosx.fallout.577` | Hidden-AI one-season-later fair review |
| `chaosx.fallout.578` | Exact cancellation and cleanup terminal |

One result event per presentation mode is sufficient because the selected branch and graded outcome can select triggered descriptions and effects.

Do not reserve four separate result lanes unless implementation proves that the current authenticated transaction pattern cannot safely dispatch the shared result.

## Eligibility and deterministic host selection

The candidate must be dormant behind the existing Fallout scheduler activation gates.

It must not set `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

Country eligibility:

- The country has a current Fallout country identity, resource row, and generation receipt.
- The exact live region identity is `constant:fallout_region.north_america`.
- The current phase is rival orders or later.
- The country does not already hold the durable completed-fair memory or a pending fair transaction.
- At least one branch is fully affordable at candidate-build time.
- Food and Cohesion meet named recovery thresholds, and the country is not under a severe unresolved survival crisis that would make a public fair implausible.
- The ordinary candidate slot, cooldown, fatigue, repetition, transaction, and visible-budget gates all pass.

State eligibility:

- The state is native, owned, and controlled by the candidate country.
- The state has a produced current-generation Air Winter snapshot and a current Fallout state row.
- The current state category is `rural`.
- The state has surviving population, an accepted Food reserve, accepted Supply Access, and bounded exposure and disease pressure.
- The state has enough adaptation and reclamation to support a gathering.
- The state is not carrying an unresolved hazard, evacuation, village-relocation, Ashline, frost, orchard, or other exclusive state transaction receipt.
- The state has no durable county-fair host memory.

The matrix promise says “several rural states.”

The reviewed default is therefore at least three eligible rural states owned and controlled by the country.

The selector should count those states for country admission, then choose the lowest eligible native state id as the single transaction host.

Only that host state is frozen into the transaction.

Do not expand the row into a multi-state transaction or invent partner state ids.

If static reachability shows that three states excludes nearly every plausible North American successor, the parent must explicitly approve a two-state threshold and revise the premise from “several” to “two linked rural districts.”

## Opening premise

Three or more recovered rural districts have enough food and security to send produce, livestock, repaired tools, household crafts, and volunteers to one host ground.

The immediate question is not whether the people can survive one more day.

The question is what kind of institution should stand behind the gathering.

The opening should acknowledge country government identity and relevant durable memories without letting one previous chain become a mandatory prerequisite.

Year Zero may influence which date the organizers use.

The Orchard Flowers Once, False Spring Losses, Seed Vault, and food-compact memories may influence agricultural confidence.

Market Under the Viaduct may influence stall discipline.

A New Funeral and Names for the Missing may influence the remembrance pavilion.

Weapons in the Nursery, Ammunition Winter, and command memories may influence the militia branch.

These are text, grading, and AI-weight connections.

They must not consume, clear, or overwrite the earlier chains’ durable ownership.

## Four authored choices

All costs and thresholds belong in a dedicated script-constant category.

The table specifies relative resource identities and consequences rather than approving magic numbers.

Each visible option must disclose its real cost, principal risk, delayed timing, and the fact that the host state will be rechecked before resolution.

| Branch | Player direction | Admission and cost direction | Delayed identity | Main trade-off |
| --- | --- | --- | --- | --- |
| Civic exhibition | Put the county boards, households, youth clubs, repair crews, and food cooperatives in charge. | Spend Food and Scrap, require workable Cohesion, and use Power only if the existing report-ground pattern proves it is a real constraint. | Civic trust, Recognition, fair order, repair credit, and household participation grade the result. | Best peaceful legitimacy and Cohesion route, but a weakly organized fair wastes stores and exposes local divisions. |
| Seasonal exchange | Give seed, livestock, preserved food, tools, and transport stalls priority. | Spend Food and Fuel, require accepted Supply Access and infrastructure, and never invent a bilateral partner or market-access treaty. | Trade trust, route reliability, Food reserve, and merchant discipline grade the result. | Best resource and supply route, but crowding, spoilage, and speculative pricing can turn the fair into a ration dispute. |
| Militia muster | Use the gathering to inspect local companies, recruit volunteers, and demonstrate disciplined security. | Spend Fuel and military Equipment through the proven stockpile contract, with Command Power or Army Experience used only if the current branch-cost convention supports it. | Arms discipline, military readiness, civic trust, crime pressure, and militia alignment grade the result. | Best recruitment and security route, but failure can cause an accident, theft, coercive recruiting, or militia political pressure. |
| Memorial gathering | Put family rolls, relief kitchens, recovered names, and a quiet remembrance pavilion at the center. | Spend Food and Medicine, require public-health capacity, and read but do not duplicate A New Funeral memory. | Family trust, cause memory, public health, religious tension, and Cohesion grade the result. | Best family trust and cause-memory route, but poor health control or competing ritual claims can turn remembrance into grievance. |

No branch may be a cost-free safe answer.

Invalid or unaffordable branches must have zero AI weight and a truthful human availability tooltip.

The candidate must not be produced when all four routes are unaffordable.

## Frozen ledgers and deterministic grading

The opening should freeze only variables that the result actually consumes.

Country-side frozen inputs:

- Food, Scrap, Fuel, Medicine, Recognition, and Cohesion.
- Military Equipment stockpile, War Support, Command Power, Army Experience, arms readiness, crime pressure, civic trust, and militia alignment when used by the muster branch.
- Family trust, religious tension, public health, and cause memory when used by the memorial branch.
- Calendar, market, orchard, seed, frost, funeral, missing-person, and command memories only where they change a threshold, AI weight, or result description.
- Selected branch, generation, country identity, region, transaction token, mode, and event-token receipts.

Host-state frozen inputs:

- Native state id, owner, controller, state-row generation, state category, and population.
- Food reserve or the current accepted agricultural-capacity variable.
- Air Winter adaptation, reclamation, exposure, disease pressure, and Supply Access.
- Infrastructure and any proven route or market memory.
- Current hazard and exclusive-transaction receipts.

The delayed result should occur 35 days after a valid choice.

Each branch should resolve to success, partial success, or failure through named thresholds.

No random list and no MTTH should grade the result.

Suggested grading emphasis:

| Branch | Strongest positive inputs | Strongest negative inputs |
| --- | --- | --- |
| Civic exhibition | Cohesion, Recognition, civic trust, safe host state, repair memory | Low Cohesion, local grievance, weak infrastructure, high disease |
| Seasonal exchange | Food reserve, Supply Access, infrastructure, trade trust, route reliability | Spoilage pressure, weak supply, low fuel, market grievance |
| Militia muster | Equipment, readiness, arms discipline, state supply, accepted military memory | Crime pressure, coercion memory, low civic trust, weak equipment |
| Memorial gathering | Family trust, public health, cause memory, Cohesion, accepted funeral memory | Disease pressure, religious tension, unresolved public grievance |

Failure should remain a local institutional setback rather than an apocalypse.

Possible failure consequences are spoiled stores and ration disorder for the exchange, broken stands or infrastructure strain for the civic route, an accident or arms theft for the muster, and illness or ritual conflict for the memorial.

Any civilian loss must use the accepted Deaths contract, preserve the minimum remaining population, and identify the cause through existing cause-memory surfaces.

This chain must not write global Air Contamination or invent a natural-disaster card.

## First seasonal callback and bounded recurrence

The callback should occur 365 days after the delayed result.

It asks whether the first fair became a durable annual institution.

The callback reauthenticates the country, generation, host state, owner, controller, branch, result, callback token, and current memories before applying effects.

Callback directions:

- A successful civic exhibition becomes an annual civic fair with a durable public-institution memory and modest Recognition or Cohesion support.
- A successful seasonal exchange becomes a recurring agricultural exchange with durable trade trust and route memory.
- A successful militia muster becomes a disciplined inspection and recruitment day when arms discipline and civic trust held, or a militia-pressure memory when they did not.
- A successful memorial gathering becomes a remembrance and relief tradition when family trust and public health held, or a contested-memory marker when they did not.
- A partial first fair produces a smaller local tradition and a recoverable grievance rather than deleting the institution.
- A failed first fair leaves a named failure memory and clears the annual-established flag.

This callback is the end of the present tranche.

It may set a durable `annual fair established` memory for later consumers.

It must not schedule itself forever, add a new yearly on action, or create a repeatable decision.

A genuine recurring seasonal event family remains queued until the first callback has implementation proof and the scheduler has an accepted recurrence contract.

## Memory ownership

Proposed durable memory identities should follow the final event suffix or chain slug selected during implementation.

The following semantic roles are required even if the final variable names change:

- Boolean country memory that a first fair has completed.
- Boolean country memory that an annual fair was established.
- Enum variable for fair identity: civic, exchange, muster, or memorial.
- Numeric or graded country ledgers for fair trust, trade trust, militia pressure or discipline, memorial trust, and cause memory.
- Boolean host-state memory that the state has hosted the reviewed fair.
- Boolean or enum host-state memory for the branch outcome.
- Durable result and callback Event Log history.

Use flags for boolean ownership and variables only for values with more than two states.

Do not use a numeric zero-or-one variable as a flag.

Do not clear durable memories during exact cleanup.

## Human and hidden-AI parity

The hidden AI opening must enter the same branch-selection helper, pay the same costs, reserve the same delayed child, freeze the same ledgers, use the same grading effects, schedule the same callback delay, and pass through the same exact cleanup contract as the human opening.

AI weighting should express expected ordering rather than force a single universal branch:

| Scenario | Expected ordering |
| --- | --- |
| High Cohesion, high Recognition, peaceful continuity or civic government, good repair capacity | Civic exhibition should lead. |
| Food compact, scavenger syndicate with legitimate markets, strong Food, Fuel, infrastructure, and Supply Access | Seasonal exchange should lead. |
| Warlord command, active war, high crime pressure, strong Equipment and readiness | Militia muster should lead when affordable, but low arms discipline must reduce it. |
| Religious refuge, high recorded Deaths, strong family trust, manageable religious tension and disease | Memorial gathering should lead. |
| Low resources or unsafe host state | The candidate should fail admission rather than let AI choose an invalid branch. |

Implementation must begin weighted-logic review with read-only `hoi4.probability_inspect` on the hidden-AI event-option block.

After source exists, use named scenario evaluation and compare the final weights against the expected ordering above.

Do not invent exact probability percentages in advance.

## Event Log, localisation, and catalogue directions

The Event Log uses history `9159` after the collision rescan.

The primary actor is the country.

The secondary actor is the authenticated host state.

Required Event Log surfaces are the opening choice, graded delayed result, and one-season callback for all four branches.

Required localisation directions:

- One authored opening title and description that makes the public recovery premise clear.
- Four authored option labels and effect tooltips.
- Branch-specific success, partial, and failure result descriptions.
- Branch-specific callback descriptions.
- Honest unavailable-cost and stale-transaction text.
- Event Log name, detail, and history payloads.
- State-name substitution only after the state target is authenticated.

Player-facing prose should describe the gathering, its people, and the world state.

It should not mention candidates, arrays, constants, schedulers, caps, reworks, implementation history, or testing.

Avoid anachronistic carnival rides, brand names, direct use of real organization names, and pasteable historical claims that the research does not support.

Catalogue direction for `docs/spreadsheets/chaos_redux_events_catalog.xlsx`:

| Field | Direction |
| --- | --- |
| Event id | `FALLOUT-572` |
| Event name | Final title should evoke the return of a county or agricultural fair without treating the working label as locked localisation. |
| Type | Routine or recovery regional incident, aligned with the workbook’s existing vocabulary. |
| Details | Several stable rural districts gather produce, repairs, livestock, volunteers, and remembered names at one host ground. |
| Choices | Civic exhibition, seasonal exchange, militia muster, memorial gathering. |
| Delayed outcome | The first fair is graded after 35 days and its survival as an annual institution is reviewed after 365 days. |
| Status | Needs Testing until runtime delivery and Event Log rendering are proven. |

The workbook is the only editable catalogue source.

After an accepted implementation update, the parent should run `.tools/export_event_catalog_csv.py` and must not edit exported CSV files directly.

## Asset handoff

The chain needs one dedicated static fictional report image.

Proposed stable consumer names, subject to the collision and registration review:

- Source workspace: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/`
- Runtime DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds`
- Sprite: `GFX_report_event_fallout_county_fair_returns`
- Runtime size: the existing Fallout report-event card convention, expected `210x176`

Art direction:

- A cold-recovery North American rural fairground built from repaired timber, canvas, and salvaged sheet metal.
- Foreground seed, preserved-food, livestock, and repaired-tool exhibits.
- Civilians, farm families, repair workers, and a restrained militia presence rather than a military parade.
- A small remembrance board may appear, but it must carry no readable generated text.
- Period documentary framing and the established sepia Fallout report-card treatment.
- No modern carnival rides, no zombies, no real-person portrait, no copyrighted logo, no national flag, no readable banner, and no super-event composition.

The asset should be generated as fictional alternate-history art and processed through the Fallout report-card pipeline.

A static image is preferable because this is a routine report popup whose value comes from the mix of civic, agricultural, trade, militia, and memorial details.

Animation, an icon family, audio, a portrait, and a GUI surface would add scope without improving this bounded chain.

## Implementation surfaces

If accepted, the parent implementation should touch only the normal Fallout chain surfaces:

- `events/fallout_world_end_events.txt`
- Dedicated county-fair script constants
- Dedicated county-fair scripted triggers
- Dedicated county-fair scripted effects
- The ordinary candidate registry and its deterministic state selector
- Dynamic modifiers only where the result and callback need durable mechanical expression
- English localisation with UTF-8 BOM
- Scripted Event Log localisation and actor mapping
- Report-image GFX registration and the final DDS
- The reviewed regional matrix disposition
- The next numbered reviewed spec
- Scheduler proof, reviewed-candidate proof, event-id ledger, implementation status, source-of-truth map, and asset manifest
- The workbook row and generated CSV exports only after implementation facts exist

No focus tree, decision, mission, scripted GUI, map rewrite, country creation, technology, doctrine, formable, or super-event surface is required.

The installed package has no Technology Tree Viewer.

No technology or doctrine change is proposed, so that limitation does not block the chain and must not be replaced by invented technology evidence.

## Engine-sensitive evidence gates

The chain is not implementation-complete until the parent has evidence for all of the following:

1. The shared-worktree collision rescan confirms events `572` through `578`, candidate `572`, transaction `710054`, route `7154`, and history `9159` as one ownership set.
2. The event-token table contains the seven named County Fair tokens, the candidate identity table contains the candidate, transaction, and route names, and the route upper bound is `7155`.
3. The candidate proves the exact runtime region `constant:fallout_region.north_america` rather than using an older thematic regional label.
4. The rural admission sweep counts the required eligible states and the deterministic host selector chooses the lowest eligible native state id.
5. The candidate freezes only one host state and does not pretend that a multi-state transaction exists.
6. The exact dispatch-issued wrapper and child delayed transaction are committed before the ordinary opening receipt is consumed.
7. Every delayed result and callback reauthenticates event token, mode, generation, country row, host state, owner, controller, and pending transaction.
8. A lost, transferred, invalid, or stale target fails closed through exact cancellation without clearing a newer transaction.
9. Human and hidden-AI lanes pay the same costs and reach the same result, callback, memory, Event Log, and cleanup effects.
10. Every due delay lies inside the scheduler’s accepted 1-to-730-day child window.
11. Any population loss uses the Deaths contract and preserves the accepted minimum remaining population.
12. The chain adds no global `on_daily`, `on_weekly`, or `on_monthly` country sweep and does not set either scheduler activation flag.
13. Tuning values live in script constants, while duration fields use the currently proven variable handoff when the engine field does not accept a constant token directly.
14. Event Log actor mapping preserves the country as primary actor and the authenticated state as secondary actor.
15. Narrow read-only `hoi4.event_inspect` trace, target, timing, terminal, and state-flow review is attempted after implementation.
16. If event inspection again returns `EVENT_ISSUE_LIMIT` on the large Fallout source, that result is recorded as a tooling limitation and not treated as passing engine proof.
17. User-owned runtime validation still covers popup order, host authority, save recovery, multiplayer delivery, Event Log state rendering, and full-screen Fallout presentation.

Acceptance scenarios:

- A North American country in rival orders with three safe rural states and a strong civic ledger selects the lowest state id, pays the civic cost, receives a deterministic result, and returns through the annual callback.
- A food-compact country with strong Food, Fuel, infrastructure, and Supply Access prefers the exchange branch and never creates a bilateral partner.
- A warlord at war with sufficient Equipment prefers the muster, while the same country with low arms discipline receives reduced muster weight.
- A religious-refuge country with high Deaths, strong family trust, and controlled disease prefers the memorial branch without rewriting A New Funeral memory.
- A country with only two qualifying rural states fails the default three-state admission gate.
- A country with no affordable branch produces no candidate.
- A host state that changes owner before result cancels only the matching fair transaction.
- A host state that becomes unsafe before callback receives the authored interrupted-tradition outcome or exact cancellation selected during implementation, with no leaked receipt.
- Human and AI paths produce identical deltas for the same frozen scenario.

## Queued work and deliberate exclusions

The following work remains queued because it would broaden this reviewed ordinary row beyond one safe transaction:

- A truly recurring annual county-fair family after the first 365-day callback.
- Delegations, livestock contracts, or market invitations involving a live neighboring country.
- Named organizers, real extension-service continuity, real historical symbols, or real institution claims.
- A fair decision category, mission, focus branch, achievement, country package, formable, scripted GUI, animated sprite, portrait, or audio cue.
- Province-level fairground placement or map geometry.
- Additional North American regional rows and the unfilled regional and archetype release-floor anchors.
- The scheduler activation setter, native host-authority proof, save recovery, multiplayer delivery, Event Log runtime proof, full-screen blackout, and the `660` manually reviewed living-world release floor.
- The exact all-valid-province thermonuclear sweep.
- Bilateral, relationship, and major-arc payload contracts that the current scheduler still fails closed.

These exclusions are not approved fallbacks.

They remain explicit incomplete surfaces outside this bounded plan.

## Promotion and parent handoff

Keep this file in `docs/plans/air_cleanliness_fallout_plans/` until the parent accepts the candidate and locks the collision-checked identifiers.

If accepted, promote the design into `docs/specs/air_cleanliness_fallout_specs/specs/53_reviewed_regional_county_fair_returns.md`, or the next available numbered filename, and add it to `SOURCE_SPEC_INDEX.md`.

The accepted spec should absorb the final title, exact constants, final admission thresholds, final modifier names, final Event Log wording direction, and final asset consumer names.

The working regional-matrix row should then be marked implemented as dormant rather than deleted.

Design problem: the reviewed Fallout library lacks a positive North American recovery institution connecting rural surplus, repair, public gathering, recruitment, and remembrance.

Proposed expansion: one seven-block state-targeted county-fair chain with four distinct policies, a 35-day deterministic result, a 365-day institution review, durable memory, human and AI parity, authenticated cleanup, one static report asset, Event Log coverage, and catalogue directions.

Research basis: North American agricultural fairs, agricultural societies, county extension, youth agricultural clubs, livestock and crop judging, repair and machinery display, and community gathering.

Implementation surfaces affected: the ordinary Fallout event, candidate, constants, triggers, effects, modifiers, localisation, Event Log, GFX, asset, documentation, ledger, proofs, and catalogue surfaces listed above.

Open questions for parent resolution are limited to the collision rescan, whether three rural states remain reachable enough to preserve the matrix premise, exact centralised costs and thresholds, and whether an unsafe callback should use an authored interrupted-tradition payload or exact cancellation.

Prior-addendum status: Ashline Firebreak is implemented and documented, so no prior addendum for the same event remains unresolved.

This county-fair addendum remains queued until accepted, implemented, folded into the reviewed specs, or rejected with a recorded reason.
