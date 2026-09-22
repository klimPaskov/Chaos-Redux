# 075 · Interface and localisation direction

## One event-specific value to manage

The main category exposes one persistent event-specific numeric summary: **Readiness**, expressed as a percentage of the currently selected preparation objective.
Its adjacent text names the ambition and the current bottleneck.
The player can inspect actual equipment, manpower, industry, and the paid reserve through their appropriate native or event detail views.
Those stocks are not repackaged as four new currencies.

Readiness uses the weakest required component of the objective, rather than an average that lets surplus rifles conceal absent recruits or fuel.
The final implementation must explain the displayed objective and keep its requirement stable during the chosen preparation program.
An evolution's larger future ambition is announced as a change in policy.
It cannot silently make yesterday's paid soldiers disappear.

After the reveal, the same display becomes a reserve-and-replacement readiness summary only where it remains useful.
Continental certification and world victory use concise objective text and native map-based counts.
There is no additional permanent “deception,” “influence,” “aid wealth,” or “world conquest energy” meter.

## Presentation choice

The event uses ordinary decisions, targeted country selection, missions, native focus navigation, and standard event windows.
A bespoke scripted-GUI dashboard is not justified by the current decision loop.
Readiness can be formatted in the ordinary category description with an explanatory tooltip.
This package does not assume that an unverified category picture is itself an interactive progress bar.

A small static category illustration is suitable only if the final consumer remains a simple text/list category.
If implementation later introduces rich controls or a scripted panel in that same space, remove or redesign the illustration instead of layering competing systems.
No permanent focus inlay is planned.
No animated sprite is required merely to make paperwork appear active.

## Category states

| State | Main information | Visual direction |
|---|---|---|
| Protection and aid | Sponsor status, current appeal priorities, Readiness, the largest shortage | Restrained embassy or correspondence detail |
| Defensive emergency | Current threat, actual reserves that can deploy, interrupted deliveries | Existing category treatment with a clear alert state |
| Reveal committed | Opening targets and the one-time mobilization outcome | A short transition notice, not a repeatable management state |
| Continental expansion | Active fronts, replacement needs, leading continental objective | Military planning and supply emphasis |
| Global campaign | Current theater, overseas preparations, remaining independent opposition | Naval chart and transport emphasis |
| Defeat or completion | Resolved outcome and the real donor history | Closed historical record, no live purchase controls |

The visual state always follows the campaign state.
A saved game cannot show defensive aid buttons after the wars have begun.
A defeated episode cannot leave an active readiness panel that appears to promise another army.

## Focus visibility and search

The visible opening names concern protection, industrial development, training, and defense.
Later conquest and global families use matching branch visibility, focus availability, filters, and navigation conditions.
The player should not reveal a hidden branch through a search shortcut that ignores the branch gate.
Supported observer views need testing because the plan does not claim stronger secrecy than the game can implement.

The main branch anchors use the user-provided names.
Additional node names are working directions until the final localisation pass.
Tooltips communicate useful requirements and varied rewards without exposing internal flags, helper names, custody bookkeeping, or debug counters.
A disabled focus should explain the actual missing condition, such as a supplied coastal position or a funded training program.

## Writing the deception

Requests use plausible official language and a specific stated need.
The changeable threat is framed as TAN's reported concern when it is fabricated.
Narration does not establish an untrue invasion as a world fact.
Repeated requests vary their explanation without contradicting the political situation or pretending that a nonexistent Soviet Union still controls the region.

The humor comes from the mismatch between the small request and the eventual combined army.
Option text can be dry, skeptical, or ironic.
Avoid repeated jokes about the country's name in every popup, insulting Tuvan culture, and modern internet slang in official correspondence.
Political power is political effort, not a suitcase of cash.
Foreign recruits are people entering a stated service agreement, not a new natural resource deposit.

## Writing the reveal

The first reveal can identify that foreign assistance helped create the army.
It cannot say all countries funded TAN when the recorded network says otherwise.
The dominant contribution can shape a local description: equipment, training, manpower, industrial plant, or a balanced network.
The second reveal identifies an earned continent and the decision to pursue global conquest.
It does not reuse the first event's language as if the deception were still unknown.

Donor reactions use the recipient's completed contributions and the actual current war relationship.
A donor that is not at war with TAN should not be told its capital is already under Tuvan attack.
A historical country name must come from the actual campaign scope.
Only substantiated real quotations can be attributed to a real person.

## Access and legibility

Decision text, tooltips, icons, event art, and focus layouts require review at supported interface scales.
Numbers use localized formatting and unit labels.
Long donor names and translated focus labels must fit without covering a price, progress field, or connector.
Important conditions need words as well as color or a small icon.

Keyboard and ordinary mouse access must reach the core controls through the game's existing navigation.
A visual title card must not be the only source of an opening-war warning.
A player who disables music or super-event presentation still sees the strategic consequence.

## Localisation deliverables

The production pass covers the opening and repeat offers, accept/smaller/substitute/refuse options, delivery and interruption reports, industrial and reserve programs, focus names and descriptions, reveal warnings, donor reactions, conquest and integration, evolutions, continental certification, global preparation, submission, defeat, ending, achievements, event history, and catalog-facing summaries.
All are written from the finished design and current scopes.
This source specification provides direction and user-supplied anchors, not an unreviewed final copy pack.
