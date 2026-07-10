# Event 011 improvement-loop resolution

Date: 2026-07-10

Disposition: all accepted must-fix tranches A-G from `011_secret_alliance_implementation_improvement_addendum.md` are implemented. None remains queued, rejected, or superseded. The optional future ideas remain optional and are recorded in the Event 011 future-plans section. They are not part of the accepted completion boundary.

The strict decision and mission re-audit resolves DM-01 through DM-14 and RA-01 through RA-02. The strict localisation re-audit is CLEAN and resolves LOC-011-01 through LOC-011-08, including workbook mirroring. These clean reports supersede their earlier incomplete snapshots and confirm that no accepted improvement tranche has reopened.

## Resolution map

| Tranche | Implemented result | Primary evidence |
| --- | --- | --- |
| A: standing conference, roles, commitments | Every member receives a motive, commitment band, primary role, support capability, and private commitment. Recruitment, doctrine, dispute, and reveal behavior read these profiles. | `secret_alliance_assign_current_member_profile`, member-profile constants, member arrays and dispute helpers in `common/scripted_effects/011_secret_alliance_effects.txt` |
| B: operation dossiers and pacing | One substantial operation is owned at a time with actor, family, surface, risk, evidence class, readiness layer, recent-family penalty, and adaptive recovery. MTTH cadence responds to evolution, readiness, alertness, preparedness, recovery, and controlled channels. | `secret_alliance_launch_weighted_operation`, operation dossier variables, `common/mtth/011_secret_alliance_mtth.txt` |
| C: evidence and suspect curation | Six source-aware evidence classes prevent duplicate class/source farming. Corroboration and independent-class thresholds govern public actions. The full AI suspect array is separate from the capped three-card visible array and confidence bands. | `secret_alliance_register_operation_clue`, `secret_alliance_apply_new_clue`, `secret_alliance_rebuild_visible_suspects`, Event 011 scripted GUI/localisation |
| D: maintained Preparedness and objectives | Seven capped maintained components, timed burdens, expiry events, action-family caps, and named state/country mission objectives replace permanent click accumulation. Full, partial, and failure outcomes use one weighted resolver. | preparedness constants/effects, `secret_alliance_prepare_*_objective`, mission effects, decisions and ideas |
| E: interruptible evolution | Evolution I recruits toward a wider minor roster. Evolution II approaches one sponsor and opens serious operations. Evolution III permits a second sponsor, pressure, warning, conference, preparation, and preemption. Human invitations have explicit consent choices, and pre-fire evolved starts use the same stage helpers. | evolution effects, invitation/sponsor events, concealed pulse, pre-fire evolution helpers |
| F: public faction, roles, Resolve | The reveal creates a real Anti-[target] faction, maps doctrine into public goals, converts hidden values into four public-war values, preserves turned, delayed, and fractured consequences, and updates Resolve from war facts and settlement choices. | faction template/rules/goals, `secret_alliance_reveal_pact`, reveal conversion, public-war effects, settlement effects |
| G: AI, scenario, achievements | Role-aware member, sponsor, remote-support, target-defense, and maximum-scenario AI are active. All five scenario types and four intensities affect composition and packages. All six achievements use exact origin and reveal snapshots. | `common/ai_strategy/011_secret_alliance.txt`, scenario registry/effects/triggers/localisation, achievement definitions and Event 011 achievement documentation |

## Accepted completion scenarios

- Normal baseline opening selects exactly three distinct valid AI minor founders and fixes the human target.
- Pre-fire Evolution II and III openings use the same member/profile, counter-network, sponsor, and warning systems as active evolution.
- Investigation, protection, diplomacy, deception, border, public, emergency, and wartime actions have non-PP resource commitments and matching AI routes.
- Evidence cannot reach complete-network state through one repeated method or source.
- Preparedness expires by component and affects only relevant operations and reveal conversion.
- A normal hostile target war reveals immediately and calls every valid active member into the existing war.
- Planned reveal preserves turned-member, false-plan, delayed-call, and fracture consequences.
- Coalition Unmasked retains terminal-state, scope, composition, and human-consent gates while bypassing normal automatic prerequisites.
- Cleanup removes missions, burdens, border conflict, arrays, event targets, AI strategies, and transient member/suspect state.

## Source-of-truth promotion

The accepted addendum did not change the five-part source specification's scope. It supplied causal implementation detail already required by the specification. The completed behavior is summarized in `docs/events/011_secret_alliance.md`, while this resolution file remains the audit trail showing that every accepted improvement item was closed.
