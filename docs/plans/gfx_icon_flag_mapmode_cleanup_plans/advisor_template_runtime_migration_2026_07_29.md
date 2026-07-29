# Canonical advisor-template runtime migration

Date: 2026-07-29

## Result

Every live `65x67` advisor DDS that repository evidence tied to the removed advisor compositor has been regenerated with `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py`. The migration covers fourteen later-stage Doctor Warren Kruger cards, sixteen Utopia Manifesto cards, and two New Zealand fallout cards. The Kruger Stage 0 card already used the canonical workflow and was retained unchanged.

No sprite name, texture path, character token, or gameplay consumer changed. Each complete source portrait is resized to the native `65x67` canvas before one uniform no-warp transform. The unchanged canonical `advisor_template.png` is then composited once as the top layer.

The shared transform is rotation `-6`, offset `-1 -1` from opening center `25 32.5`, and sepia strength `0.18`. Utopia Manifesto and New Zealand fallout cards use transformed size `33x46`. Kruger cards use `33x46`, except clone cards at `36x50` and temporal cards at `39x54`.

## Runtime inventory

| Family | Migrated cards | Runtime location |
| --- | ---: | --- |
| Event 016 later Kruger stages | 14 | `gfx/interface/ideas/016_brilliant_scientist/` |
| Event 015 Utopia Manifesto advisors | 16 | `gfx/leaders/015_utopia_manifesto/advisors/` |
| Fallout New Zealand advisors | 2 | `gfx/interface/ideas/fallout_world_end/nzl_lifeboat_state/` |

