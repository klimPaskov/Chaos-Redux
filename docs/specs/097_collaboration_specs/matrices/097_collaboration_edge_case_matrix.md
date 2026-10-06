# Event 097 Collaboration: Edge Case Matrix

Each row states a situation the implementation must handle and the required behavior. These are design rules, not optional checks.

| Situation | Required behavior |
| --- | --- |
| Fewer than two participants | Event 097 is unavailable and shows `N/A` in the event list. |
| A participant stops existing during the application pass | Its batch is skipped. Pairs that include it are skipped. Nothing else changes. |
| A participant is annexed after layers were applied | Its outgoing and incoming collaboration become irrelevant through the engine. Event 097 performs no cleanup of native values. |
| A country is created after a firing | It joins at the next firing with no back-payment. |
| Civil war breakaway | It is a participant if it owns territory and uses ordinary civilian systems. Collaboration of others inside the original country does not transfer to it. |
| Government in exile with no owned state | It receives no incoming layer. It keeps receiving outgoing layers. |
| Special Chaos country or nonhuman country | Excluded in both directions. Existing collaboration from other sources is untouched. |
| A country becomes a special Chaos country after receiving layers | It stops participating. Existing native values remain, but every Event 097 behavior checks participant status, so none of them fire for it. |
| Player does not answer the opening report | The first option, Accept, applies after the event timeout. |
| Multiplayer with different stances | Each human's choice made inside the response window counts. The application pass starts after the window. |
| Tag switch during the response window | The stance recorded on the country scope applies. The new player inherits it. |
| Event 097 fires again while an application pass is still running | Selection is blocked while a pass is running. The event is unavailable until the pass completes. |
| A cluster burst includes Event 097 while its pass is running | Event 097 skips with the established cluster skip reason. |
| A seated state is retaken by an ally of the owner | The seat ends and Collaborators Unmasked can appear for the owner. |
| A seated state changes hands between two enemies of the owner | The old seat ends and the new controller is checked for its own seat. |
| A host with the Fifth Column makes peace with one enemy and fights on against another | The Fifth Column is re-evaluated against the remaining enemies. |
| Two co-belligerents both qualify for the prepared-government offer | The installer selector in Part 3 picks one. The other can use the decision later only if no living government installed through this route exists for that original tag. |
| The installer is annexed | Its installed governments enter the Abandoned stage if they survive the engine's subject handling. Registry rows record the event. |
| The original country is restored over a government's territory | The registry row is retired with a restoration record. The Chaos reversal row applies according to the route. |
| A government installed through this route becomes independent through Event 063 or engine rules | The registry row is retired, the spirit is removed, and a former-collaboration marker remains for Event 095 and achievements. |
| Democratic installer and the engine refuses the route | The implementation reports the blocker. It must not exclude democracies quietly or create a separate creation route. |
| Fallout transition begins | Event 097 becomes unavailable, its pending pass stops at the next step without applying another batch, and evolution behaviors stop creating consequences. Every write to native collaboration checks the Fallout gates, so no pair can hold Event 097 collaboration after the Fallout reset and the clean-world proof is never blocked by Event 097. Its records stay for achievements. |
| A captured state is not a core of its owner | No seat, no Open Gates, and no prepared cadres for that state, because Event 097 collaborators are the host's own people in its own lands. |
| The Chaos Meter is disabled in settings | Event 097 consequences still happen. Its Chaos rows add nothing through the shared block. |
| Event 097 is still in the rework disable queue | The event cannot fire until registration, logging, and Event Details wiring are complete and Event 097 is added to the reworked default-enable list in the same change. |
| World-end state reached | Ordinary automatic event firing stops through the shared rule. Event 097 adds nothing special. |
| Event 097 disabled in settings | No firing and no new evolution activation. Behaviors of evolutions that already activated continue, because they describe existing networks. |
| One evolution disabled after activation | Its behavior stops at the next evaluation. Its records stop updating. Other evolutions continue. |
| Manual or forced trigger from settings | The event runs normally and sets the shared forced-setup marker that disqualifies Event 097 achievements. |
| Console collaboration command | The engine already disables achievements. Event 097 behaviors read the native value normally, but only for hosts with Event 097 networks. |
| Fewer than two powers left with governments after competing orders fired | Nothing is refunded. The milestone stays recorded. |
| A country chooses Screen while already under Loyalty Commissions | Only the incoming multiplier applies. The commissions keep their duration. |
| An installed government is itself a host in a later war | It participates in Divided Loyalties like any other country. |
