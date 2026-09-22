# Event 072: Ireland Reclaims the North

[Read the campaign specification](specs/core/072_campaign.md) · [Browse every file](INDEX.md) · [Open the Codex goal prompt](prompts/072_ireland_reclaims_north_goal_prompt.md)

A real northern reclamation war earns the new Irish campaign only after a successful limited settlement.
Failure permanently leaves the previous focus tree in place.
The later design includes national integration, Gaelic institutions, a substantive Gaelic Empire, a sovereign-member Celtic federation, a primary Atlantic strategy, and full army, navy and air development.

## Package structure

The archive has one parent folder, `072_ireland_reclaims_north_specs/`, with thematic source subfolders.
The specification belongs in `docs/specs/072_ireland_reclaims_north_specs/` in the repository.
Implementation plans and review handoffs belong separately in `docs/plans/072_ireland_reclaims_north_plans/`.
Their bundled copy is under `handoff/072_ireland_reclaims_north_plans/`.

| Directory | Content |
| --- | --- |
| specs/core/ | Campaign, catalog contract, reclamation war and victory/failure rules |
| specs/focus_tree/ | Architecture and 65 focus groups across eight lanes |
| specs/military/ | Real opening-force tables, equipment accounting and permanent-army transition |
| specs/mechanics/ | Evolutions, two public values, three spirit families, territorial routes and Celtic countries |
| specs/decisions/ | 42 actions with costs, gates, timing, effects and interruption rules |
| specs/ai/ | Opening behavior, route strategies and probability audit requirements |
| specs/presentation/ | Events, writing, exact-state GUI, 155 asset-planning rows, ten achievements and two super-event briefs |
| specs/integration/ | Runtime contracts, Chaos impact, cross-event relationships and technology compatibility |
| diagrams/ | Three editable Mermaid route and lifecycle diagrams |
| prompts/ | Seven implementation, asset, decision, focus, achievement, super-event and goal prompts |
| research/ | Research boundaries and hashed reading ledger for all 42 supplied text sources |
| original/ | The user's event brief |
| handoff/ | Build sequence, ownership, 20 role assignments, 60 validation fixtures and 12 probability scenarios |

The 65 focus groups are not a fixed final node count.
The implementation agent chooses the actual node layout and splits groups where each focus has a meaningful purpose.
The asset inventory likewise contains planned requirements, not generated files or a claim of completed artwork.

## Put the files in the repository

From the extracted folder, run the optional local installer with the repository path:

```bash
python3 install_spec_package.py /path/to/Chaos-Redux
```

The installer copies only this documentation package into the two locations above.
It does not edit game scripts, run the game, contact the network, commit changes, or alter catalog workbooks.
It refuses conflicting existing files unless `--overwrite` is explicitly supplied.
Use `--dry-run` to print the planned changes first.
Manual copying is also possible by placing the source folder in docs/specs and its bundled plan folder in docs/plans.

Then use [the goal prompt](prompts/072_ireland_reclaims_north_goal_prompt.md) with the installed specification.
The goal prompt is within the required 3,500 to 4,000 character range.
The longer [coding prompt](prompts/072_ireland_reclaims_north_coding_prompt.md) supplies the full implementation obligations.

## Main design decisions

The opening packages have cumulative ceilings of five, ten, fifteen and twenty divisions by tier, with separately accounted equipment and personnel reserves.
These numbers are initial tuning, not playtested balance.
Northern victory requires all objective land provinces and five continuous days of control.
The initial 180-day attempt can receive one paid 90-day extension.
Success requires the actual peace and ownership postconditions, not a popup claiming victory.

The imperial foundation is the approved Irish and Scottish homeland set under Irish ownership and control, with separate Scottish core integration.
The federation is a binding bloc whose members retain their country tags and sovereignty.
Atlantic access is a treaty relationship unless sovereignty is explicitly and lawfully transferred.
Man and Cornwall remain optional only where the installed setup represents them appropriately.

All baseline routes remain complete with Evolutions disabled.
Only Northern Settlement and External Strain are public custom numerical values.
The national spirit budget is three owned families, including temporary variants.

## Read record and limits

All 42 supplied text files were fully read, including all 20 provided subagent profiles.
The reading ledger verifies contiguous coverage across 102 recorded packets and stores file hashes.
The earlier progress-message counts of 43 texts and 21 profiles were incorrect and are superseded by this inventory.
The existing Event 072 script and localisation, generic peace eligibility, MTTH skill and listed registry guidance were also inspected as documented in the research file.

Not all external sources referenced by the skills were read in full.
Installed vanilla documentation, the complete offline wiki set, installed mod identities, final asset references, music catalog and live tool artifacts remain partly or wholly uninspected.
No independent subagent was launched here.
The profiles informed parent review and the implementation handoffs, which do not masquerade as completed independent audits.
No game scripts, final localisation, generated art, licensed audio or live gameplay tests are included.

The main engineering gate is the limited settlement against faction-leading Britain while preserving unrelated wars and territory.
It must be proven in the installed game before the larger implementation can be called complete.
Exact state sets, current engine identifiers, focus-progress handling and resource-capacity representations also require verification.
See [the full blocker record](handoff/072_ireland_reclaims_north_plans/validation/072_parent_review_and_blockers.md).

## Package verification

From the original extracted archive folder, run `python3 validate_package.py` to check the archive's structural contracts and SHA-256 manifest.
Those checks cover files, internal links, focus-group and action coverage, asset inventory, source-reading records, cost-type limits and prompt length.
They do not execute HOI4 or establish live balance.
The [verification report](handoff/072_ireland_reclaims_north_plans/validation/072_package_verification.md) records that distinction.
