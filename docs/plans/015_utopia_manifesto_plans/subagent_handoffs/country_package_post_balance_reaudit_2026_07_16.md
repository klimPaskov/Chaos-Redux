# Event 015 country-package post-balance re-audit

Date: `2026-07-16`  
Role: `chaosx_country_package_auditor`  
Mode: read-only source, lifecycle, hash, and visual audit  

## Verdict

**PASS. No blocker and no P0, P1, P2, or P3 finding remains in the inspected country-package and balance-transition surface.**

The repaired snapshot preserves the complete country package that passed `country_package_current_reaudit_2026_07_15.md`. The only gameplay-source changes since that report are the centralized three-day presentation duration and 56 lines that detect an Assignment public-band crossing, expose one of two mutually exclusive timed presentation flags, suppress a false animation during initialization, and clear the new presentation state during teardown. Removing those exact additions in memory reproduces both prior audited hashes byte-for-byte.

No identity, formation, leader, succession, idea, League, case, diplomacy, achievement, military-growth, recipient, event, decision, focus, trigger, or on-action source regressed. No fallback or simplification was used.

## Authorities and references

The audit read `AGENTS.md`, all files under `docs/specs/015_utopia_manifesto_specs/`, the current country-package report, the annexation follow-up, and the Event 015 source-of-truth packet. It used:

- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

The required offline wiki snapshot was consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, country creation, cosmetic tags, portraits, achievements, factions, interfaces, and scripted GUI. The corresponding installed vanilla documentation was read for characters, scripted GUI, on actions, decisions, script constants, factions, AI strategies, effects, and triggers. Vanilla precedents included `AAT_Iceland.txt` for political state, cosmetic identity, and character promotion, and current national-focus precedents for faction creation, membership, and removal.

## Frozen current source snapshot

Hashes are SHA-256 over the exact current bytes.

