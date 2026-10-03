# Repo Explorer Handoff

## Scope read
- Parent task: Assess the source and history route for the 29 date-gated CBRN identities, verify the dormant-holder precedent and tag-isolation risks, and report references and runtime limits.
- Explicit constraints: Read-only source research. No gameplay edits, staging, game launch, or unrelated log search. The only write in this subtask is this requested handoff.
- Skills or docs read: Supplied `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md`. The CBRN dated holder is a character history and transfer surface. Event 016 was inspected only for holder lifecycle risk.

## Primary findings
The route is supported by the installed country-scoped `set_nationality` syntax and by an existing Chaos Redux KRG transfer path. The current shared tree contains a dedicated, stateless CSH holder, 29 history recruits, and 29 guarded country-scope transfers. Source inspection confirms the current dated helpers contain zero runtime `recruit_character` calls. This source arrangement is not fresh-start engine proof.

The existing home-country history roster has 38 static recruits. The shared `history/general/chaosx_startup_character_recruitment.txt` now has 67 recruits total, split into those 38 home-country recruits and 29 CSH holder recruits. The current `common/scripted_effects/chaosx_startup_history_effects.txt` has 29 `set_nationality` blocks and zero `recruit_character` calls.

The earlier user-reported 58 main-menu warnings concerned the prior runtime-recruit implementation. The changing copy of the authorized `docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log` initially lacked those warnings in one read; the parent and country auditor later confirmed all 58 under SHA-256 `edb523793e8c7ea1c79ff53546b1cfe5789c498217160191c9b022f09a85bab3`. The latest January 1 fresh-USA report cites `Unknown character` at old source lines 424, 662, and 671, which were the prior Haldane, Velikanov, and Fishman `recruit_character` lines. The current shared CSH source contains no runtime recruit commands, so those line references establish prior-source errors or a source/log mismatch. They neither prove nor disprove the current CSH transfer route. This agent did not search or reread logs.

The three identities are the only dated transfers eligible on January 1: Haldane before 1936.03.14, Velikanov before 1938.04.08, and Fishman before 1937.06.05. Their static definitions exist in the cited character files. No exact-token definitions were found in the inspected installed vanilla character, country-history, or general-history trees. The older November 1936 Fishman save is evidence for the previous runtime-recruit route only.

