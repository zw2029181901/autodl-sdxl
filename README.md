# SDXL 生图

输入文字生成图片，支持三种画幅、负面提示词与随机种子。

AutoDL.Art：[SDXL-TextToImage](https://www.autodl.art/i/zw2029181901/autodl-sdxl/SDXL-TextToImage)。v1已提交审核，等待平台通过后开放创建实例。

源码仓库不包含模型权重。本次导出环境把模型、独立依赖和启动配置放在系统盘，使用之后保存就绪的镜像无需再次安装或下载模型。模型版本固定在 `app.json`。

镜像 `autodl-sdxl-20261111`，UUID `image-ab8145a6f9`，平台体积7.75GB，已就绪。社区审核及公开状态以平台当前状态为准。

镜像使用说明见 [IMAGE_README.md](IMAGE_README.md)，验收及保存记录见 [IMAGE_VALIDATION.json](IMAGE_VALIDATION.json)。

## 从源码另行安装

以下命令在AutoDL Linux实例执行。已使用保存镜像的用户直接打开6006即可。

```bash
cd /root
git clone https://github.com/zw2029181901/autodl-sdxl.git
cd /root/autodl-sdxl
bash install.sh
.venv/bin/python runtime/prefetch.py --project .
.venv/bin/python runtime/doctor.py --project . --models
bash start.sh
```

已在RTX3090 24GB完成1024×1024、20步HTTP生图验收；建议24GB显存、32GB内存起测，使用CPU offload。其他GPU未逐一实测。

模型约6.94GB，输出等预留空间建议12GB；基础框架和Python依赖另计。保存镜像只保存系统盘，数据盘不会随镜像分发；本次权重位于系统盘 `/root/autodl-active/models`。平台实际镜像体积与账号总容量须逐份核对。

许可：CreativeML Open RAIL++（权重）；Apache-2.0（Diffusers）。[模型项目](https://github.com/huggingface/diffusers)。本项目提供中文界面、运行配置与部署脚本，模型算法归原作者。许可文件随代码保留。
