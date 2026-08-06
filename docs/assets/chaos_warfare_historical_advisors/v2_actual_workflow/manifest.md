# Chaos Warfare Historical Advisor Cards: Actual Workflow Manifest

Status: `complete` for the advisor-card asset and wiring gate; the wider CBRN goal remains separate.

This package supersedes the earlier advisor-card evidence for production and review purposes. The source portraits are the accepted existing Chaos Redux 156x210 scientist portraits; this pass does not alter their identity, source files, or large-portrait consumers.

## Accepted reference and consumer

- Canonical advisor family: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/`.
- Canonical top layer: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png`.
- Template SHA-256: `8F594EF62AFBA6FDEC58DE66A80609350DCFE884320B11E6CB6220F1A0E19F58`.
- Native canvas: `65x67` RGBA/32-bit BGRA DDS with one mip level.
- Review canvas: `260x268` nearest-neighbour 4x PNG.
- Live sprite registration: `interface/cbrn_historical_advisors.gfx`.
- Live consumer: `common/characters/cbrn_historical_specialists.txt`.
- Live card directory: `gfx/interface/advisors/cbrn/`.
- Political-advisor consumers use `portraits.civilian.small`; theorist consumers use `portraits.army.small`; the existing full scientist portrait remains `portraits.army.large`.

## Exact production workflow

Each card used the complete existing 156x210 source portrait without a new crop, decoded it to a durable PNG for evidence, and then ran `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py`. The compositor first resizes the complete source to the native 65x67 intermediate, applies the task-specific transform, and composites the untouched canonical template as the final top layer.

The common transform is `--portrait-size 44 57 --rotation 0 --portrait-offset -2 3 --sepia-strength 0.18`. `USA_ira_baldwin` uses the same transform with `--portrait-offset -8 3` to keep the face clear of the paper tab.

The processed PNG was then independently converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 65 --height 67` into both the staged candidate and the live runtime path. The compositor-generated DDS was not treated as the final conversion step.

Representative command:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py `
    --source gfx/leaders/scientists/portrait_AST_howard_florey.dds `
    --template .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png `
    --portrait-size 44 57 `
    --portrait-offset -2 3 `
    --rotation 0 `
    --sepia-strength 0.18 `
    --preview docs/assets/chaos_warfare_historical_advisors/v2_actual_workflow/processed/AST_howard_florey.png `
    --review-preview docs/assets/chaos_warfare_historical_advisors/v2_actual_workflow/review_4x/AST_howard_florey_4x.png `
    --output docs/assets/chaos_warfare_historical_advisors/v2_actual_workflow/runtime_candidate/AST_howard_florey.dds
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py `
    --input docs/assets/chaos_warfare_historical_advisors/v2_actual_workflow/processed/AST_howard_florey.png `
    --output gfx/interface/advisors/cbrn/AST_howard_florey.dds `
    --width 65 --height 67
```

## Per-card provenance and hashes

The `source_png` files are decoded evidence copies of the live scientist DDS files, not alternate or replacement identity sources. The processed PNG and runtime DDS were generated in this v2 pass.

