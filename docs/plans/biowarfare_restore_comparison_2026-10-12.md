# Biological warfare restore comparison — 12 October 2026

A12 and B11 are implemented in `3deac2d4da401de6e47c04f3170a409833ddffa4`.

Acceptance basis: the owner's A12 and B11 instructions of 12 October 2026 require the earlier direct deployment and containment flow, fast policy changes, and removal of Disease Containment Board entry points.
History was traced with `git log -S/-G`, `git show`, and the offending changes' parent blobs.

| Surface | Earlier implementation | Rejected implementation | Restore source |
| --- | --- | --- | --- |
| State response | Direct field-hospital and quarantine decisions, introduced in `1bbbc89fa` on 22 August 2025 | Capacity investments, reservations, pending orders and intensity-banded sustainment missions added by `8307afb3c` | `8307afb3c^`, retaining the earlier direct flow |
| Treatment | Separate antibiotic production, withdrawal, retrofit and vaccination actions | Countermeasure expansion in `8307afb3c` and treatment consolidation in `ce26c6e58` | Earlier decision bodies in `8307afb3c^` |
| Native deployment | Research and native aircraft/payload requirements; preparation before war, launch during war | Policy authorization and handling-context gates in the July 2026 raid expansion | `3a3d61422^` for ordinary raid target, preparation and launch blocks |
| Policy | No policy ladder in the year-old implementation | `3a3d61422` introduced the ladder, terminal milestone and 90-day reassessment lock | Remove those added delay/milestone requirements; retain immediate newer choices |
| Board | No containment board | Board first added in `4732ed690`, expanded for Black Plague, and consolidated by `23c6e94c1` | Detach the category header and disable both visible bindings; retain files |
| Decision list | The original field-hospital and quarantine definitions already used `map_only` | A12 temporarily exposed them in the decision list as well | B11/C12 restore `map_only`: both direct state responses remain on the map and out of the category list |

The earlier flow has no policy step to restore.
The closest reading of the owner's instruction keeps ordinary biological raids independent of the newer policy ladder and retains its three choices for other delivery systems as immediate actions with the existing dynamic five-Command-Power price.
New exact-state outbreak accounting, automatic handling, native payload collection and Event 016 authority remain behind the restored flow; they do not require a staging-selection decision.
Live dynamic values remain in historical wording and effects where the owner expressly permits them.

The Black Plague response selector is retained independently of the rejected board because newer Event 020 response decisions need its selected state.

13 October follow-up: the year-old source `8307afb3c^:common/decisions/biowarfare_disease_containment_decisions.txt` and current source both contain the same 15 response IDs: field hospitals, quarantine, close/reopen borders, and pathogen-specific antibiotic production, research, vaccination, and withdrawal. The two map-targeted state actions use `map_only`; the retained Black Plague state selector is a separate Event 020 dependency. No category step, division assignment, or timed deployment preparation is required before either state response can be started.
Response icon references follow the recovered decision definitions; no containment texture or GFX path is replaced.

Field hospitals cost 10 Command Power and 150 support equipment and complete after 8 days; quarantine costs 10 Political Power and completes after 15 days.
The historical field-hospital requirement checked only 100 support equipment despite charging 150; the shared live price now supplies both affordability and payment, preserving the old two-resource action without the mismatch.
Field Hospital I–IV restore 20%, 30%, 40% and 50% modifier reduction; quarantine adds 20%.
The exact `reduce_contamination_effects` body and its zombie-prevention helper come from `726103283^`, before that commit removed them.
Current outbreak variables are rebuilt before the old reduction applies once, preventing repeated refreshes from compounding it.
National antibiotic ideas automatically provide both the newer lifecycle protection and the old factory-scaled protection, with no distribution decision.
Grant, revoke and state-response completion refresh active controlled outbreaks directly.
The original formula is uncapped: Field Hospital IV plus quarantine leaves 30% of the freshly calculated state burden, while adding maximum Anthrax, Plague and Tularemia protection produces a total reduction of 1.65 and a factor of −0.65.
That sign reversal is retained under the owner's exact-restoration instruction; no cap or reinterpretation was introduced.

The decision audit confirmed field-hospital willingness scores of 10/20 with Field Hospital II and quarantine scores of 5/2.5 below 40% stability; original antibiotic production/research and vaccination weights were recovered without retuning.
These are source-derived scores, not click probabilities.
Policy prices remain five Command Power for an accepted change, including Unrestricted Authorization without terminal command; no choice sets the reassessment flag.
Ordinary raid preparation has no war prerequisite, while launch and accepted outcomes still require war and a valid target; modern native aircraft, payload and outcome accounting remain.
The board header and popup have `visible = { always = no }`, the category has no board attachment, and Black Plague selection no longer writes or refreshes board state.
No requested response action or deployment route is omitted; no design fallback was used.

