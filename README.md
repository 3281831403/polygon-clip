# 多边形裁剪：Sutherland-Hodgman 与三角化

裁剪后的多边形在边界处多出尖刺、面积不对：裁剪没有逐边处理，交点按线段端点取，顺/逆时针没有统一，点在多边形内判定漏掉射线穿过顶点，面积用有向面积但没取绝对值，三角化把凹多边形当凸的扇形，退化边没有剔除，批量裁剪只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
geometry/__init__.py
geometry/polygon_clip.py
tests/test_polygon_clip.py
```

## 当前状态

`geometry/polygon_clip.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_polygon_clip.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 裁剪逐边处理
2. 交点按直线求交
3. 统一逆时针
4. 点在多边形内判定
5. 面积取绝对值
6. 三角化按扇形
7. 退化边剔除
8. 批量裁剪统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `geometry/polygon_clip.py`
后 15 条用例应全部通过。
