# Event 023 achievement asset documentation reconciliation

Date: 2026-10-03.
Role: `chaosx_documentation_curator`.
Disposition: `implemented` documentation reconciliation for the selected achievement artwork replacement.
Live consumer status remains `needs_user_review`.
No gameplay completion, live-game acceptance, original-prompt recovery, commit, or staging is claimed.

## Exact scope and acceptance basis

The parent requested reconciliation of the completed Event 023 achievement artwork replacement in the Chaos Redux repository at `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
The authorized write scope was four named asset documentation files, the asset section and 21 achievement rows in `docs/events/023_sov_nuclear_bombs.md`, and this new Event 023 plans handoff.
The current request explicitly reports user authorization for fresh generation and replacement after the original prompt file was absent from checkout and history.
It also supplies the selected seven lineages, completed parent review of all v1/v2 native64, 4x, lineage, alpha sheets and full selected sources, 21 completed runtime copies, and 21/21 SHA-256 equality to selected candidates.
These statements and the runtime promotion handoff establish acceptance within the artwork scope.
Spec locations, dated status labels, candidate-worker observations, and the existence of runtime files do not establish acceptance of other design claims.

The curator used `chaos-redux-event-assets`, `chaos-redux-events`, and `chaos-redux-subagents` after reading `AGENTS.md`.
The asset skill's state-layer, versioned-lineage, template, crosswalk, and parent-review rules guided the selected chains and historical notices.
The events and subagents rules guided the bounded event-doc edits, acceptance evidence, dispositions, and parent handoff.
No additional subagent was spawned.

## Source-of-truth map

| Evidence class | Source | Authority and limit |
| --- | --- | --- |
| Explicit user direction and parent acceptance | Current reconciliation request | Authorizes fresh artwork replacement, supplies the selected lineages and completed parent static review, restricts edits to documentation, forbids a commit, and keeps live review pending. |
| Selected runtime transaction | [Runtime promotion handoff](023_achievement_icon_runtime_promotion_2026-09-26.md) | Records seven selected triplets, 21 copies, 21/21 runtime/candidate SHA-256 matches, stable identifiers and wiring, and no live acceptance. |
| Current exact inventory | [Selected 21-state crosswalk](../../../assets/023_sov_nuclear_bombs/notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26.md#current-selected-runtime-crosswalk) | Lists 21 exact master, state-layer, preview, candidate, runtime, and alias chains. |
| V1 source and processing evidence | [V1 artist handoff](023_icon_artist_replacement_2026-09-26.md), verbatim v1 replacement prompts, v1 processor log and sheets | Retains seven candidate triplets and all focused-edit branches, with four subsequently selected and three superseded. |
| V2 source and processing evidence | [V2 artist handoff](023_icon_artist_replacement_2026-09-26_v2.md), verbatim v2 prompts, v2 processor log and sheets | Retains three fresh candidate triplets, all subsequently selected. |
| Current local linkage and byte evidence | `interface/chaosx_achievements.gfx:1588` through line 1608 and the selected candidate/runtime DDS paths | This reconciliation checked 21 exact alias/destination pairs and 21/21 SHA-256 matches, without changing source or art. |
| Historical recovery evidence | The 2026-09-25 recovery paths and audit links preserved in the manifest, GFX handoff, and event asset section | Describes the previous artwork package and its then-current runtime equivalence, with current inventory claims superseded. |
| Missing original provenance | `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set.md` | The current request and artist handoffs report absence from checkout/history, and this reconciliation confirms the path remains absent. |
| Engine and live consumer evidence | MCP attempts below and the parent/user review boundary | No new MCP artifact or live consumer acceptance was obtained. |

## Selected runtime set

| Achievement ID | Selected lineage | Disposition and evidence |
| --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | v2 `GEN-08` | `implemented` artwork replacement, accepted by parent selection in the current request and recorded in the promotion handoff, with all three runtime hashes matching selected candidates and live status `needs_user_review`. |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | v2 `GEN-09` | `implemented` artwork replacement, accepted by parent selection in the current request and recorded in the promotion handoff, with all three runtime hashes matching selected candidates and live status `needs_user_review`. |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | v1 `GEN-03` | `implemented` artwork replacement, accepted by parent selection in the current request and recorded in the promotion handoff, with all three runtime hashes matching selected candidates and live status `needs_user_review`. |
| `023_sov_nuclear_bombs_scattered_arsenal` | v1 `EDIT-04A` | `implemented` artwork replacement, accepted by parent selection in the current request and recorded in the promotion handoff, with all three runtime hashes matching selected candidates and live status `needs_user_review`. |
| `023_sov_nuclear_bombs_firebreak` | v1 `EDIT-05A` | `implemented` artwork replacement, accepted by parent selection in the current request and recorded in the promotion handoff, with all three runtime hashes matching selected candidates and live status `needs_user_review`. |
| `023_sov_nuclear_bombs_first_and_last` | v2 `GEN-10` | `implemented` artwork replacement, accepted by parent selection in the current request and recorded in the promotion handoff, with all three runtime hashes matching selected candidates and live status `needs_user_review`. |
| `023_sov_nuclear_bombs_the_last_telephone` | v1 `GEN-07` | `implemented` artwork replacement, accepted by parent selection in the current request and recorded in the promotion handoff, with all three runtime hashes matching selected candidates and live status `needs_user_review`. |

V1 GEN-01, GEN-02, and GEN-06 are `superseded` by v2 GEN-08, GEN-09, and GEN-10.
The reasons were the unrequested cabinet star, the bomb occupying the supposedly empty cradle, and the unreadable wrench-cloud reflection.
All sources and intermediate branches remain retained at their versioned paths.

## Files changed and document dispositions

| Edited document | Disposition | Acceptance basis, evidence, and reason |
| --- | --- | --- |
| `docs/assets/023_sov_nuclear_bombs/manifest.md` | `implemented` current inventory, historical candidate/recovery inventory claims `superseded` | Parent-selected three-v2/four-v1 set and promotion handoff replace the stale no-promotion claim, with the exact current crosswalk named as replacement and dated records preserved. |
| `docs/assets/023_sov_nuclear_bombs/gfx_handoff.md` | `implemented` current achievement wiring record, historical recovery inventory `superseded` | Stable 21 alias/destination pairs and selected runtime hashes support current linkage, with the selected crosswalk and promotion handoff replacing old recovery source chains. |
| `docs/assets/023_sov_nuclear_bombs/notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26.md` | `implemented` current 21-state crosswalk, original candidate inventory `superseded` | Explicit user authorization and parent selection establish the artwork acceptance basis, with 21 exact selected chains replacing candidate-only mappings and historical tables retained. |
| `docs/assets/023_sov_nuclear_bombs/notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26_v2.md` | `implemented` three selected v2 triplets, no-promotion statement `superseded` | Parent selects GEN-08/09/10, and the promotion handoff plus current 21-state crosswalk identify the nine runtime states and their validation limit. |
| `docs/events/023_sov_nuclear_bombs.md`, asset section and 21 achievement rows only | `implemented` artwork documentation reconciliation, old achievement inventory `superseded` | Exact selected source, state-layer, preview, candidate, runtime, and alias chains replace recovered-master chains, with parent selection and promotion evidence recorded independently of live acceptance. |
| This handoff | `implemented` documentation audit and reconciliation record | Records the authorized scope, source-of-truth map, dispositions, contradictions, validation, and unresolved limitations for parent review. |

No documents were merged or deleted.
The two candidate handoffs and the promotion handoff were read and left unchanged as dated evidence.
The replacement prompt files were read and left byte-for-byte unchanged.
The gameplay sections, specs, workbook, runtime artwork, other event docs, and unrelated concurrent edits were outside the write scope.

## Plan, handoff, and provenance disposition table

| Record or outstanding item | Disposition | Basis and next owner |
| --- | --- | --- |
| `023_icon_artist_replacement_2026-09-26.md` | Production evidence `implemented`, candidate-only current inventory `superseded` | Four selected v1 lineages were promoted, and three were superseded by the v2 handoff and selected inventory, with the original dated handoff preserved. |
| `023_icon_artist_replacement_2026-09-26_v2.md` | Production evidence `implemented`, pending-promotion claim `superseded` | Three v2 triplets were accepted by the parent and promoted, with the runtime promotion handoff as the named replacement for current status. |
| `023_achievement_icon_runtime_promotion_2026-09-26.md` | `implemented` runtime promotion evidence | The current parent request and local 21/21 hash checks agree with its selection and stable destinations, with live acceptance pending. |
| Original `prompts/icon_prompt_set.md` provenance | `unresolved` | The original remains absent from checkout/history, and no reconstruction is authorized or claimed. |
| New verbatim v1/v2 replacement prompts | `implemented` replacement provenance | Explicit authorization after the original was missing establishes their role as new provenance, with exact text retained unchanged. |
| Live HOI4 achievement consumer acceptance | `unresolved` | Parent static review is recorded, and live status remains `needs_user_review` under the user-owned acceptance boundary. |
| Fresh MCP source/inspection artifact | `blocked` for this reconciliation | The exact no-result routes below produced no usable artifact, revision, or service-health evidence. |
| Explicit staging of ignored asset evidence | `accepted and queued` | The parent expressly owns scoped force-add through the shared-Git workflow, and this task forbids a commit. |

No gameplay plan was promoted into an accepted spec, queued, rejected, or otherwise reclassified.
No unresolved spec acceptance was inferred from the historical crosswalk's spec path.

## Contradictions resolved and still open

| Path | Previous conflicting claim | Resolution or remaining limit |
| --- | --- | --- |
| `docs/assets/023_sov_nuclear_bombs/manifest.md` | No replacement candidate was promoted, and previous recovered package DDS matched current runtime. | Records the selected seven promoted triplets and marks old candidate/recovery inventory as historical and superseded. |
| `docs/assets/023_sov_nuclear_bombs/gfx_handoff.md` | Current achievement sources and runtime equivalence came from the unchanged recovered-master package. | Points to selected versioned replacement chains and separates the dated recovery comparison. |
| Both replacement crosswalks under `docs/assets/023_sov_nuclear_bombs/notes/` | All versions still awaited selection and no version was promoted. | Current 21-row crosswalk and v2 status record completed parent selection and promotion, with historical staging records retained. |
| `docs/events/023_sov_nuclear_bombs.md`, achievement rows | All 21 rows described recovery inputs with runtime DDS unchanged by that recovery. | All 21 rows identify selected replacement masters, processed inputs/previews, candidates, and stable runtime files. |
| Missing original prompt path | Earlier source claims cite a prompt file that is absent. | Remains unresolved historical provenance, with new authorized replacement prompts identified separately. |
| Parent static review versus live acceptance | A completed source and template review could be mistaken for in-game sign-off. | Every current selected inventory retains live consumer status `needs_user_review`. |

No conflict among the seven parent selections remains open.
The missing original provenance and absent fresh engine/live evidence remain explicit limitations.

## Duplicate, superseded, and stale instruction inventory

The manifest's v1/v2 tables and the historical candidate crosswalks remain dated evidence rather than parallel current inventories.
The current 21-state crosswalk is the named replacement for their current inventory claims.
The v2 crosswalk retains its three-ID correction record and links to the full selected inventory.
The 2026-09-25 source recovery chains and package/runtime review sheets remain historical evidence.
The original candidate handoffs still contain stage-time instructions to await parent selection and promotion, which are superseded for these seven selections by the promotion handoff and this reconciliation.
The v1/v2 prompt headers remain their original candidate-stage provenance records and are not outstanding generation assignments.
No prompt body was changed, no generation was repeated, and no historical lineage was erased.

## Markdown hard-wrap audit

The four edited asset documents, the edited event asset section, and this handoff use complete prose sentences on physical lines.
No accidental mid-sentence or mid-clause hard wraps were found in the scoped pre-existing Markdown.
Reconciled prose was written sentence-by-sentence without introducing hard wraps.
Paragraph boundaries, headings, lists, tables, fenced code in the retained evidence, and historical quotations remain intact.
The 54 ordinary asset rows and all event content outside the asset section are unchanged.

## MCP routes and evidence limits

The connected tool inventory exposes `mcp__hoi4_agent_tools__hoi4_source_lookup` and `mcp__hoi4_agent_tools__hoi4_event_inspect`.
Exposure alone does not establish service health or standalone viewer availability.
A read-only source lookup for `GFX_achievement_023_sov_nuclear_bombs_a_hundred_suns` with `includeReferences=true`, `maxLines=15`, `maxDefinitions=3`, and `maxReferences=5` returned no result before the orchestration wait was terminated.
The first narrow event-inspect request was rejected with `MCP error -32602` because `selector.kind` was missing.
The corrected request used `mode="scan"`, `selector={kind:"event",eventId:"chaosx.nr23.1"}`, `maxNodes=10`, `maxEdges=10`, and `maxDepth=1`.
It returned no result within the explicit 55-second read-only request bound.
No source revision, artifact URI, continuation URI, coverage, transaction, or recovery data was returned.
The failure to obtain a result is recorded as an evidence-route blocker, without asserting that the service itself is unhealthy.
Local alias and hash checks are source/artifact evidence and do not substitute for MCP or engine evidence.
No event-chain structural comparison was performed because the task changed only artwork documentation.
Focus, technology/doctrine, GUI layouts, maps, and weighted logic were outside this reconciliation scope and were not reviewed.
No probability result or scenario-specific auditor handoff was altered or inferred.
Standalone viewer availability was not assessed for this achievement-documentation task, and no viewer capability is claimed.

## Meaningful validation

The final current crosswalk contains exactly 21 unique state rows, covering seven stable IDs and three states per ID.
Each row names an existing selected generated master, processed state layer, composited review PNG, candidate DDS, and runtime DDS.
All 21 runtime DDS files match their selected candidate SHA-256 values.
All 21 stable alias/destination pairs resolve exactly once in `interface/chaosx_achievements.gfx`.
The event document has exactly 21 achievement rows with the same six exact chain/alias references.
The 54 ordinary rows and event content outside `## Visual asset audit` compare unchanged against the pre-edit document snapshot.
The five edited existing documents compare to the expected bounded patch results.
Targeted searches confirmed the stale present-tense no-promotion and recovered-runtime statements were replaced or explicitly dated and superseded.
The original prompt path remains absent.
The replacement prompts, selected masters, processed states, candidates, and runtime assets were not edited.
The four edited `docs/assets/` Markdown files remain ignored and were not staged.

The canonical 64x64 BGRA, template equality, grayscale/overlay, and genuine-alpha audits are the inherited v1/v2 production evidence supplied by the parent and the artist handoffs.
The curator did not rerun image processors or inspect binary artwork because this task was documentation-only and supplied completed parent visual review.
No game was launched, and no live consumer test was performed.
Required fresh MCP evidence remained unavailable as described above.
No commit or shared-index mutation was made.

## Parent follow-up and remaining risks

The parent should review this documentation patch and use the selected 21-state crosswalk to continue integration without repeating generation, source recovery, selection, or promotion.
The parent owns explicit staging of final ignored evidence through its shared-Git commit workflow.
Live consumer status remains `needs_user_review`.
The absent original prompt remains an unresolved provenance limitation that must not be described as recovered.
Fresh MCP service/artifact evidence remains blocked for this reconciliation, and source-only checks must not be represented as equivalent engine proof.
Historical candidate instructions remain preserved as dated records, so future workers should follow the selected inventory and promotion handoff.
No additional artwork or design decision is required by this cleanup.
No simplification was introduced within the authorized documentation scope.

