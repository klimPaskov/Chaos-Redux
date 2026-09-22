# Engine evidence and open questions

## Evidence scope

Repository inspected: `klimPaskov/Chaos-Redux`.
Pinned revision: `879b3007d3b6bf75c726c11635473fccda45c569`.
The upload is the baseline for planning instructions and catalogs.
The repository inspection supplements that baseline with the existing Event 078 implementation and relevant native-effect documentation.
It does not establish that the user's current local checkout is identical to the pinned remote revision.

## E1: existing Event 078

Path: `events/078_border_war.txt`.
Read in full through the connected GitHub file action.
The old hidden entry chooses one random country, then a neighbor.
The visible event contains an option that declares a normal annexation war.
It also uses a single global opponent variable and delayed callbacks.
The subsequent native setup loops through bordering states and requests automatic state transfer.

These are observed behaviors of the inspected source.
They are incompatible with the requested worldwide allocation and the proposed conflict-specific single-state settlement.
The source is a migration input, not a safe template to extend by merely changing a loop.

## E2: documented native border-battle effects

Path: `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`.
Read relevant lines 620 through 707, with header and several additional ranges noted in the source manifest.
The file identifies itself as a wiki snapshot captured on 19 September 2026.
Its border-war section distinguishes native battle effects from the separate state-based `set_border_war` feature.

The inspected section documents `start_border_war` with attacker and defender state endpoints, per-side win, loss, and cancellation event IDs, and the `change_state_after_war` option.
It states that the participating countries are determined by the owners of the specified states.
It documents endpoint-addressed `cancel_border_war`, `finalize_border_war`, and `set_border_war_data`.
Its example disables automatic state transfer.

This supports using native combat with an explicitly handled territorial result.
It does not prove the callback scope contains a unique battle identity in a multi-conflict case.
It also does not prove that every diplomatic relationship or concurrent configuration is legal in the installed version.
The installed game's own documentation and fixtures must settle those questions.

## E3: existing project precedents

Search excerpts from `common/scripted_effects/008_tensions_rising_effects.txt` show native border battles with automatic transfer disabled.
Search excerpts from `common/scripted_triggers/008_tensions_rising_triggers.txt` also show a country-level existing-border-war exclusion.
That exclusion cannot be reused as Event 078's admission rule.

Search excerpts from resource-dispute and infantry-trial files show other uses of native border battles and documented literal-value handling.
A prior famine-and-migration corridor handoff describes Event 019 as freezing state identities and a nonce before using distinct side callbacks.
The same handoff warns that the generic border-war-lost hook is not a complete conflict-context source.
These are useful leads for the implementing explorer.
The full implementations and their installed-engine behavior were not reviewed in this session.

Do not cite those old handoffs as proof that Event 078's much broader concurrency already works.
Do not assume a nonce stored once per country remains safe for several simultaneous battles.

## E4: MTTH guidance

Path: `.agents/skills/chaos-redux-mtth/SKILL.md`.
Read in full through the GitHub connector.
It requires the project's probability workflow for MTTH analysis and distinguishes verified game-adapter timing from unsupported source-only inference.
Its cited current MTTH implementation file was not read.
The 90-day planning target in this package therefore remains an unverified timing input.

## Release-blocking questions

| Gate | Required proof | Current status |
| --- | --- | --- |
| B1 | One country can run native battles against several neighbors simultaneously | Not established |
| B2 | One pair can run independent simultaneous native battles on distinct endpoints | Not established |
| B3 | Each callback can resolve exactly its own battle after concurrency, delays, and save/load | Not established |
| B4 | An unrelated normal war does not invalidate the otherwise legal participant | Not established in a native fixture |
| B5 | Manual single-state transfer and immediate next battle preserve a valid native military state | Not established |
| B6 | Capital, last-state, diplomatic, occupied-state, and special-adjacency cases are classified correctly | Not established |
| B7 | Concurrent cleanup coexists safely with other project border-war systems | Not established |
| B8 | Native troop selection and AI behavior remain functional at worldwide scale | Not established |

A failure in B1 or B2 cannot be repaired by calling sequential fights simultaneous.
A failure in B3 cannot be repaired by storing the latest opponent in a country or global variable.
A failure in B4 cannot be hidden behind a blanket peacetime requirement.
An evidenced hard engine limit is a blocker requiring a revised design decision, not permission for an unannounced fallback.

## References for the implementing reader

Use the pinned repository and the exact paths above to reproduce the inspection.
The following are full-file or excerpt leads, with the scope of this session's read stated explicitly.

| Reference | Path | This session |
| --- | --- | --- |
| R1 | `events/078_border_war.txt` | Full file |
| R2 | `localisation/english/078_border_war_l_english.yml` | Search excerpts only |
| R3 | `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | Selected ranges |
| R4 | `common/scripted_effects/008_tensions_rising_effects.txt` | Search excerpts only |
| R5 | `common/scripted_triggers/008_tensions_rising_triggers.txt` | Search excerpts only |
| R6 | `common/scripted_effects/018_resources_found_decision_effects.txt` | Search excerpts only |
| R7 | `common/scripted_effects/019_infantry_spawn_achievement_effects.txt` | Search excerpts only |
| R8 | `docs/plans/famine_and_migration_system_plans/subagent_handoffs/corridor_attack_owner_exploration.md` | Search excerpts only |
| R9 | `.agents/skills/chaos-redux-mtth/SKILL.md` | Full file |
| R10 | `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md` | Search excerpts only |

Public web searches did not produce a sufficiently verified primary source for the unresolved concurrency behavior.
No forum recollection or unrelated search result was used to declare an engine capability proven.

## Pinned source locators

events/078_border_war.txt

`https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/events/078_border_war.txt`

.agents/skills/chaos-redux-mtth/SKILL.md

`https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/.agents/skills/chaos-redux-mtth/SKILL.md`

paradox_wiki/Effects - Hearts of Iron 4 Wiki.md

`https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/paradox_wiki/Effects%20-%20Hearts%20of%20Iron%204%20Wiki.md`

