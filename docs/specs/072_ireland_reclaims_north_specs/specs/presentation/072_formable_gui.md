# Decision presentation and exact-state puzzles

## Human-facing layout

Use HOI4-native decision-category presentation with a compact status area and an exact-state puzzle for territorial formation and integration.
The top line contains the current phase and, after victory, Northern Settlement and External Strain.
A second compact line shows the current territorial or charter requirement.
The map canvas sits inside the actual category description width and never covers the decision list.
One to three missions and the current three to five relevant actions follow.
Do not add a separate full-screen management interface for the same decisions.

The state puzzle is informational.
A state piece is not a button and must not display a fake click action.
The actual formation or integration decision remains the action surface.
AI uses its eligibility helper without opening the GUI.
The reference preview required during implementation must resemble the game's decision interface and be checked against an existing native category.
This package supplies the logical layout and state contracts, not a rendered in-game mockup.

## The shared registry

The reviewed active geometry source is docs/formables/state_registry/generated/state_geometry_registry.json.
Use the finite candidate set and a consumer declaration conforming to the repository's current schema.
Geometry is never generated with an image model, drawn by hand, or copied from a different map revision.
Do not duplicate state masks or row runs into an independent Event 072 geometry registry.

The current template workflow records that the prior registry builder and consumer compiler are archived and are not routine supported commands.
A new consumer or changed map requires deliberate restoration and review of that producer chain or an approved replacement.
The runtime generator may process only consumers whose manifests are complete with final DDS evidence.
A design declaration with unresolved state IDs remains draft and must not be marked runtime complete.

## State meaning by category

The reclamation display uses the real northern state outline and shows full-objective control and the five-day hold requirement.
Its hover distinguishes current ownership from control and does not treat a single captured city as the whole state.
The domestic integration puzzle covers the exact relevant Irish state set and northern legal integration.

The imperial puzzle shows IRELAND and SCOTLAND as required, with separate optional later candidates revealed only when their route becomes relevant.
Green qualification means Irish ownership and control under the same helper used by the formation decision.
A Scottish subject or ally does not qualify that state for imperial formation.
The federal puzzle uses a different policy: Irish states must qualify through Ireland, Scottish states through Scotland, and Welsh states through Wales.
It also shows each required member's charter status as factual icons or text.
The map does not imply Irish annexation of those members.

The Atlantic puzzle covers only its approved finite candidate states.
Access status, treaty validity, and sovereign ownership are displayed distinctly.
A qualifying access piece does not imply that it is an Irish core.
The category's action tooltip states which rule is being tested for the selected project.

## State-piece and hover contract

Each required state has one exact geometry entry, its own compact hover region, and a static unresolved and qualifying sprite family.
Unresolved pieces are grey with a hatch or texture cue.
Qualifying pieces are green with a check or inner outline cue.
Both retain the same geometry and outer border.
Color alone cannot carry the state meaning.
Pieces, outlines, and status cues remain static sprites.

Every hover reports the current state name, owner, controller, relevant territorial result, and core result where the decision uses it.
Missing owners and controllers need an explicit valid fallback.
The hover bounds follow the transparent state-piece bounds and cannot be one oversized rectangle for the full map.
Keep the common projection and recorded seam rule so adjacent states fit together.

One policy helper supplies the piece status, hover conclusion, qualifying count, summary, decision availability, and AI eligibility.
A live bounded trigger count is preferred.
Do not create a daily or weekly world scan to maintain GUI values.
A presentation-only dirty value is allowed only where the verified engine contract requires it and all relevant update callers are proven.
It never substitutes for the live formation condition.
Do not feed saved event targets into scripted GUI where the offline guide warns that they break the context.

## Attachment crosswalk

| Category | Policy | Consumer status in this package | Required implementation evidence |
| --- | --- | --- | --- |
| Reclamation | Northern objective and current hold | Draft design | Installed state geometry, actual linked GUI and mission result |
| United Ireland | Irish legal integration | Draft design | Exact domestic set and northern core policy |
| Gaelic Empire | Irish ownership and control of empire foundation | Draft design | Full required set, optional-state reveal, formation helper agreement |
| Celtic Compact | Each essential member owns and controls its own set | Draft design | Member-specific scope, charters, summary agreement |
| Atlantic Policy | Treaty-specific access or administration qualification | Draft design | Accepted-access semantics, holder changes and target visibility |
| National Development | Out of territorial formation family | Explicitly outside attachment scope | No formation or territorial integration decisions in this category |

Record the exact generated scripted-GUI identifier and window from the actual generator output.
Do not guess them from a naming formula.
Each in-scope category metadata block must link its generated block with decision_category context.
A correct-looking isolated window is insufficient if the category is not attached.
All five in-scope categories must be present in the category audit.

## Visual acceptance

Before and after each UI tranche, use the installed read-only GUI inspection and rendering tools for matching states and resolutions.
Render unresolved, partly qualifying, fully qualifying, optional-hidden, long-text, missing-localisation, absent-target, imperial, federal, and Atlantic-access cases.
Inspect hierarchy, category attachment, state bounds, hover regions, sprite references, and clipping.
Use corresponding map inspect and map render evidence for the active state and province set.

Convert each processed state PNG using the repository converter and verify its final DDS header, dimensions, alpha, byte length, and pixel-equal decoded round trip.
The current workflow requires one-level uncompressed 32-bit BGRA output.
The exact converter contract remains authoritative.
No map or GUI inspection artifact independently proves DDS correctness.
Keep artifacts and failed checks in the implementation evidence folder.
No MCP rendering, installed geometry extraction, or runtime DDS generation was performed for this planning package.
