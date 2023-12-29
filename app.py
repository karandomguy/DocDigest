import gradio as gr
from main import load_and_predict

def summarize_text(input_text):
    # Call your function from the other file
    result, audio_result = load_and_predict(input_text)
    return result, audio_result

iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(),
    outputs=["text", "audio"],
    live=True,
    title="DocDigest",
    description="DocDigest is a Python application designed to simplify the summarization of textual content by providing both written and auditory representations.",
    analytics_enabled=False,  # Optional: Set to True if you want to enable analytics
)

iface.launch()
