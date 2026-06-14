# Coding Prompt — Implement Event 009 White Peace

Implement Event ID `9`, **White Peace**, from the spec package at:

`docs/specs/009_white_peace_specs/`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and relevant HOI4 wiki/vanilla documentation before editing. Do not use fallbacks or simplifications without reporting them clearly.

## Core requirements

- Register Event `9` as a repeatable event and Peace cluster ID `4` member.
- Keep the event unavailable when there are no active wars or no safe settlement candidates.
- Implement dynamic selection weight and cap behavior:
  - usually below default `1000`;
  - rises with active wars and safe minor-war candidates;
  - environment cap never above `1500`;
  - higher evolution stages reduce likelihood;
  - normal repeatable recovery and repeatable decay still apply.
- Implement base branch: one safe minor-versus-minor white peace.
- Implement stage I: repeated minor settlements from one firing, capped.
- Implement stage II: rare major-country settlement with strict safety gates.
- Implement stage III: broad diplomatic settlement, capped and protected-war safe.
- Popup must have one acknowledgement option only; no continue-war option.
- Avoid civil conflicts, near-capitulation cases, protected scripted wars, recent pair repeats, nonhuman/special threat actors, and unsafe subject/faction cases.
- Record event log, event detail, evolution detail, and Peace cluster detail.
- Add all required localisation, scripted localisation, skip reasons, and player-facing text.
- Add documentation under `docs/events/` and keep event catalog wording aligned after implementation.
- Implement or queue achievements from `prompts/009_white_peace_achievement_prompt.md` with explicit evidence.
- Use `prompts/009_white_peace_asset_prompt.md` for report image and achievement icon asset handoff.

## Required helper work

Create or reuse helpers for:

- runtime candidate preparation;
- dynamic cap calculation;
- country-level white-peace eligibility;
- pair-level eligibility;
- candidate scoring;
- applying pair settlement effects;
- marking recent country/pair settlement memory;
- evolution stage logging;
- event-list and cluster skip reasons.

If any dynamic helper is created, document it in the matching helper documentation file in the same change.

## Dynamic weight acceptance

Validate these cases and report real evidence:

1. no wars: unavailable;
2. one safe minor war: low cap below default event weight;
3. several safe minor wars: higher cap but not above `1500`;
4. protected wars only: unavailable;
5. stage II major branch: possible only with major stage and safety gates;
6. stage III broad branch: capped pair count and capped Chaos reduction;
7. repeat firing: normal repeatable decay lowers effective cap;
8. recent pair memory: same pair excluded until memory expires.

## Audit and subagent routing

Use `chaosx_scripted_system_architect` for dynamic helper design/patching if repeated logic is needed. Use `chaosx_localisation_auditor` before completion. Use `chaosx_event_completion_auditor` before claiming the event complete. Use `chaosx_spreadsheet_doc_worker` after final player-facing wording exists. Route visual work through the asset prompt and the correct asset subagents.

## Completion report

Report changed files, helper names, event IDs, localisation keys, cluster IDs, evolution IDs/stages, constants, variables/flags, validation scenarios, assets, achievements, docs, catalog status, and every simplification or blocker. If there are no simplifications, say so with evidence.
