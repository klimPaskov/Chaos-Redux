# Event 090: Deal with the Devil

**Status: specification reconciled with the user brief (10 Oct 2026 spec audit); not implemented.**
The legacy Suicide Craft script `events/090_kamikaze.txt` is still live and is replaced at implementation.
No catalog edit, gameplay script, localisation, model, image or sound has been produced for this design.

A mysterious stranger solves a nation's worst problem, asks for a small, reasonable concession, and comes back.
Five accepted bargains hand the country to Mephistopheles without a shot fired; refusing him every time forces him into the open; anything in between becomes a civil war fought against the country's own rescued institutions.
The Mephistophelean Dominion that emerges can bargain with the rest of the world, and with enough signatures and Chaos above 1000 it can bind the world's governments in the Last Signature.

## Authority

The [original user brief](../../plans/090_deal_with_the_devil_plans/sources/090_original_user_brief.txt) is authoritative; its evolution sections are mirrored verbatim in the [source evolution requirements](matrices/090_source_evolution_requirements.md).
The parts develop the brief into an implementable design.
Design choices the parts add beyond the brief were proposed in the 2 Oct 2026 draft (see the plans folder's [source and decision register](../../plans/090_deal_with_the_devil_plans/sources/2026-10-02_source_and_decision_register.md)) or set by the 10 Oct 2026 spec audit under the user's planning-package brief, as the revision log records.
Numbers are starting tuning for balance review, collected in the [tuning register](matrices/090_tuning_register.md).

## Specification parts

Read the parts in order; they are the only copy of the design.

| Part | Content |
| --- | --- |
| 01 | [Identity, secrecy, and the first meeting](specs/090_spec_part_01_identity_and_secrecy.md) |
| 02 | [Courtship, the five main deals, retaliation, and rare variants](specs/090_spec_part_02_courtship_and_main_deals.md) |
| 03 | [Military, economic, and political offers](specs/090_spec_part_03_material_and_political_offers.md) |
| 04 | [Knowledge, medicine, diplomacy, and the ruler](specs/090_spec_part_04_science_medicine_diplomacy_and_leaders.md) |
| 05 | [Discovery, safeguards, the changing face, and breaking away](specs/090_spec_part_05_discovery_portraits_and_breakaway.md) |
| 06 | [Manifestation and the three Dominion origins](specs/090_spec_part_06_manifestation_and_three_origins.md) |
| 07 | [The shared tree and the question of rule](specs/090_spec_part_07_shared_focus_tree_and_liberation.md) |
| 08 | [Armies, industry, and infernal research](specs/090_spec_part_08_armies_industry_and_research.md) |
| 09 | [Foreign bargains, clients, and the Infernal Compact](specs/090_spec_part_09_foreign_bargains_and_clients.md) |
| 10 | [Evolutions, the Last Signature, defeat, and system connections](specs/090_spec_part_10_evolutions_world_end_and_connections.md) |
| 11 | [AI choices, balance, and consequences](specs/090_spec_part_11_ai_balance_and_consequences.md) |
| 12 | [Presentation, assets, and achievements](specs/090_spec_part_12_presentation_assets_and_achievements.md) |

## Matrices

[Route map](matrices/090_route_transition_map.md), [offer index](matrices/090_offer_index.md), [decision and focus map](matrices/090_decision_and_focus_map.md), [ownership map](matrices/090_cross_event_ownership_map.md), [tuning register](matrices/090_tuning_register.md), [Chaos impact map](matrices/090_chaos_impact_map.md), [requirement coverage](matrices/090_requirement_coverage.md), [source evolution requirements](matrices/090_source_evolution_requirements.md), [asset manifest](matrices/090_asset_manifest.json), and [54 acceptance scenarios](matrices/090_acceptance_scenarios.md).

## Prompts

The [goal prompt](prompts/090_goal_prompt.md) stays under 4,000 characters.
The [master prompt](prompts/090_master_implementation_prompt.md), [asset prompt](prompts/090_asset_production_prompt.md) and [audit prompt](prompts/090_audit_prompt.md) cover implementation; the [continuation prompt](prompts/090_continuation_prompt.md) resumes the remaining design gates.

## Open gates

Gate definitions live in the plans folder's [parent review](../../plans/090_deal_with_the_devil_plans/review/2026-10-02_parent_review.md).
G01 (reconciliation with the brief) is closed by the 10 Oct 2026 audit.
Still open: G02 one-state separate country (open question 1), G03 reusable portrait overlays, G04 formation transfer, G05 mixed human/demon audio, G06 current specialist, medical, famine and condemnation interfaces, G07 terminal arbitration and military measure, G08 unit economics, G09 asset production, G10 live campaign acceptance.

## Open questions

1. **One-state hosts** (touches the brief's host pool of “every valid player-controlled country”).
A one-state country cannot lose territory to a separate Dominion and remain playable.
Recommendation: add a viability condition so a host needs at least one connected foothold region it can lose while keeping a capital; one-state players are not selected until a supported method exists.
Alternatives: an approved same-tag internal siege for one-state hosts, or engine evidence for a separate-country method that steals no foreign territory.
Disposition: unresolved; needs the user's decision.
2. **Post-completion reversal of the Last Signature** belongs to the shared world-end framework, not to Event 090.
Disposition: unresolved; decide when that framework's owner contract is read (G07).

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.
Disposition of the changes below: promoted into an accepted spec.

- Deleted `090_deal_with_the_devil_full_spec.md` (194 KB), a second full copy of the twelve parts; the parts are now the only copy, and `package_metadata/START_HERE.md` points to this README.
- Restored the brief's four-visit clean courtship (better second offer, tailored third, less generous final visit with a shorter deadline), replacing the draft's five-invitation rule (draft decision D01).
- Restored the brief's retaliation and punitive offers after a refusal that follows one to three acceptances; the draft had made those refusals consequence-free.
- Added four safeguards (Independent Records, Loyal Command, Protected Successor, Outside Witness) as the single output of the inquiry, read by loopholes, seizures, revolt footprints, Possession Moves and liberation; settlement became one event per institution.
- Developed Evolutions I and II, which the draft had not specified; personal deals now advance possession more directly as the brief asks, without counting twice.
- Added the brief's missing rare variants, the enclave's opening defense and host emergency tools, the final attempt to move after defeat, and a defeat super-event.
- Unified the three origin identities as cosmetic variants of one Mephistophelean Dominion package and kept the brief's origin branch names.
- Connected offers to current systems: famine reserves and relief through the famine owner, condemnation evasion and exposure through the envoy, camps for coercive rule, and a world-threat source at Last Signature ratification.
- Replaced the 90-row heading inventory in the requirement coverage with a semantic reconciliation against the brief, which closes G01 for the brief.
- Updated the route, decision, tuning, Chaos and ownership matrices, the asset manifest (Dominion identities, defeat image), and scenarios A05, A06 and A46–A54.
- Rewrote the prompts for the current Claude workflow (`CLAUDE.md`, `.claude/skills` links, subagents through `chaos-redux-subagents`, user-owned live testing) and removed Codex-specific and project-source-protocol instructions.
