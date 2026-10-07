# Mines everywhere: Event 088 planning package

## Placement

Copy `088_mines_everywhere_specs/` into the repository's `docs/specs/` folder.

Copy `088_mines_everywhere_plans/` into the repository's `docs/plans/` folder.

Preserve the event-specific subfolders. This package does not contain gameplay replacements and should not be extracted as a replacement repository.

## Start here

Read the five numbered specification files in order. They contain the event design. The separate coding, asset, achievement and goal prompt files are ready implementation handoffs. The goal prompt is under 4,000 characters.

Use the companion plans for sources, limitations, current-code findings, implementation order, future subagent briefs and tests. The root manifest records the exact contents and hashes of the delivered package.

## Delivery boundary

All 42 supplied text sources and profiles were read in full before drafting. Not all referenced external documentation or visual resources were fully read. No custom subagents or HOI4 MCP routes were executed. No game implementation, live test, generated runtime art or workbook edit is claimed. The detailed source ledger explains the remaining requirements.

The design preserves global current-map coverage, a fixed 1,000-mine addition for every eligible owner-region pair, separate ownership, normal caps, existing fields, once-only application and real sweeping. No random-region or permanent-refill fallback has been substituted.
