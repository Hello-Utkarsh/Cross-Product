class cross_product:
    
    def __init__(self, vec):
        self.vec = vec

    def __mul__(self, vec2):
        pro_list = []
        cap = ["i","j","k"]
        for i in range(len(self.vec)):
            a = i+1
            b = i+2
            if a>2:
                a=a-3
            if b>2:
                b=b-3
            pro_list.append(f"{self.vec[a]*vec2.vec[b]-self.vec[b]*vec2.vec[a]}{cap[i]}")
        return pro_list

vec1 = cross_product([3,2,-4])
vec2 = cross_product([2,-3,-6])
vec3 = vec1 * vec2
print(vec3)