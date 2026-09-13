# Planning, improvement, and routing skill cleanup handoff

Disposition: implemented editorial cleanup, subject to parent review.

## Authority and scope

The parent assigned only the three skill entrypoints listed below and this handoff.
The user requested slightly more concise, logically organized, internally consistent wording with every distinct condition, exception, example, explanation, dependency, step, strength, scope, and ordering requirement preserved.
No child agents were spawned and no production workflow, runtime tool, external application write, generation, paid operation, or Git commit was performed.
The latest user correction preserves Astra for 3D model authoring while changing only the separately owned TOML model defaults to Sol high.
Every Astra workflow clause in these three skills remains identical to the saved original.

## Read inventory and limits

The original source is `C:/Users/klimp/.codex/tmp/chaos-redux-skill-cleanup-20260913/original/.agents/skills/`, including pre-existing user changes.
The Git HEAD diff was not used as the preservation baseline.
AGENTS.md was read in full through ranges 1–240 and 241–end.
The official `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md` was read in full, with the latter half independently reread.
Before further edits, both versions of every owned skill were read completely in bounded chunks.
Planning original: 1–400, 401–800, 801–1200, 1201–1500, 1501–1650, 1651–1950, 1951–2150, 2151–2291.
Planning current before these edits: 1–400, 401–800, 801–1100, 1101–1400, 1401–1700, 1701–1950, 1951–2150, 2151–2290.
Improvement original: 1–150 and 151–287.
Improvement current before these edits: 1–150 and 151–289.
Routing original: 1–170 and 171–363, with 271–363 independently reread.
Routing current: 1–170, 171–280, 281–364, with 26–45 independently reread.
Oversized initial mixed calls were truncated and were not accepted as full reads.
The only gap in the subsequent planning original chunk was recovered by the independent 998–1024 read, and the current routing truncation near its identifier mapping was recovered by the independent 26–45 read.
Offline wiki core pages were opened and their introduction/usage excerpts consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
The Localisation basics and optional version-number passage were also read.
Installed vanilla `documentation/script_concept_documentation.md` introduction and bindable-localisation/collection examples, `common/script_constants/documentation.md` in full, and `documentation/effects_documentation.md` introduction were consulted.
Wiki and vanilla sources were consulted as editorial references, not claimed as a full runtime-system review.
Reference consultations for cross-file meaning included the current asset skill Flags section, the planning skill’s own flag/source rules, and narrow search results from the super-event and 3D pipeline skills.
A Python reference-excerpt read using the Windows default encoding failed on Localisation and was rerun with UTF-8.

## File dispositions and structural changes

| File | Disposition | Changes |
| --- | --- | --- |
| `.agents/skills/chaos-redux-event-planning/SKILL.md` | implemented | Retained numbered heading hierarchy cleanup, properly nested writing-style examples, exact duplicate evolution-bullet merge, and historical-flag handoff clarification from the interrupted worker after independent review. Moved the folder convention before input, localisation handoff under Writing style, formation/UI questions under Cleanup and quality gate, and the two addendum paragraphs under Improvement-loop expansion specs. |
| `.agents/skills/chaos-redux-improvement-loop/SKILL.md` | implemented | Retained prerequisite/folder blocks before cadence and grouped nine surface-specific subsections. Clarified sourced real-flag references and final reconstruction. |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | implemented | Retained Routing gates and Specialist routing hierarchy, moved plan/spec paths before patch handoffs, and reduced extra blank lines. All body instructions remain verbatim. |

These are moves of descriptive guidance, not reordered execution steps.
Every conditional prerequisite, same-event anti-stacking restriction, plan acceptance gate, closure handoff, optional GUI rewrite route, MCP evidence requirement, parent/worker scope boundary, source rule, no-DLC compatibility requirement, value budget, paid-attempt limit, and example remains present.
Repeated cross-file rules were retained because guaranteed loading of their complete shared instruction was not established.
The duplicate merge removes only the adjacent identical `- evolutions` bullet under Possible links include.

## Corrections and evidence

C1: Planning Asset prompt handoff changed “whether a flag, symbol, or portrait must be sourced historically instead of generated” to distinguish historically sourced flag designs followed by imagegen reconstruction from sourced symbols/portraits.
The basis is the original planning Mandatory asset coverage section and its Asset prompt handoff paragraph, which explicitly require every new flag to use imagegen after cited historical design research, corroborated by the current asset skill Flags section.
This retains both sourced historical evidence and generated final-flag reconstruction and prevents the original bullet being read as a sourced final flag exemption.
C2: Improvement Asset and visual improvement changed the real-flag portion of “Use source-based assets for real people, real flags, real symbols, and real historical images” into “Real flags require sourced design references followed by reference-constrained imagegen reconstruction.”
The basis is the owning asset skill’s explicit “Always use `$imagegen` for every new flag” rule and the planning skill’s matching flag contract.
Other source classes, generated fictional/symbolic/supernatural/impossible classes, and the blocked-no-weak-substitute rule remain unchanged.

## Unresolved boundaries and scoped distinctions

