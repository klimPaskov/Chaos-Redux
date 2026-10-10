# Event 105 Random Idea: scripted-system feasibility handoff

## Parent disposition after research

The parent accepts the complete effective-loadout generated registry as the next implementation route if a supported complete native runtime enumerator is not established.
This acceptance is within the user's explicit request to investigate generated or load-time approaches before a maintained pool.
The original proposal-for-acceptance wording retained below is superseded on acceptance status only.
All native discovery, duplicate-definition, category, dispatch, identity-persistence, installed-documentation, and MCP evidence gaps remain open implementation gates.
No smaller maintained, curated, source-limited, or opt-in-only pool is authorized by this disposition.
The final design also freezes C, the recipient roster, every recipient's B, and the effective evolution stage before the first global dispatch.
Current ownership is refreshed per draw.


## Status and authority

Design-only research by `chaosx_scripted_system_architect`.
Parent task constraints govern: all loaded technically addable national ideas; no thematic, ideology, country, usefulness, compatibility, or DLC entitlement curation; owned identities excluded only for fresh distinct draws.
Global source gate passed at 2026-10-09 19:47:17 UTC before this research.
Repository evidence is pinned to `klimPaskov/Chaos-Redux` master commit `a3ef485c5da7e2337122eca04ac65c175050f251`.
No gameplay, scripts, localisation, UI, spreadsheets, or repository implementation was changed.
Sources and blob identities are in `architect_evidence.json`; offline page copies are retained in `offline_refs/`.

Read role TOML, all current AGENTS.md and subagents guidance, relevant event helper-output/transaction/MCP/constant sections, current dynamic-effect API, and targeted offline references.
HOI4 tool-name discovery returned zero exposed routes.
Required `hoi4.reference_context/search/read`, `source_lookup`, `script_validate`, `event_inspect` and `probability_inspect` therefore cannot be called here.
The requested installed Windows documentation directory is unavailable in this Linux workspace; no matching installed documentation basename was found under this task workspace.
These are explicit evidence gaps; offline source reading is not engine validation.

## Main finding

True runtime discovery remains preferred but unverified.
The supplied offline database-array reference does not document any all-ideas array or iterator.
It documents `global.technology`, countries, states, ideology groups and operations, but no equivalent ideas database [R1:1779–1815].
This does not prove the current engine lacks a newer or undocumented iterator: token sections explicitly discuss version 1.12 while the repo descriptor declares 1.19.*, so installed documentation and native inspection are decisive.
Do not assert that `global.ideas`, `global.idea`, a country-owned array, or a union of countries' owned ideas is complete.
Repo code search for `global.ideas` returned no indexed results, a weak negative only.

Tokens solve passing a KNOWN identity, not discovering UNKNOWN definitions.
The offline reference documents `token:<id>`, token equality and `GetTokenKey`, and includes ideas among tokenizable database types [R1:955–983].
It also says raw language tokens such as native-effect names can tokenize [R1:985].
Walking internal numeric IDs or the generic token-string table cannot identify national ideas, completeness, categories or addability.
Ideas have no idea-object scope [R1:551], so `random_scope_in_array` is not established as an idea-token selector.

If no supported complete runtime enumerator is found, a generated registry of the complete EFFECTIVE active loadout is a feasible design candidate, subject to load-resolution and exact native dispatch proof.
A shipped Chaos-only list, vanilla-only list, curated bundle, opt-in registration bus or country-owned union would fail the requested universe.
The existing CXT extension bus is opt-in and intentionally applies only registered package setup; it demonstrates token dispatch, not discovery [R7:100–124].

## Technical pool membership

