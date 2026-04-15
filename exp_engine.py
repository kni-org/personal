import ast
import operator as op

ops = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.BitAnd: op.and_,
    ast.BitOr: op.or_,
    ast.BitXor: op.xor,
    ast.LShift: op.lshift,
    ast.RShift: op.rshift
}

cmp_ops = {
    ast.Eq: op.eq,
    ast.NotEq: op.ne,
    ast.Lt: op.lt,
    ast.LtE: op.le,
    ast.Gt: op.gt,
    ast.GtE: op.ge
}

bool_ops = {
    ast.And: all,
    ast.Or: any
}

unary_ops = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
    ast.Not: op.not_,
    ast.Invert: op.invert
}

def safe_eval(expr, variables):
    def eval_(node):
        if isinstance(node, ast.Constant):
            return node.value

        elif isinstance(node, ast.Name):
            if node.id in variables:
                return variables[node.id]
            raise Exception("Undefined variable")

        elif isinstance(node, ast.BinOp):
            return ops[type(node.op)](eval_(node.left), eval_(node.right))

        elif isinstance(node, ast.UnaryOp):
            return unary_ops[type(node.op)](eval_(node.operand))

        elif isinstance(node, ast.BoolOp):
            values = [eval_(v) for v in node.values]
            return bool_ops[type(node.op)](values)

        elif isinstance(node, ast.Compare):
            left = eval_(node.left)
            for op_, comp in zip(node.ops, node.comparators):
                right = eval_(comp)
                if not cmp_ops[type(op_)](left, right):
                    return False
                left = right
            return True

        elif isinstance(node, ast.Expression):
            return eval_(node.body)

        else:
            raise Exception("Invalid expression")

    tree = ast.parse(expr, mode='eval')
    return eval_(tree.body)
