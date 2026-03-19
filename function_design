def analyze_password(
    password,
    min_length=8,
    require_digit=True,
    require_upper=True,
    require_symbol=False,
    banned_words=None
):
    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']

    rules = []
    passed = 0
    missing_rules = []

    rules.append("min_length")
    if len(password) >= min_length:
        passed += 1
    else:
        missing_rules.append("min_length")

    if require_digit:
        rules.append("digit")
        if any(char.isdigit() for char in password):
            passed += 1
        else:
            missing_rules.append("digit")

    if require_upper:
        rules.append("upper")
        if any(char.isupper() for char in password):
            passed += 1
        else:
            missing_rules.append("upper")

    symbols = "!@#$%^&*()-_=+[]{};:,.?"
    if require_symbol:
        rules.append("symbol")
        if any(char in symbols for char in password):
            passed += 1
        else:
            missing_rules.append("symbol")

    rules.append("banned_word")
    if any(word.lower() in password.lower() for word in banned_words):
        missing_rules.append("banned_word")
    else:
        passed += 1

    total_rules = len(rules)
    score_percent = int((passed / total_rules) * 100)

    is_strong = passed == total_rules

    return is_strong, score_percent, missing_rules

result1 = analyze_password("Test1234")
print(result1)
print("Pouziti pouze pozicních argumentu je kratke, ale mene prehledne – není hned jasne, co ktery parametr znamena.\n")

result2 = analyze_password("Test1234", 10, require_symbol=True)
print(result2)
print("Kombinace pozicních a pojmenovanych argumentu zlepsuje citelnost – klicove parametry jsou jasne pojmenovane.\n")

result3 = analyze_password("Test1234", require_symbol=False)
print(result3)
print("Pouziti pojmenovaneho argumentu pro vypnutí pravidla je velmi citelne – hned je jasne, co se meni.\n")

result4 = analyze_password("Admin123", banned_words=["admin", "root"])
print(result4)
print("Pouziti vlastniho seznamu zakazanych slov je flexibilni – umoznuje prizpusobeni pravidel konkretnim potrebam.\n")

