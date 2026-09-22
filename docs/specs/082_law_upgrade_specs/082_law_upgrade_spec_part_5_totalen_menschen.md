# Law Upgrade
## Part 5. Totalen Menschen!!!

## Place and purpose

Totalen Menschen!!! is the final conscription law, immediately after Scraping the Barrel. It replaces the existing conscription law.

The law makes 99% of the population covered by the country's recruitment system legally recruitable. Its attraction is the ability to continue reinforcing and raising forces after every normal manpower policy has been exhausted. Its price is catastrophic damage to the workforce and administration that make those forces usable.

This is the desperate manpower endpoint. It must not become a generally superior conscription choice for a country that already has sufficient recruits.

## What 99% recruitment means

The law's recruitable-population setting is 99%, not a 99% bonus to the previous percentage and not an additional grant equal to 99% of population.

Recruitment still uses the country's real eligible population. The law does not grant cores, erase occupation restrictions, recruit foreign populations twice, recover the dead, or redefine a subject's and overlord's ownership of the same population.

The ordinary mobilization process releases recruits over time. The event itself does not place the entire legal pool into immediately available manpower. Training, equipment, deployment, reinforcement, and supply remain separate processes.

Other recruitable-population bonuses must not allow the legal pool to exceed the 99% ceiling. National restrictions that govern which population is accessible continue to apply. The installed-game implementation must prove that its displayed legal rate, population accounting, and actual pool respect these distinctions.

The design requires the actual 99% law setting. A large one-time manpower award is not an acceptable substitute when the engine-facing implementation is difficult.

## Proposed penalties

All values below are this law's contributions, replacing rather than retaining Scraping the Barrel's old payload. They are proposed starting balance.

| Area | At 0% War Support | At 100% War Support |
| --- | ---: | ---: |
| Military factory output | -95% | -80% |
| Dockyard output | -95% | -80% |
| All construction speed | -90% | -65% |
| Repair speed | -90% | -65% |
| Training time | +250% | +100% |
| Army experience gain | -75% | -50% |
| Research speed | -90% | -65% |
| Political Power gain | -50% | -25% |
| Population growth | -99% | -90% |
| Stability | -50 percentage points | -30 percentage points |

Maximum War Support still leaves an 80% law-owned output loss, severely reduced construction and research, and doubled training time. The 99% recruitment setting should feel extraordinary because its civilian consequences are also extraordinary.

The law does not add an attack bonus, supply discount, free organization, military experience award, or special equipment efficiency. Having more legally recruitable people does not make them better supplied or better trained.

## Workforce consequences

The workforce penalties represent the legal system reserving almost everyone for military use and repeatedly disrupting civilian employment. They apply while the law is held, even when the country has not yet deployed all of its legally recruitable population.

This prevents a player from retaining a theoretical 99% reserve while treating the remaining economy as if the law were harmless until the final recruit is mobilized.

War Support mitigates disruption and administration. It does not create additional people to perform civilian work.

## Training and reinforcement

A training-time increase of 250% means a law-owned duration multiplier of 3.5, not 2.5. A 100% increase means a multiplier of 2.

The law does not directly destroy already-trained divisions or strip their experience on entry. Its Army experience-gain penalty affects continuing institutional learning rather than retroactively deleting earned experience.

Existing reinforcement priorities and equipment shortages remain operative. A country can therefore have a huge legal manpower pool and still be unable to create an effective army.

## Population and losses

Reduced growth is a continuing capacity effect. It does not repeatedly subtract a percentage of the whole population and does not trigger the project's death accounting merely because a law is held.

Actual war casualties remain actual losses. Re-entering the law, loading a save, or being selected by Event 82 again cannot recreate people who have already died or grant the same recruits again.

A country cannot increase population by alternating between this law and Scraping the Barrel.

## Returning to Scraping the Barrel

The manual action restores Scraping the Barrel at the doubled current adjacent-change price.

Already-deployed military personnel remain deployed under the game's ordinary law-change behavior. The action does not automatically kill, disband, or return every soldier to civilian life.

The legal recruitment ceiling falls to that of the restored law. Available reserves and further mobilization must reconcile through the verified native population system. There must be no Event 82 refund or top-up that preserves an illegally created duplicate reserve.

The reduced law can still leave the country overcommitted to its military. Reversal ends this law's continuing penalties, but it does not recover dead soldiers or instantly undo an army expansion.

## Choosing which extreme law to leave

A country with plenty of manpower and insufficient weapons normally gains more from reversing this law first. It retains the industrial emergency while recovering a much larger share of productive capacity.

A country facing immediate reinforcement failure can instead keep this law while leaving the economy extreme, especially when civilian rebuilding or Political Power recovery is more urgent than additional military production.

Neither choice is mandated. The AI and the player should evaluate the country's actual shortages, war position, support, and price of recovery.

## No artificial escape subsidy

The design keeps Political Power penalties below a total law-owned suppression of political income. It does not compensate the player with free Political Power, exempt the AI from costs, or make reversal cheaper after a fixed waiting period.

Acceptance testing must nevertheless demonstrate a viable saving route in an ordinary country after optional Political Power spending is stopped. If the implementation accidentally makes the combined law package permanently prevent its own manual reversal in that baseline, the balance or effect mapping fails.