| File | Current SHA-256 | Relation to prior country audit |
| --- | --- | --- |
| `events/015_utopia_manifesto.txt` | `a7d27155c463424f19fb1d661356a42ccb90cc4b29f8e42a03ea78ba86b9b164` | exact match |
| `common/decisions/015_utopia_manifesto_decisions.txt` | `5dcd41ef8669a4384fedb2efa9761e657fe8a5ff8ea686e45046005fd23d17fd` | exact match |
| `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `8a905d4b1922ab88bfab97716ba79721fc5b42679863c9543fb04d2cd489fc05` | exact match |
| `common/characters/015_utopia_manifesto_characters.txt` | `5cdf2ea793216351b5a250bbb1bb0eea84103e7668791b30867216af436749cb` | exact match |
| `common/country_leader/015_utopia_manifesto_traits.txt` | `6cd9a84026b739030115c2a81d2303c5a94bd4a3b4b5178b10947897603230a2` | exact match |
| `common/ideas/015_utopia_manifesto_ideas.txt` | `84f1e322ef827edd4eedff68ba99e67ae61e6c4ed1172193cf77eb3f4d05326a` | exact match |
| `common/countries/cosmetic.txt` | `db7814f7dad4a1b27b95f6afa8d87713ebe7a630bb5b4743bbe76550c38b25e4` | exact match |
| `common/script_constants/015_utopia_manifesto_constants.txt` | `75abb0707e63730e871d7582ed6aaa6b275d3a0bc0a37ab5b7e4e5bfeb5ff700` | one presentation constant added |
| `common/script_constants/015_utopia_manifesto_country_constants.txt` | `f53c2eade8230ac93c8af734e41b01b42fe861a3bdb2ec6944d048545af67326` | exact match |
| `common/script_constants/015_utopia_manifesto_decision_constants.txt` | `870516531db2a480be8c2f0626997e7b1a65c6fd4c35e796bb6049b93d84d8c9` | exact match |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `fd7b62671d1f49eb00363316914c6893463c08f4ea24a2c972d37093a8c87cd7` | 56 presentation-only lines added |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | `da2b2c86a47979dde9b7cae022e4f1798bac6029955858ca90fddd8a9167fa75` | exact match |
| `common/scripted_effects/015_utopia_manifesto_country_effects.txt` | `078ccd44ef44d768e1954b3beb914726417fa742a0fe35f8bc5c5938977998aa` | exact match |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | `0eeedf55b22818d4452e18adbe75bb106bf45ffcd33cbf6d3573cab6125bc33a` | exact match |
| `common/scripted_effects/015_utopia_manifesto_achievement_effects.txt` | `bab3fc080661918b35d88b0418a4067ca716e458a63e36a86aa37a5da6f886e2` | exact match |
| `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt` | `0e027f7512bdf07dd04123ef97802235cd18db5d6f46e6de909d8376df7cce4d` | exact match |
| `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` | `1d757540eab0082a09df425578e4208e09cb364832d7b170591ea763d50c60c4` | exact match |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | `d0c304d2b4cd5dccd72b40cff8e9ab4caa3beab58838ce68057eacf31bcfe9af` | exact match |
| `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt` | `ba4ac12603651718c633a0b3c90b530097ceadcf16969fadcec69c77508a1c5e` | exact match |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `c2b26e499078d0c7782e46db587d377d8d64cee02e372f2ae8e087c7cea7ea81` | exact match |
| `common/achievements/chaos_redux_achievements.txt` | `c1c729f4717129e8abb60303a79e6fe4318598e6ac0221c79c65faa1ffe4391c` | exact match |
| `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` | `de37ba78051436a69abdc4a79799749210b9e208b9d3a5396ea012206fde8dbd` | current presentation binding |
| `interface/015_utopia_manifesto.gfx` | `8d7bb8d4889ac2a08cdefa95fe49c591d775a973c43a8e706c5032e7d9f9a6e2` | current sprite registry |
| `interface/015_utopia_manifesto_ledger.gui` | `93dc265e487d72424a3c9143c61615a32da41fca1634af75f762adc67c8df51e` | current layout consumers |
| `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json` | `952aa49bf24dc3d627007557345909b1e74f03b822a702ee0773e66973be89f2` | current focused asset proof |
| `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/asset_records.json` | `828f18554094f6b214a07dde11f4fa61df290b881d8261cc3b6eeb3677f54ea7` | exact match |
| `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/imagegen_source_evidence_2026_07_15.json` | `7f892568ced49d74eb0d7e9cdfe3a796aee4dce13200b3f7a16b3fb2b16b6e18` | exact match |
| `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/advisor_validation_2026_07_15.json` | `9e261b1ccd51249bdaebcd4cc2335a45988014e8aa740b43fad7c7dc8e25b02f` | current advisor proof |
| `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/institutional_portrait_validation_2026_07_15.json` | `0da653422920087a28794a577963860b0dd2fbe2252353de241bf256c02d655d` | current institutional proof |

## Exact central-effects regression proof

The prior audited effects hash was `ed44d3a9892061bb77ebe6e6039be8d7a6a1bcc5f292091c4e5ede32b39d2b8d`. An in-memory reconstruction removed only these current line ranges:

- lines 397 through 400, initialization suppression and flag reset
- lines 585 through 626, the directional presentation helper and its separating line
- lines 637 through 642, previous-band capture
- line 648, presentation refresh call
- lines 6228 through 6230, previous-band and timed-flag teardown

Those 56 removed lines reproduce `ed44d3a9892061bb77ebe6e6039be8d7a6a1bcc5f292091c4e5ede32b39d2b8d` exactly. No other current byte differs from the prior audited central-effects snapshot.

The prior constants hash was `a426f72ee144e8bbf940ffb46460777b8b69f6f2fbf8b1989c020a663cf901e1`. Removing only current line 639, `balance_shift_animation_days = 3`, reproduces that hash exactly.

This proves that the central-effects edit did not alter identity formation, safe recipient logic, original-country restoration, characters, advisors, staged ideas, paid growth, League relations, Necessary Ground cases, reverse indexes, achievements, succession, or their cleanup.

## Country-package audit results

| Required surface | Result | Current evidence |
| --- | --- | --- |
| Safe recipient and rejection | PASS | Three ordered candidate classes share the absolute weak-country safety gate. Majors, protected or mature trees, active event packages, civil wars, offensive wars, near capitulation, insecure capitals, dominant faction leaders, industrial powers, subject empires, extensive occupiers, and unsafe subjects are excluded. Rejection calls the idempotent runtime clearer without loading the tree or installing identity. |
| Original-country restoration | PASS | Acceptance records exact ruling ideology token, exact leader token and ideology subtype, and election permission. Teardown drops only the cosmetic tag, restores the exact surviving eligible leader and political state, retires all Event 015 characters, and does not fabricate a replacement. |
| Five route identities | PASS | Voluntary Commonwealth, Council Union, Planned Utopia, Closed Island, and Practical Commonwealth remain the only five cosmetic identities. The original tag is never replaced. |
| Original flag until formation | PASS | The five `set_cosmetic_tag` calls occur only inside final route identity helpers, reached from the formation event after route proof. Route commitment installs institutions and ideas but no cosmetic tag. The recipient's no-suffix base flag remains untouched. |
| Character package | PASS | The live character file has 24 definitions, consisting of eight institutional founder or successor entries and sixteen advisors. Recruitment is idempotent, political promotion is formation-gated, and teardown retires the whole Event 015 roster. |
| Institutional portraits | PASS | Four distinct people-free `156x210` tableaux serve the eight founder and successor IDs in four intentional pairs. The unchanged asset record and ImageGen evidence hashes preserve exact generated-source and runtime provenance. |
| Advisor dossiers | PASS | Sixteen advisors have sixteen role-specific characters, traits, availability gates, costs, AI weights, add/remove hooks, and distinct `65x67` dossier cards. The advisor validation and source-evidence records remain current. |
| Staged ideas | PASS | The file still defines 50 ideas across the accepted 12 lifecycle families. Administration, social order, and institution stages are cleared and replaced independently. Terminal cleanup removes every package stage. |
| Party, leader, and succession | PASS | The four institutional routes set their route ideology and promote the correct institution only at formation. Practical Commonwealth retains the constitutional leader. Four institutional successors and the practical constitutional-election proof are idempotently gated by `utopia_manifesto_identity_successor_installed`. |
| Formation proof | PASS | Common proof still requires a completed island or capital-ring project, first resolved external case, real external network, resolved conduct, minimum Plenty, no constitutional crisis, and no stewardship failure. Each route also requires its capstone and route-specific Concord, Choice or Assignment, reserve, defense, city, autonomy, or humanist proof. Formation changes identity only after a second live proof refresh. |
| League autonomy and cohesion | PASS | Candidate entry, observer and sponsor handling, cohesion gains and losses, obligations, refusal memory, exit, expulsion, faction promotion, collapse, and route-specific leadership remain present. Ordinary membership excludes majors while major powers use sponsor or observer paths. Formal faction creation remains conditional and cleanup dismantles only the founder-led Event 015 faction. |
| Exact diplomacy and reverse links | PASS | Country, state, League, association, access, guarantee, district, and stewardship relations remain founder-attributed. `.163` owns exact target-annexation disposition, `.164` owns annexed-founder cleanup, and delayed `.165` independently validates exact state founders. Cleanup removes only the affected founder's access or guarantee and preserves pre-existing or other-founder relations. |
| Achievements | PASS | Fourteen Event 015 achievements remain registered behind acceptance plus durable positive proofs and conduct disqualifiers. The achievement source and tracking-effect hashes are unchanged. |
| No free units, equipment, cores, or annexation | PASS | `add_state_core`, `annex_country`, and `load_oob` have zero Event 015 occurrences. Eight `create_unit` variants exist only in the centralized paid-growth helper after live manpower, equipment, and experience deduction. Equipment additions are negative-cost deductions or exact partner transfers after sender payment. The three state transfers are the paid purchase path, exact return path, and long-stewardship integration path. Formation grants none of them. |
| Complete cleanup | PASS | Rejection, disable, annexation, target loss, state-control change, route exit, stewardship failure, League collapse, association withdrawal, district loss, and terminal teardown retain explicit cleanup. The repaired Ledger initializer and runtime clearer also clear both new timed presentation flags and the previous-band scratch variable. |

## Balance-transition presentation audit

The new presentation is bound to public Assignment bands rather than raw value movement.

1. Ledger initialization clears `utopia_assignment_band`, `utopia_manifesto_previous_assignment_band`, and both recent-shift flags before the first refresh. This prevents an acceptance-time false transition.
2. A normal refresh captures the previous public band only when one exists, rebuilds and clamps the Ledger, calculates the current band, then calls `utopia_manifesto_refresh_balance_shift_animation`.
3. The helper is route-gated by `utopia_manifesto_has_resolved_route`.
4. A lower public Assignment band clears the Assignment flag and sets `utopia_manifesto_balance_shift_to_choice_recent` for three days.
5. A higher public Assignment band clears the Choice flag and sets `utopia_manifesto_balance_shift_to_assignment_recent` for three days.
6. An unchanged band sets neither flag. The scratch variable is cleared after comparison.
7. The scripted GUI maps each flag to exactly one element. Both decorative elements occupy `x = 516, y = 70`, use `alwaystransparent = yes`, and cannot be visible concurrently through normal helper execution.
8. GFX registers two separate eight-frame, `5 fps`, non-looping, `play_on_show` sequences and their frame-007 reached-state companions. Each animated final frame remains the reached state during the bounded presentation window.
9. Runtime teardown clears the scratch variable and both timed flags. No recurring world on-action was introduced.

The current focused asset report records `status = pass`, five active animation families, 13 unique GUI sprite references, no duplicate sprite definition, and `balance_shift_binding.status = pass`.

## New animation source and runtime hashes

All sixteen source images have distinct hashes and were visually reviewed as separate generated physical mechanism states. The Choice sequence opens independent routes. The Assignment sequence engages guides and forms a measured matrix. Neither sequence is transform-only.

| Frame | Choice source SHA-256 | Assignment source SHA-256 |
| ---: | --- | --- |
| 000 | `38cfacd7af997525e516d899179ede7e3483f3adde3930364511285a19c4e0a6` | `b70070df05f2069b7c9d10351a704330a4195e99e6a179019314fb92f8b3140d` |
| 001 | `0d73fdc1444f5805a3a7e359088d3b378805648fc4fb9d056e9edd02bc081702` | `99b1f7d763c59186b890af96e5e896acfabba259d9cfaf006488f5286d4dce7f` |
| 002 | `7fffc55730a150047aa463e22ffda0f427211889855e11224ef20140889f4803` | `ca651df3336d77a5e2ba93334fef1d07a7712ad177b91aae45c6502fda57facd` |
| 003 | `0097dc5ad2a66e673257b006077d0aa51199ae3b2d75397cef53b07ad7a528bb` | `553a2d5101cebc55c4224dcd2d935f4e45f013b7db8f3e1fd5e693085bb22c1f` |
| 004 | `dc8d2fd8633981355d114ca5b2d406dfaa46d054b98c89dc4871d8a36cb760ec` | `0dfefc180711ed3afe6caebf94383e3dfb823f615919f5515518d94b1a005d25` |
| 005 | `7832cf10e8c8cee190d9826c623b0eee71ebf55cf75f385764c787432e083f40` | `247b8b8f743e9e567d35a79f493875b8e266aceb8f883db8b526f1c83d0a3b34` |
| 006 | `1325a1ee4c7eb0274bbdc29f557c29aa0260f91e1a707752cb6993d36f0cdfc0` | `f702b1b4b09784769f683ad067bf83914968eb8831554ca8638e3b7fcaedfbca` |
| 007 | `30c45ca5d11e219d9905aac8ff9b5e817d4c7490b6add056b63321253dfd4fff` | `07722ab8239d022638af58f35fbd0d475dc00ba44bd69be1f178224087834b66` |

| Runtime DDS | Dimensions | SHA-256 |
| --- | --- | --- |
| `utopia_balance_to_choice_sheet.dds` | `1264x24`, eight `158x24` frames | `cd0440db72fce608ee20cd0f5496ede0f9396ed1756aed72c694c9586f2ca13c` |
| `utopia_balance_to_choice_static.dds` | `158x24` | `126081178829c4e7092e72b52c774e07388c39b9626518a4eee4c414bca0b953` |
| `utopia_balance_to_assignment_sheet.dds` | `1264x24`, eight `158x24` frames | `cfb74421c21b650b061042f738cd735aeb338e0c3cb96d2624aceb0d46ca8241` |
| `utopia_balance_to_assignment_static.dds` | `158x24` | `202a9ab4120cec445d07ef4b0509a57baff8e8ef9272a722c9be204d281efd62` |

## Limitations

- This is a static exact-source, hash, lifecycle, and visual review. It does not claim an interactive engine trace or live scripted-GUI render.
- Exact original-leader restoration remains deliberately conditional on the saved character still existing and being eligible for country leadership. No substitute leader is fabricated.
- The separately registered static reached-state sprites are package companions. The current bounded presentation consumes the non-looping animated sprites, whose last frame is byte-equivalent to each reached-state companion during the three-day visibility flag.

These limits do not hide an omitted country-package requirement and do not create a P0 through P3 finding.

## Files changed by this audit

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_package_post_balance_reaudit_2026_07_16.md`

No gameplay, localisation, GUI, GFX, asset, spreadsheet, skill, or other documentation file was edited. No commit was created.

## Simplifications, omissions, fallbacks, and blockers

None.
