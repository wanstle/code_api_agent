# Module: internal/ceres
> **Package**: `internal/ceres` | **Source**: `internal/ceres/cuda_sparse_cholesky.cc` (`514` lines)

---

<!-- MODULE-LEVEL: Quick Summary table listing ALL symbols in this module -->
## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `CudssContext` | class | CUDA稀疏Cholesky求解器上下文管理类 |
| `CudaSparseCholesky<float>` | class | CUDA稀疏Cholesky求解器的float模板特化实现 |
| `CudaSparseCholesky<double>` | class | CUDA稀疏Cholesky求解器的double模板特化实现 |
| `CuDSSMatrixBase` | class | CUDSS底层矩阵基类封装 |
| `CuDSSMatrixDense` | class | CUDSS密集矩阵封装 |
| `LinearSolverTerminationType` | enum | 线性求解器终止类型枚举 |
| `DenseIterativeRefiner` | class | 稠密迭代改进器 |
| `Evaluator` | class | 求值器接口类 |
| `LineSearchFunction` | class | 线搜索函数接口类 |
| `Summary` | class | 线搜索摘要信息类 |
| `UnaryCostFunction` | class | 一元代价函数类 |
| `BinaryCostFunction` | class | 二元代价函数类 |
| `TernaryCostFunction` | class | 三元代价函数类 |
| `Projective` | class | 投影代价函数类 |
| `Metric` | class | 度量代价函数类 |
| `VaryingResidualFunctor` | class | 可变残差函数对象 |
| `CostFunction` | class | 代价函数基类 |
| `EvaluationCallback` | class | 评估回调接口类 |
| `LossFunction` | class | 损失函数基类 |
| `CRSMatrix` | class | CRS稀疏矩阵表示类 |
| `Program` | class | 优化问题程序结构类 |
| `ResidualBlock` | class | 残差块类 |

---

## 模块概述

本模块是Ceres Solver中用于实现高性能线性求解的底层模块，主要负责提供基于CUDA加速的稀疏Cholesky分解算法，以支持大规模优化问题的快速求解。该模块通过封装CUDSS库接口，实现了对稀疏矩阵的高效处理能力，特别适用于需要频繁求解线性系统的优化场景。模块内部还包含多种求解器实现，如CPU端的密集Cholesky求解器和CUDA端的稀疏Cholesky求解器，为不同硬件环境下的优化任务提供灵活选择。此外，模块还提供了线搜索、代价函数、评估回调等辅助功能，作为整个优化流程中的关键组件。

---

## 类参考

### `CudssContext`
<!-- api: class | visibility: public | source: internal/ceres/cuda_sparse_cholesky.cc:193 -->

> **Summary**: CUDA稀疏Cholesky求解器上下文管理类

**Type**: `class` | **Module**: `internal/ceres`

**See Also**: `CudaSparseCholesky<float>`, `CudaSparseCholesky<double>`

---

### `CudaSparseCholesky<float>`
<!-- api: class | visibility: public | source: internal/ceres/cuda_sparse_cholesky.cc:505 -->

> **Summary**: CUDA稀疏Cholesky求解器的float模板特化实现

**Type**: `class` | **Module**: `internal/ceres`

**See Also**: `CudaSparseCholesky<double>`, `CudssContext`

---

### `CudaSparseCholesky<double>`
<!-- api: class | visibility: public | source: internal/ceres/cuda_sparse_cholesky.cc:506 -->

> **Summary**: CUDA稀疏Cholesky求解器的double模板特化实现

**Type**: `class` | **Module**: `internal/ceres`

**See Also**: `CudaSparseCholesky<float>`, `CudssContext`

---

### `CuDSSMatrixBase`
<!-- api: class | visibility: public | source: internal/ceres/cuda_sparse_cholesky.cc:110 -->

> **Summary**: CUDSS底层矩阵基类封装

**Type**: `class` | **Module**: `internal/ceres`

**See Also**: `CuDSSMatrixDense`

---

### `CuDSSMatrixDense`
<!-- api: class | visibility: public | source: internal/ceres/cuda_sparse_cholesky.cc:173 -->

> **Summary**: CUDSS密集矩阵封装

**Type**: `class` | **Module**: `internal/ceres`

**See Also**: `CuDSSMatrixBase`

---

### `LinearSolverTerminationType`
<!-- api: enum | visibility: public | source: internal/ceres/dense_cholesky.cc:139 -->

> **Summary**: 线性求解器终止类型枚举

**Type**: `enum` | **Module**: `internal/ceres`

**See Also**: `DenseCholesky`, `EigenDenseCholesky`

---

### `DenseIterativeRefiner`
<!-- api: class | visibility: public | source: internal/ceres/dense_cholesky.h:170 -->

> **Summary**: 稠密迭代改进器