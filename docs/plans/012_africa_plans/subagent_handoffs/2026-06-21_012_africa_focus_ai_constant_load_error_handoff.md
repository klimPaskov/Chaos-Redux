# 2026-06-21 Event 012 Africa Focus AI Constant Load Error Handoff

## Scope

Fixed the Event 012 Africa focus load-error surface reported from the game log:

- `common/national_focus/012_africa_authority_focus.txt`
- `common/national_focus/012_africa_focus.txt`

The reported malformed tokens were `constant:africa_ai.strong`, `constant:africa_ai.preferred`, and `constant:africa_ai.normal` in focus `ai_will_do` weight fields. The current workspace already used file-scoped `@africa_ai_*` constants in those fields. I preserved that parser-safe pattern and added a short comment above both local mirror blocks so future edits do not reintroduce `constant:africa_ai.*` in focus AI weights.

## Changed Files

- `common/national_focus/012_africa_authority_focus.txt`
  - Added a comment documenting that focus `ai_will_do` rejects `script_constants` in this parser and that local `@africa_ai_*` constants must stay mirrored with `common/script_constants/012_africa_constants.txt`.
- `common/national_focus/012_africa_focus.txt`
  - Added the same parser-safety comment above the local `@africa_ai_*` constants.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_focus_ai_constant_load_error_handoff.md`
  - This handoff.

No decision files were edited.

## Replaced Tokens And Counts

Unsupported `constant:africa_ai.*` tokens remaining in the two parsed national focus files:

| File | Remaining `constant:africa_ai.*` tokens |
| --- | ---: |
| `common/national_focus/012_africa_authority_focus.txt` | 0 |
| `common/national_focus/012_africa_focus.txt` | 0 |

Current parser-safe local AI weight references, excluding the four file-scoped definitions in each file:

| File | `@africa_ai_low` | `@africa_ai_normal` | `@africa_ai_preferred` | `@africa_ai_strong` | Total AI weight references |
| --- | ---: | ---: | ---: | ---: | ---: |
| `common/national_focus/012_africa_authority_focus.txt` | 0 | 15 | 15 | 29 | 59 |
| `common/national_focus/012_africa_focus.txt` | 18 | 70 | 96 | 14 | 198 |

The local values match `common/script_constants/012_africa_constants.txt`:

| Local constant | Mirrored script constant | Value |
| --- | --- | ---: |
| `@africa_ai_low` | `constant:africa_ai.low` | 0.35 |
| `@africa_ai_normal` | `constant:africa_ai.normal` | 1 |
| `@africa_ai_preferred` | `constant:africa_ai.preferred` | 1.5 |
| `@africa_ai_strong` | `constant:africa_ai.strong` | 2.25 |

## Changed Focus IDs

No focus IDs changed. No prerequisites, route locks, mutual exclusions, rewards, icons, localisation keys, or decision unlocks changed.

## Route Behavior Before And After

Before:

- The user-provided game log indicates the active parsed focus files contained unsupported `constant:africa_ai.*` tokens in `ai_will_do` weight fields.
- In the current workspace, those focus files already had parser-safe local `@africa_ai_*` constants before this handoff pass.

After:

- The two focus files contain no `constant:africa_ai.*` tokens in national focus AI weight fields.
- AI route weighting remains behavior-equivalent because the local `@africa_ai_*` values mirror the shared `africa_ai` script constants.
- Comments in both focus files document why these AI weight values intentionally use local `@` constants instead of `constant:` tokens.

## Validation Performed

- Consulted offline Paradox wiki National focus, AI modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, and Idea modding pages.
- Consulted vanilla focus examples under `/home/klim/projects/Hearts of Iron IV/common/national_focus/`; vanilla focus `ai_will_do` examples use literal numeric `factor` values such as `1`, `30`, `50`, `100`, and `150`.
- Consulted vanilla script constant documentation:
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/common/script_constants/documentation.md`
- Ran a targeted search for `constant:africa_ai` under `common/national_focus`; no parsed national focus references remain.
- Counted current local `@africa_ai_*` usage in both affected focus files and checked the values against `common/script_constants/012_africa_constants.txt`.

## Skipped Validation

- Did not run an in-game load or external HOI4 parser pass from this subagent environment.
- Did not edit or validate Event 012 decision files because the task explicitly reserved decisions for another subagent.

## Remaining Risks

- Historical handoff markdown files still mention old `constant:africa_ai.*` usage. They are not parsed by the game and were left unchanged.
- The two focus files still use other `constant:africa_*` tokens in rewards and variable checks. Those were outside the reported malformed AI weight field surface and were not changed.
- If future edits copy `constant:africa_ai.*` back into focus `ai_will_do`, the same load error can recur; the new comments mark the local pattern to avoid that.
