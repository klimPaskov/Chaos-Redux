# 020 Black Plague state status matrix

| State status | Entry condition direction | Exit condition direction | Decisions visible | Mapmode direction | Cleanup notes |
| --- | --- | --- | --- | --- | --- |
| Clean | No infection, no exposure, no recent cure marker. | Exposure from neighbor, port, troops, weapon strike, or prevention action. | Basic surveillance and preparation. | Neutral. | Clear stale Black Death flags if no exposure remains. |
| Prepared | Clean state with active prevention or national protection. | Threat exposure or expiry of preparation. | Maintain readiness, stockpile, port hygiene. | Subtle shield or prepared marker. | Preparation should decay or require maintenance. |
| Threatened | Neighbor, port, troop route, refugees, or rat border exposure. | Infection, preparation success, or exposure removed. | Border checks, port checks, medical buildup, troop restrictions. | Sickly border tint. | Remove threat if source state clears. |
| Infected | Active Black Death load. | Contained when load and spread pressure fall. | Quarantine, lockdown, field hospitals, army cordon, treatment, vector control. | Deep black-red disease tint. | Death ticks and spread checks active. |
| Contained | Infection present but spread suppressed. | Recovering, relapse, or lockdown failure. | Maintain cordon, reopen slowly, monitor relapse. | Disease tint with containment ring. | Death ticks lower, relapse checks active. |
| Recovering | Load falling and cure progress sufficient. | Cured or relapse. | Cleanup, local aid, infrastructure recovery. | Faded disease tint. | Remove harsh modifiers gradually. |
| Cured | Infection cleared, recovery memory remains. | Prepared, clean, or relapse if cleanup was rushed. | Prevention maintenance and recovery support. | Pale recovery marker then clears. | Remove state modifiers after recovery window. |
| Weaponized | Hit by deployment or accident exposure. | Infected, contained, or recovered after response. | Emergency containment, evidence, countermeasures, retaliation hooks. | Harsh black warning marker. | Link condemnation and source tracking. |
| Rat-held | Controlled by rat nation or King. | Retaken and cleaned by humans. | Human owner sees military containment nearby. Rat country gets warren actions. | Black fog and rat marker. | Disease persists until retaken and cleanup succeeds. |
