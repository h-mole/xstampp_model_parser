import json
from py_ltl_parser import parse_xstampp_ltl


def test_parsing_ltl():
    ltl = "[] ((((controlAction==IncreasePower))->(((!((controlAction==IncreasePower)))U(((MyVar==Abnormal)))))))"
    # ltl = "[] (controlAction==IncreasePower) -> A U x"
    parsed = parse_xstampp_ltl(ltl)
    print(json.dumps(parsed.to_dict(), indent=2))
    print(parsed.unparse())

    ltl = "[] (((((ACE4==direct)&&(ACE3==direct)&&(ACE1==normal)&&(ACE2==normal)))->(!((controlAction==Providedisplacementandforcevariablesofthedrivingstick)))))"
    # ltl = "[] (controlAction==IncreasePower) -> A U x"
    parsed = parse_xstampp_ltl(ltl)
    print(json.dumps(parsed.to_dict(), indent=2))
    print(parsed.unparse())


