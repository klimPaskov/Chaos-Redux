# Event 039 ENG Succession Ownership Audit

Disposition: unresolved.

Scope: read-only review of ENG opening successors, current native ownership, and directly dependent British focus and event paths. No gameplay, history, localisation, assets, map data, or focus files were changed. No country identity or date gate is proposed.

Acceptance basis: the user authorized this bounded audit and named Part 1 and Part 3 of the Event 039 specification. Their opening-leader and character-ownership gates are treated as binding. The user's current instruction rejects attaching an absent Chamberlain token with set_nationality. The Churchill row below is a conditional proposal for parent review, not accepted design.

## Finding

ENG_stanley_baldwin to ENG_neville_chamberlain is not supported as a standard vanilla ENG opening row. The static Chamberlain token is absent from the 1936 recruitment list. In the 1939 history block, vanilla recruits and promotes that exact token and retires Baldwin in the same block. The later vanilla Baldwin resignation event creates a different, dynamically created leader named Neville Chamberlain. The current Event 039 helper treats the static token as attachable whenever ENG lacks it, so it can transfer a foreign-held character or act on a character whose current recruitment is unproven.

ENG_stanley_baldwin to ENG_winston_churchill is a source-grounded conditional candidate. Churchill is recruited in the base ENG history, has a native country_leader role with conservatism ideology and an existing vanilla portrait, and vanilla later promotes that exact token to lead democratic Britain. This preserves the democratic government group while changing the sub-ideology from Baldwin's liberalism to Churchill's conservatism. Vanilla does not directly define Baldwin-to-Churchill succession.

The row is safe only when the live country state proves that ENG itself is the current tag, Baldwin is the ruling leader, Churchill is currently on ENG's roster with a country-leader role, and ENG has not committed to a conflicting political route. No live roster or focus scenario was returned by the HOI4 MCP calls. The exact 1936 ruling leader therefore remains unverified. The source comment claiming Chamberlain is the starting leader conflicts with the actual character list and is not used as evidence.

## Candidate decisions

| Candidate route | Native evidence | Audit decision |
| --- | --- | --- |
| ENG_stanley_baldwin → ENG_neville_chamberlain | C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\characters\ENG.txt:184-198 defines the exact leader role, liberalism ideology, and portrait. The installed history file at history\countries\ENG - Britain.txt:354-356 recruits and promotes Chamberlain, then retires Baldwin in the 1939 block. The base history's character list at lines 628-633 recruits Baldwin and Churchill but not Chamberlain. Vanilla events\Britain.txt:829-865 later retires the current country leader and creates a named Chamberlain with create_country_leader, rather than recruiting the static ENG_neville_chamberlain token. | Do not authorize this as a normal vanilla row. It could be reconsidered only in a nonstandard current state where the exact static token is already recruited by ENG and Baldwin is still ruling. No such context was found in the mod or the installed approved mod sources. |
| ENG_stanley_baldwin → ENG_winston_churchill | Installed common\characters\ENG.txt:2-76 defines Churchill's country-leader role as conservatism and his advisor role. history\countries\ENG - Britain.txt:630-631 recruits Baldwin and Churchill in the base character sequence. events\Britain.txt:237-278 includes a later native democratic succession that promotes Churchill and retires Chamberlain. common\national_focus\uk.txt:9611-9627 requires Chamberlain for ENG_motion_of_no_confidence and bypasses that focus when Churchill is ruling. | Conditional source candidate only. Authorize it only behind the current-state and route guards below. The guard must fail closed when Churchill is absent, retired, transferred abroad, or not a country leader on ENG's roster. The default 1936 ruling leader and the current political commitment state were not engine-verified. |

No date limit follows from the history comment or from this audit. The exact current leader and successor ownership checks should decide eligibility at the prefire check and again in the opening transaction.

## Country-package coverage checklist

