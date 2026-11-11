import functools
from runtime.common import guarded, image_rgb, model_path, output_path, page_header, require_gpu, seed_generator


@functools.lru_cache(maxsize=1)
def pipeline():
    import torch
    from diffusers import StableDiffusionXLPipeline
    require_gpu()
    pipe = StableDiffusionXLPipeline.from_pretrained(model_path(), torch_dtype=torch.float16, variant="fp16", use_safetensors=True)
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_tiling()
    return pipe


@guarded
def generate(prompt, negative, shape, steps, guidance, seed):
    if not prompt.strip():
        raise ValueError("请输入画面描述")
    if len(prompt) > 2000 or len(negative) > 2000:
        raise ValueError("描述请限制在 2000 字符以内")
    width, height = {"方形": (1024, 1024), "横向": (1152, 768), "竖向": (768, 1152)}[shape]
    image = pipeline()(prompt=prompt, negative_prompt=negative, width=width, height=height,
                       num_inference_steps=int(steps), guidance_scale=float(guidance), generator=seed_generator(seed)).images[0]
    destination = output_path(".png")
    image.save(destination)
    return image, str(destination)


def build_ui():
    import gradio as gr
    with gr.Blocks(title="SDXL 生图") as ui:
        page_header()
        prompt = gr.Textbox(label="画面描述（英文效果更稳定）", value="A ceramic teapot on a wooden table, soft morning light, product photography", lines=3)
        negative = gr.Textbox(label="不希望出现的内容", value="blurry, low quality")
        shape = gr.Radio(["方形", "横向", "竖向"], value="方形", label="画幅")
        steps = gr.Slider(10, 40, value=25, step=1, label="步数")
        guidance = gr.Slider(1, 12, value=6, label="提示词强度")
        seed = gr.Number(value=42, precision=0, label="随机种子")
        button = gr.Button("生成图片", variant="primary")
        result = gr.Image(label="生成结果")
        download = gr.File(label="下载 PNG")
        button.click(generate, [prompt, negative, shape, steps, guidance, seed], [result, download], api_name="generate")
    return ui
