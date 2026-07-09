# Achievement Prompt for Event 018 Resources Found

Use existing Chaos Redux achievement patterns. Use this prompt together with the main spec and asset prompt. All titles are working labels only and not final localisation.

## Achievement list

| Working label | Visibility | Eligible route | Unlock conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| Boom Without Blood | visible | owner | Maintain a high-richness field, complete safety missions, keep worker deaths below strict threshold, never enter public danger. | public monster attack, field closure before richness threshold, Cave Host emergence | medium | bright resource seam with intact helmet |
| Resource Curse | visible | owner or challenger | A resource field border crisis ends with the discovery state transferred. | ordinary conquest unrelated to the event | medium | split border over ore vein |
| Close the Mouth | hidden | owner prevention | During public danger, close or collapse the site before Evolution IV. | Cave Host emerges | hard | sealed cave mouth with resource glow behind it |
| Surveyors Came Back Wrong | hidden | owner containment | Reach sickness stage, complete medical and safety chain, then stabilize without Cave Host. | public attack stage or closure before sickness resolved | hard | corroded tools and medical emblem |
| Hard Attack Solves Geology | visible | anti-Host war | Defeat Cave Host after fielding or using strong hard attack, anti-tank, heavy artillery, or equivalent anti-armor preparation. | Cave Host world-end | hard | anti-tank shell against stone hide |
| Starve the Deep | hidden | anti-Host war | Keep Cave Host below a low non-origin resource capacity for a long period, then defeat or contain it. | allowing Cave Host to exceed capacity threshold | very hard | empty mineral vein and chained cave mouth |
| The Mine Owns the Map | hidden | Cave Host route | As Cave Host or with player control allowed, control a defined number of resource-rich states and complete a late hunger or continental lane. | world-end can either be required or separate, implementation chooses and documents | very hard | claw over resource map without text |
| Continental Maw | secret | world-end | Trigger Cave Host world-end scenario through continental control at chaos over 1000. | none beyond ordinary achievement system rules | very hard | cracked continent with cave mouths |
| All That Glitters | visible | ordinary repeatable mastery | Have several Event 018 discoveries across different resource types without any one reaching public danger. | Cave Host emergence | medium | six resource motifs around a survey seal |
| Paid in Concessions | visible | diplomacy | Use multiple foreign concessions or trade deals on a resource field without losing the state or becoming a subject. | state lost, puppet or subject status caused by concession chain | medium | contract and resource crate |
| The Last Shift Came Home | hidden | humanitarian | During public danger, complete evacuation and safety missions with low civilian deaths. | evacuation mission failure, high death threshold | hard | miners leaving lit shaft |
| Sealed Riches | hidden | sacrifice | Close an Evolution III all-resource field before breach, losing the deposit. | Cave Host emergence or keeping site open beyond final threshold | hard | sealed vault with multiple resource colors |

## Tracking notes

The implementation should track:

- event-added field richness
- discovered resource types count across campaign
- worker deaths and civilian deaths from Event 018
- public danger entered
- site closure phase
- Cave Host spawned
- Cave Host defeated
- Cave Host non-origin capacity high watermark
- field state transferred by event border crisis
- concessions accepted and owner subject status
- evacuation mission success and failure
- world-end trigger
- player control or achievement eligibility for Cave Host

## Asset notes

Each achievement needs a completed 64x64 icon. Do not reuse focus icons or idea icons by resizing. Create achievement-specific icons and variants according to the asset skill.
