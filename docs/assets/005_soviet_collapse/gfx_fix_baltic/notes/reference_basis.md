# Visual Reference and Flag Basis

## Canonical focus references

The canonical reference contact sheet was inspected before individual files. The reference family is `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/national_focus/contact_sheet.png`; its matching `CATALOG.md` entries identify `focus_aus_danubian_socialist_communes.png`, `focus_aus_defence_of_the_homeland.png`, and `focus_generic_population_growth.png` as Vanilla HOI4 assets at 100x88. Those files were then inspected individually for aged painterly shading, medallion treatment, readable central subjects, and transparent margins. They were used only as style and composition references, never as final art.

The contact sheets for `visual_components/focus_pieces/` and `visual_components/focus_backgrounds/` were inspected. Their catalog rows are `reference`, not layer assets; no component layer was used in the generated icons.

## Installed vanilla focus precedent

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/goals.gfx` registers `GFX_goal_generic_major_alliance` at `gfx/interface/goals/goal_generic_major_alliance.dds`. The installed DDS is 89x79 with alpha range 0–255 and SHA-256 `240bccf204d533acfa0918a51557ec84f5a8af14bd531d8c4a7d2b0a8fba591c`; a review-only decoded copy is `notes/vanilla_major_alliance_preview.png`. This precedent informed the aged alliance-medallion treatment. New and repaired outputs follow the parent’s explicit nominal 94x86 target.

## Flag geometry used in ImageGen prompts

- Estonia: the President of Estonia’s official symbols page defines equal horizontal blue, black, and white bands, with a flag ratio of 11:7: [Estonian State Flag](https://president.ee/en/republic-of-estonia/symbols/index.html).
- Latvia: the official law defines carmine, white, carmine horizontal bands in a 2:1:2 height ratio: [Law on the National Flag of Latvia](https://likumi.lv/ta/en/en/id/200642-law-on-the-national-flag-of-latvia).
- Lithuania: the official state-flag law defines three equal horizontal bands, yellow, green, red: [Lithuanian State Flag law](https://www.e-tar.lt/rs/legalact/TAR.07CAE5E6C2B3/).

The selected restoration pact and Pan-Baltic war-room sources use those stripe orders; the other generated icons omit national flags.
