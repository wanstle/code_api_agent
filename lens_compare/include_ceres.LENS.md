# Module: include/ceres
> **Package**: `include/ceres` | **Source**: `include/ceres/loss_function.h` (432 lines)

---

## 快速概览

| 符号 | 类型 | 概述 |
|--------|------|---------|
| `LossFunction` | class | 损失函数接口类，用于对残差进行加权处理 |
| `SoftLOneLoss` | class | 软 L1 损失函数，用于鲁棒优化 |
| `TolerantLoss` | class | 容忍损失函数，适用于异常值处理 |
| `ComposedLoss` | class | 复合损失函数，组合多个损失函数 |
| `LossFunctionWrapper` | class | 损失函数包装器，用于封装自定义损失函数 |
| `CostFunction` | class | 代价函数接口类，定义残差计算逻辑 |
| `EvaluationCallback` | class | 评估回调接口类，用于在评估过程中插入自定义逻辑 |
| `LossFunction` | class | 损失函数接口类，用于对残差进行加权处理 |
| `Manifold` | class | 流形接口类，定义参数空间的几何结构 |
| `Solver` | class | 求解器接口类，提供优化问题的求解方法 |
| `CRSMatrix` | class | 压缩行存储矩阵，用于表示稀疏矩阵 |
| `Preprocessor` | class | 预处理器，用于优化问题的预处理 |
| `ProblemImpl` | class | 问题实现类，内部管理问题结构 |
| `ParameterBlock` | class | 参数块类，表示优化变量 |
| `ResidualBlock` | class | 残差块类，表示一个残差项 |
| `EvaluateOptions` | class | 评估选项类，控制评估行为 |
| `FirstOrderFunction` | class | 一阶函数接口类，用于梯度问题 |
| `GradientProblem` | class | 梯度问题类，用于定义梯度优化问题 |
| `EuclideanManifold` | class | 欧几里得流形，表示参数空间为欧几里得空间 |
| `SubsetManifold` | class | 子集流形，表示参数空间的子集 |
| `QuaternionManifold` | class | 四元数流形，用于表示旋转参数 |
| `EigenQuaternionManifold` | class | Eigen 四元数流形，基于 Eigen 实现的四元数流形 |
| `X` | class | X 轴旋转角度定义 |
| `Y` | class | Y 轴旋转角度定义 |
| `Z` | class | Z 轴旋转角度定义 |
| `Even` | class | 偶数旋转顺序定义 |
| `Odd` | class | 奇数旋转顺序定义 |
| `ProperEuler` | class | 真欧拉角定义 |
| `TaitBryan` | class | 泰特-布兰角度定义 |
| `Extrinsic` | class | 外部旋转定义 |
| `Intrinsic` | class | 内部旋转定义 |
| `EulerSystem` | class | 欧拉角系统定义 |
| `ExclusiveScanImpl` | class | 编译期前缀扫描实现 |
| `ExclusiveScanT` | class | 编译期前缀扫描类型 |
| `RemoveValueImpl` | class | 编译期移除值实现 |
| `RemoveValue` | class | 编译期移除值 |
| `IsEmptyOrAreAllEqual` | class | 编译期判断是否为空或所有元素相等 |
| `AreAnyJet` | class | 判断是否包含 Jet 类型 |
| `UnderlyingScalar` | class | 获取 Jet 类型的底层标量类型 |
| `Rank` | class | 获取 Jet 类型的秩 |
| `CompatibleJetOperands` | class | Jet 操作数兼容性判断 |
| `PromotableJetOperands` | class | Jet 操作数可提升性判断 |
| `std::common_type<T, ceres::Jet<U, N>>` | class | 标准类型特征，用于类型推导 |
| `std::common_type<ceres::Jet<T, N>, U>` | class | 标准类型特征，用于类型推导 |
| `std::common_type<ceres::Jet<T, N>, ceres::Jet<U, N>>` | class | 标准类型特征，用于类型推导 |
| `numeric_limits<ceres::Jet<T, N>>` | class | Jet 类型的数值极限特征 |
| `NumTraits<ceres::Jet<T, N>>` | class | Jet 类型的数值特征 |
| `ScalarBinaryOpTraits<ceres::Jet<T, N>, T, BinaryOp>` | class | 标量二元运算符特征 |
| `ScalarBinaryOpTraits<T, ceres::Jet<T, N>, BinaryOp>` | class | 标量二元运算符特征 |

---

## 模块概述

本模块是 Ceres Solver 的核心接口层，定义了优化问题建模所需的基础抽象。它为用户提供了构建和求解非线性最小二乘问题的接口，包括代价函数、损失函数、参数块、残差块等核心概念。模块通过定义清晰的接口和抽象类，使得用户可以灵活地组合不同的优化组件，实现复杂的优化任务。该模块作为 Ceres 的核心层，被