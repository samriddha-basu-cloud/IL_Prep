# Container Imbalance Problems — Full Solutions
The **exact five questions** (5 marks each) from *IL problems for practice final part 1* 📘, slides 2–6. Theory: [Containerization & Container Imbalance](ch03-containerization-container-imbalance.md). For 5 marks, write about 8–10 crisp points, using the PPT's terms (empty container repositioning, CIC, CAx, SOC, trade imbalance).

---

## Question 1: Container Imbalance (5 Marks) ⭐⭐⭐
An Indian exporter based in Tiruppur ships garments regularly to the USA. However, the shipping line reports frequent shortages of empty containers at Chennai port, while surplus empty containers are lying idle at US west coast ports. This situation has increased export lead times and freight rates.

**Q1.1 Identify the logistics issue in the above case.**
**Container imbalance** (container inventory imbalance) on the India–USA trade lane: a **shortage of empty containers at the export origin (Chennai)** and a **surplus of idle empties at the import destination (US West Coast)**. The exporter has cargo but no box; boxes exist but in the wrong place. It calls for **empty container repositioning** and leads to **Container Imbalance Charges**. (Chennai's CAx would be persistently **below 0.5**, US West Coast ports **above 0.5**.)

**Q1.2 Explain two causes of this issue.**
1. **Trade imbalance** — the US imports far more from India/Asia (garments, consumer goods) than it exports back on the same lane; full containers arrive in the US, are emptied and have no return cargo, so they accumulate there, while Indian ports run short.
2. **Slow/costly repositioning and storage economics** — an empty box occupies the same slot as a full one and nobody pays for it, so lines delay repositioning or prioritise higher-paying lanes (e.g. China); long dwell times, port congestion and labour disruption at US West Coast ports (ILWU–PMA negotiations) keep boxes stuck. Other valid causes: demand surges/peak season, lack of carrier cooperation (no pooling), outdated planning tools, inland empties not returned quickly.

**Q1.3 Mention one operational impact on exporters.**
**Longer export lead times and missed shipment dates** — the Tiruppur exporter must wait for equipment, so finished garments are **stockpiled** (tying up cash and warehouse space), orders are delivered late (risking cancellation, contract penalties, or expensive air freight for seasonal fashion), and it pays **higher freight rates plus CIC/peak surcharges**, squeezing margins.

---

## Question 2: Container Repositioning Strategy (5 Marks) ⭐⭐⭐
A global shipping line operates routes between China–Europe–India. After peak season, it observes excess empty containers in European ports and shortages in Indian ports. To manage this, the company decides to move empty containers without cargo.

**Q2.1 What is the process described above?**
**Empty Container Repositioning (ECR)** — moving empty containers from surplus locations (European ports) to deficit locations (Indian ports) without cargo, so that they can be loaded with export cargo there.

**Q2.2 Why is this process necessary?**
- **Trade imbalance**: Europe imports more from Asia than it exports, so empties pile up there while Indian exporters need boxes.
- To **meet export demand and protect service/revenue** in India: without boxes the line loses bookings and customers (CIMS factors: cost of customers, impact on brand, loss of revenue).
- **Storage costs**: after ~5 free days, storage can cost up to $100 per box per day; idle boxes in Europe earn nothing and congest yards.
- To keep vessels **utilised** on the next headhaul and maintain the container network's balance (avoid buying or leasing new boxes).

**Q2.3 State two costs involved in this process.**
1. **Ocean freight / slot cost** — the empty occupies a vessel slot that could carry paying cargo (opportunity cost) plus fuel.
2. **Handling and port charges** — terminal handling (lift-on/lift-off) at both ends, **empty port handling**, transhipment.
Also: drayage/inland haulage of empties to and from depots, storage/yard rent at CFS or depot while waiting, repair and cleaning, documentation, and the administrative/planning cost. (Industry-wide ECR costs **$15–20 billion a year**.)

---

## Question 3: Container Imbalance Charges (5 Marks) ⭐⭐⭐
An Indian importer notices an additional fee labelled "Container Imbalance Charge (CIC)" on the freight invoice for shipments arriving from Europe. The shipping line explains that this charge is applicable on certain trade lanes.

**Q3.1 What is Container Imbalance Charge?**
A **surcharge levied by the shipping line/carrier** on top of base ocean freight to **compensate for the cost of repositioning empty containers** between countries/regions where there is a trade imbalance. It covers the cost of moving the box back (or onward) empty, plus drayage, transhipment and empty storage. It is charged per container (per TEU/FEU) on specific lanes.

**Q3.2 Why do shipping lines levy this charge?**
- Imports into India from this lane create **inbound boxes that may not find export cargo locally** (or the line must reposition empties to where they are needed); repositioning earns no revenue.
- To **recover the cost** of empty repositioning ($15–20 bn industry-wide), storage (beyond free days) and handling of empties.
- To **price the imbalance into the lane** that causes it, and discourage it (signal to balance flows).
- Rate volatility and pandemic-era shortages made such surcharges common.

**Q3.3 Who ultimately bears this cost?**
The **cargo interest** — here the **Indian importer (consignee)**, because the PPT's rule is that the **consignee pays when it creates the imbalance by receiving more containers than it ships**; if the shipper sent more than it received, the shipper would pay. Under the sale contract, whether the importer can pass it to the exporter depends on the Incoterm (e.g. under CIF/CFR the seller pays freight but destination surcharges are often for the buyer's account). In the end, the cost flows into the landed cost and is borne by **consumers** through higher prices. Always check the contract terms for such surcharges.

