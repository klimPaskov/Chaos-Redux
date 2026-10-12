# C1 and B9 restore/source repair evidence (13 Oct 2026)

C1 is incomplete because five missing principality flags have no historical runtime originals and the source of the unlocated `UPPER_LEFT` font diagnostics is unresolved.
B9's state-pointer source defect is repaired and independently audited; visual and live execution are unverified.
The explicit prohibition on launching HOI4 was followed, so no Linux relaunch loop was performed and neither game nor its settings was touched.

## Changes and provenance

| Item | Offending change | Restoration or narrow correction | Commit |
| --- | --- | --- | --- |
| C1 elephant template | `771b609c7841dfd196af7fd2819fa9dc99150d1f` put a frontline elephant battalion in support | The entire Scavenged Elephant Column template matches that commit's parent byte for byte: elephant regiment, recon support | `3c098421e86f16eece355d268c2ea75c19d765db` |
| C1 Event 037 state names | `afad1de2b` introduced the hotspot bindings without the variable-scope marker | Added only `?` in both saved-state references; all prose and other bytes retained; the parent's event has no hotspot bindings to restore | `f64ef507a2717e7c15239243ce41c373f71d7ce1` |
| C1 original idea texture | `5b44f0d3f5c200f944aa44f3e429808b4672579c` removed an actively consumed texture | Restored `gfx/interface/ideas/generic_victors_of_ww1.dds` from its parent; historical Git blob `e63dd1b83165c663f3d89b4f66523bcd27edeb7b`, LFS payload SHA-256 `bc4a68975504687505fe246625a46a5cda0ea6667b41b67658d525deb5bb526d`, 16,448 bytes, 60x68 RGBA; decoded for review without altering the DDS | `e0f807c1d492165a29b252bc55929f94ec2bba54` |
| B9 camp state selection | `3098ed9d2` introduced `camp_admin_display_state = THIS.id` | Retained the State scope with `THIS` throughout the display array, dynamic rows and selected-site actions; the prior camp lists in that commit's parent stored actual state scopes with `value = PREV`; the administration block itself has no earlier version | `4b0967bd7ad2d8386a2ec137146af8b0cd225ad5` |

The B9 source change is one token in `common/scripted_effects/camp_administration_ui_effects.txt`.
Layout, art, wording, costs, eligibility, AI and the new administration mechanics are retained.
The missing original Hiraga scientist sprite registration in `interface/_scientists_portraits.gfx` was also restored from installed vanilla `_scientists_portraits.gfx:334-337`, lost when `7295937b5aaf85c0f7a53776d21d7dd7ff9bd015` introduced the filename override.
Its four-line original entry is retained without changing the portrait bytes or copying art to the obsolete `gfx/leaders/JAP/` path.
Commit: `6cf5d0120866354fbc023bcb2c119bc4f2357e1e`.
The remaining changed source files are `common/scripted_effects/014_cannibalism_effects.txt`, `localisation/english/037_mysterious_population_l_english.yml` and the original idea DDS listed above.
The restored idea is consumed through installed `interface/ideas.gfx`'s `GFX_idea_generic_victors_of_ww1` and `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt:6370`; no sprite is repointed.

## Checks and limits

Both Windows logs were read only.
The supplied `error.log` is 1,965,940 bytes, last written 12 Oct at 13:33:54; SHA-256 `5f7e1cc59937d984bf7230929b5850f1a9221b655a234963a7074cb99545d0c9`.
`text.log` is empty.
The log contains 30 load entries and 345 distinct diagnostics when concatenated timestamp records are separated; unrelated later gameplay errors are not claimed resolved by this load/camp pass.
The current localisation inventory has zero key collisions across 386 files and zero duplicate scripted-localisation names across 5,594 definitions.
The Event 037 correction preserves every byte except the two added question marks and follows installed `bba_events_l_english.yml:253`'s `[?ROOT.ETH_bop_state.GetName]` precedent.

All 63 camp buttons have a mapped handler or an explicit disabled locked variant: 40 click handlers and 23 locked controls.
The independent decision auditor traced navigation, mutually exclusive pickers, typed state selection, availability rechecks, shared payment/effects and dismantlement's three cost types, and found no additional confirmed button wiring defect.
The parent reviewed that handoff and the final one-token diff.
This is source evidence, not proof of native button execution.

