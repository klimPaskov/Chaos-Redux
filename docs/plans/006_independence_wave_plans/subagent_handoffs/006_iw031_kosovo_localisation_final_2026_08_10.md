# IW-031 Kosovo final localisation and documentation handoff

**Date:** 2026-08-10  
**Scope:** final bounded IW-031 Kosovo localisation and documentation audit after portrait wiring, including the linked FORM-09 text surface.  
**Mode:** localisation and documentation patch only. No gameplay redesign, central attestation change, staging, commit, or spreadsheet edit.

**Authority note (2026-08-13):** The package boundary cited below is a dated pre-IW-040/IW-044 snapshot. Current Event 006 routing is 31 content-attested packages across 28 compatible reservation groups, 162 unattested selectable rows, and 39 runtime adapters; the Kosovo localisation findings remain valid.

This handoff supersedes the unresolved-character conclusion in `006_iw031_kosovo_localisation_audit_2026_08_09.md`. The three character definitions, names, descriptions, sprites, DDS source placeholders, checkpoint recruitment calls, roster proof, route promotion calls, and cleanup calls now exist.

## Outcome

The current source defines 129 scoped English localisation keys across the Kosovo package, Kosovo portraits, and FORM-09 files. The audited source-derived package set contains 97 Kosovo package keys, six character keys, and 26 FORM-09 keys. No scoped key is missing or duplicated.

All displayed Kosovo ledger limits, thresholds, gains, losses, route effects, and costs still match the called constants and effect chains. The character and package documentation now records the completed source-placeholder wiring and its chronology limits without claiming that wartime photographs were taken in 1936.

IW-031 is now present in the central content-attestation trigger and the exact KOS/state-802 normal and scenario preflight branches. At this handoff's dated snapshot, the boundary was 28 content-attested packages across 25 compatible reservation groups, with 165 selectable rows unattested and 36 registered adapters; that arithmetic is superseded for current routing by the authority note above.

## Missing key list

None in the assigned Kosovo, Kosovo portrait, or FORM-09 source surface.

The direct consumer check found every `name`, `desc`, `custom_cost_text`, `custom_effect_tooltip`, party-name, idea-name, idea-description, character-name, and character-description key used by the scoped package source. The seven FORM-09 state-puzzle summary and state-tooltip keys also exist exactly once.

## Duplicate key list

None. The scan compared all 129 scoped keys against every English localisation file.

## Scripted localisation issues

None found in the Kosovo package. Its two compact ledgers and all displayed deltas use direct scoped variables or script constants.

The linked FORM-09 state-puzzle summary and state tooltips call existing shared scripted-localisation functions. No selector name was changed or removed.

## Dynamic text opportunities

No new dynamic selector was justified. Civic Concord, Municipal Reach, their exact limits, the stable threshold, every cost, and every effect delta are already dynamic.

The three grounded character names remain stable character localisation keys. A `character_name` formatter would add indirection without changing any current display because the roster identities are fixed and the route tooltips intentionally name the incoming government leader.

## Cross-surface alignment

- `KOS_independence_wave_ferhat_draga` and both route tooltips now use the full sourced display name `Ferhat Bey Draga`.
- The socialist character description no longer assigns later wartime partisan language to the 1936-facing roster. It describes Popović's communist organising role through the same mine, workshop, railway, and municipal institutions used by the route.
- `docs/events/006_independence_wave/kosovo_package.md` now records all three installed character consumers, their route roles, source-placeholder mode, source dates, runtime dimensions, DDS and sprite wiring, and current attestation boundary.
- `docs/events/006_independence_wave/form09_balkan_federation.md` identifies Kosovo as an eligible member through the centrally attested IW-031 package and state 802 anchor.
- `independence_wave_form09_ratify_border_board_cancel_effect_tt` now discloses the exact failure deltas when war, capital loss, or carrier invalidation cancels the Federal Border Board project.
- `independence_wave_form09_invitation_response_cancel_effect_tt` now explains why a FORM-09 invitation response disappears before consent is recorded.
- `006_source_of_truth_map.md`, `006_independence_wave_resume_packet.md`, and `docs/events/006_independence_wave/overview.md` now record the complete roster, exact admission paths, and current 28/25/165 boundary.

