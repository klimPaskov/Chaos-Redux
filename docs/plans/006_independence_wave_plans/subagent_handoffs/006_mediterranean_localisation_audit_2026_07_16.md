# Event 006 Mediterranean Localisation Audit Handoff

Date: 2026-07-16

Mode: audit with permission for small localisation-only corrections

Verdict: **READY** for parent integration.

## Bounded scope

This audit covers the English localisation tranche for IW-017 Corsica (`COR`), IW-018 Sardinia (`ARX`), IW-019 Sicily (`ASX`), and FORM-05 Mediterranean Island League (`MIX`):

- `localisation/english/006_independence_wave_mediterranean_l_english.yml`
- `localisation/english/006_independence_wave_form05_l_english.yml`
- Their current character, idea, focus, tooltip, decision, mission, event, party, AI-plan, scripted-localisation, country-identity, cosmetic-identity, and player-facing dynamic-value consumers.

Gameplay logic, assets, allocator/admission work, and git history were not changed.

## Source-of-truth review

The audit was checked against:

- `AGENTS.md`.
- The complete `chaos-redux-events` and `chaos-redux-subagents` skill instructions.
- The required offline wiki core, Localisation, Event Modding, Decision Modding, Idea Modding, AI Modding, Character Modding, Country Creation, Cosmetic Tag Modding, and National Focus Modding guidance.
- Vanilla localisation formatter/object documentation and the relevant documented effects and triggers, with vanilla country, character, idea, decision, focus, and event localisation conventions as precedents.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`.
- The accepted Mediterranean direction in the Event 006 specification, `docs/events/006_independence_wave/mediterranean_island_packages.md`, and `docs/events/006_independence_wave/form05_mediterranean_island_league.md`.
- The current Mediterranean country-package, focus-tree, and localisation handoffs in this folder.

## Consumer reconciliation

The current mod-owned inventory remains fully resolved:

| Surface | Expected | Defined | Missing | Duplicate definitions |
| --- | ---: | ---: | ---: | ---: |
| Mediterranean owned file | 308 | 308 | 0 | 0 |
| FORM-05 owned file | 125 | 125 | 0 | 0 |
| Canonical shared Event 006 files | 49 | 49 | 0 | 0 |
| **Total mod-owned consumers** | **482** | **482** | **0** | **0** |

The 49 intentionally shared definitions are the 30 ARX/ASX country-identity keys, six shared decision-cost labels, ten names/descriptions for the five adviser traits used here, two Mediterranean focus scripted-localisation labels, and one Mediterranean formable-family name. Vanilla remains the single source for the base COR identity and its ideology variants; this tranche does not override them.

The 308-key Mediterranean file resolves:

- 14 character names and the six political-adviser descriptions.
- 50 short/long party-name keys.
- Three public package-value labels.
- Nineteen package national spirits and their descriptions.
- Three decision categories, 29 decisions/missions, and their descriptions.
- Seventeen package decision/effect summaries.
- Nineteen package focuses, their descriptions, and their completion summaries.
- All 42 title/description/option/option-tooltip keys used by events `chaosx.nr6.21` through `.27`.
- Seventeen readable AI strategy-plan labels.

The 125-key FORM-05 file resolves:

- The full 15-key MIX base and ideology identity set.
- The charter category and its description.
- Thirteen scripted-localisation outputs for the delegation ledger, congress-seat model, and delegation status.
- Three public charter values and their descriptions.
- Sixteen decisions/missions and their descriptions.
- Thirteen dynamic cost labels and thirteen effect summaries.
- Three FORM-05 national spirits and their descriptions.
- All 25 title/description/option/option-tooltip keys used by events `chaosx.nr6.28` through `.34`.

Every scripted event option in `.21` through `.34` has a matching single definition. No player-facing consumer in the bounded gameplay files resolves to a working label, placeholder, duplicate, or absent key.

## Content findings

- COR remains Corsica and uses its vanilla country identity. ARX is explicitly Sardinia rather than Sardinia-Piedmont. ASX is explicitly Sicily; the Two Sicilies material is presented as a political claims dossier, not as existing ownership or cores. MIX is consistently a Mediterranean Island League cosmetic identity whose members remain sovereign.
- Character localisation follows the all-male package contract. No female name, gender marker, or female pronoun appears in either owned file.
- The six adviser descriptions describe offices and policies only. None claims an adviser icon, portrait, dossier card, or other visual asset.
- Event options are complete, and the prose follows the Event 006 political/institutional tone. No update-history wording, setup-attestation language, placeholder prose, em dash, semicolon, or prohibited dialectical formula was found.
- Player-facing variable and script-constant expressions all carry an explicit integer or percentage format (`|0` or `|%0`); zero unformatted numeric expressions were found.
- Both owned files are UTF-8 with BOM, contain no `:0` keys, and have no duplicate key inside the file.

## Changes made

- Localisation corrections: none. The current text required no safe local correction.
- Keys added, removed, or rewritten: none.
- Gameplay or asset files changed: none.
- This audit handoff is the only file created by this pass.

## Remaining risks and parent notes

- Both owned localisation files are currently untracked in the shared worktree. Their content is ready, but the parent must include them in the eventual integration scope.
- Exact FORM-05 allocator/admission completion remains outside this audit. If that gameplay surface changes its public keys or meanings, the affected localisation should be reconciled again.
- No runtime language rendering was requested or performed; the verdict is based on source consumer resolution, current accepted documentation, and file-format/content review.

## Final status

**READY.** The bounded Mediterranean and FORM-05 localisation surface has complete single-definition coverage, matches the accepted country and league identities, contains no prohibited adviser-visual claims or gender mismatch, and needs no localisation correction before parent integration.
