import gradio as gr

def arithmetic_calculator(question):
  """Evaluates a simple arithmetic expression and returns the result."""
  try:
    result = eval(question)
    return str(result)
  except (SyntaxError, NameError):
    return "Invalid arithmetic expression."

iface = gr.Interface(
  fn=arithmetic_calculator,
  inputs=[gr.Textbox(lines=1, placeholder="Enter an arithmetic question")],
  outputs="text",
  title="Basic Arithmetic Calculator",
  description="Enter a simple arithmetic question (e.g., '2 + 2' or '3 * 4') and get the answer.",
)

iface.launch()