| Surface | Status | Finding |
| --- | --- | --- |
| Tag and country identity | Partial, bounded to this route | The intended native tag is ENG. The current helper checks original_tag = ENG but not tag = ENG, so an ENG-origin tag can enter the same branch. Add an exact current-tag check to the ENG row. No country tag, cosmetic name, flag, or country definition was changed. |
| Politics, leader, party, and succession | Reviewed for the three named candidates | Baldwin and Chamberlain use liberalism; Churchill uses conservatism. A democratic ENG government can promote Churchill through the native britain.9 succession. The standard 1936 ruling character remains unresolved because the history comment conflicts with recruitment order and the political setup precedes the character recruitment list. |
| Portraits and assets | Native references checked | The installed portrait sprites and DDS files exist for Baldwin, Chamberlain, and Churchill. No portrait production or asset wiring is needed for the proposed conditional Churchill row. |
| Focus route dependencies | Source reviewed; MCP incomplete | The relevant tree is vanilla british_focus in common\national_focus\uk.txt. The motion-of-no-confidence focus explicitly bypasses when Churchill rules. The UK political branch roots and route markers are listed below. MCP focus inspect and render returned no result. |
| Decisions and ideas | Bounded review | Vanilla ENG decisions contain ruling-Churchill checks in common\decisions\ENG.txt. Churchill also has an advisor role in common\characters\ENG.txt. No Event 039 static Churchill death or removal reference was found. |
| Chaos ownership | Exact-token scan completed | No Chaos Redux gameplay file other than the Event 039 helper references the static Baldwin, Chamberlain, or Churchill character tokens. The Chamberlain Easter Egg creates a separate dynamic leader and portrait. Its later leader replacement is a follow-up interaction risk, not ownership of the static Churchill token. |
| Map and state setup | Outside this assignment | No map or state dependency is implicated by the candidate ownership path. Map ownership, capitals, supply, rails, and state data were not audited. No map write occurred. |
| Flags, country localisation, advisors beyond candidate roles, and party names | Outside this assignment | No package changes were made. Full country-localisation, flag, party, and advisor coverage was not audited. |
| Starting military, technology, industry, supply, and production | Outside this assignment | No setup changes were made or validated. |
| AI and probability | Outside this assignment | Host weights and focus-selection weights were not analyzed or changed. No probability result is claimed. Any later change to those weights requires the chaosx_ai_probability_auditor pass. |

## File-surface checklist

| File | Identifiers and lines | Finding |
| --- | --- | --- |
| common\scripted_effects\039_murder_mystery_character_effects.txt | murder_mystery_install_emergency_successor:328-354; murder_mystery_try_curated_successor:360-380; SHA-256 D555E20B0EA68B5E363AF0456632A96E03CB4DEE169C986A724A67AC25F89C0E at final source recheck | The curated row checks original_tag = ENG, democratic government, and Baldwin as the victim. If ENG does not have static Chamberlain, it calls set_nationality = PREV, then promotes him. It does not prove current ENG ownership before the transfer. If the row is not marked used, the caller creates the generic emergency body. |
| common\scripted_triggers\039_murder_mystery_integration_triggers.txt | murder_mystery_prefire_host_is_valid:14-17; murder_mystery_host_is_eligible:37-62 | The shared host gate excludes special Chaos and actual nonhuman countries, terminal states, current Event 039 states, and countries without a leader. It does not check a country-specific safe successor or committed ENG focus route. SHA-256 at the final source recheck: 9CFEAFDBFDA9FD76301C3B72031A8BFD3F1BAC9EE66471DDE52927BFAC376274. |
| events\039_murder_mystery.txt | chaosx.nr39.1:27-38 | The hidden entry event uses murder_mystery_prefire_host_is_valid and calls murder_mystery_run_opening. No ENG-specific row is visible in the event trigger. SHA-256 at final source recheck: 749105E395578F57F0AF0C9937D593DC252495D920D05DD568A8611AA3661892. |
| common\scripted_effects\039_murder_mystery_integration_effects.txt | murder_mystery_select_weighted_prefire_host:32-47 and murder_mystery_prepare_opening_package | Host selection uses the shared prefire gate. The ENG candidate gate needs to run before ENG can enter the host pool and again during the opening transaction. SHA-256 at final source recheck: 8637B23CB3B6BA35757FCAAEF1E63DDF5E110F204CC5C43FE1F1ABD0990C4D87. |
| common\characters\ENG.txt in installed vanilla | ENG_winston_churchill:2-76; ENG_stanley_baldwin:79-92; ENG_neville_chamberlain:184-198 | Native roles and ideology values are defined. |
| history\countries\ENG - Britain.txt in installed vanilla | set_politics:592-602; 1936 recruitment sequence:628-633; 1939 history:354-356 | The base sequence recruits Baldwin and Churchill but not the static Chamberlain token. The 1939 block recruits and promotes the static Chamberlain token, then retires Baldwin. The comment at line 628 is not used to assert the actual ruling leader. |
| events\Britain.txt in installed vanilla | britain.9:237-278; britain.22:829-865 | The 1940 succession promotes static Churchill from ruling Chamberlain. The later Baldwin resignation event creates a dynamic leader named Neville Chamberlain and does not recruit the static token. |
| common\national_focus\uk.txt in installed vanilla | ENG_motion_of_no_confidence:9607-9645; branch roots at 9254, 10957, 11192, 11493, and 12840 | ENG_motion_of_no_confidence is Chamberlain-gated and bypasses when Churchill is ruling. The political roots ENG_steady_as_she_goes, ENG_a_change_in_course, ENG_the_kings_party, ENG_organize_the_blackshirts, and ENG_concessions_to_the_trade_unions provide concrete completed-focus route guards. |
| events\GOE_Raj.txt and common\decisions\RAJ_GOE.txt in installed vanilla | GOE_RAJ_loyalist.11 transfer at events\GOE_Raj.txt:4897-4923; return at common\decisions\RAJ_GOE.txt:5284-5334 | The approved native route transfers Churchill from ENG to RAJ and has a return path. An ENG-side has_character = ENG_winston_churchill guard prevents Event 039 from taking him back from RAJ. |
| interface\_leader_portraits.gfx and installed vanilla leader DDS files | Churchill 3814-3816; Baldwin 3819-3821; Chamberlain 3834-3836 | The three vanilla sprite paths resolve to existing DDS files. |
| events\_chaosx_easter_eggs.txt in Chaos Redux | chaosx.easter_egg.1:4-43 | This event creates Chamberlain The Immortal as a different dynamic leader after a long British war and retires the current country leader. It does not reference the static Chamberlain or Churchill tokens. The current Baldwin ruling check excludes it as a starting candidate; post-opening interaction with an Event 039 run remains unverified. |
| docs\events\039_murder_mystery.md and docs\plans\039_murder_mystery_plans\agent_decisions_2026-10-04.md | Event doc line 29; decision D9 line 82; D22 lines 230-236 | These documents still assert the Baldwin-to-static-Chamberlain transfer by nationality. D22 records that implementation as completed, while the current user instruction rejects attaching an absent or foreign-held character. Treat that mechanism as superseded by the current instruction and reconcile the stale documents after parent review. |

