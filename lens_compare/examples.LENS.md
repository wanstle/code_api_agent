# Module: examples
> **Package**: `examples` | **Source**: `examples/libmv_bundle_adjuster.cc` (858 lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `EuclideanCamera` | class | 欧式相机模型类 |
| `EuclideanPoint` | class | 欧式点模型类 |
| `Marker` | class | 标记点类 |
| `EndianAwareFileReader` | class | 字节序感知文件读取器 |
| `OpenCVReprojectionError` | class | OpenCV重投影误差代价函数 |
| `NISTProblem` | class | NIST问题类 |
| `Nelson` | class | Nelson问题类 |
| `CostFunction` | function | 代价函数 |
| `PGMImage` | class | PGM图像类 |
| `Real` | function | 实数类型转换函数 |
| `EstimateHomographyOptions` | class | 单应性估计选项类 |
| `Homography2DNormalizedParameterization` | class | 2D归一化参数化单应性类 |
| `HomographySymmetricGeometricCostFunctor` | class | 对称几何单应性代价函数 |
| `TerminationCheckingCallback` | class | 终止检查回调类 |
| `F1` | class | Powell函数F1 |
| `F2` | class | Powell函数F2 |
| `F3` | class | Powell函数F3 |
| `F4` | class | Powell函数F4 |
| `OdometryConstraint` | class | 里程计约束类 |
| `RangeConstraint` | class | 距离约束类 |
| `FieldsOfExpertsCost` | class | 专家领域代价函数类 |
| `FieldsOfExpertsLoss` | class | 专家领域损失函数类 |
| `FieldsOfExperts` | class | 专家领域模型类 |
| `PointToLineSegmentContourCostFunction` | class | 点到线段轮廓代价函数 |
| `EuclideanDistanceFunctor` | class | 欧式距离函数器 |

---

## 模块概述

本模块是 Ceres Solver 的使用示例集合，展示了如何在多种实际问题中应用优化框架进行建模与求解。这些示例涵盖了从视觉 Bundle Adjustment 到非线性最小二乘优化等多个领域，体现了 Ceres 核心组件（如 `CostFunction`、`Problem`、`Solver`）的组合使用方式。每个示例通过具体问题背景，演示了如何定义代价函数、构建优化问题、设置求解器参数并获取优化结果。此外，示例中还涉及数据读取、参数初始化及结果输出的具体实现方式，帮助开发者理解如何将 Ceres 应用于特定领域问题。

---

## 类参考

### `EuclideanCamera`
> **Summary**: 欧式相机模型类，用于表示相机参数和投影模型。

**Type**: `class` | **Module**: `examples`

**Source**: `examples/libmv_bundle_adjuster.cc:143`

#### 字段

| 名称 | 类型 | 默认值 | 描述 |
|------|------|---------|-------------|
| `camera_id` | `int` | `0` | 相机唯一标识符 |
| `rotation` | `std::vector<double>` | `[]` | 相机旋转参数 |
| `translation` | `std::vector<double>` | `[]` | 相机平移参数 |

#### 构造方法

```cpp
EuclideanCamera(int camera_id, const std::vector<double>& rotation, const std::vector<double>& translation)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `camera_id` | `int` | 相机唯一标识符 |
| `rotation` | `std::vector<double>` | 相机旋转参数 |
| `translation` | `std::vector<double>` | 相机平移参数 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `project(const std::vector<double>& point)` | `std::vector<double>` | 将3D点投影到图像平面 |

---

### `EuclideanPoint`
> **Summary**: 欧式点模型类，用于表示三维空间中的点。

**Type**: `class` | **Module**: `examples`

**Source**: `examples/libmv_bundle_adjuster.cc:156`

#### 字段

| 名称 | 类型 | 默认值 | 描述 |
|------|------|---------|-------------|
| `point_id` | `int` | `0` | 点唯一标识符 |
| `coordinates` | `std::vector<double>` | `[]` | 三维坐标 |

#### 构造方法

```cpp
EuclideanPoint(int point_id, const std::vector<double>& coordinates)
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| `point_id` | `int` | 点唯一标识符 |
| `coordinates` | `std::vector<double>` | 三维坐标 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `get_coordinates()` | `std::vector<double>` | 获取点坐标 |

---

### `Marker`
> **Summary**: 标记点类，用于表示图像中的标记点。

**Type**: `class` | **Module**: `examples`

**Source**: `examples/libmv_bundle_adjuster.cc:168`

####