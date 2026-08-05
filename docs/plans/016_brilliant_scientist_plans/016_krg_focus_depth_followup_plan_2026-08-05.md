# Event 016 Kruger State focus-depth follow-up plan

Date: 2026-08-05

Owner: `/root/event16_focus_audit`

Status: reviewed and not promoted in the 2026-08-05 audit tranche; no new focus IDs or broad focus-tree edits are included.

## Purpose

The implemented Kruger State tree has 100 authored focuses and covers every named route, but the branch-family counts are uneven against the approximate architecture targets in `docs/specs/016_brilliant_scientist_specs/matrices/016_focus_tree_architecture.md:95-109`.

The current implementation allocates five focuses to diplomacy and former-host settlement (`KRG_a_state_without_friends` through `KRG_build_the_submission_network`, 089-093), four focuses to expansion and integration (`KRG_secure_the_laboratory_corridors` through `KRG_the_continental_laboratory_network`, 094-097), and three focuses to Evolution IV and terminal commitments (`KRG_evolution_four_sovereign_science`, `KRG_commit_to_the_laboratory_world`, and `KRG_commit_to_the_strategic_singularity`, 098-100).

The architecture document explicitly records these counts as the 100-focus layout and states that decision categories carry many route contracts, so this is not a parser omission or an immediate broken-route finding. It is a deferred depth pass if the parent elects to enforce the approximate branch targets of ten to fourteen diplomacy focuses, ten to fourteen expansion focuses, and ten to sixteen world-conquest/terminal focuses.

## Evidence and current behavior

- Focus source: `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` contains 100 unique focus IDs, 108 connectors, and no KRG layout crossings, intersections, long connectors, or same-row spacing diagnostics in the parent `hoi4.focus_inspect` result.
- Diplomacy and former-host settlement are represented by `KRG_a_state_without_friends`, `KRG_found_the_foreign_intelligence_bureau`, `KRG_settle_accounts_with_the_former_host`, `KRG_open_the_scientific_commonwealth`, and `KRG_build_the_submission_network` (089-093).
- Expansion and integration are represented by `KRG_secure_the_laboratory_corridors`, `KRG_recover_the_stolen_facilities`, `KRG_integrate_by_project`, and `KRG_the_continental_laboratory_network` (094-097).
- Evolution IV and terminal commitments are represented by `KRG_evolution_four_sovereign_science`, `KRG_commit_to_the_laboratory_world`, and `KRG_commit_to_the_strategic_singularity` (098-100), with an explicit terminal mutex and opposite-terminal cancellation helpers.
- The ten Event 016 decision categories and their scripted consumers already supply recurring foreign-operation, settlement, facility, integration, administration, and terminal actions. Their existence reduces urgency but does not make the focus surface as deep as the approximate branch targets.
- The current improvement-loop addendum (`docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_improvement_loop_addendum.md:353-363`) predates implementation and recommends no new branch until implementation proves a missing route. This plan records the implementation evidence as a queued follow-up rather than silently changing that disposition.

## Proposed future tranche

The main agent may implement additional shared or route-gated focuses only after deciding that the approximate branch targets are binding for the final package. New nodes should deepen existing decisions and consumers, not create a parallel tree or a new country identity.

### Diplomacy and intelligence depth

Add a small set of route-aware focuses around recognition, patronage, scientific recruitment, intelligence pressure, and the choice between a commonwealth and a submission network.

Potential focus roles are an evidence-based recognition protocol, a foreign patron compact, a scientist-recruitment exchange, an intelligence penetration charter, and a public-versus-coercive diplomatic doctrine lock.

Each role must consume or unlock an existing Event 016 decision, mission, scripted effect, or event target, and must have a distinct route-aware AI factor rather than a generic additive reward.

Do not add a recognition super-event or duplicate the already rejected R1 surface from the improvement-loop addendum.

### Expansion and integration depth

Add focuses between host settlement and the continental network for claims or war-goal posture, facility recovery, resource corridors, protectorate or subject administration, and postwar compliance.