`hoi4.gui_inspect` returned `GUI_INSPECTED` for `repression_ledger_window`, fixture `c1_b9_camp_baseline`, 187 inspected elements, shared revision `45990713f5f4bff2d7211272a397a307762c2f8cae8c2f5939d4a46f9b5bb161`.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/955733755d604500eb17eb818fba33b143dfca935c98d9a72cdb95108f5485d6/05c7b43809c20dcda1daabfd71d5680f786ad1a9a639188f27d971c366fb518a/gui-inspect.45990713f5f4bff2.json`.
The fixture leaves gameplay facts unresolved; default-enabled navigation and intentionally overlaid tab art/labels are not treated as defects merely because the checker warns about them.
The requested source preview at 1920x1080 and 1280x720, fixture `c1_b9_locations_source`, timed out after 600 seconds; no image or pixel/click-region comparison was delivered or claimed.
No unchanged renderer retry was made.

`hoi4.script_validate` first rejected file mode with explicit kind/scope; the single corrected file-mode attempt returned `SCRIPT_CHECK_PARTIAL`, 318 commands checked, no findings, `valid = null`, 179 argument blocks unchecked and 15 helper roots with unknown scope.
Its checks included syntax, command kind, declared scope, event popups and known mistakes; parameter semantics and game behavior remain outside that result.
Documentation revision: `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
No further retry was made; further attempts require a changed tool contract/input that addresses the uncovered helper or argument semantics.

## References

`hoi4.reference_context`, `reference_search`, `reference_read` and `source_lookup` were discovered after the initial exposed-tool inventory and used when callable.
GUI context included both installed documentation and offline wiki with no missing or omitted required source kinds.
The wiki Dynamic Lists read returned lines 249-297, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`.
The installed-document read timed out after 600 seconds; its relevant text was read locally, so the returned source list alone is not counted as reading the rule.
Installed `common/scripted_guis/_documentation.md:62-90` documents effect/trigger bindings and `change_scope`; SHA-256 `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`.
Offline `Scopes - Hearts of Iron 4 Wiki.md:254-270` documents `THIS`, `PREV` and variable scopes; SHA-256 `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`.
Offline `Data structures - Hearts of Iron 4 Wiki.md:424-466` documents persistent and temporary variables; SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed `documentation/effects_documentation.md:7821-7910` documents setters; SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Vanilla `common/units/cavalry.txt` defines elephantry as a mobile frontline battalion; its division-template placement is separately confirmed against the historical parent block.
Source lookup identified `camp_admin_refresh_interface:326-434`, workspace index revision `443cf6209ca1f6f7333e2a08aab418d7af41d4727d23270efc4125efad665268`, and left references incomplete.
Scratch handoffs, original diffs, inventory and exact-byte checks are grouped in ignored `.tmp/c1_b9/`.

## Unresolved restoration and verification

- MQC, MQT, MQE, MQO and MQN have no runtime flag binaries in Git history or the examined local LFS archive; unbound generated candidates do not qualify as historical originals and were not installed.
- The 288 `No font with name UPPER_LEFT` messages have no source path; no `font`/`buttonFont` assignment to that token or incorrect text-box format was found, and quoted/unquoted grid format values both occur in vanilla.
- The single `Unknown promotion Ven` message has no matching current localisation expression.
- The original Matignon DDS remains unavailable according to the existing A5 audit; this pass introduces no replacement and does not claim to restore it.
- No game was launched, no fresh Linux log exists for this pass and no error-free-load or live-button claim is made.

The five missile automatic-event warnings and the six MQA/MQJ 24bpp warnings in the supplied log predate `03214eab58ef22b8619fdaec3504f429ac8f45e1`.
That current commit uses a two-day native MTTH base with reciprocal 0.5 to preserve median timing and keeps the original flag artwork in 32bpp; this pass leaves both corrections intact.
`generic_disjointed_gov.dds` already matches the historical pre-deletion original restored by `539006cd864907373edfdeffb3a447b0235b8b52`.
There are no design simplifications or prose/art reinterpretations in these commits.
The omitted Linux loop and unavailable/unrecoverable outputs above prevent claiming C1 fully complete.

Skills used: shared-git-commit, scripted-gui, decisions-missions, subagents and event-assets; specialists additionally used the unit/equipment/event and portrait checklists.
No skill was changed.
