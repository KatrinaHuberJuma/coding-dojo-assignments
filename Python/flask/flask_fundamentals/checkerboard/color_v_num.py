def what_is_this(val):
    if val.isdigit():
        return {'num': int(val)}
    else:
        return {color: val}