# Legacy findings and requirement trace

## Repository inspection

The existing Event 79 event and decisions were fetched in full from `klimPaskov/Chaos-Redux` at commit `879b3007d3b6bf75c726c11635473fccda45c569`.

The event file uses one global target, selects a peaceful factionless minor smaller than the initiating country, registers a limited set of rivals, gives guarantees, and places the final puppet effect inside a later popup option. The decision file appends historical score values to a ranking array and uses political-power purchases that can instantly create civilian and military factories. These are source observations, not runtime test results. [R1, R2]

## Replacement requirements

| Legacy finding | Required replacement | Owning specification |
| --- | --- | --- |
| One `global.minor_to_attract` | Target plus race-generation identity for every record | Parts 01, 07, implementation contracts |
| Initiator-relative factory ceiling | Any valid independent AI minor, regardless of player size | Part 01 |
| Peaceful, factionless target gate | Preserve valid faction and third-party-war cases through a proven takeover contract | Parts 01 and 08 |
| Limited ideological participant roster | Every major and every player, including player minors | Part 01 |
| Free opening guarantees | Registration without new diplomatic guarantees | Parts 01 and 08 |
| Historical maximum-score array | Live ranking from current per-race scores | Part 02 and state contracts |
| PP-only instant industrial output | Real factory commitments and delivered project contracts | Part 04 |
| Extreme cheap popularity changes | Priced campaign durations, saturation, and explicit political operations | Parts 03 and 06 |
| AI preference against human rivals | Contextual strategy with no human-targeting bias | AI specification |
| Delayed popup-dependent puppet | Same-flow threshold commit, reports afterward | Part 08 |
| Broad guarantee and war cleanup | Relation ownership and exact native reconciliation | Part 08 |

## User requirement trace

The catalog identity is preserved in the overview and integration section. The independent AI minor target rule is in Part 01. The universal major/player roster and player-minor route are in Parts 01 and 09. Initial ideology, party, relations, faction, guarantee, economic, military, political, intelligence, and historical factors are all specified in Part 02.

All five action families have prices, duration, output, and political meaning in Parts 03 and 04. Rival interference and its limits are in Part 05. Government and institutional change are in Part 06. The two evolution thresholds, active upgrades, evolved openings, repeated firing, and simultaneous races are in Part 07. Actual puppet victory and campaign closure are in Part 08. The compact decision category and expanded rankings are in the interface section.

The unresolved universal-subject hierarchy case is explicitly preserved as a critical proof gate. This package does not silently narrow that requirement and does not pretend it is already solved in the engine.

## Repo reference identifiers

**R1.** `events/079_the_master.txt`, blob `11a710010238731c62da841195bfc2cf6d19b3ac`, full content read.

**R2.** `common/decisions/079_the_master_decisions.txt`, blob `fbe4c6747457ffda8983ac1a4b5ec258dcfe97c0`, full content read.

**R3.** `.agents/skills/chaos-redux-mtth/SKILL.md`, blob `7d86c0fe166a23264fcb2a9f512994977f372a80`, full content read from default branch during this session.

**R4.** `docs/systems/universal_cost_modifier.md`, blob `f053e8d76ef5d7232fd622a18b7ae7d9faa77e83`, full content read from default branch during this session.

**R5.** `paradox_wiki/Autonomy state modding - Hearts of Iron 4 Wiki.md`, blob `a01324b7cdc9d2a3ea086ccdc5b187800b4e8dae`, full content read at the pinned commit. The page identifies itself as a 19 September 2026 snapshot.

**R6.** `docs/testing/chaosx_test_country.md`, partial content read. The requested response was truncated. The package uses the observed extension contract as a reference direction and requires a full current read before implementation.

The archive's sources are separately enumerated with SHA-256 hashes and full chunk coverage in the source-reading audit.
