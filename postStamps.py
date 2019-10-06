import random

def hex_color_to_rgb(red, green, blue):
    return int('%02x%02x%02x%02x' % (red*255,green*255,blue*255,255),16)

sel_node = nuke.selectedNodes()

for num, i in enumerate(sel_node):
    post_node = nuke.createNode("PostageStamp")
    post_node.setInput(0, i)

    otherPost_node = nuke.createNode("PostageStamp")
    otherPost_node.setInput(0, post_node)

    random.seed(num)
    random_r = random.random()

    random.seed(num + 1)
    random_g = random.random()

    random.seed(num + 2)
    random_b = random.random()

    post_node.knob("tile_color").setValue(hex_color_to_rgb(random_r,random_g,random_b))
    otherPost_node.knob("tile_color").setValue(hex_color_to_rgb(random_r,random_g,random_b))

