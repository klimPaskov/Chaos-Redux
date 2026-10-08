# Weaponized zombie native raid helpers

These helpers preserve the existing six native air-raid capabilities while checking current authorization and exact selected targets at outcome resolution.
They use the existing Biological Raids category, aircraft, payload, icons, sounds, success factors, losses, experience, preparation, and Command Power allocation.
The parent accepted target-specific strategic permission and the fixed tier/friendly event map on 2026-10-08 under the accepted CBRN overhaul.

## Helper map

| Helper | Scope and ROOT | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- | --- |
| `capture_weaponized_zombie_native_raid_context` | RAID_INSTANCE | Native `actor_country`, `victim_country`, `target_state` dynamic scope pointers | Saves regular targets `zombie_native_raid_actor`, `zombie_native_raid_victim`, `zombie_native_raid_target_state`; no persistent dispatch data | All 18 accepted raid callbacks, immediately before their fixed actor country event |
| `weaponized_zombie_raid_actor_is_authorized` | Actor country | Current existence, capitulation, world-end, project/technology unlock, Kruger authority | Boolean; no payment or policy change | Visibility and shared preflight/final checks |
| `weaponized_zombie_raid_can_target_from` | Actor country ROOT, victim FROM | Actor gate, war, faction relationship, target-specific strategic policy, selected native state | Boolean; existing policy helper writes temporary target ID; passability, friendly target and canonical-convergence exclusions apply | `show_target`, `available`, `launchable`, and the leading AI zero gate of six raids |
| `weaponized_zombie_native_raid_context_is_valid` | Country ROOT = captured actor | Three exact regular targets, matching event actor, current actor gate, victim existence, war, faction relationship, current exact-victim strategic policy, target controller, current target eligibility | Boolean and temporary policy target ID; no debit or refund | Both resolver helpers, after the fixed event's exact tier/friendly check |
| `resolve_minor_weaponized_zombie_native_raid` | Country ROOT = actor | Valid captured context | One shared final-gated consequence block and existing minor outbreak helper in state-to-actor nesting | Odd bridge IDs `.1`, `.3`, `.5`, `.7`, `.9`, `.11` |
| `resolve_weaponized_zombie_native_raid` | Country ROOT = actor | Valid captured context | Same shared final gate and consequence helper, then existing full outbreak helper | Even bridge IDs `.2`, `.4`, `.6`, `.8`, `.10`, `.12` |

There are no defaults for missing native pointers: the final gate rejects them.
The consequence API is documented in `zombie_special_project_effects.md`.
The preflight and final helpers live with existing zombie triggers in `common/scripted_triggers/002_zombie_outbreak_triggers.txt`.
The state helper is safe only with actor country ROOT; physical native target filters remain actor-neutral.

## Static outcome identity

| Tier and profile | Limited success | Success and critical success |
| --- | --- | --- |
| Low hostile | `.1` | `.2` |
| Medium hostile | `.3` | `.4` |
| High hostile | `.5` | `.6` |
| Low friendly | `.7` | `.8` |
| Medium friendly | `.9` | `.10` |
| High friendly | `.11` | `.12` |

All IDs use namespace `zombie_native_raid_bridge` and are triggered-only hidden actor country events with no delay.
Each checks the exact tier flag and friendly/hostile flag family before its resolver.
No country/global pending scalar, synthetic capture marker, or fabricated native receipt exists.
Fixed IDs cannot overwrite one another when separate raids resolve.
Regular targets carry within the originating effect/event chain and automatically expire at its end.
No global targets are added by this bridge; existing outbreak profile/news targets retain their owner lifecycle.

## Policy, tuning and resource settlement

Unrestricted Authorization permits the wartime raid.
Retaliation Only permits it only with a current unexpired retaliation right against the exact victim.
Battlefield Authorization does not authorize this strategic route, including when a stale retaliation record remains.
Friendly anti-zombie profiles share this requirement and retain their zombie-controlled target restriction and achievement.
Doctrine and Kruger desirability coefficients never supply permission or change policy.
The visibility gate has no target binding, so it checks actor authority and profile; exact national use permission is applied once a target exists.
The native payload remains 125, Command Power allocation 15, preparation 10 days, and reenabling interval zero.
Existing success values and all preference coefficients remain; a leading zero modifier rejects unauthorized target choices.
The existing `weaponized_zombies.raid_payload` constant continues to serve stock affordability; no new constants are introduced.
Launch and resolution do not require stock already collected by the native raid to remain free.
Native `essential_equipment` and `command_power` are the sole payment/allocation path.
The upfront payload and Command Power appear through native cost rows.
The six prepare-time payload stock gates are hidden requirements, so their text does not repeat the native 125-payload payment.
The separate authorization requirement tooltip remains visible.
The exclusive unused `weaponized_zombie_raid_available_tooltip` localisation key is removed.
These are source presentation facts; live native row layout and deduplication are not established by the source tests.
Outcome effects do not refund or debit resources.

## Migration and validation limits

Each prior consequence `actor_effects` call and independent outbreak `victim_effects` call becomes one hidden actor dispatch plus a neutral conditional victim tooltip.
Failure outcomes retain only their existing aircraft losses.
Consequences precede spawn inside the same accepted block so zombie-control classification reads the selected state's original controller.
The existing spawn helpers receive country ROOT and state PREV; strain resolution, controlled profiles, outbreak construction, evolution/news, and achievements retain their existing implementation.
The native bridge does not prove engine outcome callback cardinality, equipment recovery on cancellation, or successful dynamic country/unit creation.
MCP event inspection/rendering may omit scripted helpers and native raid definitions, and the probability service has no native raid AI/success adapter; those limits are recorded in the dated handoff.
No fallback or simplification is introduced.

## Assets and future work

No new icons or art are required.
Existing consumers use `GFX_raid_type_icon_weaponized_zombie_strike`, `GFX_zombie_disease_bomb_equipment_medium`, and their existing report/news assets.
Future bridge changes should preserve fixed profile identity, exact scope targets, shared final acceptance, and native-only settlement.
Any deeper profile or zombie event redesign belongs to the owning feature plan.
