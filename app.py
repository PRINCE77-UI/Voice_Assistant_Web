import ast
import operator
import os

import pyjokes
import wikipedia
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# ---- Safe calculator (replaces eval) ----
OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Pow: operator.pow, ast.USub: operator.neg, ast.Mod: operator.mod,
}


def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        left, right = safe_eval(node.left), safe_eval(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ValueError("exponent too large")
        return OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](safe_eval(node.operand))
    raise ValueError("unsupported expression")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/wiki")
def wiki():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify(ok=False, text="What should I search on Wikipedia?")
    try:
        wikipedia.set_lang("en")
        return jsonify(ok=True, text=wikipedia.summary(q, sentences=2))
    except wikipedia.exceptions.DisambiguationError as e:
        return jsonify(ok=False, text=f"Multiple results found. Be more specific, for example: {e.options[0]}")
    except wikipedia.exceptions.PageError:
        return jsonify(ok=False, text=f"I couldn't find a Wikipedia article on {q}.")
    except Exception:
        return jsonify(ok=False, text="Something went wrong with the Wikipedia search.")


@app.route("/api/joke")
def joke():
    return jsonify(ok=True, text=pyjokes.get_joke(language="en", category="all"))


@app.route("/api/calc", methods=["POST"])
def calc():
    expr = (request.get_json(silent=True) or {}).get("expr", "")
    for a, b in [("multiplied by", "*"), ("divided by", "/"), ("plus", "+"),
                 ("minus", "-"), ("times", "*"), ("into", "*"), ("x", "*")]:
        expr = expr.replace(a, b)
    try:
        result = safe_eval(ast.parse(expr.strip(), mode="eval"))
        return jsonify(ok=True, text=f"The answer is {result}.")
    except Exception:
        return jsonify(ok=False, text="Sorry, I couldn't calculate that.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
