import sys

theorem: str = sys.argv[1]
# theorem = "(((𝜓 → 𝜓) → (¬ 𝜓 → ¬ ¬ ¬ 𝜑)) → 𝜓)"

operations = { "→": "wi" }

def init_dict(d: dict):
    d["operation"] = ""
    d["left"] = {}
    d["right"] = {}

def split(value: str) -> dict:
    started: bool = False
    ret: dict = {}

    curr_dict: dict = ret
    init_dict(curr_dict)

    for s in value:
        if s != '(' and not started:
            continue

        started = True

        if s == '(':
            root_dict: dict = curr_dict
            curr_dict = curr_dict["left"]
            curr_dict["root"] = root_dict
            init_dict(curr_dict)
        elif s == ')':
            curr_dict = curr_dict["root"]
            curr_dict["value"] = f"({curr_dict["left"]["value"]} {curr_dict["operation"]} {curr_dict["right"]["value"]})"
        elif s in operations:
            root_dict: dict = curr_dict["root"]

            root_dict["operation"] = s

            curr_dict = root_dict["right"]
            curr_dict["root"] = root_dict
            init_dict(curr_dict)
        elif s != ' ':
            if "value" in curr_dict:
                curr_dict["value"] += f" {s}"
            else:
                curr_dict["value"] = s

    return ret

def print_solution(value: dict, depth_level: int = 0, already_output: list = []) -> str:
    ret: str = ""

    if value["left"] == {} and value["right"] == {}:
        return ""

    if value["left"] != {}:
        ret += print_solution(value["left"], depth_level + 1)
    if value["right"] != {}:
        ret += print_solution(value["right"], depth_level + 1)

    if value["value"] in already_output:
        return ""
    
    already_output.append(value["value"])
    
    ret += f"wff {value["left"]["value"]}, wff {value["right"]["value"]}, {operations[value["operation"]]}\n"
    ret += f" > wff ({value["value"]})\n\n"


    return ret
    
if __name__ == "__main__":
    spl = split(theorem)
    prt = print_solution(spl)
    print(prt)
