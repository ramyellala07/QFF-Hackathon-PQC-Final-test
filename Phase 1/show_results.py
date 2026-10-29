import csv

PATH = "qff_phase1_p3/results/tables/AB_comparison.csv"
rows = list(csv.DictReader(open(PATH)))

print("| Processor | Circuit | Bits | Version | Depth | 2Q gates | All-to-all 2Q | SWAPs | P(correct) carry-chain | P(correct) mixed |")
print("|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    version = "optimized" if r["version"].startswith("optimized") else "baseline"
    print("| {p} | {c} | {n} | {v} | {d} | {q} | {a} | {s} | {c1} +/- {e1} | {c2} +/- {e2} |".format(
        p=r["processor"][:1], c=r["circuit"], n=r["n_bits"], v=version, d=r["depth"],
        q=r["two_qubit_gates"], a=r["all_to_all_2q_gates"], s=r["swap_count"],
        c1=r["noisy_success_carry_chain"], e1=r["noisy_success_se_carry_chain"],
        c2=r["noisy_success_mixed"], e2=r["noisy_success_se_mixed"]))
