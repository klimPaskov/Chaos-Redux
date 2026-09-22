# Interface and state puzzles

## The focus-tree inlay

A compact event-owned inlay presents Momentum, Authority, the current imperial phase, and the selected campaign. It uses the game's normal visual language and readable text. It does not occupy the center of the tree or cover focus connections.

The two meters show current values, direction, and the most recent meaningful cause. A supply warning names a missing route or reception site. A political warning names an unresolved succession or dispute. These remain conditions, not new meters.

## Decision category

The category presents the current action family and one selected target. Target selection can show a filtered list of relevant countries or regions. Invalid targets include a short reason. The list does not pretend that every distant country is available for an immediate invasion.

Primary actions remain ordinary controls with actual hover, disabled, and click behavior. A painted image of a button is not an interactive element. The state puzzle and category artwork occupy an owned, bounded region of the interface.

## Territorial qualification

A selected formable or regional settlement displays the actual required state set. Each piece comes from validated game geometry. It can show whether the state is missing, occupied, owned, held by an eligible khanate, or satisfied by an agreement when that specific settlement allows it.

The summary must count the same set as the formation action. Occupation is not shown as permanent ownership. An optional ambition is not silently added to the mandatory set. A state lost during play changes the puzzle and the action's availability together.

A finite reviewed state manifest is the source of truth for each settlement. Regional names in this planning package are semantic design targets until the installed map is bound. Hand-drawn outlines or guessed state numbers cannot replace that work.

## Layout states

Required visual states include the opening, an active campaign, an unavailable target, a successful settlement, a cut route, a tributary in arrears, a succession, fragmentation, and a restored smaller empire. Each state must be reviewed at normal UI scale with long text, actual values, and valid hover behavior.

The reference layout should be created before implementation. The final proof must come from the real GUI inspection and rendering tools plus live-game review. A planning diagram or generated image is a reference only.

## Accessibility and feedback

Text remains readable at the normal game resolution and UI scale. Color is supplemented by labels or symbols so territorial qualification does not rely on color alone. Tooltips explain the reason for a disabled action and show the complete cost.

No player-facing element contains debug identifiers, asset-production instructions, missing-source notes, or development status. Those belong in the planning and validation files.

## Ownership and cleanup

The custom work belongs to Event 073's window, category, puzzle, or inlay. Shared interface controls are not rewritten without a separate approved integration change. When the event ends for a country, its obsolete controls disappear. Successor countries retain only the interface elements that belong to their current regional package.

The category cannot keep offering tribute collection or central appointments to a country that is no longer the imperial center. Save reload must restore the correct phase and selected target without duplicating controls.
