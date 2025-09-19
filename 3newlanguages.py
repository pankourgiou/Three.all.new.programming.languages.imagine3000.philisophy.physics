import sys

# --------------------------
# Shared Utilities
# --------------------------

def eval_condition(cond: str) -> bool:
    """Very simple condition evaluator (for demo only)."""
    cond = cond.strip().lower()
    return cond in ["true", "yes", "1", "certain"]

# --------------------------
# Language Implementations
# --------------------------

def imagine3000(code):
    """
    .imagine3000 - Surreal creative programming
    Commands: print, if, loop, try/catch
    """
    tokens = code.strip().split()
    if not tokens:
        return "💭 empty imagination"

    if tokens[0] == "print":
        return f"✨ {code[6:]}"
    elif tokens[0] == "if":
        # Syntax: if <condition> then <output> else <output>
        parts = code[3:].split("then")
        if len(parts) < 2:
            return "Usage: if <cond> then <yes> else <no>"
        cond, rest = parts
        cond_val = eval_condition(cond)
        if "else" in rest:
            yes, no = rest.split("else", 1)
        else:
            yes, no = rest, ""
        return f"💡 {yes.strip()}" if cond_val else f"🌙 {no.strip()}"
    elif tokens[0] == "loop":
        try:
            n = int(tokens[1])
            body = code.split(maxsplit=2)[2]
            return "\n".join([f"🔁 {body}" for _ in range(n)])
        except:
            return "Usage: loop <n> <action>"
    elif tokens[0] == "try":
        if "catch" in code:
            idea, fallback = code[4:].split("catch", 1)
            if "fail" in idea.lower():
                return f"🚑 fallback: {fallback.strip()}"
            else:
                return f"🚀 succeeded: {idea.strip()}"
        else:
            return "Usage: try <idea> catch <fallback>"
    else:
        return f"Unknown .imagine3000 command: {tokens[0]}"

def philosophy(code):
    """
    .philosophy - Reflective abstract programming
    Commands: print, if, loop, try/catch
    """
    tokens = code.strip().split()
    if not tokens:
        return "🤔 silence"

    if tokens[0] == "print":
        return f"📜 {code[6:]}"
    elif tokens[0] == "if":
        parts = code[3:].split("then")
        if len(parts) < 2:
            return "Usage: if <cond> then <yes> else <no>"
        cond, rest = parts
        cond_val = eval_condition(cond)
        if "else" in rest:
            yes, no = rest.split("else", 1)
        else:
            yes, no = rest, ""
        return f"⚖️ Thesis: {yes.strip()}" if cond_val else f"🌀 Antithesis: {no.strip()}"
    elif tokens[0] == "loop":
        try:
            n = int(tokens[1])
            body = code.split(maxsplit=2)[2]
            return "\n".join([f"♻️ Reflect: {body}" for _ in range(n)])
        except:
            return "Usage: loop <n> <action>"
    elif tokens[0] == "try":
        if "catch" in code:
            thesis, antithesis = code[4:].split("catch", 1)
            if "paradox" in thesis.lower():
                return f"🔄 Synthesis: {antithesis.strip()}"
            else:
                return f"🧠 Reasoning holds: {thesis.strip()}"
        else:
            return "Usage: try <thesis> catch <antithesis>"
    else:
        return f"Unknown .philosophy command: {tokens[0]}"

def physics(code):
    """
    .physics - Scientific simulation programming
    Commands: print, if, loop, try/catch
    """
    tokens = code.strip().split()
    if not tokens:
        return "⚛️ no experiment"

    if tokens[0] == "print":
        return f"🔬 {code[6:]}"
    elif tokens[0] == "if":
        parts = code[3:].split("then")
        if len(parts) < 2:
            return "Usage: if <cond> then <yes> else <no>"
        cond, rest = parts
        cond_val = eval_condition(cond)
        if "else" in rest:
            yes, no = rest.split("else", 1)
        else:
            yes, no = rest, ""
        return f"✅ Law holds: {yes.strip()}" if cond_val else f"❌ Rejected: {no.strip()}"
    elif tokens[0] == "loop":
        try:
            n = int(tokens[1])
            body = code.split(maxsplit=2)[2]
            return "\n".join([f"🔁 Sim step: {body}" for _ in range(n)])
        except:
            return "Usage: loop <n> <action>"
    elif tokens[0] == "try":
        if "catch" in code:
            experiment, fallback = code[4:].split("catch", 1)
            if "error" in experiment.lower():
                return f"🧯 Using fallback law: {fallback.strip()}"
            else:
                return f"⚡ Experiment succeeded: {experiment.strip()}"
        else:
            return "Usage: try <experiment> catch <fallback>"
    else:
        return f"Unknown .physics command: {tokens[0]}"

# --------------------------
# REPL
# --------------------------

LANGUAGES = {
    ".imagine3000": imagine3000,
    ".philosophy": philosophy,
    ".physics": physics
}

HELP_TEXT = """
AI Programming REPL
Available languages: .imagine3000, .philosophy, .physics
Common commands:
  print <text>
  if <condition> then <yes> else <no>
  loop <n> <action>
  try <expr> catch <fallback>

Type 'examples' for usage.
"""

EXAMPLES_TEXT = """
Examples:

.imagine3000 print rainbow code
.imagine3000 if true then dream big else stay small
.imagine3000 loop 3 paint stars
.imagine3000 try flying machine catch parachute

.philosophy print "I think therefore I am"
.philosophy if false then existence else illusion
.philosophy loop 2 meditate
.philosophy try paradox catch synthesis

.physics print gravity detected
.physics if true then stable orbit else chaos
.physics loop 3 simulate particle
.physics try experiment catch error law
"""

def repl():
    print("Welcome to the AI Programming REPL! Type 'help' for instructions.\n")
    while True:
        try:
            user_input = input(">> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            if user_input.lower() == "help":
                print(HELP_TEXT)
                continue
            if user_input.lower() == "examples":
                print(EXAMPLES_TEXT)
                continue

            prefix = user_input.split(maxsplit=1)[0]
            if prefix in LANGUAGES:
                code = user_input[len(prefix):].strip()
                output = LANGUAGES[prefix](code)
                print(output)
            else:
                print("Unknown language prefix. Type 'help' for instructions.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
