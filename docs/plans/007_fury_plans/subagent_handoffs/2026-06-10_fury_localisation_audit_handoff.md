# Fury Localisation Audit Handoff

Date: 2026-06-10
Agent role: Chaos Redux localisation subagent
Scope: Event 007 Fury localisation and scripted-visible text only.

## Files Changed

- `localisation/english/chaosx_gui_l_english.yml`

## Changed Keys

- `chaosx.scenarios.fury.desc.pact`
- `chaosx.scenarios.fury.desc.hostile`
- `chaosx.events_log.window.event_details.fury`

## Before And After

- Before: the triggerable scenario descriptions used `safe AI minors`.
- After: they use `eligible non-player minor countries` / `eligible minors`, matching the actual exclusion rules without using internal selection wording.
- Before: the event details body described `scaled stockpiles` and a `weekly reinforcement loop`.
- After: it describes `stockpiles scaled to its size` and `recurring reinforcement waves`, keeping the same behavior but avoiding implementation-facing wording.
- Before: the event details body said Fury seeks `valid AI neighbors`.
- After: it says Fury seeks `valid non-player neighboring targets`, which better matches the player-facing rule that player and player-linked countries are excluded.

No gameplay meaning changed.

## Dynamic Localisation Added Or Fixed

- None. Existing Fury dynamic scope references were coherent:
  - `[fury_news_actor.GetName]` is backed by `save_event_target_as = fury_news_actor` before `chaosx.news.7007`.
  - `[fury_terminal_player_target.GetName]` is backed by `save_global_event_target_as = fury_terminal_player_target` before `chaosx.nr7.52`, with cleanup present.

## Validation

- Re-ran a Fury key coverage audit over the scoped localisation files and Fury script references:
  - focus title/description keys: 0 missing
  - idea title/description keys: 0 missing
  - decision title/description keys: 0 missing
  - decision category title/description keys: 0 missing
  - achievement name/description/tooltip keys: 0 missing
  - explicit Fury scripted/localisation references: 0 missing
  - duplicate keys in scoped localisation files: 0
  - `:0` keys in scoped localisation files: 0
- Confirmed `localisation/english/chaosx_gui_l_english.yml` still begins with UTF-8 BOM after the patch.
- Checked Fury cost text against `common/script_constants/007_fury_constants.txt`; the visible cost values match the current script constants for the audited decisions.

## Findings For Parent Review

- No missing Fury localisation keys found in the requested surfaces.
- No duplicate Fury localisation keys found across `localisation/english/*.yml`.
- No broken Fury scripted-localisation references found for scenario, event-detail, or super-event slots `59` and `60`.
- No hidden-route spoiler text found in the Fury scenario/detail strings inspected.

## Residual Risk

- This was a static text/key audit. It did not run the game UI or validate in-engine rendering.
- The wider worktree is dirty with parent/user changes; this handoff only claims the three Fury localisation key edits above.
