import gradio as gr

from datas.load_datas import load_csv

with gr.Blocks() as demo:
    gr.Markdown("# データ解析ツール")
    with gr.Tab("データ読み込み"):
        input_data = gr.File(file_types=["csv"], type="file", label="読み込むCSVデータを入力")
        output_data = gr.DataFrame()
        examples = gr.Examples(
            examples=["input_datas/iris.csv"],
            inputs=[input_data],
            outputs=[output_data],
            fn=load_csv,
            cache_examples=True,
            run_on_click=True,
            api_name="load_csv",
        )
    with gr.Tab("データ変換"):
        output_data
    with gr.Tab("データ解析"):
        pass
    with gr.Tab("データ可視化"):
        pass
    # データ読み込み
    input_data.change(load_csv, inputs=[input_data], outputs=[output_data], api_name="load_csv2")
    # データ変換
    # データ解析
    # データ可視化

if __name__ == "__main__":
    demo.launch()
