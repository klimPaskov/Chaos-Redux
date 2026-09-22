# 11. Decision-category influence board

## Primary view

Use a compact native scripted GUI anchored in the Event 79 decision category. The board's hierarchy is target first, competition second, actions third. It should look like an HOI4 decision system with native flags, text, progress bars, and buttons. Text and values must not be baked into a background texture.

The initial arrangement is a target header, a two-row contest summary, a narrow political-alignment strip, and the six action families beneath it. A single-target baseline does not need a target grid. Under The Great Game, a compact selector lists the active target countries and their leaders. Selecting a target changes the player's view only.

| Region | Always-visible information | Interaction |
| --- | --- | --- |
| Target header | Target flag, localized country name, actual ruling ideology, current evolution stage | Open target country view or select another active race |
| Player row | Player flag, exact Influence, progress bar to 100, pending completion indicator | Detailed seed and gain breakdown |
| Rival row | Leading rival flag, name, exact Influence, progress bar | Expand full rankings and select an interference target |
| Political strip | Pledged ideology support and target ruling alignment using native values | Expand institutions and political history |
| Campaign area | Five positive families plus interference, real costs, time, slot availability | Choose subtype, confirm target and payment |
| Active work area | Up to three campaign summaries across the player's targets | Inspect receipts, progress, cancellation terms |

Influence is the only new headline meter. Native ideology popularity is shown as a political fact. Institutions appear as short sponsor-and-expiry statuses in the expanded view. Economic project progress is a work indicator belonging to that project, not another national power meter.

## Expanded competition view

Rank all registered participants by current authoritative Influence, with tied scores shown as tied. Sorting must not establish a hidden gameplay winner. The expanded row can show active or suspended status, pledged ideology of an ongoing campaign, recent delivered assistance, and whether the participant is inside its inactivity grace period.

Display the leading rival relative to the local player. If the player leads, the rival row shows the strongest other participant. If no rival is registered, show an empty-rival state. A withdrawn or suspended participant remains discoverable without being mistaken for an active paid campaign.

Interference selection requires a specific rival row. The confirmation dialog repeats both target country and selected rival. It also shows the remaining rolling loss budget. Clicking a flag in another target cannot change a saved operation.

## Payment and delivery display

Show political, command, experience, and equipment quantities with their correct native text icons where available. At most three inline quantities appear on the action row. A fourth payment component belongs in the expanded breakdown. Display factory commitments as reserved capacity and funded days, not as an ordinary one-time political cost.

For equipment aid, show both the donor debit and the recipient delivery quantity. A supported administrative discount may reduce political power. It cannot make a 500-weapon donation debit 250 and create 500 at the target. For investment, identify the state, building, reserved factories, elapsed funded work, paused work, and the output that will appear on completion.

The cancellation panel distinguishes already spent service costs, escrowed material, funded construction credit, and released future capacity. Never summarize all of those as one generic refund percentage.

## UI states

Provide designed states for an active race, an uncommitted player, an exhausted action slot, insufficient resources, political recipient unavailable, direct-war suspension, a paused investment, a full rival-loss budget, an imminent completion, target invalidation, and completed takeover. The winner announcement cannot leave clickable stale campaign buttons behind it.

A newly opened target should be selected only if the player has not deliberately pinned another active target. When the selected target closes, move to the next active target and retain the closed result in the event log. Do not move the view when an unrelated target's five-day work installment runs.

## Sizing and accessibility

Plan the compact board around an approximately 500-pixel usable category width, with the exact geometry fitted to the actual owning interface. The expanded panel should remain usable at 1366×768 and 1920×1080 at normal scale. Test 1280×720 as a compact stress case and 2560×1440 for text and asset scaling.

Use flags and text together for participant identity. Use percentage or exact-value text with each bar, so color is not the only way to understand a lead. Allow wrapping or controlled ellipsis for long country names while the tooltip exposes the full name. Avoid narrow click targets and overlapping hover regions.

## Implementation and visual proof

Before native GUI implementation, the interface worker needs a reviewed reference image showing this category in an actual HOI4-style frame. This planning package provides the layout contract and art directions, not an approved rendered reference or an in-game screenshot.

Inspect the exact owner window and native consumer with `hoi4.gui_inspect`, then use the available GUI renderer and comparison tools on baseline, Great Game, paused investment, long names, and completed-race states. Record exact viewport and scale. Inspect hit regions and text overflow in addition to the visual image.

The GUI worker owns only the Event 79 category board and its event-owned files. Shared Event Log and settings windows remain with the parent integration owner. GUI art can decorate the board, but every live score, tooltip, selection, and payment remains native.
