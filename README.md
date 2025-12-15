# MMDecode
Tools for understanding the composition and structure of certain metamath theorems.

`wff_finder.py`: Takes in two arguments, the first one being the original solution to a theorem, and the second being the modified solution. This will tell you what in the modified theorem will correspond to each WFF in the original theorem. It also checks to ensure the theorems correctly correlate, erroring if they do not.

EXAMPLE:
```
python wff_finder.py "⊢ (((𝜒 → (¬ 𝜑 → 𝜓)) → 𝜏) → (𝜑 → 𝜏))" "⊢ ((((𝜑 → 𝜓) → (¬ ¬ 𝜑 → 𝜓)) → ¬ (((((𝜓 → 𝜓) → (¬ 𝜓 → ¬ 𝜓)) → 𝜓) → 𝜓) → ((𝜓 → 𝜓) → (𝜓 → 𝜓)))) → (¬ 𝜑 → ¬ (((((𝜓 → 𝜓) → (¬ 𝜓 → ¬ 𝜓)) → 𝜓) → 𝜓) → ((𝜓 → 𝜓) → (𝜓 → 𝜓)))))"
𝜒: (𝜑 → 𝜓)
𝜑: ¬ 𝜑
𝜓: 𝜓
𝜏: ¬ (((((𝜓 → 𝜓) → (¬ 𝜓 → ¬ 𝜓)) → 𝜓) → 𝜓) → ((𝜓 → 𝜓) → (𝜓 → 𝜓)))
```

`splitter.py`: Takes in any WFF or theorem, splits it up into its basic parts, and shows steps on how it was assembled together.

EXAMPLE
```
python splitter.py "((𝜓 → 𝜓) → (¬ 𝜓 → ¬ 𝜓))"
wff 𝜓, wff 𝜓, wi
 > wff ((𝜓 → 𝜓))

wff ¬ 𝜓, wff ¬ 𝜓, wi
 > wff ((¬ 𝜓 → ¬ 𝜓))

wff (𝜓 → 𝜓), wff (¬ 𝜓 → ¬ 𝜓), wi
 > wff (((𝜓 → 𝜓) → (¬ 𝜓 → ¬ 𝜓)))
```