The Event 016 per-card hash table is in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_advisor_template_migration_handoff.md`.

## Utopia Manifesto and New Zealand evidence

| Asset | Source SHA-256 | Processed PNG SHA-256 | Runtime DDS SHA-256 |
| --- | --- | --- | --- |
| `advisor_utopia_manifesto_advocate_of_limits` | `E37BC27F4ADC4AED66025956010BD62046143868466FEB3F884896EAD04A56E5` | `1F0C1686B5F53B9159F3734AC560A9B8E713B46ACD0B1A8F7F492FB6E6C57943` | `5AE45EE6AE3ECCA7E84E39AD6A85BACDED37B53EC90B3D187AF67D8C3443CAB6` |
| `advisor_utopia_manifesto_chief_surveyor` | `9633069E743CEF1993362C4A1BC5DD9E61985562F4002688DE7B54F6E60D3F16` | `ED77CCBDDF41694FE704A8744F69ED621DDD55B0DD1EA1527A52F1EF1ACEB6BB` | `4566357DB726ECFC327A71A708DD547F5A3FDCBFB04A303A20AE8596521564F9` |
| `advisor_utopia_manifesto_civic_engineer` | `8B9C9371D91A28B9EEFE5B086DB47B6BFFBC8DA817ED600C1932093558AEACFD` | `995E6A3D1AB3E169C9D44DFC8099711487F49AE47F4020159438F640DD6FA15C` | `9A244ADD1E6B713F3E640BE36A93B53BD408843BBB746D88DC9F0BD631B63690` |
| `advisor_utopia_manifesto_constitutional_jurist` | `5D8E13887457940F758504BF8278CA11D1E21BD277260F732C7F9DCD0A13ECEE` | `89AC5B833EFA9B7ACC8BE2EA1439DAAC2B5EE0AEBF78C1B6F47304E132E409D8` | `2E9C732607D9D4F23D5ED941D723267A96D9E7D6117232F0F46F9F8CFC140C6B` |
| `advisor_utopia_manifesto_contract_broker` | `47A6FCD8C754541BDFB9545B6A8ED385281C07B7D5EDC9FADA05B39465F6B4EC` | `751971A3958A285AFD79D1B1F635CC63DDB9EDF845E5A5ABB5A7E6CE1A0C6D8E` | `52C02152AEA137B2F3F9DCF064CD0B46F36DE8F4D40C7AFA48E71409A18DC584` |
| `advisor_utopia_manifesto_council_organizer` | `FCCD45FC6EC4D3D7235450E66E82BA04F0117B242BD04B75EEA23970482A120D` | `8E06FB0BB7A490D489CB77A66FCD9C7C1E2585432EB596C09361763D5033A4D9` | `1FAC9F28F228509BF3BB94BA93D21127DF70FEF83BA6A7DBEB836A16F04268FC` |
| `advisor_utopia_manifesto_general_provisioner` | `2DDBA39E48EC5466A157F8E17A74BB12652784D89BC769D968D9F972CC28E1BE` | `4C0639F30F9B9527C69A8C9D3B909A3DDD378881186C83C2E5B8B29EE6DE9E41` | `424D83FD11EFC749790DCEC7B21F7EF62B592E387EB3C8A99BD160F019C53D50` |
| `advisor_utopia_manifesto_interpreter` | `D12C737834D2D41A61D17AC29C336F48620A54393BB99B11535231AA8C87490D` | `9DA68958D35E4EF1674F6B649910D8B8F8298E534BEB8417D975F2CCBF347076` | `FC01B486D60425FE338B3045CC39C149E94FCD6CA9E6080FB88C3C2E9AC65603` |
| `advisor_utopia_manifesto_keeper_of_stores` | `D3ED67B2CAB194AA3861B18574DBBCD431D49144E943CC2520D802843923B27A` | `CDF5E44FBA1AFFD737DD6BEEBE62EAD5034EC3573B0C8CBAFAA0833FA233C6B2` | `FC2F54A7496B2ADF975112964429D8D258BECDD346A0AA0E85EF893E4A1BCCBD` |
| `advisor_utopia_manifesto_league_envoy` | `45716F0CB67D9FCF6346301DF90DCD40E0E16C297A2E8F75AF5D5923153FB202` | `1D5A9563F6B9874364B32F4A4B777A36D15B6DBEF72617BEC0A5C185AB25936E` | `E5797E8FCA18DE0745D93EE7D66686DD0E6B476167E5A7F295A22A526F87E754` |
| `advisor_utopia_manifesto_public_auditor` | `5D85F24155713055F1C90F8AC6EA47A77CA7C4F966BE7A996A418469AFD4567C` | `916787E362664B53A23E354897777945CDBC975429166559F032F7D4576B1E0D` | `3557AC5C9504CDB5FF0FDB6537B176395678A7B9CAD6DEF7CA86178A2D33B987` |
| `advisor_utopia_manifesto_secretary_of_callings` | `DEF97BE91DFD0321FB38754BEE215251CFBCAF30880FAE36CE4315F3470C7118` | `3601D38BABF6DA61057E4771086FB77058470CA0A8B3CBCD725F5F0F273086DC` | `EBDA812BC51894430F6A3F2BBC78FE042346464BC2800DF34388731419E39977` |
| `advisor_utopia_manifesto_social_workshop_planner` | `B281A4F5DEABDB4C4A8AC1C680E6969407E2A54FCC423BDBB01A9E7EAB97EA7B` | `1A959C90CF797AF70F4A649677E78D1F82D43E670E159A3D5530D22877A227E4` | `3AEBBCE3468D55EBFB464B8DB1D89AAEEBF785589FC228A0C985C1C7E8B4F587` |
| `advisor_utopia_manifesto_standards_engineer` | `6E47964E015120A41FCC9EC2C6CDF4FD235D6ED7BC862194144C9175F6F0CA43` | `FB07E84EB8E396AB18D3834265E8556F40FFCECDCC2617822B0D94527A0F3EDE` | `37361737DC894CA940B97B3E686F59AC6DCBBD00999E9D36B4E192F0BFCE4BED` |
| `advisor_utopia_manifesto_steward_of_service` | `404932D2CBF73A14022B8811E9B74EC74A8043764B86B58C313A4D005D5BD43B` | `C363234AF29B99B82EFA71CF7CD383574C19CEBD2B5764BEA546302CC87A5AAF` | `B177B578CD04504979FB421804E5CB55C5E1C26A4C933CB5595BB40E721C2D8D` |
| `advisor_utopia_manifesto_surveyor_of_shores` | `522D57CCDF3122B358A493601EA9E039D4B800ABF8544AA8D40B19220D920466` | `6A562361DF32786CFFED55C4833EB6552B109521D9B652816442DCEF3B3BC770` | `7225DFEE17D8864259ABAE55A4D7BD83BD3F90C536F1474FB129837E88FA086A` |
| `NZL_fallout_dairy_relief_commissioner` | `8ACE0A57F2C071AAF82CC1F1B2CA8EB17FBF1D20F8D0869B794C68A866DCA08D` | `A0E4985D7D8950B2898ED077D8A95589CC0985B818022AD1CC9B01F128788E1D` | `9174A695B9A14EB87BD780C6535ED8F2E565DDBB141F92C9B10297FEBCD3452F` |
| `NZL_fallout_storm_port_engineer` | `DE19A5CFEE608EA9AE3E160EFC2E8F05E5420EE4B66D5C8EC688315C0120D8AC` | `E2C592F7D6D6F80A01A76ABC9635E8A0EABDDCE6B4B49289A0F3FB700D59BD7D` | `FB5C7BF0F14568B7428979E12838C8797EFCA417F8C01FC80FE0C43310FCDCCD` |

## Validation

All thirty-two migrated PNGs are pixel-identical to their decoded runtime DDS files. Every output is `65x67`, every DDS is a one-level 32-bit BGRA texture, and all 897 fully opaque canonical-template pixels remain exact in every card. The Utopia package mirrors under `final_dds/advisors/` and `decoded_png/advisors/` match the migrated runtime files.

The combined Utopia and New Zealand contact sheet is `docs/assets/advisor_template_migration_remaining_18_contact_sheet.png`, SHA-256 `E4A6EB392CC68894ABC37593ED3A67F89C8892E6F861B1766E33DF241F7619DD`. Independent review passed all eighteen cards with no artistic or placement correction. The reviewer confirmed native readability, zero opening gaps, zero exterior portrait spill, paper clearance, visible left rotation, retained identity, exact template and alpha integrity, and coherent family presentation.

## Supersession

The removed compositor’s per-card metadata and approvals are historical provenance, not current artifact attestations. Those records were moved into explicitly superseded history directories. Current metadata, validation, approval, contact sheets, and hashes point to the canonical template compositor and the pixels above. Earlier workflow descriptions that require separate generated frame and paper overlays are superseded for the current runtime advisor cards.
