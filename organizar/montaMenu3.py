import pprint

def list_to_tree(data):
    out = { 
        0: { 'id': 0, 'parent_id': 0, 'name': "Root node", 'sub': [] }
    }

    for p in data:
        out.setdefault(p['parent_id'], { 'sub': [] })
        out.setdefault(p['id'], { 'sub': [] })
        out[p['id']].update(p)
        out[p['parent_id']]['sub'].append(out[p['id']])

    return out[0]


data = [
    { 'id': 1, 'parent_id': 2, 'name': "Node1" },
    { 'id': 2, 'parent_id': 5, 'name': "Node2" },
    { 'id': 3, 'parent_id': 0, 'name': "Node3" },
    { 'id': 4, 'parent_id': 5, 'name': "Node4" },
    { 'id': 5, 'parent_id': 0, 'name': "Node5" },
    { 'id': 6, 'parent_id': 3, 'name': "Node6" },
    { 'id': 7, 'parent_id': 3, 'name': "Node7" },
    { 'id': 8, 'parent_id': 0, 'name': "Node8" },
    { 'id': 9, 'parent_id': 1, 'name': "Node9" }
]

tree = list_to_tree(data)
# pprint.pprint(tree)
print(tree)