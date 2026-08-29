# Asteroid Incoming, Part 3: Impact Damage and Local Aftermath

## Resolution contract

The impact resolves as one guarded transaction. It determines every affected state, applies the strongest applicable profile once, records actual civilian losses, updates country totals, creates crater states, starts dust, and only then sends reports and presentation events.

The map effect can reuse the existing thermonuclear or nuclear explosion presentation. The gameplay transaction must use asteroid-specific source identity from beginning to end.

## Main impact profiles

### Ring 0: Main crater

The locked center is destroyed.

- Remove all civilian population.
- Remove all state buildings and building levels.
- Destroy infrastructure, railways, supply hubs, ports, air bases, radar, anti-air, forts, factories, dockyards, reactors, rocket sites, refineries, fuel storage, and any other building surface present in the state.
- Clear or invalidate active state projects that cannot exist in a permanent crater.
- Apply the permanent asteroid crater state profile.
- Mark the state as the unique main crater for Event 028.
- Preserve state ownership and control unless another game system changes them.
- Prevent ordinary reconstruction from restoring the state to a normal populated industrial area.

The main crater should remain traversable only under the project's established wasteland rules. It should impose severe supply and movement problems and should never become a free empty construction site.

### Ring 1: Catastrophic zone

Direct land neighbors receive the strongest survivable damage profile.

- Remove about 50 percent of civilian population.
- Cause severe damage to factories, infrastructure, railways, supply hubs, ports, air bases, radar, anti-air, forts, and strategic installations.
- Apply a long-lived catastrophic impact-zone modifier.
- Create the highest local recovery burden outside the crater.
- Place these states first in emergency rescue and transport missions.

A Ring 1 state should remain usable after major investment. The profile must not quietly become another complete wasteland.

### Ring 2: Major damage zone

The next shortest adjacency ring receives a major regional disaster profile.

- Remove about 25 percent of civilian population.
- Cause major damage to industry, infrastructure, railway, supply, and military installations.
- Apply a medium recovery burden.
- Make repair and medical actions useful without requiring years of mandatory cleanup.

### Ring 3: Outer shock zone

The third ring receives a lighter but visible profile.

- Remove about 5 percent of civilian population.
- Damage vulnerable infrastructure, railways, supply routes, and some buildings.
- Apply a short recovery burden.
- Use reports and state modifiers that distinguish the outer shock zone from ordinary natural-disaster damage.

## Building-damage principles

The population percentages are fixed design anchors. Building losses can use category-specific ranges so that the result feels physical and avoids identical state outcomes.

- Infrastructure, railways, supply hubs, air bases, radar, forts, and anti-air should usually take heavier proportional damage than distant civilian industry because shock and debris attack the transport and exposed network first.
- Civilian factories, military factories, dockyards, refineries, reactors, and rocket sites should take severity-scaled damage with clear floors.
- A state with only one level of a critical building should still have a meaningful chance to lose or disable it in Ring 1 and Ring 2.
- Building damage should never add levels through rounding.
- Damage should clamp to existing levels and should not create negative values.
- The transaction must include buildings introduced by supported DLC or the mod when they exist.

The exact category ranges belong in the tuning matrix. The implementation should centralize them and avoid scattering separate values through every event branch.

## Permanent asteroid crater profile

The main crater is a distinct permanent state identity. It is not radioactive fallout and should not borrow radioactive text or icons.

The profile should communicate:

- The state has no surviving civilian population.
- Ordinary buildings cannot be restored.
- Infrastructure and supply remain effectively absent.
- Movement and operations through the state are difficult.
- The controller still owns a geographic and strategic position.
- Extraordinary mineral control, when active, comes from this state.

The profile should use a permanent state modifier and the shared wasteland or unusable-state framework where compatible. Any borrowed framework must preserve the asteroid source and must not add radiation, nuclear contamination, nuclear winter, or nuclear-use records.

Fragment centers use a separate persistent fragment-crater profile. They keep surviving population and buildings after their 50 percent loss. They remain difficult recovery zones and mineral sites, but they are not complete wastelands.

## Civilian population transactions

Every population change must remove real state population without leaving an unintended recruitable-manpower credit.

For each affected state, the event should:

1. Read the population before the impact.
2. Calculate the requested loss from the strongest applicable profile.
3. Preserve any project-wide minimum population rule only outside the main crater.
4. Apply the exact loss once.
5. Record the actual applied value in the Deaths system.
6. Add the actual value to the affected-country incident total.

The main crater uses a zero remaining-population target. Ring and fragment profiles use proportional loss rounded consistently. A state with extremely low population should not report more deaths than it contained.

## Continuing rescue-period deaths

The initial percentages represent the immediate impact. Ring 1, Ring 2, and fragment-center states can suffer a smaller continuing loss during the emergency period from burns, collapse, water failure, debris, and medical overload.

