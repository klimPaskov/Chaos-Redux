# Event 012 Africa — AI, Balance, and Validation Spec

## Balance goals

The Africa event should feel dangerous and continent-scale without becoming an instant unstoppable snowball. The player should see a new African power with a legal claim to the continent, but the actual path to unity should require war, diplomacy, faction management, logistics, integration, and internal legitimacy.

## Power pacing

| Phase | Power granted | Power held back | Why |
| --- | --- | --- | --- |
| Initial firing | Cosmetic identity, continental legal claim/core promise, first decisions, first focus tree, opening army package | Full effective integration, free annexation, infinite manpower, instant colonial war goals against everyone | Makes the fantasy visible without deleting the campaign. |
| Congress formation | Faction, protection actions, limited readiness, diaspora and supply tools | Forced annexation of members, global sponsorship, mythic units unless chaos supports it | Establishes anti-colonial identity first. |
| Continental war | Anti-colonial war goals, military preparations, regional units, intervention decisions | Immediate cores from every occupied state without resistance/integration work | Wars become playable campaigns. |
| Africa Is One | Dramatic identity, major economy/manpower, post-unification branch | Immediate world annexation | Sets up global chaos instead of ending all play instantly. |
| Global sponsor | Influence and proxy tools for other continent unifiers | Free creation/annexation of other continents | Requires other event systems to do their own work. |
| World-end | Terminal world union path | Ordinary random-event continuation | World-end is final and explicitly gated. |

## Dynamic scaling factors

Every major number should be tuned through script constants or documented tuning. The spec expects dynamic formulas based on:

- chaos tier and chaos value;
- selected country's industry, manpower, stability, war support, and army size;
- number of African states controlled by colonizers;
- number of independent African countries alive;
- number of African countries already in the congress faction;
- percent of African strategic regions controlled;
- active wars involving African states;
- colonial backlash and scramble pressure;
- Congress Cohesion and Continental Legitimacy;
- route flags, evolution stage, and world-end flags;
- supply access, ports, railways, convoys, trains, and fuel;
- whether the selected actor is RSA in Allies.

## Cost palette

Important decision costs should use varied resources. Political power may appear, but should not dominate.

| Action type | Preferred costs/requirements | Notes |
| --- | --- | --- |
| Protect African state | Infantry equipment, support equipment, convoys/trains, diplomatic legitimacy, access route | Must feel like actual aid. |
| Prepare anti-colonial offensive | Army XP, command power under safe cap, fuel, equipment, supplied divisions in named regions | Avoid one-click war-goal spam. |
| Integrate member | Legitimacy, cohesion, local support, time, garrison/supply requirement, stability risk | Forced integration creates backlash. |
| Build industry/logistics | Civilian factory burden, trains, steel, controlled rail/port states | Industry should change the map. |
| Invite diaspora return | stability threshold, consumer goods burden, convoys, housing/industry capacity | Garvey/Black Star inspiration, not a free manpower button. |
| Mythic action | high chaos, mythic charge, stability/war support risk, environmental consequence | Weird power must carry costs. |
| Sponsor other continent | convoys, fuel, equipment, intelligence exposure, foreign suspicion, overreach | Prevents global influence farming. |

## Exploit prevention

| Exploit risk | Prevention |
| --- | --- |
| Instant continent cores make manpower infinite | Separate legal core promise from effective integrated benefits where possible; use integration stages and resistance/overstretch ideas. |
| Congress members annexed repeatedly | One-time integration flags, cooldowns, member consent/resistance state, cleanup after annexation/puppet transfer. |
| Free unit loops | Unit decisions have one-time target flags, escalating equipment/manpower costs, active cap, route locks, and AI limits. |
| War-goal spam | War goals gated by regional readiness, focus unlock, cooldown, target validity, and active war cap. |
| Equipment farming through subjects | Subject aid decisions cost central stockpiles and cannot be repeated on dead/invalid targets. |
| Other continent sponsorship snowball | Overreach and suspicion rise; sponsorship target cap; no free continent spawn; requires target event gate. |
| RSA civil-war peace abuse | Allied peace only after African Congress wins the civil war and specific aftermath event fires. |
| High-chaos nonhuman tags treated as normal | Register with shared special/nonhuman classifications and block ordinary migration/ideology/event effects where appropriate. |

