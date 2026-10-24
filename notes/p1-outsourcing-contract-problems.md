# Outsourcing, KPI & Contract Problems — Full Solutions
These are the **exact problems** from the course file *"KPIs, outsourcing and contract problems word copy.docx"* 📘 (Que 1 to Que 13, with the file's own numbering; note that the file uses "Que 4" twice). The file gives the questions only, so every answer below is a worked model answer. Where a question needs data that is not given (probabilities, ratings, weights), the assumption is stated in **bold** first: in the exam, state your assumptions the same way and you get full credit. Turn on **Self-test** (press `T`) to hide the answers.

Theory for all of these is on [Outsourcing, Contracts & Partnerships](ch01-outsourcing-contracts.md).

---

## Que 1. Vendor Selection — ABC Electronics (PCB assembly) ⭐⭐⭐
ABC Electronics wants to outsource PCB assembly. Four vendors have been shortlisted. Ratings are out of 10.

| Criteria | Weight | Vendor A | Vendor B | Vendor C | Vendor D |
|---|---|---|---|---|---|
| Cost | 30 | 8 | 9 | 7 | 6 |
| Quality | 25 | 7 | 8 | 9 | 9 |
| Delivery | 20 | 9 | 7 | 8 | 8 |
| Technology | 15 | 8 | 8 | 9 | 7 |
| Sustainability | 10 | 6 | 9 | 8 | 8 |

**Q1.1 Calculate the weighted score of each vendor.**
Weighted score = Σ (weight × rating) ÷ 100.

| Criteria (weight) | A | B | C | D |
|---|---|---|---|---|
| Cost (30) | 30×8 = 240 | 30×9 = 270 | 30×7 = 210 | 30×6 = 180 |
| Quality (25) | 25×7 = 175 | 25×8 = 200 | 25×9 = 225 | 25×9 = 225 |
| Delivery (20) | 20×9 = 180 | 20×7 = 140 | 20×8 = 160 | 20×8 = 160 |
| Technology (15) | 15×8 = 120 | 15×8 = 120 | 15×9 = 135 | 15×7 = 105 |
| Sustainability (10) | 10×6 = 60 | 10×9 = 90 | 10×8 = 80 | 10×8 = 80 |
| **Total (out of 1000)** | **775** | **820** | **810** | **750** |
| **Weighted score (out of 10)** | **7.75** | **8.20** | **8.10** | **7.50** |

**Q1.2 Rank the vendors.**
1st **Vendor B (8.20)**, 2nd Vendor C (8.10), 3rd Vendor A (7.75), 4th Vendor D (7.50).

**Q1.3 Which vendor should be selected?**
**Vendor B.** It has the best cost rating (9) on the heaviest criterion, strong quality (8) and the best sustainability (9). The margin over C is small (0.10), so before signing, verify B's quality claims with a pilot lot and a site audit, and keep C as the backup/second source.

**Q1.4 If the sustainability weight increases to 25%, does the ranking change?**
Sustainability rises from 10 to 25 (+15 points), so the other weights must fall by 15 points in total to keep 100. Two common ways:

*Method 1 — reduce the other four proportionally* (each × 75/90): Cost 25, Quality 20.83, Delivery 16.67, Technology 12.5, Sustainability 25.

| Vendor | Calculation | Score |
|---|---|---|
| A | 25×8 + 20.83×7 + 16.67×9 + 12.5×8 + 25×6 = 200 + 145.8 + 150 + 100 + 150 | **7.46** |
| B | 25×9 + 20.83×8 + 16.67×7 + 12.5×8 + 25×9 = 225 + 166.7 + 116.7 + 100 + 225 | **8.33** |
| C | 25×7 + 20.83×9 + 16.67×8 + 12.5×9 + 25×8 = 175 + 187.5 + 133.3 + 112.5 + 200 | **8.08** |
| D | 25×6 + 20.83×9 + 16.67×8 + 12.5×7 + 25×8 = 150 + 187.5 + 133.3 + 87.5 + 200 | **7.58** |

New ranking: **B (8.33) > C (8.08) > D (7.58) > A (7.46)**. B stays first; **A and D swap** places because A has the weakest sustainability rating (6).

*Method 2 — take the 15 points from Cost* (Cost 15, Quality 25, Delivery 20, Technology 15, Sustainability 25): A = 7.45, B = 8.20, **C = 8.25**, D = 7.80. Now **C overtakes B** and D again beats A.

**Conclusion:** Yes, the ranking changes. The top choice is sensitive to how the extra weight is funded; B wins if all other criteria are scaled down, C wins if the weight comes out of cost. A, the least sustainable vendor, falls to last either way. This is why a sensitivity analysis belongs in every vendor-selection answer.

---

## Que 2. Outsourcing Risk Analysis — pharmaceutical packaging abroad ⭐⭐⭐
Risks: IP leakage, quality failure, delayed shipment, regulatory non-compliance, currency fluctuation, labour strike.

**Q2.1 Prepare a Risk Matrix using Probability × Impact.**
**Assumption: 1–5 scales (1 = very low, 5 = very high), rated for pharma packaging in a lower-cost country.**

| Risk | Probability (1–5) | Impact (1–5) | Score P×I | Rating |
|---|---|---|---|---|
| Quality failure (wrong label, mix-up, contamination, seal failure) | 3 | 5 | **15** | High |
| Regulatory non-compliance (GMP, US FDA/EU GMP, serialisation) | 3 | 5 | **15** | High |
| IP leakage (formulation, artwork, packaging design) | 3 | 4 | **12** | Medium-high |
| Delayed shipment | 4 | 3 | **12** | Medium-high |
| Currency fluctuation | 4 | 2 | 8 | Medium |
| Labour strike | 2 | 3 | 6 | Low |

Heat-map view (Impact across, Probability down):

| P \ I | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | | | | | |
| **4** | | Currency (8) | Delay (12) | | |
| **3** | | | | IP leakage (12) | Quality (15), Regulatory (15) |
| **2** | | | Strike (6) | | |
| **1** | | | | | |

**Q2.2 Identify the top three risks.**
1. **Quality failure** (15) — a packaging mix-up in pharma causes recalls and patient harm.
2. **Regulatory non-compliance** (15) — a GMP warning letter or import alert can stop all supply to a market.
3. **IP leakage / delayed shipment** (12 each) — joint third; for a patented drug rank IP leakage third, for a generic rank delay third.

**Q2.3 Suggest mitigation strategies.**
| Risk | Mitigation |
|---|---|
| Quality failure | Supplier qualification and GMP audit before award; quality agreement; AQL sampling and batch release by your QA; line clearance and vision systems; CAPA process; pilot lots |
| Regulatory non-compliance | Choose a site already approved by US FDA / EU / WHO-GMP / CDSCO; regulatory warranty; audit rights; serialisation and track-and-trace compliance (DSCSA, EU FMD) |
| IP leakage | NDA, IP ownership and indemnity clauses; share only what is needed (split artwork/data); restricted access; legal protection in that country; audits |
| Delayed shipment | Safety stock; dual sourcing; delivery SLA with LDs; visibility (ASN, tracking); buffer lead time; freight contract with priority |
| Currency fluctuation | Price in INR/USD; currency adjustment band; forward contracts/natural hedging |
| Labour strike | Business continuity plan; second site; force-majeure definitions that exclude supplier's own labour disputes |

**Q2.4 Which risks should be transferred through contractual clauses?**
- **Quality failure** → quality agreement, warranty, rejection/replacement at supplier's cost, recall-cost indemnity, liquidated damages.
- **Regulatory non-compliance** → compliance warranty and indemnity for fines/recalls, right to terminate for cause.
- **IP leakage** → NDA, IP clause, indemnity, injunctive relief, audit rights.
- **Delayed shipment** → delivery SLA with **liquidated damages** and service credits.
- **Currency** → currency clause (fixed currency or sharing band), or transfer financially through hedging.
- **Labour strike** → cannot be fully transferred: if it is the supplier's own labour dispute, exclude it from force majeure so the supplier remains liable; otherwise mitigate operationally (dual sourcing).

---

## Que 3. SLA Design — outsourced e-commerce warehouse ⭐⭐⭐
**Q3.1 Design an SLA covering order accuracy, order fulfilment time, inventory accuracy, customer complaints, warehouse safety and damage rate; for each give target, measurement method, penalty and incentive.**
**Assumptions: monthly measurement, fee-based contract; penalties and incentives as service credits on the monthly management fee, capped at 10% of the fee.**

| KPI | Definition / formula | Target | Measurement method | Penalty (service credit) | Incentive |
|---|---|---|---|---|---|
| **Order accuracy** | Orders shipped with correct SKU, quantity and address ÷ total orders × 100 | ≥ 99.5% | WMS scan-verified pick/pack data + customer-reported mis-ships; monthly | 1% of monthly fee for each 0.1% below 99.5%; supplier bears re-shipping cost | 2% bonus if ≥ 99.8% for 3 consecutive months |
| **Order fulfilment time** | Hours from order release to carrier hand-over (dispatch) | 95% of orders dispatched within 24 h; same-day for orders before 2 pm | WMS time-stamps (order release → manifest scan) | 1% of fee for each 1% below 95% | 1% bonus if ≥ 98% within 24 h |
| **Inventory accuracy** | Locations/SKUs with system qty = physical qty ÷ counted × 100 | ≥ 99.5% | Weekly cycle counts (ABC), quarterly wall-to-wall audit by buyer or third party | Supplier pays for shrinkage above 0.2% of inventory value + 1% fee credit per 0.1% shortfall | 1% bonus if ≥ 99.9% |
| **Customer complaints** | Complaints attributable to warehouse ÷ orders × 100 | ≤ 0.1% | CRM/ticketing tagged by root cause; monthly | 1% fee credit per 0.05% above target | Recognition + 1% bonus if ≤ 0.05% |
| **Warehouse safety** | Lost-time injuries (LTIFR) and safety audit score | Zero lost-time injuries; audit score ≥ 90% | Incident register; monthly safety audit; quarterly external audit | 2% credit per reportable incident due to non-compliance; corrective plan within 7 days | 1% bonus for 6 months incident-free |
| **Damage rate** | Orders damaged in warehouse handling ÷ orders shipped × 100 | ≤ 0.2% | Returns inspection + carrier claims + photo evidence at packing | Supplier reimburses product value of damaged goods + 1% credit per 0.1% over | 1% bonus if ≤ 0.1% |

Add: data source owned by buyer (WMS access), monthly KPI review, quarterly business review, root-cause and CAPA within 10 days for any miss, exclusions (force majeure, buyer-caused system outages, volume above forecast +20%), escalation ladder, and termination right after three consecutive months of failure on two or more KPIs.

---

## Que 4 (first). Hidden Cost of Outsourcing — textile production ⭐⭐⭐
Annual contract value = **$8 million**.

| Item | Cost ($) |
|---|---|
| Supplier audit | 120,000 |
| Travel | 80,000 |
| ERP integration | 150,000 |
| Quality inspection | 200,000 |
| Contract management | 170,000 |

**Q4.1 Calculate the total outsourcing cost.**
Hidden costs = 120,000 + 80,000 + 150,000 + 200,000 + 170,000 = **$720,000**.
Total outsourcing cost = 8,000,000 + 720,000 = **$8,720,000**.

**Q4.2 What percentage of total cost is hidden cost?**
720,000 ÷ 8,720,000 × 100 = **8.26%** of total cost. (As a share of the contract value it is 720,000 ÷ 8,000,000 = 9%.)

**Q4.3 Why are hidden costs often ignored?**
They sit in other departments' budgets (IT, quality, travel), not procurement's; many arise after the decision (transition, integration); vendor proposals show only the price; procurement is measured on price savings; they are hard to estimate in advance; and decision makers are optimistic about a smooth transition.

**Q4.4 Suggest methods to reduce these costs.**
Use TCO in the business case; choose certified suppliers to cut audit and inspection (rely on ISO 9001/OEKO-TEX certificates, risk-based audits); shift to supplier self-inspection with third-party random checks (AQL); use virtual audits and fewer, combined trips; integrate through EDI/cloud portals or the supplier's existing connectors instead of custom ERP work; build quality clauses so the supplier pays for defects; standard contract templates and vendor-management tools; long-term contracts that spread one-time costs.

---

## Que 4 (second). Contract Breach — missed Monday deliveries ⭐⭐⭐
A supplier agreed to deliver components every Monday and missed deliveries for four consecutive weeks. The manufacturer suffered production stoppage, emergency procurement and customer penalties. The contract includes liquidated damages, force majeure and a termination clause.

**Q4.5 Which contract clauses become applicable?**
- **Liquidated damages** — applies straight away: each missed delivery is a breach and the pre-agreed LD amount becomes payable without proving the exact loss.
- **Termination clause** — four consecutive misses are a persistent/material breach, which normally triggers the right to terminate for cause (after any notice/cure period).
- **Force majeure** — applies only if the supplier proves an event beyond its control that prevented delivery and gave timely notice. If it does, LDs are suspended for that period. If not, FM is not a defence.

**Q4.6 Can the buyer terminate immediately?**
Only if the contract allows immediate termination for this breach. Most termination clauses require **written notice of breach and a cure period** (e.g. 15–30 days); if the supplier fails to cure, the buyer terminates. If the contract makes "time of the essence" for Monday deliveries, or lists repeated failure (e.g. 3 misses in a quarter) as grounds for immediate termination, the buyer can terminate at once. Practically, the buyer should first secure supply (a second source), then serve notice, so termination does not worsen the stoppage.

**Q4.7 What evidence is needed before claiming damages?**
The contract and delivery schedule; purchase orders and the supplier's acknowledgements; proof of non-delivery (GRN records, gate logs, ASN vs receipt); written notices sent to the supplier and its replies; production stoppage records (downtime logs, idle labour/machine cost); emergency procurement invoices and the price difference; customer penalty invoices and correspondence linking them to the shortage; evidence of mitigation; and proof that no force-majeure notice was received (or that the claimed event does not qualify).

**Q4.8 What preventive clauses could have avoided the issue?**
Early-warning/notice obligation (supplier must alert within 24 h of any risk to delivery); safety-stock or **vendor-managed inventory/consignment** clause; **dual sourcing** right and step-in rights; escalating LDs per week of delay; KPI/OTIF SLA with reviews; cure period with a recovery plan; capacity reservation; business continuity plan obligation; clear force-majeure definition with mitigation duty; right to buy elsewhere at the supplier's cost ("cover" clause).

---

## Que 5. Outsourcing vs Offshoring — software company ⭐⭐
Option A: hire another Indian IT company. Option B: open its own development centre in Vietnam.

**Q5.1 Which option is outsourcing?**
**Option A** — a third party does the work (domestic/onshore outsourcing).

**Q5.2 Which option is offshoring?**
**Option B** — the work moves to another country but stays in-house (captive offshoring).

**Q5.3 Compare cost, control, flexibility and IP protection.**
| Factor | Option A — outsource to Indian IT firm | Option B — own centre in Vietnam |
|---|---|---|
| **Cost** | Low set-up cost; variable fees with vendor margin; quick savings | High set-up cost (entity, office, hiring, legal); lower long-run cost per developer once at scale |
| **Control** | Lower: managed through contract and SLA | High: own people, processes and culture |
| **Flexibility** | High: scale up/down by changing the contract | Lower: fixed costs, local labour law, exit is slow |
| **IP protection** | Weaker: code and know-how with a third party (mitigate with NDA, IP clauses) | Stronger: IP stays in the company, though Vietnam's IP enforcement must be checked |
| Other | Same time zone and language, fast start | Time to build (6–12 months), new legal and tax regime, talent risk |

**Q5.4 Recommend one option with justification.**
For a company whose aim is **cost reduction** now: **Option A** — fastest savings, no capital, flexible, and IP can be protected contractually; keep architecture and core IP in-house. Choose Option B only if the work is core/IP-sensitive and the company expects a large, long-term team (e.g. > 100 developers for 5+ years), where captive economics and control beat vendor margins.

---

## Que 6. Contract Negotiation — transportation contract ⭐⭐⭐
Supplier offers: $900 per container, 4-day delivery, minimum annual volume 5,000 containers. Buyer wants: price below $850, delivery within 3 days, no minimum commitment.

**Q6.1 Identify the negotiation issues.**
Three issues, all in conflict: **price** (gap of $50/container = $250,000 a year at 5,000 containers: 5,000 × $900 = $4.5 million vs 5,000 × $850 = $4.25 million), **transit time** (4 vs 3 days), and **volume commitment** (5,000 vs none). Underlying interests: the carrier needs **asset utilisation and predictable volume** to plan trucks/space; the buyer needs **low cost, speed and flexibility** because its demand is uncertain.

**Q6.2 Suggest possible trade-offs.**
- **Volume for price**: buyer commits to a realistic volume (e.g. 3,500–4,000) in exchange for a price near $850–870.
- **Tiered pricing**: $880 up to 3,000 containers, $850 beyond 3,000 (volume discount).
- **Speed for price**: standard 4-day service at the lower price plus a **3-day express option** at a premium (e.g. +$30) for urgent loads only.
- **Contract length for price**: 2–3 year contract in exchange for a lower rate.
- **Payment terms**: faster payment (15 days) for a discount.
- **Fuel indexation (BAF)** so the carrier is protected against fuel risk and can quote lower base rates.
- **Shortfall fee** instead of a hard minimum: buyer pays a small fee per container below the commitment.
- **Bonus/penalty**: on-time bonus for 3-day delivery achievement.

**Q6.3 Define BATNA for buyer and supplier.**
- **Buyer's BATNA**: use other carriers/the spot market, or another contract carrier's quote (e.g. $870 with 3.5 days); or rail/multimodal. If the spot rate averages below $900 with acceptable speed, the buyer has a strong BATNA.
- **Supplier's BATNA**: sell the capacity to other shippers or on the spot market; if the market is tight (high demand), its BATNA is strong and it can hold price; if there is overcapacity, it needs this volume.

**Q6.4 Recommend a win-win agreement.**
A **two-year contract** with a **committed volume of 3,500 containers/year**, **tiered price** of $870 for the first 3,000 and $840 above 3,000 (blended ≈ $866 at 3,500), **3.5-day standard transit** with a **3-day express lane at +$30** for up to 20% of loads, **BAF fuel indexation**, **95% on-time SLA** with a 1% rebate for misses and a 1% bonus above 98%, and a **shortfall fee of $25/container** below 3,500 instead of a hard minimum. The buyer saves vs $900 and gains speed; the carrier gets predictable volume and fuel protection.

---

## Que 7. Multi-Sourcing vs Single Sourcing — smartphone batteries ⭐⭐⭐
Option A: single supplier, lowest cost, excellent quality, located in one country. Option B: three suppliers, higher cost, lower disruption risk, flexible capacity.

**Q7.1 Compare advantages and disadvantages.**
| | Option A — single supplier | Option B — three suppliers |
|---|---|---|
| Advantages | Lowest unit cost (volume leverage), excellent and consistent quality, simple management, deep collaboration on design (battery is a critical, safety-relevant part) | Lower disruption risk, flexible capacity for demand spikes, competition keeps prices and service honest, bargaining power |
| Disadvantages | Single point of failure (earthquake, fire, export ban, sanctions); concentrated in one country; supplier gains bargaining power; capacity limits | Higher unit cost and more management (three qualifications, audits, tooling); quality variation between batteries; smaller volume per supplier |

**Q7.2 Which strategy supports supply chain resilience?**
**Option B (multi-sourcing)** — geographic and supplier diversity means one disruption does not stop production; spare capacity elsewhere absorbs shocks.

**Q7.3 Recommend a sourcing strategy after a major earthquake.**
Move immediately to **multi-sourcing (Option B)**: shift orders to the unaffected suppliers, expedite (air freight), build safety stock, and qualify suppliers in **different countries/seismic zones**. A practical steady design is **dual/triple sourcing with a 60/25/15 split** so the main supplier keeps scale but others are "warm" and qualified.

**Q7.4 How would your answer change during stable economic conditions?**
In stable conditions cost and quality dominate, so **Option A (single sourcing)** or a **primary supplier with a small qualified backup (e.g. 80/20)** is attractive. Even then, keep a qualified second source and some safety stock for a critical component, because disruptions are unpredictable.

---

## Que 8. Outsourcing Failure — cold-chain transportation for a food company ⭐⭐⭐
Problems: temperature excursions, delayed deliveries, product spoilage, customer complaints.

**Q8.1 Identify root causes using a Fishbone (Ishikawa) diagram.**
Head of the fish (effect): **"Temperature excursions → spoilage, delays and complaints."**

```
 MAN (People)            MACHINE (Equipment)        METHOD (Process)
 - Untrained drivers      - Old/poorly maintained     - No pre-cooling of vehicle/product
 - Doors opened often       reefer units              - Poor loading (blocked airflow)
 - Fatigue, no incentive  - Reefer switched off to    - No SOP for breakdowns
   to protect temp          save fuel                 - Route planning ignores traffic
          \                        |                        /
           \_______________________|_______________________/____ EFFECT: Temperature
           /                       |                        \     excursions, spoilage,
          /                        |                         \    delays, complaints
 MATERIAL                  MEASUREMENT                ENVIRONMENT / MANAGEMENT
 - Poor insulated packaging - No real-time IoT loggers  - High ambient heat, traffic jams
 - Wrong gel packs/dry ice  - Uncalibrated sensors      - Contract awarded on lowest price
 - Mixed loads with          - No alarm/escalation      - No temperature/OTIF SLA or penalty
   incompatible temps                                    - Weak supplier audits
```

**Q8.2 Recommend corrective actions.**
Immediate: quarantine and inspect affected stock; root-cause each excursion from logger data; replace defective reefers. Corrective/preventive (CAPA): mandatory **real-time IoT temperature monitoring** with alerts to both parties; pre-cooling and loading SOPs; driver training and certification (e.g. GDP-style); preventive maintenance schedule for reefer units; better insulated packaging; route optimisation and time-window planning; backup vehicles; **temperature and OTIF clauses with penalties** in the contract; monthly joint reviews.

**Q8.3 Should the company terminate the contract or improve supplier performance?**
**First improve, with a deadline.** Issue a formal notice and a 60–90 day **performance improvement plan** with measurable targets (excursions, OTIF). Termination is costly and disruptive (finding and qualifying a new cold-chain carrier takes time) and the causes are mostly fixable. **Terminate** if the supplier refuses to invest, misses the improvement targets, or there is a food-safety incident. Meanwhile qualify a second carrier as a backup.

**Q8.4 Design five KPIs to monitor future performance.**
| KPI | Formula | Target |
|---|---|---|
| Temperature compliance | Shipments kept within range for 100% of transit ÷ total shipments | ≥ 99.5% |
| Temperature excursion incidents | Number of excursions (> X minutes outside range) per 100 shipments | ≤ 0.5 |
| On-time delivery (OTIF) | Deliveries on time and in full ÷ total deliveries | ≥ 97% |
| Spoilage / damage rate | Value (or units) spoiled ÷ value shipped | ≤ 0.2% |
| Customer complaints | Cold-chain-related complaints per 1,000 deliveries | ≤ 1 |
(Also: reefer uptime, data-logger availability, claim settlement time.)

---

## Que 9. Global Outsourcing Decision — automotive supplier in India, Mexico or Poland ⭐⭐⭐
| Factor | India | Mexico | Poland |
|---|---|---|---|
| Unit cost ($) | 145 | 160 | 170 |
| Lead time (days) | 30 | 18 | 15 |
| Quality (%) | 96 | 98 | 99 |
| Tariff (%) | 5 | 8 | 4 |
| Political risk | Medium | Medium | Low |
| Currency risk | High | Medium | Low |

**Q9.1 Recommend a supplier using a weighted decision matrix.**
**Assumptions: weights — landed cost 30, lead time 20, quality 20, political risk 15, currency risk 15; ratings 1–10 (10 = best).**

| Criterion (weight) | India | Mexico | Poland |
|---|---|---|---|
| Landed cost (30) | 10 → 300 | 7 → 210 | 6 → 180 |
| Lead time (20) | 4 → 80 | 8 → 160 | 9 → 180 |
| Quality (20) | 6 → 120 | 8 → 160 | 10 → 200 |
| Political risk (15) | 6 → 90 | 6 → 90 | 9 → 135 |
| Currency risk (15) | 4 → 60 | 6 → 90 | 9 → 135 |
| **Total ÷ 100** | **6.50** | **7.10** | **8.30** |

**Recommendation: Poland (8.30)** — best quality, shortest lead time and lowest political/currency risk; it loses only on price. Even if cost weight is raised to 50% (others 15/15/10/10), Poland (7.65) still edges India (7.50) and Mexico (7.10).

**Q9.2 Which country minimises total landed cost?**
Landed cost = unit cost × (1 + tariff):
- India = 145 × 1.05 = **$152.25**
- Mexico = 160 × 1.08 = **$172.80**
- Poland = 170 × 1.04 = **$176.80**

Adjusting for quality (cost per good unit = landed cost ÷ quality yield): India 152.25 ÷ 0.96 = $158.59; Mexico 172.80 ÷ 0.98 = $176.33; Poland 176.80 ÷ 0.99 = $178.59. Adding in-transit inventory carrying cost (**assume 20% a year**: value × 20% × days ÷ 365): India +$2.50, Mexico +$1.70, Poland +$1.45 → India ≈ $161.1, Mexico ≈ $178.0, Poland ≈ $180.0.
**India has the lowest total landed cost** (about $19 a unit cheaper than Poland), even after quality and pipeline inventory. Freight is not given; adding it would widen the gap slightly against India for a European or US plant.

**Q9.3 How should geopolitical risk influence supplier selection?**
It should be an explicit weighted criterion and a **cost** in the landed-cost model (risk premium, buffer stock, insurance). Consider political stability, trade wars and tariffs (USMCA for Mexico, EU single market for Poland, India's FTAs), sanctions, export controls, conflict near shipping routes (Red Sea for India–Europe), currency volatility, and the exposure of a long, single route. High-risk sources need safety stock, dual sourcing, contracts in hard currency and hedging.

**Q9.4 Should the company adopt nearshoring or offshoring?**
For an automotive (often JIT/JIS) supply chain, **nearshoring** — Mexico for a North American plant, Poland for a European plant — because short lead times, low inventory, quality and low risk outweigh India's ~$15–20 unit cost advantage. **Offshoring to India** makes sense for standard, high-volume, non-time-critical parts where cost dominates, possibly as a second source (a "China+1/India+nearshore" dual strategy).

---

## Que 10. Outsourcing Ethics — underage workers at a garment supplier ⭐⭐⭐
The contract contains a Code of Conduct, an ESG compliance clause and audit rights.

**Q10.1 What ethical responsibilities does the buyer have?**
Duty of care for human rights in its supply chain (UN Guiding Principles, ILO conventions C138 and C182); protect the children's welfare first (no harm from the remedy); investigate and verify; remediate; be transparent with stakeholders; prevent recurrence; ensure its own buying practices (low prices, short lead times) are not driving the abuse; comply with law (India's Child and Adolescent Labour Act; foreign due-diligence laws for export markets).

**Q10.2 Which contract clauses should be enforced?**
- **Code of Conduct** — breach of the no-child-labour requirement.
- **ESG compliance clause** — material breach; demand a corrective action plan and possibly penalties.
- **Audit rights** — unannounced and third-party audits (SA8000, SMETA, WRAP) of all lines and sub-contractors.
- Also: remediation obligations, reporting, and the termination-for-cause clause if the supplier fails to remediate.

**Q10.3 Should the contract be terminated immediately?**
**Not automatically.** Immediate termination ("cut and run") can push children into more dangerous work and workers lose jobs. Recommended: suspend new orders, require an immediate **remediation plan** — remove the children safely from work, continue paying their wages or a stipend while they attend school until legal working age, offer the job to an adult family member, age-verification for all workers. **Terminate** if the supplier refuses, conceals, repeats the violation, or uses forced labour.

**Q10.4 Recommend a supplier development plan.**
1. Root-cause analysis (why children were hired: cost pressure, sub-contracting, poor HR checks).
2. Corrective action plan with deadlines; age-verification and HR systems.
3. Training for management and HR on labour law and the Code.
4. Fair purchasing: realistic prices and lead times so compliance is affordable; longer-term orders.
5. Worker grievance mechanism / helpline.
6. Regular third-party audits and transparent reporting; traceability to sub-contractors.
7. Recognition: preferred-supplier status and more orders for sustained compliance.

---

## Que 11. Force Majeure During a Pandemic — nationwide lockdown ⭐⭐⭐
A supplier could not deliver because the government imposed a nationwide lockdown. The buyer wants compensation.

**Q11.1 Does force majeure apply?**
Most likely **yes**, if the clause covers epidemics/pandemics, government action, lockdowns or "acts of government" (India's Ministry of Finance in Feb 2020 declared COVID-19 a natural calamity for FM in government procurement). A government lockdown is beyond the supplier's control and makes performance impossible or illegal. It applies only for the **duration** of the lockdown, only if the lockdown actually **caused** the non-delivery, and only if the supplier gave **timely notice** and tried to mitigate. If the contract has no FM clause, the supplier can rely on **frustration** (Indian Contract Act s.56). FM normally means **no damages** for the period, so the buyer's compensation claim fails.

**Q11.2 What evidence must the supplier provide?**
The government order/notification and its dates; proof that the facility and logistics were covered (not an essential service); written FM notice sent to the buyer promptly as the clause requires; evidence of the causal link (production halted, transport stopped); evidence of mitigation attempts (alternative sites, partial supply, essential-service permits); and resumption plans once restrictions lifted.

**Q11.3 What alternatives can the buyer pursue?**
Source from alternative suppliers (in unaffected regions/countries); use safety stock; reallocate available inventory; negotiate partial or phased deliveries; extend the delivery schedule; renegotiate terms/prices; terminate if FM continues beyond the period allowed in the clause; claim on **business interruption or contingent business interruption insurance** if covered.

**Q11.4 How should future contracts be revised after the pandemic?**
Name **pandemics, epidemics, lockdowns and government orders** explicitly; require notice within a fixed time (e.g. 7 days) with evidence; a **duty to mitigate** and partial performance; allocation of available capacity; a time limit after which either party may terminate (e.g. 90 days); price/currency adjustment and **hardship** clauses; business continuity and multi-site obligations; data/visibility sharing; and dual sourcing rights for the buyer.

---

## Que 12. Outsourcing Financial Evaluation ⭐⭐⭐
Current spend: production $12 million, logistics $1.5 million, administration $0.8 million. Supplier proposal: outsourcing price $11 million, transition cost $600,000, annual contract management $400,000, expected productivity improvement 5%.

**Assumption: the $11 million price covers all three activities (production, logistics and administration), and the 5% productivity improvement reduces the outsourced cost by 5% of $11 million = $0.55 million a year from Year 2 (Year 1 is taken up by transition).**

**Q12.1 Calculate the first-year outsourcing cost.**
First-year cost = outsourcing price + transition cost + contract management
= 11,000,000 + 600,000 + 400,000 = **$12,000,000**.
Current in-house cost = 12 + 1.5 + 0.8 = **$14.3 million**, so Year-1 saving = 14.3 − 12.0 = **$2.3 million**.

**Q12.2 Calculate annual savings after Year 1.**
From Year 2 there is no transition cost:
Annual outsourcing cost = 11.0 + 0.4 = $11.4 million → saving = 14.3 − 11.4 = **$2.9 million a year**.
With the 5% productivity improvement (5% × 11 = $0.55 million): cost = 11.4 − 0.55 = $10.85 million → saving = **$3.45 million a year**.

**Q12.3 Estimate the payback period.**
Payback = one-time investment ÷ annual saving = 0.6 ÷ 2.9 = **0.21 years ≈ 2.5 months** (0.6 ÷ 3.45 = 0.17 years ≈ 2.1 months with the productivity gain). Even counting Year 1, the $2.3 million saving recovers the $0.6 million transition cost within the first quarter.

**Q12.4 Should outsourcing be approved?**
**Yes, financially** — savings of $2.3 million in Year 1 (16% of current cost) and $2.9–3.45 million a year after, with a payback of under three months. Approve subject to: an SLA with KPIs and penalties for quality and delivery; IP and confidentiality protection; a risk review of the supplier's financial health; a phased transition with a parallel run; and an exit clause.

> **Alternative reading** (if the $11 million replaces only production, and logistics and administration stay in-house): Year-1 cost of the outsourced part = $12.0 million vs $12 million today → **no saving in Year 1**; from Year 2 the saving is 12.0 − 11.4 = $0.6 million (or $1.15 million with productivity), and payback = 0.6 ÷ 0.6 = **1 year** (≈ 0.5 years with productivity). Still approvable, but the case is much weaker, and qualitative factors (control, quality, risk) decide. Say which reading you use.

---

## Que 13. Contract Performance Dashboard — outsourced warehouse (KPIs) ⭐⭐⭐
Data for the month: orders shipped 24,500; correct orders 24,100; average fulfilment time 19 hours; inventory records 10,000; correct inventory records 9,850; damaged orders 180; customer complaints 45.

**Q13.1 Calculate order accuracy, inventory accuracy, damage rate and complaint rate.**
- **Order accuracy** = 24,100 ÷ 24,500 × 100 = **98.37%**
- **Inventory accuracy** = 9,850 ÷ 10,000 × 100 = **98.50%**
- **Damage rate** = 180 ÷ 24,500 × 100 = **0.73%**
- **Complaint rate** = 45 ÷ 24,500 × 100 = **0.18%**
- (Average fulfilment time = 19 hours — no target given; good if the SLA is 24 h.)

**Q13.2 Compare the results against the targets.**
| KPI | Actual | Target | Gap | Status |
|---|---|---|---|---|
| Order accuracy | 98.37% | ≥ 99% | −0.63 pts (≈155 more errors than allowed: 400 wrong vs 245 allowed) | ❌ Below |
| Inventory accuracy | 98.50% | ≥ 99.5% | −1.0 pt (150 wrong records vs 50 allowed) | ❌ Below |
| Damage rate | 0.73% | ≤ 0.5% | +0.23 pts (180 vs 122 allowed) | ❌ Above limit |
| Complaint rate | 0.18% | ≤ 0.2% | −0.02 pts (45 vs 49 allowed) | ✅ Meets |

**Q13.3 Recommend corrective actions for any KPI below target.**
- **Order accuracy**: barcode/RF scan verification at pick and pack, pick-to-light or voice picking, weight check at packing, slotting look-alike SKUs apart, picker training and error-based coaching, root-cause log of mis-picks.
- **Inventory accuracy**: ABC cycle counting (A items weekly), immediate put-away scanning, location labelling, control of adjustments, investigate variances, restrict system overrides, WMS discipline.
- **Damage rate**: better packaging standards and dunnage, handling training, equipment maintenance (forklifts, conveyors), proper stacking/load limits, damage root-cause by SKU and shift, carrier hand-over inspection with photos.

**Q13.4 Should the supplier receive a performance incentive or a penalty?**
**A penalty (service credit).** Three of four KPIs miss target, including the two most important (order and inventory accuracy). Apply the contractual service credits, require a **corrective action plan** within an agreed time (e.g. 15 days) and track monthly. No incentive is due; the complaint rate meeting its target does not offset the other failures. If the misses repeat for three months, escalate under the termination/step-in provisions.