This continuing loss must be bounded.

- It applies only while the state's recovery burden remains unresolved.
- It uses a protected population floor.
- It is highest in Ring 1 and fragment centers.
- It is reduced by the target country's shelter and hospital preparation.
- It can be shortened by medical and debris-clearing actions.
- It stops when the emergency phase closes or the state reaches its recovery threshold.

Continuing deaths should make response choices matter. They should remain much smaller than the fixed immediate losses.

## Deaths system reasons

The Deaths log should distinguish at least these source families.

- Asteroid main impact
- Asteroid main impact, first ring
- Asteroid main impact, second ring
- Asteroid main impact, third ring
- Asteroid fragment center
- Asteroid fragment, first ring
- Asteroid fragment, second ring
- Asteroid rescue failure

Every entry is civilian. Military casualties from divisions in the states can use the project's established military-loss or unit-damage systems if supported, but they must not be estimated from civilian population.

## Country aggregation

After all main and fragment state transactions, the event builds one incident summary per affected country. A country counts as affected when it owned or controlled at least one damaged state at impact time or lost population through the transaction.

The summary should retain:

- Total civilian deaths
- Number of affected states
- Worst damage profile suffered
- Whether the country held the main center
- Number of fragment centers suffered
- Industry and logistical levels destroyed
- Whether its capital was relocated
- Current emergency burden

The country receives one report. The report can name the worst affected state and list totals through dynamic localisation. It should not open separate popups for each state or fragment.

A global news summary can report the total number of affected countries and fragments. It should not repeat every country report.

## Country and government continuity

### Target country survives

Main target construction ensures that the selected country has a valid surviving state. The event should not silently delete the country because one state became a crater.

### Capital destruction

The capital moves before the center is erased. The target receives a temporary government-dislocation state whose severity depends on the emergency stance and whether the capital was hit.

### Leaders and advisors

The event should not randomly kill named leaders, advisors, commanders, scientists, or characters unless a later accepted design adds a dedicated character-survival system. The civilian death total already represents mass loss. Untracked character deletion would create broken country packages and weak feedback.

### Units in affected states

Divisions, aircraft, and ships should suffer through established map, strength, organization, equipment, supply, or base-loss mechanics when supported. The event should avoid deleting all units by script without regard to location or evacuation. The main crater must not leave units operating normally inside a state with no supply or infrastructure.

## Local state modifiers

The state aftermath should use a small readable family.

### Main asteroid crater

Permanent. Communicates complete physical destruction and any mineral control.

### Catastrophic impact zone

Long duration. Used by Ring 1. Carries the highest recovery burden and strongest transport, construction, and local output penalties.

### Major impact zone

Medium duration. Used by Ring 2.

### Outer shock zone

Short duration. Used by Ring 3.

### Fragment crater

Persistent. Used by each fragment center. Carries the mineral site under Extraordinary Minerals.

### Fragment damage zone

Timed. Used by fragment rings at heavy or light severity.

Each family should have a visible lifecycle. Recovery decisions shorten, replace, or remove timed modifiers. The main crater and fragment crater persist.

## Nuclear-system separation

The map visual is the only nuclear-adjacent surface.

The asteroid transaction must not:

- Count as a nuclear or thermonuclear strike
- Add nuclear condemnation
- Trigger nuclear retaliation
- Add radioactive fallout
- Add a nuclear-use Chaos ladder entry
- Fulfil nuclear achievements or decisions
- Trigger nuclear diplomatic reactions
- Record a nuclear attacker or victim
- Use a nuclear Deaths reason
- Start Fallout through a nuclear-use path

Dust and Air Cleanliness changes are asteroid-derived environmental pressure. They should remain distinguishable in history and tooltips.

## Interaction with prior damage

The event can strike states already damaged by war or disaster.

- Population loss uses current population.
- Building loss uses current building levels.
- Reports state actual losses, not theoretical undamaged values.
- The main crater still removes whatever remains.
- Recovery burden starts from the event profile and can account for pre-existing infrastructure weakness.
- A state already carrying a temporary natural-disaster modifier may keep it when compatible. Duplicate generic penalties should be consolidated where possible.

## Control and report edge cases

- When owner and controller differ, population and building losses apply to the state once.
- The controller receives the immediate operational report and recovery actions.
- The owner receives a territorial-loss report when it remains a distinct country and the project report framework supports it.
- Deaths attribution should identify the civilian country associated with the state under the shared Deaths contract.
- A country that ceases to exist during report dispatch should not receive a broken popup. Its totals remain in global history.

## Recovery closeout

A country's emergency phase closes when all of its timed impact-zone burdens have expired or been resolved. The category should record the recovery date and remove obsolete emergency actions.

The closeout does not restore the main crater, remove fragment sites, clear dust globally, or cancel extraordinary mineral control. Those are separate persistent or global states.
