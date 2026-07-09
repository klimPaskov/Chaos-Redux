# 012 Africa Charter League target mechanics matrix

| Target state | Entry condition | Main values | Available actions | Exit condition | Cleanup notes |
| --- | --- | --- | --- | --- | --- |
| Observed | African-capital country, African subject, colonial African state, restored polity, or civil-war side becomes visible | confidence baseline, rival appeal | invitation, observe, defense offer | invited, protected, lost | clear if target dies or leaves Africa scope |
| Invited | unifier sends Charter League invitation | confidence, autonomy demand, rival appeal | accept, delay, conditional acceptance, refuse | member, protected, refused, rival | remove invitation flags after answer or timeout |
| Protected | target receives defensive guarantee or aid | confidence, influence, local support | deliver aid, send volunteers, defend capital | member, failed protection, lost | cancel defense missions after war or target death |
| Member | country is inside League | confidence, influence, autonomy demand, rival appeal | aid, shared reserves, federal work, subject pressure | federal candidate, subject candidate, exit, rival | keep display values until stable route chosen |
| Federal candidate | high confidence and route permission | confidence, autonomy demand, regional stage | accession vote, service project, autonomy settlement | federal member, delayed, refused | remove candidate missions after accession or refusal |
| Subject candidate | influence high and route allows pressure | influence, autonomy demand, rival appeal | associated state, protectorate, resource protectorate | subject, revolt, rival appeal | clear pressure flags after subject route chosen |
| Coerced target | route permits force and target resists | influence, resistance, rival appeal | ultimatum, military governor, annexation project | annexed, revolt, rival bloc | raise regional resistance and run cleanup after war |
| Rival member | target joins rival African bloc | rival appeal, confidence, bloc strength | reconciliation, cold war, war | reconciled, defeated, stable rival | remove League member actions unless negotiating |
| Lost target | invalid or closed target | none | none | possible future observation | remove all missions, target flags, and selected target markers |
