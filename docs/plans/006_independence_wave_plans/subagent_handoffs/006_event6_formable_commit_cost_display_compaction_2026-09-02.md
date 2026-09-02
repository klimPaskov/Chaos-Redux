# Event 006 formable commit cost display compaction

Date: 2026-09-02

## Scope

This bounded localisation-only pass improves the readability of the selected formable commitment cost while preserving the accepted payment contract.

## Changed surface

- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `independence_wave_formable_commit_cost_civic`
- `independence_wave_formable_commit_cost_revolutionary`
- `independence_wave_formable_commit_cost_military`

## Repair

The civic, revolutionary, and military rows now use deliberate line breaks so the strategic, transport, and reserve charges do not collapse into one overlong horizontal string in the decision panel.

Every previously displayed charge remains present, including stability, command power, the convoy-or-train transport alternative, manpower, army experience, infantry equipment, and support equipment where the selected method consumes them.

The trigger and payment effect remain unchanged: negotiated, dynastic, and league methods use the civic palette, revolutionary uses strategic plus security-standard, and military or hidden high-chaos methods use strategic plus security-major.

No cost amount, resource type, selector, availability check, AI behavior, route gate, category visibility rule, pre-event surface, or fallback changed.

## Validation

The edited localisation file retains its UTF-8 BOM and the three method rows retain the same dynamic constants and scripted transport selector as their pre-patch values.

The shared commit decision still references `independence_wave_cost_selected_formable_commit`, and its custom cost trigger and payment effect remain aligned with the method selector.

No live Hearts of Iron IV launch or production decision-render claim is made because the installed read-only decision-cost render route is unavailable.

Event 006 remains HOLD / PARTIAL under the current package, rights, probability, GUI, super-event, and live-runtime gates.
