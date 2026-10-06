# Event 097 Collaboration: Research Notes

These notes collect the engine facts and historical anchors that shaped the Event 097 design. They are design inputs, not player-facing text. Every claim is tied to a cited source or marked as uncertain.

## Engine facts from the offline wiki snapshot

The installed vanilla game and its `documentation/` folder are not available in the planning environment. The offline Paradox wiki snapshot under `paradox_wiki/` was read instead. The implementation agent must confirm every item below against the installed vanilla documentation and precedents before relying on it.

| Topic | Source section | Fact used by the design |
| --- | --- | --- |
| `add_collaboration` | `Effects - Hearts of Iron 4 Wiki.md`, diplomacy table, lines 1246 and 1320 to 1327 | Country scope with `target = <country>` and `value = <0-1>`. The wiki describes it as adding collaboration in the target country with the scoped country. The scoped country is therefore the beneficiary and the target is the host whose people collaborate. |
| `set_collaboration` | same table, line 1247 | Sets an absolute value. The design never uses it for ordinary layers because it would erase collaboration earned through vanilla intelligence operations. |
| `has_collaboration` trigger | `Triggers - Hearts of Iron 4 Wiki.md`, line 642 | Country scope, `target` plus `value` with `<` or `>`. The wiki notes that the target is occupied by the current scope. Whether the trigger reads a meaningful value when the host is not occupied is uncertain. The design only reads pair values in occupation contexts (state capture, Fifth Column, capitulation). |
| `has_collaboration` game variable | `Data structures - Hearts of Iron 4 Wiki.md`, line 1512 | Described as the collaboration of the target within its cores occupied by the current country. The wording is ambiguous and must be verified before any display or arithmetic depends on it. |
| Surrender limit | `Defines - Hearts of Iron 4 Wiki.md`, line 480 | `SURRENDER_LIMIT_REDUCTION_PER_COLLABORATION = 0.3`: each percent of collaboration lowers the surrender limit by 0.3 percent. Whether the reduction is relative or in absolute points is uncertain. |
| Capitulation recipient | same, line 481 | `SURRENDER_RECIPIENT_SCORE_PER_COLLABORATION = 1.0`: countries with collaboration get a bonus when the engine chooses which enemy receives a capitulation. |
| Compliance at capitulation | same, line 482 | `COMPLIANCE_PER_COLLABORATION = 1.0`: each percent of collaboration becomes one point of compliance at capitulation. |
| Initial capture compliance | same, line 493 | `INITIAL_STATE_COMPLIANCE = 0.0`. Collaboration does not raise compliance on ordinary pre-capitulation captures, which is why Evolution II needs an event-owned capture hook. |
| Compliance and resistance | same, lines 494 to 531 | Compliance growth, decay toward a stable value, resistance target reduction of `-0.5` per compliance point, and peace-cost discounts tied to compliance. |
| State effects | `Effects - Hearts of Iron 4 Wiki.md`, lines 3728 to 3744 | `add_compliance`, `set_compliance`, `add_resistance`, `add_resistance_target` with removable `id` and `occupied` country, `remove_resistance_target`, and `add_state_resistance_compliance_modifier`. |
| Occupation triggers | `Triggers - Hearts of Iron 4 Wiki.md`, lines 1158 to 1161 and 2006 to 2016 | `core_compliance`, `core_resistance`, `has_core_occupation_modifier`, state `compliance`, `resistance`. |
| Capitulation triggers | same, lines 1087 to 1090 | `surrender_progress`, `has_capitulated`, `days_since_capitulated`. |
| Modifiers | `List of modifiers - Hearts of Iron 4 Wiki.md`, lines 328 to 394 | `surrender_limit`, `starting_compliance`, `compliance_gain`, `compliance_growth`, `compliance_growth_on_our_occupied_states`, `resistance_target`, `resistance_target_on_our_occupied_states`, and the `operation_collaboration_government_*` operation modifiers. |
| On actions | `On actions - Hearts of Iron 4 Wiki.md`, lines 250 to 260 and 450 | `on_capitulation` and `on_capitulation_immediate` (ROOT capitulated, FROM winner), `on_state_control_changed` (ROOT new controller, FROM old controller, FROM.FROM state), `on_war_relation_added`, `on_peace`, `on_annex`, `on_puppet` (peace conference only), `on_government_exiled`, `on_exile_government_reinstated`. |
| Collaboration governments | `Effects - Hearts of Iron 4 Wiki.md`, line 4723 | Vanilla scripted effect `instantiate_collaboration_government` creates a collaboration government with the current scope as overlord. The target is read from the `country_to_initiate` temporary variable. |
| Ideology rule | `Ideology modding - Hearts of Iron 4 Wiki.md`, lines 44 and 73 | `can_create_collaboration_government` and `can_collaborate` ideology rules. |
| Autonomy | `Autonomy state modding - Hearts of Iron 4 Wiki.md`, line 39 | `can_create_collaboration_government` exists as an autonomy-state rule. |
| Naming | `Localisation - Hearts of Iron 4 Wiki.md`, line 258 | Collaboration governments use names such as `$OVERLORDADJ$ $NONIDEOLOGY$` through `COUNTRY_autonomy_collaboration_government`. |