## Minimal conditional row and guards for parent review

This is a source-grounded proposal, not an applied patch or accepted spec change. The same ENG predicate should gate host selection and be rechecked before promotion in the opening transaction.

~~~text
limit = {
	tag = ENG
	original_tag = ENG
	murder_mystery_host_is_eligible = yes
	has_government = democratic
	has_country_leader = {
		character = ENG_stanley_baldwin
		ruling_only = yes
	}
	has_character = ENG_winston_churchill
	has_country_leader = {
		character = ENG_winston_churchill
		ruling_only = no
	}
	NOT = { has_completed_focus = ENG_steady_as_she_goes }
	NOT = { has_completed_focus = ENG_a_change_in_course }
	NOT = { has_completed_focus = ENG_the_kings_party }
	NOT = { has_completed_focus = ENG_organize_the_blackshirts }
	NOT = { has_completed_focus = ENG_concessions_to_the_trade_unions }
	NOT = { has_completed_focus = ENG_motion_of_no_confidence }
	NOT = { has_country_flag = edward_viii_married_wallis_simpson }
	event_target:murder_mystery_victim_character = {
		is_character = ENG_stanley_baldwin
	}
}
promote_character = ENG_winston_churchill
~~~

Keep the existing postcondition that sets murder_mystery_curated_successor_used only after has_country_leader = { character = ENG_winston_churchill ruling_only = yes } succeeds. Do not call set_nationality or recruit_character for this row. The ENG-side ownership check blocks both an unrecruited static identity and a Churchill currently transferred to RAJ. The current tag check blocks an ENG-origin dynamic country from taking the native row.

The existing host gate excludes special Chaos and actual nonhuman countries through is_special_chaos_country and is_actual_nonhuman_country, and it rejects Event 039 terminal and derivative tags. Retain those gates. The exact tag = ENG check adds protection when a country retains original_tag = ENG.

The listed focus checks block completed political route commitments. The installed trigger documentation and source search did not establish a supported test for a selected but unfinished focus. If Part 3 treats an in-progress focus as committed, the route guard remains unresolved until that engine state can be checked through verified documentation or MCP evidence. Do not call the generic emergency body a substitute for this ENG native succession row. If ENG fails the successor preflight, exclude it from the host pool or abort the opening transaction before the generic fallback runs.

## Spec and ownership findings

Part 1, section “Opening sequence,” requires the successor to be prepared before the murder and the sitting leader to pass a safe-succession gate. Part 3, sections “Required ownership audit,” “Opening leader gate,” and “Route-aware successor,” require a stable current leader, a successor already prepared and not active elsewhere, and a political route that remains valid.

