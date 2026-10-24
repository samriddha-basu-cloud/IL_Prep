# Transportation KPIs, Freight Terms & Carrier Scorecards
Exam topic 8 of 8 📘 — the **KPIs book case**. The zip has the book cases (*Case 11.1 Vibrant Video* and *Case 11.2 Bob's Custom BBQs*, from the transportation chapter of Coyle, Langley, Novack & Gibson, *Supply Chain Management: A Logistics Perspective*, Ch. 11) and the **pre-read material**: Table 11.4 (FOB freight terms), 11.5 (modal capabilities), 11.6 (performance ranking of modes), 11.7 (common transportation metrics) and 11.8 (transportation performance scorecard). This page teaches every table; the two cases are solved on [KPI Book Cases](p6-kpi-book-cases.md). Warehouse/outsourcing KPIs (order accuracy, inventory accuracy, damage and complaint rate) are in [Outsourcing Problems Que 13](p1-outsourcing-contract-problems.md).

---

## 1. Freight terms: FOB origin vs FOB destination ⭐⭐⭐ 📘
In US domestic practice "FOB" terms (different from Incoterms FOB) answer two separate questions:
1. **FOB point** — where **title and risk** pass → *who owns the goods in transit and who files claims*: **FOB Origin** (buyer owns from the shipping point) or **FOB Destination** (seller owns until delivery).
2. **Freight payment term** — *who pays the carrier and who ultimately bears the cost*: **Freight Collect** (buyer pays carrier), **Freight Prepaid** (seller pays carrier), plus **Charged Back** (seller prepays, then adds freight to the invoice) and **Collect & Allowed** (buyer pays carrier, then deducts it from the invoice).

### Table 11.4 — Freight control and payment terms ⭐⭐⭐ 📘
| FOB term & freight payment responsibility | Who owns goods in transit? | Who handles freight claims? | Who selects and pays carrier? | Who ultimately bears freight costs? | Best used when ___ has greater influence with carrier |
|---|---|---|---|---|---|
| **FOB Origin, Freight Collect** | Buyer | Buyer | Buyer | Buyer | **Buyer** |
| **FOB Origin, Freight Prepaid** | Buyer | Buyer | Seller | Seller | **Seller** |
| **FOB Origin, Freight Prepaid & Charged Back** | Buyer | Buyer | Seller | **Buyer** — seller adds freight costs to goods invoice | **Seller** |
| **FOB Destination, Freight Prepaid** | Seller | Seller | Seller | Seller | **Seller** |
| **FOB Destination, Freight Collect** | Seller | Seller | Buyer | Buyer | **Buyer** |
| **FOB Destination, Freight Collect & Allowed** | Seller | Seller | Buyer | **Seller** — buyer deducts freight cost from goods payment | **Buyer** |
Source: adapted from Bruce J. Riggs, "The Traffic Manager in Physical Distribution Management", 1968.

**How to remember:** the FOB point decides **ownership + claims** (columns 1–2); the payment term decides **who pays the carrier** (column 3); "charged back" and "allowed" move the **ultimate cost** (column 4) to the other party. **Control** goes with whoever **selects** the carrier.

**Link to Incoterms 📗:** FOB Origin, Freight Collect ≈ FCA/EXW (buyer controls and pays carriage, bears transit risk); FOB Destination, Freight Prepaid ≈ DAP (seller controls, pays and bears risk to destination); FOB Origin, Freight Prepaid ≈ CPT (seller pays freight, buyer bears transit risk).

---

## 2. Modal capabilities ⭐⭐⭐ 📘
### Table 11.5 — Comparison of modal capabilities
| Mode | Strengths | Limitations | Primary role | Primary product characteristics | Example products |
|---|---|---|---|---|---|
| **Truck** | Accessible; fast and versatile; customer service | Limited capacity; high cost | Move smaller shipments in local, regional and national markets | High value; finished goods; low volume | Food, clothing, electronics, furniture |
| **Rail** | High capacity; low cost | Accessibility; inconsistent service; damage rates | Move large shipments of domestic freight long distances | Low value; raw materials; high volume | Coal/coke, lumber/paper, grain, chemicals |
| **Air** | Speed; freight protection; flexibility | Accessibility; high cost; low capacity | Move urgent shipments of domestic freight and smaller shipments of international freight | High value; finished goods; low volume; time sensitive | Computers, periodicals, pharmaceuticals, e-commerce deliveries |
| **Water** | High capacity; low cost; international capabilities | Slow; accessibility | Move large domestic shipments via rivers and canals; large shipments of international freight via oceans | Low value; raw materials; bulk commodities; containerised finished goods | Crude oil, ores/minerals, farm products, clothing, electronics, toys |
| **Pipeline** | In-transit storage; efficiency; low cost | Slow; limited network | Move large volumes of domestic freight long distances | Low value; liquid commodities; not time sensitive | Crude oil, petroleum, gasoline, natural gas |
Source: Brian J. Gibson.

### Table 11.6 — Performance ranking of modes ⭐⭐⭐ 📘
(1 = best to 5 = worst for service criteria; cost: 1 = lowest cost to 5 = highest cost)

| Criteria | Truck | Air | Rail | Water | Pipeline |
|---|---|---|---|---|---|
| Accessibility | **1** | 3 | 2 | 4 | 5 |
| Transit time | 2 | **1** | 3 | 4 | 5 |
| Reliability | 2 | 3 | 4 | 5 | **1** |
| Security | 3 | 2 | 4 | 5 | **1** |
| Cost | 4 | 5 | 3 | 2 | **1** |
Source: Edward J. Bardi.

Read-outs: truck wins **accessibility** (door-to-door), air wins **transit time** but is **costliest**, pipeline is most **reliable, secure and cheapest** but least accessible and slowest; water is cheap but slowest and least reliable among the others.

### Mode and carrier selection criteria 📗
Transit time and reliability (consistency), capability/capacity, accessibility, security (loss and damage), cost (rates and total landed cost), customer service, technology (tracking, EDI), financial stability, sustainability (emissions). Selection steps: problem recognition → search → choice (evaluate against criteria) → post-choice evaluation (**carrier scorecards**).

---

## 3. Transportation performance metrics (KPIs) ⭐⭐⭐ 📘
### Table 11.7 — Common transportation metrics
| Metric | Formula | Typical target |
|---|---|---|
| **On-time delivery** | Total on-time deliveries ÷ total deliveries | **> 95%** |
| **Transit time average** | Sum of transit times ÷ total deliveries | **Low variation around goal** |
| **Damage rate** | Total units damaged ÷ total units shipped | **< 1%** |
| **Shortage rate** | Total units lost or stolen ÷ total units shipped | **< 1%** |
| **Billing accuracy** | Total accurate freight bills ÷ total freight bills | **> 99%** |
| **Perfect delivery index** | On-time % × damage-free % × billing accuracy % | **> 95%** |
Source: Brian J. Gibson.

Why it matters (pre-read): a delivery that is **on time, damage free and with an accurate bill** eliminates the need for administrative work, tempers the use of premium (expedited) service, and promotes customer satisfaction, inventory reduction and supply chain stability.

### Perfect delivery index — worked example 📗
On-time 96%, damage-free 99.2% (damage 0.8%), billing accuracy 98.5% → PDI = 0.96 × 0.992 × 0.985 = **93.8%** < 95% target. Notice how a small shortfall in each metric compounds.

### Other logistics KPIs worth knowing 📗
| Category | KPIs |
|---|---|
| Service | OTIF (on time in full), perfect order rate, fill rate (order, line, unit), order cycle time, customer complaints |
| Cost | Freight cost per unit / per kg / per km / as % of sales, cost per shipment, total landed cost, empty-mile %, accessorial charges |
| Asset utilisation | Truck/container utilisation (cube and weight), load factor, dwell time, turnaround time, vessel/berth productivity |
| Quality | Damage and claims ratio, claim settlement time, shortage rate, temperature compliance (cold chain) |
| Speed | Transit time and variability, dock-to-stock time, customs clearance time |
| Sustainability | CO₂ per tonne-km, % intermodal/rail, fuel efficiency |
| Warehouse | Order accuracy, inventory accuracy, picking productivity, inventory turns |
Good KPI practice: **SMART**, aligned to strategy, a few vital metrics, a clear data source and owner, targets with benchmarks, and a review cadence (monthly scorecard, quarterly business review).

---

## 4. The carrier performance scorecard ⭐⭐⭐ 📘
A **weighted scorecard** converts several KPIs into one number so carriers can be compared, rewarded (more volume, awards) or eliminated:
1. Choose **performance criteria** (on-time delivery, loss/damage, billing accuracy, equipment condition, customer service, loads rejected…).
2. Assign a **weight factor** to each (total 100).
3. Define a **performance evaluation scale** — bands of actual performance mapped to points (e.g. 5 = best … 0 = unacceptable).
4. Category score = **weight × points**; **potential score** = weight × 5; total potential = 500.
5. **Total score** = Σ category scores; compare carriers and over time.

### Table 11.8 — Transportation performance scorecard (example) ⭐⭐⭐ 📘
| Performance criteria | Weight | Carrier performance | Performance scale | Points | Category score |
|---|---|---|---|---|---|
| On-time delivery | 35 | 96.7% | >98% = 5; 96.01–98% = 4; 94.01–96% = 3; 92.01–94% = 2; <92% = 0 | 4 | **140** |
| Loss and damage rate | 30 | 0.6% | <0.5% = 5; 0.5–1% = 4; 1–1.5% = 3; 1.5–2% = 2; >2% = 0 | 4 | **120** |
| Billing accuracy | 15 | 98.1% | >99% = 5; 97–99% = 3; 95–96% = 1; <95% = 0 | 3 | **45** |
| Equipment condition | 5 | Acceptable | Safe & clean = 5; poor condition = 0 | 5 | **25** |
| Customer service | 15 | Outstanding feedback on customer surveys | Superior = 5; good = 4; average = 3; fair = 2; unacceptable = 0 | 5 | **75** |
| **Total score** | 100 | | | | **405 / 500** |
How to read it: the carrier scores **81%** of potential (405/500). It loses most points on **on-time delivery** (−35: 140/175) and **billing accuracy** (−30: 45/75); these are its improvement areas.

---

## Self-test
**Q1. In FOB Destination, Freight Collect and Allowed, who owns the goods, who pays the carrier and who bears the cost?**
The seller owns the goods in transit and files claims; the buyer selects and pays the carrier; but the buyer deducts the freight from its payment, so the seller ultimately bears the freight cost. It is best when the buyer has more influence with carriers.

**Q2. Which term gives the buyer full control and full cost?**
FOB Origin, Freight Collect: buyer owns goods in transit, handles claims, selects and pays the carrier and bears the cost.

**Q3. Write the formula for the perfect delivery index.**
PDI = on-time % × damage-free % × billing accuracy %; typical target above 95%.

**Q4. Rank the modes on transit time and cost (Table 11.6).**
Transit time: air 1, truck 2, rail 3, water 4, pipeline 5. Cost: pipeline 1 (lowest), water 2, rail 3, truck 4, air 5 (highest).

**Q5. How is a weighted carrier scorecard built?**
Choose criteria, weight them to 100, define banded point scales (e.g. 0–5), multiply weight × points for each criterion and add up; compare the total to the 500 potential and across carriers.

**Q6. What are the strengths and limitations of rail (Table 11.5)?**
Strengths: high capacity, low cost. Limitations: accessibility, inconsistent service, damage rates. Role: large domestic shipments over long distances; low-value, high-volume raw materials like coal, lumber, grain, chemicals.
