# Fallout Ash-week capital and character event proof

Status: dormant additive implementation, not release-floor credit.

## Scope

This tranche completes the missing event blocks for the accepted Ash-week orientation contract. It defines the capital condition root, hidden AI root, human result, and hidden AI result at `chaosx.fallout.66` through `.69`. It also defines the first character or institution root, hidden AI root, human result, and hidden AI result at `chaosx.fallout.78` through `.81`.

The blocks remain in `events/fallout_world_end_events.txt` under the Fallout namespace. They do not set either scheduler activation flag, create a caller, materialize a successor, or change the manual scenario.

## Capital condition

Event `66` accepts three authenticated branches:

- seal and heat the civic core
- disperse stores and offices across surviving districts
- evacuate the poisoned core into the prepared receiving state

Every option repeats the typed availability trigger at click time and writes the issued event token before calling the shared branch chooser. The branch chooser applies the accepted cost table, freezes the branch, sets the three-day result delay, and uses the shared score calculation for both human and hidden AI modes.

Event `67` is hidden AI and calls the same deterministic branch chooser. Event `68` presents nine manually authored descriptions selected by branch and result band. Its immediate resolver calls `fallout_orientation_resolve_capital_condition`, which authenticates the issued token and applies the accepted state mutation, balanced migration, repair or damage, and Deaths receipt. Event `69` is the hidden AI result companion.

The human root and result use the dedicated `GFX_report_event_fallout_capital_condition` sprite. The root text exposes the frozen grade, phase, exposure, shelter, recovery, adaptation, reclamation, supply access, infrastructure-backed population, and regional weather description.

## Character or institution

Event `78` requires the current curated candidate registry and exposes three distinct branches:

- relief and administration
- security and extraction
- regional institution

The branch trigger hides any candidate whose exact resource cost or installation surface is unavailable. Event `79` uses the same branch score and affordability logic for hidden AI. Event `80` resolves through a scripted localization selector that reads the durable branch and outcome receipt. Nine concrete result paragraphs cover installation, limited mandate, refusal, contested security, rupture, institutional compact, and institutional collapse. Event `81` resolves the same transaction without a player window.

The root and result use the dedicated `GFX_report_event_fallout_character_institution` sprite. The result helper preserves the exact installed candidate or institution, relationship memory, liability modifier, and Deaths receipt before the existing closure sequence continues.

## Static checks

- event ids `66` through `69` and `78` through `81` are unique in the dedicated event file
- all eight blocks use the Fallout orientation component, mode, generation, and event-token gates already owned by the shared transaction layer
- capital result descriptions cover three branches and three score outcomes
- character result text is selected from nine branch and outcome combinations through `GetFalloutOrientationCharacterResultText`
- all visible keys and option tooltips are present in the BOM-encoded orientation localization files
- the dedicated capital and character sprites already exist in the Fallout asset manifest and GFX handoff
- no zombie asset, id, audio, sprite, or path is reused

## Remaining gates

The orientation package remains dormant. It still lacks a proven host-authoritative successor caller, complete nine-region and twelve-archetype manual coverage, a final candidate install surface for every selected country, event-log and event-detail rows, workbook alignment for these new keys, and a completion audit. The read-only event inspector remains blocked by its fixed helper projection ceiling. HOI4 was not launched.
