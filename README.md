# Benchmarking Code Generation Capabilities of Large Language Models for Data Science Workflows

This project benchmarks the ability of free-access LLMs (GPT-3.5, Gemini 1.5 Flash, Claude 3 Haiku) to generate correct, complete, and efficient code for typical data science tasks.

## Project Structure

- `prompts/` — Prompt files for each stage of the data science workflow
- `responses/` — Model outputs copied manually from ChatGPT, Gemini, and Claude
- `evaluation/` — Jupyter notebook to run and test generated code + results CSV
- `images/` — Placeholder for your pipeline diagram

## Steps to Run
1. Visit each LLM (ChatGPT, Gemini, Poe).
2. Paste prompts from `/prompts/` into each interface.
3. Copy model outputs into `/responses/{model_name}/`.
4. Open `codegen_benchmark_test.ipynb` and test each response.
5. Record outcomes in `results_template.csv`.

## Tools Used
- Google Colab
- pandas, scikit-learn, seaborn, matplotlib
- Manual analysis (no paid APIs, no programmatic API keys)

## Report
See the main PDF/Word report for methodology, results, and discussion.
