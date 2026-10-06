# Event003 Holy Realm focus release handoff

Status: the source-level Schism response lock is implemented and the committed layout pass is partially validated; the focus-tree geometry is not release-complete because current renders still show through-node paths, crossings, long connectors, and linear detours.

Continuation closeout: no collision-checked full coordinate map was ready for parent review, so no further position edits were applied. The earlier `THR_four_teaching_seats` proposal at `(23,8)` was rejected because it remained on the `THR_many_lamps_one_flame` to `THR_buddha_mandate` connector; any future placement must put Four Teaching Seats in a true side lane. The current source-matched reference is the full render [pass2_9CA398360A0C7395941043B44D5BE6A9F15E17A3480D87A4843A3F040E44342E_full.png](<focus_release_20261006_evidence/pass2_9CA398360A0C7395941043B44D5BE6A9F15E17A3480D87A4843A3F040E44342E_full.png>) and its [core crop](<focus_release_20261006_evidence/pass2_9CA398360A0C7395941043B44D5BE6A9F15E17A3480D87A4843A3F040E44342E_core.png>); neither is evidence of final geometry acceptance.

The parent authorized the shared Schism availability predicate, its localized tooltip, and bounded position-only cleanup. The current source is commit `ce0b926dc78a129037d3196ea0b747d75b580817`; no source or weight changes were made after that commit in this continuation.

## Route coverage

| Route | Source coverage | Audit status |
|---|---|---|
| Refuge, acceptance, and founding mandate | `THR_mountain_refuge`, the seal/formation route, and the mandate stages establish the Holy Realm and load its focus tree. | Present. |
| Teaching and foreign Dharma | `THR_send_first_envoys`, `THR_translation_houses`, `THR_teach_under_bombardment`, and `THR_many_lamps_one_flame` connect teaching decisions to the route. | Present. |
| Meditation and awakening | `THR_sit_beneath_prayer_flags` through `THR_fourth_quiet` gate the Unshaken Seat and `THR_buddha_mandate`; `THR_the_awakened_one` follows the successful transition. | Present; the Fourth Dhyana trigger remains separate from focus prerequisites. |
| Governance and administration | Council, Protector Regent, and Pilgrim Assembly are three selectable governance branches with distinct support focuses; Arhat administration and its industrial, military, and envoy branches feed Buddhahood. | Present; governance branch geometry is still crowded. |
| Refuge logistics and guardians | Stores, roads, clinics, Vow-Keeper regiments, the high-pass guardian chain, and the Unbroken Pass are present. | Present. |
| Mandala diplomacy and expansion | Mandala formation, refusal/acceptance memories, Himalayan completion, borderland petitions, regional registers, and the World Is a Border capstone are present. | Present. |
| Anti-chaos Buddha powers | Power revelation, discipline, emergency response, and the World Collapse Sun-and-Moon focus are present. | Present; several late-route connectors still pass through other focuses. |
| Hidden Schism response | Debate, Exile, Break, and Absorb remain the four authored outcomes after the Awakened One. | Present; pairwise exclusion arrows were replaced by an availability lock with equivalent ordinary-selection behavior. |
| Final Silence and aftermath | Doctrine, witnesses, extinction, final authorization, Final Silence, and Empty Seat aftermath are present. | Present; final-route geometry still has through-node defects. |

The current tree has 111 focus nodes, 16 more than the 75–95 focus target recorded in the accepted Buddhahood package. This audit found all named route families in source but did not establish that every branch is necessary or accepted at its current depth.

`THR_buddha_mandate` currently has six separate AND prerequisite groups—Snowline Labs, Refuge Foundries, Vow-Keeper Regiments, Quiet Envoys, Many Lamps One Flame, and Fourth Quiet—plus an OR group for the three governance choices. The route is stricter than the minimum gates expressed in parts of the package specification; acceptance of that stricter gate is unresolved, so no prerequisite was changed here.

