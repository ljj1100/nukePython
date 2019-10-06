def shuffleLayer(node, layer):
    shuffleNode = nuke.nodes.Shuffle(label=layer, inputs=[node])
    shuffle_node['in'].setValue(layer)


def createNode(node):
    channel = node.channels()
    layers = list(set([c.split('.')[0] for c in channel]))
    layers.sort()

    for j in layers:
        export_name = "{0} ''.join(layers)"
        shuffleLayer(node, j)


createNode(nuke.selectedNodes()[0])