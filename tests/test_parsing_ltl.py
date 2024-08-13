from xstampp_model_parser import parse_ltl


def test_parsing_ltl():
    ltl = "[] ((((controlAction==IncreasePower))->(((!((controlAction==IncreasePower)))U(((MyVar==Abnormal)))))))"
    # ltl = "[] (controlAction==IncreasePower) -> A U x"
    parsed = parse_ltl(ltl)
    print(parsed.to_dict())
    print(parsed.unparse())