The installed effects documentation defines set_nationality as a transfer of the character in scope from one country to another. The current helper invokes it when ENG lacks Chamberlain, which does not distinguish an unrecruited token from a token currently held by another country. The installed has_character trigger checks whether the scoped country has that character. has_country_leader accepts an exact character token and ruling_only = yes/no, so those checks can enforce current leader and successor ownership without a nationality transfer.

The native country-history wiki says static characters must be recruited in country history to appear. It also notes recruitment order and set_politics ordering affect who becomes leader. Here the ENG history sets politics before the displayed character sequence, and a nearby comment contradicts the exact token list. The actual ruling leader must therefore be read from current campaign state. This audit does not infer it from a comment or add a calendar cutoff.

## MCP and reference evidence

The connected tool inventory exposed hoi4.reference_context, hoi4.reference_search, hoi4.reference_read, hoi4.source_lookup, hoi4.event_inspect, hoi4.event_render, hoi4.focus_inspect, and hoi4.focus_render. The documentation workspace ID was mod_chaos_redux_ea3b2d67c2c0.

hoi4.reference_context succeeded for surface = event and surface = focus. The event context reported the installed effects documentation and offline wiki sources, and listed Event modding and On actions under omittedSources. No claim in this handoff relies on those omitted sections. The focus context identified the offline National focus modding source, but the focus-specific inspect and render routes did not return.

Successful revision-bound MCP reads were:

- Installed effects_documentation.md, promote_character, lines 5149-5172, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
- Installed effects_documentation.md, set_nationality, lines 7397-7420, the same revision.
- Offline Effects - Hearts of Iron 4 Wiki.md, Dual scopes, lines 250-314, revision 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c.
- Offline Country creation - Hearts of Iron 4 Wiki.md, Starting characters, lines 568-614, revision 0c0e57915a7d1eef9ddeebe91c7329e18f4f224af98ac33fac5edd35e3aaa35d.

hoi4.reference_search located installed triggers_documentation.md sections for has_character, has_completed_focus, and has_country_leader. The live reference_read call for those sections remained pending and was cancelled. I read the installed files directly at triggers_documentation.md:3410-3420, 3501-3508, and 3640-3652 as the local fallback. The installed effects_documentation.md:6437-6457 distinguishes retire_character from retire_country_leader; this was also read locally. The trigger documentation search returned revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.

The first hoi4.source_lookup batch was rejected because maxDefinitions = 12 exceeded the live maximum of 3 and maxReferences = 60 exceeded the live maximum of 20. Corrected bounded lookups were issued for the three native character identifiers, the Event 039 helper, and the ENG focus dependency. They remained pending without source payloads and were cancelled.

Read-only hoi4.event_inspect trace calls were issued for selector { kind = event, eventId = chaosx.nr39.1 }, including a smaller retry without refresh. The calls remained pending without status, revision, diagnostics, or artifact IDs and were cancelled. hoi4.event_render was issued for the same selector and a neighborhood view; it did not return an artifact. hoi4.focus_inspect was issued for british_focus in common\national_focus\uk.txt, and hoi4.focus_render was issued for that same tree. Neither returned a source revision, diagnostics, or render artifact before cancellation. These surfaces are unresolved MCP coverage, not engine-validated findings.

The connected tool list did not expose a HOI4 server health or version route. Tool exposure is recorded separately from service health. No technology, GUI, map, native task, or probability route was required by this bounded ownership slice.

## Validation, changes, and remaining risks

Completed local evidence includes exact-token searches through Chaos Redux source and documentation, installed vanilla source, and installed approved reference mods 1521695605 and 2265420196. Neither approved mod had exact-code references to the three static ENG tokens. Approved mod 1458561226 was not installed at its documented Workshop path. Exact vanilla portrait sprites and DDS paths were inspected and the three DDS files exist.

No live roster test, focus-tree MCP render, event-chain MCP render, HOI4 launch, save inspection, map inspection, or probability analysis was performed. No AI weights were changed or analyzed. These are limits on the audit, not passing results.

Changed file: this handoff only. No tags, states, leaders, parties, focus IDs, localisation keys, flags, formables, assets, or gameplay source were changed. No commit was created.

Before a Churchill row can be certified, the parent still needs a successful Event 039 and british_focus MCP inspect/render, current-state proof for the ruling Baldwin and ENG-held Churchill conditions, and a decision on how to reject a political route that is selected but not yet completed. The user's current instruction supersedes the D22 nationality-attachment mechanism. The Churchill row remains a proposal until the parent accepts it.