A brace-balanced source graph audit of all 111 focuses found zero missing prerequisite IDs, zero self-prerequisites, zero prerequisite cycles, zero direct prerequisite/exclusion deadlocks, and zero ancestor exclusion deadlocks. An earlier alert that `THR_guardians_outer_passes` required itself was a parser false positive: its only prerequisite is `THR_complete_himalayan_mandala`, and `THR_letters_beyond_passes` is its downstream child.

## Schism response lock

The four Schism focuses now call `holy_realm_schism_response_unresolved` from their existing `available` blocks. The shared scripted trigger requires all four response focuses to remain uncompleted, and `THR_false_buddha_response_unresolved_tt` displays “Choose one response to the False Buddha.”

The old graph declares all six pairwise exclusions among the four responses. The shared gate is equivalent for every completion-state combination when considering only uncompleted candidate focuses: before any response is completed, all four pass the exclusivity layer; after at least one completes, every remaining uncompleted response fails it. Existing route-specific availability checks still apply on top of this shared gate.

| D/E/B/A completion mask | Completed response(s) | Uncompleted responses passing the old pairwise layer and new shared gate |
|---|---|---|
| `0000` | None | Debate, Exile, Break, Absorb |
| `0001` | Absorb | None |
| `0010` | Break | None |
| `0011` | Break, Absorb | None |
| `0100` | Exile | None |
| `0101` | Exile, Absorb | None |
| `0110` | Exile, Break | None |
| `0111` | Exile, Break, Absorb | None |
| `1000` | Debate | None |
| `1001` | Debate, Absorb | None |
| `1010` | Debate, Break | None |
| `1011` | Debate, Break, Absorb | None |
| `1100` | Debate, Exile | None |
| `1101` | Debate, Exile, Absorb | None |
| `1110` | Debate, Exile, Break | None |
| `1111` | Debate, Exile, Break, Absorb | None |

Mask order is Debate, Exile, Break, Absorb; a bit of 1 means that response is completed. The table describes only the exclusivity layer, not the separate pressure, legitimacy, Mandala Reach, or Chaos requirements.

The four response focuses retain their original prerequisites, `allow_branch` gate, availability requirements, completion rewards, and AI blocks. None declares a focus-level `bypass` or `cancel_if_invalid`, and a source search found no `complete_national_focus` caller for these IDs. Cancelling an incomplete national focus leaves the completion mask at `0000`; after one ordinary focus completion, the remaining responses become unavailable. Console/debug forced completion is outside normal availability handling, as it also bypasses ordinary focus constraints.

The native trigger body passed `hoi4.script_validate` against installed trigger documentation in country scope. A separate call on the wrapper name returned a partial unresolved finding because the validator treats the project-owned scripted-trigger name as an undocumented native command; this did not invalidate the checked native `NOT` and `has_completed_focus` body.

## Icons, localization, rewards, and AI

| Surface | Evidence and finding |
|---|---|
| Focus icons | Current render lists 111 focus icons and 70 unique sprites with no missing-focus-icon diagnostic. No icon reference changed. `GFX_focus_smiling_buddha` is reused seven times, `GFX_goal_THR_final` six times, and `GFX_focus_generic_diplomatic_treaty` five times; these are visual variety opportunities, not missing assets. |
| Custom filters | BODHI, TEACHING, GOVERNANCE, COMPACT, NIRVANA, and HIDDEN have labels and priorities in current source. No filter was changed in this continuation. |
| Localization | All four Schism focus title/description/effect keys exist, and the new response-lock tooltip is present. The localization file retains UTF-8 BOM; its current SHA-256 is `7F104846920112A03EE6E05C537FD8BBCB9D07FC0F658F5B390AE0FA9822AF06`. The only render localization warning is the unrelated vanilla `continuous_restrict_freedom_desc` reference. |
| Rewards | The four Schism completion rewards remain Debate, Exile, Suppression, and Absorb scripted effects. No reward or focus tooltip was altered. |
| AI weights | No `ai_will_do` or focus weight was changed. Current source inspection counted 63 explicit focus weights and 48 implicit defaults. |

