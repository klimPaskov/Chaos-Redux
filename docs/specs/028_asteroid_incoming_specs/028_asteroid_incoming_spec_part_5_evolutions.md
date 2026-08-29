# Asteroid Incoming, Part 5: Evolutions

## Evolution structure

Event 028 has two sequential evolutions. They change the impact opening. They do not create separate repeatable events.

- Global Fragmentation becomes available at 600 Chaos.
- Extraordinary Minerals becomes available at 800 Chaos and requires Global Fragmentation.

Both evolutions must respect their individual enable state. A disabled Global Fragmentation evolution also blocks Extraordinary Minerals because fragment craters are part of the second evolution's design.

The evolutions are recorded only when the player chooses an impact and the evolved behavior actually resolves. Choosing the miss avoids both evolutions and creates no evolution history row.

## Evolution I: Global Fragmentation

### Campaign role

The altered trajectory destabilizes the asteroid. The main body still reaches the selected country. Several smaller fragments separate and strike unrelated states around the world.

The evolution turns one directed regional disaster into a global risk. The chooser controls the main target and accepts uncertainty about the rest of the planet. Fragment sites can include the chooser's territory.

### Availability

- Minimum Chaos: 600
- Global Fragmentation evolution enabled
- Event 028 impact option selected
- Enough valid separated fragment centers exist for at least two fragments

When fewer than two valid fragment centers exist, the evolution should remain unavailable for that firing and should not be logged as applied. The main impact still resolves.

### Fragment count

The intended fragment count scales with Chaos and is capped by valid geographic space.

- 600 to 699 Chaos: 3 planned fragments
- 700 to 799 Chaos: 4 planned fragments
- 800 to 899 Chaos: 5 planned fragments
- 900 to 999 Chaos: 6 planned fragments

The actual count can be lower when the world lacks separated valid states. The system reports the actual count. It never overlaps centers or inserts weak invalid targets to meet the plan.

### Fragment center selection

A fragment center must:

- Be a valid populated land state
- Not be inside the main three-ring footprint
- Not be a permanent crater or wasteland
- Not be inside another fragment center's first ring
- Have at least one valid land neighbor when the global pool allows it

Distribution preferences should:

- Use several continents
- Avoid several fragments in one country
- Avoid clustering around the main target
- Include majors and minors through suitability scoring
- Allow the chooser's country to be struck
- Avoid actual nonhuman and system-only countries

Fragment positions are not shown before impact.

### Fragment damage

Each fragment uses a smaller two-ring profile.

#### Fragment center

- Remove about 50 percent of civilian population.
- Remove about 50 percent of existing building levels, with heavy damage to exposed logistics.
- Apply a persistent fragment-crater state modifier.
- Record asteroid-fragment deaths.
- Under Extraordinary Minerals, mark the state as a mineral site.

#### Fragment Ring 1

- Remove about 25 percent of civilian population.
- Cause heavy building, infrastructure, railway, and supply damage.
- Apply a timed heavy fragment-damage modifier.

#### Fragment Ring 2

- Remove about 5 percent of civilian population.
- Cause lighter building and logistical damage.
- Apply a short fragment-damage modifier.

The normal nuclear explosion effect can present each fragment. The transaction remains classified as asteroid fragmentation.

### Resolution order

1. Lock every fragment center before applying damage.
2. Build every fragment footprint.
3. Merge overlaps by strongest profile.
4. Resolve the main impact center and rings.
5. Resolve fragment profiles that are stronger than any main profile already applied.
6. Create fragment craters.
7. Add fragment destruction to Dust Load.
8. Aggregate country reports.
9. Broadcast one fragment summary after the main impact presentation.

This order prevents random selection from changing after the first state is destroyed.

### Reports

Countries affected only by fragments receive the same consolidated report system as countries affected by the main impact. A country hit by several fragments still receives one report.

The global news summary should state the actual fragment count and broad affected regions. It should not open a separate global popup for each fragment.

### Evolution logging

Global Fragmentation uses one evolution log entry tied to Event 028.

- Type: fragmentation
- Stage: 1
- Display tier: Chaos Tier
- Actor: none

