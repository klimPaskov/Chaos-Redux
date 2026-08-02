# Event 012 Africa — Common Reserve Deployment

This document records the runtime contract for the Charter League's common reserve. It uses the existing `africa_common_defence_stockpile` variable and does not create a second material store.

## Opening and mobilisation

`africa_select_mobilise_continental_defence` remains a post-unification Scramble-response action. Its validator now requires the existing host to hold the configured minimum stockpile, prove one real transport receipt or logistics focus flag, and be in the intervention phase. A full result calls `africa_common_reserve_activate`; partial and failed results do not open the reserve posture.

Activation records the host's opening day, a bounded settlement window, and the deployment sequence. The posture is visible through the existing Charter Ledger stockpile readout and the action result localisation.

## Defensive deployment

`on_war_relation_added` treats `ROOT` as the attacker and `FROM` as the defender. A protected, achievement-counted partner with a controlled capital can receive one deployment when the current host's reserve posture is active and the stockpile can pay the configured per-war cost. The host stockpile is debited at deployment, the partner receives a deployment flag and deadline, and the sequence is copied to the partner for exact positive-proof counting.

The defensive trigger also requires `africa_member_host_generation_is_current`, so a protected receipt from a superseded host cannot spend the successor host's reserve.

Protected partners that start an offensive war receive no reserve. The host records `africa_achievement_reserve_offensive_abuse` so the achievement cannot be satisfied by a misused posture.

## Settlement and cleanup

The existing `on_peace`, `on_capitulation`, and `on_annex` callbacks close the deployment without a daily scan. An on-time settlement with the partner's capital still controlled calls `africa_achievement_record_reserve_war_answered`. Capitulation, capital loss, or an out-of-window settlement writes sticky achievement disqualifiers. Partner deployment flags and deadline variables are cleared in every terminal path.

The reserve remains a finite stockpile-backed posture. When the store cannot fund another deployment, or the bounded posture window expires, the deployment trigger fails closed and the next war callback clears the posture; no negative stockpile or passive free unit store is created. RSA exile succession carries the stockpile, deployment sequence, and active posture markers to the accepted successor host.

## Icons and UI

No new art is required for this kernel. The action uses the registered `GFX_decision_012_africa_charter_ledger` decision icon. The existing focus family sprite `GFX_goal_africa_focus_family_army_common_reserve` remains the visual identity for reserve preparation. If a future reserve mission gains a dedicated sprite, register it in `interface/012_africa.gfx` before wiring a localisation key.

## Future extension

The next safe extension is a reviewed regional-command mission that spends the same stockpile and binds to an explicitly selected protected partner. It must preserve the defender-only callback, sequence-based achievement owner, deadline disqualifier, and idempotent cleanup rather than adding a second reserve array or a recurring world iteration.
