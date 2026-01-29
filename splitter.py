import sys

theorem: str = sys.argv[1]
# theorem = "(¬ (¬ (((𝜒 → (𝜃 → (𝜓 → 𝜏))) → ¬ 𝜂) → (¬ 𝜓 → ¬ 𝜂)) → ¬ 𝜃) → ¬ 𝜑)"

operations = { "→": "wi", "¬": "wn" }
no_left = ["¬"]

def init_dict(d: dict):
    if hasattr(d, "operation") or hasattr(d, "left") or hasattr(d, "right"):
        raise f"DICT HAS ALREADY BEEN INITIALIZED: {d}"
        
    d["operation"] = ""
    d["left"] = {}
    d["right"] = {}

def create_value(d: dict):
    if d["operation"] in no_left:
        d["value"] = f"{d["operation"]} {d["right"]["value"]}"
    else:
        d["value"] = f"({d["left"]["value"]} {d["operation"]} {d["right"]["value"]})"

def split(value: str) -> dict:
    started: bool = False
    ret: dict = {}

    curr_dict: dict = ret
    curr_dict["root"] = {}
    init_dict(curr_dict)

    for s in value:
        if s != '(' and not started or s == ' ':
            continue

        started = True

        if s == '(':
            root_dict: dict = curr_dict
            curr_dict = curr_dict["left"]
            curr_dict["root"] = root_dict
            init_dict(curr_dict)
        elif s == ')':
            curr_dict = curr_dict["root"]
            create_value(curr_dict)

            if "operation" in curr_dict["root"]:
                while curr_dict["root"]["operation"] in no_left:
                    curr_dict = curr_dict["root"]
                    create_value(curr_dict)
        elif s in operations:
            root_dict: dict
            if s not in no_left:
                root_dict = curr_dict["root"]
            else:
                root_dict = curr_dict

            root_dict["operation"] = s

            curr_dict = root_dict["right"]
            curr_dict["root"] = root_dict
            init_dict(curr_dict)
            if s in no_left:
                root_dict["left"] = {}
        elif s != ' ':
            curr_dict["value"] = s
            
            if "operation" in curr_dict["root"]:
                while curr_dict["root"]["operation"] in no_left:
                    curr_dict = curr_dict["root"]
                    create_value(curr_dict)

    return ret

def print_solution(value: dict, depth_level: int = 0, already_output: list = []) -> str:
    ret: str = ""

    if value["left"] == {} and value["right"] == {}:
        return ""

    if value["left"] != {} and value["operation"] not in no_left:
        ret += print_solution(value["left"], depth_level + 1)
    if value["right"] != {}:
        ret += print_solution(value["right"], depth_level + 1)

    if value["value"] in already_output:
        return ""
    
    already_output.append(value["value"])
    
    if value["operation"] not in no_left:
        ret += f"wff {value["left"]["value"]}, "

    ret += f"wff {value["right"]["value"]}, {operations[value["operation"]]}\n"
    ret += f" > wff {value["value"]}\n\n"


    return ret
    
if __name__ == "__main__":
    spl = split(theorem)
    prt = print_solution(spl)
    print(prt)
