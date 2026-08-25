# Event 014 final localisation and secrecy audit

## Scope and result

This bounded pass audited `localisation/english/014_cannibalism_l_english.yml`, `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`, and Event 014 visible consumers needed to prove localisation coverage and the pre-reveal identity gate.

Seven visible sentences violated the repository ban on semicolons. They were repaired in the owned English localisation file without changing gameplay meaning, costs, requirements, dynamic tokens, route identity, or reveal behavior.

No pre-reveal player-facing reference to Hannibal Lecter was found. The protected revealed name remains exactly `Hannibal Lecter`.

## Changed files and keys

- `localisation/english/014_cannibalism_l_english.yml`
  - `cannibalism_emergency_reinforcement_desc`
  - `cannibalism_emergency_reinforcement_cost_text`
  - `cannibalism_unified_mobile_consumption_effect_tt`
  - `cannibalism_unified_launch_air_interdiction_desc`
  - `cannibalism_unified_destroy_coalition_hub_desc`
  - `cannibalism_wendigo_press_terminal_hunt_requirements_tt`
  - `cannibalism_muster_wendigo_pack_from_enemy_death_receipt_requirements_tt`
- `common/scripted_localisation/014_cannibalism_scripted_localisation.txt` was audited and did not require a change.
- This handoff records the bounded audit and patch.

## Before and after display

Before the patch, seven descriptions, effect tooltips, requirements tooltips, or cost strings joined clauses with semicolons. After the patch, each clause is a direct sentence or a compact parenthetical separated by a comma. The displayed costs, readiness-only reserves, consumed receipts, and continental-ledger consequences are unchanged.

No dynamic localisation was added or changed. Every existing variable, constant, scope token, formatting code, and scripted-localisation call in the changed keys was preserved.

## Missing keys

None found.

The audit covered 2,033 declarations in the owned English file, direct visible key references from the Event 014 events, decisions, decision categories, focuses, ideas, characters, leader traits, hidden activation technologies, irregular units, scripted GUI, and GUI layout, nested `$key$` references, and `GetCannibalism*` calls.

The only `localization_key` targets in the Event 014 scripted-localisation file absent from English localisation were `GFX_sort_button_100x29` and `GFX_chaosx_sort_button_100x29_2`. These are deliberate sprite tokens returned by sprite selectors, not missing localisation keys.

## Duplicate keys

None found inside `014_cannibalism_l_english.yml` or across the English localisation set for keys declared by that file.

## Scripted localisation issues

None found. No duplicate `defined_text` names, missing `GetCannibalism*` definitions, or unresolved Event 014 scripted-localisation target keys were detected.

The shared event-log selectors explicitly require `cannibalism_reveal_complete` for the Evolution III title and description in the main Evolutions list, History details, Event Details evolution catalog, selected detail title, and selected detail body. The Event Details selector resolves the pre-reveal description first when the reveal flag is absent. The Event Details evolution preview adds Evolution III only after the reveal flag.

## Pre-reveal secrecy evidence

- `cannibalism_create_unified_country_from_selected_host` sets `cannibalism_reveal_complete` before creating or exposing the CBL country, Hannibal character, portrait, focus tree, reveal report, reveal news event, or reveal super-event audio.
- The Wendigo merge path likewise sets `cannibalism_reveal_complete` before transformed country identity, leader, portrait, focus overlay, report, news, or audio-facing work.
- Events `chaosx.nr14.70`, `.71`, `.72`, and all later reveal-route reports require `cannibalism_reveal_complete` or are fired only after the guarded reveal transaction.
- The revealed and Wendigo mechanic windows require `cannibalism_reveal_complete`. Their Hannibal titles and portraits therefore have no pre-reveal consumer.
- The unified and Wendigo focus trees are post-reveal packages. Their public Hannibal text cannot appear before the country creation or overlay load that follows the reveal flag.
- The visible achievement tracker row that resolves the defeat-Hannibal tooltip requires `cannibalism_reveal_complete`. The engine achievement entry is `hidden = yes`, and its static public name, `The Command Mantle Falls`, does not reveal the identity.
- The manual Event 014 scenario names, type labels, and descriptions contain no Hannibal or Lecter reference. The pre-reveal Event Details description and Evolution I and II text also contain neither name.
- The public world-end scenario titles are `The World Is the Larder` and `No Thaw Will Come`. Their Hannibal-bearing super-event bodies are reachable only through post-reveal terminal routes.
- Audio filenames and sound tokens containing `hannibal` are internal metadata. The reveal helper is called only after the reveal flag is set in both route transactions.
- Country and leader localisation preserve `CBL_hannibal_name: "Hannibal Lecter"` and `ZZZ_hannibal_wendigo_name: "Hannibal Lecter"` after reveal.
- No ancient-general disclaimer or substitute identity was introduced.