## Meaningful validation plan for implementation

### Spec-to-file validation

- Event 012 registered as `Minor Fire-Once`, valid-target logic covers African-capital countries, unavailable event shows N/A.
- Entry event `chaosx.nr12.1` exists and branches into normal Africa package or RSA civil-war package.
- Event detail text describes premise, not raw effects.
- Event log actor mapping points to selected unifier after pre-fire target setup.
- Evolutions log only true mutation tracks, not baseline stages.

### Focus tree validation

- Route coverage table compares required routes from `012_africa_focus_tree_plan.md` against implemented routes.
- Political, liberation, integration, industry, military, diaspora/diplomacy, post-unification, high-chaos, and global sponsor lanes exist or are explicitly merged with reason.
- No large branch is a thin vertical chain of generic modifiers.
- Focus filters/search categories are assigned.
- Focus AI respects route validity.

### Decision and UI validation

- Decision categories stage content by phase and route.
- Congress Board GUI, if implemented, has AI equivalents for meaningful buttons.
- Nonstandard costs have readable blocked localisation.
- Obsolete target decisions clean up after war, annexation, route change, or target death.
- Active missions have varied duration and real objectives.

### Country and formable validation

- Selected actor gets cosmetic identity, leader/title/country-name updates, and focus tree loading only for event-created or event-transformed context.
- RSA civil-war branch only happens when RSA is selected and in Allies.
- Regional subjects do not spawn as empty tags if expected to fight.
- High-chaos nonhuman packages have shared classifier coverage.
- Dynamic union names and merger gates require completed continent-unifier partners.

### Asset validation

- Every visible focus, decision, idea, achievement, flag, portrait, faction emblem, report/news/super-event image, GUI piece, and animated state has an asset entry or a documented not-needed reason.
- Historical flags/symbols and real portraits are sourced, not generated.
- Generated nonhuman/supernatural assets are clearly fictional.
- Animated assets have static fallback, frame-sheet plan, target surface, sprite name, and state logic.

### Super-event validation

- No unresearched title, quote, button text, cultural remark, or audio is wired.
- Every final super-event has researched quote, licensed audio, final image, localisation, docs, and spreadsheet alignment.
- World-end super-event is terminal and gates incompatible future systems.


## Expanded edition validation: niche polities

Additional validation scenarios:

1. **Regional reveal:** fire the event with a West African host and confirm only plausible West/Sahel modules are visible at first, not every continent-wide module.
2. **Module cap:** unlock Old Polity Archive decisions and confirm active mission caps prevent UI flooding.
3. **Forced integration revolt:** centralise one module with low Regional Trust and verify a resistance, exit, or revolt outcome can occur.
4. **Peaceful integration:** integrate one loyal module through trust, construction, equipment, and time costs without instant free cores.
5. **High-chaos nonhuman actor:** unlock Primate Forest or Forest Elephants and verify it has institutional/nonhuman identity, no human party text, and classification as special/nonhuman where implemented.
6. **Source-mode asset audit:** ensure historical flags, religious symbols, royal insignia, scripts, and real portraits are sourced or blocked, while fictional/high-chaos assets are generated and documented.
7. **AI validity:** confirm AI does not choose modules outside reachable regions or high-chaos absurd routes before gates are valid.
## Authority Atlas balance checks

The Authority Atlas adds many possible offices and actors, so balance must prevent both content spam and instant snowballing.

Validation expectations:

- Atlas decisions are staged by region and selected target; the player never sees every authority action at once.
- Historical offices require survey/state/local mandate work before granting rewards.
- Restoration subjects have autonomy and resistance logic; forced integration is faster but dangerous.
- Specialist schools use geography and concrete costs; they are not generic free division buttons.
- Nonhuman/sanctuary actors cannot be annexed, conscripted, or converted into normal manpower.
- High-chaos construct/living-monument units require Archive Integrity and expensive inputs.
- AI selects atlas entries based on host geography and route, not random availability.
