import numpy as np
import pandas as pd
import gradio as gr

with gr.Blocks() as demo:
    # layouts
    gr.Markdown("# sample demo.")

    with gr.Tab("Flip Load"):
        df_input = gr.File(
            label="CSVファイルを選択してください",
            file_types=["text"] # csvはなさそう
        )
        with gr.Column(visible=False) as df_send_col:
            df_output = gr.Dataframe()
            df_button_send = gr.Button('Send')
        with gr.Column(visible=False) as df_result_col:
            df_result = gr.Dataframe()

    with gr.Tab("Flip Text"):
        text_input = gr.Textbox()
        text_output = gr.Textbox()
        text_button = gr.Button("Flip")
    
    with gr.Tab("Flip Image"):
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("Flip")

    # functions
    def flip_text(x):
        return x[::-1]

    def flip_image(x):
        return np.fliplr(x)

    def load_csv(file):
        dataframe = pd.read_csv(file.name)  # CSVファイルをPandasのDataFrameとして読み込む
        return [
            dataframe,
            gr.update(visible=True)
        ]
    
    def send_csv(df):
        return [
            df,
            gr.update(visible=True)
        ]

    # events
    df_input.change(load_csv, inputs=df_input, outputs=[df_output, df_send_col])
    df_button_send.click(send_csv, inputs=df_output, outputs=[df_result, df_result_col])

    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)

# gr.Interface(
#     # fn=greet, 
#     # inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
#     # outputs="text",
#     examples=examples,
#     # allow_flagging='never', # フラグ機能削除
# )

demo.launch(
    server_name = "0.0.0.0", 
    server_port=7860, 
    # share=True # share=Trueにすることで発行されるURLにより.gradio.live経由で他者にも共有できる
)
