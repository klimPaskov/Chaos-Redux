# Event 005 Soviet Collapse Final Completion Report

Audit date: 2026-05-21

This report records source-level evidence for the final clean merged Soviet Collapse package from `tmp/soviet_collapse_final_clean_merged_spec_package/specs/`. A current audit found that the package is not yet closed because the final spec requires unique focus icon assignments and the current source still has duplicate icon assignments. The current asset gate requires custom Event 005 tags and explicit cosmetic route tags to have valid flags, existing vanilla-supported tags to keep their game-provided flags by default, and new/Event 005 portraits to avoid vanilla portrait reuse. It does not claim an external live playthrough; the repository workflow leaves live-session verification to the user.

## 1. Source files read

The implementation pass read all seven final clean merged spec parts, `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `hoi4-focus-trees`, and `hoi4-decisions-missions`. Required offline wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, and national focuses. Vanilla documentation was consulted for effects, triggers, script concepts, and script constants.

## 2. Files changed

Event 005 changes span `events/005_soviet_collapse.txt`, scripted effects/triggers/constants/MTTH, decisions/categories, ideas, focus trees, country tags/history, interface sprite files, localisation, achievements, assets, and docs. The main source surfaces are under `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt`, `common/script_constants/005_soviet_collapse_constants.txt`, `common/mtth/005_soviet_collapse_mtth.txt`, `common/decisions/005_soviet_collapse_decisions.txt`, `common/national_focus/005_soviet_collapse_*.txt`, `interface/005_soviet_collapse*.gfx`, `localisation/english/005_soviet_collapse*_l_english.yml`, and `docs/events/005_soviet_collapse_*.md`.

## 3. Implementation ledger path

The requirement ledger is `docs/events/005_soviet_collapse_full_implementation_ledger.md`. The unique focus icon assignment row remains partially complete pending replacement or distinct-variant handling for duplicate focus icon assignments. The flag and portrait row has been revised: ordinary/internal vanilla-supported tags no longer receive generated default flag overrides, custom/cosmetic flag coverage remains active, and portrait uniqueness is source-complete after the 2026-05-23 and 2026-05-24 portrait passes.

## 4. Country package coverage

The country package evidence is split across `docs/events/005_soviet_collapse_republic_package_audit.md`, `docs/events/005_soviet_collapse_high_chaos_package_audit.md`, and `docs/assets/005_soviet_union_collapse/manifest.md`. The current asset audit records 32/32 custom Event 005 tags with normal, medium, and small flags plus leader/council portraits. Existing vanilla-supported ordinary/internal tags use vanilla flags by default; route-specific existing-tag flag changes must be implemented through cosmetic tags such as `UKR_BLACK_BANNER`. The five vanilla-hash portrait replacements completed on 2026-05-23, and the 2026-05-24 council-leader portrait wiring for `MOL`, `UZB`, `TAJ`, `TMS`, and `FER`, remain part of the active evidence.

## 5. Republic and internal republic coverage

The ordinary and vanilla-supported internal republic audit covers `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`. The audit verifies tag/history/localisation/flag surfaces, terminal release and subject-freeing membership, dynamic setup, runtime focus routing, dynamic units, league joining, recognition, and internal-sovereignty news/report integration. Event 005 does not add default flag overrides for these tags; it relies on game-provided flags unless a focus or event applies an explicit cosmetic tag.

## 6. High-chaos splinter coverage

High-chaos and evolved packages cover Kronstadt, Green Army, UDC, SDZ, Basmachi, Black Banner, factory states, Pale Railway, Tunguska, Iron Commissariat, Red Martyrs, Dead Soldiers, Northern Revenant Fleet, Old Great Bulgaria, ancient restorations, Don/Kuban hosts, Far Eastern/Siberian/Ural/Idel-Ural/Birobidzhan/Arctic/Northern Lights successors, and related special actors. The high-chaos package audit records one-row source-complete package evidence.

## 7. Focus tree rewrite summary

Current source recount finds 1,696 focuses across 41 Event 005 trees. Every counted focus has an icon assignment, completion reward, `ai_will_do`, coordinates, localisation coverage, and resolved references in the current audits. A stricter duplicate-icon audit now finds 1,480 unique icon sprite names across those 1,696 focus assignments, leaving 216 duplicate extra assignments in 143 duplicate groups that still need unique variants or a documented design change from the final spec.

## 8. Route coverage table for every major focus tree

| Tree | Focuses | Route coverage |
| --- | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 81 | survival, democratic/Rada, socialist, military, grain/industry, League, Black Sea, Black Banner, Bread State |
| `soviet_collapse_belarus_focus_tree` | 53 | Minsk authority, legal/socialist/military routes, rail sovereignty, forest defense, corridor diplomacy |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | steppe authority, Alash, socialist planning, military district, resources, southern cascade, recognition |
| `soviet_collapse_baltic_focus_tree` | 42 | legal continuity, archives, Baltic League, ports/customs, coastal/forest defense, tag-gated Baltic branches |
| `soviet_collapse_caucasus_focus_tree` | 40 | mountain federation, national restoration, oil, pass defense, Georgian/Armenian/Azerbaijani branches |
| `soviet_collapse_central_asia_focus_tree` | 45 | local councils, border authority, Uzbek/Tajik/Kyrgyz/Turkmen routes, federation, cotton/water logistics |
| `soviet_collapse_moldova_focus_tree` | 48 | Chisinau legitimacy, Dniester defense, Romanian/Prut/Ukraine/Eastern Buffer/neutral bridge routes |
| `soviet_collapse_internal_republic_focus_tree` | 62 | Karelia, Komi, Tatar/Bashkir/Crimea, Yakut/Far Eastern/Buryat/Tuvan, old-name and common-front routes |
| `soviet_collapse_breakaway_focus_tree` | 36 | legal records, militia, depot repair, home industry, patrons, League observers, road/rail repair |
| `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` trees | 47 each | political identity, industry/logistics, military/security, diplomacy/League, expansion or settlement, endgame |
| `PRA_soviet_collapse_focus_tree` | 22 | rail authority, dispatcher politics, workshop economy, armed rail protection, corridor diplomacy, railway sovereignty |
| `TSC`, `RMC`, `DSC`, `NRF`, `ICD` trees | 18 each | compact special-actor authority, industry/logistics, armed survival, diplomacy, settlement/extreme endgame |
| `CFR_soviet_collapse_focus_tree` | 47 | civilian factory politics, production society, border construction, reconstruction protectorates, rivalry/endgame |
| `MFR_soviet_collapse_focus_tree` | 58 | arsenal politics, worker/officer routes, weapons programs, proxy/client production, factory guards, rivalry/endgame |
| `OGB_soviet_collapse_focus_tree` | 23 | restoration politics, heritage guard, Volga/Idel-Ural claims, trade cities, modern war, state restoration |
| `KZR`, `SOG`, `KHW`, `ALN` ancient-restoration trees | 16 each | emergency council, administration, industry/roads, guard, diplomacy, broader claims, symbolic or expansionist charter endings, returned-name decision access, high-chaos myth capstones |

## 9. Unique focus icon coverage

The validation report records 1,696 focus icon assignments, but the current duplicate-icon audit records only 1,480 unique icon sprite names. Earlier cleanup passes replaced the largest duplicate groups with unique generated variants; the latest recount leaves 143 duplicate icon groups and 216 duplicate extra assignments. The largest remaining duplicate groups are 4-use groups. This fails the literal final-spec requirement that every focus have a unique icon assignment unless the spec is explicitly amended to allow branch-level reuse.

## 10. Remove-idea tooltip cleanup

The focus-file audit found focus-reward `remove_ideas` only inside `hidden_effect` blocks with visible replacement tooltips. Scripted lifecycle cleanup still removes idea families where mechanically required, but repeated visible remove-idea spam is gone from focus rewards.

## 11. Mission cleanup summary

The mission audit records 118 timed Soviet objective missions with activation helpers, active cap checks, active-objective increments, and terminal cleanup. Terminal collapse cleanup removes every Soviet objective mission. The current activation layer gates mission 011-015 legal-settlement objectives behind a legal-settlement phase check, so they do not consume the active objective cap before a breakaway and a credible central legal response exist.

## 12. Mission clarity fixes

Mission localisation and triggers now use named capitals, corridors, depots, rail routes, ports, and regions rather than vague phrases. The validation report records zero hits for the former vague mission-place phrases in main Event 005 localisation.

## 13. Threat and balance summary

The balance audit records calm strong-USSR opening threat at 7.25, severe opening at 50.25, failure deltas below terminal thresholds, guarded monthly pressure, first-month Union Unmade lock, and terminal gates requiring collapse ingredients.

## 14. Exploit check summary

The exploit audit covers free units, equipment farming, factory loops, influence farming, puppet abuse, war-goal/claim/core spam, mission pressure farming, and release farming. Scenario 28 in the validation report points to this checklist.

## 15. MTTH release summary

The MTTH family audit covers western/eastern European, Baltic, Caucasus, Central Asian, Kazakhstan-after-cascade, vanilla-supported internal republic, and Mountain Republic release paths. Cause reports, cooldowns, weights, release/miss paths, and internal focus routing are documented.

## 16. Influence system summary

The sponsor influence audit covers Germany, United Kingdom, Japan, France, United States, Turkey, Iran, Poland, Romania, Finland, Sweden, Italy, Moscow, and the Free Republics' League aid channel. Recognition, arms/logistics, reconstruction, volunteers, advisers, and patronage-risk ideas mature through four stages.

## 17. League and faction implementation summary

Local league quorum triggers prevent one-member Baltic, Caucasus, Central Asian, and Free Republics' League formation. The faction-goal audit covers purpose, membership, refusal, withdrawal, shared decisions, war goals, AI, success/failure conditions, rewards, consequences, and news/report-only presentation.

## 18. Union Unmade release and war logic

Union Unmade releases ordinary and internal republics, frees Soviet republican subjects with `autonomy_free`, assigns dynamic breakaway setup, forms valid local leagues, expands or forms the Free Republics' League, spawns high-chaos successors where appropriate, and puts released republics into the anti-Soviet war.

## 19. Puppet release aftermath

Terminal subject release paths free Soviet republican puppets before successor setup. News/report IDs cover terminal subject release, dynamic unit explanation, league joins, foreign recognition, internal sovereignty, and puppet-release aftermath reporting.

## 20. Super-event cleanup

Ordinary league formation and republic-route capstones now use news events. Active super-events are limited to Union Unmade and rare campaign-defining high-chaos transformations: Black Banner Returns, The World as One Factory, and Every Port a Council. Retired ordinary league and route-capstone super-event art is preserved only as manifest history.

## 21. News and report events

The news/report audit maps local leagues, liaison offices, terminal subject release, dynamic units, league joins, foreign recognition, internal sovereignty, mission/faction reports, MTTH cause reports, high-chaos notices, and route capstones to event IDs and localisation.

## 22. Asset coverage

The asset manifest records focus, idea, decision, flag, portrait, faction emblem, achievement, news, report, super-event, and UI/progression coverage. Current direct texturefile checks show 860 unique Event 005 DDS texture paths referenced from `interface/005_soviet_collapse*.gfx` and zero missing texture references. The 2026-05-23 generated asset passes add missing ancient ideology variants for `KZR`, `SOG`, `KHW`, and `ALN`, replace vanilla-hash portraits for `KZR`, `SOG`, `OGB`, `KHW`, and `ALN`, and replace byte-identical ideology-flag copies for 28 custom successor tags. The 2026-05-24 historical flag pass replaces `KZR`, `SOG`, `KHW`, `ALN`, and `OGB` historical-restoration flags with historically grounded motif designs. The generated ordinary/internal flag package has been removed so existing tags fall back to vanilla flags; Ukraine's Black Banner route now uses the `UKR_BLACK_BANNER` cosmetic tag from its route focus. The 2026-05-24 follow-up adds unique 156x210 council portraits and sprite wiring for `MOL`, `UZB`, `TAJ`, `TMS`, and `FER`, with runtime leader creation in the breakaway setup package. Returned Names decision/category/idea placeholder reuse has been replaced with dedicated generated DDS assets, and the earlier focus icon duplicate replacement passes remain wired. Focus icon coverage remains incomplete against the final unique-assignment requirement because 216 focus assignments still reuse sprite names.

## 23. Achievement implementation

The achievement audit records 40 Event 005 achievement definitions, 40 matching name/description/tooltip localisation sets, 120 DDS sprite references, 120 existing achievement DDS files, and a dedicated manifest with completed, grey, and not-eligible variants.

## 24. AI behavior

The AI audit records 1,696 focus blocks with `ai_will_do`, 1,068 focus blocks with contextual AI modifiers, 1,555 focus AI modifier entries, 122 non-mission decisions with AI, zero non-mission decisions missing AI, and scripted activation for the 118 timed missions. Audited AI surfaces include Soviet crisis actions, breakaways, sponsors, leagues, factory states, special successors, target gating, and MTTH releases.

## 25. Validation scenario results

The validation report lists all 28 required scenarios with expected result, observed source evidence, status, and blocker columns. Scenario 26 now records `source_partial` because the focus-icon uniqueness audit found duplicate focus icon assignments.

## 26. Simplifications and deviations

The remaining source-level deviation is focus icon uniqueness. Every focus has an icon field, but 216 of the 1,696 focus assignments reuse a sprite name already used by another focus. Returned Names placeholder icon reuse, ordinary/internal flag coverage, ancient ideology flags, custom successor ideology flags, and vanilla-hash portrait blockers have been resolved with dedicated generated assets.

## 27. Blockers

Source blockers and open risk areas remain for the final clean merged package. Unique focus icon assignment coverage is still unresolved: the current source has 1,696 focus icon assignments but only 1,480 unique sprite names. Event 005 now has dedicated strategic AI plans in `common/ai_strategy/005_soviet_collapse.txt` in addition to action-surface weighting, trigger, decision, and MTTH logic. The compact special-actor settlement/extreme capstones now have route-specific payoffs before their shared final helpers, but several expansion branches and compact shared trees remain source-valid while lighter than the deepest bespoke trees.

The previous ancient ideology-flag gap, custom successor ideology-flag duplication, five vanilla-hash Event 005 portrait blockers, and active-leader portrait gaps for `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` were resolved by the asset and wiring passes. The generated ordinary/internal default flag package was removed by the later flag-rule correction, and the historical-restoration flags were rebuilt with historically grounded motifs. Live-session feel, pacing, and UI scanning remain practical user verification surfaces after source completion.

## 28. Remaining work

Required source implementation work remains for Event 005: replace the 216 duplicate extra focus icon assignments with unique, appropriate icon variants or keep the user's relaxed focus-icon standard for this pass; deepen the remaining light expansion/shared-tree branches if they are still expected to match the bespoke route standard; then rerun the focus, AI, and validation audits. Future live pacing and UI feel review remains separate practical validation after source completion.