### Player-visible vanilla behavior from secondary sources

The following points come from player guides, not from installed files. They describe the vanilla collaboration-government decision and must be verified in the installed `common/decisions/` files before implementation.

- An occupier can form a collaboration government once average compliance in the occupied cores of a country reaches 80 percent ([Nerds and Scoundrels guide](https://www.nerdsandscoundrels.com/hoi4-collaboration-government/)). Several other player guides returned by web search repeat the same threshold, but only this page was opened.
- Democratic governments cannot form collaboration governments in vanilla (same guide).
- The collaboration government receives the cores of its occupied states and resistance no longer applies there (same guide).
- Player discussion reports that the vanilla decision lives in `common/decisions/foreign_influence.txt`, costs nothing, and is always taken by AI ([Paradox forum thread title in search results](https://forum.paradoxplaza.com/forum/threads/a-way-and-a-mod-to-fix-collaboration-government-spam.1355579/)). The thread body could not be loaded, so the file name and AI claim are uncertain.
- The La Résistance operation Prepare Collaboration Government lowers the target's surrender limit and sets compliance at capitulation according to collaboration. This point comes from a web-search summary that listed a [PC Invasion article](https://www.pcinvasion.com/?p=210073) among its results. The article itself was not opened, and the point agrees with the define descriptions above.
- The console command `collaboration <value>` adds collaboration against a selected country ([hoi4commands entry](https://hoi4commands.com/command/collaboration)). This is useful for implementation testing only and disables achievements.

### Engine uncertainties carried into the specification

1. Whether `add_collaboration` accepts negative values. Several counterplay actions in the specification require a reduction. The implementation must verify this and report a blocker instead of substituting another mechanic.
2. Whether `has_collaboration` returns a meaningful value outside occupation.
3. Whether the surrender-limit reduction is relative or absolute.
4. Whether `instantiate_collaboration_government` honors the ideology rule. Evolution IV opens the route to every ideology, so a democratic installer may hit an engine refusal.
5. Whether the collaboration value and the vanilla collaboration-government decision require La Résistance. Compliance and resistance were part of the 1.9 free update, but the exact DLC boundary of collaboration display and creation must be confirmed.
6. Whether a state-scope effect exists that changes control without ownership (`set_state_controller` or an equivalent) for the Open Gates incident.
7. Which state trigger reliably detects friendly divisions present in a state.

## Historical anchors

The event is fictional and global. It never claims that real collaborators existed in a given country during the campaign. Historical precedents were used to choose the shape of each evolution, the vocabulary of the text direction, and the visual motifs for assets.

### The fifth column

During the Nationalist advance on Madrid in October 1936, General Emilio Mola was reported to have spoken of four columns outside the city and a fifth inside it, meaning sympathizers waiting behind the lines. Web-search summaries of the [phrases.org.uk entry](https://www.phrases.org.uk/meanings/fifth-column.html), the [Wikipedia article on Emilio Mola](https://en.wikipedia.org/wiki/Emilio_Mola), and the [UC San Diego Spanish Civil War collection](https://libraries.ucsd.edu/speccoll/visfront/espionaje.html) agree on this outline and date an American newspaper use of the phrase to 14 October 1936. The pages were not opened, and the exact wording and occasion of Mola's remark are disputed, so final text must not quote him without the super-event research workflow.

Design use: Evolution III takes its name and behavior from this idea. The column appears when the front approaches, and it matters most where the defender is already close to collapse.

### Administrations prepared before conquest

On 1 December 1939, one day after the Red Army entered Finland, the Soviet Union proclaimed the Finnish Democratic Republic at Terijoki under Otto Kuusinen. Kuusinen and Molotov signed a mutual assistance agreement in Moscow on 2 December. The regime was created to govern Finland after a Soviet conquest, gained no recognition beyond the Soviet Union, and was dissolved into the Karelo-Finnish SSR on 12 March 1940 after the Moscow Peace Treaty ([Finnish Democratic Republic on Wikipedia](https://en.wikipedia.org/wiki/Finnish_Democratic_Republic), opened and checked). A related [FRUS telegram](https://history.state.gov/historicaldocuments/frus1933-39/d797) appeared in search results and was not opened.

Design use: Evolution II and Evolution IV draw on the idea of a government that exists before the territory it claims. The Terijoki case also shows the failure mode. A prepared government collapses when the war does not deliver the territory, which informs the Abandoned stage of the installed-administration lifecycle.

### Local committees formed as troops arrived

In occupied China from 1937, Japanese units worked with local committees, often described as peace maintenance or public safety committees, that took over district administration as towns fell. A web-search summary of the [FRUS 1938 volume III text](https://search.library.wisc.edu/digital/AVDSBL2EUX3DVC8O/text/ANJJDOA36AS4RU8E) reports a Peace Maintenance Commission installed in Canton on 20 December 1938. Timothy Brook's study [Collaboration: Japanese Agents and Local Elites in Wartime China](https://readings.com.au/product/9780674023987/9780674023987) is the standard scholarly treatment of these local committees. Neither page was opened in this planning pass, so dates and names are marked uncertain until the implementation research pass verifies them. Search summaries also mention local auxiliary forces raised in captured areas under names such as Peace Preservation Corps.

Design use: Evolution II seats a prepared administration the moment a state changes hands. The installed-administration package raises local auxiliaries instead of regular divisions.

### Civil services that stayed in place

After the Dutch government left for London in May 1940, the secretaries-general of the ministries became the highest-ranking officials in the occupied Netherlands under the German Reichskommissar. The page opened from Joods Monument states that the system of government remained intact, that only a few senior officials were replaced, and that more than three hundred mayors and other officials, including police commissioners and public prosecutors, were replaced over time ([Joods Monument on the civil administration](https://www.joodsmonument.nl/en/page/657/civil-administration)). Web-search summaries of other sources, including the [Wikipedia overview of collaboration](https://en.wikipedia.org/wiki/Collaboration_with_Nazi_Germany_and_Fascist_Italy), describe the secretaries-general as following a policy of cautious cooperation. Those pages were not opened, so that characterization is marked uncertain.

Design use: Evolution I describes networks that reach civil administration, police, industry, and military bureaucracy. The design treats these as sectors of one network instead of separate counters.

### Sensitivity boundary

Historical collaboration regimes took part in deportations, forced labor, and mass murder. The event must not present collaboration as harmless, comic, or heroic. Minor-event irony is allowed in option direction, but it must condemn the speaker or expose cynicism. It must never joke about victims. Real collaborator names must not appear in player-facing text, and no real person is generated or depicted in event art.

## Source list

- Offline wiki pages under `paradox_wiki/`: Effects, Triggers, Data structures, Defines, List of modifiers, On actions, Ideology modding, Autonomy state modding, Localisation.
- [Emilio Mola, Wikipedia](https://en.wikipedia.org/wiki/Emilio_Mola)
- [Fifth column, phrases.org.uk](https://www.phrases.org.uk/meanings/fifth-column.html)
- [Spanish Civil War espionage, UC San Diego Library](https://libraries.ucsd.edu/speccoll/visfront/espionaje.html)
- [Finnish Democratic Republic, Wikipedia](https://en.wikipedia.org/wiki/Finnish_Democratic_Republic)
- [FRUS 1933-1939, telegram 760i.61/147](https://history.state.gov/historicaldocuments/frus1933-39/d797)
- [FRUS 1938 volume III, digital text](https://search.library.wisc.edu/digital/AVDSBL2EUX3DVC8O/text/ANJJDOA36AS4RU8E)
- [Timothy Brook, Collaboration, Harvard University Press listing](https://readings.com.au/product/9780674023987/9780674023987)
- [Civil administration, Joods Monument](https://www.joodsmonument.nl/en/page/657/civil-administration)
- [Collaboration with Nazi Germany and Fascist Italy, Wikipedia](https://en.wikipedia.org/wiki/Collaboration_with_Nazi_Germany_and_Fascist_Italy)
- [HOI4 collaboration government guide, Nerds and Scoundrels](https://www.nerdsandscoundrels.com/hoi4-collaboration-government/)
- [Collaboration console command, hoi4commands](https://hoi4commands.com/command/collaboration)
- [Paradox forum thread on collaboration-government spam](https://forum.paradoxplaza.com/forum/threads/a-way-and-a-mod-to-fix-collaboration-government-spam.1355579/) (body not retrieved)
