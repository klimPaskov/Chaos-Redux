# Hannibal Anti-Spoiler Audit

## Audit result

The package contains internal Hannibal design because implementation requires it. It contains no final player-facing localisation. Every early public surface is directed to use neutral wartime, ritual, cell, network, commune, island, and warlord language.

## Surface rules

| Surface | Pre-reveal rule | Audit test |
| --- | --- | --- |
| Entry event | Military breakdown only | No Hannibal, master, unifier, final portrait, or supreme command wording |
| Baseline follow-ups | Evidence, hunger, command, cells | No personal source of coordination |
| Evolution I | Ritual ideology | No global command claim |
| Evolution II | Shared methods and uncertain coordination | No name, pronoun, portrait, title, or unique leader symbol |
| Event Details | Premise and spread risk | No later country or world-end spoiler |
| Event log preview | Spoiler-safe evolution direction | Evolution III row does not exist before trigger |
| Normal decisions | Containment and network terms | No counter-Hannibal labels before reveal |
| Warlord focus tree | Alignment, manipulation, defiance | No named master before reveal |
| GUI | Network nodes and shared orders | No leader card, face, or personal title |
| Scenario | Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, Convergence | No Hannibal or Wendigo type label |
| Achievements | Early achievements visible, late achievements hidden | No visible late title before reveal |
| Portraits | Generic warlords only | Hannibal sprite never appears in public selector or default state |
| Flags | Regional Host and Commune symbols | No unified symbol before reveal |
| Super-event defaults | Empty or safe fallback | Reveal slot cannot show early text, image, or audio |
| Music and audio UI | No player-visible identity metadata | Track name does not spoil before event |
| Spreadsheet Details | Baseline premise | Evolution and terminal content confined to their proper columns and wording |

## Internal identifiers

Internal script, character, asset, achievement, and documentation identifiers may contain `hannibal` where precision is required. They must not be printed by player-facing localisation or UI before the reveal.

## High-risk implementation leaks

1. Scripted-localisation default branch returns the revealed name before a flag check.
2. Event Details evolution catalog lists Evolution III title from game start.
3. Hidden achievement title is visible in the achievement browser.
4. Scenario detail mentions the unifier or alternate branch.
5. Warlord focus search filters contain the final name.
6. Hannibal portrait is assigned to a hidden character that still appears in a country character list.
7. Super-event image getter defaults to the reveal sprite.
8. Audio documentation or station title is surfaced in game.
9. A generic warlord uses the same scars, mantle, silhouette, or emblem as Hannibal.
10. Wendigo country presence causes a pre-reveal tooltip to name the alternate form.

## Required implementation grep and UI review

Search all player-facing localisation, scripted localisation, GUI, focus, decision, achievement, scenario, event-log, super-event, and country-name files for the final identity. Review every match manually. A match is valid only when it is internal-only or guarded by the reveal state.

The completion auditor must treat any early leak as a blocking defect.