## Relevant files
| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/scripted_effects/chaosx_startup_history_effects.txt` | Eight dated country helpers now check that the home country lacks the identity and CSH has it, then transfer it with country-scope `set_nationality`. Retirement and post-transfer character-flag logic remain in these helpers. | Current Haldane transfer and retirement at lines 429-450; current SOV dated transfers at lines 756-785; total count is 29 transfers and zero runtime recruits. |
| `history/general/chaosx_startup_character_recruitment.txt` | Retains 38 fixed home-country recruits and adds the 29 delayed identities to CSH during history loading. | Original roster at lines 13-85; CSH block and roster at lines 88-120. |
| `common/on_actions/chaosx_on_actions.txt` | Runs the one-time startup grants and calls the dated roster helpers for AST, CAN, ENG, GER, JAP, POL, SOV, and USA. | Lines 8-21 and 48-55. |
| `common/on_actions/cbrn_historical_startup_on_actions.txt` | Preserves bounded tag-specific daily retry callbacks for the same eight home tags. | Lines 9-57. No world-wide periodic country loop is used for this roster. |
| `common/country_tags/cbrn_scientist_holder.txt` | Registers the internal CSH tag. | Lines 1-2. |
| `common/countries/CBRN Scientist Holder.txt` | Gives the internal tag its country definition and display color. | Lines 1-4. |
| `history/countries/CSH - Scientist Registry.txt` | Defines the stateless holder bootstrap: capital 1, empty-OOB reference, zero research slots, and neutral politics, with no owned state or core. | Lines 1-10. |
| `history/units/cbrn_scientist_holder.txt` | Supplies an empty OOB so the holder creates no templates, divisions, or stockpiles. | Lines 1-3. |
| `common/characters/cbrn_historical_scientists.txt` | Owns the Haldane and Fishman scientist definitions. | Haldane at lines 124-135; Fishman at lines 533-544. The file has no `allowed`, `available`, or `original_tag` gates. |
| `common/characters/cbrn_historical_specialists.txt` | Owns Velikanov's scientist and advisor definition. | Lines 400-421; the advisor has `allowed = { original_tag = SOV }` and doctrine availability. Other specialist advisors also have home-tag `allowed` checks. |
| `history/general/016_brilliant_scientist_character_recruitment.txt` | Closest dormant-holder recruitment precedent: a bounded `every_possible_country` history block recruits six fixed characters to KRG. | Lines 11-19. |
| `history/countries/KRG - Kruger State.txt` | KRG is a stateless, unreleased tag with capital 1 and zero research slots. | Lines 4-15. It also references an empty OOB. |
| `common/scripted_effects/016_brilliant_scientist_effects.txt` | Shows the country-scope explicit-character transfer from the dormant KRG tag into an eligible host. | Lines 2830-2852. The direct KRG scope is an explicit fallback when no reachable holder country is found. |
| `common/scripted_effects/016_brilliant_scientist_country_effects.txt` and `events/016_brilliant_scientist_kruger_state_events.txt` | Show KRG's future lifecycle and route-specific character handling. The effects restore a fixed KRG office roster and the hidden `.90` event activates only selected fixed staff. | Country effects lines 1014-1046; event `.90` lines 481-504. These scripts do not generically move every character held by KRG. |
| `history/general/015_utopia_manifesto_character_recruitment.txt` | A second event-owned holder precedent, with fixed DJX roster. | Lines 11-35. DJX has its own Event 015 lifecycle and is not a neutral shared holder. |
| `docs/testing/chaosx_test_country.md` | Documents why CXT is an active test harness instead of a storage tag. | Lines 5-21 describe console activation and territory transfer; lines 87-105 describe one-time setup and the package-registration bus. |

## Existing patterns
KRG and DJX prove that Chaos Redux uses `history/general` with `every_possible_country` and a tag limit to attach fixed rosters to dormant tags. KRG is not a safe CBRN storage reuse candidate because Event 016 can make it a playable country. Its scripted lifecycle addresses a fixed six-character KRG roster, while the historical scientist definitions have no country availability predicate. CBRN advisor definitions in `cbrn_historical_specialists.txt` include some `original_tag` hiring restrictions, but that does not protect the scientist roles in `cbrn_historical_scientists.txt`.

CXT is also unsuitable as a hidden holder. It is a console-activated, landless test harness with its own large CBRN fixture inventory, initialization, and player-only refill and package decisions. Putting date-delayed CBRN personnel on CXT would change the character pool used by that harness.

At the start of this exploration, the exact CSH token did not appear in the inspected mod or installed vanilla country-tag, country-definition, and country-history paths. The current shared tree now intentionally registers CSH in `cbrn_scientist_holder.txt`; I observed and preserved the parent's changes. No existing use of CSH surfaced before that addition.

## Vanilla or reference precedents
The installed HOI4 documentation section `effects_documentation.md`, lines 7397-7420, identifies `set_nationality` as supporting COUNTRY and CHARACTER scopes and gives the country-scope form with `target_country` and explicit `character`. Live `hoi4.reference_read` succeeded for this section with revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.

The offline snapshot `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, lines 2730-2764, describes country-scoped `set_nationality`, the `target_country` and `character` parameters, and the need for the explicit-character form when the receiving country does not already have the character. Live reference search and read returned revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.

The offline snapshot `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`, lines 211 and 606-613, says `recruit_character` is history-file recruitment and shows the history form. Live reference search returned the Starting characters section as ID `05dff7eb6288867e61f9b9528680a243d85198bdd7748989c617fef6f5d009a7`, revision `0c0e57915a7d1eef9ddeebe91c7329e18f4f224af98ac33fac5edd35e3aaa35d`; its `reference_read` call did not return within the bounded wait, so I read the corresponding local snapshot lines directly. The installed effects documentation has no `recruit_character` section at the searched path.

