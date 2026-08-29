# Event 35 Great Depression 2.0 research notes

## Research purpose

The research supports mechanic structure, recovery philosophies, contagion, relapse, and political consequences. It does not turn Event 35 into a literal simulation of one country between 1929 and 1939.

The historical record shows several interacting failure channels and several policy responses. Their effects varied by country, timing, institutions, debt, trade, and political conditions. The specification therefore treats each recovery doctrine as conditional. No doctrine is written as universally correct.

Research was checked on 2026-08-27.

## Banking panic, credit contraction, and deflation

Federal Reserve History describes the Great Depression as a sequence of stock-market, regional banking, national banking, and international financial crises. Its account of the 1930 to 1931 banking panics explains that deflation pushed banks, firms, and debtors toward bankruptcy, reduced consumption, increased unemployment, and transmitted pressure internationally through the gold standard.

Design use:

- Credit and banking stress is a hidden Severity component.
- Bank panic is a visible incident, not the whole event.
- Debt, demand, and unemployment reinforce each other.
- A bank holiday can stop a panic but imposes a short disruption.
- Reopening and reform require proof that institutions are viable.

Sources:

- Federal Reserve History, `Banking Panics of 1930-31`: https://www.federalreservehistory.org/essays/banking-panics-1930-31
- Federal Reserve History, `The Great Depression`: https://www.federalreservehistory.org/essays/great-depression
- Federal Reserve History, `Banking Panics of 1931-33`: https://www.federalreservehistory.org/essays/banking-panics-1931-33

## Bank holiday, recapitalization, and durable reform

The Emergency Banking Act followed a nationwide bank holiday and created a process for reopening institutions judged sound. The Banking Act of 1933 separated commercial and investment banking functions and created federal deposit insurance. These measures support a distinction between immediate panic containment, recapitalization, and longer institutional reform.

Design use:

- Finance and Trade uses a staged route.
- Temporary closure can lower panic while reducing short-term output.
- Audit and recapitalization precede a durable guarantee.
- Repeated rescue without reform creates fiscal pressure and rescue dependence.

Sources:

- Federal Reserve History, `Emergency Banking Act of 1933`: https://www.federalreservehistory.org/essays/emergency-banking-act-of-1933
- Federal Reserve History, `Banking Act of 1933 (Glass-Steagall)`: https://www.federalreservehistory.org/essays/glass-steagall-act
- Federal Reserve History, `Banking Act of 1935`: https://www.federalreservehistory.org/essays/banking-act-of-1935

## Public works and employment relief

The National Archives records that FERA distributed federal relief and employed more than 20 million people by the end of 1935. The WPA and related agencies provided jobs through public projects. The National Industrial Recovery Act also linked recovery, public works, purchasing power, unemployment relief, industrial organization, and labor standards.

Design use:

- Public works commits current civilian capacity instead of granting free construction.
- Employment affects demand and social pressure as well as infrastructure.
- Projects need local targets and lasting conversion.
- Too many projects create fiscal and logistics strain.
- Relief without structural work slows deterioration but does not complete recovery.

Sources:

- US National Archives, `Family Experiences and New Deal Relief`: https://www.archives.gov/publications/prologue/2012/fall/fera.html
- US National Archives, `Records of the Work Projects Administration`: https://www.archives.gov/research/guide-fed-records/groups/069.html
- US National Archives, `National Industrial Recovery Act`: https://www.archives.gov/milestone-documents/national-industrial-recovery-act

## International contagion

NBER research on 1931 describes a crisis beginning in Austria, striking several European countries, forcing Britain off the gold standard, and spreading across the Atlantic. Other NBER work finds that interbank links transmitted liquidity shocks and amplified lending contraction. IMF historical work also describes the 1931 crisis as a chain of contagious financial failures.

Design use:

- Financial Contagion follows proven relationships.
- Strong subject, creditor, market, faction, and event-created support links matter more than generic proximity.
- Secondary countries receive lighter exposure first.
- Propagation depth reduces pressure.
- The same source-target link cannot convert a country repeatedly.
- Coordinated rescue, ring-fencing, diversification, and abandonment are distinct actions.

Sources:

- NBER, `Transatlantic Contagion During the Financial Crisis of 1931`: https://www.nber.org/system/files/working_papers/w17437/revisions/w17437.rev0.pdf
- NBER, `Interbank Connections, Contagion and Bank Distress in the Great Depression`: https://www.nber.org/system/files/working_papers/w25897/w25897.pdf
- NBER, `Network Contagion and Interbank Amplification during the Great Depression`: https://www.nber.org/system/files/working_papers/w22074/w22074.pdf
- IMF eLibrary, `Learning Lessons from Previous Crises`: https://www.elibrary.imf.org/display/book/9781513514277/ch002.xml

## Gold, trade, protection, and economic blocs

Historical accounts connect fixed exchange-rate commitments, deflation, interest-rate pressure, trade contraction, protectionism, and retaliatory policy. The design cannot reproduce gold convertibility or exchange rates directly in HOI4. It can represent external constraint through trade access, convoys, credit relationships, clearing agreements, capital controls, and economic blocs.

Design use:

- Trade and external-finance stress is hidden inside Severity.
- The player sees material causes such as blocked imports or failed clearing.
- Protectionist blocs can defend members while weakening global recovery.
- Currency or debt actions use event effects and relationships without claiming an exchange-rate simulation.

