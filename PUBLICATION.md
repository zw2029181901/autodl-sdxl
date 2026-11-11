# SDXL 生图 发布填写材料

| 字段 | 填写内容 |
|---|---|
| 显示名称 | SDXL 生图 |
| 仓库名/仅英文镜像名 | autodl-sdxl |
| GitHub账号 | zw2029181901 |
| 拟用项目链接 | https://github.com/zw2029181901/autodl-sdxl |
| AutoDL.Art账号 | 200211（金鳞） |
| 介绍 | 输入文字生成图片，支持三种画幅、负面提示词与随机种子。 |
| 服务端口 | 6006 |
| 启动命令 | bash /root/autodl-sdxl/start.sh |
| 模型容量 | 约6.94GB；模型及输出预留12GB，依赖另计 |
| 上游 | https://github.com/huggingface/diffusers |
| 许可 | CreativeML Open RAIL++（权重）；Apache-2.0（Diffusers） |

项目链接见上表。云镜像需先完成真实任务与新实例验收，再提交平台审核；源码已上传不等于云镜像已上线。

原创算法/论文：不勾选，上游模型归原作者。
原创代码：按平台定义如实提交中文界面、部署脚本等增量说明，不因新建自己的仓库就勾选整套模型代码原创。
收益以平台当前审核及结算规则为准；不承诺上架或收益。

本包是独立Gradio应用。发布社区镜像后，是否成为应用广场APP须走平台对应入口与审核；也不会自动变成由AutoDL部署维护的ComfyUI工作流API。