The log entry describes a global mutation. The chooser and target remain available through the Event 028 history and detail views.

## Evolution II: Extraordinary Minerals

### Campaign role

The main crater and fragment craters contain material with unusual structural properties. Control of a site improves the armour of a country's land forces. The disaster creates permanent strategic objectives that can change front lines and peace settlements.

The scientific explanation should remain uncertain in public text. Reports can refer to dense meteoric alloys, fused impact material, or unfamiliar crystalline structures. The gameplay effect remains consistent across flavor variants.

### Availability

- Minimum Chaos: 800
- Global Fragmentation evolution enabled and applied
- Extraordinary Minerals evolution enabled
- Event 028 impact option selected

The second evolution is not available for an ordinary nonfragmented impact.

### Main crater benefit

The current controller of the original main crater receives plus 100 percent to existing land-division armour.

This means:

- Existing positive armour values are doubled.
- A division with zero base armour does not gain a flat armour value from multiplication alone.
- The effect applies to land-division armour.
- It does not increase piercing, hardness, naval armour, aircraft defense, or unrelated equipment statistics.
- The benefit does not depend on state ownership, cores, compliance, or ideology.

### Fragment-site benefit

The current controller receives plus 20 percent to existing land-division armour for each fragment crater controlled.

Fragment bonuses stack. The accepted design has no cap. The implementation must expose the controlled-site count in the modifier tooltip and must test high-stack outcomes.

### Transfer and recalculation

Benefits follow current control.

The system should refresh when:

- A crater state changes controller
- A crater state changes owner
- A country is annexed
- A civil war changes control
- A peace conference transfers the state
- A state is released to a subject
- A controller ceases to exist

The refresh should derive each country's current main-crater control and fragment count from the registered sites. It should replace stale modifiers instead of adding another copy on every control change.

A site with no valid controller grants nothing. A country that loses every site loses the full benefit immediately or at the next bounded control-change refresh.

### Strategic objective behavior

Crater states become high-priority objectives.

- AI defense and front planning should value controlled sites.
- AI offensives should value nearby enemy sites when the military situation allows it.
- Peace and state-transfer logic should treat sites as strategic territory.
- Crater controllers gain decisions to survey, secure, and fortify the perimeter.
- Countries at war with a crater controller can receive intelligence or strategic reports that explain the armour advantage.

The event should not grant free claims, cores, or war goals to the whole world. Expansion comes through normal war, existing claims, or bounded high-Chaos crater-conflict actions.

### Site flavor profiles

Each crater can receive one scientific flavor profile for reports and icons. These profiles do not change the armour value.

- Dense metallic material
- Fused silicate composite
- Shock-formed crystal and glass

The profile should be assigned once and persist. It adds replay value without creating several balance tracks.

### Evolution logging

Extraordinary Minerals uses one evolution log entry tied to Event 028.

- Type: extraordinary minerals
- Stage: 1
- Display tier: Totalen Chaos
- Actor: none

The event detail view should show the current main-crater controller, total fragment sites, and each country's controlled fragment count after the evolution exists.

## Disable behavior

- Disabling Global Fragmentation removes fragment strikes from future Event 028 resolution and makes Extraordinary Minerals unavailable.
- Disabling Extraordinary Minerals leaves fragmentation damage and dust intact but creates no armour benefits or mineral-site decisions.
- Rebuilding Event Details must preserve each evolution toggle.
- Disabling an evolution after it has already applied should follow the project's normal evolution-toggle policy. It must not silently erase a campaign outcome unless the existing UI explicitly defines retroactive disabling.

## Balance requirements

The user-defined armour values are intentionally large. Balance review should focus on their campaign consequences. The values cannot be reduced without approval.

Required scenarios include:

- One country controls only the main crater.
- One country controls one fragment site.
- One country controls the main crater and three fragment sites.
- One country controls all planned fragment sites at 900 Chaos.
- Several rival countries each control one or two sites.
- Infantry-only armies with zero base armour.
- Armoured armies near common piercing thresholds.

The implementation must report whether the modifier creates unexpected negative, multiplicative, or non-land effects. A balance concern is evidence for review, not permission to change plus 100 or plus 20 values silently.
