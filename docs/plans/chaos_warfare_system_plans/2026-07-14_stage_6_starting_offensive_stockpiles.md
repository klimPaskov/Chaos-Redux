# Stage 6: Starting Offensive Chemical Stockpiles

Status: implemented as a bounded startup-history tranche; the overall Chaos Warfare goal remains incomplete

## Accepted design source

The `country_program_and_designer_matrix.md` starting offensive stockpile table is the controlling source. Its country values are relative program indices rather than literal equipment quantities. Startup grants use twelve strategic agent lots per index point so the opening reserves can support several preparations without removing the need for production, profile conversion, protection, or headquarters preparation.

This twelve-lot scale is gameplay tuning. The country ordering and program identities have useful historical grounding, but exact totals are low-confidence abstractions and must not be presented as archival inventory figures.

## Implemented mapping

| Country | Choking lots | Blister lots | Total lots | Opening identity |
| --- | ---: | ---: | ---: | --- |
| Britain | 1,200 | 840 | 2,040 | chlorine and phosgene reserve; mustard air profile |
| France | 1,080 | 840 | 1,920 | phosgene artillery profile; mustard air profile |
| Germany | 960 | 720 | 1,680 | chlorine and phosgene reserve; mustard delivery profiles |
| Soviet Union | 1,200 | 960 | 2,160 | large uneven reserve; mustard delivery profiles |
| United States | 360 | 840 | 1,200 | chlorine reserve with mustard and lewisite; lewisite delivery profiles |
| Italy | 480 | 360 | 840 | limited chlorine and mustard program |
| Japan | 480 | 420 | 900 | theater chlorine and mustard program |

The split inside a class preserves country identity while matching each accepted class index exactly. No country receives a starting nerve-agent lot. Biological project progress remains separate from chemical equipment stock.

## Runtime behavior

- The startup grant replaces legacy cylinder grants with exact `*_agent_lot_1` equipment.
- Each country receives a deterministic shell-filling and prepared-air profile after payload-logistics initialization.
- Stock remains national strategic material. It does not prove headquarters preparation, formation presence, policy authorization, a completed route, or exposure.
- Existing startup idempotence remains unchanged; the grant still runs only through the established global startup-history guard.

## Migration boundary

This tranche changes only new-game startup grants. It does not activate the legacy-cylinder migration effect. That migration remains without a caller until every old cylinder consumer has been retired or converted, preventing double conversion and mixed accounting.

## Validation evidence

- All seven country class totals reproduce the accepted matrix indices at twelve lots per point.
- Every granted equipment ID is registered in `script_enum_equipment_bonus_type` and defined in the strategic payload equipment file.
- Every profile uses an agent that the same country receives at startup.
- No startup grant adds nerve payload, use history, evidence, casualties, contamination, Condemnation, or readiness.

## Remaining Stage 6 work

Operational balance must still be tested against route payload costs, conversion losses, replacement production, and differentiated AI reserve targets. Legacy cylinder consumers and the idempotent migration caller remain unresolved and prevent Stage 6 closure.