U1: Planning Super-event text boundary and research gate permits already researched/sourced/documented exact wording inside a spec, and Super-event research handoff preserves researched title/quote/button exceptions.
Planning Writing style instead prohibits final localisation universally, expressly including the same super-event surfaces.
Both passages remain intact because external source verification proves wording accuracy, not which planning-output boundary the user intends.
Decision needed: whether sourced finished super-event wording may appear in an event spec or only its separate research prompt/package.
U2: Planning Output rules says “You do not give implementation guidance, you are just handing off ideas” and discourages technical tables and detailed wiring.
Planning 3D model and skeletal animation planning standard mandates precise consumer keys, paths, measurements, component matrices, hashes, FPS/frame policies, and export/reimport evidence, while Final prompt files mandates detailed coding-agent instructions.
Both passages remain intact.
Decision needed: whether the Output rules prohibition applies only to core design prose, allowing separate mandatory matrices/prompts, or whether the prescribed technical material itself should change.
S1: Routing Spreadsheet catalog routing explicitly restricts the context-light worker to the workbook and named player-facing source material, and says it should not read wiki or vanilla material.
AGENTS.md has a global pre-change reference rule.
The spreadsheet passage is a clearly role-specific reading restriction for spreadsheet-only work, retained exactly and classified as a scoped tension rather than silently broadening this worker’s preflight.
No new precedence rule or workbook-reading requirement was invented.
S2: Sol high TOML defaults and preserved Astra 3D authoring prose are an accepted intentional distinction under the latest explicit user correction, not an unresolved model conflict.

## Verification

- `chaos-redux-event-planning`: frontmatter byte-identical, all 5 fenced blocks byte-identical as a multiset, inline technical-literal multiset unchanged, and all Astra clauses unchanged.
  Original SHA-256: `b8c66449ff6d4b2a2e89e0ec40bef33f7f955769f8ca3768a5fa2de4a41b3bc2`.
  Revised SHA-256: `6e50baef92b2ae25ebf08b15f934228ea12f0dc053bc3ceb04f934cd926e3f98`.
- `chaos-redux-improvement-loop`: frontmatter byte-identical, all 2 fenced blocks byte-identical as a multiset, inline technical-literal multiset unchanged, and all Astra clauses unchanged.
  Original SHA-256: `633f02bb2807ce788fa77c925ff58354f869139f045cc72d5317a25c146923d8`.
  Revised SHA-256: `571c04eaedbf50457ddc5154c5bc39eab4a77fd7440f8df92d1f8f906cab30d4`.
- `chaos-redux-subagents`: frontmatter byte-identical, all 5 fenced blocks byte-identical as a multiset, inline technical-literal multiset unchanged, and all Astra clauses unchanged.
  Original SHA-256: `3a290277233b393e72e9fed2f0eecbe7bbce16f43515c03915ea5461be42aff7`.
  Revised SHA-256: `6ca2544eae0439d9a91fecf37cced2cb57aa89d96af728f421fddd7b7625c762`.

The official quick_validate.py returned “Skill is valid!” for all three skills.
All pre-existing heading texts and anchors are retained, including the moved subsection headings.
A comparison confirmed that Markdown-link targets are unchanged and every named `chaos-redux-*` skill reference resolves to an existing local SKILL.md.
Numbered top-level sections 1–21 retain their numbering, and existing decimal subsections retain their numbers under the appropriate hierarchy.
Conditional use of the named skills, paths, commands, examples, dimensions, values, and dispatch literals is preserved.
Folder-location guidance precedes new planning output, localisation guidance stays under writing style, and formation/UI review questions precede the final rejection review.
The two flags clarifications are the only prose corrections.
A file-writing attempt through apply_patch failed without changing a file, so bounded UTF-8 writes applied the reviewed changes.
Those writes initially introduced CRLF through Python on Windows, which the byte audit caught and restored to the original LF before final checks.
No behavioral forward test, production workflow, viewer, engine, or live-game validation was executed for this editorial task.
No gameplay simplifications were made.

## Passage-level preservation map

Ranges below are one-based original and revised line numbers.
Every nonblank original passage is mapped.
“Preserved” includes heading-level changes and corrected Markdown list indentation but no body text change.
Consecutive preserved passages with consecutive destinations are grouped, while moves have separate ranges.
Blank-line reductions have no instruction content.
C1/C2 are the evidenced corrections above, and D1 is the genuine exact duplicate merge.

### chaos-redux-event-planning

Complete coverage: 673 original passages mapped to revised passages.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–31 | 1–31 | preserved |
| 33–1361 | 53–1381 | preserved |
| 1363–1374 | 1383–1393 | D1 exact duplicate merge |
| 1376–1593 | 1395–1612 | preserved |
| 1595–1748 | 1635–1788 | preserved |
| 1750–1767 | 1790–1807 | C1 |
| 1769–1855 | 1809–1895 | preserved |
| 1857–1869 | 1901–1913 | preserved |
| 1871–1889 | 1614–1632 | preserved |
| 1891–1893 | 1897–1899 | preserved |
| 1896–1914 | 33–51 | preserved |
| 1916–2092 | 1915–2091 | preserved |
| 2094–2108 | 2136–2150 | preserved |
| 2110–2151 | 2093–2134 | preserved |
| 2153–2291 | 2152–2290 | preserved |

### chaos-redux-improvement-loop

Complete coverage: 118 original passages mapped to revised passages.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–46 | 1–46 | preserved |
| 48–72 | 80–104 | preserved |
| 74–86 | 48–60 | preserved |
| 88–104 | 106–122 | preserved |
| 106–122 | 62–78 | preserved |
| 124–175 | 124–175 | preserved |
| 177–247 | 179–249 | preserved |
| 249–249 | 251–251 | C2 |
| 251–287 | 253–289 | preserved |

### chaos-redux-subagents

Complete coverage: 140 original passages mapped to revised passages.

| Original lines | Revised lines | Disposition |
| --- | --- | --- |
| 1–79 | 1–78 | preserved |
| 81–209 | 82–210 | preserved |
| 211–243 | 230–262 | preserved |
| 245–261 | 212–228 | preserved |
| 263–363 | 266–364 | preserved |