Each role must preserve the existing one-target-at-a-time expansion brake, supply and administration checks, overextension cleanup, and route-specific integration consumers.

No direct arbitrary cores, global claims, free war goals, or instant annexation effects should be introduced merely to fill the count.

### World conquest and terminal depth

If the final target requires a larger terminal family, add shared conquest-administration focuses before Evolution IV and commitment-specific preparation focuses after Evolution IV.

Potential roles are global command doctrine, subject-network administration, opposition suppression, terminal disarmament verification, singularity component security, and final counterplay safeguards.

Laboratory World must continue to require overwhelming control, integration, administration, submission, chaos threshold, and no major opposition. Strategic Singularity must continue to require its multi-year component race and remain vulnerable to raids, denial, disarmament, or premature failure.

Do not make either terminal available from a short focus rush, and do not create a third terminal ending.

## Implementation boundaries

- This plan does not assign new IDs, coordinates, icons, localisation keys, decisions, formable chains, country tags, or reusable custom-technology APIs.
- Reuse existing focus-owned flags and scripted consumers wherever possible.
- Keep the existing AND-style convergence and explicit terminal mutex.
- Keep hidden `available` gates only where the route cannot be made legible without a larger layout decision; any new node should prefer a visible prerequisite connector when that improves player comprehension.
- Preserve the three visible lifecycle spirit slots and the bounded project-force rebuild contract.
- Preserve the biological branch as incomplete until its native stockpile/debit callback is available; no fallback delivery mechanic is authorized.

## Acceptance and validation for a future implementation

1. Update the Event 016 focus architecture and relevant specification surfaces before adding nodes, or record an explicit parent disposition that the approximate branch targets remain non-binding.
2. Use `hoi4.focus_inspect`, `hoi4.focus_render`, and the focus lint surface after each tranche, with zero new crossings, intersections, unresolved references, or unexplained blocking diagnostics.
3. Cross-check every new title, description, effect tooltip, icon, normal/shine sprite, and DDS texture.
4. Add or update route-specific AI plans and verify that plan handoffs reach diplomacy, expansion, Evolution IV, and both terminal plans under charter, rebellion, enclave, takeover, project, disabled-Evolution, and interrupted-transfer scenarios.
5. Re-run the focus flag consumer ledger and decision/mission audit so every new unlock has an executable reader and every decision has a visible and available gate.
6. Re-run the static balance review for focus durations, political-power and factory-use costs, integration capacity, overextension, chaos thresholds, and terminal counterplay.
7. Perform parent-owned live HOI4 scenario validation; no focus subagent should launch the game or claim in-game completion.

## Risks and open decisions

- Adding nodes can make the 100-focus layout exceed the intended 85-115 total unless shared nodes replace redundant filler or the parent explicitly raises the target.
- Hidden convergence gates can remain hard to discover even after depth is added; this is a UI/readability decision, not a parser defect.
- The current AI strategy plans are statically complete, but live sequencing is not proven. Some origin plans list all four supply choices with equal focus factors, and several project plans end at their project capstones before a later diplomacy or expansion plan takes over.
- Decision surfaces are deeper than the focus surface, so a count-only expansion would be harmful if it repeats generic bonuses or duplicates decision text.
- The biological stockpile/debit integration and full live terminal scenarios remain external blockers to a completion claim.

## Parent disposition

The approximate branch-family counts are not treated as binding in this tranche. The implemented tree already contains 100 bespoke focuses, stays inside the requested 85-to-115 total, covers every required route family, and delegates recurring diplomacy, integration, expansion, and terminal actions to their existing decision systems. Adding count-only nodes would risk filler rewards, duplicate decision content, or pushing the tree beyond its intended size.

This plan therefore does not supersede the implemented architecture and is not queued for immediate implementation. Its route-depth observations remain useful if later scenario play identifies a concrete missing handoff, unreadable convergence, weak AI transition, or absent route-specific consumer. Any future promotion must name that gameplay gap and replace or deepen an existing contract rather than merely raise a branch count.
