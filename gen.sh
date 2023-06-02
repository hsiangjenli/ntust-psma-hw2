IMAGE=https://hsiangjenli.github.io/hsiangjenli/static/image/ntust.png
pdoc graph_algo/graph_algo -o ./docs --favicon "$IMAGE" --logo "$IMAGE" --docformat "numpy"
python to_pdf.py