word_to_digit = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

valid_ops = {"add", "sub", "mul", "rem", "pow"}

def convert_word_number(word):
    number = ""
    i = 0
    while i < len(word):
        found = False
        for k in word_to_digit:
            if word[i:i+len(k)] == k:
                number += word_to_digit[k]
                i += len(k)
                found = True
                break
        if not found:
            return None  # invalid digit word
    return int(number) if number else None

def resolve_operand(token):
    if token.count('c') == 0:
        return None
    parts = token.split('c')
    digits = []
    for part in parts:
        digit = word_to_digit.get(part)
        if digit is None:
            return None
        digits.append(digit)
    return int("".join(digits))

def evaluate_expression(tokens):
    if not all(t in valid_ops or 'c' in t for t in tokens):
        return "expression evaluation stopped invalid words present"

    def get_value(token):
        return resolve_operand(token)

    try:
        if tokens[0] in valid_ops:
            if tokens[1] in valid_ops:  # Form: op1 op2 a b c
                op1, op2, a, b, c = tokens
                a_val = get_value(a)
                b_val = get_value(b)
                c_val = get_value(c)
                if None in (a_val, b_val, c_val):
                    return "expression evaluation stopped invalid words present"
                inner = apply_operation(op2, a_val, b_val)
                result = apply_operation(op1, inner, c_val)
                return result
            elif tokens[2] in valid_ops:  # Form: op1 a op2 b c
                op1, a, op2, b, c = tokens
                a_val = get_value(a)
                b_val = get_value(b)
                c_val = get_value(c)
                if None in (a_val, b_val, c_val):
                    return "expression evaluation stopped invalid words present"
                inner = apply_operation(op2, b_val, c_val)
                result = apply_operation(op1, a_val, inner)
                return result
            else:  # Simple: op a b
                if len(tokens) != 3:
                    return "expression is not complete or invalid"
                op, a, b = tokens
                a_val = get_value(a)
                b_val = get_value(b)
                if None in (a_val, b_val):
                    return "expression evaluation stopped invalid words present"
                return apply_operation(op, a_val, b_val)
        return "expression is not complete or invalid"
    except:
        return "expression is not complete or invalid"

def apply_operation(op, a, b):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "rem":
        return a % b
    elif op == "pow":
        return a ** b
    else:
        raise Exception("Unknown operation")

# ---------- INPUT/OUTPUT ----------
print("Enter Prabhu's expression:")
input_line = input().strip()
tokens = input_line.split()

result = evaluate_expression(tokens)
print("Output:")
print(result)
