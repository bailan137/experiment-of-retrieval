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
- 实验运行命令：python /root/autodl-tmp/ITR_bge_l2/retrieval_CIRCO.py
- 结果输出路径：/root/autodl-tmp/ITR_bge_l2/results/predictions.json

### 输出结果

/root/autodl-tmp/ITR_bge_l2/results/predictions.json
