# Module: internal/ceres
> **Package**: `internal/ceres` | **Source**: `internal/ceres/cuda_sparse_cholesky.cc` (514 lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `CudssContext` | class | CUDA Cholesky 求解器上下文 |
| `CudaSparseCholesky<float>` | class | 使用 CUDA 的稀疏 Cholesky 分解器（float 类型） |
| `CudaSparseCholesky<double>` | class | 使用 CUDA 的稀疏 Cholesky 分解器（double 类型） |
| `LinearSolverTerminationType` | function | 线性求解器终止类型枚举函数 |
| `cholmod_sparse` | function | CHOLMOD 稀疏矩阵构造函数 |
| `cholmod_dense` | function | CHOLMOD 稠密矩阵构造函数 |
| `cholmod_factor` | function | CHOLMOD 因子矩阵构造函数 |
| `UnaryCostFunction` | class | 单参数成本函数测试类 |
| `BinaryCostFunction` | class | 双参数成本函数测试类 |
| `TernaryCostFunction` | class | 三参数成本函数测试类 |
| `Projective` | class | 投影几何测试类 |
| `Metric` | class | 度量几何测试类 |
| `VaryingResidualFunctor` | class | 可变残差函数测试类 |
| `Residual1Param` | class | 一参数残差函数测试类 |
| `Residual2Param` | class | 二参数残差函数测试类 |
| `Residual3Param` | class | 三参数残差函数测试类 |
| `Residual4Param` | class | 四参数残差函数测试类 |
| `Residual5Param` | class | 五参数残差函数测试类 |
| `Residual6Param` | class | 六参数残差函数测试类 |
| `Residual7Param` | class | 七参数残差函数测试类 |
| `Residual8Param` | class | 八参数残差函数测试类 |
| `Residual9Param` | class | 九参数残差函数测试类 |
| `Residual10Param` | class | 十参数残差函数测试类 |
| `CostFunction` | class | 成本函数接口类 |
| `EvaluationCallback` | class | 评估回调接口类 |
| `LossFunction` | class | 损失函数接口类 |
| `CRSMatrix` | class | CRS 格式稀疏矩阵类 |
| `Program` | class | 优化问题程序类 |
| `ResidualBlock` | class | 残差块类 |
| `ProblemImpl` | class | 问题实现类 |

---

## 模块概述

本模块是 Ceres Solver 的核心实现模块之一，主要负责提供稀疏线性代数求解器、成本函数、损失函数以及问题建模相关的底层功能。它作为 Ceres 的核心引擎，为上层优化算法提供数值求解支持。该模块依赖于底层线性代数库如 CUDA、SuiteSparse 等，同时也被 `ceres::Solver` 和 `ceres::Problem` 等高层模块所调用。

---

## 类参考

### `CudssContext`
> **Summary**: CUDA Cholesky 求解器上下文

**Type**: `class` | **Module**: `internal/ceres`

**Source**: `internal/ceres/cuda_sparse_cholesky.cc:193`

#### 字段

| 名称 | 类型 | 默认值 | 描述 |
|------|------|---------|-------------|
| `context` | `void*` | `nullptr` | CUDA Cholesky 上下文句柄 |

---

### `CudaSparseCholesky<float>`
> **Summary**: 使用 CUDA 的稀疏 Cholesky 分解器（float 类型）

**Type**: `class` | **Module**: `internal/ceres`

**Source**: `internal/ceres/cuda_sparse_cholesky.cc:505`

---

### `CudaSparseCholesky<double>`
> **Summary**: 使用 CUDA 的稀疏 Cholesky 分解器（double 类型）

**Type**: `class` | **Module**: `internal/ceres`

**Source**: `internal/ceres/cuda_sparse_cholesky.cc:506`

---

### `UnaryCostFunction`
> **Summary**: 单参数成本函数测试类

**Type**: `class` | **Module**: `internal/ceres`

**Source**: `internal/ceres/problem_test.cc:62`

---

### `BinaryCostFunction`
> **Summary**: 双参数成本函数测试类

**Type**: `class` | **Module**: `internal/ceres`

**Source**: `internal/ceres/problem_test.cc:80`

---

### `TernaryCostFunction`
> **Summary**: 三参数成本函数测试类

**Type**: `class` | **Module**: `internal/ceres`

**Source**: `internal/ceres/problem_test.cc:101`

---

### `Projective`
> **Summary**: 投影几何测试类

**Type**: `class` | **Module**: `internal/ceres`

**Source**: `internal/ceres/autodiff_test.cc:137`

---

### `Metric`
> **Summary**: 度量几何测试类

**Type