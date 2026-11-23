import json
def validate_response(raw, schema):
    """Parse and validate a model's JSON reply against a {field: type} schema.

    Return the cleaned dict, or None if it cannot be trusted.
    """
    # pass
    try:
        d = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return None
    if not isinstance(d,dict):
        return
    
    c = {}

    for k,t in schema.items():
        if k not in d:
            return None
        v = d[k]

        if not isinstance(v,t) or (t is int and isinstance(v,bool)):
            return None
        c[k] = v 
    return c
