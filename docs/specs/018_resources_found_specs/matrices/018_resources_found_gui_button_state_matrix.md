# Event 018 Resources Found GUI Button State Matrix

All labels are working labels only. They are not final localisation.

| Button family | Hidden when | Locked when | Disabled when | Available when | Active state | Completed state |
| --- | --- | --- | --- | --- | --- | --- |
| Survey | no active field or Cave Host active | field not acknowledged | lacks civilian capacity or owner invalid | baseline or expanded field active | survey mission running | survey result applied |
| Extraction | no active field or sealed | public danger if extraction paused by emergency | lacks capacity, trains, or local support | field stable enough to work | extraction cooldown running | exploitation stage raised |
| Safety | no active field or sealed | no pressure yet | lacks support equipment or civilian capacity | pressure is visible | safety work active | safety stage improved |
| Concession | no foreign interest | diplomacy blocked by war or rival invalid | no valid interested country | interest exists and owner can negotiate | concession mission running | concession granted or refused |
| Border crisis | no border rival | border crisis already resolved | rival invalid or no contested border | pressure, rival, and field value align | crisis timer running | state transferred, settled, or cooled |
| Evacuation | no public danger | public danger not yet visible | lacks trains, trucks, manpower, or capacity | settlements at risk | evacuation mission active | population loss reduced |
| Hunt | no public danger | no cave attack stage | lacks divisions, equipment, or XP | public danger and military access | hunt mission active | incident reduced or failed |
| Closure | no strange incidents | closure not revealed yet | lacks resources, engineers, units, or evacuation | public danger or last window active | sealing active | field sealed or closure failed |
| Cave Host capacity | Host not active | Host card hidden | no captured resource state changed | Host controls valid resource states | refresh cooldown active | capacity updated |
| Human counter | Host not active | technology or decision family locked | lacks hard attack prep, industry, or equipment | Host nearby or world threat active | counter mission active | counter bonus or target pressure applied |

## Tooltip validation

| State | Tooltip must include |
| --- | --- |
| Locked | broad unlock source without hidden spoilers |
| Disabled | unmet costs and requirements in icon-first form |
| Available | cost, public effect direction, and risk direction |
| Active | timer, objective, target state, and failure direction |
| Completed | result and whether follow-up remains |
| Warning | why the action is risky and what visible harm may follow |
