# **Practice of Social Media Analytics CS5128701**

This is a code written for the ***Practice of Social Media Analytics*** course.  

The code was written by [@李享紝 - Hsiang-Jen Li](https://github.com/hsiangjenli), but there is no guarantee that all algorithms are error-free. Therefore, users need to assume their own risk when using these code.

## **Project structure**

```yaml
.
├── ./README.md
├── ./by_cn.ipynb # 測試
├── ./by_deep_cn.ipynb # 測試
├── ./hw02.ipynb # 最終版
├── ./networkX.ipynb # networkX 直接使用套件
├── ./data
│   ├── ./data/sampleSubmission.csv
│   ├── ./data/test.csv
│   └── ./data/train.csv
├── ./docs # 文件檔
├── ./gen.sh # 建立文件檔的 shell script
└── ./graph_algo
    ├── ./graph_algo # 本次撰寫的演算法
        ├── ./graph_algo/graph_algo/base.py
        ├── ./graph_algo/graph_algo/graph.py
        ├── ./graph_algo/graph_algo/pipeline.py
        ├── ./graph_algo/graph_algo/score_func.py
        └── ./graph_algo/graph_algo/sparsification.py
```
## **Create documentation from source code**
```shell
IMAGE=https://hsiangjenli.github.io/hsiangjenli/static/image/ntust.png
pdoc graph_algo/graph_algo -o ./docs --favicon "$IMAGE" --logo "$IMAGE" --docformat "numpy"
```


