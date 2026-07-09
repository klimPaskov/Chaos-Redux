# Infantry Spawn template and unit family matrix

All labels are working labels and not final localisation.

## Spawn family matrix

| Phase | Family | Unit identity | Strength band | Weirdness | Equipment fill | Strain cost | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | Local rifle company | weak infantry | low | low | low | low | most common result |
| Baseline | Territorial militia | weak defense | low | low | low | low | more common in low stability |
| Baseline | Rural cavalry screen | cavalry patrol | low medium | low | low medium | low | wide rural areas |
| Baseline | Field gun detachment | infantry with artillery | medium | low | low | medium | industrial or wartime weight |
| Baseline | Support cadre | infantry with one support | medium | low | medium | medium | capitals and depots |
| Evolution I | Mustered infantry regiment | organized line | medium | low | medium | medium | stronger baseline |
| Evolution I | Reserve cavalry regiment | mobile reserve | medium | low | medium | low medium | good for minors |
| Evolution I | Artillery-backed regiment | line artillery | medium high | low | medium | high | stronger but supply-heavy |
| Evolution II | Serious infantry | larger line division | high | low medium | medium high | medium high | at-war weight |
| Evolution II | Motorized column | motorized infantry | high | medium | medium | high | fuel and trucks matter |
| Evolution II | Mechanized cadre | mechanized | high | medium | low medium | high | can appear without tech |
| Evolution II | Tank detachment | armor | high | medium | low medium | very high | rare and costly |
| Evolution II | Armored car patrol | scout or suppression | medium | medium | medium | medium | occupation and wide states |
| Evolution II | Helicopter-only oddity | absurd specialist | variable | high | low | high | only if unit exists in mod |
| Evolution III | Broken fragment | one or two battalions | very low | high | variable | low | worst case on-demand result |
| Evolution III | Usable oddity | mixed small division | medium | high | variable | medium | common crisis result |
| Evolution III | Serious accidental force | large mixed division | high | high | variable | high | lucky and risky |
| Evolution III | Absurd machine | huge strange template | very high | extreme | variable | extreme | rare and dangerous |
| Evolution IV | Base zombie unit | base zombie only | profile-based | chaos | manpower-based | leakage | trainable after authorization |
| Evolution IV | Ghost division | spawn-only ghost | profile-based | chaos | special | leakage | no Death country mechanics |
| Evolution IV | Golem division | spawn-only golem | profile-based | chaos | special | leakage | slow and defensive |
| Evolution IV | Future chaos family | registry-defined | registry | registry | registry | registry | add through registry only |

## Random battalion pool direction

The implementation should include vanilla base battalions and support companies where the mod supports them safely. The pool should include infantry, cavalry, camels, bicycles, motorized, mechanized, light armor, medium armor, heavy armor if present, amphibious armor, flame armor, armored cars, artillery, rocket artillery, anti-air, anti-tank, marines, mountaineers, paratroopers, and all base support companies that can be added without invalid templates.

## Quality roll factors

| Factor | Raises quality | Raises weirdness |
| --- | --- | --- |
| Country at war | yes | slightly |
| High army XP | yes | no |
| Strong industry | yes | no |
| High supply strain | no | yes |
| High command confusion | no | yes |
| High roster backlog | no | yes |
| High formation absurdity | no | strongly |
| High chaos value | partly | strongly |
| Prior reckless on-demand use | no | strongly |
| Successful organization decisions | yes | lowers |
| Possessed general concession | yes short-term | raises later |

## Equipment and training bands

| Band | Use |
| --- | --- |
| Bare | Broken fragments, bad militia, high absurdity |
| Partial | Ordinary baseline and many random units |
| Serviceable | Evolution I organized units and wartime countries |
| Strong | rare lucky outcomes and high-war-state countries |
| Impossible | units with equipment not researched, never a production unlock by itself |
