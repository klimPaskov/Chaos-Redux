# Greenland Sale: specification index

Checkpoint: `GS-092-D1`.
Date: 2 October 2026.
Event: `092`, Greenland Sale.
Catalog classification: Minor Fire-Once, Chaos level 1, no cluster, To Be Reworked.

## Read the design in this order

All 13 design parts are present.
The baseline is a complete auction with its own no-bid and cancellation outcomes.
The four evolutions expand what can be offered without changing the funded highest-bid rule.
The main parts describe the intended game experience and its concrete contracts rather than a parser-level implementation blueprint.

| Part | Subject |
| --- | --- |
| 01 | [The first auction: entry, inspection, funded bids, the closing clock and terminal outcomes](092_greenland_sale_spec_part_01_the_first_auction.md) |
| 02 | [Purchasing power and payment: industrial opportunity cost, escrow, receipts and usable proceeds](092_greenland_sale_spec_part_02_purchasing_power_and_payment.md) |
| 03 | [Dynamic value: economic assessment, seller policy, bidder interest and material changes](092_greenland_sale_spec_part_03_dynamic_value.md) |
| 04 | [Territory and sovereignty: divided Greenland, real ownership, subjects and protected survival](092_greenland_sale_spec_part_04_territory_and_sovereignty.md) |
| 05 | [Governments at market: buyer and seller motives, war, rivals and affordable AI commitments](092_greenland_sale_spec_part_05_governments_at_market.md) |
| 06 | [Overseas Auctions: a continuing market in ordinary remote possessions](092_greenland_sale_spec_part_06_overseas_auctions.md) |
| 07 | [Colonial Markets: coherent regional lots formed from current ownership and geography](092_greenland_sale_spec_part_07_colonial_markets.md) |
| 08 | [Strategic Auctions: ports, resources, staging positions, chokepoints and military value](092_greenland_sale_spec_part_08_strategic_auctions.md) |
| 09 | [Everything Has a Price: homeland disposal, domestic cost and receipt-backed reconstruction](092_greenland_sale_spec_part_09_everything_has_a_price.md) |
| 10 | [The living market: evolution timing, permission combinations, pacing and campaign continuity](092_greenland_sale_spec_part_10_the_living_market.md) |
| 11 | [Connections and consequences: other events, persistent state systems and direct Chaos](092_greenland_sale_spec_part_11_connections_and_consequences.md) |
| 12 | [Decisions and presentation: player actions, visible commitments, missions and localisation direction](092_greenland_sale_spec_part_12_decisions_and_presentation.md) |
| 13 | [Mastery and visual identity: four achievements and a bounded production asset plan](092_greenland_sale_spec_part_13_mastery_and_visual_identity.md) |

## Specialist production prompts

[Goal prompt](092_greenland_sale_goal_prompt.md) provides the compact implementation entry prompt.
[Coding prompt](092_greenland_sale_coding_prompt.md) owns implementation sequencing, compatibility, source gates and proof requirements.
[Decision and mission prompt](092_greenland_sale_decision_mission_prompt.md) owns player actions, timing, feedback and native presentation.
[Asset prompt](092_greenland_sale_asset_prompt.md) owns the production inventory, source references and consumer verification.
[Achievement prompt](092_greenland_sale_achievement_prompt.md) owns four receipt-backed mastery conditions and canonical icon production.

These prompts are handoffs, not claims that their work has already run.
The goal prompt remains bounded to 4,000 characters including its final newline.

## Authority and proposals

The preserved user brief controls the identity, live-owner sale, worldwide eligibility, dynamic value, ten-day high-bid rule, four thresholds and continuing bounded market.
The 15-day preparation period, industrial reserve, opening-price ratios, pacing, reconstruction mission, direct Chaos milestones and achievements are proposed expansions.
They are specified consistently but have not been separately approved by the user or calibrated in the game.
A different economic implementation must preserve paid principal, equal seller value, useful proceeds, actual-paid refunds and a real opportunity cost.
Do not silently replace the selected reserve with political power or free credit.

## Package placement

This package lives in `docs/specs/092_greenland_sale_specs/`, with working evidence in `docs/plans/092_greenland_sale_plans/`.
The supplied-source ZIP was removed at the user's request in commit `6a2ebc838`.
Its reading ledger and source hashes remain historical receipts, and no current task should require or restore that archive.
Open `docs/plans/092_greenland_sale_plans/092_greenland_sale_plans_index.md` for the reading ledger, coverage, execution map, role handoffs, reviews and validation status.

## Completion boundary

This is the 2 October 2026 parent-authored specification draft and production handoff.
The following reading and execution statements describe that planning pass, rather than current tool availability or implementation status.
All 46 supplied text files were fully read before drafting, including all 20 role definitions.
Some required external references remain unread or partly read, including the current repository MTTH file and installed-game evidence.
The source-reading protocol was not found in the searched locations.
No actual subagent, independent improvement-loop audit, HOI4 MCP probability audit, native transaction prototype, final asset production, final localisation or game test was performed.
Abstract design checks and document integrity checks have narrower scopes recorded in the validation report.
The status must not be promoted to implementation complete on the strength of these documents alone.
