# Custom-Cost Affordability Skill Note Handoff

Date: 2026-09-02

## Status

Complete for the bounded skill-maintenance scope. This subtask changed only the existing decisions skill and this handoff. No gameplay, MCP, configuration, generated-agent, log, asset, or spreadsheet files were changed. No commit was created.

## Verification proof

- The offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:299-319` documents `custom_cost_trigger` and `custom_cost_text`, states that a custom cost does not itself debit resources, and documents manual subtraction in `complete_effect` plus the fixed `ai_hint_pp_cost` hint for political power.
- The vanilla AUS precedent separates `available` from `custom_cost_trigger` (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AUS.txt:983-995`) and manually subtracts the displayed political-power and command-power payment in `complete_effect` (`AUS.txt:1018-1023`).
- A focused search of the existing decisions skill found cost-budget and cost-localisation guidance but no reusable rule connecting custom-cost display, availability gating, shared affordability predicates, one-time debit, and `ai_hint_pp_cost`.

## Exact skill edit

Updated `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-decisions-missions\SKILL.md` under `## 6. Cost localisation`.

Added `### Custom-cost affordability and payment` requiring a shared inclusive affordability predicate in both `available` and `custom_cost_trigger`, one manual debit in `complete_effect`, and a fixed `ai_hint_pp_cost` when political power is included. It permits `hidden_trigger` for the availability duplicate when the cost row already explains payment, and cautions against inferring undocumented engine behavior from display alone.

## Caveats and parent review

- This is reusable documentation guidance only. No MCP call, game run, log inspection, or live engine comparison was performed.
- The skill contains no event-specific identifiers, scenarios, paths, or history.
- The parent should review the focused diff and create the meaningful closure-tranche commit separately.
