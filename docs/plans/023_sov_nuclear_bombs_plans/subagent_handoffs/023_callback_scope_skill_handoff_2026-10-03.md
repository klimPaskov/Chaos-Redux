# Callback scope skill maintenance handoff

Disposition: implemented for this bounded skill change.
Acceptance basis: the parent explicitly authorized concise reusable guidance for caller-versus-ROOT scope, exact nonce mirrors, actor-owned asynchronous pointers, and same-identity owner/holder accounting.
This handoff does not establish completion of Event 023 or validate its runtime behavior.

## Changes and preserved ownership

Updated `.agents\skills\chaos-redux-events\SKILL.md` only in the existing `Country activation and ROOT` section.
Added lines 478–488, with a separating blank line at 489, as observed after the patch.
The addition contains 208 words and no event-specific identifiers, paths, balance values, or history.
The patch also serialized the existing context lines 477 and 490 with LF endings, without changing their wording.
Comparison against the in-memory pre-edit snapshot confirmed that all pre-existing text outside the insertion was preserved.
The updated skill SHA-256 is `C8AF998498461944A7419371D4F8236FE216F6A1E235CE1E331C15C80FB6B7A7`.

| Added line | Reusable guidance |
| --- | --- |
| 478 | Native annex and state-control callback ROOT/FROM bindings. |
| 479–480 | Trace the actual callback-to-helper chain and read the calling owner's receipt through PREV only inside the state entered from that country. |
| 481–482 | Return to the state for state flags inside stored-owner/holder country scopes, while retaining valid ROOT uses and nesting-specific PREV meanings. |
| 484 | Match actor/state nonce mirrors and exact source-state identity before closure or accounting. |
| 485–486 | Persist asynchronous project pointers on the actor, revalidate site identity/holder at resolution, and isolate dead-actor cleanup from another living actor's selection. |
| 487–488 | Partition owner/holder accounting even when their identities coincide, and review matching/stale nonce, repeated closure, and cleanup cases through exact call chains. |

Used `skill-creator`, `chaos-redux-subagents`, and `chaos-redux-events`.
Read current `AGENTS.md` and both requested repo skills completely.
Checked decisions-missions and state-ledgers only to establish routing and existing coverage.
Their finite population-release and custody guidance does not cover these callback receipts.
Left those skills, subagent routing, and AGENTS.md unchanged.
Created no new skill or skill-local workflow.
No routing or generated-definition update is needed.

## Reasoning and source call-chain evidence

