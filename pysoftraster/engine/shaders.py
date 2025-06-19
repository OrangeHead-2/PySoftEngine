import math

class ShaderBase:
    def vertex(self, vtx, uniforms):
        raise NotImplementedError

    def fragment(self, data, uniforms):
        raise NotImplementedError

class LambertShader(ShaderBase):
    def vertex(self, vtx, uniforms):
        mvp = uniforms['mvp']
        pos = mvp @ vtx['position']  # vtx['position'] is a 4-vector
        normal = vtx['normal']  # Assume already normalized
        return {'pos': pos, 'normal': normal, 'base_color': vtx.get('color', (1,1,1))}

    def fragment(self, data, uniforms):
        normal = data['normal']
        light = uniforms['light_dir']
        color = data['base_color']
        intensity = max(0, sum(n*l for n,l in zip(normal,light)))
        return tuple(int(255*c*intensity) for c in color)

class PhongShader(ShaderBase):
    def vertex(self, vtx, uniforms):
        mvp = uniforms['mvp']
        pos = mvp @ vtx['position']
        normal = vtx['normal']
        return {'pos': pos, 'normal': normal, 'color': vtx.get('color', (1,1,1))}

    def fragment(self, data, uniforms):
        normal = data['normal']
        color = data['color']
        light = uniforms['light_dir']
        view = uniforms['view_dir']
        diffuse = max(0, sum(n*l for n,l in zip(normal,light)))
        reflect = tuple(2*diffuse*n-l for n,l in zip(normal,light))
        spec = max(0, sum(r*v for r,v in zip(reflect,view)))**16
        return tuple(min(255, int(255*c*(diffuse+0.5*spec))) for c in color)

def as_matrix(matlist):
    class Mat:
        def __init__(self, m): self.m = m
        def __matmul__(self, v):  # v is list/tuple of 4
            return [sum(self.m[i][j]*v[j] for j in range(4)) for i in range(4)]
    return Mat(matlist)