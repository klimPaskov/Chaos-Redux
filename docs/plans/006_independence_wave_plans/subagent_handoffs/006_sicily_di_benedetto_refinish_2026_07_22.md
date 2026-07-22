# IW-019 ASX Sicily — Di Benedetto refinish handoff

Date: 2026-07-22  
Producer package: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/sicily_di_benedetto_trial_01/`  
Status: `needs_user_review`

## What is ready

The unchanged Senate public-domain master is copied byte-for-byte, the explicit
face-visible crop is recorded, and a source-only `156x210` preview plus a style
comparison sheet are present. The crop keeps the civilian suit and tie exactly;
no military uniform or insignia has been invented.

Source master SHA-256: `EC033B2FCD0DC44441A57C93B12B8C9D64828CF72BD3DD2AD646D40480169553`  
Crop box: `(8,0,305,401)` from `314x401` source, yielding `297x401`  
Source crop SHA-256: `596393635FF9C0DC2511A4319B4583C2F33DA7C2A7488C81EEE386F941239617`  
Source-only `156x210` preview SHA-256: `0C7A9D51FA13A9AB27CCA02F3B09026851CA67D3F9DF7549C66AD4C1AED2AE18`

## What is intentionally pending

This sourced visual role is prohibited from generating or reconstructing a real
person, so it did not make the requested ImageGen edit. The included
`imagegen_prompt.md` is a handoff for an allowed generated-art producer: use the
exact crop as the sole identity reference, preserve face/age/pose/civilian
clothing, apply only a restrained HOI4-painted treatment, and output a separate
opaque `156x210` PNG. The result then needs independent identity/style review
before standard DDS conversion. No final DDS is present and no runtime/GFX/
gameplay file changed.

## Role and rights

Di Benedetto was born in Enna, Sicily (29 Jan 1866), had a senior Italian army
career, was alive in 1936, and has a Senate portrait recorded by Commons as PD
Italy and PD-1996/US. Career records place him at disposal/unemployed in the
1930s. The parent-approved wording is therefore “retired Sicilian general
recalled for the synchronized independence emergency,” not an active-1936
historical command claim. Preserve the Senate/Commons attribution and direct
source URL:

- https://commons.wikimedia.org/wiki/File:Senatore_Vincenzo_Di_Benedetto.gif
- https://upload.wikimedia.org/wikipedia/commons/3/32/Senatore_Vincenzo_Di_Benedetto.gif

Exact/variant ownership scans found no current Chaos Redux or installed vanilla
character/portrait owner. The full search roots and source metadata are in the
package manifest.

## Wiring handoff

If and only if the painted result passes audit, parent may use sprite
`GFX_portrait_ASX_independence_wave_sicily_army_commander` at
`gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_sicily_army_commander.dds`.
Keep this as a full large portrait only; no advisor, dossier, `_small`, navy, or
alternate sprite is authorized.

## Simplifications/blockers

- No generated finish or final DDS is included because this sourced subagent
  cannot generate/edit a real portrait.
- The civilian visual and retired-emergency role are intentional and must not
  be rewritten as a uniformed active 1936 command.
- The package is not runtime-complete until an allowed producer supplies and an
  independent audit accepts the painted result.
