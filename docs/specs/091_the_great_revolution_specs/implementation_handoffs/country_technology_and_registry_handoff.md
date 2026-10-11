# Country, technology, and public registry handoff

## Accepted source contract

This handoff translates accepted country and presentation design into implementation responsibilities. Exact engine identifiers are verified in the implementation checkout before use. Values expressly described as initial tuning are design proposals to evaluate, not claims of native engine behavior or measured game balance.

## Country package inventory

| Surface | Required implementation result | Evidence and ownership |
| --- | --- | --- |
| Country registration | One complete World Revolution identity, preferring the existing dormant REV package after the full collision audit | Search installed vanilla, Chaos Redux, workshop content, and relevant local mods. Record tags, aliases, cosmetic identities, live countries, and conflicting definitions |
| Country and ideology names | Fixed World Revolution identity, coherent ideology and route variants, correct adjective and country presentation | Localisation owner writes final wording from direction, with current name and cosmetic consumers checked |
| Party and government | Communist revolutionary government with collective, central, and distributed institutional variants | Route changes affect Revolutionary Government and actual governance, with no duplicate ruling characters |
| Capital and settlements | A valid capital in the selected sovereign origin, with later relocation only to a real controlled city | Use actual map and victory-point data. Lenin's body, administrative capital, and origin anchor remain separate facts |
| Settlement naming | Preserve local and historical names at activation. A later symbolic renaming requires a route-specific choice and researched language | Record former and new presentation, legitimate controller, and restoration behavior. No global automatic Russian renaming |
| Leadership | One authoritative Lenin, actual current Stalin and Trotsky checks, legitimate inherited rebel leaders | Character owner proves ownership and role transfers, with grounded portrait handoff for every real person |
| Commanders | Preserve inherited commanders where native transfer and political disposition allow it. Recruit local cadres only through actual regional development | Do not invent a global historical roster without identity and date checks. Fictional supernatural command roles must be labeled and sourced through their distinct portrait workflow |
| Advisors and institutions | Prefer the three core institution families and existing legitimate characters. Add an advisor only when a specific program needs a distinct mechanical role | Cost, eligibility, slot, discount stacking, removal, identity, portrait, and DLC compatibility must be documented |
| Laws | War-capable mobilization, economic and trade laws justified by origin conditions and political route | Inspect current native law availability and valid requirements. A country can field its starting army without instant maximal laws |
| Stability and war support | Useful but imperfect initial governance and war readiness derived from origin conditions, actual uprising support, and inherited institutions | Retire the old maximum defaults. Initial balancing starts around 50 stability and 75 war support, with a disclosed origin adjustment of at most 15 points, then tests low and high support openings |
| Factories, resources, buildings | Actual transferred or locally administered state assets, damage, supply, and access | No duplicate grant for nominated overlaps. Foundry programs repair or build through actual costs and a named site |
| Stockpiles | Documented inherited, defected, captured, produced, or delivered equipment and finite seed tools | Actual source debit and destination credit, with model identity, fuel, convoys, and reinforcement accounted separately |
| Divisions | All eight custom family pathways and a playable finite opening package, plus preserved compatible inherited formations | One muster owner and actual template, manpower, equipment, naming, model, counter, audio, and provider proof |
| Air and navy | Relevant inherited assets and earned development when valid bases, fuel, equipment, and deployment exist | Preserve exact ships, wings, manpower, and stock semantics. Unsupported transfers remain concrete blockers rather than guessed spawn commands |
| Diplomacy | Revolutionary membership terms, independent partner route, refusal, subject progression, free independence, and final terminal choice | Current factions, wars, autonomy, and subject relationships revalidated before mutation |
| Existing countries | Add crisis content without replacing meaningful existing focus trees, laws, commanders, or political history | Country-specific route adapters preserve alternate leaders, small states, colonies, occupation, and valid exile |

The initial stability and war-support proposal is deliberately bounded resource tuning. It creates neither a territorial minimum nor immunity from genuine collapse. The country-package auditor must test whether the actual low-industry, high-war, and isolated-origin cases remain playable and explain any necessary revision to the parent.

## Technology inheritance and placement

The starting package has three research slots. It inherits a coherent compatible origin technology set and additional donor knowledge only where actual transferred forces, equipment, institutions, or an accepted research agreement justify it. A tank stockpile can precede domestic tank production. The presence of one captured aircraft does not grant the latest air technology of every opening participant.

Use the current `union_compatible_researched_technologies_from_donor` interface with its scope, output initialization, and compatibility rules. Preserve prerequisite and exclusivity semantics. Do not implement a second broad technology enumerator or copy every world's researched technology because all countries appeared in the opening snapshot.