| Character | Source DDS SHA-256 | Decoded source PNG SHA-256 | Offset | Processed PNG SHA-256 | Runtime DDS SHA-256 | Runtime bytes |
| --- | --- | --- | --- | --- | --- | ---: |
| AST_howard_florey | `98DC7C95278658A08820E1AAB6465283574D694E57DE568D6F80D05303A127E2` | `3B68B9B95F68179B433FDE48AA7122614D66C151C95C4DC5F0A0134138707CE7` | `-2, 3` | `459DCA57B3518287BB8FBC53E2B1D190F3237A791E72F4B8A2762F72530CF407` | `704636AB0C564E26648BDFDAA65EC5B514581D1F81DD2F7EF3E372F7F520EB18` | 17548 |
| ENG_paul_fildes | `5BAF538B7EB09733E2387424C18885C5C854C9BD926DCCE8A020E8B9457AF1E5` | `925F997937539FC6A13BD9C8CF1F6099F4C409471A368A978E56B8CD0C5D9233` | `-2, 3` | `A44B58639141A2C98C39AF258C040175EF8657CF3ED9BC8023EAF510F12F3A0C` | `6B5277411A4CFA9B7B01A857D1532D1918012D8577F54F3B17B7D357DA4CD0A1` | 17548 |
| ENG_alexander_fleming | `A4EC2E9656C029DC01843D0D659DAA72EFE666477D9A88D9F366D679577CDD44` | `6929362F309159CEBE431DAF330C557EE68F8F3912F6A214C615F8146FFDB1FA` | `-2, 3` | `F939F1658159DC39C568C77FDD4B6B70E5C74DAEC2ECF8D9A03AD9CCB49DD6B5` | `AAB2E1D591E21D792884642FF6AB8FB3D9D44B42E7F6240B67B37296D7BCB2FA` | 17548 |
| GER_gerhard_schrader | `08E168B09D16F6A8B972F6EE9A873C283AA13356C0E7FC02AA0533107DD95AF6` | `BDEB158121B893C7308497350484870333136AACC38C208FEDBFD4DE2AE885A4` | `-2, 3` | `BA065FABB166FF9FE3C128A6BA56434DD1F1EF840E0AAAD471852C56ECB9447D` | `0FF48A8F2B5C3616BD6AC80E8332339C38C96BA5CB3F2CFE1A34F0303FB0965F` | 17548 |
| GER_kurt_blome | `02BA623450B7645114E9473CE8490C558D35C10DAD802A85F2ABF10C5D7FB4E2` | `E40C0AAEA441A6407082064389EC69E774E68528F0734F4FCFDCB2081A1DE9F5` | `-2, 3` | `ABD2B07D4876F42998D485C1BB0682E199A94A54308F39CDFE9D4DF9D9A734F0` | `2B73F9AE2035E15FEAAB013787B3E2DB9E55E4CC729B8B2984D8668C4F99067F` | 17548 |
| JAP_shiro_ishii | `BA806C1BA5C12CFD8C79E5E207F96501B704BC2022F44CBB40296EF74588A985` | `AAFB0B1E42DE77BE98E5A2F73FEBCC1C5D53704E5329790822657262FF98630C` | `-2, 3` | `7EC7DDBA5F3FE9E4578F016DBA6CD606CD07B6A85F3DD451F722468176309AB6` | `C1B569035D4B3B983650EDCA9DF2F07EF8233AB1EC6302F55DD9AF39A84DC3DB` | 17548 |
| JAP_masaji_kitano | `AB11D4D4AB13BFD906F76F63B7C68B078A52AF1EA4FDF292EC130CB7440A4421` | `6F701DA0EA9A85500E47F87EDD7633E12E4509386915CEAA0DB8D5F97648DAA9` | `-2, 3` | `32C61FB9ACBBE0E8B5D060DAB307A4E6E642F8C48D3A64EBD28A313573C3AFD8` | `8979817E2DF0B27241C40E9BAD8919C8967441947BF02C853F92DC1D29E7046F` | 17548 |
| POL_franciszek_witaszek | `720BC822C3C8AE285573A0267FBCF2AEA1B2A19BA5B698635FC9BAA7A48A6670` | `EEBBDF2A54D15D762FC30BBAECCC3CA7F8EE04D7ADB3C1E688DF98FD30B5AEB0` | `-2, 3` | `2E85A293FE61CF3DCBC6CA9BFEC3443FA20593843B2F4593F10959B7CE8F095C` | `82C5F7C29D633215168F2B1DAB607E1FA75B9B3F334B967610074A12BC38502C` | 17548 |
| SOV_grigory_mairanovsky | `A6B219A9CDE2A93CA76030A69A74DC135F606F7A187DAB85C47F65E282F28038` | `5F670BECC6E17926F20FF8A353FCE992FDF621E027AA9FE6622408ACB57CCB0F` | `-2, 3` | `F67EDB26EC0BAADBFC68A15597420AD045360129D515D67C4264D33C4261E3D1` | `9CB94B0DABC5C6C3FCEC0090F463842C00AD643921D9907A04B1FE674187AA73` | 17548 |
| SOV_ivan_mikhailovich_velikanov | `053752E40A48C28AD69780A8F229EA233D6EDA05BE9C2ABCEC6DF01194315445` | `6A0039B966278FDC6830AC3C32740FDAA07EC7685592EC723521D9D90454F5D4` | `-2, 3` | `59F4FA0B272019BFCECA2CC5BD1D5ED2DBB7DE3D65B2D16EB7E60DE57B8C7A3A` | `BAC849715B3790F8EB66A4B8A6145EB980AFF32771F44A2EF42CE6580AFEF039` | 17548 |
| USA_frank_olson | `898520BE5692A36956DC5EBFD8E3638ABEDED4C3A7B48D9175AB9F95AB426FEB` | `721A2C6F71623D8818F0367EEE97F51565AB3007F10611961D33D6B138CB8279` | `-2, 3` | `91F8272634D706B6B686D9D7B18D0CCE050CAABC0D8541AAAC55577CE5AF469A` | `DE1B3587655DEDEF8879E49F1DF2EE3A839963E197FC59222249676936B6EEFF` | 17548 |
| USA_ira_baldwin | `9EA3896726D4748B4E6FD7B90FDAF876D8281A0036AA6230E0E4CBA4AB36EDC2` | `A906E844786BB074768247C6DA99EF3B3B744B8939BD243739080C6AA18553F7` | `-8, 3` | `8C349277D35E149C78C95AD43B386D8878E25FE3018A0E56A789D38942E11EEB` | `DCFBF680BF4E9B6B9C9FA86A50F5342D78C29D7C4FA2D2E133DFCD998C05DB34` | 17548 |

## Review evidence and gate

- Native source contact sheet: `review/source_contact_sheet.png`.
- Native card contact sheet: `review/native_cards_contact_sheet.png`.
- Independent visual review: `review/independent_visual_review.md`.
- Native card previews: `processed/*.png`.
- Nearest-neighbour 4x previews: `review_4x/*_4x.png`.
- Legacy-versus-v2 comparison: `review/legacy_v1_4x_comparison_contact_sheet.png`.
- Automated source-decoding equality: all twelve source PNGs equal their source DDS pixels.
- Automated DDS round-trip equality: all twelve runtime candidates equal their processed PNG pixels.
- Automated alpha check: all four native outer corners are transparent on all twelve cards.
- Independent visual review: `review/independent_visual_review.md` records the parent integration review as a separate reviewer from the production session and passes all twelve cards at native and nearest-neighbour 4x scale.

No generic advisor icon, direct 156x210 runtime, plain 50x67 resize, cross-type substitute, or existing Chaos Redux icon is used.
