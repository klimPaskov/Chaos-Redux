# British Tax: research notes and bibliography

## Scope and evidence labels

The universal taxation system is fictional alternate history. Historical sources below support presentation, period vocabulary, and quotation research. They do not establish that Britain historically imposed the worldwide mechanism described in these specs.

The local project archive and pinned repository sources support project integration. Documentation excerpts identify candidate engine facilities, not proof that those facilities have the required current runtime behaviour. Installed-game documentation, native modifier behaviour, and the mandatory tool workflows remain separate checks.

## Project evidence

**P01: supplied project archive.** `all-project-sources(20260922-060330).zip`, supplied for this task. All 22 top-level text files and all 20 subagent definitions extracted from the nested archive were read in full before the source specification was written. The companion reading ledger records each filename and SHA-256. Referenced files not contained in that archive are not covered by this claim.

**P02: existing Event 81 event script.** `events/081_england_tax.txt`, repository `klimPaskov/Chaos-Redux`, commit `879b3007d3b6bf75c726c11635473fccda45c569`. Full file inspected through the connected GitHub read. The old root sends a British event, excludes allies and enemies from its demand loop, applies a one-year tax idea on acceptance, gives immediate Political Power and stability-related outcomes, and gives Britain an optional annexation-goal response to refusal. This is the superseded implementation baseline, not the requested new design.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/events/081_england_tax.txt`

**P03: existing Event 81 idea.** `common/ideas/081_england_tax_ideas.txt` at the same commit. Full file inspected. It includes `consumer_goods_factor`, `extra_trade_to_target_factor`, `trade_cost_for_target_factor`, `cic_to_target_factor`, and `mic_to_target_factor` in the legacy setup. Their presence proves the existing implementation uses these names. It does not establish that the signs, scope, consumer-goods units, or independent-country transfers are correct for the redesigned system.

Source: `https://github.com/klimPaskov/Chaos-Redux/blob/879b3007d3b6bf75c726c11635473fccda45c569/common/ideas/081_england_tax_ideas.txt`

**P04: offline HOI4 modifier documentation.** Targeted excerpts from `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md` at the same commit were inspected through repository search. The documented targeted civilian and military modifiers allocate portions of industry to the target. The documented trade-cost modifier describes the target's cost of purchasing the modifier owner's resources. Therefore seller and buyer direction must be checked separately. The whole offline wiki document was not read in this session.

The legacy positive trade-cost entry on the taxpayer targeting ENG appears inconsistent with the intended cheap British purchase direction under that documented interpretation. Treat this as a supported diagnostic hypothesis pending installed-engine verification, not as a completed runtime fix.

**P05: catalog snapshots.** The supplied events, clusters, and scenarios CSV files were read in full. Event 81's events row is older and the Negative Economy cluster snapshot does not yet include the user's High member assignment. The explicit current brief takes precedence. The canonical workbook was not supplied or edited. CSV exports must not be edited directly.

## Historical and cultural research

### H01: Declaration of Independence, 1776

The United States National Archives provides the adopted document and transcript. Its grievances include an objection to taxes imposed without consent. This gives an accurately sourced historical voice for opposition to externally imposed taxation, not a statement about the fictional twentieth-century policy.

Verified short candidate, preserving the source's capitalisation: “For imposing Taxes on us without our Consent:”

Source: `https://www.archives.gov/milestone-documents/declaration-of-independence`

Status: relevant transcript passage read. Candidate only. Final super-event use and placement are not approved by this package. No additional quotations from this source are needed.

### H02: Stamp Act, 22 March 1765

The Yale Avalon Project transcribes the parliamentary act. The opening provisions describe a wide range of paper and legal transactions subject to duties and place the measure within a defence-related rationale. This is useful grounding for Britain's fictional expansion of taxable categories and the bureaucratic specificity of the humour.

Source: `https://avalon.law.yale.edu/18th_century/stamp_act_1765.asp`

Status: opening and selected provisions inspected, not a claim of reading every provision or related act. The historical measure concerned the specified colonial setting, not universal taxation of every country. No direct quotation is adopted.

### H03: McCulloch v. Maryland, 1819

The Cornell Legal Information Institute reproduces the reported case. The opinion text explicitly identifies Chief Justice Marshall before the later passage concerning destructive taxing power. Earlier passages include advocates' arguments and must not be misattributed to the Court.

Verified short candidate from Marshall's opinion: “the power to tax involves the power to destroy”.

Source: `https://www.law.cornell.edu/supremecourt/text/17/316`

Status: opinion attribution and the relevant passage verified. It concerns the constitutional relationship between state taxing power and a federal institution, not a historical judgement about British Tax. Its broader use would be a deliberate cultural analogy requiring contextual acceptance.

### H04: Bank of England archive record OV44/1

The Bank's catalogue describes a file concerning sterling and sterling-area policy, dated from 27 November 1939 to 22 December 1947. Its description mentions trade and payments agreements, sterling balances, and preparations for convertibility. These are useful research leads for period economic vocabulary.

Source: `https://www.bankofengland.co.uk/CalmView/Record.aspx?id=OV44%2F1&src=CalmView.Catalog`

Status: catalogue metadata read. The archival file itself was not accessed. No precise claim about financial transfers, colonial extraction, or a historical tax rate is derived from the catalogue description.

### H05: Irish legislation, 1938

The official Irish statute index lists the Finance (Agreement With United Kingdom) Act 1938 and the Agreement With United Kingdom (Capital Sum) Act 1938. This is a lead for research into negotiated economic settlements.

Source: `https://www.irishstatutebook.ie/eli/1938/act`

Status: the official index was read. Attempts to retrieve the full act pages failed. Their operative provisions and any historical settlement figures are not verified here and are not used as design facts.

### H06: ceremonial musical direction

A publisher and a recording label identify Elgar's Pomp and Circumstance March No. 1. The recording label's page identifies a particular organ performance and recording details. These support the work's existence as a concrete ceremonial audio candidate. They do not grant redistribution rights or establish the suitability of an unheard excerpt.

Primary publication and recording sources: `https://www.rundel.de/en/article/pomp_and_circumstance_no_1/MVSR0312` and `https://www.hyperion-records.co.uk/dw.asp?dc=W4356_GBAJY8825801`

Status: publisher and label search-result descriptions inspected. Audio not downloaded, listened to, licensed, clipped, or accepted. This is an audio research lead, not a final music selection. No lyric text is reproduced.

### H07: recording-rights research lead

The Library of Congress National Jukebox makes historical recordings available for listening and maintains separate rights and access information. A publicly playable recording still requires recording-specific rights review before redistribution in a mod.

Source: `https://www.loc.gov/collections/national-jukebox/about-this-collection/`

Status: collection description located. No individual recording has been cleared. A final audio researcher must obtain an appropriate source and document its actual licence or permission.

## Research decisions

Use the colonial-tax and constitutional-tax sources as distinct voices, not as interchangeable proof of the same historical event. Use the 1939-to-1947 archive catalogue only as a lead for period language. Keep the fictional international order distinct from Britain's actual historical institutions.

Final super-event title, button, description, main quotation selection, recording, timestamps, and rights remain open production work. Candidate words must not become localisation merely by being copied from this note. The asset and super-event prompts require those gates explicitly.

## Access date

External sources and the repository snapshot were inspected for this planning task on 22 September 2026. The pinned repository commit identifies the code actually inspected and does not claim to be a complete live checkout.
