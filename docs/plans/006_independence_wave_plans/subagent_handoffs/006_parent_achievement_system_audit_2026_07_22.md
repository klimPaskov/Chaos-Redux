# Event 006 parent achievement system audit

Date: 2026-07-22

Scope: all sixteen accepted Event 006 achievements across the specification
matrix, runtime registry, proof triggers, proof writers, narrow on-actions,
English localisation, icon triplets, and system documentation.

## Result

The definition and presentation surface is complete. The accepted matrix has
sixteen unique IDs. All sixteen IDs have one achievement definition, one final
proof trigger, one name, one description, one condition tooltip, and the
correct visible or hidden disposition. All forty-eight runtime DDS files exist
as 64 by 64 textures. The four hidden IDs match the matrix exactly:

- `chaosx_006_volga_bulgaria`
- `chaosx_006_assyria_survives`
- `chaosx_006_radical_bloc`
- `chaosx_006_every_flag_survival`

The English localisation file is UTF-8 with BOM. The runtime definitions keep
the shared any-country `possible` contract and delegate the full condition to
the matching scripted trigger in `happened`.

## Proof coverage

| Accepted proof family | Runtime evidence | Result |
| --- | --- | --- |
| One-state survival | Origin date, anchor opening, legitimacy, recognition, capacity, sovereignty, subject history, reunion exclusion | Wired |
| Patron independence | Recognition, security, patron warning, permanent dependency history, client-route exclusion | Wired |
| Former-host settlement | Property and citizenship receipts, recognized separation, five-year clock, war and forced-settlement disqualifiers | Wired |
| Reconquest defense | Former-host attack direction, anchor-loss grace period, peace resolution, sovereignty and client-route checks | Wired |
| Natural league formation | Founder ledger, five-member threshold, five charter pillars, pre-formed scenario exclusion | Wired |
| Cross-regional league | Member and region counts, cohesion, two-year continuous clock, radical and pre-formed exclusions | Wired |
| Member rescue | Exact rescuer and target pointers, one-year target survival, voluntary-reunion disqualifier | Wired |
| Regional formable | Committed transaction and complete first-stage integration receipts | Wired for admitted families |
| Volga Bulgaria | Exact CHU and IW-043 generation, route exclusivity, cosmetic identity, two-state control, Event 5 exclusion | Wired, currently unreachable while package admission is closed |
| Assyria | Exact ASY and IW-058 generation, recognition, community protection, settlement, host-conflict proof, route identity, anchor control, client and Event 5 exclusions | Wired, currently unreachable while package admission is closed |
| One-state major | Institutional-major receipt before formable activation, professional army, successful league goal | Wired |
| Radical bloc | Radical route, dangerous-milestone qualification, external containment engagement, one-year survival, scenario-forced exclusion | Wired, no currently admitted route can complete the full proof |
| Scenario survival | Low non-Common-Congress launch, exact scenario plan ledger, five-year clock, 85 percent independent-survivor test | Wired |
| Balanced patrons | Three unique major-aid patrons, permanent dependency exclusion, client-route exclusion, concession buyout | Wired |
| League arbitration | One leadership term, five arbitrations, member-war and coercive-settlement exclusions | One accepted disqualifier is still missing a writer |
| Host remnant | One-state host, exact settlement count, ten peaceful years, sovereignty, non-reconquest record, capital, stability, civilian factories, infrastructure | Wired |

The proof-writer effects are called by the shared Event 6 origin transaction,
country-state refresh, patron transaction, league formation and leadership,
DM-43, DM-44, DM-51, the danger milestone, the scenario commit, origin cleanup,
and the narrow war, peace, state-control, annexation, and subject on-actions.
No daily, weekly, monthly, or whole-world achievement scan is used.

## Asset evidence

Every achievement ID has completed, grey, and not-eligible runtime DDS files in
`gfx/achievements/`. Every ID also has one source image and three processed PNG
records under `docs/assets/006_independence_wave/`.

The Assyria triplet that an older system document called missing is present in
both the dated static-icon package and the runtime directory. Its three states
have a dated parent visual approval record. This audit does not grant country
package or portrait admission.

## Open acceptance gap

The league specification accepts expulsion as a real charter action and lists
expulsion as a disqualifier for the arbitration achievement. The trigger checks
`independence_wave_achievement_member_expulsion_during_term`, but no current
effect writes that flag because the league has no complete expulsion
transaction. The achievement cannot receive a false positive from an existing
expulsion action because no such action exists. The wider Event 6
implementation is still incomplete until a charter-governed expulsion vote,
membership removal transaction, cohesion and confidence consequences, AI
behavior, localisation, and this proof writer are implemented and audited.

## Files reviewed

- `docs/specs/006_independence_wave_specs/matrices/006_achievement_matrix.csv`
- `common/achievements/chaos_redux_achievements.txt`
- `common/script_constants/006_independence_wave_achievement_constants.txt`
- `common/scripted_triggers/006_independence_wave_achievement_triggers.txt`
- `common/scripted_effects/006_independence_wave_achievement_effects.txt`
- `common/on_actions/006_independence_wave_achievement_on_actions.txt`
- `localisation/english/006_independence_wave_achievements_l_english.yml`
- `docs/achievements/006_independence_wave/achievements.md`
- `docs/assets/006_independence_wave/manifest.md`

## Meaningful validation

- Matrix to registry count: 16 of 16.
- Matrix to completion-trigger count: 16 of 16.
- Matrix to name, description, and condition-tooltip coverage: 16 of 16.
- Hidden disposition: exact four-ID match.
- Runtime achievement texture count: 48 of 48 at 64 by 64.
- Source and processed record coverage: 16 of 16 IDs.
- Achievement-specific trigger flags without a writer: one, the accepted but
  unimplemented league-expulsion disqualifier described above.

