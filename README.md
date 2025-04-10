# experiment-of-retrieval
此项目用于传输每次实验结果
## 配置
- 使用模型：例如BGE
- 使用压缩方法：例如三值化text-model
- 使用数据集：例如coco-train
- 训练轮次：例如epoch：100
- 使用batch-size：例如batch-size：16
- 使用的学习率及调整算法：例如1e-6 余弦退火
- 实验运行命令：例如 python /root/autodl-tmp/nyh/tnClip/tmp.py
- 模型输出路径：例如 /root/autodl-tmp/nyh/my_saved_model
## 输出结果
- 将模型输出的log文件传入
- 将模型输出的plt文件传入

## 2025/4/10 BGE-VL-base+L2检索

### 配置

- 使用模型：BGE-VL-base
- 使用数据集：CIRCO-test
- 检索办法：使用faiss索引faiss.IndexFlatL2
- 实验运行命令：`python /root/autodl-tmp/ITR_bge/retrieval_CIRCO.py --method=“l2” --output_file=“/root/autodl-tmp/ITR_bge/results/predictions_test_bge_l2.json”`
- 结果输出路径：/root/autodl-tmp/ITR_bge/results/predictions_test_bge_l2.json

### 输出结果

Recall@5: 32.12
Recall@10: 38.5
Recall@25: 46.88
Recall@50: 52.12

mAP@5: 23.43
mAP@10: 23.38
mAP@25: 24.94
==mAP@50: 25.5== < 34.3 (paper claimed)

mAP@10 results for each semantic aspect:
Cardinality: 20.62
Addition: 24.57
Negation: 24.2
Direct Addressing: 23.96
Compare & Change: 21.03
Comparative Statement: 23.19
Statement with Conjunction: 22.79
Spatial Relations & Background: 25.36
Viewpoint: 20.44
