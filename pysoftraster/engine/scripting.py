class SceneNode:
    def __init__(self, id, mesh=None, transform=None, children=None):
        self.id = id
        self.mesh = mesh
        self.transform = transform if transform else [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        self.children = children if children else []
        self.visible = True

class Scene:
    def __init__(self):
        self.nodes = {}
        self.root = SceneNode('root')
        self.lights = []
        self.camera = None

    def add_node(self, node, parent_id='root'):
        self.nodes[node.id] = node
        parent = self.nodes.get(parent_id, self.root)
        parent.children.append(node)

    def add_light(self, light):
        self.lights.append(light)

    def set_camera(self, camera):
        self.camera = camera

    def apply_transforms(self, transforms):
        for node_id, mat in transforms.items():
            if node_id in self.nodes:
                self.nodes[node_id].transform = mat

    def render(self):
        # Real implementation would walk scene graph, apply transforms, feed to renderer.
        print("Rendering scene, nodes:", list(self.nodes.keys()))