The probability auditor’s four-response subpool evaluation for `003_HR_schism_response_unresolved` returned Debate score 3 / 66.3728%, Exile 1.6 / 19.7061%, Break 1.4 / 13.4561%, and Absorb 0.5 / 0.4650%. It flagged `THR_absorb_the_shadow` as `PROBABILITY_STARVED_OUTCOME`. These shares apply only to the declared four-response pool, not to every available Holy Realm focus.

The AI matrix audit also found source gaps: Council lacks the matrix’s high-stability factor; Pilgrim Assembly uses a low-Chaos factor but lacks the refugee-pressure factor; and the Protector Regent factor applies only when a special-chaos enemy exists rather than using the matrix’s broader weakness/capital-threat cases. No AI patch was authorized or made.

The before/after probability comparison is unresolved. The exact layout-only baseline file with recorded raw hash `FAA838BFE108D7B9BDDC344AFF13999A98F134DDDE880B53C5E11287238B1986` was not preserved as a source file. A semantic inverse snapshot is available at [schism_pairwise_before_semantic_reconstruction.txt](<focus_release_20261006_evidence/schism_pairwise_before_semantic_reconstruction.txt>) with raw SHA-256 `14722940949783FE26D9492B5DAA96E5A8C996827E1C57EA76580EB36BF346FD`; it restores the six original pairwise declarations and removes the four new availability blocks, but it does not byte-match the FAA source hash. The auditor’s inspect of this snapshot and its probability comparison attempts returned `Transport closed`, so no numeric before/after result is claimed.

## Geometry and navigation

The committed first position-only pass changed focus coordinates while preserving prerequisites, rewards, AI, IDs, and filters. It relocated the existing governance support, meditation/support, teaching, Schism, Mandala expansion/register, and Empty Seat register clusters; the current full render and crops below show the resulting geometry before any further layout patch.

The current source-matched inspect reports 111 focus nodes, 129 connectors, 41 occupied columns across x=0–40, and 24 rows across y=0–23. The exact remaining layout counts are 24 avoidable crossings, 24 unsatisfied crossing pairs, 25 connector-through-node warnings, 4 long connectors, and 7 linear detours. The four remaining long links all converge on `THR_buddha_mandate`: Council of Abbots spans H3/V5, Protector Regent H5/V5, Pilgrim Assembly H7/V5, and Many Lamps One Flame H9/V3. Other visible through-node groups include the Buddha convergence, Lotus Bridge/Witnesses/Reactors, the Vanishing/Seated-in-the-Sky/Sun-and-Moon network, Extinction/Ministry of Release, and the Mandala Receives Borderlands/Pacification Mandate edge.

The Schism choice cluster now has no pairwise red exclusion connectors, but the current geometry still has two prerequisite paths from the Awakened One running through other response-focus boxes. K4 by itself is planar; the earlier visual defect came from combining the pairwise exclusions with the required dependency layout and fixed-depth neighboring branches.

No additional position changes were applied after root committed the `9CA398…342E` focus source. A complete collision-checked coordinate proposal for the remaining core fan-in and late-route crossings was not ready for parent review when work was stopped. The full current diagnostics and raster crops are preserved so the next geometry pass can start from exact evidence rather than a stale preview.

No custom national-focus shortcut entries were found in `003_holy_realm.txt`. The 111-focus tree spans 41 columns, so navigation depends on normal tree panning/zoom and the existing focus filters; the offline National Focus Modding shortcut section and vanilla `china_communist_sea.txt:37–69` provide the available shortcut precedent. Shortcut additions remain an unresolved navigation improvement, not an implemented change.

## MCP and source evidence