---

## Question 4: Decision-Making in Container Repositioning (5 Marks) ⭐⭐⭐
A shipping company must decide whether to reposition empty containers from Dubai to Mumbai or lease containers locally in India during the export peak season.

**Q4.1 Identify two factors influencing this decision.**
1. **Cost comparison** — repositioning cost (Dubai→Mumbai ocean slot, handling at both ends, drayage, port charges) vs **local leasing cost** (per-diem lease rate × days of use + pick-up/drop-off charges + off-hire location fees) in peak season, when lease rates rise.
2. **Time and availability** — transit time Dubai→Mumbai (≈3–5 days sailing + port time) and vessel space vs how fast leased boxes are available in India; missing peak bookings costs revenue and customers.
Other factors: number of boxes needed and for how long; whether boxes will return loaded (lane balance afterwards); container type/condition needed (reefers, high cubes); the opportunity cost of using Dubai's surplus elsewhere; storage costs in Dubai if not moved; vessel slot availability on the Dubai–Mumbai service; lessor's drop-off locations; the line's own fleet utilisation/ROI.

**Q4.2 Suggest the better option with justification.**
**Reposition from Dubai to Mumbai** — recommended in most cases because:
- Dubai–Mumbai is a **short, cheap feeder leg** (a few days, frequent services) and the line already **owns** the idle boxes — repositioning uses sunk assets and stops Dubai's storage/idle costs.
- **Peak-season leasing** in India is expensive and scarce (high per diem and pick-up charges) and leased boxes must be returned/off-hired later, often with drop-off fees.
- The line keeps **control of equipment quality** and avoids lessor terms.

**Leasing locally is better** when: the repositioning cost per box (including handling at both ends) exceeds the total lease cost for the period; vessel space from Dubai is not available in time; demand is **short-term or uncertain** (lease short, avoid owning surplus later); or specialised boxes are needed. A practical answer: **reposition the base requirement from Dubai** and **lease locally (one-way/short-term) for the peak top-up**, using street turns and depot-direct moves in India to stretch supply.

*Illustration (assumed figures):* repositioning ≈ $250/box (slot $150 + two lifts $60 + drayage $40) vs leasing ≈ $3/day × 60 days + $150 pick-up = $330/box → reposition. If peak slot rates jump to $350, repositioning ≈ $450 > $330 → lease.

---

## Question 5: Impact of Container Imbalance on Supply Chain (5 Marks) ⭐⭐⭐
During the COVID-19 pandemic, exporters faced severe container shortages and high freight rates across Asian ports.

**Q5.1 Explain how container imbalance contributed to this situation.**
- **Demand shock**: in 2020–21 consumers in the US and Europe shifted spending from services to goods; **imports from Asia soared**, so full containers flowed west.
- **Boxes stuck at the wrong end**: Western ports and inland depots were congested (labour shortages, quarantine, warehouse capacity), dwell times rose sharply, and empties were not returned; the US/EU had little cargo to send back — so empties **accumulated in the West** while **Asian ports ran out**.
- **Carriers rushed empties back to Asia**, some shipping **~75% of containers from the US/Europe to Asia empty**, but repositioning could not keep pace.
- **Capacity cuts and blank sailings** in early 2020, port closures in China, and fewer box manufacturing outputs reduced supply further.
- With boxes scarce in Asia, **spot rates rose to records** (Asia–Europe/US rates up several-fold in 2021) and carriers added surcharges (CIC, peak-season, equipment imbalance); Asian CAx values stayed below 0.5.

**Q5.2 Mention two supply chain impacts.**
1. **Delays and longer lead times** — exporters waited weeks for equipment and vessel space; products reached shelves late; inventory shortages and stock-outs (and contract penalties for missed deadlines).
2. **Sharply higher logistics costs** — record freight rates and surcharges raised landed costs and squeezed margins, especially for low-value goods (e.g. furniture, garments); some shipments became uneconomic.
Also: cash-flow stress from stockpiled goods, production slowdowns due to missing inputs (bullwhip), reduced reliability and predictability of global shipping, and more fuel use/emissions from empty moves.
