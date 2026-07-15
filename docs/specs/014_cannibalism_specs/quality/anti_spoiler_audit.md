# Hannibal Anti-Spoiler Audit

Status date: 2026-07-13

## Public boundary

`cannibalism_reveal_complete` is the atomic public boundary. Ordinary and Wendigo unification both set it before public country identity, leader, portrait, focus, decision, report, news, super-event, GUI, terminal-row, or audio-facing operations.

Before that flag, every visible surface uses only current evidence: supply failure, missing soldiers, ritual cells, shared symbols, courier routes, communes, islands, warlords, coordinated operations, convergence, and uncertain command. It does not discuss a hidden identity, later revelation, future leader, final portrait, or terminal route.

## Surface results

| Surface | Current result |
| --- | --- |
| Entry and baseline events | Military breakdown only. No exact or indirect identity claim |
| Evolution I and II | Ritual and network language remains impersonal and uncertain |
| Event Details | Baseline premise before reveal. Named command only after reveal |
| Terminal Event Details | Scenario IDs 6 and 7 are absent from the visible list before reveal |
| Warlord focus tree | 68 of 68 title/description/tooltip sets contain no Hannibal, Lecter, or Wendigo leak |
| Decisions and missions | Pre-reveal actions use network and convergence language |
| Scripted GUI | Early and network windows exclude revealed portrait and name selectors |
| Achievement tracker | Five baseline rows open at system start. Late rows open only at exploitation, Island Host, Evolution II, convergence, reveal, merge, or aftermath |
| Scenario `SCN-010` | All five types remain neutral and stage the reveal in-world |
| Portraits and flags | 56 generic warlord portraits and pre-reveal flags do not reproduce the revealed leader identity |
| Reports and news | Pre-reveal assignments use neutral images. Reveal and transformed images are gated |
| Super-events and audio | All four Event 014 emitters require reveal. No default Event 014 slot surfaces identity early |

## Internal identifiers

Internal script, character, asset, achievement, audio, and documentation identifiers may contain `hannibal` where precision is required. They must not be printed through a player-facing lookup before reveal. Historical handoffs and source manifests may also name the character because they are not game UI.

## Staged achievement boundary

The Career Profile achievement schema provides static hiding only. Five baseline achievements remain visible and thirteen late-route achievements remain statically hidden there. The implemented read-only tracker is the verified stage-aware presentation surface. Its 18 entries call the real achievement completion triggers and cannot grant, disqualify, or modify gameplay.

## Visual and cultural boundary

- No actor or celebrity likeness.
- No actor likeness or borrowed living ceremonial, sacred, tribal, or authenticity framing.
- No living Indigenous ceremonial clothing, regalia, sacred motif, ritual object, tribal shorthand, language, name, or authenticity claim.
- The internal Wendigo identifier does not license borrowed folklore presentation.
- Generated victims are fictional adults. Real atrocity photography and identifiable victims are excluded.

## Audit disposition

The known source/route, indirect-foreshadowing, dynamic-value, implementation-terminology, punctuation, and staged-achievement visibility defects were remediated. The final dedicated localisation re-audit is recorded in package status. This document does not claim an in-game runtime review.