Repository evidence below was inspected read-only.
All mod-relative paths resolve under `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

| Source and lines | Observed chain and implication |
| --- | --- |
| `common\on_actions\023_sov_nuclear_bombs_on_actions.txt`, 39–56 | State-control callback enters FROM.FROM and invokes state reconciliation while ROOT remains the new controller. |
| Same file, 71–86 | Annex callback enters FROM and invokes annexed-country cleanup while ROOT remains the winner. |
| `common\scripted_effects\023_sov_nuclear_bombs_runtime_effects.txt`, 1673–1693 | Country assembly closure enters its stored source state and compares the state nonce with PREV's country nonce. |
| Same file, 2033–2060 and 2064–2076 | State callback cancellation enters SOV, whose country closure enters the stored dismantlement state and compares its mirrored nonce with PREV's owner nonce. |
| Same file, 3033–3059 | Annex cleanup invokes country receipt closure and clears local custody pointers, with shared selection cleanup gated to its owning country. |
| Same file, 1400–1500 and 1541–1586, with the missing-disposition definition located at 1504 | Dismantled/missing dispositions enter recorded-owner and holder country pointers from the state and inspect the operationalized state flag through PREV, partitioning operational accounting. |
| `common\scripted_triggers\023_sov_nuclear_bombs_event_triggers.txt`, 660–673 | Assembly validity compares exact state ID and nonce mirrors against the calling country. |
| Same file, 1050–1070 | Local project validity checks the actor-owned state pointer and ID, registration, state disposition, physical holder, and territorial authority. |
| `common\scripted_effects\023_sov_nuclear_bombs_event_effects.txt`, 3047–3123 | Each asynchronous local project completion rechecks that validity trigger before applying its stage outcome. |
| `common\on_actions\023_sov_nuclear_bombs_on_actions.txt`, 98–111 | Native-launch receipt validation intentionally reads ROOT as launcher, confirming that a blanket ROOT-to-PREV substitution is incorrect. |

The source review supports the reusable scope distinction and the parent's supplied experience.
It is not an independent full gameplay audit or observed engine execution.
Matching and stale nonce, owner-equals-holder, repeated closure, and dead-actor cases were reviewed as call-chain invariants, not executed simulations.

## Documentation and revisions

| Reference | Read lines | SHA-256 revision |
| --- | --- | --- |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 260–263, 811–838 | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md` | 257 and adjacent rows, 450 and adjacent example | `6822ADC85A374A1C1364F2DEF6F32C6D66DA9FB0280319DDD6AF4B84B33D882A` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263–288, 426–443 | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\on_actions\00_on_actions.txt` | 1615–1624, 5075–5084 | `52A751456F1774AD5001C86D41D4E46494F751D79B6C224B6CD4C0EEBB615EB9` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 2733–2751, 6505–6518 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |

Installed `00_on_actions.txt` comments explicitly bind annex ROOT to the winner and FROM to the annexed actor, and state-control ROOT to the new controller, FROM to the old controller, and FROM.FROM to the state.
The offline scope reference defines PREV by the containing scope rather than actor identity.
The global-target references explain why clearing a global selection from a dead actor's scope can still affect a living actor.

| Reviewed mod source | Observed SHA-256 |
| --- | --- |
| `common\on_actions\023_sov_nuclear_bombs_on_actions.txt` | `B8B9E20220CE345540C2160B8948D9D21376618DE9AAD0C54D9ED6B4B61DC39E` |
| `common\scripted_effects\023_sov_nuclear_bombs_runtime_effects.txt` | `89BDD16A12D23DBFFEDFE31806CC5E0E7ECF7F909412806C134A20588492A9A3` |
| `common\scripted_effects\023_sov_nuclear_bombs_event_effects.txt` | `C590E8E883D375702500E321E8B81B29EB03E9A88C71E3458673EF25E4FBF2CB` |
| `common\scripted_triggers\023_sov_nuclear_bombs_event_triggers.txt` | `90D44CC3BE29BC20971489031B3B94A8417658274A70C69629B0A9A789DC9D1E` |

These are observed revisions in a concurrent working tree, not immutable fixtures.
The parent must review its final source revisions.

## Validation limits and MCP findings

The official skill validator returned `Skill is valid!`.
The pre-edit snapshot comparison verified preservation of existing wording, including concurrent skill changes.
No gameplay, localisation, asset, workbook, staged index, or commit mutation was performed.
No game launch, log search, service restart, or validation flag was introduced.

Verified exposed live schemas for `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
The connected source-lookup schema accepts symbol/kind and bounded line reads, but exposes no view/keyPath structure arguments.
`hoi4.script_validate` is absent from the exposed tool list.
Tool exposure does not establish service health or runtime correctness.

Reference context and reference search returned `OK` for workspace `mod_chaos_redux_ea3b2d67c2c0`.
Context reported no missing files but omitted sources including On actions and Data structures, so pertinent sections were read locally as recorded above.
It identified Scopes/Dual scopes at lines 245–328 with revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`.
Search identified Scopes/PREV usage at lines 811–872 under the same revision.
The installed on-actions documentation heading spans lines 1–6 with revision `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4`.
Those six installed-documentation lines were read locally and contain only a heading/update note, so callback contracts were checked in installed vanilla source comments.

Three bounded reference-read calls requested Scopes lines 260–263, PREV usage lines 811–826, and the installed documentation heading lines 1–6 using the returned IDs and revisions.
They produced no result before the waiting orchestration was terminated.
Their remote outcomes remain unknown, and no reference-read success or server cancellation is claimed.
No source-lookup retry was made after the parent reported two 600-second timeouts, including the bounded 12-line retry.
That timeout history is parent-supplied evidence, not a new timeout observed by this subagent.
Successful context/search retrieval is documentation evidence only.
No engine proof, event lifecycle validation, or runtime scenario pass is claimed.

## Remaining risks and parent handoff

Skill maintenance is complete with no simplifications.
No skill conflict with AGENTS.md was introduced.
The parent retains final source review, required event/probability audits, evidence reconciliation, full-spec completion, and focused commits.
Recheck the actual scope chain if any helper gains another scope layer, and preserve ROOT where the receiving event or native callback contract requires it.
The parent's final audit still needs to cover stale and matching nonce mirrors, equal and distinct owner/holder identities, repeated disposition/closure, and dead-actor selection isolation.
MCP source-lookup timeout history, unresolved reference-read outcomes, and absent script validation remain explicit evidence limits rather than fake acceptance gates.