## File encoding concerns

None. The Kosovo package, Kosovo portrait, and FORM-09 localisation files all begin with `EF BB BF`, contain no duplicate scoped keys, and retain UTF-8 with BOM.

## Prose-quality repairs

### Vagueness

`independence_wave_kos_hold_cantonal_compact_together_desc` previously said to raise "both public ledgers." It now names Civic Concord and Municipal Reach and states that a government must be established.

### Bloat

No further compression was safe in the exact host-settlement or corridor tooltips. Each shows two distinct called effect bundles, so removing either paragraph would hide real value changes.

### Obvious explanation

The stale package sentence explaining what portrait admission still required was replaced with the installed roster, route roles, source-placeholder wiring, and provenance facts.

### Repetition

No new repetitive player-facing passage remained after the previous icon-first cost pass. Route and national-spirit descriptions retain distinct civic, socialist, federal, and emergency institutions.

### Overcomplication

The compact mission description now uses the visible value names instead of the abstract phrase "public ledgers." The dense host and network effect tooltips remain split by the actual settlement and accord actions.

### Style-rule repair

The Popović description no longer uses an anachronistic wartime `partisan discipline` claim. Both Ferhat route tooltips match the complete sourced identity. No em dash, sentence semicolon, working label, prompt fragment, update-history phrase, staged contrast formula, or hidden-route disclosure remains in the audited player-facing files.

## Sourced quotation preservation

No inspected player-facing key contains an attributed quotation. The attributed constitutional quotations in the Kosovo flag research handoff were not edited, shortened, repunctuated, or modernised.

## Sourced identity and chronology notes

- Ferhat Bey Draga is consistently identified under that full display name in the character key, route tooltips, package document, and portrait manifest.
- Miladin Popović retains the Serbian Latin spelling with `ć`. His source photograph is dated circa 1943 to 1944, so the documentation identifies it as a later archival source placeholder rather than a 1936 photograph.
- Shaban Polluzha retains the sourced public name, with `Shaban Mustafë Kastrati` preserved as the manifest alias. His runtime source is a named-individual archival portrait reproduced in a later exhibition photograph, with the earlier group-image crop retained only as rejected research evidence and the original photographer/date caveat documented.
- All three are intentional grounded source placeholders under the accepted portrait workflow. No generated or repainted likeness, styled-final request, advisor derivative, dossier derivative, or small portrait is claimed.

## Changed files and keys

### Localisation

Changed `localisation/english/006_independence_wave_kosovo_l_english.yml`:

- `independence_wave_kos_hold_cantonal_compact_together_desc`
- `independence_wave_kos_civic_route_effect_tt`
- `independence_wave_kos_federal_route_effect_tt`

Changed `localisation/english/006_independence_wave_kosovo_portraits_l_english.yml`:

- `KOS_independence_wave_miladin_popovic_desc`

Added to `localisation/english/006_independence_wave_form09_l_english.yml`:

- `independence_wave_form09_ratify_border_board_cancel_effect_tt`
- `independence_wave_form09_invitation_response_cancel_effect_tt`

No dynamic token, formatter, colour terminator, cost, threshold, requirement, or consequence was removed.

### Documentation

Changed:

- `docs/events/006_independence_wave/kosovo_package.md`
- `docs/events/006_independence_wave/form09_balkan_federation.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- this handoff

## Display before and after

- Before, the founding mission referred to unnamed public ledgers. After, it names Civic Concord and Municipal Reach.
- Before, the civic and federal route effects shortened Ferhat Bey Draga's sourced name. After, they match the character display key.
- Before, Popović's description projected later partisan language onto the 1936-facing roster. After, it describes the institutions he organises in the route.
- Before, the package document said the portrait roster and wiring were still required. After, it records the installed source-placeholder consumers and their chronology limits.
- Before promotion, FORM-09 documentation treated IW-031 admission as pending. After the country owner added the central attestation and exact preflight branches, the page identifies the package and state-802 member path as admitted.
- Before, cancelling the Federal Border Board exposed the raw applied deltas without a concise consequence line. After, the custom cancellation tooltip states that Legitimacy, Recognition, and Security each fall by the exact dynamic minor value and Instability rises by the same dynamic value.
- Before, three shared FORM-09 response decisions called a missing cancellation key. After, each displays that the invitation response was withdrawn before consent was recorded.

## Meaningful validation

- Compared the Kosovo decision, trigger, payment-effect, reward-effect, and failure-effect chains against every displayed cost and delta. Administration costs disclose Command Power, manpower, and one civilian factory. The strategic cost discloses Stability, War Support, Command Power, the equal ten-unit convoy-or-train alternative, and one civilian factory.
- Verified all 129 scoped definitions against the English localisation tree. No scoped duplicate exists.
- Verified all direct source references collected from the Kosovo and FORM-09 decision, category, idea, character, and party consumers. No required key is missing.
- Verified both cosmetic families retain base, `_DEF`, `_ADJ`, and all four ideology-specific variants.
- Verified every party short and long key used by `set_party_name` exists.
- Verified the three character names and descriptions against their character definitions, portrait manifest, roster event, route promotion calls, and cleanup calls.
- Verified the three localisation files retain UTF-8 with BOM after the patch.

## MCP evidence and limitations

The required event inspection for hidden roster checkpoint `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` in workspace `mod_chaos_redux_ea3b2d67c2c0`. The linked trace artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24e3af077a8724612fd9c26818d8f55ff1380251a4628b8036639ce74f281f9c/2c73de352deab293035955e5b7c5e66575fbb0b1a72084bd45de2a4015a61730/event-trace-7e8e9a563058.json`

The linked FORM-09 GUI inspection returned `GUI_INSPECTED` and produced:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec82d4184b5e0ae447325429a9d221818be8fefdbc0794965ddebf521f5e1c77/c2eddb85200d44ebe497c726c52107463a8a21032f97784db271449f52d410c6/gui-inspect.e23e700c424cdd81.json`

The focused normal, long-text, and missing-localisation render at 1920x1080 produced:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5cf4a0e6908e754ba9e1bae29b05ae013092399118afcfe42cedf62d2833fe9/264747d985d2409ff0e8200d6fced2a074227d9fcff02a5b8f020b10e65b0ae5/chaosx_independence_wave_formable_state_puzzle_w-full.svg`

The shared GUI inspection was not clean enough to prove isolated FORM-09 overflow. It reported repository-wide diagnostic truncation, 2,000 retained blocking graph diagnostics, 1,034 visible-overlap diagnostics, and thousands of dropped shared-source diagnostics. The render returned `GUI_RENDERED`, but its response was truncated and its validation did not pass. These aggregate diagnostics are not assigned to the FORM-09 text, and the source review is not treated as equivalent visual proof.

## Skipped meaningful validation

- The installed MCP exposes no default decision-category localisation render route. Exact source coverage is complete, but live wrapping of the longest Kosovo host and network tooltips remains a consumer-side observation.
- The FORM-09 shared GUI render could not isolate a clean family-only validation result because the global GUI graph exceeded diagnostic ceilings.
- The Technology Tree Viewer is absent from the installed package. No technology surface belongs to IW-031.
- No in-game validation was performed. Live consumer validation belongs to the user.

## Unresolved wording and parent follow-up

None. The remaining evidence limitations are validation boundaries rather than unresolved wording decisions.
3. A later family-isolated FORM-09 render should confirm the summary and state-802 tooltip at supported resolutions if the MCP diagnostic ceiling is repaired.

## Simplifications, omissions, and blockers

No gameplay or localisation fallback was introduced. No sourced quotation or dynamic token was altered. Clean family-isolated GUI overflow evidence remains unavailable from the installed MCP route and is reported as an evidence limitation rather than inferred from source.

No improvement plan was written because the remaining issues are bounded admission, documentation ownership, and tooling-evidence gates rather than a missing mechanic.