## Dynamic text and icon-first wording

Existing resource cost lines that use vanilla resources remain icon-first. The Event 014 mechanic windows use image-backed meter rows for Field Hunger, Command Integrity, Cult Cohesion, Larder, Frenzy, Network Alignment, Network Reach, anchors, and transformation progress. No separate inline Event 014 texticons are registered for those custom values, so adding unregistered `£` tokens would create broken glyphs. No unsafe localisation-only icon substitution was made.

State, country, actor, target, cost, timer, threshold, and meter values already use dynamic scopes or integer-formatted variables where the consumer needs them. No proven static-value defect required a new selector.

## Cross-surface consistency

No contradiction was found among Event 014 event text, Event Details pre-reveal and revealed descriptions, evolution titles and descriptions, country and leader names, decision and mission text, focus text, achievement tracker gating, scenario text, GUI titles, world-end scenario titles, or event-log selectors.

The pre-reveal text consistently describes missing burial parties, falsified ration and casualty records, ritual ranks, courier routes, and a concealed command center. Post-reveal surfaces consistently use Hannibal Lecter.

## Encoding

`localisation/english/014_cannibalism_l_english.yml` retains UTF-8 BOM bytes `EF BB BF`. No encoding concern was found. The scripted-localisation `.txt` source does not use a localisation YML header and was not rewritten.

## Prose-quality findings and repairs

- Vagueness: no proven vague passage remained in the audited visible set.
- Bloat: no bounded deletion was needed. Changed sentences retain only the readiness, consumption, receipt, and ledger facts needed by their mechanics.
- Obvious explanation: no title-repeating tooltip defect required a change.
- Repetition: no repeated sentence required a change.
- Overcomplication: the seven semicolon-linked clauses were simplified into direct sentences or a compact comma parenthetical.
- Style-rule repair: all seven semicolons were removed. No em dash, staged contrast formula, staccato chain, prompt fragment, implementation-history note, or hidden-mechanic explanation remains in the owned English file.

## Sourced quotations

The four attributed super-event quotations were preserved verbatim, including their capitalization and punctuation:

- `chaosx_super_event.49.q`, Thomas Hobbes, *Leviathan*
- `chaosx_super_event.50.q`, William Shakespeare, *King Lear*
- `chaosx_super_event.52.q`, Walt Whitman, *Specimen Days*
- `chaosx_super_event.53.q`, Lord Byron, *Darkness*

No sourced quotation was edited.

## MCP evidence

Event inspection and lint completed against workspace `mod_chaos_redux_ea3b2d67c2c0`:

- Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/09c690294ef7a9e3e1f64a0cc6e3d6aefd40378aff022cc880f3e9822d0a7f9a/a03f3c2d3cf972daa754675bd86c137211640d2866b9a04277bd05655b1a746f/event-trace-59143acd4a23.json`
- Lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f110acf169335ba4d00b0e042cb6002dc755662082c7387c18dc7b04dc2448f0/8b983257459110d2cb373b8b429d545132a6e351350e3d757010f820f5978e9f/event-lint-59143acd4a23.json`

Fresh `hoi4.gui_inspect` completed for all five Event 014 windows. Fresh 1920x1080 renders completed for the `normal`, `long-text`, and `missing-localisation` state request:

