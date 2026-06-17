# 012 Africa idea icon handoff

Date: `2026-06-17`
Scope: regenerate the bounded Event 012 Africa idea and national-spirit icon batch with transparent backgrounds only

## Outputs

- `/home/klim/projects/chaos_redux/gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds`
- `/home/klim/projects/chaos_redux/gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds`
- `/home/klim/projects/chaos_redux/gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds`
- `/home/klim/projects/chaos_redux/gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds`

Evidence package:

- `/home/klim/projects/chaos_redux/docs/assets/012_africa/icon_regen_ideas_batch_conflict_chaos/manifest.md`
- `/home/klim/projects/chaos_redux/docs/assets/012_africa/icon_regen_ideas_batch_conflict_chaos/source_png/`
- `/home/klim/projects/chaos_redux/docs/assets/012_africa/icon_regen_ideas_batch_conflict_chaos/processed_png/`
- `/home/klim/projects/chaos_redux/docs/assets/012_africa/icon_regen_ideas_batch_conflict_chaos/contact_sheets/`

## Method

- Inspected `/home/klim/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas` before generation.
- Generated four separate idea-icon source artworks with image generation rather than reusing or shrinking goal icons.
- Copied original generated PNGs into the evidence package as source artifacts.
- Cleaned baked checkerboard background tones from the generated PNGs, then trimmed, centered, resized to `64x64`, and converted to DDS with alpha preserved.
- Did not edit `.gfx`, scripts, localisation, goals, or any idea icon outside this batch.

## Validation

- All four final DDS files exist and read as `64x64`.
- Processed PNG and DDS corner pixels are fully transparent for all four icons.
- Checker/dark contact sheet: `/home/klim/projects/chaos_redux/docs/assets/012_africa/icon_regen_ideas_batch_conflict_chaos/contact_sheets/idea_icons_checker_dark_contact.png`
- Goal-vs-new-idea comparison sheet for the overlap-risk pair: `/home/klim/projects/chaos_redux/docs/assets/012_africa/icon_regen_ideas_batch_conflict_chaos/contact_sheets/goal_vs_new_idea_compare.png`

## Notes

- The image generator did not return true-alpha PNGs even with transparent prompts. The delivered checkerboard was removed during processing by keying only the two background tones used in the generated source PNGs. Final processed PNGs and DDS outputs have real alpha.
- `idea_africa_high_chaos_bestiary` was intentionally redesigned away from the matching goal icon composition.
- `idea_africa_high_chaos_actor` uses a supernatural nonhuman mask and crown to keep the spirit explicitly fictional.
- No git staging or commit work was performed.
