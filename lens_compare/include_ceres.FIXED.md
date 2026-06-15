# Module: include/ceres
> **Package**: `include/ceres` | **Source**: `include/ceres/loss_function.h` (432 lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `LossFunction` | class | 损失函数接口类 |
| `SoftLOneLoss` | class | 软 L1 损失函数 |
| `TolerantLoss` | class | 容忍损失函数 |
| `ComposedLoss` | class | 组合损失函数 |
| `LossFunctionWrapper` | class | 损失函数包装器 |
| `CostFunction` | class | 代价函数接口类 |
| `EvaluationCallback` | class | 评估回调接口类 |
| `Manifold` | class | 流形接口类 |
| `Solver` | class | 求解器接口类 |
| `CRSMatrix` | class | 压缩行存储矩阵 |
| `Preprocessor` | class | 预处理器类 |
| `ProblemImpl` | class | 问题实现类 |
| `ParameterBlock` | class | 参数块类 |
| `ResidualBlock` | class | 残差块类 |
| `EvaluateOptions` | class | 评估选项类 |
| `FirstOrderFunction` | class | 一阶函数接口类 |
| `GradientProblem` | class | 梯度问题类 |
| `EuclideanManifold` | class | 欧几里得流形类 |
| `SubsetManifold` | class | 子集流形类 |
| `QuaternionManifold` | class | 四元数流形类 |
| `EigenQuaternionManifold` | class | Eigen 四元数流形类 |
| `X` | class | X 轴旋转类 |
| `Y` | class | Y 轴旋转类 |
| `Z` | class | Z 轴旋转类 |
| `Even` | class | 偶数旋转类 |
| `Odd` | class | 奇数旋转类 |
| `ProperEuler` | class | 真欧拉角类 |
| `TaitBryan` | class | 泰特-布赖恩角类 |
| `Extrinsic` | class | 外部旋转类 |
| `Intrinsic` | class | 内部旋转类 |
| `EulerSystem` | class | 欧拉系统类 |
| `ExclusiveScanImpl` | class | 排除扫描实现类 |
| `ExclusiveScanT` | class | 排除扫描类型类 |
| `RemoveValueImpl` | class | 移除值实现类 |
| `RemoveValue` | class | 移除值类 |
| `IsEmptyOrAreAllEqual` | class | 空或全相等判断类 |
| `AreAnyJet` | class | 任意 Jet 类型判断类 |
| `UnderlyingScalar` | class | 基础标量类型类 |
| `Rank` | class | 秩类型类 |
| `CompatibleJetOperands` | class | 兼容 Jet 操作数类 |
| `PromotableJetOperands` | class | 可提升 Jet 操作数类 |
| `std::common_type<T, ceres::Jet<U, N>>` | class | Jet 类型通用类型类 |
| `std::common_type<ceres::Jet<T, N>, U>` | class | Jet 类型通用类型类 |
| `std::common_type<ceres::Jet<T, N>, ceres::Jet<U, N>>` | class | Jet 类型通用类型类 |
| `numeric_limits<ceres::Jet<T, N>>` | class | Jet 类型极限值类 |
| `NumTraits<ceres::Jet<T, N>>` | class | Jet 类型数值特性类 |
| `ScalarBinaryOpTraits<ceres::Jet<T, N>, T, BinaryOp>` | class | 标量二元操作特性类 |
| `ScalarBinaryOpTraits<T, ceres::Jet<T, N>, BinaryOp>` | class | 标量二元操作特性类 |
| `EIGEN_STRONG_INLINE` | function | EIGEN 强内联函数 |

---

## 模块概述

本模块是 Ceres Solver 的核心头文件集合，提供优化问题建模、求解和相关数学工具的接口。它定义了代价函数、损失函数、流形、求解器等关键组件的抽象接口和实现，支持非线性最小二乘优化问题的建模与求解。模块作为整个优化框架的基础层，负责定义问题结构、约束表达和求解策略，被上层应用模块调用以执行优化任务。其依赖于底层的线性代数库和数值计算组件。

---

## 类参考

### `LossFunction`
<!-- api: class | visibility: public | source: include/ceres/loss_function.h:86 -->

> **Summary**: 损失函数接口类，用于对残差进行加权处理，以提高鲁棒性。

**Type**: `<class>` | **Module**: `include/ceres`

**See Also**: `SoftLOneLoss`, `TolerantLoss`, `ComposedLoss`, `LossFunctionWrapper`

---

### `SoftLOneLoss`
<!-- api: class | visibility: public | source: include/ceres/loss_function.h:131 -->

> **Summary**: 软 L1 损失函数