- Early header render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fcfae968916de2c03f1a02f42bf5dc720fcc83c255414d77af125652efc1ea15/a0c0174950c3cbd30b245afdc3e4c65dd1ca5ab907f40c6e0bff1e6dfb715476/cannibalism_early_header_window-full.svg`
- Network render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/a328b80fa464482856624781167fa7dccc27fe4f0fd248fbba3850476c33247c/cannibalism_network_window-full.svg`
- Warlord render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/356eda9a5565ef7475fbeca05d9002dcef5a8fbdc5f659787da7ef3a485f6ca7/1e6746525cce6b7553a78d99e9c37a40eb7bed9c31066d2f1f2e1efbd99b6ba0/cannibalism_warlord_command_window-full.svg`
- Revealed render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/d77cb097f1465c3215c618bcab316b01451061c0b3c3cedd87971cf2be179c84/cannibalism_revealed_command_window-full.svg`
- Wendigo render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5dca062f0ceea5b6be78543b2af1390a739f0896c5517587b74aaa42190738c7/0a9cc03e7bb971278cc7acdf9a8d1efd7df9742b9eac15ab62176d636f862317/cannibalism_wendigo_command_window-full.svg`

Fresh focus inspection and rendering completed for `cannibalism_unified_focus_tree`, `cannibalism_warlord_focus_tree`, and `cannibalism_wendigo_focus_tree`. The source-linked SVG artifacts are:

- Unified: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2171b48941e8dcc68b7e9b6b38c925d6eca4c4b3d8f6f4189e1d9c92bfa46884/74de8d3c8b0d7da3e58278b2abcda7f1c07c4e4f55eced06204b309e70bbb316/cannibalism_unified_focus_tree.focus.svg`
- Warlord: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5791167975f262b44ac05dacf7889e5132b14aa0f2ea9fadd1cd9da71db377fe/b99f7f8d5735c5c60a3afbc99398f8a70d23241ad7e5ef71871b17843a7eeddc/cannibalism_warlord_focus_tree.focus.svg`
- Wendigo: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/232389eb0676368c65dd7d366ccaac11558a757021802f9dd4c4c0119274643d/52734bef75ceb134687fa83df4b3bf58c3911d829e20794fbee1e3d17f4da10a/cannibalism_wendigo_focus_tree.focus.svg`

The installed MCP exposed a technology inspection route despite the repository note that a Technology Tree Viewer may be absent. The scan completed, and the hidden bridge technology `cannibalism_scavenger_warband_tech` rendered with source-linked metadata:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6977695c3245910ed6b1304915b83f90be2706e4f1e6c33d4cc40a74542c2b7f/e570e3bf7adbe1aa7e90f6b5795c71b95e40fc818a8d57c6c3cf38c42a98187f/technology-technology-da5928f7108c.svg`

The authoritative render call returned `TECH_RENDERED_PARTIAL` with status `ok`; no technology source changed.

## Meaningful validation and blockers

- Structural localisation checks found no missing or duplicate Event 014 keys, unresolved dynamic references, malformed rows, empty values, or lost integer formatters.
- The protected-name scan confirms that every public leader identity remains exactly `Hannibal Lecter` after reveal.
- The final owned English file contains no semicolon or em dash.
- The YML BOM remains intact.
- `hoi4.event_render` for the large Event 014 namespace timed out after 180 seconds. This is the only skipped current MCP render evidence. The narrower event trace and lint both completed, and every linked focus and GUI surface received a fresh successful inspection and render.
- No `hoi4.gui_rewrite` was used because no GUI layout or source change was required.
- No spreadsheet update was needed because the seven changes affect decision descriptions, costs, effect tooltips, and requirements tooltips rather than catalog-mirrored Event Details, evolution, or scenario prose.

## Unresolved wording decisions and follow-up

None. No new mechanic, lore, route, or cross-owner script change was required, so no separate design plan was written.

No simplification or fallback was used.