| Technology or research surface | Intended location and prerequisites | Unlock or effect | Asset and verification requirement |
| --- | --- | --- | --- |
| Initial infantry and industry knowledge | Existing compatible infantry, support, construction, and production branches from the actual origin donor | Reproduce the ordinary weapons and industry that sustain the initial host | Inspect the resulting graph and production list, including designer and DLC variations |
| Awakened and specialist family access | Event recruitment and focus unlocks connected to existing infantry and support prerequisites | Eligibility to muster the appropriate family with real tools, arms, and cadres | Distinct unit and equipment art where a new consumer exists, provider registration and CXT coverage |
| Motor standardization | Existing motorization and support technologies with actual trucks, fuel, and workshops | Sustainable Red Motor Column production and repair | Verify equipment token compatibility, captured older models, production costs, and icon consumers |
| Foundry armor development | Existing compatible armor and industrial research with a secured heavy-industry program | Domestic manufacture or repair of the accepted heavy family | Check chassis and designer variants rather than granting mutually exclusive designs together |
| Cavalry and engineering development | Existing mounted and support-engineer prerequisites with local horses, specialists, and equipment | Regional mobility, supply repair, and siege support | Do not introduce a new technology folder merely to rename existing capability |
| Air and naval research | Actual compatible inherited or licensed equipment and a working airfield or port program | Conditional aviation or maritime development described by the country routes | Inspect native ship and aircraft design compatibility and the relevant tree branches |
| Fourth research slot | A completed protected research exchange, a protected industrial center, and a real foreign partner or qualified domestic research institution as contributor | One additional research slot, once | The research focus enables a meaningful exchange mission, with success receipt and icon |
| Fifth research slot | Completed late foundry research network with two functioning regional commands and 90 days of sustained research participation | One additional research slot, once | Loss before completion interrupts the mission. Later loss affects ongoing cooperation, not a repeat slot grant |
| Focus research bonuses | Relevant program completion and named technology category | A bounded useful bonus tied to the branch's actual next work | Inspect category, amount, uses, prerequisites, exclusivity, and existing bonus stacking |

The accepted baseline uses the relevant existing technology structure and event-owned family unlocks. If native custom equipment requires an added technology node, place it beside its closest verified infantry, support, motor, or armor precedent with explicit prerequisites and a researched visual identity. That is a specific integration need requiring parent approval of the graph change, not permission to invent a parallel technology tree during implementation.

Inspect affected grants, prerequisites, doctrine interactions, categories, folders, and bonuses with `hoi4.tech_inspect`. Render the relevant branches with `hoi4.tech_render`, then use `hoi4.tech_inspect` (`mode = compare`) on the implemented revision against its recorded baseline. Check the standalone Technology Tree Viewer only if the task needs it. Apply current AGENTS.md retry limits and use source/reference review and useful local checks if optional routes are unavailable. Record missing renders as visual limitations. Source review alone does not prove the graph appears or behaves correctly in the installed game.

## Reserved integration identifiers

| Role | Presentation slot | Playback audio ID |
| --- | ---: | ---: |
| Opening, frozen month Revolution | 121 | 121 |
| The Red World | 122 | 122 |
| Earned defeat | 123 | 123 |

The public Red World world-end registry identity is `18 / red_world`.
The parent reserved these identities after separate namespace checks in [the shared identifier registry](../../shared_identifier_registry.md).
Revalidate reservations before implementation and preserve implemented IDs. Matching presentation/audio numbers are independently checked allocations, not an inference that their namespaces are interchangeable.
These reservations do not register runtime content or approve any candidate track, image or quote.

## Public registries and documents

| Registry or document | Required accepted state | Important preservation rule |
| --- | --- | --- |
| Event catalog | 091, The Great Revolution, Major, Chaos level 5, no cluster, To Be Reworked until explicit status authorization | Current brief overrides old export values. The month title does not rename this row |
| 001 evolution details | Three owned evolution stages and the historical Whispers unlock pointing to separate Major 091 | Do not create a duplicate 001 evolution firing for 091 |
| Selection and Events tab | Current eligibility, retained stored weight, correct unavailable display | Historical unlock and weight survive active containment |
| Event history and actor | One successful 091 firing, correct actual date and month, World Revolution actor | Actor reservation precedes generic history recording. Failed preflight records no false firing |
| Event details | Clear player-facing return, global uprising, alignment, sovereignty, powers, and Red World premise | Final writing comes from mechanics, with raw helper names and formulas kept out of player copy |
| World threat | One owned 091 source and aggregate refresh on actual activation and defeat | Never clear unrelated sources |
| Red World scenario | One audited stable scenario identity, public row, persistent branch toggle, shared global disable behavior, separate super-event association | Revalidate reserved `18 / red_world` against hidden and active registry entries before wiring |
| Shared identifier reservations | Existing reservations in `docs/specs/shared_identifier_registry.md`, with namespace, owner, status and evidence | Reservation does not prove runtime registration or design acceptance. Do not renumber live IDs to fit a proposal |
| Music catalog | Three unused works or recordings, distinct playback IDs, final attribution and source evidence | Playback ID 91 is occupied. Revalidate reserved audio 121/122/123 and presentation 121/122/123 separately |
| Achievements | Eight active designs through the shared achievement owner, with the month meta-achievement explicitly parked | No false across-campaign persistence or easy unlock shortcuts |
| Unit providers and CXT | Every standalone family or attachment has its documented provider disposition and current CXT registration | A renamed unit does not inherit complete shared support automatically |
| Mechanics and event documentation | User-facing systems, lifecycle, source ownership, force growth, endings, costs, and AI reflect the implemented result | Promote durable accepted design. Retire stale behavior and misleading old docs with consumer proof |
| Asset and subagent handoffs | Every asset requirement traced to source, production, consumer, and validation, with unresolved items explicit | Promote durable provenance before event-scoped cleanup. User live-game observations are reviewed when supplied and are not a delivery gate |

The supplied catalogs were export CSV snapshots. No editable catalog workbook was supplied in this planning environment. Implementation must locate and edit the authoritative workbook under `docs/spreadsheets/` through the owning XLSX workflow, then regenerate its exports and compare the expected rows. Reading a CSV does not establish complete live registry occupancy.

## Completion evidence

The country-package auditor checks origin activation, character continuity, meaningful existing countries, industry and stocks, laws, all research-slot routes, land forces, conditional air and navy, equipment compatibility, alternate starts, and tag collisions. The documentation owner checks all public surfaces against the actual implementation. The parent accepts their evidence and reports concrete blockers. This planning handoff performs no country activation, technology grant, registry edit, or workbook mutation.