## Sources and verification limits

Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 576–595, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, defines the three map/list modes.
Installed `common/decisions/_documentation.md`, lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, defines targeted scopes and trigger evaluation.
Vanilla `common/decisions/AFG.txt`, line 489, uses `map_and_decisions_view`.
Installed `common/raids/_documentation.md`, lines 75–178, and vanilla `common/raids/nuclear_raids.txt`, lines 43–72, distinguish type visibility, preparation, launch and native equipment collection.
Installed `common/scripted_guis/_documentation.md`, lines 9–50, and offline `Scripted GUI modding - Hearts of Iron 4 Wiki.md`, lines 149–177, establish category attachment and visible bindings.
These references were read through the available MCP reference workflow or directly after the slow source/validation route; they establish source contracts, not observed game behavior.
The parent A11 file-mode `hoi4.script_validate` request timed out after 600 seconds; no unchanged retry was made because there was no useful input correction.
Further validation for that route requires a responsive service; direct source and history checks remain the verification route for this task.

## Related scientist restoration

A11 is implemented in `d2f7111d16e84b6b9a8fadf4b9967af12d165d15`.
The 67 scientist role bodies and home-country recruitment come from `33b6946dd^`; three later defensive advisor roles remain.
Offending changes include `33b6946dd`, `aa64dc833`, `863b59ced`, `d5287e577`, `4f7dbb6cb`, `fbf2c40da`, `cab3acb5b`, `ba194d7ed` and `2df595e9f`.
Independent source audit confirmed all 67 complete scientist roles match the parent baseline, all 67 identities recruit once into their home tags, and no active roster retirement, transfer or scientist-visibility gate remains.
Skill levels 1–4 have 6, 6, 27 and 28 scientists respectively; the roster is not uniformly level 3.

## Related chemical restoration

A13 is implemented in `d640c653cb864864df84a8432acf8ab8d9f092fa`, with canonical localisation row endings in `0e2814d61b981479c82a9a2348534e717ddd4cb9`.
Offenders are `81972d868` (AI disable), `726103283` (impossible gate, removed state effects and cylinder production), `067d392c1` (inert abilities and deleted helper closure), and `cc5f0e876` (three original icon replacements).
Ability bodies, dependency closure, original state modifier and twenty cylinder-production blocks come from `726103283^`; active ability AI comes from `81972d868^`.
The original trait-selection weight comes from `76bfc2885`, and manual assignment/academy callbacks use `309d1df5c`; later High Command and service mechanics remain.
The original icon bytes and unchanged sprite consumers are documented in [the commander contract](../systems/cbrn_warfare/chemical_warfare/chemical_operations_commander_trait.md).
Current exact-state raids remain a second route, with separate state-modifier readers and cleanup so they cannot erase the restored ability's timed effect.
The original production eligibility body has a dedicated alias to keep newer confirmed-use history intact; this is a name-only compatibility change.
No restored wording was restyled; exceptions are live dynamic values, necessary compatibility names and the owner's lowercase-`k` number formatting rule.

Skills used: shared Git commit, characters/leaders, decisions/missions, native raids, scripted GUI, event assets, subagents and the probability auditors' AI-strategies skill.
The canonical characters/leaders skill was updated only to reflect direct recruitment of the restored roster.

## Civilian mask state-choice restoration

13 October follow-up: `d4a27b58facddf55def7f13dffb7de94eac3429` removed the player's exact-state choices for priority issue, full distribution, filter replacement, and occupied supply. The current source restores those four original IDs as state-targeted decisions with their historical costs, project durations, decision cooldowns, and `FROM` completion scopes: `cbrn_priority_state_mask_issue`, `cbrn_full_state_mask_distribution`, `cbrn_replace_state_mask_filters`, and `cbrn_supply_occupied_population`.

The three standard state actions use the current shared state-target guards and debit helpers; the occupied action uses the selected state's live mask quote, reserves actual model stock through the existing state escrow, charges its historical 25 PP only after a valid reservation, and refunds unused escrow on cancellation. Each target owns its project lock and target receipt, so multiple states can run in parallel. The national full distribution and sale-aware national occupied programs remain distinct optional routes, while stock-backed automatic maintenance continues independently.

The four state decision definitions use `state_target = any_controlled_state` and `map_and_decisions_view`, preserving the controlled-state `FROM` pool while limiting entries to eligible controlled targets. The direct occupied custom-cost display covers PP, the selected state's actual available mask quantity, and the two native-reserved civilian factories. Its pre-click affordability gate checks factory capacity before the native reservation starts, while the complete effect rechecks PP and the selected-state receipt without rejecting the order against its own two-factory reservation. The transaction ledger remains owned by the national sale-aware pair; the direct historical route uses state escrow only and does not claim a Black Friday discount.