Sources:

- Federal Reserve History, `Stock Market Crash of 1929`: https://www.federalreservehistory.org/essays/stock-market-crash-of-1929
- NBER, `International Policy Coordination: The Long View`: https://conference.nber.org/confer/2011/MECf11/eichengreen.pdf
- IMF, `Sovereign Debt and Financial Crises: An Historical Analysis`: https://www.imf.org/en/publications/fandd/issues/2018/03/debroeck

## Debt, austerity, restructuring, and default

World Bank historical work reports that countries which interrupted debt service often recovered more quickly than countries that resisted default, while also warning that policy packages and causality complicate simple comparisons. The interwar debt network amplified crisis through common exposure, foreign-currency obligations, and weak international coordination.

Design use:

- Austerity is viable under strong institutions and moderate Severity.
- Austerity can worsen unemployment and Social Collapse.
- Debt restructuring or standstill can lower fiscal and credit pressure at a diplomatic or access cost.
- Market clearing and default are not automatic victories.
- International debt conferences belong in Evolution III.

Sources:

- World Bank, `The Interwar Debt Crisis and Its Aftermath`: https://documents.worldbank.org/curated/en/980571468142185470/pdf/multi-page.pdf
- World Bank, `Dealing with Debt`: https://documents1.worldbank.org/curated/en/374721468765628202/pdf/multi0page.pdf
- IMF, `Sovereign Debt and Financial Crises: An Historical Analysis`: https://www.imf.org/en/publications/fandd/issues/2018/03/debroeck

## Relapse and premature withdrawal

The US recovery was interrupted by the sharp 1937 to 1938 recession. Federal Reserve History records major declines in output and industrial production and a renewed rise in unemployment.

Design use:

- Stabilization is not the same as recovery.
- Support withdrawn before the proof period can cause relapse.
- The full opening shock does not repeat during an ordinary relapse.
- Policy whiplash and a new material shock can restore severe pressure.

Source:

- Federal Reserve History, `Recession of 1937-38`: https://www.federalreservehistory.org/essays/recession-of-1937-38

## Political extremism and social conflict

NBER and other historical research connects economic contraction, unemployment, bank failure, and austerity with support for political extremism in specific institutional and regional contexts. The relationship is not automatic and varies with prior ideology, propaganda, institutions, and local exposure. ILO material from the period discusses mass unemployment, public employment, social protection, and political fear around unemployment.

Design use:

- Social Collapse needs prolonged Severity, weak stability, organized movements, and failed response.
- One high Severity check cannot change ideology or start civil war.
- Existing parties, movements, military institutions, and regional identities shape the outcome.
- Employment, negotiation, social insurance, repression, and emergency government have different consequences.

Sources:

- NBER, `Austerity and the Rise of the Nazi Party`: https://www.nber.org/system/files/working_papers/w24106/revisions/w24106.rev1.pdf
- NBER, `Economic History and Contemporary Challenges to Globalization`: https://www.nber.org/system/files/working_papers/w25364/w25364.pdf
- ILO, `The Social Effects of the Economic Depression in North America`: https://researchrepository.ilo.org/view/pdfCoverPage?download=true&filePid=13100822780002676&instCode=41ILO_INST
- ILO, `The ILO involvement in economic and social policies in the 1930s`: https://www.ilo.org/media/333826/download

## War demand and recovery

Federal Reserve History notes that full output and employment in the United States returned during the Second World War. This does not mean war is a universal recovery button. War demand can employ idle plants while blockade, bombing, resource shortage, and civilian displacement worsen other parts of the crisis.

Design use:

- War-demand relief is conditional.
- Secure military orders can protect strategic centers.
- Losing ports, fuel, resources, or industrial states reverses the benefit.
- Peace can create a postwar demand shock when the economy depends on armament orders.

Source:

- Federal Reserve History, `The Great Depression`: https://www.federalreservehistory.org/essays/great-depression

## Social protection and public employment

ILO historical material describes a shift toward unemployment insurance, employment services, and public works as persistent mass unemployment changed public policy. Later ILO reviews explain public works as a long-standing unemployment response and distinguish direct employment from wider demand effects.

Design use:

- Social relief can reduce instability and demand collapse.
- Public employment is a doctrine with costs, capacity limits, and lasting institutions.
- Social insurance can become a recovery legacy.
- Relief remains distinct from factory reopening and finance.

Sources:

- ILO, `The Social Effects of the Economic Depression in North America`: https://researchrepository.ilo.org/view/pdfCoverPage?download=true&filePid=13100822780002676&instCode=41ILO_INST
- ILO, `Employment and Unemployment: Government Policies since 1950`: https://researchrepository.ilo.org/view/pdfCoverPage?download=true&filePid=13116698920002676&instCode=41ILO_INST
- ILO, `An ILO for All Seasons`: https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_dialogue/%40actrav/documents/publication/wcms_749391.pdf

## Design cautions

- Historical policy outcomes varied by country and timing.
- The event should not equate one ideology with one mechanically correct route.
- Financial systems in HOI4 are abstract. The design uses observable proxies and event-created relationships.
- Economic depression is not physical factory destruction on day one.
- Political radicalization needs institutions and movements, not a random ideology roll.
- Public works, bank reform, austerity, planning, and market restructuring all need costs and failure states.
- Evolution III should create worldwide contraction without forcing identical national crises.
