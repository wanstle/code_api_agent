# Module: examples
> **Package**: `examples` | **Source**: `examples/libmv_bundle_adjuster.cc` (858 lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `EuclideanCamera` | class | 欧几里得相机模型类 |
| `EuclideanPoint` | class | 欧几里得点模型类 |
| `Marker` | class | 标记点类 |
| `EndianAwareFileReader` | class | 字节序感知文件读取器 |
| `OpenCVReprojectionError` | class | OpenCV 重投影误差函数 |
| `NISTProblem` | class | NIST 问题类 |
| `Nelson` | class | Nelson 函数类 |
| `CostFunction` | function | 成本函数 |
| `PGMImage` | class | PGM 图像类 |
| `Real` | function | 实数函数 |
| `EstimateHomographyOptions` | class | 同态估计选项类 |
| `Homography2DNormalizedParameterization` | class | 2D 归一化参数化同态 |
| `HomographySymmetricGeometricCostFunctor` | class | 对称几何同态代价函数 |
| `TerminationCheckingCallback` | class | 终止检查回调类 |
| `F1` | class | Powell 函数 F1 |
| `F2` | class | Powell 函数 F2 |
| `F3` | class | Powell 函数 F3 |
| `F4` | class | Powell 函数 F4 |
| `OdometryConstraint` | class | 里程计约束类 |
| `RangeConstraint` | class | 距离约束类 |
| `FieldsOfExpertsCost` | class | 专家领域代价函数 |
| `FieldsOfExpertsLoss` | class | 专家领域损失函数 |
| `FieldsOfExperts` | class | 专家领域模型 |
| `PointToLineSegmentContourCostFunction` | class | 点到线段轮廓代价函数 |
| `EuclideanDistanceFunctor` | class | 欧几里得距离函数 |

---

## 模块概述

本模块是 Ceres Solver 的示例程序集合，用于展示如何使用 Ceres 进行各种优化任务。它包含多个独立的示例程序，涵盖了从基础的数学优化到复杂的视觉重建问题。这些示例不仅演示了 Ceres 的核心功能，还展示了其在实际应用中的使用方式。模块中的类和函数通常作为优化问题的定义或辅助工具，被主优化器调用。该模块不依赖于其他模块，而是作为 Ceres 的外部应用示例存在。

---

## 类参考

### `EuclideanCamera`
> **Summary**: 欧几里得相机模型类

**Type**: `class` | **Module**: `examples`  
**Source**: `examples/libmv_bundle_adjuster.cc:143`

#### 构造方法

```cpp
EuclideanCamera()
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| 无 |  | 无 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `EuclideanCamera()` | `void` | 默认构造函数 |
| `EuclideanCamera(const EuclideanCamera& other)` | `void` | 拷贝构造函数 |

---

### `EuclideanPoint`
> **Summary**: 欧几里得点模型类

**Type**: `class` | **Module**: `examples`  
**Source**: `examples/libmv_bundle_adjuster.cc:156`

#### 构造方法

```cpp
EuclideanPoint()
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| 无 |  | 无 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `EuclideanPoint()` | `void` | 默认构造函数 |
| `EuclideanPoint(const EuclideanPoint& other)` | `void` | 拷贝构造函数 |

---

### `Marker`
> **Summary**: 标记点类

**Type**: `class` | **Module**: `examples`  
**Source**: `examples/libmv_bundle_adjuster.cc:168`

#### 构造方法

```cpp
Marker()
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| 无 |  | 无 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `Marker()` | `void` | 默认构造函数 |
| `Marker(const Marker& other)` | `void` | 拷贝构造函数 |

---

### `EndianAwareFileReader`
> **Summary**: 字节序感知文件读取器

**Type**: `class` | **Module**: `examples`  
**Source**: `examples/libmv_bundle_adjuster.cc:269`

#### 构造方法

```cpp
EndianAwareFileReader()
```

| 参数 | 类型 | 描述 |
|-----------|------|-------------|
| 无 |  | 无 |

#### 方法

| 方法 | 返回值 | 描述 |
|--------|---------|-------------|
| `EndianAwareFileReader()` | `void` | 默认构造函数 |
| `EndianAwareFileReader(const EndianAwareFileReader& other)` | `void` | 拷贝构造函数 |

---

### `OpenCVReprojectionError`
> **Summary**: OpenCV 重投影误差函数

**