| Definition class | Evidence and treatment |
| --- | --- |
| `ideas/country` national spirits | Include all loaded distinct IDs technically recognized as directly addable national spirits. Empty definitions are explicitly addable [R2:30–45]. |
| `hidden_ideas` national spirits | Include when technically addable: the reference describes these as ordinary spirits whose display is hidden [R2:317–319]. No icon, modifier, usefulness or intended visibility test. |
| Other mod-defined categories | Inspect the effective `idea_tags` category and engine behavior. Do not assume only literal `country` and `hidden_ideas` cover custom national-spirit categories. Unresolved type classification requires evidence rather than invented exclusions. |
| Laws, designers, officer-corps slots | They are ideas but not automatically national spirits. Native addition to a single slot replaces its existing idea [R3:1971–1985]. Exclusion from a NATIONAL-idea mechanic follows actual type, never theme or compatibility. |
| Modern character advisors / character-slot dummy definitions | Category `character_slot` differs from idea `slot` [R2:405–442]. Cost-factor dummy ideas in character slots are described as never appearing for countries [R2:485]. Do not include all tokens merely because they occur under `common/ideas`; installed native behavior still needs confirmation. |
| Empty hidden carrier / dummy in a spirit category | Intended use as a carrier does not establish inability to add it. Actual `chaosx_cxt_extension_event012_africa_gods` is an empty hidden idea [R8:1–13]; it stays eligible if technically addable even though CXT documentation says its own dispatcher never applies it. |
| Missing, replaced-away, malformed or technically non-addable definition | Not in the loaded addable universe. Record exact technical evidence; no name-prefix blacklist or speculative compatibility exclusion. |

The reference says `add_ideas` bypasses an idea's `allowed` selection check [R2:344–354].
Consequently, country/ideology/DLC selection predicates are not permissible pool filters.
`do_effect` false suppresses modifiers without removing the idea [R2:247]; that is not proof of addition failure.
Cancellation, zero modifiers, missing artwork, callbacks that alter other systems and instant self-removal must not become usefulness or compatibility filters.

Concrete caution: `common/ideas/zzz_chaosx_vanilla_error_fixes.txt` places `TUR_nuri_demirag` under `country` [R9:1–9].
A name that resembles an advisor or carries a country tag cannot determine its loaded type.

## Complete registry requirements

1. Capture the game build, actual enabled mod descriptors and resolved order, relevant user-directory overrides, DLC mounts/disabled DLC list, paths and source hashes.
An installed-mod directory is not an active-playset manifest.
2. Resolve the effective virtual files BEFORE collecting IDs.
Same relative-path files are selected by load order; later files replace earlier whole files [R4:257–278].
Dependencies alter mod order.
`replace_path` unloads earlier indexed files in the specified folder and does not change order; later mods can contribute again [R4:511–519].
Preserve actual case-sensitive/case-insensitive behavior rather than silently normalize it; the reference reports double loading for capitalization-only filename variants [R4:559].
3. Parse ideas and effective idea categories structurally.
Resolve file evaluation order separately from overlay order.
The reference documents filename character ordering, then expressly says duplicate database-entry winners vary by database [R4:280–288; R2:477–485].
There is no source here proving whether duplicate IDEA IDs across different surviving files use first, last, merge, or invalid behavior.
Do not substitute generic “last mod wins” for that missing fact.
4. Deduplicate by exact loaded identity, not by file occurrence, localisation label, stage family or source provenance.
Each identity gets one probability share regardless of how many files mention it.
Retain provenance and duplicate-resolution evidence.
5. Account for DLC content actually loaded.
The snapshot says DLC script usually lives in base files behind `has_dlc`, while DLC directories often supply assets [R4:269–278].
A purchase-locked UI definition may still load and be addable through native assignment.
Do not remove such an idea solely because DLC is disabled or unowned; only actual non-loading or technical inability changes membership.
6. Bind registry to the complete effective loadout.
Regenerate/reconcile when game, mod source, category definitions, descriptor order, replacement paths or mounts change.
An unknown or stale universe cannot be silently advertised as ALL.

Chaos's pinned descriptor replaces only `gfx/loadingscreens` [R10:1–12].
This does not establish any other active mods or whether the user's machine-specific descriptor matches it.

## Uniform fresh draws and callback lifecycle

