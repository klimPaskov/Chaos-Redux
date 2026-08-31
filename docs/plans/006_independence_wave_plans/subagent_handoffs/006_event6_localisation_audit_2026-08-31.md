# Event 006 localisation audit and named-bonus repair

Date: 2026-08-31 (Europe/Kyiv).

Owner: `chaosx_localisation_auditor` for `/root`.

Status: narrow localisation patch applied; parent review required.

## Scope and authority

This audit covers the current Event 006 English localisation set, event titles, descriptions and options, decision and mission titles and descriptions, decision categories, shared and package focus text, ideas, scripted-localisation consumers, Event Log and Event Details selectors, current source-of-truth documents, and the retired pre-event crisis compatibility surface.

The accepted authority remains HOLD / PARTIAL: 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, 161 unattested rows, and the exact `3/4/5/7/10` ladder. The public Event 006 report remains the first player-facing indication. No crisis, pressure, category, mission, cost, queue, history row, or other Event 006 indication may appear before that report.

## Defect found and patch

Six named research or doctrine bonuses in `common/national_focus/006_independence_wave_focus.txt` had no English localisation. Their `name` fields are player-facing bonus labels, so the raw identifiers could appear in the technology or doctrine bonus display.

The following keys were added to `localisation/english/006_independence_wave_focus_l_english.yml`:

- `independence_wave_industrial_administration_bonus`: `Independent Industrial Administration`
- `independence_wave_professional_defense_bonus`: `Professional Defense Institution`
- `independence_wave_domestic_arsenal_bonus`: `Domestic Arsenal Program`
- `independence_wave_league_standardization_bonus`: `League Army Standardization`
- `independence_wave_patron_industry_bonus`: `Patron-Financed Industrial Development`
- `independence_wave_network_industry_bonus`: `Civil-Service Exchange`

Before the patch, the six named bonuses had no matching English keys. After the patch, each focus reward retains its existing source identifier and displays a concise label tied to the granting focus. No focus effect, bonus value, category, AI weight, route, package gate, admission rule, or visibility trigger changed.

## Audit lists

- Missing keys: the six named bonus keys above were the only missing current Event 006 display references found. They are now repaired.
- Duplicate keys: none among the 37 Event 006 English localisation files, and none of their keys are duplicated elsewhere in the mod English localisation set.
- Malformed keys: none. No Event 006 key uses `:0`, a malformed header, or a nonconforming localisation line.
- Scripted localisation issues: none found. All 45 Event 006 getter calls found in the English text resolve to defined `GetIndependenceWave*` scripted-localisation methods, all Event 006 `localization_key` consumers resolve, and dynamic bracket and dollar-key delimiters are balanced.
- Dynamic text opportunities: no safe missing dynamic value was found. Existing costs, timers, state names, country names, actor names, and ledger values retain their current dynamic tokens. The six bonus labels are identities rather than tunable values and should remain static.
- Cross-surface mismatches: none found in the current Event 006 Event Details, event/evolution selector, decision, category, focus, or idea reference graph. The premise-only Event Details key remains free of exact thresholds, package identifiers, and rival-bloc ledger selectors.
- File encoding concerns: none. All 37 Event 006 English files have the UTF-8 BOM, including the patched focus file after the edit.
- Pre-event wording: no retired `independence_wave_crisis*` English keys remain. The only exact retired runtime references are inert compatibility helpers: the effects are empty, the triggers return `always = no`, and hidden event `chaosx.nr6.3` only clears stale flags and a stale variable. Package-local post-report uses of the word “crisis” remain valid and are gated by package setup or post-release state.
- Sourced quotation preservation: `chaosx_super_event.23.q`, the attributed Woodrow Wilson quotation, was inspected and left byte-for-byte unchanged. No quotation-bearing key was edited.

## Prose-quality review

- Vagueness: no current scoped passage required a safe rewrite. The six new labels name the institution or program that grants the bonus.
- Bloat: no prose was expanded. Each repaired label is a short noun phrase.
- Obvious explanation: no tooltip or description was added that repeats a visible focus effect.
- Repetition: the labels intentionally track their granting focus but do not duplicate a description or consequence line.
- Overcomplication: the repaired labels avoid implementation terms, identifiers, and administrative clauses.
- Style-rule repair: no sentence punctuation or sourced prose changed. The new labels contain no em dash, semicolon, staged contrast, fragmentary instruction, or tuning history.

## Meaningful validation

- A complete current-source scan resolved 2,767 explicit Event 006 localisation references after the patch. Decision parsing found 792 decision or mission ids with title and description keys; category parsing found 88 category ids with titles; focus parsing found 318 actual focus ids with titles and descriptions; idea parsing found 422 idea ids with titles and descriptions; and 152 referenced Event 006 ideas resolve. The focus-tree container id was excluded because it is not a focus node and does not consume an `_desc` key.
- All 208 Event 006 dollar-key substitutions resolve, all 45 used `GetIndependenceWave*` methods resolve, and the scan found no unbalanced dynamic localisation delimiter.
- Read-only `hoi4.event_inspect` traced `chaosx.nr6.1` downstream and returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08314948091a6bab5e947fa39898fbe892f3cf3e5d00ce49b85f94b0243fc322/641296575776ffeb6e1ade7bb451f392958d15393777a85082527b58616d89d8/event-trace-cfdc65be2a28.json`. The artifact is source-linked but remains partial because workspace-wide helper and lifecycle projections were deferred.
- Read-only `hoi4.focus_inspect` for `common/national_focus/006_independence_wave_focus.txt` returned `FOCUS_INSPECTED` at revision `fd50335e92fb6d0d3ca7afe3c2bfc9b1193553b78ec49285d414ae1393383519`, with 184 resolved focus titles and no Event 006 focus diagnostic. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae8f6f802ad919d671fbbd857eaf85ffd6322c6c9048a0def37b9798cb3b27f2/a10cf01a42316c61aa2b096ac78c476e5b456965f689c23a92bc3115db354f2e/focus-inspect.fd50335e92fb6d0d.json`.

## Skipped or blocked validation

The required production GUI inspection for `events_log_event_details_window` accepted the object-shaped Event 006 review scenario but did not return after more than 90 seconds and was terminated without an artifact. No `hoi4.gui_render` was attempted because its prerequisite inspection did not complete. Therefore this audit does not claim current production-render proof for Event Details wrapping, clipping, overflow, or long-text layout, and source checks are not treated as equivalent visual evidence.

No live Hearts of Iron IV process was launched, and no live standalone report, save/load, release, or post-release UI claim is made. No probability route was run because the patch changes no weight or AI surface.

## Changed files

- `localisation/english/006_independence_wave_focus_l_english.yml`: added the six named bonus keys listed above.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_localisation_audit_2026-08-31.md`: added this audit and patch handoff.

Dynamic localisation added or fixed: none.

Sourced quotations and all existing dynamic tokens were preserved without exception.

## Remaining risks and parent follow-up

The shared Event Details production render remains unverified because the GUI MCP inspection did not return. Event inspection remains partial rather than engine-complete. The broader Event 006 disposition remains HOLD / PARTIAL at 32/29/40/161, and none of the 161 unattested rows is promoted or given fallback localisation by this patch.

No gameplay, admission, AI, weight, asset, spreadsheet, or pre-event surface change was made. No simplification or fallback was introduced.
