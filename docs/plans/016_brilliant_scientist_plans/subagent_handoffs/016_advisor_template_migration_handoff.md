# Event 016 remaining advisor-template migration handoff

Date: 2026-07-29

## Scope and result

The fourteen Kruger advisor cards after Stage 0 were regenerated from their matching complete `156x210` leader or scientist portraits with the canonical advisor-template workflow. Runtime filenames and the fifteen existing `GFX_idea_doctor_warren_kruger_*` sprite identifiers remain unchanged. Stage 0 already used the approved workflow and was not regenerated in this tranche.

The migration covers Stage I, Stage II, and the six Stage III and six Stage IV route variants: alien revealed, clone, machine, synthesis, temporal, and xenobiological.

## Workflow contract

- Compositor: `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py`
- Compositor SHA-256: `0080C7BA20C7A19B50C49885B66B775C1967B2CAAAEDCB63230725CB3656E0B0`
- Canonical template: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png`
- Canonical template SHA-256: `8F594EF62AFBA6FDEC58DE66A80609350DCFE884320B11E6CB6220F1A0E19F58`
- Source handling: load the complete portrait, resize it to the native `65x67` advisor canvas, apply one uniform no-warp transform, and alpha-composite the untouched template once on top.
- Shared transform: rotation `-6`, offset `-1 -1` from template opening center `25 32.5`, final portrait center `24 31.5`, and sepia strength `0.18`.
- Standard transformed size: `33x46`.
- Clone transformed size: `36x50`.
- Temporal transformed size: `39x54`.

The two larger profiles retain the complete route-specific group composition while covering the frame opening. They are deliberate content-sensitive fits, not perspective warps or template changes.

## Output evidence

| Variant | Transform size | Processed PNG SHA-256 | Runtime DDS SHA-256 |
| --- | --- | --- | --- |
| `stage_1` | `33x46` | `6EC7CD0267BDAEE0783C9D0AAF0B6AADF513E95DDC0996C8C1AF455AB86A1467` | `055493B37F4AA2E586F46FB51C08B2C4316B4FD0669526173CB3CB34CECB17CD` |
| `stage_2` | `33x46` | `4AE1F5220E30870A2C59CA393A55FF9005C0B98D7418729CCF449A167AD8B284` | `6684F4A9D9F18FA37351B18AFC3F635B53579BC63F83548742FBB2620508521A` |
| `stage_3_alien_revealed` | `33x46` | `367DD276D95F9A780141041B21F64D0377F4BDB2F9C8F1DD5725057D5B1A6BEF` | `B4E829277E07FB997D3767FDDE0A9954E0207E95F39D73334AA7935BC2EC84A3` |
| `stage_3_clone` | `36x50` | `0BFADC711306F16659774AA76CEB276D69EC415B19AFE6218986E23132E3973B` | `C466B93C9341BA08815CC7A591FFD1C08553E240D464DE3BABF48F62F86BC2D3` |
| `stage_3_machine` | `33x46` | `0E0894D32C9A209AAC7272A535063CF785CA89434DDBAC3B793D99D3E7C70AF4` | `38E633551C111C56FD22A3A42182075993B2E0727659FC2BC0F5080E64895D25` |
| `stage_3_synthesis` | `33x46` | `6854064964A9C8121B3248F368579BEDBFC2C884D12F1713EC0CBD3F61A13497` | `ED739A6F610F54332F5BBF9CEA2A0A641A014982CD3C007C958BC1A8C28DEFDD` |
| `stage_3_temporal` | `39x54` | `2AA53A76E231A3B3FA9A19F139B6428E4C4FE1F4EF680533E489588A0041C331` | `C9966DE7EFA0F95BD359377D8D5379A41C143B6A250EE06B716252C1EFCE68FA` |
| `stage_3_xenobiological` | `33x46` | `4BFDFDF58CE7CA2D95A5C6A7C5C8F5C18532E3DB1AB9E1BA1FA33003BC65FE64` | `3D2EA1E0B763E95767C53D3A546D46850D09DE8CDCCB1557BF26D6C766BA6291` |
| `stage_4_alien_revealed` | `33x46` | `2B953B85C768743DE0F95DA77D5E1842BE35835285CBB65E0C2780E0C2975399` | `4D73656BC324100A623A85E2BE70036E039834355E50549290E27CD3C8A597E5` |
| `stage_4_clone` | `36x50` | `ED21DF6CE201B3EA502DB22289B16B01D8CD420C1F3BB41425500018040E018D` | `7A62D7F033BDF884DE91CCF2534F92BBCA7BBEDBA95D3C5FA8950C51E7A1E41F` |
| `stage_4_machine` | `33x46` | `4BE1D6C2CDFD2EA6D4ADAFC0B26FF971B02F809AD2110BE59CDAA861D794C4C5` | `6B7B3E551374938BD5D3D457E7757124A484DE93FE9D4A22222EA5F0406CB8D5` |
| `stage_4_synthesis` | `33x46` | `DC377904CD4BF011256E431F7C70DAB95774309EBF20916FA59BC5EDF8BA816A` | `38AA0C63749AF71472AE3D15EF979729398BE19C2445BD45F43887A50F617A28` |
| `stage_4_temporal` | `39x54` | `8D04D1DBC72018469FBD33D39D4BDD56359D67B66B2AAC9615E70AD012CB024C` | `771C81126B42340B2BCB5787B77A9FB9EDA7023ABA64976EBFA8CE9B34DE6BDD` |
| `stage_4_xenobiological` | `33x46` | `FF2B9F76A0E276A26EE68246DCC892C9B20EB82A706F4FA5AB79766A4DA0CFB5` | `1FE39A9890E8C19D70BE7A29970B9F5BE56E69B6AFFC1EE28070889A5C19AE09` |

The final contact sheet is `docs/assets/016_brilliant_scientist/contact_sheets/kruger_advisor_template_migration_final.png`. Each processed PNG is pixel-identical to its decoded runtime DDS. Every output is `65x67`, and all 897 fully opaque pixels in the canonical template remain exact in every card.

Independent batch review passed all fourteen cards for complete-source use, native readability, frame coverage, paper clearance, left rotation, route identity, exact template retention, alpha integrity, and coherent progression. The reviewer required no artistic correction. The review did identify fourteen obsolete per-card JSON attestations from the removed processor; those records were deleted and replaced by `docs/assets/016_brilliant_scientist/advisor_candidates/metadata/kruger_advisor_template_migration.json`, which records the current processor, template, transforms, source hashes, PNG hashes, DDS hashes, and acceptance evidence.

## Scope boundary

Repository inventory found eighteen additional live `65x67` advisor cards: sixteen Utopia Manifesto cards and two New Zealand fallout cards. Their metadata explicitly identified the removed advisor processor, so the repository-wide continuation migrated them through the same canonical template workflow. Their evidence is recorded in `docs/plans/gfx_icon_flag_mapmode_cleanup_plans/advisor_template_runtime_migration_2026_07_29.md`.

Final gameplay state selection remains parent-owned. This handoff proves runtime asset presence, stable sprite registration, canonical template composition, and visual review; it does not claim that every later gameplay transition already selects the corresponding sprite.