Use one share per distinct currently eligible identity.
Eligibility at each fresh draw is structural loaded national-idea addability minus identities currently owned and identities already directly selected in this invocation.
A stage, hidden identity and negative national spirit have the same share as every other eligible identity.
The offline `random_list` reference explicitly normalizes weights by total weight [R3:4518–4562].
A generated flat equal-weight candidate list is therefore a documented candidate design; syntax, scale/performance and ownership gating need native proof.
If segmented selection is needed, choose segments proportional to their current eligible identity count, then uniform within segment: equal segment weights would bias IDs.
Do not cap the pool at a loop ceiling or truncate a registry suffix.

An integer random-index design is another candidate: `set_variable_to_random` documents inclusive minimum and exclusive maximum with integer mode [R1:564–595].
That range alone does not establish current engine uniformity, numeric precision, dynamic maximum parsing or array-token dispatch.
Do not use rounded floating draws without proving equal endpoint probabilities.

Native `on_add`, `on_remove`, `cancel` and civil-war inheritance are part of the selected definition's normal behavior [R2:218–247].
The source establishes those callbacks exist but does not establish their exact execution ordering relative to the caller's next effect.
Arbitrary callbacks can mutate ownership, replace themselves, invoke other systems or re-enter Event 105.
They prevent a claim of globally reversible atomic addition.

Parent's proposed semantics are sound with this qualification:
record an exact direct-dispatch receipt once structural/native preflight has established the ID and before native dispatch, so synchronous re-entry cannot consume the same draw.
A technical failure proved BEFORE dispatch may search the remaining exact pool.
After dispatch begins, uncertain execution, immediate absence, replacement or normal cancellation must never trigger retry, rollback or compensating removal.
Report direct selected/dispatched identity and retained presence separately.
Without an engine success return or a witnessed callback receipt, “dispatch performed” is not proof of delivered/retained idea.
Missing after the call is not proof that nothing occurred.

For multiple fresh draws, recheck current ownership between native dispatches because callbacks can grant another pool identity.
Record only Event 105's direct selected identities; a before/after ownership difference cannot prove which callback granted a foreign identity.
Parent's burden set `B = historical Event-105 directly drawn identities intersect currently owned identities` is honest and computable.
It excludes originally held identities that were skipped and does not claim uninterrupted causal ownership.
Loss and later re-addition of the same identity can return it to B under the explicitly chosen semantics.

Persist identity semantically by the stable idea STRING key and loadout identity, not a raw internal numeric token ID or dense registry ordinal alone.
This is an identity requirement, not a claim that native HOI4 variables can store arbitrary strings.
Implementation must prove that saved token values rebind by their key, or provide generated stable keyed storage plus an explicit migration map; neither persistence mechanism is established by these sources.
Token IDs are indexes into an engine-memory table [R1:957]; persistence/rebinding across changed loadouts is unverified.
A generated ID-to-token reconciliation map needs evidence after save/load and loadout changes.
Unknown historical IDs must retain unresolved history rather than resolve to another index.

## Proposed narrow helper contract

These are design names, not implemented code.
Keep Event 105 orchestration owner-local rather than expanding shared dynamic helpers without reusable callers.

| Helper | Scope / inputs | Outputs / side effects |
| --- | --- | --- |
| `random_idea_validate_universe` | Country; current engine/registry loadout identity | Caller-owned ready/status and exact universe count; no gameplay grant. |
| `random_idea_collect_fresh_pool` | Country; complete universe and invocation-selected set | Caller-owned exact candidate IDs/count; only ownership and distinctness exclusion. |
| `random_idea_draw_fresh_identity` | Country; exact complete candidate set | Caller-owned selected stable identity and token/dispatch mapping; equal identity shares. |
| `random_idea_dispatch_selected` | Country; request generation, exact selected ID, structural mapping | Exact once dispatch receipt, separate immediate retained-status; native callbacks allowed, no retry/rollback after dispatch. |
| `random_idea_refresh_owned_drawn_set` | Country; historical direct-draw IDs | Current B membership only; no provenance claims, no idea removal. |

Caller initializes consumed temporary scalar/array output storage before every helper and nested call [current events skill:175–196; R1:438–442].
Use request-generation identity and country-owned immutable receipts where callback re-entry crosses frames.
Scope pointers are country targets; idea identities remain tokens/strings, not event-target scopes.
Do not clear original ownership, remove native ideas or rewrite normal callbacks as cleanup.
Release working arrays and request locks through owner-local completion paths; lifecycle behavior under country death, annexation, tag switches and civil war remains a probe, not an established solution.