Vanilla provides a close transfer precedent in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/INS_scripted_effects.txt`, lines 974-981: country-scoped `set_nationality` names an explicit `target_country` and `character`. The live `hoi4.source_lookup` call for the built-in `set_nationality` token returned `status = ok` but zero definitions and references, so the installed documentation and source file are the supporting evidence for that command.

No MCP artifact URI was returned for the reference operations. The revision-bound section IDs and revisions above are the retained reference identifiers.

## Likely edit order for the parent
1. Keep the 29 dated identities on the dedicated CSH tag through history recruitment and leave the 38 fixed recruits on their home tags.
2. Preserve each existing date guard, home-country absence guard, CSH presence guard, retirement branch, and post-transfer character-flag logic while using the explicit country-scope `set_nationality` calls.
3. Use a fresh January 1 start as the first runtime discriminator because only Haldane, Velikanov, and Fishman qualify at that date. Treat the old-line `Unknown character` report as evidence from the previous runtime-recruit source or a source/log mismatch, not as CSH transfer evidence.
4. Keep CSH isolated from Event 016, Event 015, and CXT setup. No event or debug-country lifecycle hook is needed for this holder.

## Validation checks
Source counts currently show 38 home-roster history recruits, 29 CSH history recruits, 67 recruits total, 29 country-scope transfers, and zero `recruit_character` calls in the dated startup helper file. The CSH OOB exists and has an empty `units = {}` block.

The three January 1 date gates are current source conditions, not proof that the new holder owns or transfers the characters in game. Fresh-start runtime evidence for the CSH route remains pending. The older November 1936 SOV save proves the prior `recruit_character` route only. The parent or user should validate fresh-start presence and transfer for those three identities, the Haldane retirement branch after 1936.03.13, and a later bookmark where date-eligible and not-yet-eligible identities split across home tags and CSH.

The Event 016 read-only MCP route remains unavailable for this handoff. A valid `hoi4.event_inspect` call using `mode = roots` and selector `{ kind: event, eventId: chaosx.brilliant_scientist_krg.90 }` did not return within 60 seconds. A valid `hoi4.event_render` call using `view = overview` and the same selector also did not return within 60 seconds. No event artifact URI was produced. These are route/service response blockers, not evidence that the source inspection validates runtime behavior. Reference context, reference search, and the set-nationality reference read did return.

## Risks and blockers
- Confirmed: No fresh CSH runtime proof is available in this handoff. The January 1 error lines cite former `recruit_character` lines 424, 662, and 671. Current CSH helpers contain no such runtime commands, so the logs cannot be attributed to a CSH transfer failure from line numbers alone.
- Confirmed: Event inspect/render did not return within 60 seconds for the valid Event 016 selector. No rendered or inspected event evidence is claimed.
- Confirmed: The installed `source_lookup` route returned zero indexed definitions for the native effect token `set_nationality`; local installed documentation and vanilla source were read instead.
- Ordinary risk: If future edits add another lifecycle to CSH, they could expose or transfer delayed personnel unexpectedly. Keep this tag without territory, cores, player route, and unrelated startup setup.
- User evidence distinction: Earlier human QA reported 58 `recruit_character should only happen in game/history files` warnings. The parent and country auditor subsequently verified all 58 in the authorized cycle1 log under the hash above; the earlier absence came from a changing copy. The separate old-line `Unknown character` report is not current CSH runtime evidence. No other logs were searched.

## Recommended next action
Keep the dedicated CSH design and obtain fresh-start runtime evidence for the three January 1 identities before treating the new holder transfer route as proven. If the fresh run reports an error, compare it to the current helper line numbers and current `CSH` ownership state; do not reinterpret warnings tied only to the former runtime-recruit lines as evidence about the current transfer implementation.
