# Law Upgrade: research basis and source limits

## Authority and evidence classes

The user's supplied Event 82 brief is authoritative for this design. It overrides older catalog wording and the current legacy event's much narrower behavior.

All 42 text files in the supplied archive were read end to end before drafting the numbered specifications. This includes every supplied skill, the three catalog exports, shared mechanics, dynamic helper documentation, AGENTS, configuration, and all 20 nested agent definitions. The supplemental plans archive contains the exact per-file SHA-256 and byte manifest.

That full archive reading is not a claim that every file mentioned by those documents was also read. The repository, installed game, DLC sources, and visual-reference libraries are much larger and were not exhaustively inspected.

Distinguish user requirements, author-developed design proposals, observed source behavior, offline documentation, external research, arithmetic reference checks, and live game evidence. This task produced no live game evidence.

## Repository revision inspected

Repository: `klimPaskov/Chaos-Redux`.

The targeted repository reads used revision `879b3007d3b6bf75c726c11635473fccda45c569`. This identifies the inspected material. It is not a claim that this revision matches the user's current local worktree or is the newest available commit.

### Legacy Event 82

The complete `events/082_law_upgrade.txt` file was read. It contains a hidden worldwide dispatcher, `chaosx.nr82.1`, which sends `chaosx.nr82.2` to every country. The report's option calls `upgrade_economy_law`.

That source has no Event 82 conscription upgrade or War Support award. Its economy change occurs in the option rather than in the global dispatcher. The rework therefore needs genuine immediate effect application, not merely updated text.

The public identifiers should be preserved unless a verified migration requires otherwise.

### Existing economy helper

A targeted search of `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` found documentation that `upgrade_economy_law` advances toward Total Mobilization but grants 150 Political Power at that cap and requires adjustment for new laws.

This was a snippet read, not a full Effects-page read. Treat it as a concrete warning requiring inspection of the loaded helper, not as installed-game proof.

The same helper is also called by the existing Zombie Outbreak event. Do not globally alter its behavior for Event 82 without auditing other callers. The new cap-preserving advancement should not accidentally rewrite another event's established results.

### Idea and law implementation reference

The full offline `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md` was read. Its snapshot states that it was captured on 2026-09-19.

It distinguishes laws as idea categories, static idea modifiers from dynamic modifiers, startup/load-only `allowed` checks from continuously evaluated availability, manual-removal controls, law levels, removal costs, and slot-cost modifiers.

Those distinctions inform the implementation gates in the coding prompt. The offline snapshot does not replace the missing installed-game documentation or prove the exact current law-price and population formulas.

### Cost framework

The full `docs/systems/universal_cost_modifier.md` was read. It specifies ordinary current cost inputs, composed source ratios, final upward quantization, matching displayed and paid prices, fresh quotes at confirmation, and recorded actual payments.

It also explicitly describes bounded owner coverage and a lack of a generic engine-accessible price getter for every purchase surface. Event 82 therefore needs a proven native adjacent-law price provider. The framework's existence is not evidence that such a provider already exists.

The detailed helper contract linked by that document was not fully read in this task.

### MTTH reference

The complete externally referenced `.agents/skills/chaos-redux-mtth/SKILL.md` was read in addition to the archive. It requires inspector-backed probability and timing evidence.

Only lines 1–220 of `common/mtth/chaosx_mtth_variables.txt` were read. That inspection shows existing project conventions but is not a complete source review of that file or evidence that Event 82's proposed timing is implemented.

## Catalog reconciliation

The supplied Event 82 export row describes the old narrower economy upgrade. The supplied Military Preparation cluster export does not yet list Event 82.

The accepted specification is Minor Repeatable, Chaos level 1, Military Preparation, Low member. The implementation's documentation and catalog work must update the authoritative editable workbook and regenerate the export through the established exporter. No CSV was edited here.

The authoritative workbook was not supplied. The export is read-only evidence of the old catalog, not an editable replacement for the missing workbook.

The supplied Event 61 row is still “Half mils into civs”. A future Return to Peacetime integration is consequently labeled prospective rather than treated as an existing reverse-law system.

## Historical grounding

The UK Parliament's overview of Second World War conscription describes expanded service obligations alongside exemptions for medically unfit people and workers in important occupations. Its account also describes the later widening of service obligations to women and older men.

The useful design inference is that reserving people for essential civilian work is part of mobilization itself. Removing almost all of that reserve provides a grounded reason for catastrophic construction, administration, and production penalties. The 99% value remains the user's fictional extreme, not a historical statistic.

Source, full relevant page read: `https://www.parliament.uk/about/living-heritage/transformingsociety/private-lives/yourcountry/overview/conscriptionww2/`

An Imperial War Museums search result concerning workers on the wartime home front was located, but the page could not be fully fetched. No numerical balance choice depends on that snippet, and it is not represented as fully reviewed artwork or a licensed asset source.

## Developer research relevant to AI

An official Hearts of Iron IV developer post in the Steam announcements archive discusses International Market AI in terms of real equipment needs, reserves, and comparisons between equipment types.

The design inference is limited: Event 82's AI should examine weighted shortages and reserve needs rather than equating every stockpiled item or treating the highest law level as automatically best. The post does not verify Event 82's law formulas, current consumer-goods floor, or cumulative MTTH probabilities.

Official developer archive page inspected: `https://store.steampowered.com/news/posts/?appids=394360&enddate=1692882378&feed=steam_community_announcements`

## Missing mandatory external reading

Of the eleven core offline wiki pages named by AGENTS, Idea modding was fully read. Effects and Modifiers were inspected only through targeted snippets. Data structures, Triggers, Localisation, Scopes, On actions, Event modding, Decision modding, and AI modding were not read end to end from the repository snapshot in this task.

The installed HOI4 documentation directory, current vanilla law files, complete DLC law owners, full shared cost helpers, relevant current owner scripts, visual reference library, achievement registry and live consumer files, and the authoritative workbook were not fully read.

These omissions remain documented implementation-preflight requirements. They are not quietly treated as satisfied because related supplied skills were read.

## Subagents and verification

Every supplied agent definition was read. No provided specialist was actually spawned. This session had no usable independent-agent invocation route and no callable HOI4 probability or live-engine validation tools.

The supplemental plans include self-contained handoff prompts and a role-disposition matrix. They are ready instructions, not completed specialist reports.

The parent performed cross-checks and arithmetic reference tests. Those are expressly same-author and non-engine evidence. The mandatory isolated improvement-loop and probability reviews remain open.

No supplied text was intentionally shortened for a quicker design. External repository inspection remained targeted and sometimes partial as itemized above.