Shared constants can cover documented operation/result kinds and batch sizes.
A batch size controls work per call only, never eligible universe size.
AGENTS and the offline reference document a native 1,000-iteration limit for relevant loops [R1:1219,1828].
Chunking must preserve unvisited suffixes and exact candidate counts.
No permitted helper here adds daily whole-world scans, choices, currency or curated packages.

## Meaningful future acceptance probes

- Installed `dynamic_variables_documentation`, script-concept/effects/triggers docs: identify any complete ideas database array/iterator, scope, element type and DLC/mod coverage; compare against effective-source ground truth including never-owned and event-inactive ideas.
- Dynamic known-ID dispatch: country spirit, negative foreign-country spirit, false `allowed`, false `visible/available`, hidden spirit, empty hidden carrier, false `do_effect`; contrast a law, advisor character and character-slot dummy only to establish type/addability.
- Duplicate-ID and overlay fixtures: same-path overwrite; different-file same-ID definitions; reversed filename order; descriptor dependency; `replace_path`; DLC mount; case variants; custom `idea_tags` slot. Verify native loaded winner/category, not parser assumptions.
- Universe sizes 0, 1, several and greater than 1,000; all owned; exactly one unowned; duplicates; source added/removed. Prove no suffix loss, wrong all-owned behavior or hidden selection curation.
- Probability fixtures: all equal shares, uneven bucket sizes, ownership exclusions and multiple draws without replacement. Require specialized MCP audit when available; mathematical reasoning here is not its substitute.
- Callback fixtures: on-add self-removal, swap, grant-next-candidate, nested Event-105 dispatch, instant cancel/on-remove, country change and save/reload. Verify once-only callback execution and separate dispatched/retained reporting.
- Historical identity fixtures: reorder registry, remove definition, change mod loadout, loss/re-add same idea and civil-war inheritance; verify stable identity and B semantics without dense-index aliasing.

## Reference key

All line spans refer to the pinned repository's files, not public Paradox Wiki.
R1 `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, blob `1b8b456c1a7d0981d4a4827ab72c6e521d57d8c3`.
R2 `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`, blob `799583fa68bc85f8834e3d79d5bb1d438775f25a`.
R3 `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, blob `afc9255950157681d0202484f20d06cea9bd747c`.
R4 `paradox_wiki/Modding - Hearts of Iron 4 Wiki.md`, blob `b7b48e2380af9d548c0c15ede5a817b78cd4b2e1`.
R5 `paradox_wiki/Mod structure - Hearts of Iron 4 Wiki.md`, blob `552d50dea9a30f8d2edb52a22e4fe242c1f69c24`, dependency discussion read at 87–100.
R6 `common/scripted_effects/chaosx_dynamic_effects.txt`, blob `06e1b00524b565f1a6421bc6c9db720193ab69db`; existing API offers no all-ideas enumerator in the inspected token/array/helper surface.
R7 `docs/testing/chaosx_test_country.md`, blob `e1b10f9f5630d83d76f36319d75183fb263da6c3`.
R8 `common/ideas/012_africa_gods_cxt_extension_ideas.txt`, blob `98993eab53d393cbd53c02979583d7450610df8a`.
R9 `common/ideas/zzz_chaosx_vanilla_error_fixes.txt`, blob `c0268d0d552682dcb311f38d022937a91b23fdf6`.
R10 `descriptor.mod`, blob `a34850ccb69ea1018beb661729af8320cb982520`.
R11 `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, blob `b9bb6c3821141ac07732bfbca4b9c7615ee8d972`; `has_idea` at 910 tests current ownership, not a successful-add receipt or database completeness.

No design simplification was adopted.
Implementation readiness is blocked by complete current-engine discovery/addability/load-resolution proof and the absent mandatory MCP/installed-documentation evidence.
The complete-loadout registry route is a proposal for parent acceptance, never an undisclosed narrower fallback.