| Evidence | Identity |
|---|---|
| Current focus source | SHA-256 `9CA398360A0C7395941043B44D5BE6A9F15E17A3480D87A4843A3F040E44342E`. |
| Current scripted-trigger source | SHA-256 `9A3A67809CE355FE89FDC03C791BB8FCE5AEE65DDB59EFE52C5CA24DD378C5A3`. |
| Current localization source | SHA-256 `7F104846920112A03EE6E05C537FD8BBCB9D07FC0F658F5B390AE0FA9822AF06`. |
| Current inspect | Status `FOCUS_INSPECTED`, tree `THR_focus`, source `mod:common/national_focus/003_holy_realm.txt`, revision `f172a3667128941beba1c02499d98e62b5a075d0cb26796d00aacee755ecb359`, layout hash `38f6e6ced425f0add0e3761a8f6d3e92dda142fa12d547e68bc24aeb6520cf64`, 111 focus nodes. Artifact SHA-256 `5b108328ae18ff3abcb8a614a289cae3b5d6e6d565b9d855c8e55ff4383f277d`. |
| Current render | Status `FOCUS_RENDERED`, source hash `9CA398…342E`, layout hash `38f6e6ce…0cf64`, 7344×2904 SVG. SVG artifact SHA-256 `0432b39239568513a4ca6811c5d7e7e7288fe3b845cbd7bfaa99a348a1869cdf`; JSON artifact SHA-256 `a2ce5e040b8a6d7139a1e5b7e635694de5853099771251b60fad0334a3084d06`. |
| Native focus raster | The narrow `hoi4.focus_raster` route timed out after 600 seconds on the previous source. The pass2 full PNG and crops were rasterized from the exact current MCP SVG with the installed `sharp` bundled under `hoi4-agent-tools`; full PNG SHA-256 is `C9625A5E7ACDD6849394F4C918B049B1C1B7A4784AEEE2BB22D218B14A56B4BD`. |
| Focus rewrite | The first cleanup call returned `REWRITE_SOURCE_STALE`. The pass2 compact rewrite attempt returned `Transport closed`; neither call changed source. |

The evidence directory contains the before-pass1 and current source-matched render families, full SVG/JSON, 7344×2904 PNGs, and core/Schism/expansion crops: [focus_release_20261006_evidence](<focus_release_20261006_evidence/>). The source-aligned current files are `pass2_9CA398…342E.svg`, `pass2_9CA398…342E.json`, `pass2_9CA398…342E_full.png`, and the corresponding `_core.png`, `_schism.png`, and `_expansion.png` crops.

The rule citations for the shared predicate are: installed `triggers_documentation.md:3501–3509`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; offline Wiki Triggers `has_completed_focus` line703, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`; and offline National focus modding “Interaction with other focuses,” lines275–296, revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`. The wiki states that a focus is excluded when another listed focus has completed and documents `has_completed_focus` in `available` for boolean requirements not representable in prerequisite groups.

Disposition: the shared Schism gate is implemented under parent approval; the first layout pass is implemented but partial; the final geometry cleanup and exact probability comparison remain unresolved. No focus weights, AI modifiers, rewards, or prerequisite edges changed in the Schism patch. No commit was created by this subagent; the parent owns integration and final release status.

Final diagnostic record for this continuation: current source SHA-256 is `9CA398360A0C7395941043B44D5BE6A9F15E17A3480D87A4843A3F040E44342E`. The source-matched pass2 render still reports 24 `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`, 25 `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE`, 24 `FOCUS_AVOIDABLE_CONNECTOR_CROSSING`, 4 `FOCUS_LAYOUT_LONG_CONNECTOR`, and 7 `FOCUS_LAYOUT_LINEAR_DETOUR`. The full current SVG and JSON artifact hashes are `0432b39239568513a4ca6811c5d7e7e7288fe3b845cbd7bfaa99a348a1869cdf` and `a2ce5e040b8a6d7139a1e5b7e635694de5853099771251b60fad0334a3084d06`; the exact local evidence files are `focus_release_20261006_evidence/pass2_9CA398360A0C7395941043B44D5BE6A9F15E17A3480D87A4843A3F040E44342E.svg`, `.json`, `_full.png`, `_core.png`, `_schism.png`, and `_expansion.png`. The focus rewrite route remains blocked by the recorded `Transport closed` failure, and the previous native raster route timed out after 600 seconds; no additional MCP retries or source edits were made in this continuation.
