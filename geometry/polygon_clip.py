"""多边形裁剪：Sutherland-Hodgman 与三角化：待实现的核心模块。"""


def clip_polygon(subject, clip):
    """用凸裁剪多边形裁剪主体。"""
    raise NotImplementedError

def polygon_area(vertices):
    """鞋带公式求面积。"""
    raise NotImplementedError

def point_in_polygon(point, vertices):
    """射线法判定点是否在多边形内。"""
    raise NotImplementedError

def ensure_ccw(vertices):
    """统一为逆时针。"""
    raise NotImplementedError

def triangulate(vertices):
    """扇形三角化。"""
    raise NotImplementedError
