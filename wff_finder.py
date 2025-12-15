import sys

og_theorem: str         = sys.argv[1]
to_split_theorem: str   = sys.argv[2]

# og_theorem: str =       "⊢ (((((𝜑 → 𝜓) → (¬ 𝜒 → ¬ 𝜃)) → 𝜒) → 𝜏) → ((𝜏 → 𝜑) → (𝜃 → 𝜑)))"
# to_split_theorem: str = "⊢ (((((¬ 𝜑 → 𝜓) → (¬ (¬ 𝜏 → ¬ 𝜒) → ¬ ¬ (¬ 𝜑 → 𝜓))) → (¬ 𝜏 → ¬ 𝜒)) → 𝜏) → ((𝜏 → ¬ 𝜑) → (¬ (¬ 𝜑 → 𝜓) → ¬ 𝜑)))"

wffs: list[str] = ["𝜑", "𝜓", "𝜒", "𝜃", "𝜏", "𝜂", "𝜁", "𝜎", "𝜌", "𝜇", "𝜆", "𝜅"]

def split(og_value: str, value: str) -> dict:
    started: bool = False
    ret: dict = {}
    sync_len: int = 0
    
    for i, ogs in enumerate(og_value):
        if ogs != "(" and not started:
            continue

        started = True

        if ogs not in wffs:
            continue

        depth_value: int = 0
        build: str = ""
        for s in value[i + sync_len:]:
            build += s

            if s in wffs and depth_value == 0:
                ret[ogs] = build
                sync_len += len(build) - 1
                break
            
            if s == "(":
                depth_value += 1
            elif s == ")":
                depth_value -= 1
            elif s not in wffs:
                continue
            
            if depth_value == 0:
                if ogs in ret:
                    if ret[ogs] != build:
                        print(f"CANNOT COMPUTE: WFF VALUES ARE INCONSISTANT\n> \"{ret[ogs]}\" != \"{build}\"")
                        print(ret)
                        raise "ERROR, READ ABOVE"
                ret[ogs] = build
                sync_len += len(build) - 1
                break
    return ret

def print_split(split: dict) -> None:
    for k, v in split.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    ret = split(og_theorem, to_split_theorem)
    print_split(ret)